---
name: engineering-ui-ux-design
description: "Use when engineering work involves hierarchy, spacing, typography, flows, accessibility, heuristics. Provides senior baselines, traps, validation patterns, and focused references for this domain."
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [engineering, ui, ux, design]
    related_skills: [engineering-mastery, reasoning-mastery]
---

# UI/UX Design

## Mission

Handle hierarchy, spacing, typography, flows, accessibility, heuristics with senior discipline: frame first, inspect current context, implement/diagnose in small safe steps, verify with real evidence, and log reusable failures.

## When to Use

Use when the router selects this domain, or when the user's task directly mentions hierarchy, spacing, typography, flows, accessibility, heuristics.


## Operating Baseline
- Define user task and information hierarchy.
- Use contrast, spacing, alignment, grouping, and feedback deliberately.
- Design empty, loading, error, and success states.
- Check accessibility and cognitive load.
- Justify changes by named principles, not taste.


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
