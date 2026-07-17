# Senior Engineering Integration Contract

This reference makes the integration explicit between:

- `mohamed-agent-loop-os`
- `senior-software-engineer`
- `mohamed-coding-team`
- `mohamed-opencode-go-worker-profiles`

## Rule

For Mohamed's serious software work, these are not separate styles.
They are one stack.

### Layer 1 — Engineering discipline

Load:

`senior-software-engineer`

Purpose:

- inspect context first
- preserve scope
- build in small slices
- verify with real commands
- review security, performance, readability, and architecture
- never claim success without evidence

### Layer 2 — Durable loop orchestration

Load:

`mohamed-agent-loop-os`

Purpose:

- planner / generator / evaluator separation
- explicit success contract before execution
- file-backed state in `.agent-loop/`
- repair vs restart decision
- raw trace reading
- bottleneck detection

### Layer 3 — Worker-team routing

Load when using external workers or multi-model execution:

`mohamed-coding-team`

Purpose:

- choose who plans
- choose who implements
- choose who reviews
- prevent role confusion
- keep Hermes as accountable orchestrator

### Layer 4 — Profile routing

Load when using Mohamed's OpenCode Go workers:

`mohamed-opencode-go-worker-profiles`

Purpose:

- choose the right worker profile
- dispatch self-contained prompts
- verify worker outputs
- keep Telegram-facing orchestration clean

## Default integrated stack

### Coding or architecture task

Load in this order:

1. `senior-software-engineer`
2. `mohamed-agent-loop-os`
3. `mohamed-coding-team`
4. `mohamed-opencode-go-worker-profiles` when worker profiles are involved

## Operational meaning

- `senior-software-engineer` answers: how should engineering work be done well?
- `mohamed-agent-loop-os` answers: how should the work persist, loop, restart, and be evaluated?
- `mohamed-coding-team` answers: which worker does which role?
- `mohamed-opencode-go-worker-profiles` answers: which profile/model should execute?

## Non-negotiable behavior

If the task changes files, code, architecture, tests, CI, or production readiness:

- do not use worker profiles without engineering discipline
- do not use engineering discipline without loop structure on serious tasks
- do not let generator and evaluator collapse into one unchecked worker
- do not treat chat memory as project state

## Minimum file state for serious coding loops

Prefer the 3-file survival loop first:

- `.agent-loop/brief-contract.md`
- `.agent-loop/progress.md`
- `.agent-loop/run-log.md`

Escalate to the full loop only when complexity requires it:

- `.agent-loop/evaluator-findings.md`
- `.agent-loop/quality-rubric.md`
- `.agent-loop/scaffolding-review.md`
- `.agent-loop/bottleneck-log.md`

The full loop is not a badge of seriousness. It is a cost that must earn its place.

## Final contract

Mohamed's integrated default for serious software work is:

- senior engineering discipline
- durable planner / generator / evaluator loop
- explicit worker routing
- profile-based execution when useful
- Hermes verification at the end
