---
name: ai-agent-adoption-review
description: Evaluate whether a third-party AI agent/project is worth adopting into
  the local stack by checking live site claims, GitHub maturity, code structure, safety
  controls, and fit with existing infrastructure.
tags: [evaluation, ai-agents, adoption, tools, review]
---

# AI Agent Adoption Review

Use this skill when a user asks whether a third-party AI agent, CLI, or orchestration project is worth installing, replacing, or copying into the local system.

## When to use
- User shares a product URL and asks if it is worth adopting
- User wants a quick but grounded verdict on a new agent/tool
- You need to compare a new agent against the current stack
- The project is new, hype-heavy, or claims broad capabilities

## Goal
Return a practical recommendation:
- **Adopt now**
- **Try in a sandbox**
- **Use as reference only**
- **Skip**

Do not judge only by marketing. Check the source, code, maintenance, and operational fit.

## Workflow

### 1) Inspect the live site first
Collect:
- product name and positioning
- stated capabilities
- supported platforms/channels
- safety and permission model
- install path
- provider/model support
- any claim about always-on or daemon mode

Look for obvious red flags:
- vague marketing with no code or docs
- claims that duplicate existing stack features without clear differentiation
- setup that depends on brittle or opaque external services

### 2) Inspect the GitHub repo or source
Check:
- stars, forks, contributors, open issues
- creation date and recent update date
- release count and latest release date
- license
- repo structure
- package manager / language
- test files and CI signals
- whether docs and architecture notes exist

Helpful signals:
- recent commits and releases
- tests present
- clear build and run scripts
- separate capabilities/modules
- explicit permission and approval controls
- source code matches the website claims

### 3) Check implementation depth
Look for real evidence of production readiness:
- permission hardening or command blocklists
- scoped file access
- approval flows
- memory model
- scheduling / daemon support
- provider abstraction
- error handling and tests
- channel isolation if it supports messaging

Signs it may be thin:
- mostly landing-page copy
- tiny codebase with many unsupported claims
- no tests, no docs, no architecture notes
- no obvious hardening around shell or file operations

### 4) Compare against the existing stack
Ask:
- Does it solve a real gap?
- Does it duplicate what we already have?
- Does it improve safety, reliability, or maintainability?
- Would adoption increase operational complexity?
- Is it a better base, or just a parallel experiment?

Prefer:
- keep the current system if the new tool is mostly overlapping
- sandbox first if it is promising but immature
- adopt only if it clearly outperforms current stack in a core area

### 5) Decide with a simple rubric
Use this quick rubric:
- **Adopt now**: mature, maintained, safe, clearly better, low integration risk
- **Try in a sandbox**: promising, active, but young or overlapping
- **Reference only**: useful ideas, but not production-grade or not differentiated
- **Skip**: hype-heavy, thin, stale, or risky

### 6) Report clearly
Give the user:
- one-line verdict
- why
- strongest evidence for and against
- whether it should be installed, cloned, or ignored
- any follow-up if they want a deeper audit

## Common pitfalls
- Trusting stars alone
- Trusting a polished landing page without checking the repo
- Confusing “many features listed” with “those features are implemented well”
- Ignoring license or operational fit
- Recommending replacement when a side-by-side sandbox would be safer

## Output style
Be direct.
- If it is good but not necessary: say so plainly
- If it is not worth the switch: say that plainly
- If it is worth copying ideas from: name the ideas, not the whole tool

## Useful evidence checklist
- site claims verified in code
- repo age and release activity
- tests present
- hardening in shell/file permissions
- provider abstraction
- docs and architecture notes
- alignment with current workflows
- net benefit vs added complexity
