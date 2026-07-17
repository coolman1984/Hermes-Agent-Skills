---
name: engineering-backend
description: "Use when engineering work involves APIs, FastAPI, auth, validation, pagination, queues, reliability. Provides senior baselines, traps, validation patterns, and focused references for this domain."
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [engineering, backend]
    related_skills: [engineering-mastery, reasoning-mastery]
---

# Backend Engineering

## Mission

Handle APIs, FastAPI, auth, validation, pagination, queues, reliability with senior discipline: frame first, inspect current context, implement/diagnose in small safe steps, verify with real evidence, and log reusable failures.

## When to Use

Use when the router selects this domain, or when the user's task directly mentions APIs, FastAPI, auth, validation, pagination, queues, reliability.


## Operating Baseline
- Design contract first: resources, status codes, idempotency, pagination.
- Validate request inputs and response shape.
- Auth/authz before data access.
- Parameterize database queries.
- Log errors without leaking secrets.
- Add pagination and rate limiting for list endpoints.


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
