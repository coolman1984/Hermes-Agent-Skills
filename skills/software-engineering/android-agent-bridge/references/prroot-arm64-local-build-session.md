# Android Bridge Build in Android PRoot ARM64

## When this applies

Use this when building the Hermes Android Bridge from Linux or PRoot on the same Android device, especially when the project lives under shared storage such as:

`/sdcard/Download/HermesAndroidBridge`

## Durable pattern from session

A real debug APK was built successfully after fixing two Android-on-Android build issues:

1. The Gradle wrapper file on shared storage may not be executable.
2. The Android Gradle plugin may download an x86 Linux `aapt2`, which cannot run inside ARM64 PRoot.

## Required project fixes

### 1. Generate or keep a Gradle wrapper

If the project only has the system `gradle`, generate a modern wrapper first:

```bash
cd /sdcard/Download/HermesAndroidBridge
gradle wrapper --gradle-version 8.9 --distribution-type bin --no-daemon
```

On shared Android storage, do not rely on executable permissions for `./gradlew`. Run it with Bash:

```bash
bash ./gradlew assembleDebug --no-daemon
```

### 2. Use the ARM64 local `aapt2`

If the build fails during resource processing with `AAPT2 ... Daemon startup failed`, check whether the failing `aapt2` is x86:

```bash
file /root/android-sdk/build-tools/*/aapt2 /usr/lib/android-sdk/build-tools/debian/aapt2
```

On ARM64 PRoot, pin the Debian/Termux ARM binary in `gradle.properties`:

```properties
android.aapt2FromMavenOverride=/usr/lib/android-sdk/build-tools/debian/aapt2
```

Then build with the Android SDK environment set:

```bash
cd /sdcard/Download/HermesAndroidBridge
ANDROID_HOME=/root/android-sdk ANDROID_SDK_ROOT=/root/android-sdk bash ./gradlew assembleDebug --no-daemon
```

## Verification commands

```bash
APK=app/build/outputs/apk/debug/app-debug.apk
ls -lh "$APK"
sha256sum "$APK"
unzip -tq "$APK"
```

A successful session should show:

```text
BUILD SUCCESSFUL
zip integrity OK
```

## Packaging handoff

For Mohamed, copy the APK and create a compact source handoff that excludes build caches:

```bash
cp app/build/outputs/apk/debug/app-debug.apk /sdcard/Download/HermesAndroidBridge-debug.apk
sha256sum /sdcard/Download/HermesAndroidBridge-debug.apk > /sdcard/Download/HermesAndroidBridge-debug.apk.sha256
```

When zipping the project, exclude `.gradle` and `app/build`, then include the final APK under an `apk/` folder.

## Pitfalls

- Do not claim the APK is built unless `assembleDebug` actually returns `BUILD SUCCESSFUL`.
- Do not keep retrying the same build after `AAPT2 ... Daemon startup failed`; inspect binary architecture and pin the ARM64 `aapt2`.
- Do not say the Android SDK is missing if `/root/android-sdk` or `/usr/lib/android-sdk` exists but environment variables are unset.
- Do not promise root-like Android control after the build. Accessibility and Notification Listener still require one-time manual grants.
