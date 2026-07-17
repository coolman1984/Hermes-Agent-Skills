#!/usr/bin/env bash
set -euo pipefail

TERMUX_PREFIX="${TERMUX_PREFIX:-/data/data/com.termux/files/usr}"
cmd="$(basename "$0")"
exec "$TERMUX_PREFIX/bin/$cmd" "$@"
