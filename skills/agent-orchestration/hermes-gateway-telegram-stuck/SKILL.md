---
name: hermes-gateway-telegram-stuck
description: Fix and auto-detect Telegram gateway stuck in typing loop - restart the gateway process when stuck
trigger: "Telegram gateway stuck, not responding, or stuck in typing loop"
---

# Hermes Gateway Telegram Fast Fix

## Trigger
Use this when Telegram is not answering, replies stop, the bot looks stuck, or the gateway is alive but messages are not getting through.

## First principle
Assume one of four things until proven otherwise:
1. Gateway is stopped.
2. A stale gateway state is lying about being alive.
3. Another local poller is holding the Telegram bot token or the network path is flaking.
4. The gateway is using the wrong Hermes home/profile and is writing state into the wrong directory.

## Fast triage order
1. Check live status, but do not trust it blindly in no-systemd / proot environments. A `service stopped` result can be false when DBUS/systemd is missing.
```bash
hermes gateway status 2>&1 | head -20
```
2. Check for real running processes, including other Hermes profiles that may be holding the same bot token:
```bash
ps aux | grep -E 'gateway run|telegram|sendChatAction' | grep -v grep
ps -efww | grep -F 'python -m hermes_cli.main gateway run' | grep -v grep
```
3. Check the newest gateway log tail:
```bash
tail -60 /root/.hermes/logs/gateway.log
```
4. Check state files for stale PID / stale running state in every Hermes profile that might exist:
```bash
cat /root/.hermes/gateway_state.json 2>/dev/null
cat /root/.hermes/gateway.pid 2>/dev/null
cat /root/.hermes2/gateway_state.json 2>/dev/null
cat /root/.hermes2/gateway.pid 2>/dev/null
```
5. Treat the log + process + state trio as authoritative if status lies.
6. If there is any conflict or stale state, do a clean replace restart.

## Common failure modes

### A. Gateway stopped
The gateway is not running at all. Common in proot/Termux or after a crash.

### B. Stale running state
The process died, but gateway_state.json or gateway.pid still says it is running.

### C. Duplicate Telegram poller
Another Hermes instance is already using the same bot token.

### D. Telegram network failure
The bot is running, but getUpdates / deleteWebhook / connect is timing out or falling back repeatedly.

### E. Split-profile duplicate gateway
A second Hermes home/profile (for example `/root/.hermes2`) can be running the same bot token while the main profile looks fine. In that case, kill both live gateway processes, clear both profiles’ stale gateway state files, and restart only the intended primary profile.

### F. CLI status is misleading in no-systemd environments
In proot/headless setups, `hermes gateway status` can complain about DBUS/systemd or say the unit is stopped while a foreground/nohup gateway process is actually alive. Treat the live process list, gateway log, and state file as authoritative.

### G. Update/restart flow kills the gateway but does not revive it
A Hermes update or ad-hoc restart script can send SIGTERM/SIGINT to the gateway, drain active Telegram work, and then expect systemd `Restart=on-failure` to bring it back. In this Android/proot environment, the systemd user bus is absent, so the gateway stays down with `gateway_state=stopped` and no live PID. If logs show SIGTERM/SIGINT during update/restart and no gateway process, clean stale state and manually start exactly one primary `/root/.hermes` gateway.

After restarting, also check for auto-resumed stale maintenance work. If logs show `Scheduled auto-resume for ... restart-interrupted session(s)` and child processes under the gateway are clearly old update verification commands (`hermes config migrate`, `hermes doctor`, git/version checks), terminate those exact child PIDs after confirming they are not live user work. A connected gateway can still feel broken if it is busy auto-resuming stale update work. See `references/2026-05-30-post-update-gateway-stopped-auto-resume.md`.

## Clean recovery sequence
Run these in order when Telegram is stuck. **When you are the agent operating inside Hermes terminal tools**, use `terminal(background=true)` to start the gateway — do NOT use `nohup` in a foreground shell command. The Hermes terminal tool rejects shell-level background wrappers (`nohup`, `disown`, `setsid`, trailing `&`) with an error. The `nohup`-style code block below is only for raw shell / manual operator use.

Important pitfall 1 (self-matching pkill): in Hermes terminal tools, a foreground shell command that contains `pkill -f "gateway run --replace"` can sometimes be killed by its own `pkill` pattern because the command line itself contains the match string. If a cleanup command exits `-15` or returns with no output, do not assume cleanup happened; immediately re-check processes and state files. If state remains, remove it with a Python unlink snippet or a narrower process-selection command.

Important pitfall 2 (nohup rejected): the Hermes terminal tool forbids `nohup`/`disown`/`setsid`/trailing `&` in foreground commands. To start the gateway from within a Hermes session, use `terminal(background=true)` with the gateway command — do NOT wrap it in `nohup`. If you are in a raw shell (manual operator), the `nohup` block below works fine.

Important pitfall 3 (SIGTERM may not finish): after sending SIGTERM to the exact gateway PID from `gateway_state.json` / `gateway.pid`, always re-check the process list. If that exact PID is still alive after a short wait and `active_agents=0`, send SIGKILL to the exact PID before starting a replacement. Do not start a second gateway on top of a half-stopped old one, and do not use broad self-matching `pkill` patterns.

**Agent path (inside Hermes terminal tool):**
```bash
# Step 1: Kill stale processes (avoid self-matching patterns in one-liners)
pgrep -f 'gateway run --replace' | xargs -r kill || true
pgrep -f 'python.*gateway run' | xargs -r kill || true
rm -f /root/.hermes/gateway_state.json /root/.hermes/gateway.pid
rm -f /root/.hermes2/gateway_state.json /root/.hermes2/gateway.pid
# Step 2: Start via terminal(background=true) — NOT nohup
terminal(background=true, command="env HERMES_HOME=/root/.hermes PYTHONUNBUFFERED=1 /root/.local/bin/hermes gateway run --replace")
```

**Raw shell path (manual operator):**
```bash
pkill -f "python.*hermes.*gateway run" || true
rm -f /root/.hermes/gateway_state.json /root/.hermes/gateway.pid
rm -f /root/.hermes2/gateway_state.json /root/.hermes2/gateway.pid
mkdir -p /root/.hermes/logs
nohup env HERMES_HOME=/root/.hermes PYTHONUNBUFFERED=1 /root/.local/bin/hermes gateway run --replace > /root/.hermes/logs/gateway.log 2>&1 &
```

Then verify:
```bash
sleep 5
ps -efww | grep -E 'gateway run|hermes.*gateway' | grep -v grep || true
tail -40 /root/.hermes/logs/gateway.log
cat /root/.hermes/gateway_state.json 2>/dev/null
```

If the outage happened during a Hermes update, check whether the update only killed the gateway but did not finish:
```bash
hermes --version
git -C /root/.hermes/hermes-agent status -sb
ls -t /root/.hermes/update-report*.txt 2>/dev/null | head
```
If code is up to date but dependencies are broken after a uv failure in proot, repair with:
```bash
cd /root/.hermes/hermes-agent
export UV_LINK_MODE=copy
/root/.local/bin/uv pip install --python /root/.hermes/hermes-agent/venv/bin/python -e .
```

### H. Gateway connected but agent crashes after update
Sometimes Telegram is not stopped: `gateway_state=running` and `telegram.state=connected`, but every Telegram message fails because the agent cannot initialize. After a proot update or restart, check logs for runtime import failures, especially:
- `ImportError: cannot import name 'OpenAI' from 'openai' (unknown location)`
- `RuntimeError: Failed to initialize OpenAI client`
- `cannot import name 'YAML' from 'ruamel.yaml' (unknown location)`

Do not trust `uv pip show ...` alone. Verify runtime imports with the exact gateway Python:
```bash
/root/.hermes/hermes-agent/venv/bin/python - <<'PY'
from openai import OpenAI
from ruamel.yaml import YAML
print('imports OK')
PY
```

If `openai.__file__` is `None`, or `OpenAI` cannot import, the package is corrupted as a namespace directory. Use `references/2026-05-14-openai-namespace-corruption-after-update.md` for the full diagnosis and repair. Short OpenAI fix:
```bash
cd /root/.hermes/hermes-agent
export UV_LINK_MODE=copy
PY=/root/.hermes/hermes-agent/venv/bin/python
SITE=$($PY - <<'PY'
import site
print(site.getsitepackages()[0])
PY
)
rm -rf "$SITE/openai" "$SITE"/openai-*.dist-info
/root/.local/bin/uv pip install --python "$PY" --reinstall --no-cache openai==2.24.0
/root/.local/bin/uv pip install --python "$PY" -e .
```

If `ruamel.yaml` imports as a namespace package or `from ruamel.yaml import YAML` fails, repair the exact gateway venv similarly:
```bash
cd /root/.hermes/hermes-agent
export UV_LINK_MODE=copy
PY=/root/.hermes/hermes-agent/venv/bin/python
SITE=$($PY - <<'PY'
import site
print(site.getsitepackages()[0])
PY
)
rm -rf "$SITE/ruamel" "$SITE"/ruamel.yaml-*.dist-info "$SITE"/ruamel_yaml-*.dist-info
/root/.local/bin/uv pip install --python "$PY" --reinstall --no-cache 'ruamel.yaml>=0.18.0'
```

Then restart the gateway and run a CLI smoke test (`hermes chat -q 'Reply with exactly: OK' --source telegram -Q --toolsets ''`) before declaring Telegram fixed. See `references/2026-06-19-stale-state-ruamel-yaml-repair.md` for a concrete stale-state + ruamel repair incident.

Additional update-era reference: `references/2026-07-02-v0180-update-ruamel-repair-and-statefile-gap.md` covers a successful Hermes v0.18.0 update where `ruamel.yaml` broke after the code pull, and where a restarted gateway process was alive before `gateway_state.json` reappeared. In that pattern, verify runtime imports first, then live process, Bot API `getMe`, and a CLI smoke test; do not classify the restart as failed solely because the state file is still missing during early post-update checks.

### I. Gateway connected but one Telegram DM keeps returning a tiny failure response
If logs show Telegram is connected and sending responses, but each user message logs:
- `Transient agent failure in session <session_id>`
- `TypeError ... 'NoneType' object is not iterable`
- `Repaired ... message-alternation violations before request`
- `Skipping transcript persistence for context-overflow failure in session <session_id> to prevent session growth loop`

and the Telegram session transcript contains only repeated user messages with no assistant turns, or the per-chat mapping points at a session with repeated request dumps / context-overflow failures, treat it as a poisoned per-chat session rather than only a dead gateway.

Recovery pattern:
1. Confirm `active_agents=0` and exactly one gateway process, or confirm the state PID is stale by checking `/proc/<pid>` when `gateway_state.json` claims running but no process exists.
2. Stop the exact PID from `/root/.hermes/gateway_state.json` when it exists; do not use a broad self-matching `pkill` pattern.
3. Back up then remove the affected entry from `/root/.hermes/sessions/sessions.json`, for example `agent:main:telegram:dm:<chat_id>`.
4. Move any matching `session_<session_id>.json`, `<session_id>.jsonl`, `<session_id>.json`, and `request_dump_<session_id>_*.json` into a backup directory under `/root/.hermes/sessions/`. Sometimes only request dumps exist; still remove the mapping so the next inbound Telegram message creates a fresh clean session.
5. Remove stale `gateway_state.json` / `gateway.pid`, start one primary gateway, and verify state/logs.
6. Run a CLI smoke test with the gateway source before declaring fixed:
```bash
hermes chat -q 'Reply with exactly: OK' --source telegram -Q --toolsets ''
```
The next Telegram inbound message will create a fresh clean session.

Reference: `references/2026-06-16-stale-state-plus-poisoned-telegram-session.md` captures the stale-state + context-overflow session-reset pattern.

```
Use the tool's process/session id for polling. Then verify:
```bash
sleep 10
ps -efww | grep -E 'gateway run|hermes.*gateway' | grep -v grep
cat /root/.hermes/gateway_state.json 2>/dev/null
tail -80 /root/.hermes/logs/gateway.log
```

Then run a second stable check after another short wait. A restart is not considered done until exactly one gateway process exists, `gateway_state` is `running`, Telegram state is `connected`, the state PID exists under `/proc/<pid>`, and no fresh errors appear after restart.


## What good looks like
- `Application started`
- `Connected to Telegram (polling mode)`
- `Gateway running with 1 platform(s)`
- No repeating `sendChatAction` spam
- No duplicate gateway / token lock errors

## If Telegram shows typing forever but no real work is active
If Mohamed reports constant Telegram typing animation, do not assume the gateway is dead. First check process + state + logs. A common stale chat-action case looks like:
- exactly one gateway process exists
- `gateway_state=running`
- Telegram platform state is `connected`
- `active_agents=0`
- no duplicate poller/token conflict
- recent long task already logged `response ready` / `Sending response`

Treat this as stale Telegram chat-action state. Gracefully stop the current gateway PID, remove gateway state/pid files, restart exactly one primary `/root/.hermes` gateway, then verify no fresh `sendChatAction`/warning spam. See `references/2026-05-15-stale-telegram-typing-chat-action.md`.

## If the log shows a token lock
If you see something like:
- `Another local Hermes gateway is already using this Telegram bot token`

Then stop all local Hermes gateway pollers first, remove stale state, and restart only one gateway instance.

## If the log shows network errors
If you see repeated `ConnectError`, `ReadError`, `TimedOut`, or repeated fallback IP failures:
- do not restart only because a watch pattern fired; first check whether the gateway recovered
- check live process, state PID, Telegram state, recent log recovery lines, and direct Bot API `getMe`
- if the log later shows `Telegram polling resumed after network error`, state is connected, and Bot API probes succeed, classify it as transient network/DNS/API instability and do not interrupt the working gateway
- restart cleanly once only when the process is dead, state is stale/error, Bot API probes repeatedly fail, or network errors continue without a recovery line
- do not spawn another gateway on top of the existing one
- if the problem repeats continuously after one clean restart, escalate to network troubleshooting instead of looping restarts

Reference: `references/2026-05-14-transient-telegram-network-alerts.md` captures a recovered network-alert incident and the exact verification probes used.

### J. Telegram flood control (gateway alive, replies delayed or missing)
If logs show repeated lines like:
- `[Telegram] Telegram flood control, waiting 123.0s`
- `Flood control exceeded. Retry in 41 seconds`

then the gateway is running and Telegram is technically connected, but Telegram is rate-limiting the bot because it sent too many messages in a short window. Common trigger: long responses chunked into many sequential sends (text + media groups + streaming edits).

This is NOT a gateway crash. Do not restart. Symptoms:
- User sees delayed replies or thinks the bot is stuck
- Gateway logs show normal `response ready` lines but with flood-control waits between sends
- The issue resolves itself (Telegram flood control has a countdown)
- No error_code in gateway_state.json

Recovery:
1. Wait for the flood control countdown to expire — do not restart the gateway.
2. If it recurs within the same session, the trigger is likely a single long task producing many chunked messages. Let it finish.
3. If flood control is persistent across multiple tasks, check whether streaming is enabled for Telegram (`display.platforms.telegram.streaming`) and whether response chunking is too aggressive.
4. Only restart if the gateway itself crashes or stops responding after flood control — the flood control is a Telegram-side rate limit, not a Hermes bug.

Reference: `references/2026-06-16-telegram-flood-control-delays.md`.

## Fast operator rule
Do not spend long guessing. In this order:
- status
- process check
- log tail
- stale state cleanup
- clean restart
- verify

If Mohamed reports a Telegram typing indicator with no real response, read `references/telegram-typing-loop-audit.md` and use the delayed clean restart pattern when you need to deliver the current Telegram reply before restarting the gateway. If the report comes from CLI or another non-Telegram surface, an immediate exact-PID clean restart is acceptable after verifying there is exactly one gateway, `active_agents=0`, Bot API `getMe` succeeds, and no duplicate poller exists. See `references/2026-05-15-typing-loop-and-update-restart-pattern.md`.

## Reference incidents
- `references/2026-05-14-proot-update-restart-gateway-stop.md` — gateway killed by update/restart flow in no-systemd proot, token/API healthy, manual background-tool restart required.
- `references/2026-05-30-post-update-gateway-stopped-auto-resume.md` — post-update Telegram outage where PRoot did not revive the gateway, then restart auto-resumed stale update-verification subprocesses that needed exact-PID cleanup.
- `references/2026-05-15-stale-state-self-matching-pkill.md` — stale `gateway_state.json` pointed at a missing PID; cleanup command with broad `pkill -f` self-matched and had to be followed by explicit state re-check/removal.
- `references/2026-05-15-stale-telegram-typing-chat-action.md` — gateway connected with `active_agents=0` but Telegram showed constant typing; clean single-gateway restart cleared stale chat-action state.
- `references/2026-06-15-silent-gateway-death-no-error.md` — gateway died silently mid-work with no error/traceback/OOM in log; state file stale (claimed running), PID absent from `/proc`; `hermes gateway status` misleading in PRoot; clean restart via `terminal(background=true)` recovered.
- `references/2026-06-16-telegram-flood-control-delays.md` — Telegram flood control (rate-limit) during multi-chunk sends; distinct from gateway crash. Do not restart for flood control alone. Also covers the same-day stale-state crash recovery in PRoot.
- `references/2026-06-16-stale-state-plus-poisoned-telegram-session.md` — stale `gateway_state.json` with absent PID plus a Telegram DM mapping poisoned by context-overflow/request-dump growth; reset the mapping after backup so the next Telegram message starts clean.
- `references/2026-06-24-network-recovered-stale-state-poisoned-dm.md` — old Telegram DNS/connectivity failures had recovered, but stale `draining` gateway state and a poisoned DM mapping with only a large request dump still required cleanup; verify current Bot API health before blaming old network logs.
- `references/2026-07-08-telegram-network-wedge-exact-pid-restart.md` — gateway appeared connected but had recent Telegram DNS/read-error wedging; exact-PID SIGTERM did not finish, exact-PID SIGKILL plus a single background-tool restart recovered it. Also reinforces waiting for delayed state/log proof after a live process appears.

## Optional guardrail
If the gateway keeps getting fragile, run the supervisor too:
```bash
nohup /root/.local/bin/hermes-main-supervisor > /root/service-logs/hermes-main/supervisor-launch.log 2>&1 &
```

## Mohamed's active durable watchdog
For Mohamed's primary default profile, a self-healing watchdog script exists at:
```bash
/root/.hermes/scripts/telegram_gateway_watchdog.py
```
It is scheduled as a no-agent cron job:
```text
job_id: 3e3b7f0d8f85
name: Telegram Gateway Watchdog
schedule: every 2m
script: telegram_gateway_watchdog.py
```
The script stays silent when healthy. It prints only when it takes action. It checks:
- exactly one live gateway process
- stale `gateway_state.json` PID vs `/proc/<pid>`
- Telegram platform state
- Bot API `getMe` for token/network sanity
- poisoned Telegram session mappings after context-overflow/request-dump growth

If it detects stale running state or no live gateway, it removes stale state files and starts:
```bash
env HERMES_HOME=/root/.hermes PYTHONUNBUFFERED=1 /root/.local/bin/hermes gateway run --replace
```
using `subprocess.Popen(..., start_new_session=True)` so recovery does not depend on the current agent turn. Telegram streaming is disabled in `/root/.hermes/config.yaml` (`display.platforms.telegram.streaming: false`) to reduce flood-control/edit-loop risk.

## Verification checklist
After the fix, confirm:
- Telegram session is connected
- Only one Hermes gateway process exists
- `gateway_state.json` matches a real PID
- Messages sent from Telegram get a reply
- `getUpdates` called every ~10 seconds
- No continuous `sendChatAction` calls
- Gateway connected message
- If `hermes gateway status` is ambiguous, verify bot reachability directly with Telegram Bot API `getMe` for the exact bot token in the primary `.env`
- Do not assume `hermes gateway call health` exists in every build; this environment’s reliable proof is the live process + log + state file + Bot API `getMe`
- Telegram Bot API `getMe` succeeds for the active bot token and returns the expected username

### Post-restart timing pitfall
Immediately after starting the gateway with `terminal(background=true)`, the process may exist before `gateway_state.json` is written and before the connection lines appear in `gateway.log`. Do not treat a missing state file in the first few seconds as failure if the gateway process is alive. Poll/wait another 10–20 seconds, then re-check process + state + log + Bot API. This avoids false recovery loops where the agent restarts or probes too aggressively while the gateway is still initializing.

When doing a CLI smoke test after a restart, run it only after the state file says `gateway_state=running` and Telegram says `connected`. If an early smoke test is interrupted or returns no output while the gateway is still coming up, prefer the stable process/state/log/Bot API checks over that premature smoke result.

## Auto-Detection Cron (Optional)
To add a cron health check every 5 minutes:
```bash
*/5 * * * * if grep -q "sendChatAction.*sendChatAction.*sendChatAction" /root/.hermes/logs/gateway.log 2>/dev/null; then pkill -f "hermes gateway run"; sleep 2; nohup /root/.hermes/hermes-agent/venv/bin/python3 /root/.local/bin/hermes gateway run > /root/.hermes/logs/gateway-restart.log 2>&1 & fi
```