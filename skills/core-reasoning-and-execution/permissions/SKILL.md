---
name: permissions
description: "OpenClaw/Claude Code permission system reference: allow/ask/deny rules per tool and path, permission modes (default, plan, auto, acceptEdits, bypass), mode priority, and sensitive-path denials. Use when configuring agent permissions, debugging why a tool call was blocked or prompted, or choosing the right permission mode for a task."
tags: [permissions, security, claude-code, openclaw, configuration]
---

# OpenClaw Permission System Skill

Based on Claude Code's permission model: allow / ask / deny rules per tool and path.

## Quick Reference

### Permission Modes

| Mode | Description |
|------|-------------|
| `default` | Reads allowed, asks before edits/shell/network |
| `plan` | Read-only mode, no modifications |
| `auto` | Claude decides per-call, fewer interrupts |
| `acceptEdits` | Edits auto-approved, others ask |
| `bypass` | Full power, no prompts |

### Permission Levels

| Level | Symbol | Description |
|-------|--------|-------------|
| Allow | ✅ | Executes without asking |
| Ask | ❓ | Waits for confirmation |
| Deny | 🚫 | Refuses to execute |

### Mode Priority
**Plan > Bypass > Default > Auto > acceptEdits**

### Sensitive Paths (Always Denied)
```
./.env
./secrets/**
~/.ssh/**
./credentials/**
./**/*.pem
./**/google*.json
./**/aws*.json
```

---

## How It Works

### 1. Permission Check
Every tool call goes through the permission checker:

```python
from permissions import PermissionSettings, Decision

settings = PermissionSettings(mode="auto")
decision = settings.check("Bash", "", "rm -rf /")
# → Decision.DENY
```

### 2. Risk Classifier
In auto mode, the classifier evaluates each call:

| Category | Action |
|---------|--------|
| Safe patterns (ls, cat, echo, git status) | ✅ Auto-allow |
| Dangerous patterns (rm -rf, curl \| sh, chmod 777) | 🚫 Deny |
| Unknown or medium-risk | ❓ Ask |

### 3. Settings Hierarchy

Settings load in order, tighter rules win:

1. **System settings** — cannot be overridden
2. **User settings** — `~/.openclaw/permissions.json`
3. **Project settings** — `.openclaw/permissions.json`
4. **Local settings** — `.openclaw/permissions.local.json`

---

## Skill Vetting Workflow

When a new skill is proposed:

1. **Auto-vet** → `skill-vetter-advanced.py` scans for dangerous patterns
2. **Risk level** → safe / conditional / dangerous
3. **Decision** → auto-install / ask Mohamed / block
4. **Record** → saves vetting result to skill metadata

---

## Usage Examples

### Check a tool call
```python
settings = PermissionSettings(mode="auto")
result = settings.check("Bash", "", "git push origin main")
print(result.value)  # ask / allow / deny
```

### Change mode
```python
settings.mode = "plan"  # read-only
settings.mode = "bypass"  # full power
```

### Add a custom rule
```python
settings.rules.append(PermissionRule(
    tool="Bash",
    pattern="docker run:*",
    reason="Containers need explicit approval"
))
```

---

## OpenClaw Integration

### Auto Mode (recommended)
Set `mode: "auto"` in `.openclaw/permissions.json`.
- Safe commands execute automatically
- Risky commands ask before running
- Never accidentally runs dangerous commands

### Skill Vetting
Before installing any skill from ClawdHub or GitHub:
1. Run `skill-vetter-advanced.py` on the skill directory
2. Check for dangerous patterns
3. Auto-install safe skills
4. Flag dangerous ones for Mohamed's review

---

## Key Differences from Claude Code

| Feature | Claude Code | OpenClaw |
|---------|-------------|----------|
| Permission rules | ✅ | ✅ Implemented |
| Auto mode | ✅ | ✅ Implemented |
| Settings hierarchy | ✅ | ✅ Implemented |
| Managed settings | ✅ Enterprise | Planned |
| Risk classifier | Built-in AI | Regex-based |
| Skill vetting | MCP vetting | skill-vetter |

---

## Files
- `permissions.py` — Core permission engine
- `skill-vetter-advanced.py` — Permission-aware skill vetting
- `permissions.json` — Default settings
- `SKILL.md` — This file
