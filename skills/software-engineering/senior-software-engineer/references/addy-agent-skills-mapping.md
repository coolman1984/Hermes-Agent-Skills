# Addy Osmani Agent Skills Mapping

Local source inspected: `/root/agent-skills`

## Repository facts

- Skills: 24
- Agent personas: 5 markdown files found, with 4 primary personas documented in README
- References: 5 markdown files found, with 4 primary checklists documented in README
- Main lifecycle: define → plan → build → verify → review → ship

## Adopted principles

- Spec before significant code.
- Small, verifiable tasks.
- Incremental implementation.
- Tests as proof.
- Five-axis review: correctness, readability, architecture, security, performance.
- Simplicity over cleverness.
- Source-driven decisions for unfamiliar frameworks.
- Security and observability considered before shipping, not after.

## Not copied blindly

The repository contains hooks and command integrations for Claude, Gemini, OpenCode, and other tools. Those are not installed into Hermes automatically because they are tool-specific and can change agent behavior broadly.

This Hermes skill imports the engineering workflow, not arbitrary hooks or automation.

## Useful local files

- `/root/agent-skills/skills/using-agent-skills/SKILL.md`
- `/root/agent-skills/skills/spec-driven-development/SKILL.md`
- `/root/agent-skills/skills/planning-and-task-breakdown/SKILL.md`
- `/root/agent-skills/skills/incremental-implementation/SKILL.md`
- `/root/agent-skills/skills/test-driven-development/SKILL.md`
- `/root/agent-skills/skills/code-review-and-quality/SKILL.md`
- `/root/agent-skills/skills/security-and-hardening/SKILL.md`
- `/root/agent-skills/skills/performance-optimization/SKILL.md`
- `/root/agent-skills/references/security-checklist.md`
- `/root/agent-skills/references/testing-patterns.md`
- `/root/agent-skills/references/performance-checklist.md`
- `/root/agent-skills/references/accessibility-checklist.md`

## Vetting summary

Quick scan found references to network commands, credentials, dangerous shell terms, and external URLs. Manual interpretation: these are mostly examples, documentation, hooks, validation scripts, and security checklist content. Because hooks can alter behavior, they were not installed. The workflow skill is low risk because it is markdown-only and contains no executable automation.
