# Android local build on arm64 / PRoot

Use this when building an Android bridge app locally inside Linux-on-Android / Termux / PRoot on an arm64 phone.

## Proven path

1. Install full JDK, not just `java` runtime.
   - Needed because `javac` may be missing even when `java` exists.
2. Install Android command-line tools and accept licenses.
3. Install Debian/Ubuntu Android build packages in addition to Google SDK packages when running on arm64.
4. If Gradle stalls or fails during resource packaging, verify which `aapt2` binary is actually being used.

## Key pitfall

Google SDK or Maven/Gradle may provide an `aapt2` binary for `x86-64`, which is unusable on arm64/PRoot even though the rest of the SDK installs normally.

Symptom pattern:
- Gradle reaches resource steps like `mergeDebugResources`, `packageDebugResources`, or `processDebugResources`
- build hangs or fails with `AAPT2 ... Daemon startup failed`
- `file <aapt2>` shows `x86-64` instead of `ARM aarch64`

## Durable fix

Install Debian/Ubuntu Android build-tools and override Gradle to use the arm64-native `aapt2`:

```bash
apt-get install -y android-sdk-build-tools android-sdk-platform-tools android-sdk-common android-sdk-helper android-platform-tools-base android-libandroidfw android-libandroidfw-dev
```

Common ARM-native paths seen in this environment:

```text
/usr/bin/aapt2
/usr/lib/android-sdk/build-tools/debian/aapt2
```

Verify:

```bash
file /usr/lib/android-sdk/build-tools/debian/aapt2
/usr/lib/android-sdk/build-tools/debian/aapt2 version
```

Expected result: `ARM aarch64` executable.

Then add the working path to `gradle.properties`:

```properties
android.aapt2FromMavenOverride=/usr/lib/android-sdk/build-tools/debian/aapt2
```

or, if that is where the ARM binary lives:

```properties
android.aapt2FromMavenOverride=/usr/bin/aapt2
```

This is an experimental Gradle flag, but it unblocks local arm64 builds when the Maven/Google-provided `aapt2` is not runnable.

## Gradle wrapper on shared Android storage

If the project lives under `/sdcard`, direct execution can fail even when the wrapper exists:

```text
./gradlew: Permission denied
```

Use:

```bash
bash ./gradlew assembleDebug --no-daemon
```

If no wrapper exists yet but system Gradle can run the wrapper task:

```bash
gradle wrapper --gradle-version 8.9 --distribution-type bin --no-daemon
```

## Proven local build command

```bash
cd /sdcard/Download/HermesAndroidBridge
ANDROID_HOME=/root/android-sdk ANDROID_SDK_ROOT=/root/android-sdk bash ./gradlew assembleDebug --no-daemon
```

## Debug APK handoff

After a successful build, copy a stable install artifact to Downloads and hash it:

```bash
cp app/build/outputs/apk/debug/app-debug.apk /sdcard/Download/HermesAndroidBridge-debug.apk
sha256sum /sdcard/Download/HermesAndroidBridge-debug.apk > /sdcard/Download/HermesAndroidBridge-debug.apk.sha256
unzip -tq /sdcard/Download/HermesAndroidBridge-debug.apk
```

## Hermes-specific learning

For a Hermes-controlled Android bridge, prefer starting from an upstream Hermes-native project when available rather than expanding a thin custom scaffold first.

A strong base found in practice:
- `raulvidis/hermes-android`

Why it helped:
- already designed around Hermes control flow
- includes Android app + bridge server + Hermes plugin/tool layer
- supports relay mode and direct bridge mode

## Plugin setup note

If the Hermes-side plugin depends on `aiohttp`, install it into the Hermes venv, not only a random throwaway venv, or the plugin may appear installed but fail at runtime.

## Verification checklist

After a successful build, verify all of the following:
- build output says `BUILD SUCCESSFUL`
- APK exists under `app/build/outputs/apk/debug/`
- copied APK matches source hash
- `unzip -tq` passes on the APK
- Hermes plugin is enabled if a plugin is part of the bridge
- note whether plugin activation requires a new session
- distinguish clearly between:
  - build success
  - APK file availability
  - app installation on Android
  - OS-granted permissions inside Android

## Important boundary

On Android, from a constrained Linux/PRoot environment, you may be able to open the APK installer but not silently prove installation or grant OS permissions. Report that boundary clearly instead of overstating completion.
