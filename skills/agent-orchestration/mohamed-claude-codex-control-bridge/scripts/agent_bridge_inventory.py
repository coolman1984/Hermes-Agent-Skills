#!/usr/bin/env python3
"""Safe inventory for Mohamed's Claude/Codex/Hermes bridge.

Prints versions, health summaries, and non-secret skill/config paths.
Does not read auth.json, .env, tokens, or private keys.
"""
from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


def run(cmd: list[str], timeout: int = 30) -> str:
    try:
        p = subprocess.run(cmd, text=True, capture_output=True, timeout=timeout)
        out = (p.stdout + p.stderr).strip()
        return out[:4000] if out else f"exit={p.returncode}"
    except Exception as e:
        return f"ERROR: {type(e).__name__}: {e}"


def list_dir(path: Path, limit: int = 40) -> list[str]:
    if not path.exists():
        return ["MISSING"]
    rows = []
    for p in sorted(path.iterdir())[:limit]:
        rows.append((p.name + "/") if p.is_dir() else p.name)
    return rows


def main() -> int:
    print("== binaries ==")
    for name in ["hermes", "claude", "claude-safe", "codex", "opencode", "gemini", "tmux"]:
        print(f"{name}: {shutil.which(name) or 'MISSING'}")

    print("\n== versions ==")
    checks = [
        ["hermes", "--version"],
        ["claude", "--version"],
        ["/root/.local/bin/claude-safe", "--version"],
        ["codex", "--version"],
        ["opencode", "--version"],
        ["gemini", "--version"],
    ]
    for cmd in checks:
        if shutil.which(cmd[0]) or Path(cmd[0]).exists():
            print(f"$ {' '.join(cmd)}")
            print(run(cmd, timeout=20))

    print("\n== safe config paths ==")
    for raw in [
        "~/.claude/CLAUDE.md",
        "~/.claude/settings.json",
        "~/.codex/config.toml",
        "~/.codex/skills",
        "~/.codex/skills/.system",
        "~/.local/share/opencode",
        "~/.config/opencode/opencode.jsonc",
        "~/.gemini/settings.json",
        "~/.local/bin/gemini-auto",
        "~/.local/bin/claude-auto",
        "~/.local/bin/codex-auto",
        "~/.local/bin/opencode-auto",
        "~/.hermes/skills/autonomous-ai-agents/mohamed-claude-codex-control-bridge/SKILL.md",
    ]:
        p = Path(raw).expanduser()
        if p.exists():
            print(f"{p} size={p.stat().st_size if p.is_file() else 'dir'}")
        else:
            print(f"{p} MISSING")

    print("\n== codex system skills ==")
    for item in list_dir(Path("~/.codex/skills/.system").expanduser()):
        print(item)

    print("\n== codex doctor summary ==")
    print(run(["codex", "doctor", "--summary"], timeout=60))

    print("\n== opencode auth/models summary ==")
    print(run(["opencode", "auth", "list"], timeout=30))
    print(run(["opencode", "models", "opencode-go"], timeout=60))

    print("\n== gemini auth presence ==")
    for key in ["GEMINI_API_KEY", "GOOGLE_API_KEY", "GOOGLE_GENAI_USE_VERTEXAI", "GOOGLE_GENAI_USE_GCA"]:
        print(f"{key}_present={bool(os.environ.get(key))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
