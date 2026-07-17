# Hermes Grok + Claude provider wiring (Mohamed machine)

Last verified: 2026-07-09.

## Mohamed rule

When Mohamed asks to configure or fix Hermes models/providers, **execute everything yourself** (config, auth, tests, `.env` updates, fallback chain). Do **not** tell Mohamed to run terminal commands or "try these steps." Report what changed and verification only.

## Grok inside Hermes (`xai-oauth`)

- OAuth login: `hermes auth add xai-oauth --no-browser` → user approves device URL/code.
- Persistent default:
  - `hermes config set model.provider xai-oauth`
  - `hermes config set model.default grok-4.5` (or the model Mohamed wants)
- **Name mismatch:** OAuth catalog/UI may show internal id `grok-build-0.1` while config id `grok-4.5` still works. Treat both as Grok OAuth builds; prefer the id that passes `hermes chat --provider xai-oauth --model <id> -q ...`.
- `hermes model --refresh` needs an **interactive TTY**; it fails from piped/non-interactive shells. Do not rely on it from gateway tool sessions.

## Claude inside Hermes (`anthropic`)

### Symptom A — logged out / empty env

- Mohamed: "Claude models not working" in Hermes/Telegram picker.
- `hermes auth status anthropic` → `logged out`
- `~/.hermes/.env` may have **empty** `ANTHROPIC_API_KEY` / `ANTHROPIC_TOKEN` lines even when Claude Code CLI is logged in.

Claude Code login (`claude auth status` → loggedIn) does **not** automatically register Hermes `anthropic` auth until the pool is seeded.

**Fix (agent-run, no secret echo):**

1. Confirm Claude Code OAuth is valid: `claude auth status --text` → `loggedIn: true`; token in `~/.claude/.credentials.json` → `claudeAiOauth` with `expiresAt` not expired.
2. Write the access token into `~/.hermes/.env` as **OAuth env vars** (not empty placeholders):
   - `CLAUDE_CODE_OAUTH_TOKEN=<token>`
   - `ANTHROPIC_TOKEN=<token>` (same access token; must be OAuth-shaped: `sk-ant-oat*`, `eyJ*`, or `cc-*`)
3. Reload pool: `hermes auth list anthropic` should show `claude_code` (file bridge) and/or `env:CLAUDE_CODE_OAUTH_TOKEN` with **auth_type oauth**, not only empty keys.
4. Smoke (see verification below).

**Never** register Claude Code OAuth as `hermes auth add anthropic --type api-key`. Manual `api_key` entries sort **before** `claude_code` in the Anthropic pool and can force the wrong transport (treating OAuth as `x-api-key`). If already added, remove: `hermes auth remove anthropic <label>`.

### Symptom B — `/model` saves Claude but Telegram says "provider failed after retries"

Auth can be **logged in** while API still rejects every call.

1. Read `/root/.hermes/logs/errors.log` (tail). Look for:
   - `provider=anthropic` + `You're out of extra usage` (HTTP 400)
2. Run `hermes auth list anthropic`. If every entry shows `exhausted` + `invalid_request_error (400)` with a cooldown timer, this is **Claude Pro extra-usage quota** on the native Anthropic API path—not a broken Telegram gateway and not "not logged in."
3. Claude Code CLI may still work (different client path). Do not tell Mohamed "Claude is broken everywhere."

**Working route on this machine when Anthropic pool is exhausted:** provider **`kilocode`** with models:

```text
anthropic/claude-opus-4-8
anthropic/claude-sonnet-4-6
```

Smoke:

```bash
hermes chat --provider kilocode --model anthropic/claude-opus-4-8 -q 'Reply exactly: OK' --toolsets '' --quiet
```

**Fallback chain** (edit `~/.hermes/config.yaml` when Mohamed wants Claude via `/model` on `anthropic` but quota is hit—gateway should fall through automatically):

```yaml
fallback_providers:
  - provider: kilocode
    model: anthropic/claude-opus-4-8
  - provider: kilocode
    model: anthropic/claude-sonnet-4-6
  - provider: xai-oauth
    model: grok-composer-2.5-fast
  - provider: xai-oauth
    model: grok-4.5
```

Keep primary default on Grok unless Mohamed explicitly wants Claude as default.

**If Mohamed needs native `anthropic` again:** wait for pool cooldown (`hermes auth list anthropic`) or add extra usage at `claude.ai/settings/usage`. `hermes auth reset anthropic` only clears exhaustion markers—it does not bypass Anthropic billing limits.

### Verification (always check logs, not only CLI text)

```bash
hermes auth status anthropic
hermes auth list anthropic
hermes chat --provider anthropic --model claude-sonnet-4-6 -q 'Reply exactly: OK' --toolsets '' --quiet
```

If CLI prints `OK` but `errors.log` still shows `extra usage` for that session id, treat Anthropic as **failed** and use Kilocode fallback.

### Gateway note

- A Telegram/gateway session **cannot** restart itself (`pkill hermes gateway` blocked from inside gateway).
- Config/fallback edits apply without restart; auth pool reloads on subsequent turns.

## Never

- Read or paste `~/.hermes/auth.json`, full `.env`, or `~/.claude/.credentials.json` into chat.
- Tell Mohamed to manually edit secrets.
- Add Claude OAuth tokens as manual `api_key` credentials.