# Backend Engineering Error Log

## 2026-07-08 — FastAPI TestClient emitted Starlette/httpx deprecation warning
- Symptom: backend validation passed but printed `StarletteDeprecationWarning` about `httpx` and `httpx2`.
- Root cause: installed FastAPI/Starlette test client version expects newer transport dependency naming.
- Fix: treat as warning for this validation, not failure; pin or update test dependencies in real projects.
- Prevention rule: backend validation should record dependency warnings separately from functional failures and verify current framework docs before production use.

## 2026-07-08 — Baseline created
- Symptom: domain-specific engineering failures were scattered.
- Root cause: one generic full-stack skill cannot encode specific traps.
- Fix: focused sub-skill with references and validation artifact.
- Prevention rule: add every reusable domain bug here after real work.
