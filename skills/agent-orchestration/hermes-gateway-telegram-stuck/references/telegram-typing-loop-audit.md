# Telegram Typing-Loop and Stuck Reply Audit

Use this when Mohamed reports that Telegram shows the bot as typing but no answer arrives, or when replies arrive only after a restart.

## Key lesson

In this Android PRoot/no-systemd setup, `hermes gateway status` can say the service is stopped while the real gateway is running in the foreground/nohup. Treat status output as advisory only.

## Fast audit sequence

1. Check live gateway process and any duplicate pollers:
   ```bash
   ps -efww | grep -E 'hermes gateway run|python.*gateway run|telegram' | grep -v grep
   ```
2. Check gateway state and PID:
   ```bash
   cat /root/.hermes/gateway_state.json 2>/dev/null
   cat /root/.hermes/gateway.pid 2>/dev/null
   ```
3. Check duplicate profiles and stale states:
   ```bash
   find /root/.hermes /root/.hermes2 /root/.hermes/profiles -maxdepth 3 \( -name 'gateway_state.json' -o -name 'gateway.pid' \) -print 2>/dev/null
   ```
4. Tail recent logs for:
   - `sendChatAction`
   - `ReadError`
   - `ConnectError`
   - `TimedOut`
   - `Another local Hermes gateway is already using this Telegram bot token`
5. If the current response must be delivered first, schedule a delayed clean restart instead of killing the gateway immediately.

## Delayed clean restart pattern

Use when replying over the same Telegram gateway you are about to restart:

```bash
bash -lc 'sleep 8
set +e
mkdir -p /root/.hermes/logs
{
  echo "[$(date -Is)] delayed clean restart requested after Telegram typing-state audit"
  ps -efww | grep -E "hermes gateway run|python.*gateway run" | grep -v grep || true
} >> /root/.hermes/logs/gateway-clean-restart.log
pkill -f "hermes gateway run" || true
pkill -f "python.*gateway run" || true
rm -f /root/.hermes/gateway_state.json /root/.hermes/gateway.pid
nohup env HERMES_HOME=/root/.hermes PYTHONUNBUFFERED=1 /root/.local/bin/hermes gateway run --replace >> /root/.hermes/logs/gateway-clean-restart.log 2>&1 &'
```

Then verify on the next message:

```bash
ps -efww | grep -E 'hermes gateway run|python.*gateway run' | grep -v grep
cat /root/.hermes/gateway_state.json 2>/dev/null
tail -60 /root/.hermes/logs/gateway-clean-restart.log 2>/dev/null
```

## Pitfalls

- Do not kill the current Telegram gateway before sending the user-facing message unless the user explicitly accepts the interruption.
- Do not start a second gateway to “test” Telegram; this can create token conflicts.
- Network errors that recover after one attempt are not necessarily a system failure.
