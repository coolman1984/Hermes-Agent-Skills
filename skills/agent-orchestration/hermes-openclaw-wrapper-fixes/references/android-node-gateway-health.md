# Android/PRoot OpenClaw runtime mismatch + gateway health timeout

Context captured from a live remediation session.

## Symptoms
- `openclaw --version` fails with Node requirement error when using distro node.
- Global binary exists at `/root/.local/bin/openclaw` but launcher resolves `/usr/bin/node` (v20.x).
- OpenClaw 2026.5.x requires Node >= 22.12.
- `openclaw doctor --fix` ends with: `Gateway service install not supported on android`.
- `openclaw gateway call health` times out, while raw TCP connect to gateway port succeeds.

## Practical interpretation
- Node mismatch is a launcher/runtime selection issue, not package-install failure.
- Android doctor failure can be non-fatal platform limitation (service install path unsupported).
- Health timeout with TCP success indicates app-layer gateway RPC hang/wedge.

## Stabilization pattern
1. Verify actual launcher target:
   - inspect `/root/.local/bin/openclaw` and confirm node path used in shebang/exec path.
2. Ensure Node >=22.12 is what launcher uses (Termux node in this environment).
3. Re-run:
   - `openclaw --version`
   - `openclaw doctor`
4. For gateway hang:
   - restart gateway process cleanly,
   - inspect gateway logs,
   - then re-run `openclaw gateway call health`.

## Notes
- Keep runtime selection explicit; silent PATH drift between distro node and Termux node can regress CLI behavior.
- If repo version and published package version differ, this can be normal (repo ahead of npm release).