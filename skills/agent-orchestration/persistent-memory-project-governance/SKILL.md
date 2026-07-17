---
name: persistent-memory-project-governance
description: Use when Mohamed wants a file-based project operating system for multi-step work, data projects, reports, software builds, factory workflows, or restartable autonomous execution. Preserves mission, scope, decisions, assumptions, risks, evidence, validation, memory, and handover in project files without polluting global memory.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  tags: [project-governance, persistent-memory, restartable-work, evidence, validation, file-os, mohamed]
  related_skills: [mohamed-agent-loop-os, senior-software-engineer, mohamed-opencode-go-worker-profiles]
---

# Persistent Memory and Project Governance

## Core rule

The filesystem is the project brain.

Project truth must live in files, not chat memory.

Use this skill when a task has more than one step, involves files, requires decisions, creates outputs, uses data, needs validation, or may continue later.

Do not use the full structure for tiny one-shot tasks. For medium tasks, prefer `mohamed-agent-loop-os` Level 1 three-file loop. Use this skill when the work deserves Level 2 or Level 3 governance.

## Prime directive

Do not optimize for looking helpful.

Optimize for correct, useful, verified, restartable work.

Never claim completion without evidence.
Never rely on confidence when verification is possible.
Never let the same role both create and approve final work.
Always leave the project in a state another agent can understand and continue.

## Activation rule

Activate this skill for:

- serious multi-step projects
- data/file processing workflows
- report factories
- software builds with decisions and validation
- long-running agent loops
- projects that may be resumed by another agent
- work where evidence and auditability matter

If the work is smaller, use `mohamed-agent-loop-os` minimal loop instead.

## Role system

Separate internal work into roles:

1. Mission Analyst — extracts real goal and writes requirements.
2. Planner — creates task queue and dependencies.
3. Architect — designs workflow, data logic, validation, rollback, and restart strategy.
4. Builder — creates outputs but does not approve them.
5. Evaluator — challenges outputs against the success contract.
6. Risk Officer — maintains risks and approval points.
7. Archivist — maintains memory, decisions, logs, evidence, and handover.

The builder must not approve its own work.

## Mandatory project structure

For governed projects, create:

```text
00_control/
01_inputs/raw_files/
01_inputs/user_notes/
01_inputs/references/
02_understanding/
03_design/
04_execution/working_files/
04_execution/code/
04_execution/configs/
04_execution/generated_outputs/
04_execution/temporary_outputs/
05_validation/tests/
06_final_outputs/final_files/
07_archive/old_attempts/
07_archive/rejected_paths/
07_archive/previous_versions/
07_archive/obsolete_rules/
```

Core control files:

```text
00_control/mission.md
00_control/project_scope.md
00_control/success_contract.md
00_control/task_queue.md
00_control/progress.md
00_control/decisions.md
00_control/assumptions.md
00_control/risks.md
00_control/bottlenecks.md
00_control/run_log.md
00_control/evidence_log.md
00_control/evaluation_report.md
00_control/restart_notes.md
00_control/memory_index.md
00_control/open_questions.md
```

Understanding and design files:

```text
01_inputs/source_inventory.md
02_understanding/extracted_requirements.md
02_understanding/workflow_map.md
02_understanding/logic_map.md
02_understanding/data_map.md
02_understanding/terminology.md
02_understanding/constraints.md
03_design/architecture.md
03_design/implementation_plan.md
03_design/validation_plan.md
03_design/rollback_plan.md
```

Validation and handover files:

```text
05_validation/test_results.md
05_validation/quality_checks.md
05_validation/error_log.md
05_validation/issue_tracker.md
06_final_outputs/final_report.md
06_final_outputs/handover_notes.md
06_final_outputs/proof_of_completion.md
```

## Startup protocol

At the beginning of a governed run, read or create:

- `00_control/mission.md`
- `00_control/project_scope.md`
- `00_control/success_contract.md`
- `00_control/task_queue.md`
- `00_control/progress.md`
- `00_control/decisions.md`
- `00_control/assumptions.md`
- `00_control/risks.md`
- `00_control/memory_index.md`
- `00_control/run_log.md`
- `00_control/evidence_log.md`

Then write a restart summary to:

`00_control/restart_notes.md`

The restart summary must include:

1. Current mission.
2. Current project state.
3. Completed work.
4. Pending work.
5. Active constraints.
6. Active assumptions.
7. Known risks.
8. Current bottleneck.
9. Next best action.
10. Files that are the current source of truth.

If project files already exist, continue from them. Do not ask Mohamed to repeat what is already in files.

## Success contract rule

Before major execution, create or update:

`00_control/success_contract.md`

It must define:

- mission
- required deliverables
- acceptance criteria
- quality criteria
- data requirements
- technical constraints
- formatting constraints
- naming rules
- validation method
- evidence required
- failure conditions
- human approval points
- final handover format

No major task is complete unless it satisfies the success contract.

## Task queue rule

Maintain:

`00_control/task_queue.md`

Each task should include:

- task ID
- task name
- responsible role
- status
- priority
- input files
- output files
- dependency
- validation method
- evidence required
- notes

Allowed statuses:

- Pending
- In Progress
- Blocked
- Needs Review
- Failed
- Passed
- Archived

Only the evaluator can mark a task as Passed.

## Evidence rule

Every important claim needs evidence.

Record evidence in:

`00_control/evidence_log.md`

Each entry should include:

- evidence ID
- date
- claim
- evidence type
- evidence location
- verification method
- result
- confidence

If there is no evidence, do not claim completion.

## Assumptions and risks

Record assumptions in:

`00_control/assumptions.md`

Each assumption includes:

- assumption
- reason
- risk level
- how to verify later
- impact if wrong
- status

High-risk assumptions must also be flagged in:

`00_control/risks.md`

## Data and file handling

When working with data:

1. Never modify raw inputs directly unless Mohamed explicitly instructs it.
2. Treat `01_inputs/raw_files/` as read-only.
3. Create working copies under `04_execution/working_files/`.
4. Maintain `01_inputs/source_inventory.md`.
5. Create data contracts in `02_understanding/data_map.md`.
6. Validate row counts, column counts, totals, and key fields where possible.
7. Record missing, duplicated, inconsistent, or suspicious data.
8. Keep transformations reproducible.
9. Save configuration separately from outputs.
10. For large files, profile, sample, chunk, index, or use a database instead of loading everything blindly.

## Quality gates

Use these gates:

1. Mission clarity.
2. Success contract exists.
3. Inputs are inventoried.
4. Assumptions are recorded.
5. Execution output exists.
6. Validation was performed.
7. Evidence was recorded.
8. Memory was updated.
9. Final handover is complete.

If a gate cannot be completed, write why to:

`05_validation/issue_tracker.md`

Continue with the safest possible next action.

## Roadmap and phase-planning rule

When Mohamed asks for "the next steps", "a rigorous plan", "the roadmap", or wants the
system view turned into execution order, do not answer only in chat.

Write or update:

`03_design/implementation_plan.md`

Use it as the authoritative execution roadmap.

Minimum contents:

1. current verified baseline
2. ordered phases
3. exact next phase and why it comes first
4. preconditions for later phases
5. stop conditions
6. cross-phase risks and defenses
7. verification ladder
8. recommended next action

Before writing the plan, verify the live baseline where possible (tests, demo, current branch,
key artifacts). Do not build the roadmap on stale assumptions from old control files alone.

After writing the roadmap, propagate it into the governed state:

- decompose the active next task in `00_control/task_queue.md`
- update `00_control/decisions.md` when phase order or branch policy changes
- update `05_validation/issue_tracker.md` with newly recognized blockers or controlled risks
- update `00_control/progress.md`, `00_control/run_log.md`, and `00_control/evidence_log.md`

This prevents the common failure mode where a good plan exists in one file but the rest of the
project still tells an older story.

## Core-before-infra sequencing rule

In governed product/data/code projects, prefer this order unless evidence strongly says
otherwise:

1. finish the highest-leverage visible management/user value already supported by the current core
2. validate one real workflow or real dataset
3. only then activate heavier infrastructure, search, graph, model, or deployment layers

Typical anti-pattern:

- jump to heavy tools because they are architecturally exciting
- before the current core output is fully surfaced or validated on real inputs

Correct pattern:

- close the value gap in the current slice first
- then test reality
- then scale the system

If a later subsystem depends on unresolved workflow definition, real-data profiling, or infra
ownership, mark it Blocked and document the preconditions in the implementation plan and task
queue.

## Evaluation rubric

Score every major output from 0.0 to 1.0:

- completeness
- correctness
- practical usefulness
- clarity
- robustness
- simplicity
- restartability
- evidence quality
- user fit
- professional quality

If any score is below 0.85, improve the output.
If any score is below 0.70, reject the output and rebuild.

For subjective outputs, define examples of good and bad quality before scoring.

## Failure handling

When something fails, log it in:

- `05_validation/error_log.md`
- `05_validation/issue_tracker.md`

Include:

- what failed
- where it failed
- likely reason
- evidence
- fix attempted
- result
- next action

Retry only when the cause is understood. Do not repeat the same failed action blindly.

## Restart and rollback

Restart when:

- structure is too complex
- output is built on bad assumptions
- too many patches were added
- validation keeps failing
- design no longer matches the mission
- a simpler path is available

Before restarting, update:

`00_control/restart_notes.md`

Move old attempts to:

`07_archive/old_attempts/`

Never delete useful history without recording why.

## Memory hygiene

Use:

`00_control/memory_index.md`

as the project brain.

Save only durable, useful information:

- user preferences
- project rules
- stable constraints
- workflow logic
- data meanings
- validation rules
- naming conventions
- important decisions
- known problems
- successful methods
- failed methods to avoid
- current state summary

Do not save noise, random observations, repeated facts, emotional commentary, or raw content that belongs in source files.

## Scaffolding review

At the end of each phase, review the process.

Identify unnecessary files, rules, repeated steps, obsolete assumptions, old workarounds, and over-engineered structure.

Move obsolete items to:

`07_archive/obsolete_rules/`

A system that only grows and never deletes is dangerous.

## Final handover

Before final delivery, create:

- `06_final_outputs/handover_notes.md`
- `06_final_outputs/proof_of_completion.md`

The handover must include:

1. What was completed.
2. Where the final outputs are.
3. What inputs were used.
4. What assumptions were made.
5. What was validated.
6. What evidence exists.
7. What risks remain.
8. Optional improvements.
9. Recommended next action.

Final response to Mohamed should be short, clear, and connected to the saved files.

## Skill-routed architecture for large agent systems

When a governed project grows into a large multi-tool or multi-domain agent system, do not let the main agent prompt become a giant encyclopedia of every tool, workflow, and edge case.

Prefer this structure:

1. a **lightweight routing layer** that classifies the task
2. a **central contract/core** that holds shared truth
3. **specialized skills** that execute narrow classes of work deeply

Use this pattern when:
- the project spans many tools or source types
- loading the whole system every turn is expensive or confusing
- different tasks need different depth
- you want lower token cost without losing restartability or trust

Recommended file shape inside the repo:

```text
AGENTS.md                    # short operating manual + read order
AGENT_SKILL_MAP.md           # task-routing map: which skill to load when
AGENT_CORE_CONTRACT.md       # shared truth: naming, evidence, storage, trust, handoff
agent_skills/
  spreadsheet_ingestion.md
  cost_variance_analysis.md
  management_reporting.md
  audit_and_trust.md
```

Rules:
- keep `AGENTS.md` short; it should route, not explain everything
- do not load every skill by default
- keep naming, storage, confidence, and evidence semantics centralized
- let skills specialize in execution, not redefine core truth
- when a task crosses stages, compose skills in sequence instead of improvising one giant prompt

This avoids two bad extremes:
- one monolithic prompt that reloads the entire project every task
- isolated skills that drift into inconsistent naming, storage, and trust behavior

## Umbrella-project unification rule

When Mohamed decides that several adjacent systems are really one operating system — for example idea capture, product design, book production, interactive delivery, and growth/distribution — do not keep treating them as unrelated projects and do not collapse them into one giant skill.

Use this structure instead:

1. create one umbrella project directory
2. write a short `AGENTS.md` that defines purpose and read order
3. write a central contract file such as `AGENT_CORE_CONTRACT.md`
4. write a routing map such as `AGENT_SKILL_MAP.md`
5. create local specialized skills under `agent_skills/`
6. keep existing global skills as references in phase 1 unless there is a deliberate migration plan
7. migrate one live production path first before attempting full consolidation

Recommended first-pass repo shape:

```text
AGENTS.md
AGENT_CORE_CONTRACT.md
AGENT_SKILL_MAP.md
agent_skills/
00_control/
01_inputs/
02_understanding/
03_design/
04_execution/
templates/
tools/
```

When using this pattern, each sub-line stays distinct:
- ideas/intelligence
- product definition
- core knowledge asset or book
- interactive explanation or delivery layer
- distribution/growth

Do not let one line redefine the rules of another. The umbrella exists to coordinate them, not to blur them.

Default sequencing:
1. unify the operating contract
2. map routes between lines
3. inventory current assets
4. choose one live path as the migration wedge
5. only then consider moving source-of-truth ownership from old global skills into the new project

Common pitfall:
creating the umbrella and then trying to merge every asset immediately. This creates noise, breaks references, and hides the first useful path. Start with one working lane.

## Existing project governance takeover rule

When entering a repository that already has a serious file-based operating system — for example `00_control/*`, restart notes, evidence logs, or an owner-written project OS — do **not** blindly bootstrap a second full governance tree on top of it.

Use this sequence instead:

1. Audit the existing control files first.
2. Decide whether the current governance is authoritative enough to keep.
3. If it is, preserve it as the source of truth.
4. Only add a lightweight bridge layer when you need faster restarts or a Mohamed-specific loop wrapper.
5. Align stale next-step references, restart notes, and evidence entries so the project tells one consistent story.
6. Record the takeover in the existing run log and evidence log.
7. If Mohamed asks for a rigorous roadmap, follow `references/roadmap-phase-order-pattern.md` and
   mirror the plan back into task, issue, decision, progress, and evidence files.

Default lightweight bridge shape:

```text
.agent-loop/brief-contract.md
.agent-loop/progress.md
.agent-loop/run-log.md
```

This bridge points back to the governed files instead of replacing them.

See:

`references/existing-repo-governance-bridge.md`

## Common pitfalls

1. Applying the full project OS to tiny tasks.
2. Letting logs grow without compressed summaries.
3. Treating `memory_index.md` as a dumping ground.
4. Marking tasks passed without evaluator evidence.
5. Writing outputs but forgetting handover and proof.
6. Modifying raw inputs directly.
7. Creating scaffolding that no one reads.
8. Bootstrapping a second governance system inside a repo that already has one.
9. Leaving stale "next action" references after partial progress, which breaks restart quality.

## Verification checklist

- [ ] Project structure exists.
- [ ] Startup files exist or were read.
- [ ] Restart summary exists.
- [ ] Success contract exists.
- [ ] Task queue is current.
- [ ] Assumptions and risks are recorded.
- [ ] Evidence log supports completion claims.
- [ ] Validation files record checks and failures.
- [ ] Handover and proof of completion exist before final delivery.
- [ ] Obsolete rules or attempts are archived, not silently deleted.
