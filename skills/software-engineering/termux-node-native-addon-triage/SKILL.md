---
name: termux-node-native-addon-triage
description: Diagnose and handle Node.js native-addon install failures on Android/Termux/PRoot,
  especially node-gyp errors, better-sqlite3, and android_ndk_path issues. Use when
  deciding whether to force a prebuilt binary path, patch environment variables, or
  move the workload into a real Linux userland.
tags: [termux, proot, node, native-addons, node-gyp, android]
---

# Termux/PRoot Node Native-Addon Triage

Use this when a Node.js dependency fails in Termux, PRoot-Distro, or Android aarch64 because of a native addon build.

## Trigger symptoms

- `node-gyp` build failures
- `android_ndk_path` missing or undefined
- `better-sqlite3`, `sqlite3`, `sharp`, `canvas`, or similar native modules
- install works partially but runtime still dies on `.node` loading
- optional platform package missing at runtime after a global npm install, e.g. a CLI wrapper complains about `*-linux-arm64`
- PRoot/Termux environment is detected even though the target is meant to behave like Linux

## What to do

1. Confirm the real execution context.
   - Check whether the shell is Termux, a PRoot container, or a genuine Linux userland.
   - Record `node -v`, `npm -v`, architecture, and package path.

2. Identify whether the failure is package-specific or environment-specific.
   - If the error mentions NDK, gyp, or Android toolchain variables, treat it as an environment blocker first.
   - If the addon is known to have prebuilt binaries for Linux/arm64, try that path before source builds.

3. Prefer the least invasive workaround first.
   - Attempt install with Linux/arm64 targeting flags when the package supports prebuilds.
   - Use build-from-source only if the package genuinely supports Android/Termux compilation and the required toolchain is available.

4. Stop early when the environment is the blocker.
   - If `node-gyp` still asks for `android_ndk_path` or similar Android-only configuration, do not keep grinding on random build flags.
   - Move the workload into a real Linux userland, container, VM, or host environment instead.

5. Verify the result with a runtime smoke test.
   - Re-run install cleanly.
   - Require the module.
   - Run the smallest end-to-end prompt or command that proves the addon is actually usable.

## Decision rule

If the goal is a stable service and the dependency is a native addon with poor Android/Termux support, prefer changing the runtime environment over forcing a fragile build.

## Common pitfalls

- Assuming `npm install` success means the addon is actually usable.
- Burning time on NDK setup when the package never intended to support Android.
- Forgetting that PRoot can make Linux-ish environments behave differently from real Linux.
- Treating a partial workaround as a permanent fix.

## Outcome to aim for

A clean yes/no answer:
- either the package installs and runs end-to-end in the current environment,
- or you prove the environment is the blocker and choose a better runtime.
