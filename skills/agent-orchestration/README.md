# Agent Orchestration & Hermes OS

> Multi-agent loops, Hermes configuration, profiles, workers, and handoffs.

**Skills in this domain:** 22

| Skill | Description |
|---|---|
| [`agentic-workflows-do-framework`](./agentic-workflows-do-framework/) | Build production AI workflows using Directive-Orchestration-Execution pattern — separates probabilistic reasoning from deterministic execution. |
| [`ai-coding-cli-delegation`](./ai-coding-cli-delegation/) | Use when delegating coding or review work to external AI coding CLIs such as Claude Code, Codex, OpenCode, or Gemini while Hermes coordinates scope, verifica... |
| [`ai-handoff-control-layer`](./ai-handoff-control-layer/) | Build a robust handoff/control layer for future AI agents using a document-driven operating contract, machine-readable manifest, and validation script instea... |
| [`debugging-hermes-tui-commands`](./debugging-hermes-tui-commands/) | Debug Hermes TUI slash commands: Python, gateway, Ink UI. |
| [`gemini-cli`](./gemini-cli/) | Delegate coding and research tasks to Google Gemini CLI, including install, auth, no-prompt automation, MCP, skills, and verification. |
| [`generic-agent-setup`](./generic-agent-setup/) | Bootstrap and run GenericAgent (self-evolving autonomous agent) in Linux aarch64 PRoot/Android environments. Includes dependency triage, API config, and comm... |
| [`hermes-agent`](./hermes-agent/) | Complete guide to using and extending Hermes Agent — CLI usage, setup, configuration, spawning additional agents, gateway platforms, skills, voice, tools, pr... |
| [`hermes-agent-skill-authoring`](./hermes-agent-skill-authoring/) | Author in-repo SKILL.md: frontmatter, validator, structure. |
| [`hermes-gateway-telegram-stuck`](./hermes-gateway-telegram-stuck/) | Fix and auto-detect Telegram gateway stuck in typing loop - restart the gateway process when stuck |
| [`hermes-honcho-manager-dispatch-fix`](./hermes-honcho-manager-dispatch-fix/) | Fix Hermes/OpenClaw tool outages caused by `handle_function_call() got an unexpected keyword argument 'honcho_manager'` via backward-compatible dispatcher si... |
| [`hermes-kanban-workflows`](./hermes-kanban-workflows/) | Use when operating Hermes Kanban as an orchestrator or worker: decomposing work, enforcing worker lifecycle, avoiding orchestration temptations, and verifyin... |
| [`hermes-openclaw-wrapper-fixes`](./hermes-openclaw-wrapper-fixes/) | Troubleshoot Hermes wrappers that sit behind an OpenClaw gateway, fix pairing/token issues, and verify the wrapper actually talks to the gateway. |
| [`hermes-profile-bootstrap`](./hermes-profile-bootstrap/) | Bootstrap, clone, and harden Hermes profiles for a production/experiment pair with safe config, interactive setup handling, and verification. Use when creati... |
| [`hermes-s6-container-supervision`](./hermes-s6-container-supervision/) | Modify, debug, or extend the s6-overlay supervision tree inside the Hermes Agent Docker image — adding new services, debugging profile gateways, understandin... |
| [`kanban-codex-lane`](./kanban-codex-lane/) | Use when a Hermes Kanban worker wants to run Codex CLI as an isolated implementation lane while Hermes keeps ownership of task lifecycle, reconciliation, tes... |
| [`mohamed-agent-loop-os`](./mohamed-agent-loop-os/) | Use when Mohamed wants a serious multi-agent workflow, a long-running coding/research loop, background workers, factory-style processing, or any task that mu... |
| [`mohamed-claude-codex-control-bridge`](./mohamed-claude-codex-control-bridge/) | Use when Mohamed asks Hermes to control, audit, learn from, or bridge Claude Code, Codex CLI, OpenCode CLI, and Gemini CLI, including reading their skills/me... |
| [`mohamed-coding-team`](./mohamed-coding-team/) | Use when Mohamed asks for coding work, architecture, implementation, debugging, code review, or a multi-agent coding workflow. Defines Mohamed's permanent co... |
| [`mohamed-opencode-go-worker-profiles`](./mohamed-opencode-go-worker-profiles/) | Use when Mohamed wants Hermes to run background worker profiles on OpenCode Go models, choose the right model for a task, refresh model choices, or improve t... |
| [`persistent-memory-project-governance`](./persistent-memory-project-governance/) | Use when Mohamed wants a file-based project operating system for multi-step work, data projects, reports, software builds, factory workflows, or restartable ... |
| [`subagent-driven-development`](./subagent-driven-development/) | Execute plans via delegate_task subagents (2-stage review). |
| [`team-governed-coding-workflow`](./team-governed-coding-workflow/) | Use for Mohamed's serious coding/project work when execution must flow through a fixed team: Hermes plans/orchestrates/final-verifies, deepseek-fast writes o... |

## How to use

Each skill folder contains a `SKILL.md` (required). Optional support folders:

- `references/` — deep docs and absorbed packages
- `templates/` — reusable templates
- `scripts/` — helper scripts
- `assets/` — static assets

