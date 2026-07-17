# Hermes update in Android/proot: uv hardlink and venv repair

Session pattern observed: Hermes update on Linux aarch64 PRoot/Android pulled the latest git code successfully, then dependency installation failed because uv attempted hardlink/copy operations that the filesystem did not support or could not complete.

Symptoms:
- `hermes update --backup --yes` reports it found and pulled many commits.
- Dependency install fails with errors like:
  - `Failed to hardlink files; falling back to full copy`
  - `Failed to install: croniter... failed to copy file ... No such file or directory`
  - `failed to hardlink ... Operation not permitted`
- A follow-up `uv pip install -e .` may say: `No virtual environment found` even though `/root/.hermes/hermes-agent/venv` exists.
- `git -C /root/.hermes/hermes-agent status -sb` may show up to date while `hermes --version` shows runtime packages missing, e.g. `OpenAI SDK: Not installed`.
- Gateway may remain stopped because the update killed it and no systemd user bus exists to revive it.

Reliable repair:
```bash
cd /root/.hermes/hermes-agent
export UV_LINK_MODE=copy
/root/.local/bin/uv pip install --python /root/.hermes/hermes-agent/venv/bin/python -e .
```

Then verify:
```bash
hermes --version
yes '' | hermes config migrate || true
hermes config check || true
hermes doctor || true
git -C /root/.hermes/hermes-agent status -sb
```

Gateway recovery after update:
```bash
pkill -f "gateway run --replace" 2>/dev/null || true
pkill -f "python.*gateway run" 2>/dev/null || true
rm -f /root/.hermes/gateway_state.json /root/.hermes/gateway.pid /root/.hermes2/gateway_state.json /root/.hermes2/gateway.pid
env HERMES_HOME=/root/.hermes PYTHONUNBUFFERED=1 /root/.local/bin/hermes gateway run --replace
```
Run the gateway command under the agent/tooling background-process mechanism when available, then verify process, state JSON, and logs.

Known-good final state from the session:
- Git: `main...origin/main` with no behind marker.
- Commit: `ddb8d8fa8 docs: update NovitaAI provider positioning (#25532)`.
- `hermes --version`: `Up to date`.
- `hermes doctor`: core checks pass; optional missing API keys/tools can remain warnings.
- Gateway state JSON: `gateway_state=running`, Telegram `state=connected`.
