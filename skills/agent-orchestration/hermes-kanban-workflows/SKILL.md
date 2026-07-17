---
name: hermes-kanban-workflows
description: "Use when operating Hermes Kanban as an orchestrator or worker: decomposing work, enforcing worker lifecycle, avoiding orchestration temptations, and verifying task handoffs."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [kanban, orchestration, workers, task-lifecycle, delegation, devops]
    related_skills: [hermes-agent]
---

# Hermes Kanban Workflows

## Overview

This is the class-level umbrella for Hermes Kanban operation. It covers both sides of the system: orchestrators that decompose and route work, and workers that execute scoped tasks through the injected Kanban lifecycle. Use one skill with labeled subsections instead of separate orchestrator/worker micro-skills.

Absorbed original skill packages are preserved under `references/absorbed/<skill-name>/`.

## When to Use

- A Hermes profile is acting as a Kanban orchestrator and must split work into tasks.
- A Kanban worker needs reminders about lifecycle, anti-temptation rules, or handoff quality.
- You need to decide whether to do work directly or route it to a worker lane.
- You are debugging incomplete, vague, or unverifiable Kanban task outcomes.

## Orchestrator Lane

The orchestrator's job is decomposition, assignment, sequencing, review, and synthesis — not doing the worker's implementation. Create tasks with enough context to let workers succeed independently, then verify their outputs before merging or reporting.

Full archived package: `references/absorbed/kanban-orchestrator/SKILL.md`.

## Worker Lane

The worker's job is to execute the assigned task faithfully, communicate blockers, and return verifiable artifacts. The base lifecycle is injected by Hermes; this skill adds pitfalls, examples, and edge cases.

Full archived package: `references/absorbed/kanban-worker/SKILL.md`.

## Shared Lifecycle

1. Clarify the objective and acceptance criteria from the task card.
2. Inspect the relevant files/state before editing.
3. Make the smallest coherent change that satisfies the card.
4. Run the verification command named by the card, or a justified equivalent.
5. Return a concise handoff: changed files, commands run, results, blockers, and risks.

## Common Pitfalls

1. **Orchestrator temptation.** If you are orchestrating, do not silently implement worker tasks yourself.
2. **Thin worker briefs.** A task without paths, constraints, or verification commands creates rework.
3. **Unverifiable handoffs.** Require concrete file paths, command outputs, URLs, or IDs.
4. **Parallel conflicts.** Avoid assigning overlapping file regions to multiple workers without a merge plan.

## Verification Checklist

- [ ] Role is clear: orchestrator or worker.
- [ ] Task boundaries and success criteria are explicit.
- [ ] Outputs are backed by artifacts or commands.
- [ ] The final synthesis distinguishes completed work from blockers.
