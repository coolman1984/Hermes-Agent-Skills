---
name: journey-kits-install
description: Discover and install Journey kits via the Journey API, then verify the
  install and handle kit-specific prerequisites.
tags: [journey-kits, workflows, install, inspect, compare]
---

# Journey Kits Install

Use this skill when a user asks to install, inspect, or compare Journey kits/workflows.

## What I learned

- `npx skills add journeykits/skill -g -y` installs the Journey discovery skill itself, not arbitrary kits.
- Arbitrary kits must be fetched from the Journey API directly.
- The most useful flow is:
  1. search or match kits
  2. inspect the best match
  3. install with `?target=<agent>`
  4. write the returned files under the suggested root
  5. run preflight checks
  6. run verification if provided
- In practice, kits sometimes return a nested `src/src/...` layout; flatten that before trying to use the files.
- If a kit is a cron workflow, avoid creating follow-up cron jobs from within the job unless the kit explicitly requires recursive scheduling.

## Discovery

### Search by text
```bash
curl -sSL "https://journeykits.ai/api/kits/search?q=<urlencoded query>"
```

### Match by task
```bash
curl -sSL -X POST "https://journeykits.ai/api/kits/match" \
  -H 'Content-Type: application/json' \
  -d '{"task":"<task>","tools":["<tool1>"],"constraints":["<constraint>"]}'
```

### Inspect a kit
```bash
curl -sSL "https://journeykits.ai/api/kits/<owner>/<slug>"
```

### Check install targets
```bash
curl -sSL "https://journeykits.ai/api/install-targets"
```

## Install

Always include a target:

```bash
curl -sSL "https://journeykits.ai/api/kits/<owner>/<slug>/install?target=openclaw&ref=latest"
```

Useful targets:
- `openclaw`
- `cursor`
- `claude-code`
- `codex`
- `generic`

## Install procedure

1. Fetch the install payload with `?target=`.
2. Read `selfContained`.
   - If `false`, the kit needs an existing workspace or environment.
3. Install any `dependencyKits` first.
4. Write every file under `suggestedRootDir`, preserving relative paths exactly.
5. Respect `writeMode`:
   - `create` → create new file
   - `append` → append to existing file
6. Run each `preflightChecks[].check`.
7. If `verification` exists, run it.
8. Read `kit.md` first; it is the primary workflow guide.

## Important pitfalls

- Calling `/install` without `?target=` returns a raw bundle, not the structured install response.
- Some kits are not self-contained.
- Some kits require dependencies like Node, Python, SQLite, Ollama, or an API key.
- A kit can be installed successfully but still be unusable until its runtime dependencies are installed.
- `earnings-preview`-style kits may depend on OpenClaw cron/message tooling.
- `business-strategy-council`-style kits may require Node dependencies like `better-sqlite3`.
- On Termux/Android, native Node addons like `better-sqlite3` may fail to build; a shim can unblock import-time verification but is not a full runtime substitute.
- `second-brain`-style kits may be self-contained but still prefer optional local models or Ollama.
- Some Python Journey kits ship missing source files or stale imports; verify importability before marking them ready.

## Verification pattern

When available, run the verification command directly after install.

Example checks I used:
```bash
node --version
python3 --version
sqlite3 --version
node -e "require('better-sqlite3')"
PYTHONPATH=/path/to/kits/lalomorales__second-brain/src python3 -c "from semantic_gravity_memory import Memory; m = Memory(db_path=':memory:'); m.ingest('test'); s = m.recall('test'); print('OK:', len(s['crystals']), 'crystals')"
```

## Recommended output

When reporting to the user, include:
- installed kit refs
- local install roots
- which preflight checks passed or failed
- whether the kit is self-contained
- the first blocker if any
