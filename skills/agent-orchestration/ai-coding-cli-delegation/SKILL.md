---
name: ai-coding-cli-delegation
description: "Use when delegating coding or review work to external AI coding CLIs such as Claude Code, Codex, OpenCode, or Gemini while Hermes coordinates scope, verification, and handoff."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [ai-coding-cli, delegation, claude-code, codex, opencode, gemini, tmux, verification]
    related_skills: [hermes-agent]
---

# AI Coding CLI Delegation

## Overview

This is the umbrella for running external AI coding agents from Hermes. Treat Claude Code, Codex, OpenCode, Gemini CLI, and similar tools as implementation lanes, not as replacements for Hermes' ownership of the user request. Hermes still defines scope, chooses isolation, checks outputs, runs tests, and reports verified results.

Absorbed original skill packages are preserved under `references/absorbed/<skill-name>/` for complete command details and environment-specific repair notes.

## When to Use

- The user asks to delegate implementation, review, refactoring, or repository work to a coding agent CLI.
- A task benefits from an independent agent process, tmux lane, or model-specific coding assistant.
- You need a long-running autonomous implementation lane while Hermes keeps control of verification.
- You are choosing between Claude Code, Codex, OpenCode, Gemini CLI, or another ACP/CLI worker.

Do not use this for quick mechanical shell/file edits; use Hermes tools directly when delegation adds no value.

## Delegation Contract

1. **Hermes owns the outcome.** The external CLI is a worker. Do not trust self-reported success without inspecting files, diffs, tests, or command output.
2. **Isolate edits.** Prefer git worktrees, disposable branches, or clearly bounded directories for agent work.
3. **Pass a complete brief.** Include goal, constraints, relevant paths, tests to run, and forbidden changes.
4. **Capture outputs.** Use tmux/session logs or command output so the result can be audited.
5. **Verify independently.** Run targeted tests/lints and inspect diffs yourself before finalizing.

## CLI Lanes

### Claude Code

Best for feature implementation, repo-aware refactors, and PR-oriented coding tasks where Claude Code is installed and authenticated. Note Android/PRoot/mobile keyboard pitfalls from the absorbed package.

Full archived package: `references/absorbed/claude-code/SKILL.md`.

### Codex CLI

Best for OpenAI Codex-based implementation lanes, particularly where OAuth is available. Includes Termux/arm64 install repair notes in the absorbed package.

Full archived package: `references/absorbed/codex/SKILL.md`.

### OpenCode

Best for OpenCode-based implementation and review lanes. Check installed binary/version and account for standalone binary upgrade timeout patterns.

Full archived package: `references/absorbed/opencode/SKILL.md`.

## Common Pitfalls

1. **Letting the child agent define scope.** Hermes should write the task contract and guardrails.
2. **Skipping diff review.** Always inspect changed files before accepting a worker's claim.
3. **Running multiple agents in the same tree.** Use worktrees or non-overlapping paths.
4. **Losing logs.** For tmux-based runs, capture panes or redirect logs before killing sessions.
5. **Reporting unverified success.** A child summary is a lead, not proof.

## Verification Checklist

- [ ] Worker command/session and working directory were explicit.
- [ ] Diff or generated files were inspected by Hermes.
- [ ] Relevant tests/lints/builds were run or blockers were reported honestly.
- [ ] Any follow-up handoff includes exact files, commands, and remaining risks.
