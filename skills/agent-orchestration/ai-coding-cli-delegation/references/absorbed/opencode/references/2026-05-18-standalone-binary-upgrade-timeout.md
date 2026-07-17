# 2026-05-18 OpenCode self-upgrade timeout that still completed

## Context
OpenCode was installed as a standalone binary at `/root/.opencode/bin/opencode` on Linux aarch64. It was not installed through global npm or Homebrew.

## Baseline
- `which -a opencode` → `/root/.opencode/bin/opencode`
- `opencode --version` → `1.3.0`
- `npm view opencode-ai version` → `1.15.0`
- `opencode --help` showed an `opencode upgrade [target]` command.

## Update path
Run:
```bash
opencode upgrade
```
The CLI detected method `curl` and started `1.3.0 → 1.15.0`.

## Pitfall
The command timed out in the agent terminal after 300s with `Canceled`, but a detached parent shell/curl process continued downloading:
- `curl -# -L -o /tmp/opencode_install_.../opencode-linux-arm64.tar.gz ...`

The download size was close to the expected release asset size. After waiting, the curl/bash exited and the binary was successfully replaced.

## Verification pattern
If `opencode upgrade` times out:
1. Do not immediately rerun or delete temp files.
2. Check for live upgrade processes:
   ```bash
   ps -efww | grep -E 'opencode|curl.*opencode' | grep -v grep || true
   ```
3. Check the binary version and metadata:
   ```bash
   opencode --version
   stat -c '%n size=%s modified=%y' /root/.opencode/bin/opencode
   file /root/.opencode/bin/opencode
   ```
4. Compare latest:
   ```bash
   npm view opencode-ai version
   ```
5. Confirm auth still loads:
   ```bash
   opencode auth list
   ```

## Successful final state
- `opencode --version` → `1.15.0`
- `npm view opencode-ai version` → `1.15.0`
- `opencode auth list` showed configured credentials.

## Process caution
A separate interactive `opencode` TUI process may be running. Do not kill it just to update the binary unless the user explicitly asks; new launches use the updated binary.
