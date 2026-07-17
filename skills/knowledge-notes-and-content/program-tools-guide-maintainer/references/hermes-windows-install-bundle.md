# Hermes Agent Windows 11 Install Bundle Pattern

Use this when Mohamed asks for a "ready to use/install" Hermes Agent package for Windows 11 in the regular Android-visible downloads folder.

## Goal

Create a grouped handoff bundle under:

`/sdcard/Download/Program Downloads/`

The practical bundle is ready-to-install, not necessarily fully offline. Say that clearly unless a true offline wheelhouse was built.

## Recommended contents

Folder:

`Hermes-Agent-Windows11/`

Include:

- `Hermes-Setup.exe` from the official Hermes website assets
- `install.ps1` from the official Hermes install endpoint
- `hermes-agent-v<release>-source.zip` from the official GitHub release/tag
- `START-HERE.txt` with very short steps
- `INSTALL-WINDOWS11.md` with fallback PowerShell steps and limitations
- `RUN-CLI-INSTALL.bat` that runs the local `install.ps1` with a pinned tag
- `SHA256SUMS.txt`

Final archive:

`Hermes-Agent-Windows11-ready.zip`

## Official source pattern

- Desktop installer discovery: `https://hermes-agent.nousresearch.com/`
- Windows PowerShell installer: `https://hermes-agent.nousresearch.com/install.ps1`
- Release source zip: `https://github.com/NousResearch/hermes-agent/archive/refs/tags/<tag>.zip`

Use the latest stable release tag unless Mohamed asks for bleeding-edge main.

## Verification checklist

- Downloaded files exist and are non-empty.
- `sha256sum` created for all included files.
- Final zip exists in `/sdcard/Download/Program Downloads/`.
- `unzip -tq` reports no errors.
- `program-tools-guide.md` is updated with:
  - the new archive name under files currently present
  - a short Windows bundle note under `Hermes Agent`
  - a change-log entry

## Pitfall

Do not call this a full offline installer unless you also built a Windows wheelhouse and dependency cache. The official Windows installer may still download Python, Node.js, Git, and Python packages during setup.
