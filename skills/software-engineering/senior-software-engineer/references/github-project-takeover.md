# GitHub Project Takeover Workflow

Use when Mohamed decides that a copied/forked GitHub repository is now the active project and the older repo is only an upstream reference.

## Goal

Make local work target the new GitHub repository while preserving the original repository as a named reference.

## Safe sequence

```bash
cd /path/to/project

git status --short
git branch --show-current
git remote -v

# If the new repo remote already exists under a temporary name:
git remote rename origin upstream-original
git remote rename company-dashboard-project origin

git fetch origin --prune

git checkout -b main --track origin/main 2>/dev/null || git checkout main
git pull --ff-only origin main

git status --short
git branch --show-current
git remote -v
git branch -vv
```

## Rules

- Do not make `main` the editing branch for feature work.
- Create work branches from the new repo's `main`, e.g. `hermes/<short-task>`.
- Keep the older repo as `upstream-original` for comparison/recovery only.
- Never put a GitHub token in the remote URL.
- Use `gh auth setup-git` or the configured credential helper instead.

## Verification

Minimum evidence before declaring the project switched:

```text
origin -> new GitHub project repo
upstream-original -> old/source repo
branch -> main
status -> clean except ignored generated files
```

Then run the repository's real test gates before future feature work.