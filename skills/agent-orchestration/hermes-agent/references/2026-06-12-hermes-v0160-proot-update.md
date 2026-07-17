# Hermes v0.16.0 update in Android/PRoot — 2026-06-12

Purpose: preserve the reusable maintenance pattern, not the one-off task log.

## Situation

Mohamed asked whether Hermes Agent had an update, then asked to update. The local checkout initially reported:

- `hermes --version`: Hermes Agent v0.15.1 (2026.5.29)
- `git describe`: `v2026.5.29-202-gbb79bcde6`
- branch behind `origin/main`
- latest official release found: v0.16.0 / v2026.6.5, "The Surface Release"

The active environment was Linux aarch64 / PRoot-like, where systemd status and uv hardlink behavior can be unreliable.

## Useful sequence

1. Loaded the Hermes reference skill.
2. Checked live local version, git status, git describe, recent commits, and remote tags.
3. Checked the GitHub release page for `v2026.6.5`.
4. Read `/root/Documents/Obsidian Vault/CURRENT-SNAPSHOT.md` before the important maintenance operation.
5. Captured baseline version/git/gateway state.
6. Checked for gateway processes and stale state files.
7. Ran:

```bash
export UV_LINK_MODE=copy
hermes update --backup --yes
```

8. The update command timed out after 600s during later npm-related work, but output showed the core Python package update had succeeded:

```text
- hermes-agent==0.15.1
+ hermes-agent==0.16.0
```

9. Inspected state instead of assuming success/failure:

```bash
hermes --version
git -C /root/.hermes/hermes-agent status -sb
git -C /root/.hermes/hermes-agent describe --tags --always --dirty
ps -efww | grep -E 'hermes update|npm|node|electron|uv pip|pip install' | grep -v grep || true
```

10. Explicitly repaired/reinstalled the editable package:

```bash
cd /root/.hermes/hermes-agent
export UV_LINK_MODE=copy
/root/.local/bin/uv pip install --python /root/.hermes/hermes-agent/venv/bin/python -e .
```

11. Migrated and verified:

```bash
yes '' | hermes config migrate || true
hermes config check || true
hermes doctor || true
hermes --version || true
git -C /root/.hermes/hermes-agent status -sb || true
git -C /root/.hermes/hermes-agent describe --tags --always --dirty || true
```

## Final verified state

- `hermes --version`: Hermes Agent v0.16.0 (2026.6.5), upstream `6b407364`
- config migrated from version 24 to 29
- `hermes doctor`: version files consistent, config up to date, core command install OK, main connectivity OK
- branch aligned with `origin/main`
- no gateway was running before or after, so no gateway was restarted
- pre-update backup path was reported and should be included in final summaries

## Lesson

If `hermes update` times out after a visible core package update, treat it as an ambiguous partial completion. Verify live state, run the explicit editable reinstall with `UV_LINK_MODE=copy`, then rely on `hermes doctor` and `hermes --version` rather than package metadata queried from an arbitrary Python interpreter.
