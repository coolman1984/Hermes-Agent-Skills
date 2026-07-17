---
name: engineering-hardware-support
description: "Use when engineering work involves PC/server hardware, OS faults, boot, logs, recovery. Provides senior baselines, traps, validation patterns, and focused references for this domain."
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [engineering, hardware, support]
    related_skills: [engineering-mastery, reasoning-mastery]
---

# Hardware and Technical Support

## Mission

Handle PC/server hardware, OS faults, boot, logs, recovery with senior discipline: frame first, inspect current context, implement/diagnose in small safe steps, verify with real evidence, and log reusable failures.

## When to Use

Use when the router selects this domain, or when the user's task directly mentions PC/server hardware, OS faults, boot, logs, recovery.


## Operating Baseline
- Reproduce and classify layer: power, POST, firmware, storage, OS, driver, app.
- Test one variable at a time.
- Prefer non-destructive diagnostics first.
- Preserve data before risky repair.
- Logs before guesses: dmesg, journalctl, Event Viewer, SMART.


## Workflow

1. Frame intent and success criteria.
2. Inspect existing system/docs/version.
3. Select smallest safe action.
4. Execute and verify.
5. Review security, correctness, maintainability, and failure modes.
6. Update `ERRORS.md` if a reusable issue appears.

## Common Pitfalls

See `references/baseline.md` for top traps and example patterns.

## Verification Checklist

- [ ] Problem framed.
- [ ] Current version/context checked.
- [ ] Failure cases considered.
- [ ] Runnable example/diagnosis verified.
- [ ] Result recorded in validation evidence when applicable.
