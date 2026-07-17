# Phone Control Routing Checklist

## Connect
- Ensure `adb` exists on PATH.
- Enable Wireless debugging on the Android device.
- Pair with the pairing port + 6-digit code shown on the phone.
- Connect using the ADB port shown on the main Wireless debugging screen.
- Verify with `adb devices`.
- Treat pairing ports/codes as short-lived; re-read the current screen before each pairing attempt.
- If `adb devices` shows `offline`, refresh the wireless-debugging card and pair again rather than reusing stale endpoints.
- If `adb pair` returns a protocol fault or similar mismatch, the pairing endpoint likely expired or changed.

## Observe
- `adb shell screencap -p /sdcard/screen.png`
- `adb shell uiautomator dump /sdcard/ui.xml`
- `adb shell dumpsys activity activities | grep mResumedActivity`

## Act
- `adb shell input tap X Y`
- `adb shell input swipe X1 Y1 X2 Y2 300`
- `adb shell input text "..."`
- `adb shell input keyevent ...`
- `adb shell monkey -p <package> -c android.intent.category.LAUNCHER 1`

## Verify
- Re-run the screen capture or UI dump after every action.
- Confirm the foreground activity changed when launching apps.

## Fallbacks
- If ADB is not connected, request the current pairing port/code or a fresh ADB connection port.
- If the user needs hardware access instead of UI control, route to `termux-api`.
- If the user wants managed mobile automation through a portal, route to `mobilerun`.
