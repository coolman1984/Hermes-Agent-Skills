---
name: github-workflows
description: "Use when working with GitHub repositories end-to-end: authentication, repository setup, issues, pull requests, CI triage, review, and release-adjacent gh/REST workflows."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [github, gh-cli, pull-requests, issues, code-review, repository-management, ci]
    related_skills: []
---

# GitHub Workflows

## Overview

This is the class-level umbrella for GitHub work. Use it instead of loading separate one-task skills for auth, repo setup, issues, pull requests, and review. The normal workflow is to establish authentication and remotes, inspect current git/GitHub state, perform the requested repository action with `git`/`gh`/REST, then verify the result with live command output.

Absorbed original skill packages are preserved under `references/absorbed/<skill-name>/` for complete detail and support files.

## When to Use

- Creating, cloning, forking, or configuring GitHub repositories and remotes.
- Setting up or repairing `gh` authentication, HTTPS tokens, SSH keys, and safe token handling.
- Creating, triaging, labeling, or updating GitHub issues.
- Opening, updating, reviewing, or merging pull requests.
- Investigating failed CI/checks before or after PR creation.
- Performing a code review that needs GitHub diff/comment context.

Do not use this for generic local git history questions unless GitHub state matters; use terminal/git directly for purely local operations.

## Operating Sequence

1. **Discover state first.** Run `git status -sb`, `git remote -v`, `gh auth status`, and the relevant `gh repo|issue|pr` query before changing anything.
2. **Authenticate safely.** Never print raw tokens. Prefer `gh auth status`, key presence checks, and masked environment checks.
3. **Choose the narrow lane.** Repo management, issue management, PR lifecycle, review, and CI triage are subsections below; follow only the lane needed.
4. **Make the change.** Use `gh` when it can express the operation; fall back to REST only when the CLI lacks needed fields.
5. **Verify from GitHub.** Re-query the repo/issue/PR/checks URL or status before reporting success.

## Lanes

### Authentication and token safety

Use for login repair, SSH/HTTPS credential problems, token scopes, and `gh` environment handling. Avoid echoing tokens; use masked checks and `gh auth status`.

Full archived package: `references/absorbed/github-auth/SKILL.md`.

### Repository management

Use for clone/create/fork operations, remote repair, repository metadata, branch protection/release-adjacent setup, and repo metrics such as LOC analysis.

Full archived package: `references/absorbed/github-repo-management/SKILL.md`.

### Issues

Use for issue creation, triage, labels, assignment, and issue body templates.

Full archived package: `references/absorbed/github-issues/SKILL.md`.

### Pull request lifecycle

Use for branch preparation, commits, PR body drafting, opening/updating PRs, CI status checks, conventional commits, and merge flow.

Full archived package: `references/absorbed/github-pr-workflow/SKILL.md`.

### Code review

Use for reviewing PR diffs, producing actionable findings, and optionally posting inline comments through `gh` or REST. Keep findings grounded in changed lines and include severity and fix guidance.

Full archived package: `references/absorbed/github-code-review/SKILL.md`.

## Common Pitfalls

1. **Acting before discovering the active repo and remote.** Always verify cwd, branch, and remote target.
2. **Leaking tokens.** Do not print env var values, auth files, or command lines containing secrets.
3. **Assuming a PR exists from branch name alone.** Query `gh pr status` or `gh pr view --json`.
4. **Reporting CI status from stale local output.** Re-query checks immediately before final response.
5. **Using REST when `gh` has a safer high-level command.** Prefer `gh` for auth-aware actions.
6. **Creating a repo name that already exists with different casing or visibility.** GitHub repository names are effectively account-unique; `gh repo create Best-Skills` can fail if `BEST-Skills` already exists. When creation fails with `Name already exists on this account`, immediately run `gh repo view <owner>/<name>` to verify the existing repo, report its URL/visibility, and ask whether to rename, change visibility, or reuse it before creating a different repository.

## Verification Checklist

- [ ] Current repository, branch, and remote were confirmed.
- [ ] Authentication was verified without exposing secrets.
- [ ] The GitHub object touched has a URL or ID in the final evidence.
- [ ] CI/check state was queried when PR or merge readiness mattered.
- [ ] Final response names the exact command/result used for verification.
