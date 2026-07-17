# 2026-05-30 — Telegram gateway stopped after Hermes update, then auto-resumed stale work

## Situation
After a Hermes update in Mohamed's PRoot/no-systemd environment, Telegram stopped answering correctly.

## Observed proof
- No live gateway process existed after the update.
- `/root/.hermes/gateway.pid` was missing.
- `/root/.hermes/gateway_state.json` still existed from shutdown.
- `hermes gateway status` reported the user service stopped and an outdated unit, but this was not authoritative because DBUS/systemd is absent in PRoot.
- Telegram token sanity check showed the bot token was present, correct length, and had no control characters.
- Direct Telegram Bot API `getMe` succeeded and returned the expected bot username.
- Logs showed update-triggered shutdown:
  - `Received SIGTERM — initiating shutdown`
  - `Gateway drain timed out after 60.0s with 1 active agent(s)`
  - `Skipping .clean_shutdown marker — drain timed out with interrupted agents`
  - `Exiting with code 1 ... so systemd Restart=on-failure can revive the gateway`
- In PRoot, systemd did not revive the gateway.

## Fix used
1. Remove stale gateway state and pid files.
2. Start one primary gateway with the tracked background process mechanism:
   `hermes gateway run --replace`
3. Verify with process list, state file, logs, and Bot API `getMe`.

## Extra pitfall found
On restart, the gateway scheduled auto-resume for one restart-interrupted Telegram session. That resumed the previous update-verification work inside the gateway, spawning old `hermes config migrate` / `hermes doctor` commands and making Telegram behavior look confused even though Telegram was connected.

When logs show `Scheduled auto-resume for ... restart-interrupted session(s)` after a maintenance/update shutdown, inspect child processes under the gateway. If they are clearly stale maintenance commands from the interrupted update and not user work that should continue, terminate the exact stale child processes. Do not kill the whole gateway unless the gateway itself is unhealthy.

## Good final state
- Exactly one `hermes gateway run --replace` process.
- `/root/.hermes/gateway_state.json` contains `gateway_state: running`.
- Telegram platform state is `connected`.
- `active_agents: 0` after stale resumed work is cleared.
- Logs show:
  - `Connected to Telegram (polling mode)`
  - `✓ telegram connected`
  - `Gateway running with 1 platform(s)`
- Bot API `getMe` succeeds.

## Durable lesson
For Telegram outages after updates in PRoot, check for two separate problems:
1. Gateway not restarted because systemd is unavailable.
2. Gateway restarted but auto-resumed stale interrupted maintenance work.

Fix the stopped gateway first, then clear stale auto-resumed maintenance subprocesses by exact PID if they appear.