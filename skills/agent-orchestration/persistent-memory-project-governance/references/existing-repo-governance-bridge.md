# Existing Repo Governance Bridge

## When to use

Use this pattern when Mohamed asks to download or start developing inside a repository that already contains its own file-based project operating system.

Typical signals:

- `00_control/*` already exists
- restart notes, evidence logs, task queues, or memory files already exist
- the repo's `AGENTS.md` or master plan defines its own governance rules

## Goal

Start working immediately without creating a second competing operating system.

## Recommended sequence

1. Clone the repo locally.
2. Inspect the existing governance files before writing anything new.
3. Treat the existing system as authoritative if it is coherent and active.
4. Add only a lightweight bridge if Mohamed's workflow needs a fast restart surface.
5. Update stale state references so the repo has one consistent "next action".
6. Record the takeover in the project's own run log and evidence log.

## Minimal bridge

```text
.agent-loop/brief-contract.md
.agent-loop/progress.md
.agent-loop/run-log.md
```

The bridge should say explicitly that:

- `00_control/*` remains the source of truth
- `.agent-loop/*` is a restart convenience layer only
- the current next action is aligned with the governed state

## What to fix during takeover

- stale next-step references
- restart notes that point to already-finished work
- memory summaries that no longer match the task queue
- missing evidence entry for the local clone / bridge setup

## What not to do

- do not regenerate a full second governance tree
- do not overwrite existing control files blindly
- do not leave two different task systems disagreeing about the next action

## Example outcome

A repo with `00_control/*` keeps its existing project OS, while `.agent-loop/*` gives Mohamed's agent loop a compact restart surface for the next coding task.