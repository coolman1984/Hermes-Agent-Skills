# 2026-05-18 Hermes update in Android/PRoot: v0.13.0 → v0.14.0

## Context
Hermes was running in Linux aarch64 PRoot/Android with no working systemd user bus. Telegram gateway was active before update.

## Baseline
- `hermes --version` showed `Hermes Agent v0.13.0 (2026.5.7)` and `Update available`.
- Git was behind upstream.
- Telegram gateway was running and connected.

## Safe sequence that worked
1. Stop the real live gateway PID from `/root/.hermes/gateway_state.json` with `TERM`, then `KILL` only if still alive.
2. Remove stale gateway files:
   - `/root/.hermes/gateway_state.json`
   - `/root/.hermes/gateway.pid`
   - `/root/.hermes2/gateway_state.json`
   - `/root/.hermes2/gateway.pid`
3. Run:
   `hermes update --backup --yes`
4. If update times out or shows uv hardlink/copy failures, repair explicitly:
   ```bash
   cd /root/.hermes/hermes-agent
   export UV_LINK_MODE=copy
   /root/.local/bin/uv pip install --python /root/.hermes/hermes-agent/venv/bin/python -e .
   ```
5. Verify:
   - `hermes --version`
   - `git -C /root/.hermes/hermes-agent status -sb`
   - exact runtime import:
     ```bash
     /root/.hermes/hermes-agent/venv/bin/python - <<'PY'
     import openai
     from openai import OpenAI
     print(openai.__file__)
     print(openai.__version__)
     print(OpenAI)
     PY
     ```
   - `hermes doctor`
6. Restart exactly one primary gateway as a tracked background process:
   `env HERMES_HOME=/root/.hermes PYTHONUNBUFFERED=1 /root/.local/bin/hermes gateway run --replace`
7. Verify gateway via process list, `/root/.hermes/gateway_state.json`, and fresh `gateway.log` startup lines.

## Failure pattern seen
`hermes update --backup --yes` created a backup and updated code/package metadata, but dependency installation hit PRoot/uv errors such as:
- `Failed to hardlink files; falling back to full copy`
- `failed to hardlink file ... Operation not permitted`
- `Failed to copy ... No such file or directory`
- failures around optional wheels like `google-api-python-client`, `uvicorn`, `agent-client-protocol`

The important lesson is not the exact package name; it is that PRoot can fail during uv hardlink/copy operations. The fix is to rerun the editable install with `UV_LINK_MODE=copy` against the exact Hermes venv Python.

## Successful final state
- `hermes --version` showed `Hermes Agent v0.14.0 (2026.5.16)` and `Up to date`.
- Git `main...origin/main` was aligned.
- OpenAI runtime import worked.
- Doctor passed critical checks; remaining warnings were optional credentials/tools.
- Gateway restarted with one live process and Telegram `connected`.
