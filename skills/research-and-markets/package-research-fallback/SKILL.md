---
name: package-research-fallback
description: Research Python packages and GitHub repos reliably when normal web tools fail or return blocked/low-signal responses. Use PyPI JSON, raw GitHub files, and direct HTTP fallbacks to verify package metadata, README claims, install instructions, and feature support.
---

# Package / Repo Research Fallback

Use this skill when researching a Python package or GitHub repo and the standard search/extract tools are blocked, flaky, or too vague.

## When to use
- Verifying whether a package really exists on PyPI
- Checking install commands, version, Python support, or license
- Inspecting README claims like memory, cron, skills, CLI, or shell support
- Comparing whether a repo is genuinely bash-free or only bash-disabled by config
- When web search/extract returns errors, wrappers, or generic summaries

## Core approach
1. Start with the package registry JSON if available.
   - PyPI: `https://pypi.org/pypi/<package>/json`
2. Pull the repo README or key files directly from raw GitHub URLs.
   - `https://raw.githubusercontent.com/<org>/<repo>/<branch>/README.md`
   - `pyproject.toml`, `package.json`, or similar can also be fetched raw.
3. If normal web tools fail, use direct HTTP in Python/terminal.
   - Prefer `urllib.request` or `requests` with a browser-like User-Agent.
4. Search the fetched text for targeted keywords and config flags.
   - Examples: `bash`, `shell`, `sandbox`, `cron`, `skill`, `memory`, `mcp`, `telegram`, `whatsapp`, `cli`
5. If the repo is large, inspect only the most relevant line ranges around matches.
6. Synthesize what is confirmed vs. what is only implied by the docs.

## Reliable evidence hierarchy
Prefer this order:
1. PyPI JSON / package metadata
2. Raw README / raw config files from the repo
3. Release notes / changelog / tagged docs
4. Search snippets
5. LLM-generated summaries

## Useful patterns
- If `web_search` or `web_extract` returns HTTP 432 or generic wrappers, switch to direct HTTP.
- Use DuckDuckGo HTML only as a backup search surface when needed.
- For feature verification, search the README for exact config flags and defaults.
- If a tool is claimed to be disabled by config, look for the actual flag name and default value.

## Pitfalls
- Do not assume a package is safe or bash-free just because the README mentions sandboxing.
- Do not trust install snippets without checking the current package metadata.
- README news/changelog sections may be long and noisy; search for the specific feature flags instead.
- Search snippets can be outdated or misleading; confirm in raw source whenever possible.

## Output format
When reporting back, separate:
- Confirmed facts
- Likely inferences
- Unknowns / remaining risks

## Verification checklist
Before finishing:
- Confirm package existence and current version
- Confirm install path(s)
- Confirm key feature flags or disabling knobs
- Confirm whether the docs actually support the claim you care about
- State clearly if a capability is configurable rather than absent by design