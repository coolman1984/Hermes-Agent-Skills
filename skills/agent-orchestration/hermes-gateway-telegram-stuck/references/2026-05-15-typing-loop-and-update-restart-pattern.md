# 2026-05-15 / 2026-05-18 Telegram gateway stale typing and no-systemd update restarts

## Context
Telegram gateway runs inside Android/PRoot where systemd user services are unreliable or unavailable. `hermes gateway status` can say stopped even when the real foreground gateway process is alive; trust process/state/logs instead.

## Repeating pattern
The gateway can be healthy (`gateway_state=running`, Telegram `connected`) but Telegram shows a constant typing indicator. In the observed case:
- Exactly one gateway process existed.
- `active_agents=0` in `gateway_state.json`.
- Recent long responses had completed and `Sending response` was logged.
- No duplicate poller was found.
- Bot API `getMe` succeeded.

This looked like stale Telegram chat-action state rather than a real active task.

## Fix that worked
1. Confirm there is only one live gateway/poller:
   ```bash
   ps -efww | grep -E 'hermes gateway run|python.*gateway run|telegram|sendChatAction' | grep -v grep || true
   ```
2. Read state and confirm `active_agents=0`:
   ```bash
   cat /root/.hermes/gateway_state.json 2>/dev/null
   cat /root/.hermes/gateway.pid 2>/dev/null
   ```
3. Check duplicate profile state files:
   ```bash
   find /root/.hermes /root/.hermes2 /root/.hermes/profiles -maxdepth 3 \( -name 'gateway_state.json' -o -name 'gateway.pid' \) -print 2>/dev/null
   ```
4. Gracefully stop the exact PID from `gateway_state.json` with `TERM`; only use `KILL` if it remains alive.
5. Remove stale state/pid files for the main and secondary homes.
6. Start exactly one gateway as a tracked background process:
   ```bash
   env HERMES_HOME=/root/.hermes PYTHONUNBUFFERED=1 /root/.local/bin/hermes gateway run --replace
   ```
7. Verify exactly one process, state PID exists, Telegram state is connected, and fresh logs have clean startup lines.

## Important caution
When fixing typing-loop from a live Telegram conversation, prefer a delayed restart if the current reply still needs to be delivered. If the user reports it via CLI, an immediate clean restart is fine.

## Update interaction
During Hermes updates, stop the gateway first and clear state. In PRoot, `hermes update` or parent Hermes processes may send SIGTERM and expect systemd restart-on-failure to revive the gateway, but no-systemd environments leave it stopped until manually restarted.
