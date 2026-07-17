#!/usr/bin/env python3
"""
OpenClaw Permission System
Based on Claude Code's permission model: allow / ask / deny rules per tool and path.
"""
import re
import fnmatch
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum
import json

# Permission result
class Decision(Enum):
    ALLOW = "allow"
    ASK = "ask"
    DENY = "deny"


@dataclass
class PermissionRule:
    tool: str          # tool name, e.g. "Bash", "Write", "Read"
    pattern: str       # glob or exact match, e.g. "*.env", "rm:*", "./secrets/**"
    reason: str = ""  # why this rule exists

    def matches(self, tool: str, path: str = "") -> bool:
        if self.tool != tool and self.tool != "*":
            return False
        # Support glob patterns
        return fnmatch.fnmatch(path, self.pattern) or self.pattern == "*"


@dataclass
class PermissionSettings:
    mode: str = "default"  # default | plan | auto | acceptEdits | bypass
    rules: List[PermissionRule] = field(default_factory=list)
    # Sensitive paths always denied
    sensitive_paths: List[str] = field(default_factory=lambda: [
        "./.env",
        "./secrets/**",
        "~/.ssh/**",
        "./credentials/**",
        "./keys/**",
        "./**/id_rsa*",
        "./**/*.pem",
        "./**/google*.json",
        "./**/aws*.json",
    ])

    @classmethod
    def from_file(cls, path: Path) -> "PermissionSettings":
        if not path.exists():
            return cls()
        try:
            with open(path) as f:
                data = json.load(f)
            settings = cls()
            settings.mode = data.get("mode", "default")
            for r in data.get("rules", []):
                settings.rules.append(PermissionRule(
                    tool=r.get("tool", "*"),
                    pattern=r.get("pattern", "*"),
                    reason=r.get("reason", ""),
                ))
            return settings
        except Exception:
            return cls()

    def to_file(self, path: Path):
        data = {
            "mode": self.mode,
            "rules": [
                {"tool": r.tool, "pattern": r.pattern, "reason": r.reason}
                for r in self.rules
            ]
        }
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def check(self, tool: str, path: str = "", detail: str = "") -> Decision:
        """
        Check if a tool call is allowed, needs asking, or should be denied.
        Priority: deny > ask > allow
        """
        # Plan mode: no modifications allowed
        if self.mode == "plan":
            return Decision.DENY if tool in ("Write", "Edit", "Bash", "bash") else Decision.ALLOW

        # Bypass mode: everything allowed
        if self.mode == "bypass":
            return Decision.ALLOW

        # Sensitive path check
        for sp in self.sensitive_paths:
            if fnmatch.fnmatch(path, sp):
                return Decision.DENY

        # acceptEdits mode: skip prompts for file edits
        if self.mode == "acceptEdits":
            if tool in ("Write", "Edit"):
                return Decision.ALLOW
            return Decision.ASK

        # auto mode: use risk classifier
        if self.mode == "auto":
            return _risk_classifier(tool, path, detail)

        # default mode: deny dangerous tools, ask for others
        dangerous_tools = {"Bash", "bash", "Write", "Edit", "WebFetch", "Bash"}
        if tool in dangerous_tools:
            # Check deny rules first
            for rule in self.rules:
                if rule.pattern == "deny" and (rule.tool == tool or rule.tool == "*"):
                    return Decision.DENY
            return Decision.ASK

        return Decision.ALLOW


def _risk_classifier(tool: str, path: str = "", detail: str = "") -> Decision:
    """
    Classify a tool call as safe, ask, or deny.
    Based on Claude Code's auto mode risk classification.
    """
    detail_lower = (detail or "").lower()
    path_lower = (path or "").lower()

    # ALWAYS DENY — highest risk
    deny_patterns = [
        (r"rm\s+-rf\s+/?\s|rm\s+-rf\s+\*", "Destructive root deletion"),
        (r"curl.*\|.*sh|wget.*\|.*sh", "Pipe to shell — potential injection"),
        (r"eval\s+\$.*curl", "Eval with remote curl"),
        (r"ssh\s+.*password|scp\s+.*password", "Password in SSH command"),
        (r"chmod\s+777", "World-writable permission"),
        (r"shutdown|reboot|init\s+0|init\s+6", "System shutdown/reboot"),
        (r"dd\s+.*of=/dev/sd|dd\s+.*of=/dev/n", "Direct disk write"),
        (r">\s*/etc/passwd|>\s*/etc/shadow", "System file overwrite"),
        (r"git\s+push\s+--force", "Force push — history rewrite"),
        (r"docker\s+run\s+--privileged", "Privileged container"),
        (r"openssl\s+rand.*base64.*\|.*openssl", "Key generation piped"),
        (r"rm\s+-rf\s+/\s*", "Root deletion attempt"),
    ]
    for pattern, _ in deny_patterns:
        if re.search(pattern, detail_lower) or re.search(pattern, path_lower):
            return Decision.DENY

    # ALWAYS ALLOW — low risk, routine
    allow_patterns = [
        (r"^ls\s|^ls\s+-", "Directory listing"),
        (r"^cat\s+.*\.py$|^cat\s+.*\.txt$|^cat\s+.*\.md$", "Reading text files"),
        (r"^pwd$|^whoami$|^date$|^uptime$", "System info commands"),
        (r"^echo\s+", "Echo output"),
        (r"^head\s+|^tail\s+", "File preview"),
        (r"^grep\s+|^rg\s+", "Search"),
        (r"^git\s+status$|^git\s+diff$|^git\s+log", "Git read-only"),
        (r"^python3?\s+-c\s+", "Python one-liner"),
        (r"^mkdir\s+", "Directory creation"),
        (r"^touch\s+", "File creation"),
        (r"^cp\s+.*\.\w+\s+", "File copy"),
        (r"^wc\s+", "Line count"),
    ]
    for pattern, _ in allow_patterns:
        if re.search(pattern, detail_lower):
            return Decision.ALLOW

    # ASK — medium risk, needs human judgment
    ask_patterns = [
        (r"Bash|bash|shell", "Shell command"),
        (r"Write|Edit|Edit.*file", "File modification"),
        (r"git\s+push|git\s+commit", "Git write operation"),
        (r"curl|wget|fetch|download", "Network access"),
        (r"docker\s+run", "Container execution"),
        (r"delete|remove|rm\s+", "Deletion operation"),
        (r"npm\s+install|pip\s+install|apt-get", "Package installation"),
        (r"chmod\s+", "Permission change"),
        (r"\.env$|password|secret|token|key", "Sensitive file access"),
    ]
    for pattern, _ in ask_patterns:
        if re.search(pattern, detail_lower) or re.search(pattern, path_lower):
            return Decision.ASK

    # Default for unknown: ask
    return Decision.ASK


def explain_decision(decision: Decision, tool: str, path: str = "") -> str:
    if decision == Decision.ALLOW:
        return f"✅ {tool} on '{path}' — allowed automatically"
    elif decision == Decision.DENY:
        return f"🚫 {tool} on '{path}' — denied (would explain why)"
    else:
        return f"❓ {tool} on '{path}' — needs your confirmation"


# Quick test
if __name__ == "__main__":
    test_cases = [
        ("Bash", "", "rm -rf /"),
        ("Bash", "", "ls -la"),
        ("Write", "./src/main.py", "print('hello')"),
        ("Write", "./.env", "API_KEY=secret"),
        ("Bash", "", "git push origin main"),
        ("Bash", "", "curl https://api.github.com"),
        ("Read", "./secrets/token.txt", ""),
        ("Bash", "", "echo 'hello world'"),
    ]

    settings = PermissionSettings(mode="auto")
    for tool, path, detail in test_cases:
        d = settings.check(tool, path, detail)
        print(explain_decision(d, tool, path))
