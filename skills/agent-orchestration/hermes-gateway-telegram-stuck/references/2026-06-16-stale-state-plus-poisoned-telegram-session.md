# 2026-06-16 — Stale gateway state plus poisoned Telegram DM session

## Symptom
Telegram looked broken from the user's side. The gateway status command was misleading in PRoot/no-systemd, and `gateway_state.json` claimed `gateway_state=running` with Telegram `connected`, but no live gateway process existed for the recorded PID.

Later inspection also showed the active Telegram DM mapping pointed at a session that had produced context-overflow failure logs and repeated request dumps, so simply restarting risked reusing a poisoned per-chat session.

## Useful checks
- `ps -efww | grep -E 'gateway run|hermes.*gateway' | grep -v grep`
- Read `/root/.hermes/gateway_state.json` and verify `/proc/<pid>` exists.
- Tail `/root/.hermes/logs/gateway.log` for:
  - `Skipping transcript persistence for context-overflow failure`
  - repeated request dumps for the same session id
  - no fresh gateway process after the state claims running
- Inspect `/root/.hermes/sessions/sessions.json` for the affected key, e.g. `agent:main:telegram:dm:<chat_id>`.

## Recovery pattern
1. Remove stale gateway state/pid files only after confirming there is no live matching gateway PID.
2. Start a single primary gateway using the Hermes terminal background process path:
   `env HERMES_HOME=/root/.hermes PYTHONUNBUFFERED=1 /root/.local/bin/hermes gateway run --replace`
3. If logs show the Telegram DM session itself is poisoned by context-overflow/session-growth issues, stop the restarted gateway cleanly, back up `sessions.json`, remove only the affected Telegram DM mapping, and move matching `request_dump_<session_id>_*.json` files into a backup directory.
4. Restart one gateway again.
5. Verify:
   - exactly one gateway process
   - `gateway_state=running`
   - Telegram platform `state=connected`
   - state PID exists under `/proc/<pid>`
   - Bot API `getMe` succeeds for the configured token
   - `hermes chat -q 'Reply with exactly: OK' --source telegram -Q --toolsets ''` returns `OK`
   - no fresh post-restart warnings/errors

## Important distinction
Do not treat older Telegram flood-control warnings as the active outage if the current evidence is stale state plus absent process. Flood control means Telegram is rate-limiting sends; stale gateway state with no process means the gateway is dead and needs clean recovery.
