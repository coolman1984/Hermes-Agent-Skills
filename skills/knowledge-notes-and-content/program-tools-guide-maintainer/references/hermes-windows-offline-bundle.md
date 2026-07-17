# Hermes Agent Windows 11 Fully Offline Bundle Pattern

Use this reference when Mohamed asks for Hermes Agent to be installed on a Windows PC with no internet.

## Trigger

Mohamed asks for a Windows 11 Hermes Agent package and then clarifies that the target PC has no internet.

## Key distinction

There are two different deliverables:

1. Ready-to-install online bundle
   - Official `Hermes-Setup.exe`
   - Official `install.ps1`
   - Source snapshot
   - Instructions and checksums
   - Still downloads dependencies during install

2. Fully offline bundle
   - Python installer for Windows x64
   - Node.js Windows x64 zip
   - PortableGit Windows x64 archive
   - Hermes Agent wheel
   - Windows Python wheelhouse for Python 3.11 x64
   - Offline PowerShell installer
   - Source snapshot
   - Checksums

Do not call the first one fully offline.

## Practical build pattern

Canonical destination:

`/sdcard/Download/Program Downloads/Hermes-Agent-Windows11-OFFLINE/`

Final archive:

`/sdcard/Download/Program Downloads/Hermes-Agent-Windows11-FULLY-OFFLINE.zip`

Recommended contents:

- `INSTALL-OFFLINE.ps1`
- `START-HERE-OFFLINE.txt`
- `OFFLINE-INSTALL-WINDOWS11.md`
- `requirements-windows-offline.txt`
- `SHA256SUMS.txt`
- `installers/python-3.11.x-amd64.exe`
- `installers/node-v22.x-win-x64.zip`
- `installers/PortableGit-*-64-bit.7z.exe`
- `wheelhouse-py311-win_amd64/*.whl`
- `hermes-agent-v2026.7.1-source.zip` or current release source snapshot

## Wheelhouse notes

Build a Windows wheelhouse from Linux with pip download flags:

```bash
python -m pip download \
  --dest wheelhouse-py311-win_amd64 \
  --only-binary=:all: \
  --platform win_amd64 \
  --implementation cp \
  --python-version 3.11 \
  --abi cp311 \
  -r requirements-windows-offline.txt
```

Also build/copy a local Hermes wheel:

```bash
python -m pip wheel --no-deps -w wheelhouse-py311-win_amd64 /root/.hermes/hermes-agent
```

Avoid `uvicorn[standard]` in the cross-platform wheelhouse command from Linux: pip may try to resolve non-Windows extras such as `uvloop`. Prefer `uvicorn==...` for the offline Windows wheelhouse unless building directly on Windows.

Platform markers may be ignored by the host environment during cross-download. For Windows-specific packages, include direct lines such as:

- `tzdata==...`
- `pywinpty>=2.0.0,<3`
- `concurrent-log-handler==...`
- `pywin32==...`
- `portalocker==...`
- `colorama==...`

## Offline installer behavior

The offline PowerShell script should:

1. Install bundled Python into `%LOCALAPPDATA%\hermes\python311`.
2. Extract bundled Node.js into `%LOCALAPPDATA%\hermes\node` and add it to User PATH.
3. Extract bundled PortableGit into `%LOCALAPPDATA%\hermes\git`.
4. Set `HERMES_GIT_BASH_PATH` to the resolved `bash.exe`.
5. Create `%LOCALAPPDATA%\hermes\hermes-agent\venv`.
6. Install `pip`, `setuptools`, and `wheel` from the local wheelhouse only.
7. Install the local `hermes_agent-*.whl` from the wheelhouse only.
8. Set `HERMES_HOME=%LOCALAPPDATA%\hermes`.
9. Add the venv `Scripts` directory to User PATH.
10. Tell the user to open a new PowerShell and run `hermes --version`, `hermes doctor`, and `hermes setup`.

## Verification checklist

Before reporting done:

- The final zip exists and is non-empty.
- `unzip -tq` reports no errors.
- `SHA256SUMS.txt` exists inside the folder.
- The final zip has a `.sha256` file.
- The wheelhouse contains the Hermes wheel and Windows wheels.
- The canonical guide lists both the folder and the final zip.
- The final answer states clearly that cloud models still need either internet later or a local model server.

## Limitation to state explicitly

A fully offline Hermes install does not mean fully offline AI usage. The installed agent still needs either:

- later internet access for cloud models and online tools, or
- a local model server such as LM Studio or Ollama.

Browser automation may also require a separate offline browser/Playwright cache package if the user needs that feature offline.
