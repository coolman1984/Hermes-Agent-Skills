---
name: reasoning-mastery
description: "Consult at the start of ANY non-trivial task, before choosing tools: any problem that is hard, ambiguous, open-ended, novel, stuck, risky, multi-step, or where the user asks you to figure out, solve, think through, find a way, diagnose, decide, or get to the bottom of something. Governs how every other skill is applied."
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [reasoning, problem-solving, diagnosis, decision-making, metacognition]
    related_skills: [skill-forge, systematic-debugging, data-acquisition-mastery, data-extraction-mastery, database-mastery]
---

# Reasoning Mastery

## Mission

Apply expert reasoning before execution: understand the real problem, choose the right thinking mode, test assumptions, solve rigorously, and learn from failures. This skill is the governing mind for all other skills.

## Mandatory Start for Non-Trivial Tasks

**Mohamed priority gate:** immediately after loading this skill, load and apply `standing-execution-protocol`. It supplies the required intent framing, load-bearing-item check, evidence tiers, self-attack, completeness ledger, and final delivery gate. Do this before substantive tool work.

1. Read `ERRORS.md` when the problem is hard, ambiguous, stuck, or high-stakes.
2. Fill a light version of `templates/problem_intake.md`: real intent, success criteria, assumptions, constraints, and well-posedness.
3. **Run the skill gate before tools:** classify the task, identify every relevant specialist skill, and load them with `skill_view` before the first substantive tool call. Do not rely on recognizing a skill name only; loading it is the proof that its procedure is active.
4. For Mohamed's work, apply these first-pass routes: Hermes task → `hermes-agent`; source/media link → `mohamed-unified-media-drop`; coding → `senior-software-engineer` plus the relevant engineering/testing skill; Egyptian equities → `egyptian-equity-workflow`; vault/notes → `obsidian` or `obsidian-vault`; Arabic writing → `mohamed-arabic-content-style`; ideas → `mohamed-intelligence-vault`; Android → the applicable bridge/phone-control skill.
5. Select one or more playbooks from the router below.
6. Generate at least two candidate approaches unless the task is trivial.
7. Test the preferred approach against failure modes: how could this be wrong?
8. Use tools only after framing the problem and choosing what evidence would matter.
9. After hard tasks, run `templates/retrospective.md` and update `ERRORS.md` when a reasoning failure or new prevention rule appears.

### Skill-use accountability

A skill is considered used only when its full `SKILL.md` has been loaded with `skill_view` (and any needed linked reference has also been loaded). The available-skills index is a discovery aid, not a substitute for loading. If no skill matches confidently, call `skills_list` before proceeding and record the nearest applicable route internally. If a loaded skill's instructions conflict with the user's latest explicit request, the latest request wins; otherwise follow the skill's workflow and verification rules.

## Iron Rules

- Understand before solving. Frame before answering. Derive before memorizing.
- State assumptions explicitly; never present a guess as knowledge.
- Surface the real X when the user asks for Y because they think Y solves X.
- **When the requested solution is impossible, state it. Do not silently substitute.** If the user asks for something that cannot be done (proprietary model, cloud-only service, platform constraint), say so directly. Offer to explain alternatives only after the user confirms they want them. Building a substitute without asking is a hard violation of autonomy boundaries.
- Persistence with judgment: when one path dies, switch; when all viable paths die, say so with proof and offer the nearest solvable version.
- Truth over comfort: do not bluff to avoid uncertainty.
- Make reasoning inspectable: problem frame, evidence, assumptions, options, why chosen, how it could fail.
- Prefer reversible, smallest-validating actions before large commitments.
- Distinguish fixed constraints from conventions.
- Red-team conclusions before committing on high-stakes decisions.
- Learn: every hard problem should improve a playbook, template, or error rule.

## Router: Problem Shape → Playbook

| Problem shape | First playbook | Use when | Beware |
|---|---|---|---|
| Ambiguous request / vague goal | `references/problem-framing.md` | user asks loosely, many possible interpretations | over-asking instead of choosing useful default |
| Suspicious requested solution | `references/problem-framing.md` | XY problem likely | insulting the user; surface intent respectfully |
| Fundamental design / why question | `references/first-principles.md` | assumptions feel inherited | ignoring real-world constraints |
| Big multi-part problem | `references/decomposition.md` | many moving parts | fake MECE splits with overlaps |
| Bug, failure, contradiction | `references/systems-diagnosis.md` | symptoms mislead | patching symptom before root cause |
| Decision under uncertainty | `references/uncertainty-rigor.md` | incomplete evidence, tradeoffs | false precision |
| Obvious answer feels too easy | `references/mental-models.md` + `uncertainty-rigor.md` | trap / bias risk | endless skepticism |
| Stuck / no path | `references/persistence-search.md` | repeated failed attempts | blind persistence on dead approach |
| After hard task | `references/metacognition.md` | improve future behavior | logging temporary noise as durable rule |

## Default Flow

```text
intake → frame → choose playbook → decompose/hypothesize → gather evidence → solve → red-team → verify → retrospective
```

## Templates

- `templates/problem_intake.md` — restate ×3, real intent, well-posedness, success criteria.
- `templates/hypothesis_tree.md` — decompose, hypotheses, falsifying evidence.
- `templates/debug_checklist.md` — reproduce, isolate, one variable, root cause.
- `templates/decision_record.md` — options, assumptions, expected value, risks.
- `templates/retrospective.md` — what worked, failed, new prevention rule.

## Completion Checklist

- [ ] Real intent and success criteria identified.
- [ ] Assumptions and unknowns separated.
- [ ] Correct playbook(s) selected.
- [ ] At least two candidate approaches considered when non-trivial.
- [ ] Chosen approach red-teamed.
- [ ] Evidence or tool output verified before claiming done.
- [ ] If impossible/ill-posed, refusal/proof and nearest solvable version given.
- [ ] Retrospective or `ERRORS.md` updated after hard tasks.
