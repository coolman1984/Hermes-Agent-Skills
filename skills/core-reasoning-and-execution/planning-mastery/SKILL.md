---
name: planning-mastery
description: "Use whenever the user wants to plan, scope, roadmap, schedule, estimate, set goals, forecast risks, or decide priorities for anything multi-step — a project, a build, a launch, a proposal, a phased initiative. Also triggers on what could go wrong, how long will this take, what should we do first, break this into phases. Pairs with reasoning-mastery."
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [planning, forecasting, estimation, risk, roadmap, prioritization, execution]
    related_skills: [reasoning-mastery, planning-forecasting-mastery, engineering-mastery]
---

# Planning Mastery

## Mission

Turn intent into a plan that can survive contact with reality: define the goal, choose the right planning depth, estimate honestly, sequence for learning, surface risks early, decide what not to do, and review predicted vs actual.

## Mandatory Start

1. Consult `reasoning-mastery` first: clarify real intent, assumptions, constraints, and stakes.
2. Read `ERRORS.md` before serious plans.
3. Define goal and success criteria before tasks.
4. Pick the lightest planning tool that fits the next decision.
5. Estimate in ranges and re-estimate as information arrives.
6. Run a premortem and risk register for non-trivial plans.
7. Build phase gates and review points into the plan.
8. Compare predicted vs actual and update `ERRORS.md` after execution.

## Iron Rules

- Goal before plan.
- Plan to the detail the next decision needs, not more.
- Every plan states assumptions and trade-offs.
- Estimates are ranges with buffers, never false-precision points.
- Estimate is not commitment; commitment is a negotiated scope/time/risk decision.
- Every non-trivial plan gets a premortem and risk register.
- Every phase has entry/exit criteria and measured success.
- Decide what not to do; focus is part of planning.
- Build in decision points; a plan that cannot adapt is a liability.
- Calibration compounds: compare predicted vs actual.

## Router

| Goal shape / horizon | Playbook | Template |
|---|---|---|
| Vague ambition | `references/goals-outcomes.md` | `templates/goal_brief.md` |
| Multi-step build | `references/decomposition.md` | `templates/phased_plan.md` |
| Need time/cost estimate | `references/estimation.md` | `templates/phased_plan.md` |
| Dependencies/roadmap | `references/roadmap-sequencing.md` | `templates/phased_plan.md` |
| Avoid problems | `references/risk-forecasting.md` | `templates/premortem.md`, `templates/risk_register.md` |
| Too many tasks | `references/prioritization.md` | `templates/decision_record.md` |
| Hard deadline/uncertain future | `references/scenario-planning.md` | `templates/decision_record.md` |
| Active execution/review | `references/tracking-review.md` | `templates/phase_review.md` |

## Default Flow

```text
reasoning frame → goal brief → phased plan → estimate range → dependencies → premortem → risk register → prioritization → scenarios → checkpoint → review
```

## Completion Checklist

- [ ] Goal, why, success criteria, and definition of done are explicit.
- [ ] Plan is sliced into phases, milestones, tasks, owners, inputs, outputs, acceptance criteria.
- [ ] Estimates use reference class and ranges.
- [ ] Dependencies, critical path, and parallel work are visible.
- [ ] Premortem and risk register exist for non-trivial plans.
- [ ] Priorities name what will not be done.
- [ ] Scenarios and dangerous assumptions are identified.
- [ ] Phase review compares expected vs actual and feeds `ERRORS.md`.
