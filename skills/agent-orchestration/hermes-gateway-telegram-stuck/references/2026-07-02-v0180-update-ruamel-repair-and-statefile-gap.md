# v0.18.0 update + Telegram gateway verification gap in PRoot

Use this note when Hermes was updated in the Android/PRoot environment and Telegram needs post-update verification.

## What happened
- `hermes update --backup --yes` completed successfully and upgraded Hermes from `v0.17.0` to `v0.18.0` (`v2026.7.1`, upstream `88d1d620`).
- `hermes config migrate` advanced config from version `30` to `32`.
- Runtime import verification then failed with:
  - `ImportError: cannot import name 'YAML' from 'ruamel.yaml' (unknown location)`
- Telegram Bot API `getMe` still worked, so the token/network path was not the blocker.

## Durable fix
Repair `ruamel.yaml` inside the exact Hermes venv after update:

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

Then verify:

```bash
/root/.hermes/hermes-agent/venv/bin/python - <<'PY'
from openai import OpenAI
from ruamel.yaml import YAML
print('imports OK')
PY
```

## Telegram/gateway verification pattern after the update
After restarting the gateway with:

```bash
env HERMES_HOME=/root/.hermes PYTHONUNBUFFERED=1 /root/.local/bin/hermes gateway run --replace
```

we observed this combination:
- gateway process alive
- Bot API `getMe` healthy
- CLI smoke test `hermes chat -q 'Reply with exactly: OK' --source telegram -Q --toolsets ''` succeeded
- but `gateway_state.json` still missing during the early verification window
- log tail still showed only the previous shutdown lines, not fresh connection lines yet

## Operational lesson
Do not classify the restart as failed solely because `gateway_state.json` is missing right after a post-update restart in this environment. If the process is alive, import checks pass, Bot API works, and CLI smoke succeeds, keep monitoring instead of bouncing the gateway again immediately.

Prioritized checks:
1. runtime import check (`openai`, `ruamel.yaml`)
2. live process check
3. Bot API `getMe`
4. CLI smoke test with `--source telegram`
5. `gateway_state.json` and fresh log lines as secondary confirmation

## Extra note
`hermes config migrate` on this update also surfaced:
- `platform 'telegram' references unknown toolset 'moa' — did you mean 'hermes-telegram'?`

Treat that as a configuration cleanup item to review if Telegram behavior stays odd after the runtime/import path is healthy.