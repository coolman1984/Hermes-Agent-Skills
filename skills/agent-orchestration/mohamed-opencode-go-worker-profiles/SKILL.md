---
name: mohamed-opencode-go-worker-profiles
description: Use when Mohamed wants Hermes to run background worker profiles on OpenCode Go models, choose the right model for a task, refresh model choices, or improve the multi-model worker setup.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  tags: [hermes, profiles, opencode-go, multi-agent, model-routing, mohamed]
---

# Mohamed OpenCode Go Worker Profiles

## Purpose

This skill maintains Mohamed's small team of Hermes worker profiles that run on OpenCode Go models while the default Telegram-facing assistant stays on the main GPT profile.

For any serious multi-agent, long-running, or factory-style workflow using these profiles, also load:

`mohamed-agent-loop-os`

That skill defines the permanent loop doctrine: planner, generator, evaluator, file-backed state, contract-before-execution, restart tolerance, and log reading.

Core architecture:

- Mohamed talks to the default profile on Telegram.
- The default profile acts as orchestrator and context owner.
- Worker profiles run in the background for specific tasks.
- The orchestrator reviews worker output before reporting to Mohamed.

Do not expose Mohamed to commands unless he asks. Explain the system in simple operational language.

## Current verified state

Verified on 2026-06-25:

- Default profile: `default` using `gpt-5.5` through `openai-codex`.
- OpenCode Go credential exists in `/root/.hermes/.env` as `OPENCODE_GO_API_KEY`.
- OpenCode Go endpoint verified by calling `/v1/models` and returned these relevant models:
  - `deepseek-v4-pro`
  - `deepseek-v4-flash`
  - `kimi-k2.7-code`
  - `kimi-k2.6`
  - `glm-5.2`
  - `glm-5.1`
  - `minimax-m3`
  - `minimax-m2.7`
  - `qwen3.7-max`
  - `qwen3.7-plus`
- Hermes provider profile for `opencode-go` uses base URL `https://opencode.ai/zen/go/v1` and flat model IDs, not vendor-prefixed IDs.
- These profiles were created and smoke-tested successfully with `hermes -p <profile> chat -Q --max-turns 1 -q ...`:
  - `deepseek-pro` → `deepseek-v4-pro`
  - `deepseek-fast` → `deepseek-v4-flash`
  - `kimi-code` → `kimi-k2.7-code`
  - `glm-go` → `glm-5.2`
  - `minimax-go` → `minimax-m3`
- Full profile smoke test reference: `references/2026-06-25-full-profile-smoke-test.md`.
- Full profile status verified on 2026-06-25: `default`, all five OpenCode Go workers, `operator`, `marketlab`, and `market` work. `market` was fixed by changing its provider from `kilocode` to the working `openai-codex` route used by `marketlab`.

## Worker routing table

| Profile | Model | Best use | Avoid for |
|---|---|---|---|
| `deepseek-pro` | `deepseek-v4-pro` | deep reasoning, critique, plans, hard tradeoffs, second opinions | quick cheap summaries, image-heavy tasks |
| `deepseek-fast` | `deepseek-v4-flash` | fast triage, first-pass summaries, cheap checks, broad scanning | final high-stakes decisions without review |
| `kimi-code` | `kimi-k2.7-code` | code reasoning, long structured summaries, writing, repository analysis | tasks where exact arithmetic or verified facts are not tool-grounded |
| `glm-go` | `glm-5.2` | alternative reasoning, long context analysis, policy/structure review | tasks that need image input |
| `minimax-go` | `minimax-m3` | economical long-context work, multimodal candidate, batch summarization | final strict reasoning without another reviewer |

Optional future candidate:

- `qwen3.7-max` can be added later as a sixth worker for broad general reasoning and long-context comparison, but do not add it unless Mohamed asks or repeated tasks show the current five lack coverage.

## Model observations from live research

Sources used:

- Live OpenCode Go `/v1/models` endpoint.
- `models.dev` provider/model data.
- Hermes local provider tests and provider profile introspection.

Important model facts from `models.dev` as of 2026-06-25:

- `deepseek-v4-pro`: reasoning, tool calling, structured output, very large context; best for hard analysis. Weakness: higher cost and no image input in the OpenCode Go route.
- `deepseek-v4-flash`: reasoning and tool calling with very large context; best for speed and cheap first pass. Weakness: use as triage, not sole final judge for sensitive decisions.
- `kimi-k2.7-code`: newer than `kimi-k2.6`; reasoning, tool calling, structured output, text/image/video input in model metadata; best for code and structured writing. Weakness: code-focused, so review business/investment conclusions separately.
- `glm-5.2`: newer than `glm-5.1`; reasoning, tool calling, structured output, very large context; best as a strong alternative view. Weakness: text-only in the OpenCode Go metadata inspected.
- `minimax-m3`: newer than `minimax-m2.7`; reasoning, tool calling, multimodal metadata, strong long-context economics. Weakness: treat as economical worker, not the final authority on critical reasoning.

## Refresh procedure

When Mohamed asks whether newer versions exist or asks to improve the team:

1. Load this skill and `hermes-agent`.
2. Check Hermes and profiles:

```bash
hermes --version || true
hermes profile list || true
hermes auth list || true
```

3. Query OpenCode Go live model list without printing secrets:

```bash
python3 - <<'PY'
from pathlib import Path
import json, urllib.request
key = None
for line in Path('/root/.hermes/.env').read_text().splitlines():
    if line.startswith('OPENCODE_GO_API_KEY='):
        key = line.split('=', 1)[1].strip().strip('"').strip("'")
print('has_key', bool(key))
if key:
    req = urllib.request.Request('https://opencode.ai/zen/go/v1/models', headers={'Authorization': 'Bearer ' + key, 'User-Agent': 'Hermes-Agent'})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    ids = []
    for item in data.get('data', data if isinstance(data, list) else []):
        ids.append(item.get('id') if isinstance(item, dict) else str(item))
    print(json.dumps([x for x in ids if x], ensure_ascii=False, indent=2))
PY
```

4. Check `models.dev` with a normal user agent if needed:

```bash
python3 - <<'PY'
import urllib.request, json
req = urllib.request.Request('https://models.dev/api.json', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=60) as r:
    data = json.load(r)
print(type(data), len(data) if hasattr(data, '__len__') else '')
PY
```

5. Prefer live OpenCode Go availability over hype. If a model appears on the internet but not in OpenCode Go `/v1/models`, do not assign it to a profile yet.

## Create or update worker profiles

Use cloned profiles, then edit `~/.hermes/profiles/<name>/config.yaml`:

```yaml
model:
  default: deepseek-v4-pro
  provider: opencode-go
```

Remove stale cloned `base_url` and `api_key` under `model` unless intentionally needed. The provider profile supplies the OpenCode Go endpoint.

Recommended profile names and models:

```text
deepseek-pro   deepseek-v4-pro
deepseek-fast  deepseek-v4-flash
kimi-code      kimi-k2.7-code
glm-go         glm-5.2
minimax-go     minimax-m3
```

Each worker `SOUL.md` should say it is a background worker, not Mohamed's main interface, and must return concise verified reports.

## Smoke test

After creation or model changes, run a one-turn test for every affected profile:

```bash
hermes -p deepseek-pro chat -Q --max-turns 1 -q 'اختبار قصير: رد بكلمة جاهز فقط.'
```

Expected: a short answer like `جاهز` and a session id. If a profile fails, do not mark it usable.

When Mohamed asks to test “all profiles”, do not stop at the worker team. Include `default`, worker profiles, and legacy/specialized profiles such as `operator`, `market`, and `marketlab`.

Avoid one huge foreground loop for every profile if some models are slow: it can hit the overall command timeout and hide which profile is stuck. Prefer per-profile tests or start slow profiles as background processes with completion notification, then check `process.wait` / `process.poll`.

If a legacy profile fails because its provider account lacks credits while a sibling profile with the same model works through another provider, compare their `config.yaml` model sections and align the failing profile to the working provider route after a successful retest.

See `references/2026-06-25-full-profile-smoke-test.md` for the full profile test matrix and the `market` profile repair.

## Dispatch patterns

### Important Telegram noise rule

Do not use `terminal(background=true, notify_on_complete=true)` for quick worker tests or short one-shot profile calls when Mohamed is watching Telegram. It sends raw system messages like `[Background process ... finished]` directly into the chat, including warnings and session IDs, which is noisy and not user-friendly.

For quick checks and most worker calls, run the worker in the foreground with a generous timeout, capture the output yourself, then summarize cleanly to Mohamed:

```bash
hermes -p deepseek-pro chat -Q --max-turns 1 -q 'SELF-CONTAINED TASK HERE'
```

For repo-index/review synthesis, `deepseek-fast` works well as a first-pass reviewer when the orchestrator has already generated concrete artifacts. Pass exact input paths and an exact output path, and keep the prompt self-contained:

```bash
hermes -p deepseek-fast chat -Q --max-turns 4 -q 'Read these exact files: ... Write the report to this exact path: ... Verify the file exists and report size.'
```

After the worker finishes, the orchestrator must verify the file itself and sanitize any sensitive setup/config references before delivering to Mohamed.

Use background notification only for genuinely long bounded work where Mohamed explicitly benefits from a raw completion alert. If using background is unavoidable, keep the prompt/output clean and expect Telegram to receive the raw completion block.

For interactive long-running agents, use tmux only when needed. Most tasks should be one-shot workers with self-contained prompts.

## Orchestration rules

- The default GPT profile stays the primary interface with Mohamed.
- For any coding or repo-changing worker task, the orchestrator must load and apply:

`senior-software-engineer`

as the engineering discipline layer, and:

`mohamed-agent-loop-os`

as the planner-generator-evaluator and file-backed state layer.
- Worker prompts must be self-contained because profiles do not share the current chat context automatically.
- Always pass file paths, source text, constraints, and desired output shape.
- Verify external side effects yourself; worker self-reports are not proof.
- Use `deepseek-fast` for first pass, `deepseek-pro` for hard critique, and compare when stakes are high.
- Avoid spawning too many workers for simple tasks; the overhead is not worth it.

## Mohamed-facing explanation

Explain simply:

- The main assistant is the manager.
- Each profile is a specialist worker with one model.
- Mohamed can ask the manager to choose the worker or name the worker directly.
- The worker runs in the background and returns a report.
- The manager checks the report and gives Mohamed the clean result.

## Codebase Memory integration (2026-06-27)

All five worker profiles now carry the `codebase-memory-workflow` skill in their local `skills/software-development/codebase-memory-workflow/` directory.

When dispatching a coding task to any worker:

1. The orchestrator queries the codebase graph first (using `codebase-memory-mcp cli search_graph` or `get_architecture`).
2. The orchestrator includes the graph context (entry points, hotspots, relevant files) in the worker's task prompt.
3. The worker can also query the graph directly since the tool is installed system-wide at `/root/tools/codebase-memory-test/`.
4. The worker must report which files it read and why the graph pointed to them.
5. The orchestrator verifies the worker touched the right files.

To update the skill across all workers after patching the default copy:

```bash
for p in deepseek-fast deepseek-pro kimi-code glm-go minimax-go; do
  src="/root/.hermes/skills/software-development/codebase-memory-workflow"
  dst="/root/.hermes/profiles/$p/skills/software-development/codebase-memory-workflow"
  rm -rf "$dst"
  cp -a "$src" "$dst"
done
```

Reference: `references/2026-06-27-codebase-memory-skill-distribution.md`

## Agent Loop OS distribution (2026-06-30)

All five worker profiles carry local copies of:

- `mohamed-agent-loop-os`
- `senior-software-engineer`
- `persistent-memory-project-governance`

Reason: Mohamed wants worker profiles to execute serious long-running workflows under the same planner-generator-evaluator, senior-engineering discipline, and file-based project governance, not merely receive loose prompts from the default profile.

To refresh these skills across workers after patching the default copies:

```bash
for p in deepseek-fast deepseek-pro kimi-code glm-go minimax-go; do
  mkdir -p "/root/.hermes/profiles/$p/skills/autonomous-ai-agents" "/root/.hermes/profiles/$p/skills/software-development"
  rm -rf "/root/.hermes/profiles/$p/skills/autonomous-ai-agents/mohamed-agent-loop-os"
  cp -a "/root/.hermes/skills/autonomous-ai-agents/mohamed-agent-loop-os" "/root/.hermes/profiles/$p/skills/autonomous-ai-agents/mohamed-agent-loop-os"
  rm -rf "/root/.hermes/profiles/$p/skills/software-development/senior-software-engineer"
  cp -a "/root/.hermes/skills/software-development/senior-software-engineer" "/root/.hermes/profiles/$p/skills/software-development/senior-software-engineer"
  rm -rf "/root/.hermes/profiles/$p/skills/autonomous-ai-agents/persistent-memory-project-governance"
  cp -a "/root/.hermes/skills/autonomous-ai-agents/persistent-memory-project-governance" "/root/.hermes/profiles/$p/skills/autonomous-ai-agents/persistent-memory-project-governance"
done
```

## Maintenance rule

Whenever a profile is changed, a model is upgraded, or a weakness/strength is discovered through real tasks, patch this skill immediately with:

- date
- model/profile affected
- evidence source
- routing change
- smoke-test result
