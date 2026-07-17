---
name: hermes-agent
description: Complete guide to using and extending Hermes Agent — CLI usage, setup, configuration, spawning additional agents, gateway platforms, skills, voice, tools, profiles, and a concise contributor reference. Load this skill when helping users configure Hermes, troubleshoot issues, spawn agent instances, or make code contributions.
version: 2.0.0
author: Hermes Agent + Teknium
license: MIT
metadata:
  hermes:
    tags: [hermes, setup, configuration, multi-agent, spawning, cli, gateway, development]
    homepage: https://github.com/NousResearch/hermes-agent
    related_skills: [claude-code, codex, opencode]
---

# Hermes Agent

Hermes Agent is an open-source AI agent framework by Nous Research that runs in your terminal, messaging platforms, and IDEs. It belongs to the same category as Claude Code (Anthropic), Codex (OpenAI), and OpenClaw — autonomous coding and task-execution agents that use tool calling to interact with your system. Hermes works with any LLM provider (OpenRouter, Anthropic, OpenAI, DeepSeek, local models, and 15+ others) and runs on Linux, macOS, and WSL.

What makes Hermes different:

- **Self-improving through skills** — Hermes learns from experience by saving reusable procedures as skills. When it solves a complex problem, discovers a workflow, or gets corrected, it can persist that knowledge as a skill document that loads into future sessions. Skills accumulate over time, making the agent better at your specific tasks and environment.
- **Persistent memory across sessions** — remembers who you are, your preferences, environment details, and lessons learned. Pluggable memory backends (built-in, Honcho, Mem0, and more) let you choose how memory works.
- **Multi-platform gateway** — the same agent runs on Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Email, and 8+ other platforms with full tool access, not just chat.
- **Provider-agnostic** — swap models and providers mid-workflow without changing anything else. Credential pools rotate across multiple API keys automatically.
- **Profiles** — run multiple independent Hermes instances with isolated configs, sessions, skills, and memory.
- **Extensible** — plugins, MCP servers, custom tools, webhook triggers, cron scheduling, and the full Python ecosystem.

People use Hermes for software development, research, system administration, data analysis, content creation, home automation, and anything else that benefits from an AI agent with persistent context and full system access.

**This skill helps you work with Hermes Agent effectively** — setting it up, configuring features, spawning additional agent instances, troubleshooting issues, finding the right commands and settings, and understanding how the system works when you need to extend or contribute to it.

**Docs:** https://hermes-agent.nousresearch.com/docs/

## Mohamed Update Awareness Rule

When Mohamed asks about Hermes Agent capabilities, updates, configuration, troubleshooting, or how to make the assistant more useful, do not rely only on this static skill. First refresh the live picture:

1. Check the local checkout and effective version:
   ```bash
   hermes --version || true
   git -C /root/.hermes/hermes-agent status -sb || true
   git -C /root/.hermes/hermes-agent describe --tags --always --dirty || true
   git -C /root/.hermes/hermes-agent log --oneline --decorate -n 15 || true
   ```
2. Check the official release page:
   - `https://github.com/NousResearch/hermes-agent/releases/latest`
   - `https://github.com/NousResearch/hermes-agent/releases`
3. Compare local `git describe` against the latest release tag. In Mohamed's proot setup, the reported package version can lag behind the checked-out code; trust git state, logs, and runtime checks over the version string alone.
4. Patch this skill after every meaningful Hermes update with durable capability changes, new commands, breaking changes, and environment-specific pitfalls. Do not store temporary commit counts or one-off progress here unless they explain a recurring version mismatch pattern.
5. If the update affects Telegram, gateway, tools, profiles, cron, skills, model providers, memory, or browser/computer-use behavior, add a concise note to the relevant section and verify with commands/logs before saying it works.

## Current Release Notes Snapshot: Hermes Agent v0.18.0 / v2026.7.1

Official sources:
- `https://github.com/NousResearch/hermes-agent/releases/latest`
- `https://github.com/NousResearch/hermes-agent/releases/tag/v2026.7.1`

Release framing: v0.18.0 is "The Judgment Release". The major theme is closing the full P0/P1 backlog and improving how Hermes judges whether work is actually complete, while making Mixture-of-Agents, self-improvement, desktop coding projects, gateway scaling, and security stronger.

Key durable v0.18.0 changes to remember:

- Mixture-of-Agents is now a first-class selectable provider/model path: named MoA presets appear under provider `moa`; `/moa` is mainly one-shot sugar.
- MoA reference-model outputs render as labelled blocks, and the aggregator answer can stream in CLI, TUI, and desktop.
- Hermes now has stronger verification/completion mechanics: coding work can record verification evidence, `/goal` supports completion contracts, and custom `pre_verify` hooks can define done checks.
- `/learn` can distill a workflow, directory, or URL into a reusable skill.
- `/journey` shows a learning timeline of memories and skills, with edit/delete paths; desktop also gained a memory graph.
- `delegate_task` supports background fan-out for multiple subagents, returning a consolidated result after they finish.
- Desktop gained first-class coding Projects: codebase sidebar, coding rail, review pane, worktree management, and project/repo/lane model.
- Gateway became more production-grade: scale-to-zero, drain coordination, clean quiescing before restarts/migrations/updates.
- Post-turn self-improvement is cheaper: auxiliary-model routing, context digestion instead of replaying full conversation, and adaptive cadence.
- `/prompt` opens `$EDITOR` for composing long prompts.
- Vertex AI is a first-class Gemini provider using service-account or ADC OAuth token refresh, not static API keys.
- Security hardening included MCP config persistence, cron `base_url` credential exfiltration blocking, file-read prefix secret sentinels, Slack token redaction, browser metadata floors, and `aiohttp` CVE floors.
- Latest main after v0.18.0 includes Telegram polling timeout fixes: bounded `start_polling()` at bootstrap, network-error handler, and conflict-retry paths (commits through `aaeba213d` on `origin/main` as of 2026-07-10). After any Hermes pull, verify Telegram with process list + `gateway.log`, not only `hermes gateway status` in PRoot.

**Local install snapshot (refresh when Mohamed asks to update as Hermes):** package reports `Hermes Agent v0.18.0 (2026.7.1)`; git often reads `v2026.7.1-N-g<sha>` on tracking `main` while CLI still says up to date — trust `hermes doctor`, OpenAI SDK import, and gateway behavior together.

Useful older changes still relevant:

- v0.17 added new gateway reach, stronger desktop/dashboard surfaces, image-to-image generation, major memory tool upgrades, plugin-namespace Telegram logs, and per-profile cron storage on latest main.
- v0.16 introduced native desktop/browser admin surfaces, `/undo`, Quick Setup via Nous Portal, and security hardening around SSRF/subprocess credentials.

Mohamed-specific interpretation:

- The most useful v0.18 changes for Mohamed are verification-first completion, `/learn`, `/journey`, MoA as a real model option, stronger background subagents, desktop coding Projects, and safer gateway restarts.
- In Mohamed's aarch64 PRoot setup, continue using `UV_LINK_MODE=copy` during updates and verify with `hermes doctor`, config version, git state, process/log checks, runtime imports, and Telegram gateway connectivity. Systemd gateway status may still be misleading in PRoot; trust processes, logs, state file, and Bot API checks.
- `hermes update --backup --yes` can create a very large backup and may take several minutes. If dependency installation fails, repair from `/root/.hermes/hermes-agent` with `UV_LINK_MODE=copy /root/.local/bin/uv pip install --python /root/.hermes/hermes-agent/venv/bin/python -e .`.
- The package version string can lag behind git state; trust `git describe`, `git status`, release tags, and runtime checks together.

## Mohamed Deep Hermes Operating Map

When Mohamed asks to understand how Hermes works, improve the assistant's operating system, debug/update Hermes, design agent teams, decide between memory/skills/profiles/cron/delegation, or capture "secrets" and hard-won Hermes lessons, load this reference:

`references/2026-06-23-hermes-agent-deep-operating-map.md`

It captures a verified 2026-06-23 source inspection after fast-forwarding `/root/.hermes/hermes-agent` to latest `origin/main` (`af7b7f632`), including the core loop, tool registry, delegation, async completion queue, cron, memory batch semantics, plugin extension paths, profile isolation, PRoot update checklist, and Mohamed-specific operating lessons.

## Mohamed Self-Understanding Reference

Mohamed designated the Hermes Agent Masterclass note as a durable self-understanding reference for this assistant: capabilities, boundaries, memory discipline, skill-based improvement, profiles, cron, and verification. When Mohamed asks what I can do, where my limits are, how I improve, how to configure me, or how to make me more useful over time, read the linked reference before answering.

Reference file: `references/mohamed-self-understanding.md`

Core framing: Hermes is a small operating system around the model — identity, memory, skills, session search, profiles, scheduled runs, tools, and verification — not just a chat surface.

## Quick Start

```bash
# Install
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Interactive chat (default)
hermes

# Single query
hermes chat -q "What is the capital of France?"

# Setup wizard
hermes setup

# Change model/provider
hermes model

# Check health
hermes doctor
```

---

## CLI Reference

### Global Flags

```
hermes [flags] [command]

  --version, -V             Show version
  --resume, -r SESSION      Resume session by ID or title
  --continue, -c [NAME]     Resume by name, or most recent session
  --worktree, -w            Isolated git worktree mode (parallel agents)
  --skills, -s SKILL        Preload skills (comma-separate or repeat)
  --profile, -p NAME        Use a named profile
  --yolo                    Skip dangerous command approval
  --pass-session-id         Include session ID in system prompt
```

No subcommand defaults to `chat`.

### Chat

```
hermes chat [flags]
  -q, --query TEXT          Single query, non-interactive
  -m, --model MODEL         Model (e.g. anthropic/claude-sonnet-4)
  -t, --toolsets LIST       Comma-separated toolsets
  --provider PROVIDER       Force provider (openrouter, anthropic, nous, etc.)
  -v, --verbose             Verbose output
  -Q, --quiet               Suppress banner, spinner, tool previews
  --checkpoints             Enable filesystem checkpoints (/rollback)
  --source TAG              Session source tag (default: cli)
```

### Configuration

```
hermes setup [section]      Interactive wizard (model|terminal|gateway|tools|agent)
hermes model                Interactive model/provider picker
hermes config               View current config
hermes config edit          Open config.yaml in $EDITOR
hermes config set KEY VAL   Set a config value
hermes config path          Print config.yaml path
hermes config env-path      Print .env path
hermes config check         Check for missing/outdated config
hermes config migrate       Update config with new options
hermes auth add nous --type oauth        Add Nous OAuth credential (device code flow)
hermes auth add openai-codex --type oauth Add OpenAI Codex OAuth credential
hermes auth list                        List pooled credentials
hermes auth remove PROVIDER --id ID     Remove credential
hermes doctor [--fix]       Check dependencies and config
hermes status [--all]       Show component status
```

### Tools & Skills

```
hermes tools                Interactive tool enable/disable (curses UI)
hermes tools list           Show all tools and status
hermes tools enable NAME    Enable a toolset
hermes tools disable NAME   Disable a toolset

hermes skills list          List installed skills
hermes skills search QUERY  Search the skills hub
hermes skills install ID    Install a skill
hermes skills inspect ID    Preview without installing
hermes skills config        Enable/disable skills per platform
hermes skills check         Check for updates
hermes skills update        Update outdated skills
hermes skills uninstall N   Remove a hub skill
hermes skills publish PATH  Publish to registry
hermes skills browse        Browse all available skills
hermes skills tap add REPO  Add a GitHub repo as skill source
```

### MCP Servers

```
hermes mcp serve            Run Hermes as an MCP server
hermes mcp add NAME         Add an MCP server (--url or --command)
hermes mcp remove NAME      Remove an MCP server
hermes mcp list             List configured servers
hermes mcp test NAME        Test connection
hermes mcp configure NAME   Toggle tool selection
```

### Gateway (Messaging Platforms)

```
hermes gateway run          Start gateway foreground
hermes gateway install      Install as background service
hermes gateway start/stop   Control the service
hermes gateway restart      Restart the service
hermes gateway status       Check status
hermes gateway setup        Configure platforms
```

Supported platforms: Telegram, Discord, Slack, WhatsApp, Signal, Email, SMS, Matrix, Mattermost, Home Assistant, DingTalk, Feishu, WeCom, API Server, Webhooks, Open WebUI.

Platform docs: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/

### Sessions

```
hermes sessions list        List recent sessions
hermes sessions browse      Interactive picker
hermes sessions export OUT  Export to JSONL
hermes sessions rename ID T Rename a session
hermes sessions delete ID   Delete a session
hermes sessions prune       Clean up old sessions (--older-than N days)
hermes sessions stats       Session store statistics
```

### Cron Jobs

```
hermes cron list            List jobs (--all for disabled)
hermes cron create SCHED    Create: '30m', 'every 2h', '0 9 * * *'
hermes cron edit ID         Edit schedule, prompt, delivery
hermes cron pause/resume ID Control job state
hermes cron run ID          Trigger on next tick
hermes cron remove ID       Delete a job
hermes cron status          Scheduler status
```

### Webhooks

```
hermes webhook subscribe N  Create route at /webhooks/<name>
hermes webhook list         List subscriptions
hermes webhook remove NAME  Remove a subscription
hermes webhook test NAME    Send a test POST
```

### Profiles

```
hermes profile list         List all profiles
hermes profile create NAME  Create (--clone, --clone-all, --clone-from, --no-alias)
hermes profile use NAME     Set sticky default
hermes profile delete NAME  Delete a profile
hermes profile show NAME    Show details
hermes profile alias NAME   Manage wrapper scripts
hermes profile rename A B   Rename a profile
hermes profile export NAME  Export to tar.gz
hermes profile import FILE  Import from archive
```

#### Practical profile workflow

Use this when you want a clean, reusable operator profile:

1. Create the profile from the current active profile:
   ```bash
   hermes profile create operator --clone --no-alias
   ```
2. Inspect the new profile:
   ```bash
   hermes profile show operator
   hermes profile list
   ```
3. Edit the cloned files directly in `~/.hermes/profiles/<name>/`:
   - `SOUL.md` for behavior and operating rules
   - `config.yaml` for model, memory, compression, approvals, delegation, display
   - `.env` only if the profile needs different credentials
4. Create an alias wrapper when you want a short command:
   ```bash
   hermes profile alias operator
   # or: hermes profile alias operator --name op
   ```
   This creates a wrapper in `~/.local/bin/` that forwards to `hermes -p <profile> ...`.
5. Re-check the profile after edits:
   ```bash
   hermes profile show operator
   ```
6. Only set the profile as sticky default if you really want every future Hermes session to use it:
   ```bash
   hermes profile use operator
   ```

#### Notes and pitfalls

- `hermes profile create --clone` copies the active profile's `config.yaml`, `.env`, and `SOUL.md` into an isolated profile directory.
- `--no-alias` is useful when you want to control the wrapper name yourself later.
- The profile path is the source of truth; wrappers are just convenience entry points.
- Keep production and experimentation separated. Use one profile for stable daily work and another for experiments when you need to test prompt or config changes.
- Verify the profile with `hermes profile list` and `hermes profile show <name>` after making changes.

### Credential Pools

```
hermes auth add             Interactive credential wizard
hermes auth list [PROVIDER] List pooled credentials
hermes auth remove P INDEX  Remove by provider + index
hermes auth reset PROVIDER  Clear exhaustion status
```

### Other

```
hermes insights [--days N]  Usage analytics
hermes update               Update to latest version
hermes pairing list/approve/revoke  DM authorization
hermes plugins list/install/remove  Plugin management
hermes honcho setup/status  Honcho memory integration
hermes memory setup/status/off  Memory provider config
hermes completion bash|zsh  Shell completions
hermes acp                  ACP server (IDE integration)
hermes claw migrate         Migrate from OpenClaw
hermes uninstall            Uninstall Hermes
```

---

## Slash Commands (In-Session)

Type these during an interactive chat session.

### Session Control
```
/new (/reset)        Fresh session
/clear               Clear screen + new session (CLI)
/retry               Resend last message
/undo                Remove last exchange
/title [name]        Name the session
/compress            Manually compress context
/stop                Kill background processes
/rollback [N]        Restore filesystem checkpoint
/background <prompt> Run prompt in background
/queue <prompt>      Queue for next turn
/resume [name]       Resume a named session
```

### Configuration
```
/config              Show config (CLI)
/model [name]        Show or change model
/provider            Show provider info
/prompt [text]       View/set system prompt (CLI)
/personality [name]  Set personality
/reasoning [level]   Set reasoning (none|low|medium|high|xhigh|show|hide)
/verbose             Cycle: off → new → all → verbose
/voice [on|off|tts]  Voice mode
/yolo                Toggle approval bypass
/skin [name]         Change theme (CLI)
/statusbar           Toggle status bar (CLI)
```

### Tools & Skills
```
/tools               Manage tools (CLI)
/toolsets            List toolsets (CLI)
/skills              Search/install skills (CLI)
/skill <name>        Load a skill into session
/cron                Manage cron jobs (CLI)
/reload-mcp          Reload MCP servers
/plugins             List plugins (CLI)
```

### Info
```
/help                Show commands
/commands [page]     Browse all commands (gateway)
/usage               Token usage
/insights [days]     Usage analytics
/status              Session info (gateway)
/profile             Active profile info
```

### Exit
```
/quit (/exit, /q)    Exit CLI
```

---

## Key Paths & Config

```
~/.hermes/config.yaml       Main configuration
~/.hermes/.env              API keys and secrets
~/.hermes/skills/           Installed skills
~/.hermes/sessions/         Session transcripts
~/.hermes/logs/             Gateway and error logs
~/.hermes/auth.json         OAuth tokens and credential pools
~/.hermes/hermes-agent/     Source code (if git-installed)
```

Profiles use `~/.hermes/profiles/<name>/` with the same layout.

### Config Sections

Edit with `hermes config edit` or `hermes config set section.key value`.

| Section | Key options |
|---------|-------------|
| `model` | `default`, `provider`, `base_url`, `api_key`, `context_length` |
| `agent` | `max_turns` (90), `tool_use_enforcement` |
| `terminal` | `backend` (local/docker/ssh/modal), `cwd`, `timeout` (180) |
| `compression` | `enabled`, `threshold` (0.50), `target_ratio` (0.20) |
| `display` | `skin`, `tool_progress`, `show_reasoning`, `show_cost` |
| `stt` | `enabled`, `provider` (local/groq/openai) |
| `tts` | `provider` (edge/elevenlabs/openai/kokoro/fish) |
| `memory` | `memory_enabled`, `user_profile_enabled`, `provider` |
| `security` | `tirith_enabled`, `website_blocklist` |
| `delegation` | `model`, `provider`, `max_iterations` (50) |
| `smart_model_routing` | `enabled`, `cheap_model` |
| `checkpoints` | `enabled`, `max_snapshots` (50) |

Full config reference: https://hermes-agent.nousresearch.com/docs/user-guide/configuration

### Providers

18 providers supported. Set via `hermes model` or `hermes setup`.

| Provider | Auth | Key env var |
|----------|------|-------------|
| OpenRouter | API key | `OPENROUTER_API_KEY` |
| Anthropic | API key | `ANTHROPIC_API_KEY` |
| Nous Portal | OAuth | `hermes login --provider nous` |
| OpenAI Codex | OAuth | `hermes login --provider openai-codex` |
| GitHub Copilot | Token | `COPILOT_GITHUB_TOKEN` |
| DeepSeek | API key | `DEEPSEEK_API_KEY` |
| Hugging Face | Token | `HF_TOKEN` |
| Z.AI / GLM | API key | `GLM_API_KEY` |
| MiniMax | API key | `MINIMAX_API_KEY` |
| Kimi / Moonshot | API key | `KIMI_API_KEY` |
| Alibaba / DashScope | API key | `DASHSCOPE_API_KEY` |
| Kilo Code | API key | `KILOCODE_API_KEY` |
| Custom endpoint | Config | `model.base_url` + `model.api_key` in config.yaml |

Plus: AI Gateway, OpenCode Zen, OpenCode Go, MiniMax CN, GitHub Copilot ACP.

Full provider docs: https://hermes-agent.nousresearch.com/docs/integrations/providers

### Toolsets

Enable/disable via `hermes tools` (interactive) or `hermes tools enable/disable NAME`.

| Toolset | What it provides |
|---------|-----------------|
| `web` | Web search and content extraction |
| `browser` | Browser automation (Browserbase, Camofox, or local Chromium) |
| `terminal` | Shell commands and process management |
| `file` | File read/write/search/patch |
| `code_execution` | Sandboxed Python execution |
| `vision` | Image analysis |
| `image_gen` | AI image generation |
| `tts` | Text-to-speech |
| `skills` | Skill browsing and management |
| `memory` | Persistent cross-session memory |
| `session_search` | Search past conversations |
| `delegation` | Subagent task delegation |
| `cronjob` | Scheduled task management |
| `clarify` | Ask user clarifying questions |
| `moa` | Mixture of Agents (off by default) |
| `homeassistant` | Smart home control (off by default) |

Tool changes take effect on `/reset` (new session). They do NOT apply mid-conversation to preserve prompt caching.

---

## Voice & Transcription

### STT (Voice → Text)

Voice messages from messaging platforms are auto-transcribed.

Provider priority (auto-detected):
1. **Local faster-whisper** — free, no API key: `pip install faster-whisper`
2. **Groq Whisper** — free tier: set `GROQ_API_KEY`
3. **OpenAI Whisper** — paid: set `VOICE_TOOLS_OPENAI_KEY`

Config:
```yaml
stt:
  enabled: true
  provider: local        # local, groq, openai
  local:
    model: base          # tiny, base, small, medium, large-v3
```

### TTS (Text → Voice)

| Provider | Env var | Free? |
|----------|---------|-------|
| Edge TTS | None | Yes (default) |
| ElevenLabs | `ELEVENLABS_API_KEY` | Free tier |
| OpenAI | `VOICE_TOOLS_OPENAI_KEY` | Paid |
| Kokoro (local) | None | Free |
| Fish Audio | `FISH_AUDIO_API_KEY` | Free tier |

Voice commands: `/voice on` (voice-to-voice), `/voice tts` (always voice), `/voice off`.

---

## Spawning Additional Hermes Instances

Run additional Hermes processes as fully independent subprocesses — separate sessions, tools, and environments.

### When to Use This vs delegate_task

| | `delegate_task` | Spawning `hermes` process |
|-|-----------------|--------------------------|
| Isolation | Separate conversation, shared process | Fully independent process |
| Duration | Minutes (bounded by parent loop) | Hours/days |
| Tool access | Subset of parent's tools | Full tool access |
| Interactive | No | Yes (PTY mode) |
| Use case | Quick parallel subtasks | Long autonomous missions |

### One-Shot Mode

```
terminal(command="hermes chat -q 'Research GRPO papers and write summary to ~/research/grpo.md'", timeout=300)

# Background for long tasks:
terminal(command="hermes chat -q 'Set up CI/CD for ~/myapp'", background=true)
```

### Interactive PTY Mode (via tmux)

Hermes uses prompt_toolkit, which requires a real terminal. Use tmux for interactive spawning:

```
# Start
terminal(command="tmux new-session -d -s agent1 -x 120 -y 40 'hermes'", timeout=10)

# Wait for startup, then send a message
terminal(command="sleep 8 && tmux send-keys -t agent1 'Build a FastAPI auth service' Enter", timeout=15)

# Read output
terminal(command="sleep 20 && tmux capture-pane -t agent1 -p", timeout=5)

# Send follow-up
terminal(command="tmux send-keys -t agent1 'Add rate limiting middleware' Enter", timeout=5)

# Exit
terminal(command="tmux send-keys -t agent1 '/exit' Enter && sleep 2 && tmux kill-session -t agent1", timeout=10)
```

### Multi-Agent Coordination

```
# Agent A: backend
terminal(command="tmux new-session -d -s backend -x 120 -y 40 'hermes -w'", timeout=10)
terminal(command="sleep 8 && tmux send-keys -t backend 'Build REST API for user management' Enter", timeout=15)

# Agent B: frontend
terminal(command="tmux new-session -d -s frontend -x 120 -y 40 'hermes -w'", timeout=10)
terminal(command="sleep 8 && tmux send-keys -t frontend 'Build React dashboard for user management' Enter", timeout=15)

# Check progress, relay context between them
terminal(command="tmux capture-pane -t backend -p | tail -30", timeout=5)
terminal(command="tmux send-keys -t frontend 'Here is the API schema from the backend agent: ...' Enter", timeout=5)
```

### Session Resume

```
# Resume most recent session
terminal(command="tmux new-session -d -s resumed 'hermes --continue'", timeout=10)

# Resume specific session
terminal(command="tmux new-session -d -s resumed 'hermes --resume 20260225_143052_a1b2c3'", timeout=10)
```

### Tips

- **Prefer `delegate_task` for quick subtasks** — less overhead than spawning a full process
- **Use `-w` (worktree mode)** when spawning agents that edit code — prevents git conflicts
- **Set timeouts** for one-shot mode — complex tasks can take 5-10 minutes
- **Use `hermes chat -q` for fire-and-forget** — no PTY needed
- **Use tmux for interactive sessions** — raw PTY mode has `\r` vs `\n` issues with prompt_toolkit
- **For scheduled tasks**, use the `cronjob` tool instead of spawning — handles delivery and retry

---

## Troubleshooting

### Voice not working
1. Check `stt.enabled: true` in config.yaml
2. Verify provider: `pip install faster-whisper` or set API key
3. Restart gateway: `/restart`

### Telegram vision/image analysis times out
If a Telegram image is cached and routed to native vision, but the auxiliary vision call times out, do not stop at the failed tool call.

1. Confirm the platform tools and routing:
```bash
hermes tools list --platform telegram | sed -n '/vision/Ip;/image/Ip;/browser/Ip'
grep -i "Cached user photo\|Image routing\|timeout" ~/.hermes/logs/gateway.log | tail -80
```
2. Treat the common `Codex auxiliary Responses stream exceeded 30.0s total timeout` failure as an internal auxiliary timeout unless logs prove otherwise; it can occur even when the global Hermes timeout is higher.
3. For text-heavy images, fall back to local OCR when available:
```bash
tesseract /path/to/image.jpg stdout -l ara+eng --psm 6
```
4. If present, use the reusable helper:
```bash
~/.hermes/scripts/image_ocr_fallback.sh /path/to/image.jpg
```
5. Be explicit with the user: primary vision timed out, OCR is approximate, and a clearer/cropped image may still be needed.

Session-specific detail: see `references/telegram-vision-timeout-ocr-fallback.md`.

### Tool not available
1. `hermes tools` — check if toolset is enabled for your platform
2. For messaging surfaces, verify platform-specific toggles too:
   - `hermes tools list --platform telegram`
   - `hermes tools enable browser --platform telegram`
3. Some tools need env vars (check `.env`)
4. `/reset` after enabling tools

### Browser Use cloud mode says "not configured"
If Browser Use fails with a message like "requires either BROWSER_USE_API_KEY or managed gateway":
1. Set provider selection in config:
   - `hermes config set browser.cloud_provider browser-use`
2. Enable managed tools flag in `.env`:
   - `HERMES_ENABLE_NOUS_MANAGED_TOOLS=true`
3. Add Nous OAuth credential (current flow):
   - `hermes auth add nous --type oauth --no-browser`
4. Confirm `auth.json` has a `providers.nous.access_token` entry.
5. Restart gateway/session after changes.

Note: `hermes login` has been removed; use `hermes auth add ... --type oauth`.

### Model/provider issues
1. `hermes doctor` — check config and dependencies
2. `hermes login` — re-authenticate OAuth providers
3. Check `.env` has the right API key

### Changes not taking effect
- **Tools/skills:** `/reset` starts a new session with updated toolset
- **Config changes:** `/restart` reloads gateway config
- **Code changes:** Restart the CLI or gateway process

### Updating in Android/proot or other no-systemd environments
When updating Hermes in a Linux aarch64 PRoot/Android environment, do not assume a normal systemd service will revive the gateway, and do not trust `uv` defaults if dependency install fails.

Safe sequence:
1. Capture baseline:
   ```bash
   hermes --version
   git -C /root/.hermes/hermes-agent status -sb
   ps -efww | grep -E 'gateway run|hermes.*gateway' | grep -v grep || true
   ```
2. Stop only real gateway processes, then clear stale state. Avoid broad `pkill -f` patterns inside a one-liner because they can match and kill the shell running the update command in PRoot:
   ```bash
   pgrep -af 'gateway run|hermes.*gateway' || true
   pgrep -f 'gateway run --replace' | xargs -r kill || true
   pgrep -f 'python.*gateway run' | xargs -r kill || true
   rm -f /root/.hermes/gateway_state.json /root/.hermes/gateway.pid
   rm -f /root/.hermes2/gateway_state.json /root/.hermes2/gateway.pid
   ```
3. Run the update:
   ```bash
   hermes update --backup --yes
   ```
4. If dependency installation fails with uv hardlink/copy errors, missing venv detection, or broken packages after the code pull, repair explicitly:
   ```bash
   cd /root/.hermes/hermes-agent
   export UV_LINK_MODE=copy
   /root/.local/bin/uv pip install --python /root/.hermes/hermes-agent/venv/bin/python -e .
   ```
5. Migrate/check and verify:
   ```bash
   yes '' | hermes config migrate || true
   hermes config check || true
   hermes doctor || true
   hermes --version
   git -C /root/.hermes/hermes-agent status -sb
   ```
6. Restart the gateway as a tracked/background process (or equivalent supervisor), then verify live process + state + logs. In no-systemd/proot, `hermes gateway status` may be misleading.

Pitfall: `hermes update` can successfully pull the latest git commit but fail while installing dependencies. In that state `git status` may look up to date while runtime packages are broken (for example OpenAI SDK missing). Always verify `hermes --version`, `hermes doctor`, and gateway connectivity after update.

Reference: see `references/proot-update-uv-hardlink.md` for a concrete Android/proot uv failure transcript pattern and repair checklist. Also see `references/2026-05-18-proot-update-v0140-uv-copy-repair.md` for a full successful v0.13.0 → v0.14.0 update transcript pattern, and `references/2026-06-12-hermes-v0160-proot-update.md` for a v0.15.1 → v0.16.0 update transcript pattern (including timeout-after-core-success recovery). All show the same general pattern: `hermes update --backup --yes` partly succeeded but dependency installation required an explicit `UV_LINK_MODE=copy` editable reinstall before gateway restart.

### Skills not showing
1. `hermes skills list` — verify installed
2. `hermes skills config` — check platform enablement
3. Load explicitly: `/skill name` or `hermes -s name`

### Gateway issues
Check logs first:
```bash
grep -i "failed to send\|error" ~/.hermes/logs/gateway.log | tail -20
```

### OpenClaw pairing required / gateway closed (1008)
If a Hermes wrapper or CLI is routed through OpenClaw and fails with `gateway closed (1008): pairing required`, the issue is usually the OpenClaw execution gateway, not Hermes itself.

1. Verify the gateway and device state:
```bash
openclaw devices list
openclaw gateway status
```
2. Approve the latest pending device when appropriate:
```bash
openclaw devices approve --latest
```
3. Confirm the wrapper passes the OpenClaw gateway token into the process environment. A safe pattern is to export `OPENCLAW_GATEWAY_TOKEN` from `~/.openclaw/openclaw.json` (or honor an already-set value) before exec'ing Hermes.
4. Re-test with a simple non-destructive command, then run `openclaw gateway call health` if needed.

Common pitfall: `openclaw gateway restart` may be unavailable in container/non-systemd environments. In that case, use `openclaw gateway run` or `openclaw gateway --force` under the current supervisor instead of relying on systemd.

If Telegram or another messaging platform fails with `InvalidURL` or a strange token rejection, inspect the token value in `~/.hermes/.env` for hidden control characters or pasted escape sequences. A quick sanity check is to print the token with Python and look for bytes below 32 or equal to 127. If a clean backup exists (for example under `~/.hermes/migration/.../backups/.../.env`), restore the token from that backup rather than hand-editing guesses.

Also note: in containerized environments without a working systemd user bus (`DBUS_SESSION_BUS_ADDRESS` / `XDG_RUNTIME_DIR` missing), `hermes gateway status` may report the gateway as stopped even while `hermes gateway run` is actively running. In that case, trust the process/logs instead of the systemd status output.

### Session memory / report consolidation
When asked to gather or merge memories from past Hermes sessions:
1. Use `session_search` first to find the relevant sessions and keyword hits.
2. Read the underlying `~/.hermes/sessions/session_*.json` files when summaries are truncated or too vague.
3. Extract only durable facts: fixes, preferences, environment quirks, and confirmed outcomes.
4. Exclude temporary progress notes and duplicate log chatter.
5. If memory is near capacity, remove stale temporary overrides before adding a compact summary.
6. Write a short report artifact so the human can review the consolidation without rereading full sessions.

---

## Where to Find Things

| Looking for... | Location |
|----------------|----------|
| Config options | `hermes config edit` or [Configuration docs](https://hermes-agent.nousresearch.com/docs/user-guide/configuration) |
| Available tools | `hermes tools list` or [Tools reference](https://hermes-agent.nousresearch.com/docs/reference/tools-reference) |
| Slash commands | `/help` in session or [Slash commands reference](https://hermes-agent.nousresearch.com/docs/reference/slash-commands) |
| Skills catalog | `hermes skills browse` or [Skills catalog](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) |
| Provider setup | `hermes model` or [Providers guide](https://hermes-agent.nousresearch.com/docs/integrations/providers) |
| Platform setup | `hermes gateway setup` or [Messaging docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/) |
| MCP servers | `hermes mcp list` or [MCP guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) |
| Profiles | `hermes profile list` or [Profiles docs](https://hermes-agent.nousresearch.com/docs/user-guide/profiles) |
| Cron jobs | `hermes cron list` or [Cron docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) |
| Memory | `hermes memory status` or [Memory docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) |
| Env variables | `hermes config env-path` or [Env vars reference](https://hermes-agent.nousresearch.com/docs/reference/environment-variables) |
| CLI commands | `hermes --help` or [CLI reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands) |
| Gateway logs | `~/.hermes/logs/gateway.log` |
| Session files | `~/.hermes/sessions/` or `hermes sessions browse` |
| Source code | `~/.hermes/hermes-agent/` |

---

## Contributor Quick Reference

For occasional contributors and PR authors. Full developer docs: https://hermes-agent.nousresearch.com/docs/developer-guide/

### Project Layout

```
hermes-agent/
├── run_agent.py          # AIAgent — core conversation loop
├── model_tools.py        # Tool discovery and dispatch
├── toolsets.py           # Toolset definitions
├── cli.py                # Interactive CLI (HermesCLI)
├── hermes_state.py       # SQLite session store
├── agent/                # Prompt builder, compression, display, adapters
├── hermes_cli/           # CLI subcommands, config, setup, commands
│   ├── commands.py       # Slash command registry (CommandDef)
│   ├── config.py         # DEFAULT_CONFIG, env var definitions
│   └── main.py           # CLI entry point and argparse
├── tools/                # One file per tool
│   └── registry.py       # Central tool registry
├── gateway/              # Messaging gateway
│   └── platforms/        # Platform adapters (telegram, discord, etc.)
├── cron/                 # Job scheduler
├── tests/                # ~3000 pytest tests
└── website/              # Docusaurus docs site
```

Config: `~/.hermes/config.yaml` (settings), `~/.hermes/.env` (API keys).

### Adding a Tool (3 files)

**1. Create `tools/your_tool.py`:**
```python
import json, os
from tools.registry import registry

def check_requirements() -> bool:
    return bool(os.getenv("EXAMPLE_API_KEY"))

def example_tool(param: str, task_id: str = None) -> str:
    return json.dumps({"success": True, "data": "..."})

registry.register(
    name="example_tool",
    toolset="example",
    schema={"name": "example_tool", "description": "...", "parameters": {...}},
    handler=lambda args, **kw: example_tool(
        param=args.get("param", ""), task_id=kw.get("task_id")),
    check_fn=check_requirements,
    requires_env=["EXAMPLE_API_KEY"],
)
```

**2. Add import** in `model_tools.py` → `_discover_tools()` list.

**3. Add to `toolsets.py`** → `_HERMES_CORE_TOOLS` list.

All handlers must return JSON strings. Use `get_hermes_home()` for paths, never hardcode `~/.hermes`.

### Adding a Slash Command

1. Add `CommandDef` to `COMMAND_REGISTRY` in `hermes_cli/commands.py`
2. Add handler in `cli.py` → `process_command()`
3. (Optional) Add gateway handler in `gateway/run.py`

All consumers (help text, autocomplete, Telegram menu, Slack mapping) derive from the central registry automatically.

### Agent Loop (High Level)

```
run_conversation():
  1. Build system prompt
  2. Loop while iterations < max:
     a. Call LLM (OpenAI-format messages + tool schemas)
     b. If tool_calls → dispatch each via handle_function_call() → append results → continue
     c. If text response → return
  3. Context compression triggers automatically near token limit
```

### Testing

```bash
source venv/bin/activate  # or .venv/bin/activate
python -m pytest tests/ -o 'addopts=' -q   # Full suite
python -m pytest tests/tools/ -q            # Specific area
```

- Tests auto-redirect `HERMES_HOME` to temp dirs — never touch real `~/.hermes/`
- Run full suite before pushing any change
- Use `-o 'addopts='` to clear any baked-in pytest flags

### Commit Conventions

```
type: concise subject line

Optional body.
```

Types: `fix:`, `feat:`, `refactor:`, `docs:`, `chore:`

### Key Rules

- **Never break prompt caching** — don't change context, tools, or system prompt mid-conversation
- **Message role alternation** — never two assistant or two user messages in a row
- Use `get_hermes_home()` from `hermes_constants` for all paths (profile-safe)
- Config values go in `config.yaml`, secrets go in `.env`
- New tools need a `check_fn` so they only appear when requirements are met
