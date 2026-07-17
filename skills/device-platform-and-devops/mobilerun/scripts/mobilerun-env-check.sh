#!/usr/bin/env bash
set -euo pipefail

if [ -z "${MOBILERUN_API_KEY:-}" ]; then
  echo "MOBILERUN_API_KEY is not set" >&2
  exit 1
fi

if ! command -v adb >/dev/null 2>&1; then
  echo "adb is not installed or not on PATH" >&2
  exit 1
fi

echo "mobilerun prerequisites look present"
