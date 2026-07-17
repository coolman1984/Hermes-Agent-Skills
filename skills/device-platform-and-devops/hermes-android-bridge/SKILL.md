---
name: hermes-android-bridge
description: Use when Hermes needs to control the local Android device through the Hermes Android Bridge app over 127.0.0.1.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [android, bridge, local, accessibility, notifications, hermes]
---

# Hermes Android Bridge

## Purpose

This skill is for controlling the local Android device through the Hermes Android Bridge app.

The bridge is local-only and agent-first.
Hermes talks to the bridge over:

`http://127.0.0.1:8765`

A local helper command is available:

`/root/.local/bin/hermes-android-bridge`

## When to use

Use this skill when Mohamed asks Hermes to:

- open an Android app
- inspect visible UI text
- go back or go home
- open recent apps
- open a URL on Android
- type text into the active field
- click visible text via Accessibility
- inspect recent notifications
- inspect recent bridge commands

## Preconditions

Before this works, the Android app must already be:

1. installed
2. started once
3. granted Accessibility access
4. granted Notification access
5. running the foreground bridge service

If `health` fails, do not pretend the bridge is active. Report that the app/service is not running yet.

## Commands

### Health

```bash
/root/.local/bin/hermes-android-bridge health
```

### List apps

```bash
/root/.local/bin/hermes-android-bridge apps
```

### Launch app

```bash
/root/.local/bin/hermes-android-bridge launch com.whatsapp
```

### Open URL

```bash
/root/.local/bin/hermes-android-bridge open-url 'https://example.com'
```

### Back / home / recents

```bash
/root/.local/bin/hermes-android-bridge back
/root/.local/bin/hermes-android-bridge home
/root/.local/bin/hermes-android-bridge recents
```

### Open notifications panel

```bash
/root/.local/bin/hermes-android-bridge notifications-panel
```

### Read visible UI text

```bash
/root/.local/bin/hermes-android-bridge ui-text
```

### Type text

```bash
/root/.local/bin/hermes-android-bridge type 'hello'
```

### Click by visible text

```bash
/root/.local/bin/hermes-android-bridge click-text 'Send'
```

### Tap by coordinates

```bash
/root/.local/bin/hermes-android-bridge tap 100 200
```

### Read notifications

```bash
/root/.local/bin/hermes-android-bridge notifications
```

### Read recent command log

```bash
/root/.local/bin/hermes-android-bridge commands
```

## Operating rules

- Observe first when possible.
- Prefer `ui-text` before blind taps.
- Prefer `click-text` before coordinate taps.
- Verify the result after each action.
- Treat the bridge as local-only and sensitive.
- Do not claim success if `health` fails.

## Current project paths

Source project:

`/sdcard/Download/HermesAndroidBridge`

Built debug APK:

`/sdcard/Download/HermesAndroidBridge-builds/hermes-android-0.1.0-debug.apk`

## Production choice

For a minimal local-only bridge on the same Android device, this skill remains valid.

For the full production path where Hermes needs a richer toolset, relay pairing, and Telegram-driven control, prefer the class-level `hermes-android` stack (the GitHub repo + Hermes plugin with 38 `android_*` tools). Keep this local-only bridge as the fallback/minimal path, not the default final choice.

See:

`references/termux-prroot-install-boundary.md`

## Zero-touch install boundary in Termux/PRoot

When Mohamed wants "do everything yourself" on Android, do not bluff past the platform boundary.

Before promising autonomous install/activation, check for a pre-existing privileged control channel such as:

- a working `adb devices` connection
- an already-running bridge endpoint on `127.0.0.1:8765` or relay on `127.0.0.1:8766`
- a working `termux-am` socket

If none of those exists, the realistic autonomous ceiling is:

1. build the APK
2. copy it to an Android-visible Downloads path
3. attempt launch via `termux-open`
4. report plainly that installer / Accessibility / Notification enablement is still system-gated

Prefer this wording internally:

- *I can finish the build and prepare the artifact myself.*
- *I cannot honestly claim full zero-touch activation unless a control channel already exists.*

## Limitations

This is not root.
It cannot silently bypass Android security.
Protected services still require one-time manual enablement in Android settings.
Without an existing control channel, Android package install and protected permission screens remain outside Hermes control.
