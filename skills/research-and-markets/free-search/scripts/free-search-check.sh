#!/usr/bin/env bash
set -euo pipefail

missing=()
for bin in curl; do
  command -v "$bin" >/dev/null 2>&1 || missing+=("$bin")
done

if [ "${#missing[@]}" -gt 0 ]; then
  printf 'missing: %s\n' "${missing[*]}" >&2
  exit 1
fi

if command -v ddgr >/dev/null 2>&1; then
  echo "ddgr: present"
else
  echo "ddgr: missing"
fi

if python3 - <<'PY' >/dev/null 2>&1
import importlib.util
raise SystemExit(0 if importlib.util.find_spec('trafilatura') else 1)
PY
then
  echo "trafilatura: present"
else
  echo "trafilatura: missing"
fi
