# ADB keepalive watchdog for same-device Termux/PRoot setups

## When to use
After Wireless Debugging pairing has already succeeded once and the main pain is that `adb connect` drops over time.

## Core idea
Do not chase "ADB must never disconnect" as a platform guarantee. Build a local watchdog layer that:
- stores the chosen `adb connect` target
- runs `adb start-server`
- checks `adb devices`
- re-runs `adb connect <target>` when the device disappears
- writes a status file and append-only log
- can be supervised by a long-lived background process plus a periodic self-heal cron

## Recommended command surface
A small manager CLI should expose at least:
- `set-target HOST:PORT [interval]`
- `status`
- `once`
- `run`
- `log`
- optional `clear-target` and `stop`

## Why this matters
On Android, the disconnect source is often outside the agent's control:
- Wireless Debugging toggled off
- port rotation / changed connect target
- pairing invalidation
- loopback/network changes
- power/background policy side effects

So the durable lesson is not "ADB stays up forever"; it is "make reconnect cheap and automatic."

## Same-device workflow
1. Complete Wireless Debugging pairing once.
2. Record the working `adb connect` target shown by Android.
3. If same-device loopback works, test both the shown IP and `127.0.0.1`, but keep Android's displayed port as source of truth.
4. Start the watchdog in the background.
5. Add a periodic self-heal job that restarts the watchdog if the process dies.

## Important limit
This watchdog does **not** replace Android's initial pairing UI. It starts paying off only after the first successful pair/connect.
