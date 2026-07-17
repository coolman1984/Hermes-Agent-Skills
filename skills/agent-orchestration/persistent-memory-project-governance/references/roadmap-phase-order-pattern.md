# Roadmap + Phase-Order Pattern

Use this pattern when a governed repo already exists and Mohamed asks for a rigorous next-steps plan.

## Goal
Turn architecture talk into executable order without drifting from live repo state.

## Required sequence
1. Verify the live baseline first.
   - current branch
   - test status
   - current next task in task queue
   - active bottleneck
2. Write or update `03_design/implementation_plan.md`.
3. Expand the active next task into bite-sized sub-tasks in `00_control/task_queue.md`.
4. Update `00_control/decisions.md` if branch policy, phase order, or governance handling changed.
5. Update `05_validation/issue_tracker.md` with real blockers and controlled risks.
6. Update `00_control/progress.md`, `run_log.md`, and `evidence_log.md` so the project tells one consistent story.

## What to include in the implementation plan
- verified baseline
- phase order
- why phase 1 is phase 1
- preconditions for later phases
- stop conditions
- risk table
- verification ladder
- recommended next action

## Sequencing doctrine
Prefer:
1. finish the visible user-management value already supported by the current core
2. validate one real workflow / real dataset
3. only then activate heavy infra
4. only later add deployment, enterprise search, and self-evolution

## Common failure to avoid
A roadmap file gets written, but task queue, issue tracker, and progress files still point at the old reality. That creates restart confusion and false momentum.
