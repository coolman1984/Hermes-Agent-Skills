# Senior Engineering Contract Injection for Mohamed's Coding Team

## Class of work

Use this when Mohamed wants the whole coding team — Hermes, Claude Architect, Codex Supervisor, and OpenCode workers — to behave like senior software engineers instead of generic coding agents.

## Durable pattern

Do not blindly copy an external skill pack into every agent. Keep broad external packs as references, extract the shared engineering contract, then inject a compact role-specific version into each worker wrapper.

## Current local implementation

Central contract file:

```text
/root/.hermes/coding-team/SENIOR_ENGINEERING.md
```

Wrappers that should receive the contract:

```text
/root/.local/bin/claude-architect
/root/.local/bin/codex-supervisor
/root/.local/bin/opencode-worker
/root/.local/bin/opencode-worker-cheap
/root/.local/bin/opencode-worker-hard
```

Backup location pattern before wrapper edits:

```text
/root/.hermes/coding-team/backups/YYYYMMDD-HHMMSS/
```

## Role-specific injection principle

- Claude Architect: architecture, phases, risks, affected files, acceptance criteria, test strategy; no bulk coding by default.
- Codex Supervisor: implementation supervision, task breakdown, diff review, exact repair instructions; avoids bulk implementation unless needed.
- OpenCode Worker: scoped implementation only, follows existing patterns, verifies, reports changed files and risks; no large architecture decisions alone.
- Cheap Worker: simple, repetitive, or low-risk broad edits.
- Hard Worker: complex code paths, still scoped and verified.

## Safe verification without spending model tokens

Before saying wrapper injection works, test with temporary fake binaries earlier in PATH rather than calling the real models:

```bash
TMP=$(mktemp -d)
cat > "$TMP/opencode" <<'SH'
#!/usr/bin/env bash
printf '%s\n' "$@"
SH
chmod +x "$TMP/opencode"
PATH="$TMP:$PATH" /root/.local/bin/opencode-worker 'Implement button state'
```

Check that output contains:

- `Senior Engineering Contract`
- `Current role`
- the expected role name
- the original task text
- the expected model flags for that wrapper

Also run:

```bash
bash -n /root/.local/bin/claude-architect
bash -n /root/.local/bin/codex-supervisor
bash -n /root/.local/bin/opencode-worker
bash -n /root/.local/bin/opencode-worker-cheap
bash -n /root/.local/bin/opencode-worker-hard
```

## Pitfalls

- Do not install external hooks or command integrations from broad skill packs unless explicitly vetted; they can alter agent behavior globally.
- Do not put the full external skill repository into every prompt; it adds noise and conflicting instructions.
- Do not rely on a worker's self-report that it followed the contract; Hermes still verifies diffs, tests, and build output directly.
- Do not let role injection erase the user's task. Always append the original task after the contract and role section.
