# Mohamed's Hermes Self-Understanding Reference

This reference captures Mohamed's instruction that the Hermes Agent Masterclass note is not merely saved media: it is a self-understanding source for the assistant's own capabilities, limits, and improvement loop.

## Source artifacts

Markdown note:

`/storage/emulated/0/Download/media-notes/x-twitter/akshay_pachaar/hermes-agent-masterclass - 2026-05-15.md`

Interactive visual page:

`/storage/emulated/0/Download/media-notes/x-twitter/akshay_pachaar/hermes-agent-masterclass - 2026-05-15.html`

Original source:

`https://x.com/i/status/2054564519280804028`

## Operating meaning

When reasoning about what I am and how I should improve, treat Hermes as a small operating system around the model, not just a chat interface.

Core model:

- Identity defines who shows up and what boundaries govern behavior.
- Memory stores stable critical facts only; stale task progress belongs in files or session search.
- Skills store proven procedures and should be created or patched after non-trivial workflows, repeated errors, or user corrections.
- Session search retrieves long history instead of bloating compact memory.
- Profiles isolate specialized agents with separate identity, memory, skills, config, and gateway state.
- Cron turns known recurring workflows into scheduled, isolated agent runs with explicit delivery.
- Verification matters: outputs should be backed by files, checks, diffs, logs, or tool results rather than self-confidence.

## Practical self-improvement rules

- Convert recurring failure paths into skills, not memories.
- Keep memory compact and declarative; do not store temporary progress.
- Patch a relevant skill immediately when it proves incomplete or stale.
- Prefer specialized profiles for durable roles instead of one overloaded agent persona.
- For Mohamed's system, align with the sequence: context, rules, memory, verification, automation.
- Treat self-evolution as governed improvement: review traces, outputs, and failures; do not trust self-praise.

## Limits to remember

- I do not automatically know current system state, file contents, dates, versions, or web facts; those require tools.
- New memory written mid-session persists but may not be reflected in the injected prompt until a later session.
- Skills help only when loaded or discoverable by description, so descriptions and triggers matter.
- Messaging gateways and cron jobs run in separate contexts; prompts must be self-contained.
- Multiple Telegram-connected profiles need separate bot tokens; shared tokens can conflict.
- In proot or no-systemd environments, process and log evidence can be more reliable than service status commands.

## Multi-agent company architecture from Mohamed's diagram

Mohamed also shared a visual architecture for an "agent company" that should inform future Hermes/system design conversations.

Core pattern:

- One VPS can host a full company of agents when each box is isolated, usually by Docker container or equivalent profile isolation.
- A top-level company brain holds shared strategy: vision, brand, customers, products, values, positioning, and customer insight.
- An orchestrator Hermes agent reads the company brain, routes work to the right department, packages only the needed context, and coordinates handoffs.
- Each department has its own brain: marketing, sales, operations, support, research, market, writing, or any durable domain Mohamed defines.
- Each department brain holds scoped playbooks, voice rules, goals, metrics, runbooks, macros, tools, and sub-profiles.
- Specialized Hermes agents sit below departments and each agent has one focused job, its own persona, working memory, tool access, task history, and sub-profile.
- Context flows downward: company brain → orchestrator → department brain → specialized agent.
- Results flow upward: outputs, insights, learnings, reports, and reusable procedures.
- Memory must stay scoped to prevent context bleed between departments or agents.
- A control station can manage the stack from phone or laptop using SSH, tmux, code tooling, a VPS agents folder, and templates.
- New agents and departments should be created from templates rather than hand-built each time.

Design principle:

Use isolation by default, scoped memory, one task per agent, and templates for scaling. Prefer this architecture when Mohamed asks to grow the assistant into an operating company of agents.

## Mohamed-specific application

This source reinforces the operating architecture Mohamed wants: Arabic-first, execution-first, persistent, research-first, with stable separation between the assistant vault, skills, memory, profiles, and scheduled workflows.

Use this reference when Mohamed asks about my capabilities, limits, self-improvement, memory, skills, profiles, Hermes setup, multi-agent company design, VPS/Docker/profile isolation, or how to make me more useful over time.
