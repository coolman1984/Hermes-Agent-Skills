---
name: hermes-openclaw-wrapper-fixes
description: Troubleshoot Hermes wrappers that sit behind an OpenClaw gateway, fix pairing/token issues, and verify the wrapper actually talks to the gateway.
version: 1.0.1
author: Hermes Agent
license: MIT
metadata:
  tags: [hermes, openclaw, wrapper, pairing, gateway, token, troubleshooting]
---

# Hermes + OpenClaw Wrapper Fixes

Use this skill when a Hermes wrapper works locally but fails through OpenClaw with errors like:
- `gateway closed (1008): pairing required`
- gateway timeout on `openclaw status` or `openclaw gateway call ...`
- wrapper starts Hermes but the gateway rejects the CLI because it has no auth token

## Goal
Make the wrapper self-sufficient by loading the correct OpenClaw gateway token and then verify the Hermes agent can talk to the gateway end-to-end.

## Workflow

1. Inspect the wrappers
   - Look for wrapper scripts in `/root/.local/bin` (or the user’s equivalent).
   - Identify which wrapper launches Hermes and which wrapper launches OpenClaw.
   - Check whether the wrapper already exports `HERMES_HOME` and `PATH` correctly.

2. Check OpenClaw gateway state
   - `openclaw status`
   - `openclaw gateway status`
   - `openclaw gateway call health`
   - If the CLI hangs with systemd/user-bus noise in a container, rely on `openclaw gateway call health` instead of `status`.

3. Fix pairing when needed
   - If `openclaw devices list` shows a pending request, approve it:
     `openclaw devices approve --latest`
   - Re-check `openclaw devices list --json` to confirm `pending` is empty.

4. Inject the gateway token into wrappers
   - If the wrapper talks to OpenClaw, export `OPENCLAW_GATEWAY_TOKEN` before `exec`ing Hermes or OpenClaw.
   - Best source of truth: `/root/.openclaw/openclaw.json` (or the user’s OpenClaw config).
   - Example pattern:

```bash
export OPENCLAW_GATEWAY_TOKEN="${OPENCLAW_GATEWAY_TOKEN:-$(python - <<'PY'
import json
from pathlib import Path
cfg = json.loads(Path('/root/.openclaw/openclaw.json').read_text())
print(cfg['gateway']['auth']['token'])
PY
)}"
```

   - Use the same pattern in sibling wrappers if they are meant to be equivalent.
   - If the wrapper is supposed to message Telegram, also check the wrapper-specific `.env` for `TELEGRAM_BOT_TOKEN` and `TELEGRAM_ALLOWED_USERS`; those are often the real source of truth for delivery even when the OpenClaw gateway is healthy.
   - In multi-instance setups (`/root/.hermes`, `/root/.hermes-test`, mobile variants), resolve which instance owns the target bot first: run Bot API `getMe` for each token and match expected username before changing anything.
   - When Telegram startup fails with a token rejection / `InvalidURL` / weird duplicated token string in logs, assume the token value is corrupted or includes hidden/control characters from paste/edit mistakes. Re-read the token from the actual `.env` file, verify it with Bot API `getMe`, then replace with a clean known-good token.
   - Prefer restoring from a known-good backup or re-copying the token cleanly over hand-editing guessed fixes.
   - For Hermes-native diagnosis, trust `~/.hermes/logs/gateway.log` and `hermes gateway status` last-shutdown reason: they clearly surface token rejection and later successful reconnect (`Connected to Telegram (polling mode)`).

- Specifically grep for `embedded_run_agent_end`, `embedded_run_failover_decision`, and `401 Model ... not supported`. If present, fix `agents.defaults.model.primary` in `~/.openclaw/openclaw.json` to a supported model, restart gateway, and verify the runtime log line `agent model:` reflects the new value.

5. Verify the wrapper end-to-end
   - Hermes wrapper:
     `wrapper-name chat -q 'reply with just OK'`
   - Hermes checks:
     `wrapper-name status`
     `wrapper-name doctor`
   - OpenClaw checks:
     `openclaw gateway call health`
     `openclaw status` if it is responsive
   - For Telegram delivery, if the OpenClaw message path hangs or is flaky, send a direct Bot API `sendMessage` to the target chat using the wrapper’s bot token to confirm the bot itself works before blaming Hermes or OpenClaw.
   - If user says "bot not responding", check the primary Hermes instance first (`/root/.hermes/.env`) before OpenClaw-global configs. In this environment, the critical bot is `@N8N_mflma1984_bot`.

6. Add a permanent anti-stall watchdog (Termux/headless)
   - When gateway polling silently stalls, implement a lightweight supervisor loop script that:
     - enforces single gateway instance,
     - checks gateway log freshness (idle threshold),
     - validates bot token via Bot API `getMe`,
     - restarts gateway if stale.
   - Keep logs under a dedicated path (example: `/root/service-logs/hermes-main/supervisor.log`).
   - Validate by confirming both processes are running (`hermes gateway run` + supervisor) and that `getUpdates` returns `200 OK` in `~/.hermes/logs/gateway.log`.

7. Ensure restart persistence on Android/Termux
   - Wire supervisor startup into the Termux boot entrypoint (`~/.termux/boot/openclaw.sh` or equivalent) so recovery survives reboots.
   - Syntax-check boot and supervisor scripts (`bash -n ...`) and test one-shot supervisor run (`--once`) before finishing.

5. Verify the wrapper end-to-end
   - Hermes wrapper:
     `wrapper-name chat -q 'reply with just OK'`
   - Hermes checks:
     `wrapper-name status`
     `wrapper-name doctor`
   - OpenClaw checks:
     `openclaw gateway call health`
     `openclaw status` if it is responsive

## Version and update checks (when CLI is missing)

In some environments, OpenClaw exists as a git checkout but `openclaw` is not on `PATH`.

Recommended sequence:
1. Check for source checkout first (common path: `/root/workspace/tools-lab/openclaw`).
2. Read version from repo metadata:
   - `package.json` → `version`
   - `git rev-parse --short HEAD` for exact running source state
3. Before updating, stash local edits (especially lockfiles), then fast-forward:
   - `git stash push -u -m "pre-update-<timestamp>"`
   - `git pull --ff-only origin main`
4. If stash pop creates lockfile conflicts (e.g., `pnpm-lock.yaml`), keep updated upstream lockfile by restoring `HEAD` copy and keep stash entry for manual re-apply.
5. Re-verify with `package.json` version + commit hash, then confirm clean working tree.

## Common pitfalls

- A wrapper may pass local `status`/`doctor` but still fail to reach the gateway if the token is missing.
- `openclaw status` and `hermes gateway status` can be misleading in containers or headless environments where systemd user services / linger are unavailable; trust the foreground gateway logs and `gateway call health` instead.
- A stale or wrong token in the wrapper is more common than a broken Hermes install.
- Telegram delivery failures can be caused by model/provider auth problems (`401 model not supported`) even when channel logs mention polling/network noise; always correlate Telegram errors with embedded-agent errors.
- If `hermes gateway restart` refuses to work because linger is not enabled, start the gateway in foreground with the proper environment sourced instead of fighting systemd.
- If `openclaw gateway run --force` fails because the port is still in TIME_WAIT, that is usually transient; use the existing running gateway if `gateway call health` is already OK.
- A hidden Unicode character in AGENTS.md / prompt files can block prompt construction; strip zero-width characters before retrying if you see a loader warning about invisible unicode.
- On Android/PRoot hybrids, global `openclaw` can install successfully but still crash at runtime if `/usr/bin/node` is too old. OpenClaw 2026.5.x requires Node >= 22.12; verify the actual node used by the launcher script, not just `node -v` in one shell.
- `openclaw doctor --fix` may exit non-zero on Android with `Gateway service install not supported on android`; treat this as a platform limitation, not necessarily a broken installation.
- If `openclaw gateway call health` times out while TCP connect to the same host:port succeeds, the socket layer is up but gateway RPC is wedged; restart the gateway process and re-check logs instead of only changing network settings.

## Recommended operator behavior

- Fix the wrapper, not the agent installation, unless `doctor` shows a real Hermes problem.
- Prefer `gateway call health` as the authoritative verification step.
- If multiple wrappers exist, patch them all consistently so they share the same gateway-token behavior.

## References
- `references/android-node-gateway-health.md` — Android/PRoot Node-runtime mismatch and gateway health-timeout triage pattern.

## Verification checklist

- [ ] `openclaw devices list --json` shows no pending approvals
- [ ] `openclaw gateway call health` returns `ok: true`
- [ ] Hermes wrapper `chat -q 'reply with just OK'` returns `OK`
- [ ] Hermes wrapper `doctor` shows only non-blocking warnings
