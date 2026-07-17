# 2026-07-08 — Telegram network wedge, exact-PID restart, and delayed startup verification

## Context
Mohamed reported: "telegram not working" from the CLI. The default Hermes gateway process existed and `gateway_state.json` claimed:

- `gateway_state=running`
- Telegram `state=connected`
- `active_agents=0`

But the recent log showed repeated Telegram network/DNS instability:

- `Temporary failure in name resolution`
- `httpx.ReadError`
- fallback IP failures
- `Telegram polling resumed after network error`

The runtime imports were healthy (`OpenAI`, `ruamel.yaml` OK), and Bot API `getMe` worked.

## Recovery pattern used
1. Checked status, live gateway process, gateway state, log tail, Hermes version/git state, and runtime imports.
2. Sent SIGTERM to the exact gateway PID from `/root/.hermes/gateway_state.json`.
3. The old PID survived SIGTERM after several seconds, so sent SIGKILL to that exact PID.
4. Removed stale gateway state and pid files.
5. Started the gateway inside Hermes with `terminal(background=true)`, not `nohup`.
6. Waited and verified:
   - exactly one gateway process
   - `gateway_state=running`
   - Telegram state `connected`
   - state PID exists under `/proc/<pid>`
   - Bot API `getMe` returns `N8N_mflma1984_bot`
   - log shows `Connected to Telegram (polling mode)` and `Gateway running with 1 platform(s)`

## Important pitfall
After starting the replacement gateway, the process existed before useful state/log proof appeared. An early check showed a live new process but no `gateway_state.json` yet. Waiting another short interval produced the real proof. Do not declare failure or start a second gateway during this early window if the process is alive.

## Durable lesson
When a gateway is wedged around Telegram network recovery, and exact-PID SIGTERM does not stop it quickly, escalate to exact-PID SIGKILL before starting the replacement. Do not use broad self-matching `pkill` patterns. Then wait for the post-start state file and Telegram connection lines before final judgement.
