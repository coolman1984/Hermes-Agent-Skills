# Frontend Engineering Error Log

## 2026-07-08 — Generated HTML fixture must be quoted
- Symptom: frontend validation script failed with `SyntaxError` because HTML was written as raw Python code.
- Root cause: nested triple-quote generation stripped the string delimiter.
- Fix: rewrite fixture as an explicit triple-quoted string and rerun syntax check.
- Prevention rule: generated code examples containing HTML/JS must be compiled before packaging.

## 2026-07-08 — Baseline created
- Symptom: domain-specific engineering failures were scattered.
- Root cause: one generic full-stack skill cannot encode specific traps.
- Fix: focused sub-skill with references and validation artifact.
- Prevention rule: add every reusable domain bug here after real work.
