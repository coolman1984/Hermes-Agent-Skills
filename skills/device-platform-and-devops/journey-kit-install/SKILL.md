---
name: journey-kit-install
description: Install and verify Journey kits from journeykits.ai, including openclaw-target
  bundles and Termux compatibility fixes
tags: [journey-kits, workflows, install, skills, cli]
---

# Journey Kit Install

Use this skill when a user wants to install reusable workflows from Journey kits.

## What worked

- Install the Journey skill package first:
  ```bash
  npx skills add journeykits/skill -g -y
  ```
- Query Journey for matches with:
  ```bash
  POST https://journeykits.ai/api/kits/match
  ```
  or search with:
  ```bash
  GET https://journeykits.ai/api/kits/search?q=<query>
  ```
- Install a kit with a target-specific response:
  ```bash
  GET https://journeykits.ai/api/kits/<owner>/<slug>/install?target=openclaw&ref=latest
  ```
- Write every returned file exactly under the suggested root directory.
- Read `kit.md` first; it is the primary workflow guide.

## Practical workflow

1. Fetch the Journey skill doc if needed:
   ```bash
   curl -fsSL https://journeykits.ai/api/kits/journey
   ```
2. Search or match kits.
3. Fetch the install payload with `?target=openclaw&ref=latest`.
4. Write files preserving the exact relative paths.
5. Run the kit’s preflight checks.
6. Run the verification command if provided.
7. Read `kit.md` and follow its Setup + Steps sections.

## Important pitfalls

- Do not use `/install` without `?target=`; that returns a raw bundle instead of structured install guidance.
- Some bundles may nest files under `src/src/`. If that happens, flatten the extra `src/` level so files end up at the paths declared in `kit.md`.
- On Termux/Android, native Node modules may fail to build. `better-sqlite3` is a common example.
  - If the kit only needs to load for local workflow validation, a small compatibility shim may be enough.
  - If the kit needs real SQLite behavior, prefer Linux/macOS or a compatible native build environment.
- Verify each installed kit with the exact command from its `verification` field when possible.

## Example checks

```bash
node --version
python3 --version
sqlite3 --version
```

For OpenClaw-target kits, also check relevant runtime config such as Telegram or cron availability.

## Good targets

- `openclaw`
- `codex`
- `claude-code`
- `generic`

## When to stop

Stop after:
- the files are installed,
- the required preflight checks are run,
- the verification command passes or the environment limitation is clearly identified,
- and the kit’s root `kit.md` has been reviewed.
