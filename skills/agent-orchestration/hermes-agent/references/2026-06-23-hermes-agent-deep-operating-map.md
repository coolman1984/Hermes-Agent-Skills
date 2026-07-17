# Hermes Agent Deep Operating Map — 2026-06-23

Purpose: durable notes from Mohamed's request to understand Hermes Agent deeply, update to latest GitHub main, inspect the codebase, and capture practical secrets/lessons in the `hermes-agent` skill.

## Verification snapshot

Commands run:

```bash
cd /root/.hermes/hermes-agent
git fetch --all --tags --prune
git pull --ff-only
export UV_LINK_MODE=copy
/root/.local/bin/uv pip install --python /root/.hermes/hermes-agent/venv/bin/python -e .
hermes --version
hermes doctor
hermes tools list
```

Observed state after update:

- Local checkout fast-forwarded to `origin/main` at `af7b7f632`.
- `hermes --version` reports `Hermes Agent v0.17.0 (2026.6.19) · upstream af7b7f63`.
- Latest pulled commit: `feat(agent): expose coding-context project facts as structured data + project.facts RPC (#51259)`.
- Editable reinstall succeeded with `UV_LINK_MODE=copy` in the repo venv.
- `hermes doctor` showed Python, config version, version files, API connectivity, memory, sessions, and core tool availability healthy.
- Expected environment warnings remain: no systemd in PRoot, some optional tools missing, Nous/xAI/MiniMax OAuth not logged in, WhatsApp bridge npm vulnerabilities.

## Mental model

Hermes is a small operating system around an LLM, not a single chatbot loop.

Core layers:

1. **Identity and config** — `SOUL.md`, `config.yaml`, `.env`, profile overrides.
2. **Prompt assembly** — `agent/prompt_builder.py` loads identity, memory snapshots, context files, skills, project rules.
3. **Agent loop** — `run_agent.py` / `agent/conversation_loop.py` run repeated model calls until final text or max iterations.
4. **Tool schema and dispatch** — `model_tools.py`, `tools/registry.py`, `toolsets.py`, and runtime-owned tools route calls.
5. **State** — `hermes_state.py` stores sessions, messages, compression lineage, subagent metadata, and durable session search substrate.
6. **Surfaces** — CLI, TUI, dashboard, desktop app, and gateway platforms all drive the same core agent with different transports.
7. **Long-running work** — `delegate_task`, cron, terminal background processes, kanban, and platform gateways each have different durability semantics.
8. **Compounding layer** — skills, memory, session search, profiles, and vault files are what make the system improve instead of merely answer.

## Core agent loop

`AIAgent` lives in `run_agent.py`. The simplified loop is:

1. Build messages and tool schemas.
2. Call the selected provider/model.
3. If the response contains tool calls, execute them and append tool results.
4. Repeat until a final response appears or the iteration budget is exhausted.
5. Compression can split/continue sessions when context grows.

Important invariant: preserve message-role alternation and prompt-cache stability. Hermes often chooses designs that avoid mutating old context, even if a simpler implementation would look tempting.

## Tool system secrets

- Built-in tools self-register via `registry.register(...)` in `tools/*.py`.
- A registered tool is not automatically exposed. It must be included in a toolset in `toolsets.py`.
- `get_tool_definitions()` is cached for quiet-mode callers; cache invalidates via registry generation and config fingerprint.
- Tool schemas are expensive because they are sent to the model. New capability should usually be added as a skill, CLI command, plugin, MCP server, or gated tool — not as a core always-on tool.
- Runtime-owned tools such as memory, todo, clarify, session search, context engine, and delegation may be intercepted by the agent runtime before normal `handle_function_call` dispatch.
- Tool handlers should return JSON strings. If a tool stores state, use `get_hermes_home()` so profiles remain isolated.

## Delegation secrets

`tools/delegate_tool.py` spawns child `AIAgent` instances with isolated conversation and terminal session. Parent context sees only the final summary, not every child tool call.

Key points:

- Leaf subagents cannot call `delegate_task`, `clarify`, `memory`, `send_message`, or `execute_code`.
- Default concurrency is capped by `delegation.max_concurrent_children`.
- Default depth is flat unless `delegation.max_spawn_depth` is explicitly raised.
- Subagent dangerous-command approval is auto-deny by default to avoid deadlocking the parent TUI/CLI input.
- Background delegation is process-local and best-effort; it does not survive parent process death. Use cron or tracked terminal background jobs for durable work.
- `tools/async_delegation.py` sends completed background results through the shared completion queue as a fresh turn. This preserves message-role alternation and prompt-cache integrity.

Operational rule for Mohamed: use delegation for parallel thinking/research/review; use cron or terminal background for durable jobs that must survive restarts.

## Cron secrets

Cron is not just shell cron. It is an autonomous agent-run scheduler with delivery.

Key files:

- `cron/jobs.py` — job store.
- `cron/scheduler.py` — tick loop.
- `tools/cronjob_tools.py` — model-facing management tool.

Important behavior:

- Jobs run in fresh sessions. Prompts must be self-contained.
- Cron skips memory by default (`skip_memory=True`) so scheduled tasks do not pollute user memory.
- Deliveries are not mirrored into the target gateway session; they arrive as separate cron outputs to preserve conversation invariants.
- Job features include skills, model overrides, scripts, `no_agent`, `context_from`, delivery targets, enabled toolsets, and `workdir` with project context files.
- Cron prompt scanning is stricter for user-authored prompts and looser for skill-assembled prompts to avoid false positives from security prose inside skills.
- Latest main restored per-profile cron storage. Always verify cron jobs in the active profile after updating.

Operational rule for Mohamed: schedule only mature workflows with stable prompts, source rules, and verification. Do not automate unstable reasoning too early.

## Memory secrets

`tools/memory_tool.py` keeps built-in memory compact and cache-safe.

Important behavior:

- Memory injected into the system prompt is a frozen snapshot captured at load time. Mid-session writes persist to disk but do not alter the active system prompt. This preserves prompt-cache stability.
- The `operations` array applies add/replace/remove as an all-or-nothing batch against the final character budget.
- Batch updates allow removing stale entries and adding a new entry in one call, even when a simple add would overflow.
- Memory content is scanned for injection/exfil patterns before writing.

Operational rule for Mohamed: use memory only for durable facts and preferences; procedures go to skills; project state goes to vault; temporary progress stays in session or task files.

## Skills secrets

Skills are Hermes' reusable procedural memory.

Important behavior:

- Skills should describe trigger conditions, exact commands, pitfalls, and verification steps.
- Skills can include linked files under `references/`, `templates/`, `scripts/`, and `assets/`.
- Skills loaded by the model are instruction/context, not executable magic. Good descriptions decide whether the right skill is loaded.
- Skill curation can archive stale agent-created skills but does not delete them. Pinned skills are protected from deletion.
- After v0.17, routine curator runs do not spend auxiliary-model budget unless consolidation is explicitly enabled.

Operational rule for Mohamed: every hard-won Hermes workflow should become or patch a skill, not disappear in chat history.

## Plugin and extension secrets

The preferred extension path is not always editing core.

Extension choices:

- Custom tools/hooks/commands/skills: plugin directory under `~/.hermes/plugins/<name>/`.
- External tools: MCP server in `config.yaml`.
- New model backend: model provider plugin docs.
- New gateway channel: platform adapter docs.
- Memory backend: memory provider plugin docs.
- TTS/STT: often config-driven, no Python plugin needed.

Plugin concurrency pitfall: process-wide lazy singletons can race under delegated/background work. Use `plugins/plugin_utils.py` helpers: `lazy_singleton` or `SingletonSlot`.

## Profiles and isolation secrets

Profiles are not cosmetic. They isolate config, memory, skills, cron, sessions, and gateway state.

Practical use:

- Stable daily operator profile for Mohamed's main assistant.
- Market profile for EGX workflow.
- Lab profiles for experiments.
- Separate Telegram bot tokens for simultaneously connected profiles.

Pitfall: in PRoot/no-systemd environments, service status can lie. Trust process list, logs, state files, and real message delivery checks more than systemd output.

## Surfaces map

- Classic CLI: prompt toolkit + Rich UI.
- TUI: TypeScript Ink front end talks to Python `tui_gateway` via JSON-RPC over stdio.
- Dashboard chat embeds the real TUI through a PTY bridge; do not rebuild the primary chat experience in React.
- Desktop app is separate Electron/React surface that talks to `tui_gateway` over JSON-RPC and has its own composer/transcript path.
- Gateway platforms translate platform events into the same agent core.

## Recent main-branch note after v0.17

Latest main at inspection had one commit beyond the prior local state:

- `af7b7f632 feat(agent): expose coding-context project facts as structured data + project.facts RPC (#51259)`

Meaning: coding/project context facts are becoming structured data and exposed through a project facts RPC, useful for desktop/TUI/dashboard surfaces and future coding-context-aware workflows.

## Mohamed-specific operating lessons

1. **Context first, automation last.** Hermes rewards a stable context/rules/memory/verification layer before cron or agent swarms.
2. **Use profiles like departments.** Market, operator, lab, and future company-intelligence profiles should stay isolated.
3. **Subagents are leverage, not durability.** Good for parallel review and research; not for jobs that must survive process exits.
4. **Skills are the compounding layer.** If a workflow takes debugging or more than a few tool calls, patch/create a skill.
5. **Memory must stay small.** Mohamed's memory is near capacity; use batch operations to remove stale entries and add compact facts together.
6. **Don't add core tools casually.** Prefer plugin/MCP/skill/CLI paths to avoid bloating every model call.
7. **Verify with the live system.** For Hermes itself, trust `git describe`, `hermes --version`, `hermes doctor`, logs, and runtime imports together; one signal can be stale.
8. **PRoot update rule.** Always use `UV_LINK_MODE=copy` on Android/PRoot-like setups and reinstall editable after a pull if dependencies changed or runtime looks inconsistent.

## Practical update checklist for Mohamed's PRoot setup

```bash
cd /root/.hermes/hermes-agent
git fetch --all --tags --prune
git status -sb
git pull --ff-only
export UV_LINK_MODE=copy
/root/.local/bin/uv pip install --python /root/.hermes/hermes-agent/venv/bin/python -e .
yes '' | hermes config migrate || true
hermes config check || true
hermes doctor || true
hermes --version
git status -sb
git describe --tags --always --dirty
```

If gateway behavior matters, verify with process/log evidence and a real Telegram delivery check rather than relying on systemd status in PRoot.
