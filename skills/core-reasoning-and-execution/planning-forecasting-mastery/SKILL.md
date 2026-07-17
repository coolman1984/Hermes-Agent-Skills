---
name: planning-forecasting-mastery
description: "Use at the start of any multi-step effort, roadmap, project, build, migration, research plan, investment workflow, automation rollout, estimate, forecast, risk review, prioritization, or execution sequence. Pairs with reasoning-mastery: reasoning frames the problem; this skill turns goals into adaptable plans with estimates, risks, checkpoints, and learning loops."
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [planning, forecasting, estimation, risk, judgment, execution, project-management]
    related_skills: [reasoning-mastery, skill-forge, engineering-mastery]
---

# Planning, Judgment and Forecasting Mastery

## Mission

Turn goals into executable, adaptable plans. A plan is a hypothesis, not a prophecy: define the outcome, choose the smallest useful next slice, forecast honestly, surface concrete risks, set checkpoints, and compare predicted vs actual.

## Mandatory Start

1. Load `reasoning-mastery` for intent, assumptions, and problem frame.
2. Read `ERRORS.md` for planning misses before major plans.
3. Define outcome, not just activity: success criteria and definition of done.
4. Choose planning depth: sketch, sprint plan, roadmap, risk plan, or forecast.
5. Use ranges, confidence levels, and explicit assumptions.
6. Name trade-offs: speed, scope, quality, cost, risk, learning.
7. Add checkpoints and review actual vs expected.

## Iron Rules

- A plan is a hypothesis, not a prophecy.
- Plan only to the level of detail the next decision requires.
- Forecast ranges, not fake exact dates.
- Surface specific risks: trigger, impact, mitigation, owner.
- Sequence for early learning and value.
- Use reference classes and base rates when possible.
- Every plan has a checkpoint and kill/switch criteria.
- Over-planning is failure; under-planning is failure.
- Never hide uncertainty to sound confident.
- Update `ERRORS.md` after missed risks, bad estimates, wrong priority, or wrong sequence.

## Router

| Planning shape | Playbook | Default move |
|---|---|---|
| Vague ambition | `references/goals-outcomes.md` | outcome, success criteria, done definition |
| Large effort | `references/decomposition-sequencing.md` | phases, milestones, vertical slice |
| Date/cost estimate | `references/estimation-forecasting.md` | range, confidence, assumptions, reference class |
| Risky project | `references/risk-management.md` | risk register, pre-mortem, mitigations |
| Many choices | `references/prioritization-tradeoffs.md` | decision criteria and opportunity cost |
| Uncertain future | `references/judgment-forecasting.md` | base rates, update triggers, calibration |
| Execution tracking | `references/execution-control.md` | milestones, leading indicators, checkpoint cadence |
| After completion | `references/retrospective-learning.md` | predicted vs actual, prevention rules |

## Default Flow

```text
intent → outcome → constraints → decomposition → estimate range → risks → sequence → checkpoint → execute → review
```

## Templates

- `templates/plan_intake.md` — goal, done, constraints, assumptions.
- `templates/work_breakdown.md` — phases, milestones, tasks, owners, outputs.
- `templates/risk_register.md` — risk, trigger, impact, mitigation, owner.
- `templates/forecast_record.md` — estimate range, confidence, base rate, update trigger.
- `templates/decision_tradeoff.md` — options, criteria, sacrifices, choice.
- `templates/checkpoint_review.md` — expected vs actual, what changed, next plan.
- `templates/premortem.md` — future failure story and prevention.

## Completion Checklist

- [ ] Outcome and done definition stated.
- [ ] Work split into useful slices.
- [ ] Estimate uses ranges and assumptions.
- [ ] Risks are concrete with mitigation.
- [ ] Trade-offs are named.
- [ ] Checkpoint exists.
- [ ] Kill/switch criteria exist for uncertain plans.
- [ ] Predicted vs actual review is scheduled.
