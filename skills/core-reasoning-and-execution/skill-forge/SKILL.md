---
name: skill-forge
description: Use when the user says learn a new field, become expert in, make a skill for, improve your skill, run the mastery protocol on a field, create a reusable skill package, validate a skill, or upgrade an existing skill after a real task.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [skills, mastery, research, validation, self-improvement]
    related_skills: [hermes-agent-skill-authoring, senior-software-engineer]
---

# Skill Forge

## Mission

Turn a field into a durable, tested Hermes skill package. Do not stop at a chat answer. The deliverable is files on disk plus validation evidence.

## Field Template

Replace only this block for each run:

```markdown
## THE FIELD: ____
- Branch A
- Branch B
- Branch C
```

## Protocol

1. Research branch by branch from primary sources first.
2. Map concepts and sources.
3. Practice with runnable examples.
4. Distill immediately into `SKILL.md`, `references/`, `scripts/`, and `ERRORS.md`.
5. Validate with real tasks.
6. Fix the skill when validation exposes a gap.
7. Package the skill for installation.

## Construction Rules

- `SKILL.md` stays under 500 lines and acts as router.
- Build class-level umbrella skills, not one-session-one-skill artifacts.
- Long detail goes in references.
- Session-specific findings, source maps, API notes, validation evidence, and condensed knowledge banks go under `references/` with a pointer from `SKILL.md` when needed.
- Reusable starter files go under `templates/`; re-runnable checks or generators go under `scripts/`.
- Every runnable snippet is tested.
- Every skill has `ERRORS.md`.
- Every reference ends with usage image: when to use, signal, mistake to avoid.
- Quote YAML frontmatter descriptions when they contain colons, commas, or long trigger text; unquoted `description: ... tools: ...` breaks parsing.
- For governing/router skills, make the trigger explicit enough that future sessions know when to consult it before other skills.

## Skill Library Hygiene

When a mastery or review session produces a lesson:

1. Patch a currently loaded/relevant skill first.
2. If none fits, update an existing umbrella skill.
3. Add support files under an umbrella before creating a new skill.
4. Create a new skill only when it is genuinely class-level and reusable.
5. Do not save transient environment failures as durable rules; save the reusable fix or retry pattern instead.

## User-Specified Skill Shape

When Mohamed provides an exact target skill name, directory structure, or file list after a related skill already exists, do not silently substitute the existing broader skill. Either:

- build the requested class-level shape exactly when it is reusable and not a one-off artifact, or
- explicitly say it overlaps with an existing umbrella and patch that umbrella instead.

If the requested shape is class-level and differs materially from the existing umbrella, create or update the exact requested skill and note the overlap in the final report so the curator can consolidate later.

## Validation Rules

At least six tasks for a broad field. Each task must have pass/fail, evidence, and any fix applied. If a requested validation target cannot be reproduced exactly in the current environment (for example a proprietary file format or unavailable real sample), use the closest honest substitute, label the gap in the validation table, and make the exact sample the next research item — do not claim full coverage.

When validation fails, diagnose whether the failure is a real skill/playbook gap, an artifact/state gap, or a harness/assertion bug. Patch the skill when the playbook is weak; patch the artifact when a required file, template, state update, or log entry is missing; patch the harness only when the artifact already satisfies the stated pass bar but the check is too brittle (for example matching the wrong phrase). Re-run the full validation after any fix and record the fix in validation evidence.

Before packaging, validate `SKILL.md` frontmatter with a YAML parse, confirm `name` and `description`, check description length, verify required support files exist, and test the zip archive. Do not report a skill as done until this validator passes.

## Improvement Loop

Read `references/improvement-loop.md` before finishing any skill-using task.
