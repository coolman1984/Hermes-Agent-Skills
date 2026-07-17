# 2026-06-24 — Network recovered, stale gateway state, poisoned Telegram DM mapping

## Situation
Telegram was not replying correctly. Initial checks showed no live gateway process, while `/root/.hermes/gateway_state.json` claimed a gateway PID in `draining` state with Telegram `retrying`.

Observed stale state:
- state PID existed in `gateway_state.json` but `/proc/<pid>` was absent
- `gateway_state`: `draining`
- Telegram platform state: `retrying`
- recent logs contained earlier DNS/connectivity failures for `api.telegram.org` and Telegram fallback IPs

Important distinction: the network failure was transient. By the time of recovery, direct DNS/HTTPS/Bot API checks succeeded. The durable lesson is to verify current network reachability before treating old log lines as still-active failure.

## Verification sequence that worked
1. Check real gateway processes, not only `hermes gateway status` in PRoot/no-systemd.
2. Read `/root/.hermes/gateway_state.json` and confirm whether the recorded PID exists under `/proc/<pid>`.
3. Probe current network/token health:
   - DNS resolution for `api.telegram.org`
   - HTTPS to Telegram
   - Telegram Bot API `getMe` for the active token, without printing the token
4. If network and token are healthy but the state PID is stale, remove stale state files and start exactly one gateway with:
   `env HERMES_HOME=/root/.hermes PYTHONUNBUFFERED=1 /root/.local/bin/hermes gateway run --replace`
5. Verify:
   - exactly one gateway process
   - `gateway_state=running`
   - Telegram state `connected`
   - log lines: `Connected to Telegram (polling mode)` and `Gateway running with 1 platform(s)`
   - CLI smoke: `hermes chat -q 'Reply with exactly: OK' --source telegram -Q --toolsets ''`

## Extra poisoned-session check
After gateway recovery, inspect the Telegram DM session mapping if the user reports bad replies or silence.

Signal found in this incident:
- `/root/.hermes/sessions/sessions.json` mapped the Telegram DM to a session with very high `last_prompt_tokens`
- no normal `session_<id>.json` file existed
- a large `request_dump_<id>_*.json` existed

Recovery:
1. Back up `sessions.json` and the request dump/session artifacts under a timestamped backup directory.
2. Remove only the affected `agent:main:telegram:dm:<chat_id>` mapping.
3. Move matching `request_dump_<session_id>_*.json` and any session files into the backup directory.
4. Leave the clean connected gateway running; the next inbound Telegram message creates a fresh clean session.

## Watchdog note
If the watchdog cron last run shows `Script exited with code -15`, do not assume the watchdog is broken. Treat it as a symptom to investigate alongside gateway process/state. Manually recover and verify first, then let the next watchdog tick prove stability.
