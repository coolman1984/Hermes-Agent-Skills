---
name: mobilerun
description: Route Android device control through Mobilerun/Droidrun Portal for screenshots, UI trees, taps, swipes, typing, and multi-step mobile automation. Use when OpenClaw needs managed Android app control rather than shell-only Termux commands.
metadata:
  clawdbot:
    emoji: "📲"
    requires:
      bins: ["adb"]
      env: ["MOBILERUN_API_KEY"]
      config: ["skills.entries.mobilerun.enabled"]
    primaryEnv: "MOBILERUN_API_KEY"
---

# Mobilerun

## Core rule
Use Mobilerun for managed Android UI automation when you need screenshots, UI trees, taps, swipes, typing, or app navigation.

## What this skill covers
- connecting OpenClaw to the Mobilerun/Droidrun Portal app
- using an API key from mobilerun.ai
- driving Android UI through managed commands instead of raw screen guessing
- combining UI control with Termux:API for device-native actions

## What this skill does not do
- it does not install the phone app from this shell
- it does not mint API keys
- it does not replace Android permissions or pairing steps

## Setup checklist
1. Install the Droidrun Portal APK on the Android device.
2. Get an API key from mobilerun.ai.
3. Install or enable this skill in OpenClaw.
4. Set `MOBILERUN_API_KEY` in the OpenClaw skill config using an environment reference.
5. Confirm `adb` is available on the machine that runs OpenClaw.

## Config guidance
Use an environment reference instead of a raw secret in `openclaw.json`:

```json5
{
  skills: {
    entries: {
      mobilerun: {
        enabled: true,
        env: {
          MOBILERUN_API_KEY: "${MOBILERUN_API_KEY}"
        }
      }
    }
  }
}
```

## Test pattern
After setup, verify the connection by asking the agent to:
- describe the current screen
- list visible buttons
- tap a specific control
- type text into a field
- take a screenshot if the portal supports it

## Safety
- Prefer read-only inspection first.
- Confirm before taps, text entry, or destructive actions.
- Treat API keys and device state as sensitive.

## Reference
Read `references/mobilerun-routing.md` for the integration checklist and a minimal test plan.
