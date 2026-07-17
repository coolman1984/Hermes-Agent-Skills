---
name: engineering-systems-architecture
description: "Use when engineering work involves requirements, components, data flow, trade-offs, ADRs, scalability. Provides senior baselines, traps, validation patterns, and focused references for this domain."
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [engineering, systems, architecture]
    related_skills: [engineering-mastery, reasoning-mastery]
---

# Systems Architecture

## Mission

Handle requirements, components, data flow, trade-offs, ADRs, scalability with senior discipline: frame first, inspect current context, implement/diagnose in small safe steps, verify with real evidence, and log reusable failures.

## When to Use

Use when the router selects this domain, or when the user's task directly mentions requirements, components, data flow, trade-offs, ADRs, scalability.


## Operating Baseline
- Start from requirements and constraints.
- Define components, boundaries, data ownership, and failure modes.
- Choose monolith/services/serverless by team and operational reality, not fashion.
- Capture trade-offs in ADRs.
- Design for observability and rollback.


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
