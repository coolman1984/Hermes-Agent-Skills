# Agent Loop Audit — 2026-06-30

## What was right

- The system captured the central idea: do not treat agents as chat.
- It separated planner, generator, evaluator, and Hermes verification.
- It required file-backed state and explicit contracts.
- It integrated the senior software engineering skill as the quality layer.
- It linked worker-profile routing to the loop.

## What was weak or missing

1. It risked overbuilding every task with a full folder.
   - Correction: add loop levels and prefer 3-file loop before full `.agent-loop/`.

2. Contract negotiation was described, but not strict enough.
   - Correction: evaluator must challenge the contract before generation starts.

3. The original text emphasized that a project should survive from three files.
   - Correction: add the 3-file survival test.

4. Subjective quality scoring lacked references and numeric threshold.
   - Correction: add weighted rubric with 0.0–1.0 scoring and good/bad examples.

5. Trace reading was too abstract.
   - Correction: require worker/profile, files read, files changed, checks run, and divergence point in `run-log.md`.

6. Scaffolding deletion was a principle but not operational.
   - Correction: add `scaffolding-review.md` and explicit keep/simplify/delete decision.

7. Bottleneck movement was a principle but not tracked.
   - Correction: add `bottleneck-log.md`.

8. The skill lacked reusable templates.
   - Correction: add templates for brief-contract, progress, run-log, evaluator findings, rubric, scaffolding review, and bottleneck log.

## Final standard

Start small. Keep state boring. Make success testable. Split roles. Read traces. Restart when the structure is rotten. Delete machinery that no longer earns its cost.
