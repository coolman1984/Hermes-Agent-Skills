---
name: space-cleanup-inventory
description: Practical workflow for finding removable disk-space clutter, estimating
  reclaimable space, and separating low-risk cleanup from medium/high-risk deletions.
tags: [disk-space, cleanup, inventory, storage, report]
---

# Space Cleanup Inventory

Use this skill when the user wants to free disk space, reduce clutter, or produce a cleanup report.

## Goal
Find the biggest removable storage consumers quickly, classify them by risk, and recommend a safe cleanup order.

## Workflow
1. Inspect the obvious large roots first.
   - Home subdirectories
   - Cache directories
   - Session/checkpoint folders
   - Download or bootstrap folders
   - Log folders
2. Drill down only into the largest folders.
3. Separate candidates into:
   - Low risk: caches, temporary package-manager artifacts, logs, clearly regenerable outputs
   - Medium risk: session histories, checkpoints, browser/bootstrap bundles, downloaded assets
   - High risk: state DBs, credentials, source repos, working trees, config, anything needed for startup or recovery
4. Estimate reclaimable space before deleting anything.
5. Prefer reversible cleanup first.
6. Report what was found, what is safe, and what should wait for confirmation.

## Practical inspection pattern
- Start with `du -sh` on top-level locations.
- Then inspect the largest directory’s immediate children.
- Repeat until the biggest offenders are obvious.
- If a directory scan is slow, use targeted child scans instead of a full recursive pass.

## Common low-risk targets
- `~/.cache/*`
- package-manager scratch data such as `~/.npm/_npx`, `~/.cache/pnpm`, `~/.cache/pip`, `~/.cache/node-gyp`
- temporary download caches
- append-only logs that already have a canonical source elsewhere
- stale, clearly regenerated build artifacts
- failed one-off virtualenvs or test sandboxes created during aborted installs
- broken Python package remnants that start with `~` and sit beside a valid installed package (cleanup the remnant, keep the valid package)

## Hermes / PRoot cleanup heuristics
Use these when cleaning Mohamed's Hermes environment on Android/PRoot after experiments, installs, or tool trials.

### Usually safe to remove
- tool-specific caches under `~/.cache/` when the tool can regenerate them
- heavy build/download caches such as `~/.cache/pip`, `~/.cache/huggingface`, `~/.cache/uv`, `~/.cache/pnpm`, `~/.cache/node-gyp`
- app/workflow caches such as `~/.cache/hyperframes`, `~/.cache/opencode`, `~/.cache/codebase-memory-mcp`, `~/.cache/typescript`, `~/.cache/mesa_shader_cache`
- leftover scratch browser caches not known to be part of the active automation path, e.g. `~/.cache/puppeteer`
- abandoned tool test folders under `/root/tools/`, especially failed venvs from package trials

### Verify before removing
- `~/.cache/ms-playwright*` and `~/.cache/camoufox` can be large, but keep them if browser automation is actively used; deleting them is reversible but will force re-downloads and may slow future tasks
- `/root/.hermes/agent-browser-bootstrap` is medium-risk: keep unless explicitly doing a browser-tool reset

### Do not remove without explicit intent
- `/root/.hermes/backups`
- `/root/.hermes/sessions`
- `/root/.hermes/checkpoints`
- `/root/.hermes/state-snapshots`
- `/root/.hermes/state.db*`

These are often the biggest folders, but they are operational history, recovery state, or durable context — not generic clutter.

### Post-cleanup verification
After cleanup, verify:
- disk free space improved
- the kept core tool still runs (example: `gbrain doctor`)
- the valid Python package still imports if a broken `~package` remnant was removed
- only the remnant was deleted, not the live package

Reference: `references/hermes-prroot-cleanup.md`

## Common medium-risk targets
- session histories
- checkpoints
- browser/bootstrap installations
- downloaded test assets
- generated indexes or graphs if they can be rebuilt

## High-risk targets
- state databases
- auth files and secrets
- active working repos
- config directories
- runtime state needed by supervisors or gateways

## Output format
Always return:
- Area inspected
- Biggest space consumers
- Low-risk cleanup candidates
- Medium-risk cleanup candidates
- High-risk items to avoid
- Estimated space reclaimable
- Recommended next action

## Notes
- If the environment is large or slow, prefer a quick size inventory over a full recursive listing.
- If the user only asked for a report, do not delete anything automatically.
- If anything looks like runtime state or credentials, stop and ask before removing it.
