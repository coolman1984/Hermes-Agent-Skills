---
name: mohamed-coding-team
description: Use when Mohamed asks for coding work, architecture, implementation,
  debugging, code review, or a multi-agent coding workflow. Defines Mohamed's permanent
  coding-team hierarchy across Claude Code, Codex CLI, OpenCode, Gemini CLI, and Hermes.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
tags: [multi-agent, coding-team, delegation, orchestration, workflow]
metadata:
  tags:
  - coding-team
  - architecture
  - implementation
  - review
  - claude-code
  - codex
  - opencode
  - gemini
  - hermes
  related_skills:
  - mohamed-claude-codex-control-bridge
  - claude-code
  - codex
  - opencode
  - gemini-cli
---

# Mohamed Coding Team

## Core rule

Hermes is the operator and accountable delivery manager. The other agents are specialist workers. Do not let them become a zoo.

## Mohamed-specific operating override (2026-07-01)

For serious project coding work, Mohamed wants this workflow enforced by default:

- **Hermes** = planning, task slicing, orchestration, final verification, and Mohamed-facing summary.
- **`deepseek-fast` / deepseek-v4-flash** = writing worker only.
- **`deepseek-pro` / deepseek-v4-pro** = review worker only.

Do not collapse this back into solo execution just because Hermes can code directly. If Mohamed asked to use the team, that team workflow is the default system, not an optional flourish.

Operational rule:

1. Hermes defines the slice and acceptance check.
2. The writing worker produces the draft/change.
3. The review worker critiques scope, correctness, and drift.
4. Hermes applies only the surviving parts, verifies with real commands, then reports to Mohamed.

Pitfall to avoid:

- **Wrong:** Hermes silently implements the whole slice alone for speed, then reports the result.
- **Right:** Hermes may still do tiny glue/final integration work, but the writing/review separation must remain visible on meaningful project work.

Second pitfall to avoid:

- **Wrong:** Hermes uses the team once for planning/governance, then stops after a paperwork update even though the next safe code slice is obvious.
- **Right:** when Mohamed says to continue the project using the system, Hermes should keep the team loop running across successive small slices — writer draft, reviewer critique, Hermes verification, then immediately the next smallest justified slice — until a real blocker appears.

Operational continuation rule:

- If the current slice ends with a clear next internal move and no external dependency blocks it, do not stop at status updates alone.
- Land the governance/state update, then push into the next implementation slice in the same session.
- Only pause after one slice if the next move depends on user input, external data, risky side effects, or materially ambiguous scope.

For any serious multi-agent, long-running, or factory-style coding task, load and follow:

`mohamed-agent-loop-os`

That skill is the operating doctrine for planner-generator-evaluator separation, file-backed state, explicit contracts, restart tolerance, and trace-based repair. Do not run Mohamed's serious coding workflows as loose chat delegation.

Before using the team on any meaningful software task, load:

`senior-software-engineer`

That skill is the non-negotiable engineering discipline layer: context-first discovery, small slices, real verification, security/performance review, and no fake success.

Default chain for serious coding projects:

1. **Claude Code = consulting architect only**
2. **Codex = supervising execution engineer**
3. **OpenCode = implementation workers**
4. **Gemini CLI = optional second opinion / large-context assistant after auth**
5. **Hermes = orchestration, verification, Arabic reporting, memory, and final accountability**

## Role 1 — Claude Code: consulting architect

Use Claude Code for architecture, phases, decomposition, root-cause strategy, and hard-error diagnosis.

Required default:

```bash
/root/.local/bin/claude-architect -p 'TASK' --output-format json
```

Wrapper expands to Claude Code with:

- model: `opus`
- effort: `high`
- permission mode: `auto`
- tools restricted toward reading, web, and git inspection
- max turns: limited to reduce spend

### Claude must do

- Design project architecture.
- Define phases and acceptance criteria.
- Choose technologies and tradeoffs.
- For hard bugs, explain the repair path first.
- Tell Codex/OpenCode which files/functions/tests to touch.
- Recommend which functions, abstractions, libraries, and testing style to use.
- Review strategic direction when a project starts drifting.

### Claude must not do by default

- Do not write implementation code.
- Do not perform broad edits.
- Do not run long agentic loops.
- Do not burn Opus tokens on worker-level tasks.

Only let Claude write code if Mohamed explicitly asks or if a tiny architecture-critical snippet is cheaper than ambiguity.

## Role 2 — Codex: supervising execution engineer

Use Codex as the engineering lead under Claude: implementation planning, code-quality instructions, review, patch critique, and supervising OpenCode workers.

Required default:

```bash
/root/.local/bin/codex-supervisor 'TASK'
```

Wrapper defaults:

- model: `gpt-5.5`
- reasoning: `medium`
- approval: `never`
- sandbox: workspace-write

### Codex must do

- Convert Claude's architecture into concrete engineering tasks.
- Decide small implementation steps.
- Define code-quality standards and test strategy.
- Review OpenCode diffs.
- Tell OpenCode exactly what to fix.
- Own tricky implementation details where worker models are likely to miss edge cases.

### Codex should not do by default

- Do not do all bulk coding if cheaper OpenCode workers can do it.
- Do not use higher than `medium` reasoning on `gpt-5.5` unless Mohamed explicitly changes quota policy.

## Role 3 — OpenCode: implementation workers

Use OpenCode workers for writing most code, tests, docs, and mechanical refactors.

Default worker:

```bash
/root/.local/bin/opencode-worker 'TASK'
```

Current default model:

```text
opencode-go/minimax-m3
```

Cheap worker:

```bash
/root/.local/bin/opencode-worker-cheap 'TASK'
```

Uses:

```text
opencode-go/deepseek-v4-flash
```

Harder worker:

```bash
/root/.local/bin/opencode-worker-hard 'TASK'
```

Uses:

```text
opencode-go/deepseek-v4-pro
```

## OpenCode model choice: quality versus cost

Verified `opencode-go` metadata on 2026-06-13:

- `minimax-m3`: input `0.1`, output `0.4`, context `512K`, output `131K`, reasoning/tools supported.
- `deepseek-v4-flash`: input `0.14`, output `0.28`, context `1M`, output `384K`, reasoning/tools supported.
- `minimax-m2.7`: input `0.3`, output `1.2`, context `204K`, output `131K`.
- `qwen3.7-plus`: input `0.4`, output `1.6`, context `1M`, output `65K`.
- `kimi-k2.7-code`: input `0.95`, output `4`, context `262K`, output `262K`.
- `deepseek-v4-pro`: input `1.74`, output `3.48`, context `1M`, output `384K`.

### Default recommendation

- **Primary coding worker:** `opencode-go/minimax-m3`
  - Best default balance: very cheap, large enough context, good for bulk implementation and tests.
- **Cheapest long-context worker:** `opencode-go/deepseek-v4-flash`
  - Use for large repo sweeps, simple features, repetitive edits, and low-risk scaffolding.
- **Hard worker before escalating to Codex:** `opencode-go/deepseek-v4-pro`
  - Use for complex implementation when MiniMax fails or when the code path is subtle.
- **Specialized coding experiment:** `opencode-go/kimi-k2.7-code`
  - Use when code generation quality matters more than cost, especially long code output.
- **Avoid as default:** `qwen3.7-max`, `glm-5.1`, `deepseek-v4-pro` for routine work because cost is high compared with MiniMax and DeepSeek Flash.

## Standard project workflow

### Phase 0 — intake

Hermes gathers context:

- repo path
- current branch and git status
- relevant docs
- tests/build commands
- constraints from Mohamed

### Phase 1 — architecture

Call Claude only for the plan:

```bash
/root/.local/bin/claude-architect -p '
You are Mohamed’s consulting architect. Do not write code.
Inspect the request and produce:
1. architecture decision
2. phases
3. files likely involved
4. risks
5. test strategy
6. instructions for Codex supervisor and OpenCode workers
'
```

Output should be saved or summarized before implementation.

### Phase 2 — execution plan

Call Codex to turn architecture into worker tasks:

```bash
/root/.local/bin/codex-supervisor 'Create an implementation plan from this architecture. Do not bulk-code unless necessary. Produce worker-ready tasks and review checklist.'
```

### Phase 3 — worker implementation

Use OpenCode workers on isolated tasks and workdirs/worktrees when possible:

```bash
/root/.local/bin/opencode-worker 'Implement task A. Keep changes scoped. Run relevant tests.'
```

For simple/large cheap tasks:

```bash
/root/.local/bin/opencode-worker-cheap 'Apply this mechanical refactor across the repo.'
```

For hard worker implementation:

```bash
/root/.local/bin/opencode-worker-hard 'Implement the tricky part described by Codex. Keep changes minimal.'
```

### Phase 4 — supervision review

Codex reviews worker diffs:

```bash
git diff | /root/.local/bin/codex-supervisor 'Review this diff. Find bugs, missing tests, design drift, and exact fixes for OpenCode. Do not rewrite everything.'
```

### Phase 5 — repair loop

If Codex finds issues, send exact repair instructions back to OpenCode. Repeat until Codex approves.

### Phase 6 — hard blocker escalation

Escalate to Claude only when:

- architecture is wrong
- bug cause is unclear after worker and Codex attempts
- tests fail in a confusing systemic way
- technology choice needs reassessment
- there is security/data-loss risk

Prompt Claude as advisor only:

```bash
/root/.local/bin/claude-architect -p 'Hard blocker. Do not code. Diagnose root cause and tell Codex/OpenCode the exact repair strategy, functions, tests, and technology choices.'
```

### Phase 7 — Hermes verification

Hermes verifies directly, not by trusting agent claims:

- read git diff
- run tests/builds
- inspect changed files
- confirm no secrets touched
- summarize in Arabic to Mohamed

## Strengths and weaknesses

### Claude Code

Strengths:

- Best architectural reasoning and phase design.
- Strong at hard debugging strategy.
- Good at tradeoffs and risk framing.
- Good for asking “what should the team do next?”

Weaknesses:

- Expensive tokens, especially Opus.
- Can over-engineer if allowed to implement.
- Too valuable for bulk edits.

### Codex

Strengths:

- Strong implementation supervision.
- Good at code-quality review and precise repair instructions.
- Good bridge between architecture and code changes.
- Works well with git and structured execution.

Weaknesses:

- `gpt-5.5` is still expensive.
- Can spend too much if asked to do all worker coding.
- Must stay at medium reasoning by default for quota control.

### OpenCode

Strengths:

- Cheapest practical implementation layer.
- Many model choices.
- Good for parallel workers and repetitive code edits.
- OpenCode Go models now verified working.

Weaknesses:

- Quality varies by model.
- Needs supervision on tricky edge cases.
- Worker outputs must be reviewed by Codex and verified by Hermes.

### Gemini CLI

Strengths:

- Useful large-context and Google ecosystem assistant after auth.
- Has skills, MCP, extensions, search grounding, and headless output.
- Good optional second opinion.

Weaknesses:

- Headless use currently blocked until auth is configured.
- Not part of the default coding chain until smoke-tested successfully.

## Decision rules

- New serious project: Claude architect first.
- Straight small bug: Codex supervisor may skip Claude unless the cause is unclear.
- Bulk implementation: OpenCode MiniMax.
- Cheap broad refactor: OpenCode DeepSeek Flash.
- Hard implementation but not architecture: OpenCode DeepSeek Pro, then Codex review.
- Review/fix instructions: Codex.
- Strategic confusion or repeated failure: Claude.
- Final truth: Hermes verification.

## Reference patterns

- See `references/product-project-bootstrap.md` for the validated pattern of turning Mohamed's product idea into a scoped repo bootstrap using Claude as architect, Codex as supervisor, OpenCode as worker, and Obsidian as durable project memory.
- See `references/coding-team-wrapper-contract.md` for the wrapper pattern that injects `/root/.hermes/coding-team/SENIOR_ENGINEERING.md` into Claude, Codex, and OpenCode without copying a full external skill pack into each tool.

## Budget / autonomy correction
## Budget / autonomy correction

Mohamed explicitly rejected an automatic usage-guard system that scheduled checks and rewrote model policy. Do not recreate cron-based consumption guards, adaptive policy files, or automatic model downgrades for this coding team unless Mohamed clearly asks for that mechanism again.

If Mohamed asks about costs or weekly package sufficiency, answer with a lightweight recommendation or manual check first. Keep the agreed fixed plan as default:

- Claude Code: architect only, Opus/high.
- Codex: supervisor, GPT-5.5/medium.
- OpenCode: implementation workers, MiniMax M3 default with DeepSeek Flash/Pro alternatives.

If an experimental guard or automation is rejected, remove the cron job, scripts, policy files, and skill references, then restore wrappers to the fixed plan.

## Anti-waste rules

- Do not ask Claude to write the whole codebase.
- Do not ask Codex to do bulk worker implementation unless quality risk is high.
- Do not trust OpenCode without Codex review on important code.
- Do not run multiple agents in the same workdir unless changes are read-only.
- Do not proceed to the next phase without tests or an explicit reason tests cannot run.
- Do not turn a monitoring idea into autonomous infrastructure without explicit approval.

## Company Dashboard specific rules

When working on the Company Dashboard project (`/root/Company-Dashboard`, remote `coolman1984/Company-Dashboard-Project`):

1. **Main-only branch** — Mohamed explicitly overrides AGENTS.md feature-branch rule for this repo. All work happens directly on `main`. No feature branches. Commit and push directly to origin/main.

2. **Verify task board from code** — the TASK_BOARD.md is often stale (Claude agents forget to update it). Before trusting any "Ready" or "Done" claim, grep the codebase for function names, API endpoints, and UI components. Update the board with verified commit hashes.

3. **Full test gate before every push** — run ALL of: `npm test`, `node test_i18n_coverage.js`, `python3 -m extractor.test_extractor`, `python3 test_db_schema.py`, `python3 test_map_raw_to_db.py`, `python3 -m reports.test_reports`, `python3 -m reports.test_render`, `python3 -m reports.test_scenario`, `python3 -m brain.test_brain`, `python3 -m brain.cli --check`, `python3 test_project_structure.py`, `python3 -m mcp_server.test_mcp`.

4. **Two-phase commit pattern** — when updating TASK_BOARD.md with commit hashes, commit code first, then commit the board update separately: `docs: Task Board — R<X> moved to Done`.

5. **Pull before working** — always `git pull origin main` first. Expect merge conflicts on high-churn files (server.js, app.js). Resolve by keeping the newer code and integrating the local change.

6. **New features go in the right layer** — see `ARCHITECTURE.md` for the 5-layer map. New code never lands at repo root.
