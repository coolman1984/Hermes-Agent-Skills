---
name: mohamed-claude-codex-control-bridge
description: Use when Mohamed asks Hermes to control, audit, learn from, or bridge
  Claude Code, Codex CLI, OpenCode CLI, and Gemini CLI, including reading their skills/memories,
  delegating tasks, importing useful skill workflows into Hermes, or maintaining a
  local multi-agent control layer on this Android/PRoot machine.
version: 1.4.0
author: Hermes + Mohamed
license: MIT
tags: [claude-code, codex, opencode, control-bridge, delegation, cli]
metadata:
  tags:
  - claude-code
  - codex
  - opencode
  - hermes
  - multi-agent
  - skills
  - android-proot
  - orchestration
---

# Mohamed Claude/Codex/OpenCode Control Bridge

## Purpose

This skill is the local bridge between Hermes, Claude Code, Codex CLI, and OpenCode CLI on Mohamed's machine.

Use it when Mohamed wants Hermes to:

- control Claude Code, Codex, or OpenCode from the terminal;
- verify installation, authentication, health, plans, and model availability;
- use them as specialist coding agents;
- read their local rules, skills, commands, agents, or memories;
- copy useful workflows from their skill systems into Hermes skills;
- create shared project guidance so all agents work consistently.

## Verified local state

Last verified on 2026-06-13.

- Host pattern: Android/Termux plus Linux PRoot.
- Hermes: `/root/.local/bin/hermes`, version reported as `Hermes Agent v0.16.0 (2026.6.5)`.
- Claude Code: `/root/.local/bin/claude`, version `2.1.177`.
- Claude safe wrapper: `/root/.local/bin/claude-safe`, version `2.1.177`.
- Termux npm Claude duplicate was updated to `2.1.177` to remove the stale-path mismatch.
- Codex: `/data/data/com.termux/files/usr/bin/codex`, version `codex-cli 0.139.0`.
- OpenCode: `/root/.opencode/bin/opencode`, version `1.17.4`.
- Gemini CLI: `/data/data/com.termux/files/usr/bin/gemini`, version `0.46.0` after updating `@google/gemini-cli` in the Termux npm prefix.
- tmux inside PRoot: `/usr/bin/tmux`.
- Codex doctor passed: install consistent, auth configured, websocket connected, state databases healthy. Current default is non-interactive: `approval_policy = "never"`, `sandbox_mode = "workspace-write"`.
- Claude auth status passed: Claude Pro account for Mohamed's email. `claude doctor` may be slow or hang; do not block on it if auth and smoke tests pass. Current user settings default to `permissions.defaultMode = "auto"` with `CLAUDE_CODE_ENABLE_AUTO_MODE=1`.
- OpenCode credentials list shows `OpenCode Go api` and `OpenAI oauth`.
- OpenCode Go direct smoke with `opencode-go/glm-5` now succeeds and returned `OPENCODE_GO_OK`; billing/credits are active as of 2026-06-13.
- Gemini CLI install and no-prompt wrapper are configured, but headless smoke is blocked until a Gemini auth method exists. Verification showed no `GEMINI_API_KEY`, `GOOGLE_API_KEY`, `GOOGLE_GENAI_USE_VERTEXAI`, or `GOOGLE_GENAI_USE_GCA` in the environment; smoke failed with code 41 asking for auth.

## Important paths

Claude Code:

- Global rules: `/root/.claude/CLAUDE.md`
- Settings: `/root/.claude/settings.json`
- Agents: `/root/.claude/agents/`
- Commands: `/root/.claude/commands/`
- Project memories: `/root/.claude/projects/`

Codex:

- Config: `/root/.codex/config.toml`
- Skills: `/root/.codex/skills/`
- System skills: `/root/.codex/skills/.system/`
- Memories: `/root/.codex/memories/`
- Sessions: `/root/.codex/sessions/`
- Plugins: `/root/.codex/plugins/`

OpenCode:

- Binary: `/root/.opencode/bin/opencode`
- Config: `/root/.config/opencode/opencode.jsonc`
- Auth file location reported by CLI: `/root/.local/share/opencode/auth.json` — do not read or copy this file.
- Use `opencode auth list` to check credentials.
- Use `opencode models` or `opencode models <provider>` to list models.
- Use `opencode upgrade` to update the standalone binary.
- Current global config sets `permission` to allow common tools and `share` to disabled for privacy.

Gemini CLI:

- Binary: `/data/data/com.termux/files/usr/bin/gemini`
- Auto wrapper: `/root/.local/bin/gemini-auto`
- Settings: `/root/.gemini/settings.json`
- Auth is external: cached Google sign-in, `GEMINI_API_KEY`, or Vertex/Code Assist env. Do not read credential caches.

Shared no-prompt and role wrappers:

- `/root/.local/bin/claude-auto`
- `/root/.local/bin/codex-auto`
- `/root/.local/bin/opencode-auto`
- `/root/.local/bin/gemini-auto`
- `/root/.local/bin/claude-architect`
- `/root/.local/bin/codex-supervisor`
- `/root/.local/bin/opencode-worker`
- `/root/.local/bin/opencode-worker-cheap`
- `/root/.local/bin/opencode-worker-hard`

Hermes:

- Skills: `/root/.hermes/skills/`
- Current profile skills must be modified through `skill_manage`, not ad hoc shell edits.
- Other profile skills under `/root/.hermes/profiles/<name>/skills/` must not be modified unless Mohamed explicitly asks.

## Safety boundary

Never read or copy secrets from:

- `.env`
- `auth.json`
- credential files
- token files
- private keys

Claude settings already deny reading common secret files. Keep that pattern.

Do not auto-copy whole third-party skill directories into Hermes without review. First inspect `SKILL.md`, references, scripts, license, and purpose. Copy only reusable procedures or create a clean Hermes-native skill that cites the source path.

## Claude Code control

Prefer print mode for one-shot tasks:

```bash
CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=0 claude -p 'TASK' --allowedTools 'Read,Edit,Bash' --max-turns 5 --output-format json
```

Use safe wrapper when appropriate:

```bash
/root/.local/bin/claude-safe -p 'TASK' --allowedTools 'Read' --max-turns 2 --output-format json
```

Use tmux for multi-turn interactive control:

```bash
tmux new-session -d -s claude-work -x 140 -y 40
tmux send-keys -t claude-work 'cd /path/to/project && CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=0 claude' Enter
sleep 5 && tmux capture-pane -t claude-work -p -S -80
```

Claude on this PRoot setup needs:

```bash
CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=0
```

because bubblewrap secret-scrubbing can fail under PRoot. Compensate with deny rules in `/root/.claude/settings.json` and narrow `--allowedTools`.

## Codex control

Codex is healthy and authenticated. It generally requires a git repository unless using `--skip-git-repo-check`.

Mohamed quota policy:

- Hard tasks: `-m gpt-5.5 -c model_reasoning_effort='"medium"'`
- Easy tasks: `-m gpt-5.4-mini -c model_reasoning_effort='"xhigh"'`
- Do not silently use higher reasoning on `gpt-5.5`.

Read-only smoke pattern:

```bash
cd /tmp/some-git-repo
codex exec --json --ephemeral -m gpt-5.4-mini -c model_reasoning_effort='"xhigh"' -c approval_policy='"never"' -s read-only 'Answer exactly CODEX_OK. Do not modify files.'
```

For actual coding:

```bash
codex exec -m gpt-5.5 -c model_reasoning_effort='"medium"' -s workspace-write 'TASK'
```

If a foreground Codex run hangs with no output, retry with `--json --ephemeral` and a timeout. A previous verified smoke test returned `CODEX_OK` with JSON events.

## OpenCode control

Verify:

```bash
opencode --version
opencode auth list
opencode models
```

Update:

```bash
opencode upgrade
```

One-shot run:

```bash
opencode run --format json --model opencode-go/glm-5 'TASK'
```

If OpenCode Go reports insufficient balance, do not keep retrying. Treat it as a billing/credit activation problem and ask Mohamed to check the OpenCode workspace billing page.

### OpenCode Go models observed

```text
opencode-go/deepseek-v4-flash
opencode-go/deepseek-v4-pro
opencode-go/glm-5
opencode-go/glm-5.1
opencode-go/kimi-k2.6
opencode-go/kimi-k2.7-code
opencode-go/mimo-v2.5
opencode-go/mimo-v2.5-pro
opencode-go/minimax-m2.7
opencode-go/minimax-m3
opencode-go/qwen3.6-plus
opencode-go/qwen3.7-max
opencode-go/qwen3.7-plus
```

### Other OpenCode/OpenAI models observed

```text
opencode/big-pickle
opencode/deepseek-v4-flash-free
opencode/mimo-v2.5-free
opencode/nemotron-3-ultra-free
opencode/north-mini-code-free
openai/gpt-5.3-codex-spark
openai/gpt-5.4
openai/gpt-5.4-fast
openai/gpt-5.4-mini
openai/gpt-5.4-mini-fast
openai/gpt-5.5
openai/gpt-5.5-fast
openai/gpt-5.5-pro
```

## Gemini CLI control

Gemini CLI is installed but requires auth before headless delegation works.

Update in this Android/PRoot setup:

```bash
npm install -g --prefix /data/data/com.termux/files/usr @google/gemini-cli@latest
npm config set prefix /data/data/com.termux/files/usr
gemini --version
```

No-prompt wrapper:

```bash
/root/.local/bin/gemini-auto -p 'TASK' --output-format json
```

The wrapper expands to:

```bash
gemini --approval-mode=yolo --skip-trust ...
```

Settings can persist `general.defaultApprovalMode = "auto_edit"`, but docs say full `yolo` approval must be passed as a CLI flag. If smoke fails with code 41, configure one auth route:

- interactive `gemini` Google sign-in;
- `GEMINI_API_KEY` from Google AI Studio;
- Vertex/Google Code Assist environment.

Read the dedicated Hermes skill `gemini-cli` for details.

## Codex skills discovered locally

System skills currently present:

- `imagegen`
- `openai-docs`
- `plugin-creator`
- `skill-creator`
- `skill-installer`

Useful source paths:

```bash
/root/.codex/skills/.system/skill-creator/SKILL.md
/root/.codex/skills/.system/openai-docs/SKILL.md
/root/.codex/skills/.system/skill-installer/SKILL.md
```

Durable lessons already worth importing into Hermes workflows:

- Keep skills concise; context window is a shared resource.
- Skill descriptions are the trigger surface; make them explicit about when to use the skill.
- Put detailed references and scripts under `references/` and `scripts/` instead of bloating `SKILL.md`.
- Use validation artifacts and independent checks when updating a skill.
- Choose the smallest durable surface: prompt for one-off constraints, project guidance for repo conventions, skill for reusable workflow, plugin for bundled commands/tools/assets, hook for mechanical enforcement, automation for scheduled work.

## Importing skills from Codex, Claude, or OpenCode into Hermes

1. Identify source:
   - Codex skill: `/root/.codex/skills/**/SKILL.md`
   - Claude global rule: `/root/.claude/CLAUDE.md`
   - Claude command: `/root/.claude/commands/*.md`
   - Claude agent: `/root/.claude/agents/*.md`
   - OpenCode config/session/plugin material only after inspecting non-secret files.
2. Read the source file and any referenced scripts or references.
3. Decide whether it belongs in Hermes:
   - user preference → memory;
   - reusable procedure → Hermes skill;
   - project state → vault or project files;
   - enforcement → hook/config/tooling, not just prose.
4. Create a Hermes-native skill with `skill_manage(action='create')`.
5. Preserve only useful procedure, paths, commands, pitfalls, and verification steps.
6. Do not copy secrets or auth files.
7. Verify by loading the new skill with `skill_view` and, if possible, running a harmless smoke test.

## Mohamed coding-team hierarchy

For coding projects, load and follow the `mohamed-coding-team` skill. Durable rule:

1. Hermes owns orchestration, verification, Arabic reporting, memory, and final accountability.
2. Claude Code is the consulting architect only: architecture, phases, hard-error strategy. Default wrapper: `/root/.local/bin/claude-architect`; model `opus`, effort `high`. Do not let Claude bulk-write code by default because Opus tokens are expensive.
3. Codex is the supervising execution engineer: detailed implementation plan, code-quality rules, review, and repair instructions. Default wrapper: `/root/.local/bin/codex-supervisor`; model `gpt-5.5`, reasoning `medium`.
4. OpenCode is the worker layer that writes most code. Default wrapper: `/root/.local/bin/opencode-worker`; model `opencode-go/minimax-m3`. Cheap worker: `opencode-worker-cheap` with `deepseek-v4-flash`. Hard worker: `opencode-worker-hard` with `deepseek-v4-pro`.
5. Gemini CLI is optional second opinion / large-context assistant after auth works.

Use Claude first for new serious projects and repeated hard blockers; use Codex for supervision and reviews; use OpenCode workers for implementation; verify everything directly.

## Verification checklist

Before saying the bridge works, verify at least once:

- `claude --version`
- `claude auth status --text`
- `codex --version`
- `codex doctor --summary`
- `opencode --version`
- `opencode auth list`
- `opencode models opencode-go`
- `gemini --version`
- Claude auto print smoke returns expected text.
- Codex non-interactive exec smoke returns expected text.
- OpenCode Go smoke returns expected text.
- Gemini smoke returns expected text, or if it fails, the exact auth failure mode is recorded.
- No git changes were made during smoke tests unless intentionally testing writes.

## Current smoke-test proof

Claude smoke:

- Workdir: `/tmp/agent-control-smoke`
- Command used read-only `--allowedTools 'Read'`
- Result: `CLAUDE_OK`

Codex smoke:

- Workdir: `/tmp/agent-control-smoke`
- Command used `--json --ephemeral`, read-only sandbox, approval never, easy model pairing.
- Result: `CODEX_OK`

OpenCode Go smoke:

- Workdir: `/tmp/opencode-go-smoke`
- Command used `opencode run --format json --model opencode-go/glm-5`.
- Result: failed with `Insufficient balance`, despite `OpenCode Go api` credential being present.

## Mohamed preference (Hermes model setup)

When Mohamed asks to wire, fix, or switch **Grok / Claude models inside Hermes**, do all work yourself: OAuth flows, `hermes config set`, `hermes auth add`, `.env` updates, smoke tests, and fallback chain edits. **Never** reply with a checklist for Mohamed to run commands or "try these steps." Report what you changed and the verification result only.

Detailed provider recipes: `references/hermes-grok-claude-providers.md`.

## Hermes-native Claude + Grok (not just CLI)

Claude Code and Grok CLI being logged in does **not** guarantee Hermes model picker works.

Always verify the **Hermes provider layer**:

```bash
hermes auth status anthropic
hermes auth status xai-oauth
hermes auth list anthropic
hermes auth list xai-oauth
```

If `anthropic` is `logged out` while `claude auth status` is logged in, sync Claude Code OAuth into Hermes (see reference). Empty `ANTHROPIC_*` lines in `~/.hermes/.env` are a common cause of "Claude not working" in Telegram.

If `/model` switches to Claude but Telegram returns **"The model provider failed after retries"**, read `errors.log` for `You're out of extra usage` and `hermes auth list anthropic` for `exhausted` cooldowns—that is a **quota** issue, not missing login. Route via **kilocode** (`anthropic/claude-opus-4-8` or `anthropic/claude-sonnet-4-6`) and wire `fallback_providers` per reference. **Do not** add OAuth tokens as manual `api_key` creds.

Grok OAuth (`xai-oauth`) may display internal model id `grok-build-0.1` while config id `grok-4.5` still works—set and smoke-test the id; do not assume the picker label matches the config string.

## Operating rule

For Mohamed, this bridge is not a license to create a zoo of agents. Use Claude, Codex, and OpenCode as specialist workers only when they add leverage. Keep Hermes as the operator that owns context, Arabic reporting, vault writes, memory hygiene, verification, and final accountability.
