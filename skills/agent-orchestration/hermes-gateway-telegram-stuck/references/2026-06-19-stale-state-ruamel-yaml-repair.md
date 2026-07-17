# 2026-06-19 — Telegram stale running state + ruamel.yaml namespace repair

## Symptom
Telegram bot appeared not to work correctly. `hermes gateway status` reported stopped in the PRoot environment, while `/root/.hermes/gateway_state.json` still claimed the gateway was `running` and Telegram was `connected`.

## Ground truth checks
- Process list had no live `gateway run` process.
- `gateway_state.json` pointed at an old PID that no longer existed under `/proc`.
- Telegram Bot API `getMe` succeeded for the active token, proving the token and Telegram API path were basically healthy.
- After cleanup/restart, gateway connected, but logs also exposed `cannot import name 'YAML' from 'ruamel.yaml' (unknown location)` during config saves.

## Recovery pattern
1. Treat process + `/proc/<pid>` + state + Bot API as authoritative; do not trust systemd status in PRoot.
2. Remove stale state files when the state PID is absent:
   ```bash
   rm -f /root/.hermes/gateway_state.json /root/.hermes/gateway.pid
   ```
3. Verify Bot API with the token from `/root/.hermes/.env` using `getMe`.
4. Start one primary gateway from inside Hermes with `terminal(background=true)`, not `nohup`.
5. If logs show `cannot import name 'YAML' from 'ruamel.yaml' (unknown location)`, repair the runtime package with the gateway venv:
   ```bash
   cd /root/.hermes/hermes-agent
   export UV_LINK_MODE=copy
   PY=/root/.hermes/hermes-agent/venv/bin/python
   SITE=$($PY - <<'PY'
import site
print(site.getsitepackages()[0])
PY
)
   rm -rf "$SITE/ruamel" "$SITE"/ruamel.yaml-*.dist-info "$SITE"/ruamel_yaml-*.dist-info
   /root/.local/bin/uv pip install --python "$PY" --reinstall --no-cache 'ruamel.yaml>=0.18.0'
   ```
6. Verify import before restarting again:
   ```bash
   /root/.hermes/hermes-agent/venv/bin/python - <<'PY'
from ruamel.yaml import YAML
from openai import OpenAI
print('imports OK')
PY
   ```
7. Restart the gateway after package repair and verify:
   - exactly one gateway process
   - `gateway_state=running`
   - Telegram `connected`
   - state PID exists under `/proc`
   - Bot API `getMe` succeeds
   - `hermes chat -q 'Reply with exactly: OK' --source telegram -Q --toolsets ''` returns `OK`

## Pitfall
Immediately after starting the gateway, `gateway_state.json` may not exist yet while the process is still initializing. Wait and check logs before assuming startup failed. In this case the state appeared after Telegram connected.

## Durable lesson
A gateway outage can combine a stale state file with a corrupted runtime dependency. Fix the stale state first, then scan recent `errors.log`/`gateway.log` for import failures and repair the exact gateway venv before the final restart.