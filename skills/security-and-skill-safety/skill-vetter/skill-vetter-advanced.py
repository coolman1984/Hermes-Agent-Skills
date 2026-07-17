#!/usr/bin/env python3
"""
OpenClaw Permission-Aware Skill Vetting
Checks new skills against the permission system before installation.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

# Permission patterns from the permission system
ALWAYS_DENY_PATTERNS = [
    r"rm\s+-rf", r"curl.*\|.*sh", r"eval.*\$", r"chmod\s+777",
    r"shutdown|reboot", r"dd\s+.*of=/dev/", r"git\s+push\s+--force",
    r"docker\s+run\s+--privileged", r"\.env$", r"password.*=.*",
]

ALWAYS_ALLOW_PATTERNS = [
    r"ls\s", r"cat\s", r"echo\s", r"pwd$", r"grep\s", r"mkdir\s",
    r"touch\s", r"head\s", r"tail\s", r"wc\s", r"git\s+status",
    r"git\s+diff",
]

REQUIRES_CONFIRMATION = [
    "Bash", "Write", "Edit", "curl", "wget", "pip install",
    "npm install", "apt-get", "yum install", "docker",
]


def classify_skill(skill_path: Path) -> dict:
    """Analyze a skill directory for permission requirements."""
    findings = {
        "skill": skill_path.name,
        "permission_level": "safe",
        "concerns": [],
        "allowed_tools": [],
        "requires_confirmation": [],
        "risks": [],
    }

    # Scan all files in the skill
    for file in skill_path.rglob("*"):
        if not file.is_file():
            continue
        if file.suffix in [".md", ".txt", ".git"]:
            continue

        try:
            content = file.read_text(errors="ignore")
        except Exception:
            continue

        for pattern in ALWAYS_DENY_PATTERNS:
            if re.search(pattern, content, re.IGNORECASE):
                findings["risks"].append(
                    f"⚠️  Dangerous pattern '{pattern}' in {file.relative_to(skill_path)}"
                )
                findings["permission_level"] = "dangerous"

        for pattern in ALWAYS_ALLOW_PATTERNS:
            if re.search(pattern, content, re.IGNORECASE):
                findings["allowed_tools"].append(pattern)

        for tool in REQUIRES_CONFIRMATION:
            if re.search(rf"\b{tool}\b", content, re.IGNORECASE):
                if tool not in findings["requires_confirmation"]:
                    findings["requires_confirmation"].append(tool)

    return findings


def vet_skill(skill_path: str) -> bool:
    """Vet a skill and print findings. Returns True if safe to install."""
    path = Path(skill_path)
    if not path.exists():
        print(f"❌ Skill not found: {skill_path}")
        return False

    print(f"\n🔍 Vetting skill: {path.name}\n")

    findings = classify_skill(path)

    print(f"📊 Permission Level: {findings['permission_level'].upper()}")
    print(f"✅ Allowed tools: {findings['allowed_tools'] or 'none detected'}")
    print(f"⚠️  Requires confirmation: {findings['requires_confirmation'] or 'none'}")
    print(f"🚫 Risks: {len(findings['risks'])}")

    if findings["risks"]:
        print("\n🚫 Risk details:")
        for risk in findings["risks"]:
            print(f"  {risk}")

    # Auto-install if safe, block if dangerous
    if findings["permission_level"] == "dangerous":
        print("\n❌ BLOCKED: This skill contains dangerous patterns.")
        print("   Ask Mohamed before installing.")
        return False

    if findings["requires_confirmation"]:
        print("\n⚠️  APPROVED WITH CONDITIONS:")
        print(f"   These tools will require your confirmation: {findings['requires_confirmation']}")
    else:
        print("\n✅ APPROVED: Safe to install automatically.")

    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 skill-vetter-advanced.py /path/to/skill")
        sys.exit(1)
    vet_skill(sys.argv[1])
