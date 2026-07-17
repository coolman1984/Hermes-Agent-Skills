# Reasoning Mastery Error Log

## 2026-07-08 — Skill frontmatter description with colon must be quoted
- Symptom: YAML validation failed with `mapping values are not allowed here`.
- Root cause: description contained a colon after “tools:” without quotes.
- Prevention rule: quote any frontmatter field containing colons, commas, or long trigger text.

## 2026-07-08 — Solving the requested Y instead of surfacing X
- Symptom: user asks for an implementation detail that may not solve the actual goal.
- Root cause: literal compliance before intent discovery.
- Prevention rule: for ambiguous/non-trivial requests, state the likely X and verify or proceed with the useful default.

## 2026-07-08 — Plausible answer before red-team
- Symptom: first solution sounds efficient but fails an edge case.
- Root cause: premature convergence.
- Prevention rule: ask “what would make this wrong?” before committing when stakes are non-trivial.

## 2026-07-08 — Blind persistence on a dead path
- Symptom: repeated retries without new information.
- Root cause: confusing persistence with repetition.
- Prevention rule: every retry must change one variable or test a new hypothesis; otherwise switch representation or stop with proof.

## 2026-07-08 — Fabricating solvability for ill-posed tasks
- Symptom: task asks for a unique or exact answer without enough information.
- Root cause: pressure to be helpful.
- Prevention rule: prove underdetermination, refuse fake certainty, and offer the nearest solvable version.
