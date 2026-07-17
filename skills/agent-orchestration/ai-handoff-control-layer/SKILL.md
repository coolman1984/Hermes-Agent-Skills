---
name: ai-handoff-control-layer
description: Build a robust handoff/control layer for future AI agents using a document-driven operating contract, machine-readable manifest, and validation script instead of brittle Python-only automation.
---

# AI Handoff Control Layer

Use this skill when you need to make a system easy and safe for future AI agents to operate, especially when later agents may be weaker at planning than the current one.

## When to use
- You are turning a project into an AI-operable system
- Future agents need a single canonical entrypoint
- You need to control weaker agents without fully disabling stronger ones
- You want consistent behavior across different models/providers
- You need to reduce drift between docs, files, and operating rules

## Core principle
Do **not** make the whole system rigid Python-only automation unless the task is purely mechanical.

Preferred architecture:
1. **Document-driven operating contract**
2. **Machine-readable manifest**
3. **Small validation script**
4. **Linked entrypoints inside the existing workspace/vault**

This gives:
- strong control for weaker agents
- flexibility for stronger agents
- lower breakage when tools/providers change
- better handling of ambiguous or judgment-heavy work

## Recommended file set
Create these core files:

Practical lesson from operating a real Egypt-equities system: a plain entrypoint + manifest + validator is good, but a separate session runbook makes weaker future agents much more reliable. Without it, they may know what the system is yet still fail to execute a trading session consistently.

### 1) AI-START-HERE.md
The canonical entrypoint. Must include:
- system identity and objective
- mandatory read order
- authoritative file priority
- source hierarchy
- tool priority
- skill priority
- command hints
- output schema
- edge cases
- limits on agent creativity / when to default to monitoring
- change protocol for updating the system safely

Practical lesson: include AI-START-HERE itself in the mandatory read order inside both the manifest and the handoff prompt. This sounds redundant, but it prevents weaker agents from following a stale shortened order in one file and a longer order in another.

### 2) AI-HANDOFF-PROMPT.md
A copy-paste prompt for handing the system to another AI. Keep it short, direct, and imperative.

### 3) ai_manifest.json
Machine-readable map of the system. Include:
- entrypoint
- mandatory_read_order
- authoritative_files_priority
- constraints / filters
- source hierarchy
- tools / skills priority
- known commands
- cron jobs or scheduled jobs if relevant
- required output fields
- edge-case policy
- change protocol
- control architecture note

Practical lesson: if you add a runbook, put it in both `mandatory_read_order` and `authoritative_files_priority`. Otherwise future agents may treat it like a nice-to-have note instead of an operational contract.

### 4) tools/validate_system.py
A validator should check more than file existence when the system is operationally important. Prefer checks for:
- manifest exists
- entrypoint exists
- mandatory files exist
- authoritative files exist
- AI-START-HERE read order matches the manifest exactly
- handoff prompt points to AI-START-HERE
- if a runbook exists, the handoff prompt and manifest both reference it
- key commands/binaries exist
- timezone/profile settings that affect automation are explicit
- scheduled jobs still match the intended skills and schedules
- current portfolio/watchlist/state files are internally coherent
- latest generated reports are not stale relative to current source files
- summary output in JSON

Practical lesson: if the system has cron jobs, validate local-time correctness explicitly (for example `Africa/Cairo`) or the scheduler may silently fire at the wrong hour after a profile rewrite.

Do not put investment judgment or business logic exclusively in this script. It is a validator, not the brain.

## Wiring the system
After creating the handoff layer, link it into the real workspace so future agents actually find it.

Update existing entry files such as:
- START-HERE.md
- VAULT-INDEX.md
- ACTIVE.md / project index
- system overview note
- main operating note

Add explicit language like:
- "If this task concerns X, open AI-START-HERE.md first"
- "After AI-START-HERE, open the session runbook before acting"

Practical lesson: weaker agents often stop after the identity/overview doc. A dedicated `SESSION-RUNBOOK.md` or equivalent should be linked as the next required step, not buried as a later reference.

## How to control weaker agents
Assume future agents may be worse at:
- prioritization
- distinguishing official vs historical docs
- handling ambiguity
- deciding when *not* to act

So explicitly encode:
- read order
- authoritative precedence
- default action when uncertain
- allowed sources
- required output sections
- when to avoid creativity
- when to say confidence is low

## How to preserve room for stronger agents
Do not over-script everything into rigid automation.

Allow stronger agents to:
- synthesize better conclusions
- improve docs
- refine the system
- use judgment in gray areas

But require them to:
- read the mandatory files first
- preserve the official hierarchy
- update official files when changing the system
- avoid keeping important improvements only in conversation memory

## Recommended edge cases section
Always document behavior for:
- missing avg_cost / incomplete portfolio basis
- source conflicts
- blocked/blank web pages
- unavailable web tools
- stale historical docs conflicting with current docs
- missing commands or broken cron state
- partial system updates
- generated reports that no longer match current source files after a portfolio/rules rewrite
- hidden intermediate layers (for example acceleration/tactical layers) being collapsed accidentally into generic hold/review buckets
- timezone drift causing scheduled jobs to fire at the wrong local hour
- a weekly or monthly cron job existing without its own dedicated skill/runbook, causing it to run with vague prompts and degraded consistency
- legacy prompts using outdated policy language after the main rules were updated

## Strong recommendation about Python
For decision-heavy systems, Python should be:
- a validator
- a checker
- a formatter
- a reporting helper
- a consistency enforcer

Python should **not** be the only operating layer when the workflow needs judgment.

Good rule:
- documents govern
- manifest maps
- validator checks
- AI reasons within bounds

## Verification checklist
Before you finish:
1. AI-START-HERE.md exists and is clear
2. AI-HANDOFF-PROMPT.md exists
3. ai_manifest.json exists and matches reality
4. validator runs successfully
5. workspace entry files link to AI-START-HERE.md
6. authoritative file hierarchy is explicit
7. edge cases are documented
8. future-agent behavior under uncertainty is explicit

## Example reusable outcome
A future AI should be able to enter cold and immediately answer:
- What is this system?
- What must I read first?
- Which files override older notes?
- What tools should I use?
- What do I output?
- What do I do if data is missing?
- When should I use scripts vs judgment?

If it cannot answer those questions quickly, the handoff layer is incomplete.