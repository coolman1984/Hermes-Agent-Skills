#!/usr/bin/env bash
set -euo pipefail

if ! command -v adb >/dev/null 2>&1; then
  echo "adb not found on PATH" >&2
  exit 1
fi

echo "ADB version:"
adb version

echo

echo "Connected devices:"
adb devices
