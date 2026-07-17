---
name: termux-api
description: Safe routing and usage guidance for Termux:API commands on Android. Use
  when working with battery, camera, location, notifications, clipboard, SMS, TTS,
  sensors, telephony, or proot-to-Termux wrapper access. The skill assumes the real
  Termux app shell, not a root shell, for package installation and device APIs.
tags: [termux, termux-api, android, sensors, clipboard, device]
metadata:
  clawdbot:
    emoji: 📱
    requires:
      bins:
      - termux-api
      - pkg
---

# Termux:API

## Core rule
Use Termux:API commands in the real Termux app shell. Do not assume `pkg install` works from a root shell or inside proot.

## What this skill covers
- battery status and power state
- notifications and alerts
- clipboard read/write
- location, sensors, and telephony info
- camera, torch, TTS, vibration, and media helpers
- safe wrapper patterns for proot-distro environments

## When to use
Use Termux:API when the agent needs Android hardware or local device signals that shell-only tools cannot provide.

## Installation guidance
- Install Termux from F-Droid.
- Install the companion package with `pkg install termux-api` inside the Termux app shell.
- Verify with commands like `termux-battery-status` and `termux-notification`.

## Proot guidance
If using proot-distro, bind-mount the Termux prefix and call the host binaries through wrappers or symlinks.

## Safe usage
- Prefer read-only commands first.
- Avoid sending SMS/calls/notifications unless the user asked.
- Treat clipboard and contact/call-log access as sensitive.
- Use least privilege and explicit confirmation for destructive or external actions.

## Android-visible file placement
When the user is on Android and asks you to download or save files they need to open from the phone, do **not** default to internal Linux paths like `/root/...` even if they are convenient in the agent environment. Save the user-facing copy under shared Android storage, preferably:

- `/sdcard/Download/<clear-folder-name>/`
- or the Termux shared-storage alias under `~/storage/downloads/`

Use a clear human-readable folder name such as `Program Downloads` when the user is collecting app/repo archives. If you first saved a file under an internal path for convenience, copy or move the final user-facing artifact into shared Android storage and verify it exists there before saying it is ready.

Pitfall:
- A path can be "easy" from the shell and still be invisible from the Android file manager. For phone-visible delivery, optimize for Android shared storage, not the agent's home directory.

## Reference
Read `references/termux-api-routing.md` for a practical command map and proot wrapper examples.
