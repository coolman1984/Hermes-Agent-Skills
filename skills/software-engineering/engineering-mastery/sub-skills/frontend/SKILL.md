---
name: engineering-frontend
description: "Use when engineering work involves React, components, accessibility, data fetching, responsive UI. Provides senior baselines, traps, validation patterns, and focused references for this domain."
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [engineering, frontend]
    related_skills: [engineering-mastery, reasoning-mastery]
---

# Frontend Engineering

## Mission

Handle React, components, accessibility, data fetching, responsive UI with senior discipline: frame first, inspect current context, implement/diagnose in small safe steps, verify with real evidence, and log reusable failures.

## When to Use

Use when the router selects this domain, or when the user's task directly mentions React, components, accessibility, data fetching, responsive UI.


## Operating Baseline
- Semantic HTML first.
- Accessible names, keyboard states, ARIA only when semantic HTML cannot express it.
- Loading, empty, error, and success states.
- Keep data fetching separate from presentational rendering.
- Measure before performance work.


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
