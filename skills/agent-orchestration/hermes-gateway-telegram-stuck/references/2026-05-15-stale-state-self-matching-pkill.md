# 2026-05-15 Telegram gateway stale state + self-matching pkill

## Symptom
Telegram stopped responding. `hermes gateway status` reported the user gateway service was stopped, but this is not authoritative in PRoot/no-systemd environments.

## Findings
- No live gateway process existed.
- `/root/.hermes/gateway_state.json` claimed `gateway_state=running` and pointed at PID `11158`.
- `/proc/11158` was missing, proving stale state.
- Bot API `getMe` succeeded for the configured Telegram bot, so the token and Telegram API were reachable.
- Runtime import check for `openai.OpenAI` succeeded, so this was not the post-update OpenAI namespace corruption case.

## Recovery used
1. Verified no live gateway process and stale PID.
2. Removed `/root/.hermes/gateway_state.json` and stale PID files.
3. Started exactly one gateway using the terminal background process tool:
   `env HERMES_HOME=/root/.hermes PYTHONUNBUFFERED=1 /root/.local/bin/hermes gateway run --replace`
4. Verified:
   - one live gateway process
   - state PID existed under `/proc/<pid>`
   - state said `gateway_state=running`
   - Telegram platform state was `connected`
   - log showed `Connected to Telegram (polling mode)` and `Gateway running with 1 platform(s)`
   - Bot API `getMe` still succeeded

## Pitfall discovered
A foreground cleanup command containing `pkill -f "gateway run --replace"` exited with `-15` and did not remove stale state. Likely cause: the shell/tool command line itself contained the pkill pattern and got matched. Lesson: after any pkill cleanup in Hermes terminal tools, immediately re-check state and process list; if state remains, remove files with Python unlink or use a narrower pkill pattern that does not match the invoking command line.
