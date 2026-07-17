#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="${OPENCLAW_WORKSPACE:-$HOME/.openclaw/workspace}"
TODAY="${OPENCLAW_DAILY_DATE:-$(date +%F)}"

mkdir -p "$WORKSPACE/memory" "$WORKSPACE/projects"
touch "$WORKSPACE/MEMORY.md"
touch "$WORKSPACE/memory/$TODAY.md"

printf 'memory paths ready: %s\n' "$WORKSPACE"
