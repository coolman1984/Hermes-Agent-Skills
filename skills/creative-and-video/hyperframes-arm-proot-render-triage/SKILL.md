---
name: hyperframes-arm-proot-render-triage
description: Diagnose and work around HyperFrames render/validate failures on Linux
  aarch64 / Android PRoot, especially x86-64 Chrome Headless Shell downloads mislabeled
  as linux_arm.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
tags: [hyperframes, arm, proot, termux, render, troubleshooting]
metadata:
  tags:
  - hyperframes
  - video
  - render
  - chrome
  - arm64
  - proot
  - android
  - troubleshooting
---

# HyperFrames ARM/PRoot Render Triage

Use this skill when HyperFrames is being installed or used on Linux aarch64, Android, Termux, or PRoot and browser-backed commands fail.

## Trigger symptoms

- `npx hyperframes validate`, `inspect`, `preview`, or `render` fails after `npx hyperframes browser ensure`.
- Error says something like:

```text
spawn .../chrome-headless-shell ENOENT
```

- The Chrome file appears to exist, but cannot execute.
- `npx hyperframes lint` works, while render/validate does not.

## Known cause in Mohamed's environment

On Linux aarch64 / Android PRoot, `npx hyperframes browser ensure` can report success but download an x86-64 Chrome Headless Shell into a path that includes `linux_arm`.

That makes Puppeteer report `ENOENT` even when the file exists, because the binary interpreter is for x86-64, not ARM64.

## Fast diagnosis

```bash
npx hyperframes doctor
p=/root/.cache/hyperframes/chrome/chrome-headless-shell/linux_arm-131.0.6778.85/chrome-headless-shell-linux64/chrome-headless-shell
file "$p"
"$p" --version
```

Interpretation:

- If `file` says `ELF 64-bit ... x86-64`, it is an architecture mismatch.
- If shell says `cannot execute: required file not found`, that also indicates a missing x86-64 loader on ARM, not that Chrome is absent.
- Do not repeatedly delete and redownload the cache unless HyperFrames changed the download logic; it will likely fetch the same unusable binary.

## What still works locally

```bash
npx hyperframes init my-video --non-interactive --example blank
npx hyperframes lint
```

You can still author compositions, install skills, and run static lint.

## What needs a compatible browser

These need Chrome/Chromium that actually runs on the host architecture:

```bash
npx hyperframes validate
npx hyperframes inspect
npx hyperframes preview
npx hyperframes render
```

## Workarounds

Choose one:

1. Install or provide a real ARM64 Chromium/Chrome executable and configure HyperFrames/Puppeteer to use it if the CLI supports an executable path or environment override.
2. Move render/validate to an x86_64 Linux machine where the bundled Chrome Headless Shell works.
3. Use Docker only on a compatible host; Docker was not available in the observed PRoot environment.
4. Use HyperFrames publish/remote rendering if available and acceptable for the project.
5. Keep local authoring on Android/PRoot, then hand off the project directory to a renderer host.

## Verification pattern

When setting up the capability:

1. Install skills:

```bash
npx skills add heygen-com/hyperframes --yes --global
hermes skills list | grep -E 'hyperframes|gsap|tailwind|waapi|three'
```

2. Check prerequisites:

```bash
node -v
ffmpeg -version
npx hyperframes doctor
```

3. Smoke-test authoring:

```bash
rm -rf /tmp/hf-capability-demo
cd /tmp
npx hyperframes init hf-capability-demo --non-interactive --example blank
cd /tmp/hf-capability-demo
npx hyperframes lint
```

4. Only claim full local render capability after `validate` and `render` both succeed and the output MP4 exists and is non-empty.

## Reporting guidance

Be precise with Mohamed:

- Say video authoring and static validation are available if lint passes.
- Say local MP4 rendering is blocked if Chrome architecture mismatches.
- Do not overclaim full video-export capability until a real render succeeds.
