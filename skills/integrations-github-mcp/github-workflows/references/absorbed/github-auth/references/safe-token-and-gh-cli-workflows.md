# Safe GitHub Token and gh CLI Workflows

Use this reference when Mohamed wants to grant GitHub access in a headless Hermes/terminal environment.

## Goal

Authenticate GitHub access without embedding tokens in git remotes, shell command text, or user-visible logs.

## Preferred sequence

1. Install GitHub CLI if missing:

```bash
apt-get update
apt-get install -y gh
```

2. Authenticate using stdin, not by placing the token inside a command argument:

```bash
printf '%s' "$GITHUB_TOKEN" | gh auth login --with-token
gh auth setup-git
gh auth status
```

3. Verify repository access with `gh` or `git`, then clone/push via normal HTTPS remotes:

```bash
gh repo clone OWNER/REPO /path/to/repo -- --branch BRANCH --single-branch
git remote get-url origin
```

The remote should stay clean:

```text
https://github.com/OWNER/REPO.git
```

not:

```text
https://TOKEN@github.com/OWNER/REPO.git
```

## If the token is already stored by gh

When `gh auth status` succeeds but another tool expects `GITHUB_TOKEN`, load the token from `gh` without printing it:

```bash
export GITHUB_TOKEN="$(gh auth token)"
```

Then use API or publishing tools that read `$GITHUB_TOKEN`. Do not echo the value. If verification is needed, print only boolean/length/prefix-redacted metadata.

## Safety notes

- Treat classic `ghp_...` tokens as sensitive even if the user pasted them in chat.
- Prefer fine-grained tokens limited to the target repo.
- Avoid storing credentials in git remote URLs.
- After the work is done, tell Mohamed if the token was broader than needed and recommend revoking/replacing it.
- Do not record token values in memory, skills, task logs, or notes.

## Useful verification

```bash
gh auth status
gh api user --jq .login
git config --global credential.helper
git remote -v
```

If making commits for Mohamed, set a safe no-reply identity when GitHub returns no public email:

```bash
git config --global user.name "coolman1984"
git config --global user.email "54982309+coolman1984@users.noreply.github.com"
```
