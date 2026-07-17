---
name: termux-open-source-tool-triage
description: Rapidly evaluate multiple open-source AI/tool repos on Android Termux, detect platform blockers early, and produce an execution plan (run now vs move to Linux x86_64).
version: 1.0.0
author: Hermes Agent
license: MIT
---

# Termux Open-Source Tool Triage

Use this when a user shares a list/thread of promising repos and asks to "install now" or "benefit immediately" on an Android/Termux environment.

## Goal
Get to a reliable decision fast:
1) what can run now,
2) what is blocked by platform/runtime constraints,
3) what should be moved to a Linux x86_64 host.

## Workflow

1. Resolve canonical repos first
- Use web search to map project names to official GitHub URLs.
- Prefer owner/repo links directly; avoid mirror/fork confusion.

2. **Pre-clone GitHub audit via REST API (no browser, no clone required)**
   Before running `git clone`, get a fast structural read of any public repo with just `curl` + `api.github.com`. This is the **first move** in PRoot/Termux where Playwright/Chrome-for-Testing may not be installed and a full clone is expensive.
   - Repo metadata: `curl -sL https://api.github.com/repos/<owner>/<repo>` → confirm `default_branch`, `language`, `pushed_at`, `size`, `stargazers_count`, `description`.
   - Top-level tree: `curl -sL https://api.github.com/repos/<owner>/<repo>/contents/` → see folder layout without cloning.
   - Recent commits: `curl -sL "https://api.github.com/repos/<owner>/<repo>/commits?per_page=15"` → real activity signal.
   - Any file content: `curl -sL https://raw.githubusercontent.com/<owner>/<repo>/main/<path>` → README, AGENTS.md, CLAUDE.md, pyproject.toml, etc.
   - **Privacy check first:** before doing this for a third-party repo, confirm the user wants the audit (it exposes the user as a GitHub anonymous API client). For personal repos on the user's own account, skip the question.
   - **Rate limit awareness:** unauthenticated calls are 60/hour per IP. Batch all calls for one repo into a single `for f in ... ; do curl ... ; done` loop so the budget is consumed once.
   - Pitfall: `curl | python3` requires user approval for security scanning. Prefer `curl -sL URL | head -N` for raw reads, or write the JSON to a temp file first, then parse with Python.

3. Create a clean lab directory and shallow-clone
- Use a dedicated workspace (example: `~/workspace/tools-lab`).
- `git clone --depth 1` each repo.
- Retry failed clones with `--filter=blob:none` for large repos.

3. Collect quick viability signals
- Read README for install/run commands.
- Detect stack markers:
  - JS: `package.json`, `pnpm-workspace.yaml`
  - Python: `pyproject.toml`, `requirements.txt`
  - Container: `Dockerfile`, `docker-compose.yml`
- Pull repo metadata via GitHub API (stars, language, updated_at) for prioritization.

4. Run minimal smoke tests (safe, non-destructive)
- JS repos: run install only first (`npm install` or workspace install).
- Python repos: create venv and test import path before full model/runtime setup.
- Avoid long-running services unless needed for verification.

5. Detect known Termux/Android blockers early
- Browser tooling may fail entirely on `android-arm64` or PRoot if it depends on a real desktop browser/runtime.
- For browser projects, verify these signals first:
  - official docs mention Linux-only build/runtime constraints
  - release assets include `arm64` or `aarch64` binaries
  - Playwright/Firefox wrappers can run headless without GUI dependencies
  - Xvfb / virtual display is required for headless Linux use
- Native Node addons (`*.node`, e.g. rollup binaries) may fail `dlopen` due linker namespace restrictions.
- Monorepos may require `pnpm` explicitly even if `npm install` succeeds.
- ML packages may fail due strict Python/JAX wheel compatibility on Android.

6. Produce action matrix
For each repo, output one of:
- `Ready now on Termux`
- `Partially usable (code/read workflow only)`
- `Move to Linux x86_64 for runtime`

Include exact blocker + next best environment.

7. For anti-detect / automation browsers specifically
- Check whether the project is a custom browser build, a Playwright wrapper, or an MCP server around a browser.
- Prefer the official docs over blog posts for install steps and platform support.
- Treat active-development / not-production-ready warnings as a risk flag, not a blocker by itself.
- If the project has a Python wrapper, verify whether the wrapper works without building the browser from source.
- If the repo offers Docker builds, treat Docker as the preferred escape hatch on non-Linux or constrained environments when available.

## Reference
## Practical commands

```bash
# pre-clone audit (no browser, no clone) — see references/github-api-preread.md
curl -sL "https://api.github.com/repos/<owner>/<repo>" -o /tmp/repo.json
curl -sL "https://api.github.com/repos/<owner>/<repo>/contents/" -o /tmp/tree.json
curl -sL "https://raw.githubusercontent.com/<owner>/<repo>/main/README.md" | head -40

# clone set
mkdir -p ~/workspace/tools-lab && cd ~/workspace/tools-lab

# install pnpm when monorepo scripts require it
npm install -g pnpm

# environment snapshot
node -v
npm -v
pnpm -v || true
python --version
```

## Common pitfalls
- Treating `npm install` success as runtime success (native addon load may still fail at build/run).
- Trying to fully run heavy monorepos before confirming package manager + workspace assumptions.
- Forcing TimesFM/JAX setup on incompatible Python/arch instead of pivoting quickly to x86_64.
- **Reaching for `mcp_playwright_browser_navigate` on a bare GitHub URL in PRoot/Termux** — Playwright needs Chrome-for-Testing installed, which fails on first run with "Browser chrome-for-testing is not installed". For a public repo, the curl+api.github.com path above is faster, lighter, and works without any browser install.
- **Running `search_files` with `pattern=^.*\.md$` or other regex-heavy anchors on a target=files query** — it returns 0 results even when matching files exist. Use a plain glob pattern (e.g. `*.md` or a known prefix) with `target=files` instead, or use `target=content` with a known token.
- Treating a third-party GitHub repo as a no-cost read — the audit itself is cheap, but if you then summarize and recommend action, the user is committing attention and possibly code integration. Always end with a clear next-step menu, not just a wall of facts.

## Verification checklist
- [ ] All requested repos cloned (or pre-clone audit completed via API)
- [ ] README install path identified per repo
- [ ] At least one smoke test attempted per primary stack
- [ ] Blockers tied to concrete error output
- [ ] Final recommendation split into "run now" vs "migrate environment"

## Output style
Keep it execution-oriented:
- what was installed,
- what ran,
- what failed and why,
- exactly what to do next.