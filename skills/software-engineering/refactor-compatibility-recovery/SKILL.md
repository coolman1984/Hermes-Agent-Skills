---
name: refactor-compatibility-recovery
description: Recover from ImportError/AttributeError after refactors by tracing the removed public API through git history, then restoring a compatibility shim and verifying imports.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [debugging, refactor, importerror, compatibility, git-history]
---

# Refactor Compatibility Recovery

Use this when a refactor breaks existing callers with:
- ImportError
- AttributeError
- "cannot import name ..."
- a missing helper/function that used to exist

## Steps

1. Reproduce the failure and identify the missing symbol exactly.
2. Search the codebase for current callers and stale imports.
3. Use git history to find the last working definition:
   - `git log -S 'symbol_name' -- path/to/file`
   - `git show <commit>:path/to/file`
4. Restore a small compatibility shim if callers still depend on the old API.
   - Prefer preserving behavior over forcing every caller to change at once.
   - Keep the shim tiny and documented as compatibility-only.
5. Verify the file compiles and the old import works:
   - `python -m py_compile ...`
   - `python - <<'PY' ... import symbol ... PY`

## Pitfalls

- Don’t assume a missing symbol means the new implementation is wrong; it may just be an API break.
- Don’t change multiple behaviors at once while recovering compatibility.
- If the dependency package changed shape, check whether the import path itself moved before changing the business logic.

## Good outcome

Existing imports stop failing immediately, and the refactor can proceed without breaking downstream code.