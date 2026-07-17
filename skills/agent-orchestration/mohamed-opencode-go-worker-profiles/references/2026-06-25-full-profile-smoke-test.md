# Full Profile Smoke Test — 2026-06-25

## Context

Mohamed asked to test all Hermes profiles, not only the new OpenCode Go worker team.

Profiles present:

- `default` → `gpt-5.5`
- `deepseek-pro` → `deepseek-v4-pro`
- `deepseek-fast` → `deepseek-v4-flash`
- `kimi-code` → `kimi-k2.7-code`
- `glm-go` → `glm-5.2`
- `minimax-go` → `minimax-m3`
- `operator` → `gpt-5.4-mini`
- `market` → `gpt-5.4-mini`
- `marketlab` → `gpt-5.4-mini`

## Useful testing pattern

A single foreground loop over many profiles can hit global timeout before slow profiles finish. Prefer either:

1. Quick foreground test per profile with a generous per-command timeout; or
2. Start slow profiles as background processes with `notify_on_complete=true`, then inspect with `process.wait` / `process.poll`.

Simple smoke prompt:

```bash
hermes -p <profile> chat -Q --max-turns 1 -q 'اختبار تشغيل للبروفايل <profile>: رد بكلمة جاهز فقط.'
```

Expected result:

- exit code `0`
- short reply like `جاهز`
- `session_id` printed

## Result

Working after final verification:

- `default`
- `deepseek-pro`
- `deepseek-fast`
- `kimi-code`
- `glm-go`
- `minimax-go`
- `operator`
- `marketlab`
- `market`

## Fix discovered

`market` initially failed with:

```text
HTTP 402: Add credits to continue, or switch to a free model
```

Cause: profile config used provider `kilocode` while `marketlab` used working provider `openai-codex`.

Fix applied:

```yaml
model:
  default: gpt-5.4-mini
  provider: openai-codex
  base_url: https://chatgpt.com/backend-api/codex
```

After the change, `market` smoke test returned `جاهز` with exit code `0`.

## Durable lesson

When testing the worker team, separate two questions:

1. Are OpenCode Go worker profiles healthy?
2. Are legacy/specialized profiles healthy?

If a legacy profile fails because its provider account lacks credits but a sibling profile with the same model works through another provider, treat it as a profile-routing/config issue and align it with the working provider after verifying the sibling config.
