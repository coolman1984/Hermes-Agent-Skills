---
name: engineering-software-foundations
description: "Use when engineering work involves clean-code, testing, Git, debugging, refactoring, DSA. Provides senior baselines, traps, validation patterns, and focused references for this domain."
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [engineering, software, foundations]
    related_skills: [engineering-mastery, reasoning-mastery]
---

# Software Foundations

## Mission

Handle clean-code, testing, Git, debugging, refactoring, DSA with senior discipline: frame first, inspect current context, implement/diagnose in small safe steps, verify with real evidence, and log reusable failures.

## When to Use

Use when the router selects this domain, or when the user's task directly mentions clean-code, testing, Git, debugging, refactoring, DSA.


## Operating Baseline
- Define behavior before refactor.
- Add/keep tests around changed behavior.
- Prefer clear names, small functions, simple data structures.
- Use Git history tools: diff, bisect, blame, worktree, rebase carefully.
- Complexity matters when input size or hot path makes it matter; otherwise clarity wins.


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
