---
name: phone-control
description: Full Android device control via ADB self-connect. Use for screenshots,
  UI trees, taps, swipes, typing, app launches, key presses, and observe-act-verify
  loops when the user wants OpenClaw to control an Android phone directly.
tags: [android, adb, ui-automation, phone-control, screen]
metadata:
  clawdbot:
    emoji: 🤖
    requires:
      bins:
      - adb
      config:
      - skills.entries.phone-control.enabled
---

# Phone Control via ADB

## Core rule
Use ADB to observe the screen before acting, then verify the result after every action.

## When to use this skill
- Read the current screen
- Tap buttons and links
- Swipe or scroll
- Type text
- Launch apps by package name
- Press Home, Back, Enter, Search, or Recents
- Inspect the foreground activity
- Dump the UI tree for coordinates and text

## ADB self-connect pattern
If OpenClaw is running on the same Android device through Termux:
1. Enable Developer Options.
2. Turn on Wireless debugging.
3. Pair Termux/ADB using the pairing port and 6-digit code shown on the phone.
4. Connect to the separate device `IP address and port` shown on the Wireless debugging screen.
5. Verify with `adb devices`.

Do not guess the pairing port or code. Use the values shown on the device.

### Observed Android/PRoot pairing pitfalls
- The pairing dialog port is not the same as the device connection port. After pairing, close the dialog and use the main-screen `IP address and port` for `adb connect`.
- Pairing codes expire quickly; ask for a fresh code and run the command immediately while the dialog remains open.
- In this PRoot/Termux setup, Termux ADB (`/data/data/com.termux/files/usr/bin/adb` v35.0.2) returned `protocol fault (couldn't read status message): Success` during wireless pairing. If that appears, install/use Ubuntu ADB (`/usr/bin/adb`, e.g. `apt-get install adb`) and restart the ADB server before retrying.
- When running on the same phone, test both the displayed IP and `127.0.0.1` for reachability, but still rely on Android's displayed pairing/connect ports as the source of truth.
- If `adb connect <device-ip:port>` fails before pairing, that is expected; complete pairing first with the current pairing dialog.
- After the first successful wireless pair/connect, treat persistence as a watchdog problem, not a one-time command problem: save the stable `adb connect` target (`IP:PORT` or `127.0.0.1:PORT` when same-device loopback works), run a background keepalive loop that periodically checks `adb devices`, re-runs `adb connect` when disconnected, and keeps a log/status file. This does not replace Android's initial pairing UI, but it dramatically reduces repeated reconnect friction in same-device Termux/PRoot workflows.
- For this user, prefer building a small local manager with `set-target`, `status`, `once`, and `run` commands plus a self-heal scheduler over ad-hoc manual reconnect commands. See `references/adb-keepalive-watchdog.md`.

## Observe → Act → Verify loop
1. Observe the screen state.
2. Choose the smallest safe action.
3. Act with ADB.
4. Verify the result.

## Common commands
```bash
adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png ./screen.png

adb shell uiautomator dump /sdcard/ui.xml
adb pull /sdcard/ui.xml ./ui.xml

adb shell input tap X Y
adb shell input swipe X1 Y1 X2 Y2 300
adb shell input text "hello"
adb shell input keyevent KEYCODE_BACK
adb shell monkey -p com.whatsapp -c android.intent.category.LAUNCHER 1
adb shell dumpsys activity activities | grep mResumedActivity
```

## Android browser session workflow
Use this when the user has an authenticated session in a phone browser/app (for example Comet with X/Twitter logged in) and direct Camoufox login is blocked or risky.

Rules:
- Do not search for or extract saved passwords from the browser/app.
- Prefer visual, user-observable control of the already trusted session.
- Ask the user to connect ADB via Wireless debugging; do not guess pairing ports or codes.
- After `adb devices` shows the device, identify/launch the browser package with read-only package/activity inspection first.
- Use screenshots/UI dumps before each tap and verify after every action.
- If sensitive fields or account settings appear, stop and ask the user to take over.

Typical flow:
1. Pair/connect ADB.
2. Find the browser package with package listing/search (e.g. Comet/Perplexity/browser names).
3. Launch the browser or use Android share/open-url intents for the target X article.
4. Observe whether the existing session can view the article.
5. Extract only visible page text via screenshot/OCR/UI dump where possible, or ask the user to share/export the page content. Avoid credential stores.

## Safety
- Ask before destructive actions.
- Prefer read-only inspection first.
- Treat SMS, contacts, credential stores, cookies, and browser saved passwords as sensitive.
- Use screenshots/UI dumps to understand state before tapping.

## Reference
Read `references/phone-control-routing.md` for the routing checklist and connection notes.
