# How Hermes Skills Work

## What a skill is

A reusable operating procedure packaged as markdown plus optional support files. It defines when to load, the workflow, verification, and pitfalls.

Skills are not chat memories. Memories hold facts. Skills hold procedures.

## Anatomy of SKILL.md

1. YAML frontmatter — name, description, tags, related skills
2. Mission / overview
3. When to use
4. Workflow
5. Pitfalls
6. Verification

The description field is used for relevance routing.

## Loading behavior

1. Task arrives
2. Agent classifies the task
3. Relevant skills load via skill_view
4. Instructions shape tool use and quality gates
5. Output verified against completion checks

For non-trivial work, typically load `reasoning-mastery` and `standing-execution-protocol` first, then specialists.

## Installing from this repo

```bash
SRC=./skills/software-engineering/senior-software-engineer
DST=~/.hermes/skills/software-development/senior-software-engineer
mkdir -p "$(dirname "$DST")"
cp -a "$SRC" "$DST"
```

Start a new Hermes session after install.

## Authoring tips

- Put trigger conditions in the description
- Prefer checkable verification
- Keep secrets out; reference env var names only
- Patch after real failures
