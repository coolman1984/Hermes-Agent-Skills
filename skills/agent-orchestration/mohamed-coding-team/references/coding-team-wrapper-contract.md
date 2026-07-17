# Coding Team Wrapper Contract Injection

This reference records the durable wrapper pattern for Mohamed's local coding team.

## Purpose

Keep Claude, Codex, and OpenCode aligned with the same senior-engineering contract without copying a large external skill pack into every tool.

## Central contract file

```text
/root/.hermes/coding-team/SENIOR_ENGINEERING.md
```

This file contains the shared rules:

- inspect context first
- preserve scope
- work in small verified slices
- treat tests/builds as proof
- review correctness, readability, architecture, security, and performance
- do not claim success without evidence
- each agent stays in its role

## Wrapper injection pattern

Each wrapper reads the central contract, appends a role-specific block, then appends the user task.

Expected wrappers:

```text
/root/.local/bin/claude-architect
/root/.local/bin/codex-supervisor
/root/.local/bin/opencode-worker
/root/.local/bin/opencode-worker-cheap
/root/.local/bin/opencode-worker-hard
```

Role split:

- `claude-architect`: consulting architect; architecture, phases, risks, acceptance criteria, test strategy; no bulk implementation by default.
- `codex-supervisor`: supervising execution engineer; turns architecture into tasks, reviews diffs, writes repair instructions.
- `opencode-worker`: scoped implementation worker; edits code/tests/docs only for the assigned task.
- `opencode-worker-cheap`: low-cost worker for simple or repetitive tasks.
- `opencode-worker-hard`: stronger worker for complex implementation, still without major architecture authority.

## Verification pattern without spending model calls

Use temporary fake binaries earlier in `PATH` to intercept wrapper invocations and assert prompt injection. Example shape:

```bash
TMP=$(mktemp -d)
cat > "$TMP/opencode" <<'SH'
#!/usr/bin/env bash
printf '%s\n' "$@"
SH
chmod +x "$TMP/opencode"
PATH="$TMP:$PATH" /root/.local/bin/opencode-worker 'Implement button state'
```

Check the captured output includes:

- `Senior Engineering Contract`
- `Current role`
- the role name
- `Task`
- the original task text

Also run:

```bash
bash -n /root/.local/bin/claude-architect
bash -n /root/.local/bin/codex-supervisor
bash -n /root/.local/bin/opencode-worker
bash -n /root/.local/bin/opencode-worker-cheap
bash -n /root/.local/bin/opencode-worker-hard
```

## Pitfalls

- Do not copy a whole external skills repository into each wrapper. It creates prompt bloat and conflicting instructions.
- Do not install external hooks blindly. Keep hooks/tool-specific automation separate from the shared engineering contract.
- Back up wrappers before editing them.
- Do not test wrapper changes by firing expensive model calls when shell interception can verify the prompt construction.
