---
name: engineering-mastery
description: "Use for ANY coding, software, web, backend, frontend, UI/UX, design, IT/hardware, troubleshooting, networking, system architecture, AI/LLM, or automation task — from writing one function to designing a system or diagnosing why something will not connect. Routes to the right engineering sub-skill; consult reasoning-mastery first for framing."
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [engineering, full-stack, backend, frontend, networking, architecture, ai-automation, troubleshooting]
    related_skills: [reasoning-mastery, senior-software-engineer, systematic-debugging, database-mastery]
---

# Engineering Mastery Router

## Mission

Route technical work to the right engineering discipline and enforce senior baselines: frame first, verify versions, write tested code, secure boundaries, readable design, and real validation before claiming done.

## Mandatory Start

1. Consult `reasoning-mastery` for any non-trivial task: intent, success criteria, assumptions, risks.
2. Pick the sub-skill by the task shape below.
3. Check current versions/docs for APIs, libraries, frameworks, devices, or protocols.
4. Build the smallest working slice; verify with real commands.
5. Log reusable bugs in this router or the relevant sub-skill `ERRORS.md`.

## Iron Rules

- Frame the real problem before building.
- Working, tested code only; never save an unrun snippet as a reference.
- Security, validation, error handling, and secrets hygiene are baseline.
- Prefer readable, maintainable code over cleverness.
- Version-specific details must be verified, not remembered.
- Architecture decisions need an ADR when trade-offs matter.
- Optimize only after measuring.
- Do not automate chaos; stabilize the rule and validation first.

## Router

| Task signal | Sub-skill | Default move |
|---|---|---|
| Function, refactor, tests, Git, code review | `sub-skills/software-foundations` | clarify behavior, test, refactor safely |
| API, auth, DB boundary, jobs, websocket | `sub-skills/backend` | contract, validation, auth, pagination, errors |
| React/Next/component/data UI | `sub-skills/frontend` | accessibility, loading/error/empty states, responsiveness |
| Interface look/feel, usability, flows | `sub-skills/ui-ux-design` | hierarchy, contrast, spacing, feedback, WCAG |
| PC/server fault, boot, OS support | `sub-skills/hardware-support` | reproduce, isolate layer, test one variable |
| DNS/TCP/ports/TLS/proxy/connectivity | `sub-skills/networking` | layer-by-layer diagnostics |
| System design, scalability, ADR | `sub-skills/systems-architecture` | requirements, components, data flow, trade-offs |
| LLM/RAG/agents/cron/automation | `sub-skills/ai-automation` | eval, guardrails, human gate, cost/latency |

## Suite Map

- `references/resources-and-leads.md` — master source map.
- Each sub-skill has `SKILL.md`, `ERRORS.md`, `references/`, and optional `scripts/` or `templates/`.
- `references/validation-results.md` records the 8-domain validation suite.

## Completion Checklist

- [ ] Reasoning frame done.
- [ ] Correct sub-skill selected.
- [ ] Official docs/specs checked where version-sensitive.
- [ ] Code or diagnosis verified with real output.
- [ ] Security and failure cases considered.
- [ ] ADR written for non-trivial architecture.
- [ ] Reusable lesson logged.
