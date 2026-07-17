# 2026-05-15 stale Telegram typing/chat-action state

## Symptom
Mohamed reported that Telegram showed the bot as typing continuously even though the gateway was not obviously stopped.

## Diagnosis pattern
Checks showed:
- Exactly one live gateway process existed.
- `/root/.hermes/gateway_state.json` matched a real PID.
- `gateway_state=running` and Telegram `state=connected`.
- `active_agents=0`, so the gateway was not actually processing a request.
- No duplicate live poller or token conflict was visible.
- Recent long Telegram tasks had completed and `Sending response` was logged.
- Bot API `getMe` succeeded.

This points to stale Telegram chat-action/typing state after prior long work or response delivery, not an active agent.

## Fix
Use a clean single-gateway restart, not a second gateway:

1. Gracefully stop the current gateway PID from `gateway_state.json`.
2. If it remains alive after a short wait, kill that PID only.
3. Remove `/root/.hermes/gateway_state.json` and `/root/.hermes/gateway.pid` plus duplicate-profile state files if present.
4. Start exactly one primary `/root/.hermes` gateway with `gateway run --replace` using the environment's background-process tracking.

## Verification
Confirm all of these before declaring fixed:
- Exactly one `gateway run` process exists.
- State PID exists under `/proc/<pid>`.
- `gateway_state=running`.
- Telegram platform state is `connected`.
- `active_agents=0`.
- Fresh post-restart logs show `Connected to Telegram (polling mode)` and `Gateway running with 1 platform(s)`.
- No fresh `sendChatAction`, warning/error spam, token conflict, or network loop appears after restart.

## Pitfall
Do not trust `hermes gateway status` in this PRoot/no-systemd setup. It can report the user service as stopped while the real foreground gateway is running. Use process + state + log + Bot API checks as the authority.