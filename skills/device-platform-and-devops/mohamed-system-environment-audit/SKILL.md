---
name: mohamed-system-environment-audit
description: Produce a grounded Arabic system-environment audit for Mohamed's Hermes/local agent setup, with live checks, UX/architecture critique, and an actionable roadmap for future projects.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  tags: [mohamed, hermes, environment-audit, systems-architecture, ui-ux, operations, report]
---

# Mohamed System Environment Audit

## When to use

Use this when Mohamed asks for a serious report, audit, architecture review, system environment review, or development roadmap for the environment the assistant is running in — especially Hermes, Telegram gateway, local vaults, profiles, tools, cron jobs, or future project infrastructure.

Typical triggers:

- "اعمل تقرير عن بيئة النظام"
- "عايز نطور النظام للمشاريع القادمة"
- "راجع هيرمس والبروفايلات والأدوات"
- "اعتبر نفسك خبير هندسة برمجيات وواجهة مستخدم"
- "اعمل خطة تطوير حقيقية للنظام"

## Output rule

Default deliverable is a verified Markdown report under:

`/storage/emulated/0/Download/system-reports/`

Return a short chat summary plus `MEDIA:` attachment. Do not leave the work as chat-only unless Mohamed explicitly asks for a quick answer.

## Required workflow

1. Load `hermes-agent` first if Hermes itself is in scope.
2. Read the live operational snapshot:
   `/root/Documents/Obsidian Vault/CURRENT-SNAPSHOT.md`
3. Create or update `/root/tasks/todo.md` with scope, constraints, and report intent.
4. Gather live facts using safe, non-secret checks:
   - current date and timezone
   - OS, kernel, architecture
   - CPU, memory, swap, disk
   - active Hermes/gateway/browser processes
   - Hermes version and git state
   - `hermes doctor`
   - `hermes config check`
   - profile list and profile summaries
   - enabled tools for default and Telegram
   - cron list
   - session stats
   - MCP list
   - key directory sizes
   - recent gateway logs, filtered for errors and restart events
5. Redact secrets. Never print `.env` contents, tokens, passwords, raw auth files, or private chat IDs unless already explicitly provided and needed.
6. Analyze the system like an operator, not as a generic explainer:
   - architecture
   - reliability
   - security boundaries
   - project-state management
   - UX surface
   - memory and knowledge hygiene
   - automation readiness
   - risks and tradeoffs
7. Write a detailed Arabic report with practical recommendations, not just observations.
8. Verify the report exists, is non-empty, has expected headings, and record line count or size before final delivery.

## Suggested live command set

Use these as a checklist, adapting safely to the current environment:

```bash
date -Is
TZ=Africa/Cairo date '+%Y-%m-%d %H:%M:%S %Z'
uname -a
sed -n '1,12p' /etc/os-release
nproc
lscpu | sed -n '1,35p'
free -h
df -hT / /root /storage/emulated/0 2>/dev/null || df -hT
python --version
python3 --version
pip --version || true
uv --version || true
node --version || true
npm --version || true
ps -efww | grep -E 'hermes|gateway|python|node|tmux' | grep -v grep
ps -eo pid,ppid,comm,%cpu,%mem,rss,args --sort=-rss | sed -n '1,25p'
hermes --version || true
git -C /root/.hermes/hermes-agent status -sb || true
git -C /root/.hermes/hermes-agent describe --tags --always --dirty || true
git -C /root/.hermes/hermes-agent log --oneline --decorate -n 12 || true
hermes config check || true
hermes doctor || true
hermes profile list || true
hermes tools list || true
hermes tools list --platform telegram || true
hermes cron list || true
hermes sessions stats || true
hermes mcp list || true
du -sh /root/.hermes /root/.hermes/hermes-agent '/root/Documents/Obsidian Vault' /root/llm-wiki-agent /storage/emulated/0/Download/media-notes 2>/dev/null || true
du -sh /root/.hermes/{sessions,logs,skills,cron,memories,profiles} 2>/dev/null || true
grep -iE 'error|exception|traceback|failed|timeout|unauthorized|invalid' /root/.hermes/logs/gateway.log 2>/dev/null | tail -60 || true
tail -80 /root/.hermes/logs/gateway.log 2>/dev/null || true
```

For config summaries, parse and redact keys with a script using Hermes' venv Python if system Python lacks packages. Never dump secrets.

## Report structure

Recommended sections:

1. Executive judgment.
2. Live environment summary.
3. Hermes version and health.
4. Gateway and messaging surface.
5. Running processes and resource pressure.
6. Profiles and isolation boundaries.
7. Tools, MCP, cron jobs, and session database.
8. Vault, wiki, media notes, and knowledge topology.
9. Strengths.
10. Risks and bottlenecks.
11. UI/UX assessment.
12. Proposed project operating model.
13. Phased roadmap.
14. Design decisions.
15. Priority recommendations.
16. What not to do yet.
17. Evidence and commands used.

## Mohamed-specific judgment rules

- Push back against building a big UI before project state and governance are stable.
- Prefer files and project state cards before databases or dashboards.
- Treat Telegram as a fast command surface, not the whole project-management interface.
- Recommend project templates before extra automation.
- Separate production profiles from experiment profiles.
- Highlight alias/profile collisions as operational risks.
- In PRoot/Android, trust processes and logs over service status when systemd is unavailable.
- Do not treat every warning as urgent. Distinguish production risks from optional missing integrations.

## Project template recommendation

For future projects, recommend a folder/card shape like:

```text
PROJECT.md
STATE.md
SOURCES.md
DECISIONS.md
TASKS.md
OUTPUTS.md
ERRORS.md
AUTOMATIONS.md
```

Explain that this lets future agents enter a project without asking Mohamed to repeat context.

## Verification

Before final response:

- Re-open or stat the report file.
- Confirm size is greater than zero.
- Confirm required sections exist.
- Include absolute path and `MEDIA:` attachment.
- Keep chat reply short; the detailed content belongs in the report file.

## Pitfalls

- Do not expose secrets while proving configuration.
- Do not write environment-specific failures as permanent rules; report them as current findings.
- Do not overfit a report into a new project. A report is useful only if it produces next actions.
- Do not let the audit become a generic hardware inventory. Mohamed asked for development leverage.
