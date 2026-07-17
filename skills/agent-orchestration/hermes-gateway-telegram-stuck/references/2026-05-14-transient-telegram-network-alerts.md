# 2026-05-14 — Transient Telegram network alerts vs real gateway failure

## Context
A long-running tracked gateway process (`proc_14e929cd0535`, PID `5651`) repeatedly matched the watch pattern `Telegram network error` after earlier clean restart and OpenAI dependency repair.

The alerts included:
- `httpx.ConnectError: All connection attempts failed`
- `httpx.ReadError`
- `httpx.RemoteProtocolError: Server disconnected without sending a response`
- `Network Retry Loop (Bootstrap delete Webhook)` tracebacks

## What mattered
The alerts did not automatically mean Telegram was down. In this incident:
- The gateway process remained alive.
- `/root/.hermes/gateway_state.json` still showed `gateway_state=running`, `telegram.state=connected`, and `telegram.error_message=null`.
- No duplicate `/root/.hermes2` gateway was present.
- Direct Telegram Bot API `getMe` succeeded repeatedly with ~0.5s latency.
- Logs showed recovery lines such as `Telegram polling resumed after network error`.

## Diagnostic sequence used
```bash
# 1) Poll the tracked process if it exists
# process poll/log via tool, or ps fallback
ps -efww | grep -E 'gateway run|hermes.*gateway' | grep -v grep || true

# 2) Check state and that PID exists
python3 - <<'PY'
import json, pathlib
s=json.loads(pathlib.Path('/root/.hermes/gateway_state.json').read_text())
pid=s.get('pid')
print({
  'pid': pid,
  'pid_exists': pathlib.Path(f'/proc/{pid}').exists() if pid else False,
  'gateway_state': s.get('gateway_state'),
  'telegram_state': s.get('platforms',{}).get('telegram',{}).get('state'),
  'telegram_error': s.get('platforms',{}).get('telegram',{}).get('error_message'),
  'active_agents': s.get('active_agents'),
})
PY

# 3) Inspect network events and specifically look for recovery
awk '$1=="2026-05-14" && $2>="15:58:00" {print}' /root/.hermes/logs/gateway.log \
  | grep -Ei 'Telegram network error|polling resumed|reconnect failed|Primary api|Fallback IP|ConnectError|ReadError|RemoteProtocolError' \
  | tail -120

# 4) Probe Bot API without printing token
python3 - <<'PY'
import re, json, urllib.request, time
text=open('/root/.hermes/.env','r',errors='replace').read()
m=re.search(r'^TELEGRAM_BOT_TOKEN=(.+)$', text, re.M)
print('token_present=', bool(m))
if not m: raise SystemExit
TOKEN=m.group(1).strip().strip('"\'')
print('token_len=', len(TOKEN))
for i in range(3):
    t=time.time()
    try:
        with urllib.request.urlopen(f'https://api.telegram.org/bot{TOKEN}/getMe', timeout=12) as r:
            data=json.loads(r.read().decode())
        print(i+1, 'ok', round(time.time()-t,2), data.get('ok'), data.get('result',{}).get('username'))
    except Exception as e:
        print(i+1, 'ERR', round(time.time()-t,2), type(e).__name__, str(e)[:200])
    time.sleep(2)
PY
```

## Decision rule
Do not restart only because a watch pattern fires.

Restart only if one of these is true:
- gateway process is dead or PID in state does not exist
- state is stopped/error or Telegram state is not connected
- network errors continue without a later `polling resumed` line
- Bot API probes fail repeatedly
- duplicate local poller/token lock is found
- user reports no replies and logs show no inbound/response progress

If the gateway is alive, Bot API is healthy, and logs show `polling resumed`, classify as transient network/DNS/API instability and avoid interrupting a working gateway.

## Separate failure noticed
During the same window, Telegram delivered a YouTube message, but the agent hit an internal tool error:
`Tool execute_code returned error ... SyntaxError ... Arabic text`

That is not Telegram connectivity. Separate Telegram delivery from downstream agent/tool failures:
- check inbound message lines
- check response-ready or agent/tool error lines
- verify package imports if needed (`from openai import OpenAI`)
