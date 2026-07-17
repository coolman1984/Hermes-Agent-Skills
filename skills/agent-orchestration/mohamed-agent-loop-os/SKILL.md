---
name: mohamed-agent-loop-os
description: Use when Mohamed wants a serious multi-agent workflow, a long-running coding/research loop, background workers, factory-style processing, or any task that must survive beyond one clever prompt. Turns the task into a durable planner-generator-evaluator operating loop with file-backed state, explicit success contracts, restart tolerance, and profile-based execution.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  tags: [agent-loop, multi-agent, planner-generator-evaluator, durable-state, long-running, profiles, verification, mohamed]
  related_skills: [mohamed-coding-team, mohamed-opencode-go-worker-profiles, ai-coding-cli-delegation, senior-software-engineer]
---

# Mohamed Agent Loop OS

## Core belief

Do not treat the agent as a chat.

Treat it as a worker inside an operating loop.

The model is rarely the main failure point.
The surrounding loop is.

Default doctrine:

- short loops
- simple state
- explicit contracts
- independent evaluation
- restart tolerance
- raw trace reading
- delete scaffolding when it becomes dead weight

This skill is Mohamed's permanent default for serious agentic work.

For any coding, architecture, refactor, debugging, review, CI, or production-readiness workflow inside this loop, also load:

`senior-software-engineer`

Treat `senior-software-engineer` as the quality and engineering discipline layer, and treat this skill as the orchestration and durability layer. They are paired by default, not optional cousins.

## When to load this skill

Load this skill whenever the task is any of the following:

- a multi-agent workflow
- a long-running coding or research task
- a background worker setup
- a factory workflow over many files
- a project that may run for hours or days
- a system where correctness matters more than chat fluency
- any workflow that would be fragile if it depended on conversation memory alone

If the task is trivial, do not force the full loop.
But if the task has real complexity, load this skill before acting.

## 2026-06-30 audit correction

The first version of this skill captured the spirit, but it was too easy to overbuild the loop.
Karpathy's stronger lesson is not “add many files”. It is:

- keep loops short
- keep state simple
- write contracts clearly
- delete scaffolding when it stops paying rent

Use loop levels:

| Level | Use for | State |
|---|---|---|
| 0 | trivial one-shot | no loop; verify directly |
| 1 | medium task that may resume later | 3-file loop |
| 2 | serious multi-agent, data, report, or project governance work | governed file OS via `persistent-memory-project-governance` |
| 3 | durable autonomous runner | only after Level 2 proves stable |

Default to Level 1 before Level 2 unless complexity clearly justifies the full project OS.
Do not turn every idea into infrastructure.

When the task needs formal project governance, raw-file protection, data contracts, evidence logs, handover notes, or restart by another agent, load:

`persistent-memory-project-governance`

## Non-negotiable operating rules

### 1. Write the loop, not just the prompt

Never rely on one brilliant prompt.
Build the loop:

1. gather context
2. define success
3. plan
4. generate
5. evaluate
6. repair or restart
7. verify
8. log outcome

The loop is the system.
The prompt is only one component.

### 2. Separate the roles

Always split the work into distinct roles:

- planner
- generator
- evaluator
- Hermes as orchestrator and final verifier

The generator must not be trusted to judge itself.
If one worker writes and also approves, quality drifts.

### 3. Negotiate the contract before execution

Before generation begins, define what success means in testable terms.
The evaluator should challenge the contract until it becomes concrete.

Contract protocol:

1. Planner drafts the contract.
2. Evaluator challenges it before any generation starts.
3. Hermes revises the contract file.
4. Generator starts only after the evaluator marks the contract testable.
5. Any material contract change mid-run triggers a restart review.

The generator does not get to define “done” after it has already built the thing.

Bad:

- make it good
- improve the app
- create a nice dashboard

Good:

- list exact acceptance criteria
- define edge cases
- define tests or checks
- define output files and required fields
- define stop conditions
- define non-goals
- define failure conditions

For a small app, fewer than ~15 criteria is suspiciously thin. Around 20–30 criteria can be normal if the task has UI, data, errors, and verification.

If success is vague, the loop is fake.

### 4. Put truth in files, not in chat memory

Conversation memory is helpful, not authoritative.
Authoritative state must live in files.

Use the 3-file survival test first. A worker should be able to lose the session, read three files, and continue:

```text
.agent-loop/brief-contract.md
.agent-loop/progress.md
.agent-loop/run-log.md
```

If those three files cannot summarize the task, the task may be too complex or the state is poorly designed.

Use the full folder only when needed by adding supplemental files:

```text
.agent-loop/evaluator-findings.md
.agent-loop/quality-rubric.md
.agent-loop/scaffolding-review.md
.agent-loop/bottleneck-log.md
```

Optional files:

```text
.agent-loop/restart-notes.md
.agent-loop/decision-log.md
.agent-loop/inputs.md
.agent-loop/output-spec.md
```

Any worker should be able to lose its session, read the state files, and continue.

### 5. Allow restart instead of endless patching

If the evaluator keeps finding structural problems, allow the generator to restart from a cleaner base.
Do not defend a broken implementation just because time was spent on it.

Patch when the structure is sound.
Restart when the structure is rotten.

### 6. Score subjective quality explicitly

When the work includes design, writing, dashboards, UX, or presentation quality, define weighted scoring dimensions.

Default subjective scoring protocol:

1. Pick 3–5 dimensions.
2. Assign weights that sum to 1.0.
3. Give the evaluator 2–3 good references and 2–3 bad references when available.
4. Score each dimension from 0.0 to 1.0.
5. Write one paragraph explaining the gap.
6. Set a pass threshold before generation starts.

Useful dimensions:

- function
- clarity
- craft
- originality
- trustworthiness
- design fit
- evidence quality

Do not say “make it more professional” without defining what professional means here.

### 7. Read traces, not vibes

When a run fails, inspect the raw trace or log.
Find the exact point where the worker's judgment diverged from Hermes' judgment.
Repair that point.

Every meaningful worker run should leave a trace in `run-log.md`:

- worker/profile used
- prompt or task brief path
- files read
- files changed or outputs produced
- command/test result
- evaluator decision
- exact divergence point if the run failed

Do not improve the system by intuition alone.
Use evidence from the run.

### 8. Delete obsolete scaffolding

When a newer model can reliably do something without extra ceremony, remove the old scaffolding.
A support structure that once helped can become drag.

Review all auxiliary rules periodically and after major model changes:

- Is this still necessary?
- Does it improve reliability?
- Is it now blocking a better model behavior?
- Can this be collapsed from full loop to 3-file loop?
- Can this be deleted instead of patched again?

Write the decision to `scaffolding-review.md` when the system itself changes.

If not useful, remove it.

### 9. Assume the bottleneck will move

Once coding improves, planning becomes the bottleneck.
Once planning improves, evaluation becomes the bottleneck.
Once evaluation improves, taste or prioritization becomes the bottleneck.

Track the current bottleneck explicitly:

```text
.agent-loop/bottleneck-log.md
```

Record:

- current bottleneck
- evidence
- fix attempted
- whether the bottleneck moved
- next smaller system to ship

The loop exists to expose the next bottleneck.
Then fix it.

## Default role mapping for Mohamed's worker team

Use these defaults unless the task suggests a better split.

### Planner

Prefer:

- `deepseek-pro`
- or Claude architect when architecture quality is critical

Planner responsibilities:

- turn vague intent into a concrete brief
- define scope and phases
- draft the first contract
- identify files, tools, risks, and stop conditions

Planner must not write bulk implementation.

### Generator

Prefer:

- `minimax-go` for economical bulk work
- `kimi-code` for code-heavy structured work
- `deepseek-fast` for fast first-pass generation

Generator responsibilities:

- implement the current slice only
- update progress files
- never self-approve
- explicitly note uncertainty and restart proposals

### Evaluator

Prefer:

- Codex supervisor for engineering evaluation
- `deepseek-pro` for reasoning critique
- Hermes for final verification and acceptance

Evaluator responsibilities:

- challenge the contract
- inspect diffs and outputs
- run checks when possible
- score against criteria
- decide pass, repair, or restart

### Hermes

Hermes always remains:

- orchestrator
- state keeper
- verifier
- Arabic reporter
- final accountability layer

Never hand that ownership away.

## Standard execution template

Use the included templates when creating real project state:

```text
templates/brief-contract.md
templates/progress.md
templates/run-log.md
templates/evaluator-findings.md
templates/quality-rubric.md
templates/scaffolding-review.md
templates/bottleneck-log.md
```

Bootstrap quickly with:

```bash
python scripts/bootstrap_agent_loop.py /path/to/project --level minimal
python scripts/bootstrap_agent_loop.py /path/to/project --level full
```

Use `minimal` first unless the work clearly needs full multi-agent state.

### Phase 0 — classify

Classify the request:

- execute now
- attach to an existing project
- research first
- save as idea
- reject or park

### Phase 1 — establish state

Pick the smallest useful state level.

Level 1 default:

```text
.agent-loop/brief-contract.md
.agent-loop/progress.md
.agent-loop/run-log.md
```

Level 2 add only when needed:

```text
.agent-loop/evaluator-findings.md
.agent-loop/quality-rubric.md
.agent-loop/scaffolding-review.md
.agent-loop/bottleneck-log.md
```

Minimum contents:

- objective
- scope boundaries
- acceptance criteria
- worker roles
- files/paths
- allowed tools
- forbidden actions
- verification method
- stop/restart conditions

### Phase 2 — planner pass

Planner converts the vague ask into:

- brief
- contract
- sequence of slices
- test strategy
- risk list

### Phase 3 — evaluator challenge

Evaluator reviews the proposed contract before generation starts.
If the contract is weak, revise it now.
Do not wait until after coding.

### Phase 4 — generation loop

For each slice:

1. generator executes
2. generator updates `progress.md`
3. evaluator reviews output
4. Hermes verifies evidence
5. mark pass, repair, or restart

### Phase 5 — restart logic

Trigger restart when any of these are true:

- repeated patch attempts keep failing
- the contract changed materially
- the implementation direction is structurally wrong
- files became inconsistent beyond cheap repair

On restart, write why to:

```text
.agent-loop/restart-notes.md
```

### Phase 6 — final verification

Before saying done:

- re-read outputs
- run tests/checks
- verify files exist
- verify required fields and format
- confirm the contract was met
- write final status into `run-log.md`

## File-backed state contract

Use compact, boring files.
Do not build ornate memory systems before they are needed.

Recommended file purposes:

### `brief-contract.md`

- what Mohamed wants
- why it matters
- scope and non-goals
- roles
- acceptance criteria
- failure conditions
- stop/restart conditions
- verification method
- evaluator contract decision

### `progress.md`

- loop level
- current slice
- completed slices
- blocker
- next action
- repair/restart decision
- last verified evidence

### `run-log.md`

- timestamps
- worker/profile used
- role
- task brief path
- files read
- files changed or outputs produced
- command/check result
- evaluator decision
- divergence point

### `evaluator-findings.md`

- contract challenge before generation
- findings by severity
- evidence
- required repair
- pass/repair/restart/stop decision

### `quality-rubric.md`

- good and bad references
- weighted criteria
- score from 0.0 to 1.0
- pass threshold
- gap explanation

### `scaffolding-review.md`

- helper/scaffold under review
- why it was added
- evidence it helps or hurts
- keep/simplify/delete decision

### `bottleneck-log.md`

- current bottleneck
- evidence
- fix attempted
- whether the bottleneck moved
- next smaller system to ship

## Anti-patterns

Never do these on serious tasks:

- one huge prompt with no state files
- generator self-approval
- vague “looks good” evaluation
- relying on chat memory as ground truth
- endless patching when restart is cheaper
- adding helper machinery forever without cleanup
- trusting worker claims without verification

## Mohamed-specific standing rule

For Mohamed's serious agent systems, the default is not:

- single agent
- single prompt
- pure chat memory

The default is:

- planner + generator + evaluator
- file-backed state
- contract before execution
- logs after execution
- restart tolerance
- Hermes verification
- worker profiles selected intentionally

## Quick routing guide

| Task shape | Planner | Generator | Evaluator |
|---|---|---|---|
| hard coding architecture | Claude architect or `deepseek-pro` | `kimi-code` or `minimax-go` | Codex + Hermes |
| large mechanical coding | `deepseek-fast` | `minimax-go` | Codex + Hermes |
| research synthesis | `deepseek-pro` | `deepseek-fast` | Hermes |
| design/output quality | `deepseek-pro` | `minimax-go` or local build worker | evaluator with weighted quality rubric + Hermes |
| long factory run over many files | `deepseek-pro` | `minimax-go` | `deepseek-pro` + Hermes |

## Maintenance rule

When auditing this skill against Karpathy's long-running-agent notes, also read:

`references/2026-06-30-agent-loop-audit.md`

Whenever a real task reveals a missing step, a weak contract pattern, a restart trigger, a profile-routing lesson, or unnecessary ceremony, patch this skill immediately.

This skill is living operational doctrine, not documentation theater.
