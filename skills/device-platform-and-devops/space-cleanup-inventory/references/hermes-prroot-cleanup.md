# Hermes / PRoot cleanup reference

Session pattern captured:
- User wanted anything broken removed and anything slowing the device removed.
- Correct approach was selective cleanup, not broad deletion.

## Verified reclaim path that worked well
Low-risk removals that reclaimed several GB without touching core Hermes state:
- `~/.cache/pip`
- `~/.cache/huggingface`
- `~/.cache/uv`
- `~/.cache/pnpm`
- `~/.cache/node-gyp`
- `~/.cache/hyperframes`
- `~/.cache/opencode`
- `~/.cache/typescript`
- `~/.cache/mesa_shader_cache`
- `~/.cache/codebase-memory-mcp`
- `~/.cache/puppeteer`
- failed test venvs under `/root/tools/`
- broken package remnants like `~elenium` beside a valid `selenium`

## Things intentionally preserved
- `gbrain` because it was installed and healthy
- `~/.cache/ms-playwright*` because Hermes browser tooling was clearly active
- `~/.cache/camoufox` because it may still be needed and its deletion only saves space at the cost of re-download/setup time
- Hermes durable state: `backups`, `sessions`, `checkpoints`, `state-snapshots`, `state.db*`

## Decision rule
If the user says 'remove broken things' or 'remove what slows the device', default to:
1. remove failed installs and stale caches first
2. keep active automation/browser assets unless the user wants an aggressive reset
3. avoid Hermes history/recovery folders without explicit approval
4. verify a kept core tool still works after cleanup

## Verification pattern
- compare disk free space before/after
- run a health check on one intentionally preserved tool
- verify broken package remnants are gone while the valid package remains
