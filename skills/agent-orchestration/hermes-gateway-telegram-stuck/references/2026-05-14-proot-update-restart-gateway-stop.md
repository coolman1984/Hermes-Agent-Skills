# 2026-05-14 Telegram gateway stopped after update/restart flow

Context: Mohamed reported Telegram was not working correctly. The gateway had been restarted successfully earlier, then later stopped again.

Findings:
- `hermes gateway status` reported stopped, but this is not authoritative in the Android/proot no-systemd environment.
- `ps -efww | grep -E 'gateway run|hermes.*gateway|telegram'` showed no live gateway process.
- `/root/.hermes/gateway_state.json` showed `gateway_state=stopped`, Telegram `state=disconnected`, and a stale PID that no longer existed under `/proc`.
- `/root/.hermes2` had no competing state files.
- Telegram Bot API `getMe` succeeded for `@N8N_mflma1984_bot`; token was present, 46 chars, and had no control chars.
- Logs showed SIGTERM/SIGINT during a Hermes update/restart flow around 09:49-09:50 UTC, then `Gateway drain timed out`, `Telegram disconnected`, and `Exiting with code 1 ... so systemd Restart=on-failure can revive the gateway`.
- In this environment, no systemd user bus exists, so no auto-restart happened.
- Older logs showed intermittent Telegram ReadError/ConnectError episodes that usually recovered; they were not the current blocker.
- Older logs also showed failed media sends caused by placeholder file paths like `/path/to/file.html`; this is a response-format/delivery issue, not a gateway outage.

Recovery used:
1. Clear state files in both possible homes:
   - `/root/.hermes/gateway_state.json`
   - `/root/.hermes/gateway.pid`
   - `/root/.hermes2/gateway_state.json`
   - `/root/.hermes2/gateway.pid`
2. Start exactly one primary gateway with `HERMES_HOME=/root/.hermes` and `gateway run --replace`.
3. Inside Hermes terminal tools, start it with `background=true`; a foreground command using `nohup ... &` was rejected by the terminal tool policy.
4. Verify:
   - exactly one gateway process exists
   - state PID exists under `/proc/<pid>`
   - `gateway_state=running`
   - Telegram `state=connected`
   - log contains `Connected to Telegram (polling mode)` and `Gateway running with 1 platform(s)`
   - no fresh errors after a second check 10-15 seconds later

Good post-restart evidence from this incident:
- PID 20268 running `/root/.local/bin/hermes gateway run --replace`
- `gateway_state=running`
- Telegram `state=connected`
- no errors since restart
