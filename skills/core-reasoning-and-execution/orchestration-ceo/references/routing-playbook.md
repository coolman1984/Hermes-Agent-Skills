# Routing Playbook

## Default decision tree

### 1) Is the task simple and fully specified?
- Yes -> execute directly.
- No -> continue.

### 2) Does it require planning, sequencing, or tradeoffs?
- Yes -> strategy mode.

### 3) Does it need one specialist to own a domain subtask?
- Yes -> delegate.

### 4) Does it need inspection, testing, or bug-finding?
- Yes -> review mode.

### 5) Did it fail, drift, or stall?
- Yes -> recovery mode.

### 6) Is the user repeating a pattern?
- Yes -> build a reusable tool, checklist, or skill.

## Specialist mapping
- Use `architect` for strategy, architecture, and planning.
- Use `developer` for implementation, code, and technical fixes.
- Use `reviewer-qa` for review mode.
- Use `operations-cleanup` for optimization and cleanup mode.
- Use `builder` when a setup/config/script-heavy implementation path is the best fit.
- Use `researcher` for evidence gathering and tradeoff analysis.
- Use `free-search` for zero-key web search and page extraction when `ddgr`/`trafilatura` are available in the environment.
- Use `web-search-free` for zero-key web search and cross-validation before raw `web_search` or `web_fetch` **when a `mcporter` backend is actually configured**; otherwise fall back to `tavily` or the raw web tools.
- Use `phone-control` for full Android UI control via ADB self-connect.
- Use `mobilerun` for managed Android UI control, screenshots, UI trees, taps, swipes, and app automation.
- Use `termux-api` for Android hardware access, sensor data, notifications, clipboard, camera, and other device-native actions.

## CEO control policy
- Do not become a passive relay between agents.
- Do not delegate everything automatically.
- Do not produce long managerial talk with no action.
- Do not lose track of the original mission.
- Do not approve weak specialist output without review.
- Do not create unnecessary process for simple work.
- Make decisions.
- Keep ownership.
- Intervene when specialist output is weak.
- Compress outputs into one coherent result.
- Keep the system moving forward.

## Delegation package template

Use this exact structure:

```text
SPECIALIST:
[builder / researcher / reviewer / operations / other]

OBJECTIVE:
[one clear task only]

WHY THIS SPECIALIST:
[why this routing decision is correct]

CONTEXT:
[only the most relevant context]

CONSTRAINTS:
- [constraint]
- [constraint]
- [constraint]

DO NOT:
- [important prohibition]
- [important prohibition]

EXPECTED OUTPUT:
[exact output shape required]

SUCCESS CRITERIA:
- [criterion]
- [criterion]
- [criterion]

STOP CONDITION:
[when to stop, escalate, or return]
```

## Checkpoint template
- What was attempted?
- What changed?
- What is blocked?
- What is the next check?

## When waiting
- Set a heartbeat.
- Re-check every 2 minutes for pending work.
- Notify immediately on completion.

## When done
- Verify output.
- Merge into one coherent answer.
- Update memory if it matters.

## Status labels
Use these exact labels in task updates:
- PLANNING
- EXECUTING
- WAITING
- BLOCKED
- REVIEWING
- COMPLETE

## Complete-task closure
When a task is COMPLETE, end with:
- Result
- Why this is complete
- Best next action

## Common operating policy
For each task:
1. Identify the real objective.
2. Classify the task type and mode.
3. Decide whether to answer directly, execute directly, delegate, split into phases, review first, or recover.
4. Take the highest-leverage next action.
5. Review output quality.
6. Report current status and next action.

## Status labels
Use one of:
- PLANNING
- EXECUTING
- DELEGATING
- REVIEWING
- WAITING
- BLOCKED
- COMPLETE

## Response shape for non-trivial tasks
- Objective
- Approach
- Execution
- Risks or blockers
- Status
- Next action

## Memory write policy

- Long-term memory path is exactly `~/.openclaw/workspace/MEMORY.md`
- Daily memory path is exactly `~/.openclaw/workspace/memory/YYYY-MM-DD.md`
- Never write to `~/.openclaw/workspace/memory/MEMORY.md`
- Before writing, verify parent directory and target file exist
- If missing, create them first
- If editing `MEMORY.md` fails, append the content to today’s daily log and report the failure with the exact path and reason
- Keep `MEMORY.md` concise; store project details in `workspace/projects/*.md`

## Compaction buffer

- Set `agents.defaults.compaction.reserveTokensFloor` to `20000` or higher in config to leave room for output and reduce context-limit resets.

## Memory write preflight

Before any memory write:
1. Check `~/.openclaw/workspace` exists and is writable.
2. Check `~/.openclaw/workspace/MEMORY.md` exists; create it if missing.
3. Check `~/.openclaw/workspace/memory/` exists; create it if missing.
4. Check `~/.openclaw/workspace/memory/YYYY-MM-DD.md` exists; create it if missing.
5. If `MEMORY.md` write fails, append the same content to today’s daily log and report the exact path and reason.

## Startup preflight

Prefer the PATH-level wrapper so `openclaw gateway start` preflights automatically.
It lives at `~/.local/bin/openclaw`, and shells should prepend `~/.local/bin` to `PATH`.

If you want to launch explicitly, use:

```bash
./skills/orchestration-ceo/scripts/openclaw-start-with-memory-preflight.sh
```

## Skill package install

Use the one-shot installer to install every packaged skill from `dist/` into
`~/.openclaw/skills` and refresh the capability registry automatically:

```bash
openclaw-install-skills
```

To install from another package directory or into another target root, pass the
paths directly to `./skills/orchestration-ceo/scripts/install-all-skills.sh`:

```bash
./skills/orchestration-ceo/scripts/install-all-skills.sh <dist-dir> <target-root>
```

That script installs all `.skill` archives, then runs the capability sync
refresh so the registry reflects the new packaged workflow.

If you launch OpenClaw another way, run `./skills/orchestration-ceo/scripts/ensure-memory-paths.sh` first.
If either step fails, fix the workspace path or permissions before launching the gateway.
