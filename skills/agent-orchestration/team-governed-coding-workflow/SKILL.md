---
name: team-governed-coding-workflow
description: "Use for Mohamed's serious coding/project work when execution must flow through a fixed team: Hermes plans/orchestrates/final-verifies, deepseek-fast writes only, deepseek-pro reviews only."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [team-workflow, coding, orchestration, review, mohamed]
    related_skills: [mohamed-coding-team, mohamed-opencode-go-worker-profiles, senior-software-engineer, mohamed-agent-loop-os]
---

# Team-Governed Coding Workflow

## When to use

Use this skill for Mohamed's serious coding, architecture, refactoring, debugging, or project-governance work when the work should not be done as a solo agent pass.

Trigger especially when Mohamed says or implies any of the following:
- use the team
- do not forget the programmers
- Flash writes, Pro reviews
- continue the project with the system
- run the coding team

## Non-negotiable team roles

This workflow has a fixed separation of roles:

- **Hermes** = planner, orchestrator, scope guard, verifier, final integrator, final reporter.
- **deepseek-fast** = writing worker only.
- **deepseek-pro** = review worker only.

Never collapse these roles in serious project work unless Mohamed explicitly suspends the rule.

## Core rule

If the task is serious project coding, do **not** drift into solo implementation just because it feels faster.

That is a workflow failure, not an optimization.

## Required sequence

1. **Load state first**
   - read the current project control files
   - identify the actual next slice
   - make sure the next slice is small enough for one worker pass

2. **Hermes writes the slice**
   - define the exact target
   - define the boundaries
   - define what the writer may change
   - define what the reviewer must check

3. **Dispatch the writer first**
   - send the execution brief to `deepseek-fast`
   - the writer produces draft implementation or file-ready governance content
   - the writer does not approve its own work

4. **Dispatch the reviewer second**
   - send the writer output to `deepseek-pro`
   - ask for explicit verdict, risks, and exact fixes
   - the reviewer does not become the implementer unless Hermes explicitly uses the review to direct a new writer pass

5. **Hermes decides and applies**
   - accept only the smallest correct slice
   - trim any over-expansion
   - apply only what survives review
   - re-read the changed files after applying

6. **Verify with real output**
   - run the smallest relevant tests first
   - then run the broader gate when relevant
   - do not claim completion from plan quality alone

7. **Update project state**
   - task queue
   - progress/evidence/run logs
   - restart notes if the next action changed materially

8. **Report to Mohamed operationally**
   - where we stand
   - what materially improved
   - what risk was removed
   - what remains blocked
   - what the next practical move is

## Reporting rule for Mohamed

Mohamed is not asking for programming narration.

Default reporting should avoid leading with:
- modules
- functions
- patches
- internal code structure
- tool chatter

Translate the outcome into:
- decision quality
- bottleneck movement
- risk reduction
- next action

If technical evidence is needed, keep it brief and secondary.

## Pitfalls

### Pitfall: solo drift

Bad pattern:
- Hermes starts with the team plan
- then switches into solo coding because the step looks easy
- then reports completion without using the writer/reviewer split

Fix:
- if the work is serious project coding, enforce the team sequence anyway

### Pitfall: reviewer becomes a second writer

Bad pattern:
- reviewer is asked vague questions
- reviewer rewrites strategy instead of auditing the writer output

Fix:
- ask for verdict, strengths, weaknesses, exact fixes, and recommended next step
- Hermes remains the final decision-maker

### Pitfall: over-expansion from the writer

Bad pattern:
- writer produces a package larger than the intended slice
- Hermes applies all of it because it looks useful

Fix:
- reviewer checks for scope drift
- Hermes applies only the smallest correct slice

### Pitfall: technical reporting to Mohamed

Bad pattern:
- report starts with file paths, modules, functions, and test wiring

Fix:
- report first in operational language
- mention code evidence only after the practical conclusion

## Good default prompts

### Writer prompt shape
- current project state
- exact target slice
- constraints
- files to inspect
- output format
- explicit instruction: write only, do not review, do not modify repo directly unless asked

### Reviewer prompt shape
- current project state
- writer output location
- exact review criteria
- explicit instruction: review only, do not rewrite from scratch, do not modify repo directly unless asked
- require: verdict, strengths, weaknesses, exact fixes, final recommended next step

## Verification standard

A team-governed pass is not done until Hermes has:
- checked the writer output
- checked the reviewer output
- applied only the accepted slice
- re-read changed files
- run real verification when relevant
- updated project state files if the next action changed

## When not to use

You can skip this full workflow only for:
- trivial typo/wording fixes
- very small reversible doc cleanup
- clearly mechanical non-coding edits

If in doubt, use the workflow.

## Relationship to other skills

- Use with `senior-software-engineer` for coding discipline.
- Use with `mohamed-agent-loop-os` when the project is governed by file-based control/state.
- Use with `mohamed-opencode-go-worker-profiles` when the available worker profiles and routing matter.
- Overlaps with `mohamed-coding-team`; prefer consolidating future lessons there if that skill is actively loaded and patchable.
