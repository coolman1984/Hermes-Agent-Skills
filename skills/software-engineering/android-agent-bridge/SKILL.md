---
name: android-agent-bridge
description: Build or extend an Android-native local bridge that lets Hermes operate Android capabilities from Linux/Termux via agent-first HTTP endpoints, Accessibility, notifications, and explicit one-time permission grants.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [android, bridge, accessibility, notifications, termux, hermes, agent-first, local-control]
    related_skills: [senior-software-engineer, phone-control, hermes-agent]
---

# Android Agent Bridge

## Overview

Use this skill when Mohamed wants Hermes to control or inspect Android from inside Linux or Termux on the same phone, but direct shell/ADB control is not enough or the goal is a durable app-based bridge.

This is **not** a user-facing control-panel pattern.
The default design is **agent-first**:

1. Mohamed sends Hermes a request on Telegram.
2. Hermes reasons inside Linux/Termux.
3. Hermes calls a local Android-native bridge.
4. The bridge performs allowed Android actions.

The Android app exists mainly as a native capability extension for Hermes, not as a daily manual UI for Mohamed.

## When to use

Use this skill when:

- Hermes needs Android-native abilities unavailable inside Linux/PRoot/Termux alone.
- Mohamed wants Telegram → Hermes → Android execution without manually driving the phone.
- You need a durable local bridge rather than one-off ADB commands.
- You need Accessibility, Notification Listener, app launches, local intents, or UI text extraction under one local interface.

Do not use this skill when:

- ADB direct control is already enough and no durable bridge is needed.
- The task is only a one-off screenshot or tap and does not justify maintaining an app.
- The user expects root-like unrestricted control without root.

## Core rule

Do **not** promise “full Android control”.
State the real boundary clearly:

- A normal Android app can become a powerful bridge.
- It cannot silently grant itself protected permissions.
- It cannot bypass Android sandboxing.
- It cannot replace root or privileged shell access.

The right promise is:

**Build the strongest realistic local Android bridge possible without root, then make Hermes use it autonomously.**

## Correct architecture

Prefer this architecture:

1. Hermes runs in Linux or Termux.
2. Hermes talks to a local app over `127.0.0.1`.
3. The Android app owns native permissions and services.
4. The bridge exposes explicit, minimal, auditable endpoints.
5. The UI is bootstrap-only: start service, open settings pages, explain the one-time grants.

Avoid making the app a large manual dashboard unless Mohamed explicitly asks.

## Recommended native components

Most useful baseline bridge:

- Foreground service
- Local-only HTTP server bound to `127.0.0.1`
- Accessibility service
- Notification Listener service
- Boot receiver
- Minimal bootstrap activity

Optional later:

- MediaProjection for screenshots/screen capture
- Overlay permission for floating controls
- Share target / intent receiver
- Auth/token gate for local commands
- Command log and health endpoint

## Recommended endpoint set

Start with explicit, inspectable endpoints such as:

- `/health`
- `/permissions`
- `/apps`
- `/launch?package=...`
- `/open-url?url=...`
- `/intent?action=...&data=...`
- `/back`
- `/home`
- `/recents`
- `/notifications-panel`
- `/tap?x=...&y=...`
- `/type?text=...`
- `/click-text?text=...`
- `/ui-text`
- `/notifications`
- `/commands`

Keep the bridge local-only unless a future authenticated remote design is explicitly requested.

## Bootstrap activity design

The main activity should be minimal.
Its purpose is only to:

- start the bridge service
- open Accessibility settings
- open Notification Access settings
- open app details
- explain that the bridge is for Hermes, not for manual daily use

If you find yourself adding a full manual control console by default, you are drifting away from the intended design.

## Accessibility usage pattern

Accessibility should handle actions that Hermes cannot do from Linux alone, such as:

- global back/home/recents
- tap gestures
- text input into focused editable fields
- clicking visible text matches
- reading visible UI text

Important pitfall:
Do not depend only on coordinate tapping if a semantic action is possible. Prefer:

1. visible text lookup
2. semantic click
3. coordinate tap as fallback

## Notification listener usage pattern

Use Notification Listener to expose recent notification text to Hermes.
Keep a bounded in-memory queue and avoid pretending you have full historic notification storage unless you actually implemented it.

## Build strategy

If the Android build toolchain is present, build locally.
If not, do **not** fake an APK.

Instead:

1. scaffold the real source project locally
2. verify the file tree and core classes exist
3. document the missing build prerequisites honestly
4. prefer Android Studio on Windows as the fast path when local Linux/PRoot lacks SDK/build-tools

When building in Android PRoot ARM64, do not stop at “SDK missing” just because environment variables are unset. Check likely SDK paths such as `/root/android-sdk` and `/usr/lib/android-sdk`. If the build fails at resource processing with `AAPT2 ... Daemon startup failed`, inspect binary architecture: the Android Gradle plugin may have downloaded an x86 `aapt2`. Pin the ARM64 local tool in `gradle.properties` with `android.aapt2FromMavenOverride=/usr/lib/android-sdk/build-tools/debian/aapt2`, and run shared-storage wrappers as `bash ./gradlew` because `./gradlew` may not be executable.

The durable lesson is:
**source scaffold first, truthful build status second, APK only when the toolchain is real.**

## Verification checklist

Before saying the bridge work is done:

- [ ] The project structure exists on disk.
- [ ] Manifest exists.
- [ ] Foreground service exists.
- [ ] Accessibility service exists.
- [ ] Notification listener exists.
- [ ] Local server endpoints are documented.
- [ ] README explains real limits and one-time grants.
- [ ] If no toolchain exists, say APK generation is still blocked.
- [ ] Do not claim root-like powers.

## Common pitfalls

1. Promising total Android control without root.
2. Building a user-facing panel when Mohamed wants Hermes-only operation.
3. Exposing the bridge on the public network by default.
4. Forgetting that Accessibility and Notification Access still need one-time manual enablement.
5. Claiming the app is complete when only the source exists and no APK was built.
6. Overusing coordinate taps instead of semantic UI actions.
7. Treating the bridge as a general app product instead of a native extension for Hermes.
8. On Android PRoot ARM64, Gradle may use an x86 `aapt2` and fail at resource processing. Use `references/prroot-arm64-local-build.md`: pin `android.aapt2FromMavenOverride` to an ARM-native `aapt2`, run `/sdcard` wrappers with `bash ./gradlew`, then verify APK and hash.

## Session references

See `references/agent-first-local-bridge.md` for a concrete project shape, endpoint set, and the practical scaffold pattern that worked in-session.

See `references/prroot-arm64-local-build.md` for the Android PRoot ARM64 build workaround: Bash-run Gradle wrapper from shared storage, ARM64 `aapt2` override, APK verification, and compact handoff packaging.
