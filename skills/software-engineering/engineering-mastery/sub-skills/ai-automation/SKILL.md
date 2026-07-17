---
name: engineering-ai-automation
description: "Use when engineering work involves LLMs, RAG, tool calling, agents, evals, scripts, cron, CI/CD. Provides senior baselines, traps, validation patterns, and focused references for this domain."
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [engineering, ai, automation]
    related_skills: [engineering-mastery, reasoning-mastery]
---

# AI and Automation

## Mission

Handle LLMs, RAG, tool calling, agents, evals, scripts, cron, CI/CD with senior discipline: frame first, inspect current context, implement/diagnose in small safe steps, verify with real evidence, and log reusable failures.

## When to Use

Use when the router selects this domain, or when the user's task directly mentions LLMs, RAG, tool calling, agents, evals, scripts, cron, CI/CD.


## Operating Baseline
- Ask whether an LLM is necessary.
- Define task, input, output schema, evaluation, guardrails, cost/latency.
- Keep humans in the loop for money, reputation, deletion, or irreversible actions.
- Automate stable repetitive workflows only after validation rules exist.
- Log and evaluate failures.


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
