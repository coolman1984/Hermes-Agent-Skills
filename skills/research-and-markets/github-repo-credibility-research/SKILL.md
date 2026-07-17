---
name: github-repo-credibility-research
description: Vet a GitHub/open-source project for real quality vs hype by triangulating README claims, code footprint, repo activity, issues, third-party coverage, and social sentiment.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    category: research
    tags: [github, open-source, research, credibility, code-review, social-signal]
---

# GitHub Repo Credibility Research

Use this skill when the user asks whether an open-source project is actually strong, overhyped, or weak, especially if the project has a flashy README, a trending badge, or aggressive social-media promotion.

## Goal
Separate marketing claims from evidence by cross-checking:
- repository metadata
- code footprint
- README claims vs actual source
- issue tracker signal
- third-party coverage
- X/Twitter sentiment
- Reddit sentiment when available

Return a verdict that is evidence-based, not vibes-based.

## When to Use
- User shares a GitHub repo or screenshot and asks whether it is genuinely good
- User asks if a repo is “real” or “just hype”
- User wants a credibility check before adopting a project
- User wants quick signals from X/Reddit plus a code-based sanity check

## Recommended Workflow

### 1) Identify the exact repo
- Extract owner/repo from the README, screenshot, or page title.
- Confirm with GitHub search or GitHub API.
- Do not rely on third-party mirrors alone.

### 2) Verify basic repo facts
Use GitHub API or browser-backed page inspection to collect:
- stars
- forks
- open issues
- default branch
- language
- recent update time
- license
- whether it is active

If the repo is trending, note that trending is a visibility signal, not a quality signal.

### 3) Test README claims against the codebase
Use a local clone or repo tree inspection to verify claims such as:
- “3K lines of code”
- “minimal core”
- “self-evolving”
- “supports X platforms”
- “single loop” or “9 tools”

Useful checks:
- line counts for core files vs total files
- whether the claimed core size is plausible
- whether the claimed features exist in source
- whether the README overstates autonomy or benchmark results

If the repo is small enough, clone it and count the lines in the core files separately from assets/tests/docs.

### 4) Read the repo directly if possible
Use Camoufox when browser rendering is needed or when the page is dynamic.
- Verify the GitHub README content
- Inspect third-party pages like DeepWiki or trend/stat pages only as secondary evidence
- Prefer source-of-truth repo content over summaries

If Camoufox is unavailable, use GitHub API + terminal cloning instead.

### 5) Gather social signal from X/Twitter
Use the fastest reliable method available:
1. Search web / DuckDuckGo for `site:x.com <repo name>` and the repo owner.
2. Pull relevant tweet IDs with a mirror such as FXTwitter/VXTwitter when direct extraction is hard.
3. Focus on posts that:
   - describe hands-on use
   - mention bugs or limitations
   - compare against alternatives
   - include specific technical criticism

Avoid over-weighting reposts, hype threads, or pure announcement tweets.

Good X signal examples:
- user reports of actual installation/use
- bug complaints
- comparisons against other tools
- comments about reliability, token use, speed, or UX

### 6) Gather Reddit signal, but expect blocks
- Search the web for Reddit threads mentioning the repo.
- Try Reddit only if accessible; many environments block it.
- If Reddit is blocked, say so clearly.
- If you can only reach snippets or blocked pages, do not invent sentiment.

### 7) Check issue tracker signal
Open GitHub issues and look for:
- repeated crash reports
- installation problems
- security concerns
- fake-site or scam concerns
- unanswered questions about claim validity

One or two issues are not fatal, but they reveal maturity and rough edges.

### 8) Look for third-party coverage carefully
Use third-party blogs, DeepWiki, trend sites, and news as supporting evidence only.
Important distinction:
- high-traffic reposts = social proof
- independent technical coverage = stronger signal
- SEO blog spam = weak signal

### 9) Synthesize into a verdict
Use a three-part verdict:
- **Strong**: claims are plausible, code exists, project is active, and external evidence is mostly supportive
- **Hype but real**: project exists and does something useful, but marketing outpaces maturity
- **Weak**: claims are not supported, repo is stale/broken, or evidence is mostly promotional

Include:
- what seems solid
- what seems overstated
- what is still uncertain
- whether the project is ready for adoption

## Good Evidence Hierarchy
Highest trust:
1. repository source code
2. GitHub issues / commits / release history
3. official docs / README
4. reproducible local run or smoke test
5. independent technical writeups
6. social posts with hands-on use
7. reposts / trending lists / SEO summaries

## Common Pitfalls
- Do not treat stars as proof of quality.
- Do not treat trending badges as proof of technical merit.
- Do not let reposts on X dominate the conclusion.
- Do not assume Reddit is representative if you only found one thread.
- Do not confuse a polished README with a reliable production system.
- Do not ignore open issues that directly challenge the project’s claims.

## Useful Checks
- Repo metadata via GitHub API
- `git clone` + line counts for core files
- `search_files` for feature names claimed in README
- `read_file` or Camoufox extraction for README and docs
- X mirrors (FXTwitter/VXTwitter) for specific tweet text
- DuckDuckGo HTML search for cross-site discovery
- GitHub issues API for bug/concern sampling

## Output Format
Return a compact research memo:

- **Research objective**
- **Key findings**
- **Important tradeoffs**
- **Risks or unknowns**
- **Recommended conclusion**

Optionally include a short table:

| Signal | What it suggests |
|---|---|
| README/code match | ... |
| Repo activity | ... |
| X sentiment | ... |
| Reddit sentiment | ... |
| Issue tracker | ... |
| Third-party coverage | ... |

## Example Verdict Language
- “Real project, but the marketing is ahead of the maturity.”
- “Technically interesting and active, but not yet production-hardened.”
- “Mostly hype: the repo exists, but the evidence for the big claims is thin.”
- “Strong open-source foundation with credible external corroboration.”
