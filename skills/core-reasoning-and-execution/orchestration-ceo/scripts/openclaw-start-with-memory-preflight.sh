#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REAL_OPENCLAW="${OPENCLAW_REAL_BIN:-/data/data/com.termux/files/usr/bin/openclaw}"
BIONIC_SHIM="$HOME/.openclaw/workspace/scripts/openclaw-bionic-compat.js"
WHISPER_CPP_MODEL_BASE="$HOME/.local/opt/whisper.cpp/models/ggml-base.bin"
WHISPER_CPP_MODEL_TINY="$HOME/.local/opt/whisper.cpp/models/ggml-tiny.bin"

if [ -f "$BIONIC_SHIM" ]; then
  case " ${NODE_OPTIONS-} " in
    *" --require=$BIONIC_SHIM "*) ;;
    *) export NODE_OPTIONS="--require=$BIONIC_SHIM${NODE_OPTIONS:+ $NODE_OPTIONS}" ;;
  esac
fi

if [ -f "$WHISPER_CPP_MODEL_BASE" ]; then
  export WHISPER_CPP_MODEL="$WHISPER_CPP_MODEL_BASE"
elif [ -f "$WHISPER_CPP_MODEL_TINY" ]; then
  export WHISPER_CPP_MODEL="$WHISPER_CPP_MODEL_TINY"
fi

"$SCRIPT_DIR/ensure-memory-paths.sh"
exec "$REAL_OPENCLAW" gateway start "$@"
