---
name: codex
description: "Delegate coding to OpenAI Codex CLI (features, PRs)."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Coding-Agent, Codex, OpenAI, Code-Review, Refactoring]
    related_skills: [claude-code, hermes-agent]
---

# Codex CLI

Delegate coding tasks to [Codex](https://github.com/openai/codex) via the Hermes terminal. Codex is OpenAI's autonomous coding agent CLI.

## When to use

- Building features
- Refactoring
- PR reviews
- Batch issue fixing

Requires the codex CLI and a git repository.

## Prerequisites

- Codex installed: `npm install -g @openai/codex`
- OpenAI auth configured: either `OPENAI_API_KEY` or Codex OAuth credentials
  from the Codex CLI login flow
- **Must run inside a git repository** — Codex refuses to run outside one
- Use `pty=true` in terminal calls — Codex is an interactive terminal app

For Hermes itself, `model.provider: openai-codex` uses Hermes-managed Codex
OAuth from `~/.hermes/auth.json` after `hermes auth add openai-codex`. For the
standalone Codex CLI, a valid CLI OAuth session may live under
`~/.codex/auth.json`; do not treat a missing `OPENAI_API_KEY` alone as proof
that Codex auth is missing.

Important auth boundary: Hermes `openai-codex` OAuth tokens in
`~/.hermes/auth.json` are not automatically a drop-in replacement for the
standalone Codex CLI's `~/.codex/auth.json`. Recent Codex CLI versions may
require additional ChatGPT/Codex account metadata such as an agent identity;
`codex login --with-access-token` can fail with `agent identity JWT payload is
not valid JSON` when fed a Hermes access token. In that case, either run
`codex login --device-auth` for the standalone CLI, provide a real supported
OpenAI API key via `codex login --with-api-key`, or invoke Hermes directly with
`hermes chat --provider openai-codex ...` when the goal is to use the existing
Hermes-managed Codex OAuth.

### Termux / Android arm64 install repair

If `codex` exists but exits before help/version with a missing optional dependency such as `@openai/codex-linux-arm64`, reinstall into the prefix that owns the running Termux executable, then align npm's prefix:

```bash
which -a codex
readlink -f /data/data/com.termux/files/usr/bin/codex || true
npm install -g --prefix /data/data/com.termux/files/usr @openai/codex@latest
npm config set prefix /data/data/com.termux/files/usr
codex --version
codex doctor --summary
```

If `codex doctor` is then install-consistent but auth fails, use `codex login --device-auth` or pipe an API key into `codex login --with-api-key`. Keep binary-install health separate from auth health.

Session detail and verification transcript pattern: `references/termux-arm64-install-repair.md`.

## Mohamed quota policy

When operating Codex CLI for Mohamed, do not leave model selection implicit. Use only these two pairings unless Mohamed explicitly changes the rule:

- Hard / important coding tasks: `-m gpt-5.5 -c model_reasoning_effort='"medium"'`
- Easy / low-risk coding tasks: `-m gpt-5.4-mini -c model_reasoning_effort='"xhigh"'`

Do **not** use `high` or `xhigh` with `gpt-5.5`; Mohamed wants to protect quota even on difficult work.

## One-Shot Tasks

```
terminal(command="codex exec -m gpt-5.5 -c model_reasoning_effort='\"medium\"' 'Add dark mode toggle to settings'", workdir="~/project", pty=true)
```

For scratch work (Codex needs a git repo unless `--skip-git-repo-check` is appropriate):
```
terminal(command="cd $(mktemp -d) && git init && codex exec -m gpt-5.4-mini -c model_reasoning_effort='\"xhigh\"' 'Build a tiny throwaway Python example'", pty=true)
```

For non-interactive `codex exec`, approval policy is not exposed as `-a`; set it with config override instead:
```
codex exec -c approval_policy='"never"' -s read-only 'Health check only. Do not modify files.'
```

## Background Mode (Long Tasks)

```
# Start in background with PTY
terminal(command="codex exec --full-auto 'Refactor the auth module'", workdir="~/project", background=true, pty=true)
# Returns session_id

# Monitor progress
process(action="poll", session_id="<id>")
process(action="log", session_id="<id>")

# Send input if Codex asks a question
process(action="submit", session_id="<id>", data="yes")

# Kill if needed
process(action="kill", session_id="<id>")
```

## Key Flags

| Flag | Effect |
|------|--------|
| `exec "prompt"` | One-shot execution, exits when done |
| `--full-auto` | Sandboxed but auto-approves file changes in workspace |
| `--yolo` | No sandbox, no approvals (fastest, most dangerous) |

## PR Reviews

Clone to a temp directory for safe review:

```
terminal(command="REVIEW=$(mktemp -d) && git clone https://github.com/user/repo.git $REVIEW && cd $REVIEW && gh pr checkout 42 && codex review --base origin/main", pty=true)
```

## Parallel Issue Fixing with Worktrees

```
# Create worktrees
terminal(command="git worktree add -b fix/issue-78 /tmp/issue-78 main", workdir="~/project")
terminal(command="git worktree add -b fix/issue-99 /tmp/issue-99 main", workdir="~/project")

# Launch Codex in each
terminal(command="codex --yolo exec 'Fix issue #78: <description>. Commit when done.'", workdir="/tmp/issue-78", background=true, pty=true)
terminal(command="codex --yolo exec 'Fix issue #99: <description>. Commit when done.'", workdir="/tmp/issue-99", background=true, pty=true)

# Monitor
process(action="list")

# After completion, push and create PRs
terminal(command="cd /tmp/issue-78 && git push -u origin fix/issue-78")
terminal(command="gh pr create --repo user/repo --head fix/issue-78 --title 'fix: ...' --body '...'")

# Cleanup
terminal(command="git worktree remove /tmp/issue-78", workdir="~/project")
```

## Batch PR Reviews

```
# Fetch all PR refs
terminal(command="git fetch origin '+refs/pull/*/head:refs/remotes/origin/pr/*'", workdir="~/project")

# Review multiple PRs in parallel
terminal(command="codex exec 'Review PR #86. git diff origin/main...origin/pr/86'", workdir="~/project", background=true, pty=true)
terminal(command="codex exec 'Review PR #87. git diff origin/main...origin/pr/87'", workdir="~/project", background=true, pty=true)

# Post results
terminal(command="gh pr comment 86 --body '<review>'", workdir="~/project")
```

## Rules

1. **Always use `pty=true`** — Codex is an interactive terminal app and hangs without a PTY
2. **Git repo required** — Codex won't run outside a git directory. Use `mktemp -d && git init` for scratch
3. **Use `exec` for one-shots** — `codex exec "prompt"` runs and exits cleanly
4. **`--full-auto` for building** — auto-approves changes within the sandbox
5. **Background for long tasks** — use `background=true` and monitor with `process` tool
6. **Don't interfere** — monitor with `poll`/`log`, be patient with long-running tasks
7. **Parallel is fine** — run multiple Codex processes at once for batch work
8. **For Mohamed, enforce the quota pairings** — hard tasks use `gpt-5.5` with `medium`; easy tasks use `gpt-5.4-mini` with `xhigh`; never silently increase `gpt-5.5` reasoning above `medium`
9. **Health check before real delegation** — run `codex doctor --summary`, verify auth is complete or `OPENAI_API_KEY` is present, then run a read-only smoke test in a temp git repo with the exact model/effort pairing intended for the task
10. **`codex exec` approval flag pitfall** — do not pass `-a` to `codex exec`; use `-c approval_policy='"never"'` or another config override instead
