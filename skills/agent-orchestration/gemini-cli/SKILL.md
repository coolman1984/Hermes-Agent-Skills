---
name: gemini-cli
description: "Delegate coding and research tasks to Google Gemini CLI, including install, auth, no-prompt automation, MCP, skills, and verification."
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [Coding-Agent, Gemini, Google, MCP, Skills, Automation]
    related_skills: [claude-code, codex, opencode, mohamed-claude-codex-control-bridge]
---

# Gemini CLI

Use Gemini CLI as a local coding and automation agent from Hermes. It supports interactive and headless prompts, Google Search grounding, file operations, shell commands, web fetching, MCP servers, extensions, agent skills, session resume, and output formats.

Official docs source used for this skill:

- `https://github.com/google-gemini/gemini-cli`
- `https://www.geminicli.com/docs/`
- local fetched docs under `/tmp/agent-docs/gemini-*` when available.

## Verified local state

Last verified on 2026-06-13.

- Binary path observed: `/data/data/com.termux/files/usr/bin/gemini`
- Installed package: `@google/gemini-cli`
- Version after update: `0.46.0`
- User settings: `/root/.gemini/settings.json`
- Current auth state: no `GEMINI_API_KEY`, `GOOGLE_API_KEY`, `GOOGLE_GENAI_USE_VERTEXAI`, or `GOOGLE_GENAI_USE_GCA` environment variables were present during verification; headless smoke failed with code 41 asking for an auth method.

## Install and update

```bash
npm install -g --prefix /data/data/com.termux/files/usr @google/gemini-cli@latest
npm config set prefix /data/data/com.termux/files/usr
gemini --version
```

Gemini can also be run via `npx`, but on Mohamed's Android/PRoot setup prefer the Termux npm prefix that owns the existing executable.

## Authentication

Gemini CLI requires one of:

1. Interactive Google sign-in by running `gemini` and selecting **Sign in with Google**.
2. `GEMINI_API_KEY` from Google AI Studio for headless use.
3. Vertex AI / Google Cloud credentials with `GOOGLE_GENAI_USE_VERTEXAI` and project/location environment.
4. Gemini Code Assist / enterprise setup using Google's documented auth flow.

For headless Hermes control, the practical route is a persistent API key or completed cached Google sign-in. Do not read or expose credential files. Check presence only:

```bash
python3 - <<'PY'
import os
for k in ['GEMINI_API_KEY','GOOGLE_API_KEY','GOOGLE_GENAI_USE_VERTEXAI','GOOGLE_GENAI_USE_GCA']:
    print(f'{k}_present={bool(os.environ.get(k))}')
PY
```

## Common commands

```bash
# Interactive REPL
gemini

# Headless one-shot
gemini -p "Summarize this project" --output-format json

# Prompt then continue interactively
gemini -i "Explain this codebase"

# Resume latest session
gemini -r latest

# MCP management
gemini mcp list
gemini mcp add github npx -y @modelcontextprotocol/server-github

# Extensions
gemini extensions list
gemini extensions update --all

# Skills
gemini skills list
gemini skills reload
```

## No-prompt / auto operation

Gemini settings can persist `auto_edit`, but full no-prompt operation requires a CLI flag:

```bash
gemini --approval-mode=yolo --skip-trust -p "TASK" --output-format json
```

A local wrapper was created for Mohamed:

```bash
/root/.local/bin/gemini-auto -p "TASK" --output-format json
```

Important distinction:

- `general.defaultApprovalMode = "auto_edit"` can be stored in `/root/.gemini/settings.json`.
- `yolo` cannot be persisted as `defaultApprovalMode`; docs say it can only be enabled with `--yolo` or `--approval-mode=yolo`.
- `--skip-trust` skips the folder trust prompt for the current run.

Current user settings applied:

```json
{
  "general": {
    "defaultApprovalMode": "auto_edit",
    "enableAutoUpdate": true
  },
  "billing": {
    "overageStrategy": "always"
  },
  "agents": {
    "browser": {
      "confirmSensitiveActions": false,
      "blockFileUploads": false
    }
  },
  "ui": {
    "hideTips": true
  },
  "model": {
    "name": "auto"
  }
}
```

## Model aliases

Docs list aliases:

- `auto`: default; resolves to `gemini-2.5-pro` or preview model when preview features are enabled.
- `pro`: complex reasoning.
- `flash`: fast balanced model.
- `flash-lite`: fastest/simple tasks.

Use explicit model only when the task demands it:

```bash
gemini -m flash -p "Quickly summarize README.md"
gemini -m pro -p "Deeply review this architecture"
```

## Skills and extensions

Gemini skills live under `.gemini/skills/<name>/SKILL.md` for a project, with optional `scripts/`, `references/`, and other resources. This is similar to Hermes/Codex skills: keep `SKILL.md` concise, put deterministic helpers in `scripts/`, and reload with `/skills reload` or `gemini skills reload`.

Extensions can package commands, MCP servers, context files, and tools:

```bash
gemini extensions install <git-or-path>
gemini extensions list
gemini extensions update --all
gemini extensions validate ./my-extension
```

## MCP

Gemini supports MCP servers:

```bash
gemini mcp add <name> <command> --scope user
gemini mcp add <name> <url> --transport http
gemini mcp list
gemini mcp remove <name>
```

Prefer user scope for reusable local tools and workspace scope for repo-specific servers.

## Smoke test

After auth exists:

```bash
cd /tmp/agent-auto-smoke
git init -q
/root/.local/bin/gemini-auto -p 'Reply exactly GEMINI_OK. Do not modify files.' --output-format json
```

Expected success includes a JSON result containing `GEMINI_OK`. If it fails with code 41 and asks for an auth method, installation is fine but auth is not configured.

## Pitfalls

- Headless mode will not work until an auth method is configured.
- Existing cached Google Code Assist individual/free-tier auth may fail with `IneligibleTierError: This client is no longer supported for Gemini Code Assist for individuals`; in that state `gemini-auto` is installed but unusable until Mohamed migrates/authenticates via a supported route such as API key, Vertex, enterprise Code Assist, or the current Google flow.
- `yolo` is not a persistent `defaultApprovalMode`; use the `gemini-auto` wrapper.
- Workspace settings override user settings, but trusted folders may block project-specific config if folder trust is enabled.
- Do not put secrets directly in chat or skill files; use environment variables or Gemini's cached auth flow.
- For Mohamed's PRoot setup, update via the Termux npm prefix, not an arbitrary npm prefix.

## Verification checklist

- `gemini --version`
- `python3 -m json.tool /root/.gemini/settings.json`
- `gemini --help` shows `--approval-mode` and `--output-format`.
- Auth presence check shows at least one valid auth route.
- Headless smoke returns the exact expected token.
