# Silent Gateway Death — No Error in Logs (2026-06-15)

## Symptom

Mohamed reported Telegram not answering. Investigation found:
- `hermes gateway status`: "User gateway service is stopped" (misleading — DBUS/systemd missing in PRoot)
- `ps`: no gateway process alive
- `gateway_state.json`: claimed `pid: 8710`, `gateway_state: running`, `telegram.state: connected`
- `/proc/8710`: did not exist (stale state)
- Log at `/root/.hermes/logs/gateway.log`: normal activity until 11:16 AM, then **stops mid-work with no error, no traceback, no SIGTERM, no OOM kill**. Last line was a media group send — the log just ends.

## What makes this tricky

1. `hermes gateway status` is misleading in PRoot (says "stopped" due to missing DBUS) — the real signal is the dead PID + stale state file.
2. The log provides zero clues — no crash, no error. You only know it's dead by cross-checking the state PID against `/proc`.
3. If you only check `gateway_state.json` without verifying `/proc/<pid>`, you'd think it's running.

## Recovery

1. Confirmed PID 8710 absent from `/proc`
2. Removed stale state: `rm -f /root/.hermes/gateway_state.json /root/.hermes/gateway.pid`
3. Started new gateway via `terminal(background=true)` — `nohup` was rejected by the Hermes terminal tool (see SKILL.md pitfall)
4. Verified: `gateway_state.json` matches live PID 1428, `telegram.state: connected`, Bot API `getMe` OK, `active_agents: 0`
5. Total outage: ~80 minutes (11:16 → 12:35)

## Verification checklist that passed

- Exactly one gateway process
- `gateway_state.json` PID exists in `/proc`
- `telegram.state: connected`
- Bot API `getMe` returns expected bot username
- Log shows: "Connected to Telegram (polling mode)", "Gateway running with 1 platform(s)"
- No duplicate poller, no token lock, no sendChatAction spam
