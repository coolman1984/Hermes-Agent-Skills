# 2026-05-14 — Telegram connected but agent crashes after Hermes update

## Symptom
Telegram gateway process is alive and `gateway_state.json` reports:

- `gateway_state=running`
- `telegram.state=connected`
- PID exists under `/proc/<pid>`

But Telegram messages receive an error/no useful reply. Gateway logs show agent initialization failures:

```text
ImportError: cannot import name 'OpenAI' from 'openai' (unknown location)
RuntimeError: Failed to initialize OpenAI client: cannot import name 'OpenAI' from 'openai' (unknown location)
```

## Root cause
In Android/proot after `hermes update`, uv dependency installation partially corrupted the `openai` package inside the Hermes venv. `uv pip show openai` still reported `openai==2.24.0`, but Python saw it as a namespace package with no `__init__.py`:

```text
spec= ModuleSpec(name='openai', loader=None, submodule_search_locations=_NamespacePath([.../site-packages/openai]))
origin= None
openai.__file__ = None
has OpenAI = False
```

So status checks that only verify package metadata are insufficient.

## Diagnosis commands

```bash
PY=/root/.hermes/hermes-agent/venv/bin/python
$PY - <<'PY'
import sys, importlib.util
print('sys.executable=', sys.executable)
spec = importlib.util.find_spec('openai')
print('spec=', spec)
print('origin=', spec.origin if spec else None)
print('locations=', spec.submodule_search_locations if spec else None)
try:
    import openai
    print('openai file=', getattr(openai, '__file__', None))
    print('has OpenAI=', hasattr(openai, 'OpenAI'))
except Exception as e:
    print('import exception=', repr(e))
PY
```

Healthy output must include a real file like:

```text
.../site-packages/openai/__init__.py
has OpenAI=True
```

## Fix
Use explicit Hermes venv Python and `UV_LINK_MODE=copy`. Remove the corrupted package directory and dist-info first; reinstalling over a namespace directory may not be enough.

```bash
cd /root/.hermes/hermes-agent
export UV_LINK_MODE=copy
PY=/root/.hermes/hermes-agent/venv/bin/python
SITE=$($PY - <<'PY'
import site
print(site.getsitepackages()[0])
PY
)
rm -rf "$SITE/openai" "$SITE"/openai-*.dist-info
/root/.local/bin/uv pip install --python "$PY" --reinstall --no-cache openai==2.24.0
/root/.local/bin/uv pip install --python "$PY" -e .
```

## Verify before restarting Telegram

```bash
/root/.hermes/hermes-agent/venv/bin/python - <<'PY'
import openai
from openai import OpenAI, AsyncOpenAI
print(openai.__file__)
print(openai.__version__)
print(OpenAI)
print(AsyncOpenAI)
PY
hermes chat -q 'Reply with exactly: OK' --toolsets ''
```

Then restart exactly one primary `/root/.hermes` gateway and check logs for fresh `Agent error` / `ImportError` markers.

## Lesson
After Hermes updates in proot, do not trust `hermes --version` and `uv pip show` alone. Verify runtime imports with the same Python used by the gateway.