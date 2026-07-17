# 2026-06-16: Telegram Flood Control Delays

## Incident
- **When:** 2026-06-16 ~07:46–07:48 UTC
- **Symptom:** Mohamed reported Telegram "not working correctly"
- **Root cause:** Two separate issues叠加:
  1. Gateway process (PID 13911) had crashed/died — stale state file remained
  2. Before crash, Telegram flood control triggered repeatedly during a long multi-chunk response

## Log signatures

### Flood control (gateway alive, Telegram rate-limiting):
```
2026-06-16 07:46:52 WARNING gateway.platforms.telegram: [Telegram] Telegram flood control, waiting 123.0s
2026-06-16 07:48:14 WARNING gateway.platforms.telegram: [Telegram] Telegram flood control on send (attempt 1/3), retrying in 41.0s: Flood control exceeded. Retry in 41 seconds
```

### Gateway crash (stale state, no process):
```
$ hermes gateway status
✗ User gateway service is stopped
⚠ Gateway process is running for this profile, but the service is not active

$ ps -p 13911
PID 13911 not running

$ cat ~/.hermes/gateway_state.json
{"pid":13911, ... "gateway_state":"running", "platforms":{"telegram":{"state":"connected"}}}
```

## Diagnosis sequence
1. `hermes gateway status` → reported stopped (systemd bus unavailable in PRoot)
2. `ps -p 13911` → PID not running (confirmed crash)
3. `cat gateway_state.json` → stale: claimed running + connected
4. `grep TELEGRAM_BOT_TOKEN ~/.hermes/.env` → token present (not a config issue)

## Fix applied
```bash
rm -f ~/.hermes/gateway_state.json
hermes gateway run --replace   # via terminal(background=true)
```

## Verification after restart
```
11:40:17 INFO [Telegram] Connected to Telegram (polling mode)
11:40:18 INFO Gateway running with 1 platform(s)
```
gateway_state.json: pid=4206, state=running, telegram=connected

## Key lessons
- Flood control and gateway crash are **distinct** failure modes — check logs to distinguish
- Flood control resolves itself; do NOT restart for it alone
- In PRoot, `systemctl --user` always fails — use `hermes gateway run --replace` directly
- Stale state file is the #1 misleading signal: always cross-check PID against `/proc`
