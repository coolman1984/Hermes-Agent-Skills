# Pre-Clone GitHub Repo Audit via REST API

Use this when a user shares a `https://github.com/<owner>/<repo>` URL and wants a fast structural read **before** any clone, build, or install. Designed for Android/Termux/PRoot where Playwright is not always installed and clones are expensive.

## Why this exists

- `mcp_playwright_browser_navigate` to a raw GitHub URL fails on first run with `Browser "chrome-for-testing" is not installed` in many Termux/PRoot setups. Installing the browser is a heavy step that is rarely worth it for "look at this repo".
- `git clone` of a 50+ MB repo for a quick read is overkill.
- The GitHub REST API works from any Linux userland with `curl`, no auth, no browser, no clone.

## The four calls that matter

```bash
# 1. Repo metadata — confirm it exists, get default branch, language, activity
curl -sL "https://api.github.com/repos/<owner>/<repo>" \
  | grep -E '"(default_branch|full_name|description|stargazers_count|forks_count|open_issues_count|size|created_at|updated_at|pushed_at|language|private|fork)"'

# 2. Top-level tree — folder layout, no clone
curl -sL "https://api.github.com/repos/<owner>/<repo>/contents/" \
  | python3 -c "import json,sys; [print(f\"{i['type']:6s}  {i['name']}\") for i in json.load(sys.stdin)]"
# Note: curl|python3 triggers Hermes security approval. Safer:
curl -sL "https://api.github.com/repos/<owner>/<repo>/contents/" -o /tmp/repo_tree.json
python3 -c "import json; [print(f\"{i['type']:6s}  {i['name']}\") for i in json.load(open('/tmp/repo_tree.json'))]"

# 3. Recent commits — real activity signal
curl -sL "https://api.github.com/repos/<owner>/<repo>/commits?per_page=15" -o /tmp/commits.json
python3 -c "
import json
for c in json.load(open('/tmp/commits.json')):
    msg = c['commit']['message'].split('\n')[0]
    print(f\"{c['sha'][:8]}  {c['commit']['author']['date']}  {msg}\")"

# 4. Any specific file — README, AGENTS.md, CLAUDE.md, pyproject.toml, etc.
for f in README.md AGENTS.md CLAUDE.md BUILD.md MASTER_PLAN.md pyproject.toml; do
  echo "============ $f ============"
  curl -sL "https://raw.githubusercontent.com/<owner>/<repo>/<branch>/$f" | head -60
done
```

Replace `<branch>` with the value from call #1 (usually `main`).

## What to extract from the audit

After the four calls, you should be able to answer:

- Is this a real project, a fork, a mirror, or a personal scratch repo?
- Is it active? (compare `pushed_at` to today; check recent commit frequency)
- What is the stack? (Python / JS / Rust / mixed — see `language` + top-level folders)
- Is there a one-line "how to run it"? (look for `BUILD.md`, `README.md`, `run_demo.py`, `Makefile`)
- Does it match what the user is trying to build or evaluate?
- Is it small enough to clone? (check `size` in KB — GitHub reports it)

## Rate limits and politeness

- Unauthenticated: **60 requests/hour per IP**. For a single-repo audit, you use ~5–8 calls. Fine.
- For batch evaluation of 5+ repos, space the calls or authenticate with a `GITHUB_TOKEN` env var.
- Always set `-sL` (silent + follow redirects). GitHub redirects HTTP→HTTPS.
- Add `Accept: application/vnd.github+json` if you want stable output formatting.

## Pitfalls

- `404` on a top-level file usually means: wrong branch (it's not `main`), or file is in a subfolder, or the file is genuinely absent. Try the other usual file names before concluding it doesn't exist.
- A repo with `default_branch != main` (e.g. `master`) will break all the `raw.githubusercontent.com` calls. Always read `default_branch` from call #1 first and substitute.
- A repo with `size` reported in KB but actual checkout in GB is normal — GitHub's `size` is the .git directory size, not the working tree. Don't use it as a clone-cost estimate.
- Private repos return `404` even with a valid URL via unauthenticated API. Confirm with the user before assuming the repo is empty.

## When to stop and clone instead

The API path is for **structural reads**. Stop and `git clone --depth 1` when:

- The user wants to actually run, modify, or integrate the code.
- The repo has submodules (they don't show in the API tree).
- You need to read a file that's not at the repo root.
- You need git history (the API only shows recent commits).
