---
name: hermes-honcho-manager-dispatch-fix
description: Fix Hermes/OpenClaw tool outages caused by `handle_function_call() got
  an unexpected keyword argument 'honcho_manager'` via backward-compatible dispatcher
  signature patch and restart verification.
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes-agent, honcho, dispatch, troubleshooting, version-mismatch]
metadata:
  tags:
  - hermes
  - openclaw
  - tools
  - dispatcher
  - honcho_manager
  - hotfix
---

# Hermes honcho_manager Dispatch Fix

Use this skill when most tool calls fail with:
- `handle_function_call() got an unexpected keyword argument 'honcho_manager'`

## Root cause
A wrapper/runtime started passing `honcho_manager` into `handle_function_call`, but the loaded `model_tools.py` signature does not accept it (version mismatch at dispatch boundary).

## Fast diagnosis
1. Reproduce with at least 2 tools (e.g., `terminal`, `web_search`).
2. Confirm same TypeError appears across many tools.
3. Check whether agent-level tools (e.g., todo/session search) may still work; this confirms partial outage at registry-tool dispatch layer.

## Durable fix (preferred)
Patch `handle_function_call` signature to be backward/forward compatible:
- add `honcho_manager=None`
- add `**kwargs`

Implementation target:
- `model_tools.py` in active runtime (and any vendored duplicate used by gateway/wrapper).

Minimal signature pattern:
```python
async def handle_function_call(..., honcho_manager=None, **kwargs):
    # optional: log ignored kwargs
    ...
```
(or sync equivalent `def ...`)

## Optional caller hardening
If callers conditionally pass kwargs, gate with `inspect.signature` and only pass `honcho_manager` when supported. This reduces breakage during rolling updates.

## Restart & recovery sequence
1. Stop existing gateway/agent process(es).
2. Clear stale gateway state lock if present (`gateway_state.json`) when no real PID exists.
3. Restart gateway in known-good environment.
4. Verify logs show healthy startup and no repeated TypeError.

## Verification checklist
- [ ] `terminal` tool works
- [ ] `web_search`/`web_extract` works
- [ ] `skill_view` works
- [ ] No new `honcho_manager` TypeError in logs
- [ ] End-user requested task executes end-to-end after fix

## Operational notes
- During outage, continue triage with any still-working agent-level tools (todo/session recall) while preparing fix.
- Do not trust one successful call; verify at least 3 representative tools.
- After fix, immediately resume blocked user objective (don’t stop at infrastructure-only resolution).

## Common pitfalls
- Patching only one code copy while gateway imports another.
- Restarting without clearing stale lock/state file.
- Declaring success before testing multiple tool paths.
