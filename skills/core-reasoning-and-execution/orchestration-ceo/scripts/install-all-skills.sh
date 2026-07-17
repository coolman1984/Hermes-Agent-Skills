#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
DIST_DIR="${1:-$WORKSPACE_ROOT/dist}"
TARGET_ROOT="${2:-$HOME/.openclaw/skills}"
SYNC_SCRIPT="$WORKSPACE_ROOT/skills/capability-first/scripts/sync_capabilities.py"

shopt -s nullglob
packages=("$DIST_DIR"/*.skill)
shopt -u nullglob

if [ "${#packages[@]}" -eq 0 ]; then
  echo "No .skill packages found in $DIST_DIR" >&2
  exit 1
fi

mkdir -p "$TARGET_ROOT"

for package in "${packages[@]}"; do
  skill_name="$(basename "$package" .skill)"
  target_dir="$TARGET_ROOT/$skill_name"
  echo "Installing $skill_name -> $target_dir" >&2
  rm -rf "$target_dir"
  python3 - "$package" "$TARGET_ROOT" <<'PY'
import pathlib
import sys
import zipfile

archive = pathlib.Path(sys.argv[1])
target_root = pathlib.Path(sys.argv[2])
with zipfile.ZipFile(archive) as zf:
    zf.extractall(target_root)
PY
done

python3 "$SYNC_SCRIPT" --refresh

echo "Installed ${#packages[@]} skill package(s) from $DIST_DIR into $TARGET_ROOT" >&2
