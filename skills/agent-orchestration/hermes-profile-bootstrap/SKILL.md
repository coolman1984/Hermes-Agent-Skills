---
name: hermes-profile-bootstrap
description: Bootstrap, clone, and harden Hermes profiles for a production/experiment pair with safe config, interactive setup handling, and verification. Use when creating a new Hermes profile, cloning it into a lab profile, or wiring profile-specific SOUL/config defaults.
---

# Hermes Profile Bootstrap

## Use this skill
Use this skill when you need a reusable way to create two Hermes profiles: one production profile and one experiment profile, then verify both without guessing model IDs or forcing through interactive setup.

## What changed in practice
A real bootstrap may be interactive. The setup wizard can stop for API keys or other secrets. Do not brute-force past prompts; stop, inspect the profile, and patch the config only after confirming the actual file contents.

## Operating sequence
1. Check the current state first.
2. Create or verify the production profile.
3. Clone it into a lab profile.
4. Run setup/doctor and note missing secrets or web-provider warnings.
5. Patch config only with verified values.
6. Keep SOUL concise and domain-specific.
7. Verify profile, alias, model, gateway, and doctor output.

## Step 1: inspect before editing
Run:
- `hermes profile list`
- `<profile> profile show <profile>`
- `<profile> doctor`

Record:
- path
- alias
- gateway state
- installed skills
- missing env keys
- any interactive setup prompts

## Step 2: create the profile pair
Preferred shape:
- `market` = production
- `marketlab` = experiments

If the production profile already exists, do not recreate it. Clone from the production profile into the lab profile when possible.

## Step 3: keep config conservative
For production:
- `approvals.mode: manual`
- a bounded `timeout`
- `compression.enabled: true`
- `delegation.max_iterations` modest
- default delegation toolsets limited to `web` and `file` unless terminal is truly needed

For lab:
- allow a bit more experimentation
- keep the same provider/model family if you want comparable behavior
- only widen toolsets if the experiment needs them

## Step 4: use real provider model IDs
Do not guess the model identifier.

If using OpenRouter, prefer explicit IDs like:
- `openai/gpt-4.1-mini`
- `openai/gpt-4.1`

If the model ID is unknown, verify it from the provider/model list before patching config.

## Step 5: edit SOUL sparingly
The profile SOUL should be short and operational.

Good SOUL contents:
- role of the profile
- core task loop
- hard constraints
- what not to do
- what the final output must include

Avoid putting all procedures into SOUL. Move repeatable procedures into skills instead.

## Step 6: verify the result
Verify all of the following:
- `profile list` shows both profiles
- `profile show` resolves to the right path and alias
- `doctor` passes or gives only expected warnings
- config file contains the intended delegation model and approvals mode
- SOUL.md exists and matches the intended role

## Common pitfalls
- Interactive setup may stop and ask for secrets; that is normal.
- Doctor may warn about missing web/search keys; that does not mean the profile is broken.
- Cloning does not remove the need to verify config values.
- A bare model name may not work when the provider expects a provider-qualified model ID.
- A profile can look healthy but still fail at runtime if the default provider has no local auth; verify with `hermes auth list` and try a provider that actually has a credential before changing the profile itself.
- Claude Code CLI login does not register Hermes `anthropic` auth. If Mohamed reports Claude models dead in gateway/picker, check `hermes auth status anthropic` and follow `mohamed-claude-codex-control-bridge` → `references/hermes-grok-claude-providers.md` (agent runs sync; do not ask Mohamed to run steps).
- If `anthropic` is logged in but gateway shows "provider failed after retries", inspect `errors.log` for `extra usage` and `hermes auth list anthropic` for exhausted cooldowns; fix with Kilocode Claude models + `fallback_providers`, not profile recreation.
- Overloading `market` with too many delegated toolsets makes production brittle.

## Good final report shape
When done, report:
- profile names
- paths
- alias paths
- gateway status
- config changes made
- doctor warnings left unresolved
- anything the user still needs to fill manually
