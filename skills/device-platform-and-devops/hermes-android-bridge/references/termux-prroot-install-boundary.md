# Termux/PRoot Android bridge install boundary

## What this session established

When Hermes is running inside Linux-on-Android through PRoot/Termux, there is a hard boundary between:

- **what can be completed autonomously inside Linux**, and
- **what still depends on Android system surfaces**.

## Safe autonomous path

Hermes can usually complete these steps without user help:

1. clone or inspect the bridge project
2. fix build issues
3. build the APK locally
4. copy the APK into an Android-visible path under Downloads
5. verify artifact size and checksum
6. verify whether an existing bridge / relay / ADB channel is already available

## Control-channel checks to run first

Before claiming zero-touch installation, check for any of:

- `adb devices` shows a connected device
- local bridge responds on `http://127.0.0.1:8765/health`
- relay responds on `http://127.0.0.1:8766/ping`
- `termux-am` can talk to its socket server

If one of these exists, deeper automation may be possible.

## What failed in this session and how to interpret it

These specific probes are useful because they distinguish a missing control channel from a bad build:

- direct `/system/bin/am`, `/system/bin/pm`, `/system/bin/cmd`, `/system/bin/settings` calls hit Android permission boundaries from PRoot
- `termux-open` may successfully fire an intent without giving a machine-verifiable completion signal
- `termux-am` is only usable when its socket exists; if the socket is absent, do not plan around it
- absence of listeners on `127.0.0.1:8765` and `127.0.0.1:8766` means no prior bridge is active

## Durable lesson

For Android bridge work in this environment, the agent should separate the job into two promises:

### Promise A — fully autonomous
- build
- verify
- package
- place artifact in Downloads
- prepare Hermes/plugin side

### Promise B — conditional on an existing control channel
- silent install
- launch installed app programmatically with verification
- grant Accessibility / Notification access
- complete first-run activation end-to-end

Do not collapse Promise B into Promise A unless a control channel is already present.

## Recommended phrasing

Use direct wording such as:

- "I finished everything Linux can finish on its own."
- "The remaining step is Android system-gated, not an unfinished build issue."
- "If a control channel already exists, I can try to complete the rest automatically."
