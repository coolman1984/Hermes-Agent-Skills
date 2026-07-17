---
name: uv-install-triage
description: Triage uv sync / uv pip install failures caused by editable installs, namespace packages, or broken build environments. Use when uv installs succeed partially, packages import as namespace packages, or hatchling/pluggy/build-backend errors appear.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [uv, packaging, install, editable, hatchling, pluggy, namespace-packages, debugging]
---

# uv Install Triage

Use this skill when a project installs partially with uv, but then fails during editable build, package import, or backend hook execution.

## Symptom patterns
- `uv sync` stops during build of a local workspace member
- `hatchling.build.build_editable` fails
- `pluggy.HookimplMarker` / `HookspecMarker` is missing
- Imported dependency looks like a namespace package (`__file__ is None`, no `__init__.py`)
- `uv` works in a normal venv / pip environment but fails in uv-managed build envs
- Workspace/local-source installs behave differently in Docker or CI

## Core rule
Do not guess the fix from the first failure.
First determine whether the failure is:
1. a broken build backend environment,
2. a uv cache / reinstall issue,
3. a namespace-package layout issue,
4. or a workspace source-resolution issue.

## Workflow

### 1) Reproduce with verbosity
Run the failing command with maximum useful logging.

Examples:
- `uv sync --python 3.12 -v`
- `uv sync --no-cache --python 3.12`
- `uv pip install --no-cache --python /path/to/python <pkg>`

Capture the exact last failing component, not just the summary line.

### 2) Check whether the failure is build-backend related
If the error mentions hatchling, pluggy, editable builds, or build hooks:
- inspect the local package `pyproject.toml`
- verify `[build-system]` requirements
- if editable installs are used, confirm `editables` is included when needed
- check whether the backend is trying to build a package that is not laid out as an actual package

### 3) Compare uv vs a control venv
Create a clean control environment with standard `venv` + `pip`.
Test the suspected package there.

Useful checks:
- `python -c "import pkg; print(pkg.__file__)"`
- `python -c "import pkg; print(hasattr(pkg, 'HookimplMarker'))"`
- inspect whether the package directory contains `__init__.py`

If pip works but uv does not, suspect uv cache / build isolation / install-mode behavior.

### 4) Test cache and reinstall hypotheses
Before changing project code, try the smallest install-side recovery steps:
- `uv sync --no-cache`
- `uv sync --reinstall-package <name>`
- delete the venv and recreate it
- if workspace sources are being resolved unexpectedly, try `--no-sources` in the relevant install/export step

### 5) Check layout / packaging assumptions
Look for these common pitfalls:
- two packages writing into the same namespace path
- namespace packages plus editable installs
- missing `__init__.py` causing imports to resolve as namespace packages
- a build backend configured for one layout but a different on-disk layout exists

When namespace packages are involved, prefer the simplest stable structure:
- isolated packages with distinct import roots, or
- explicit package layout with clear ownership boundaries

### 6) Verify the actual imported module
Do not stop at “installed successfully.”
Run a direct import probe in the target environment:
- `import pkg`
- print `pkg.__file__`
- print key attributes expected by the build/runtime path

This catches cases where the install completed but the package is effectively broken.

## Proven fixes observed
- `UV_LINK_MODE=copy` when hardlinking is not allowed by the filesystem
- `uv sync --no-cache` when uv reuses a bad cached build/install artifact
- adding `editables` to build-system requirements for editable local packages
- using `--no-sources` for Docker/Lambda style installs where workspace sources should not be treated as editable dependencies
- preferring non-namespace package layouts when editable installs become fragile

## What not to do
- Don’t assume the first backend traceback names the real root cause
- Don’t patch multiple packaging knobs at once
- Don’t trust a successful `uv sync` without a direct import check
- Don’t rely on namespace packages if editable installs are already unstable

## Quick verification checklist
- [ ] Reproduced with `-v`
- [ ] Compared against a clean pip/venv control
- [ ] Tested `--no-cache`
- [ ] Tested `--reinstall-package` or fresh venv
- [ ] Verified `__file__` and expected attributes in the target environment
- [ ] Confirmed whether the issue is backend, cache, layout, or workspace source resolution
