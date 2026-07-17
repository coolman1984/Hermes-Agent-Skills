# Agent-First Local Android Bridge Reference

## Trigger from session

Mohamed explicitly clarified that the Android app should be for Hermes, not for him:

- not a manual control panel
- not a user-driven interface
- Hermes should receive Telegram requests and act inside Android by itself

This is a class-level design signal, not a one-off preference.

## Concrete scaffold pattern that proved useful

Project root used in-session:

`/sdcard/Download/HermesAndroidBridge`

Core files scaffolded:

- `settings.gradle.kts`
- `build.gradle.kts`
- `gradle.properties`
- `app/build.gradle.kts`
- `app/src/main/AndroidManifest.xml`
- `app/src/main/java/com/hermes/bridge/MainActivity.kt`
- `app/src/main/java/com/hermes/bridge/bridge/HermesBridgeService.kt`
- `app/src/main/java/com/hermes/bridge/bridge/HermesAccessibilityService.kt`
- `app/src/main/java/com/hermes/bridge/bridge/HermesNotificationListenerService.kt`
- `app/src/main/java/com/hermes/bridge/bridge/BootReceiver.kt`
- `app/src/main/res/xml/accessibility_service_config.xml`
- `README.md`
- `example-hermes-check.sh`

## Native components that made sense

- Foreground service for persistent local bridge runtime
- NanoHTTPD local server bound to `127.0.0.1:8765`
- Accessibility service for semantic UI actions and fallbacks
- Notification Listener for recent notification buffer
- Boot receiver for auto-start
- Bootstrap-only activity with buttons for:
  - start bridge service
  - open Accessibility settings
  - open Notification Access settings
  - open app details

## Useful endpoint set from the session

- `/health`
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

## Important wording pattern

Use language like:

- strongest realistic local bridge without root
- native capability extension for Hermes
- one-time manual Android grants still required
- local-only and auditable

Avoid language like:

- full Android control
- full system control
- no user action needed ever

## Durable build lesson

When the session environment has Java/ADB but lacks Android SDK/build-tools:

- scaffold the source project honestly
- verify the files exist
- document the missing prerequisites
- recommend Android Studio on Windows as the faster build path if local Linux/PRoot is not ready

Do not invent APK success from an incomplete toolchain.
