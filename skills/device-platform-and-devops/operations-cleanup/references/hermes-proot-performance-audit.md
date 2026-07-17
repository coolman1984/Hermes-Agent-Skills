# Hermes/OpenClaw Performance Audit in Android PRoot

Use this when Mohamed asks to inspect or improve assistant/system performance from inside Hermes/OpenClaw.

## What mattered in the 2026-05-12 audit

- `hermes gateway status` can be misleading in no-systemd PRoot. Trust live processes, logs, and state files.
- A stale foreground tool process can survive for weeks and consume CPU. In this case an old `opencode` process had been running for more than 27 days.
- Stale gateway state in stopped profiles can mislead diagnosis. Move stale state files to a backup directory instead of deleting them blindly.
- Old `/tmp` clutter can accumulate many build artifacts and temporary shared libraries; clean only old, low-risk patterns.
- Market/profile crons may exist but not fire because that profile gateway is stopped. Do not start a second Telegram poller if it may reuse the primary bot token.

## Audit checklist

1. Write a short plan to `tasks/todo.md` for non-trivial cleanup.
2. Capture system state:
   - `date -Is`
   - `uname -a`
   - `uptime`
   - `df -h / /root /tmp /storage/emulated/0/Download`
   - `free -h`
   - `ps -eo pid,ppid,stat,%cpu,%mem,rss,etime,cmd --sort=-%cpu | head -25`
3. Check Hermes state:
   - `hermes status --all`
   - `hermes gateway status`
   - `hermes profile list`
   - `hermes cron list`
   - profile-specific cron lists when relevant, e.g. `hermes -p market cron list`
4. Check important databases with SQLite integrity checks:
   - `/root/.hermes/kanban.db`
   - `/root/.hermes/state.db`
   - `/root/.hermes/profiles/*/state.db`
5. Search logs for recent failures:
   - `/root/.hermes/logs/*.log`
   - `/root/.hermes/profiles/*/logs/*.log`
6. Inspect stale/heavy processes by age and CPU. Kill only clear stale processes, then verify they disappeared.
7. Clean safe old temporary files only:
   - old `/tmp/hermes_sandbox_*`
   - old `/tmp/pip-*`
   - old `/tmp/tmp.*`
   - old `/tmp/node-gyp-*`
   - old `.5*.so` temporary libraries
8. For stale gateway state in stopped profiles, move to `stale-state-backups/` only when the recorded PID does not exist.
9. Re-run verification: process list, gateway state, DB integrity, and recent log tail.
10. Write a concise diagnostic report in the vault when the cleanup changed system state.

## Pitfalls

- Do not use broad `rm -rf /tmp/*` in PRoot/Termux.
- Do not start profile gateways casually; a second Telegram poller can create token conflicts.
- Avoid long recursive `du` over huge trees during a live Telegram session unless scoped or timed.
- Memory pressure may come from Android/Termux outside Hermes; do not over-attribute all RAM/swap use to the assistant.
