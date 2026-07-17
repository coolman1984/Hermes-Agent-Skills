# Termux:API Routing Guide

## Command map
- `termux-battery-status` -> battery level, temperature, charging state
- `termux-notification` -> local alerting
- `termux-clipboard-get` / `termux-clipboard-set` -> clipboard access
- `termux-location` -> GPS / location
- `termux-sensor` -> device sensors
- `termux-camera-photo` -> camera capture
- `termux-tts-speak` -> text to speech
- `termux-torch` -> flashlight
- `termux-wifi-connectioninfo` -> Wi-Fi details
- `termux-telephony-deviceinfo` -> SIM/network info
- `termux-sms-send` / `termux-sms-list` -> SMS
- `termux-contact-list` / `termux-call-log` -> contacts/call logs

## Routing rules
- Use read-only commands first.
- Ask before any action that sends data off-device or changes device state.
- Prefer the smallest command that answers the question.

## proot-distro wrapper pattern
If Termux binaries need to be called from a proot shell, bind mount the Termux prefix:

```bash
proot-distro login ubuntu --shared-tmp --bind /data/data/com.termux/files/usr:/termux-host
```

Then create wrappers or symlinks for only the commands you need.

## Verification
- `command -v termux-battery-status`
- `termux-battery-status`
- `termux-notification --title test --content "ok"`

## Safety
Do not assume the APIs exist unless verified in the real Termux shell.
