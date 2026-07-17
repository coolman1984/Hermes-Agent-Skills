---
name: camoufox-proot-setup
description: Install, download, and verify Camoufox in Linux aarch64 / PRoot / Termux-like
  environments, including a headless smoke test and common pitfalls.
tags: [camoufox, proot, aarch64, termux, setup, browser]
---

# Camoufox on Linux aarch64 / PRoot

Use this skill when a user wants to try Camoufox in an Android/Termux/PRoot-style Linux environment, especially on aarch64/arm64.

## Why this workflow exists
Camoufox can work in this environment, but the right path is:
1. install the Python package in an isolated venv
2. download the browser binary with `python -m camoufox fetch`
3. verify with a tiny headless Playwright smoke test

The browser download is large and may take several minutes, so use background execution when needed.

## Observed constraints
- The environment may be Linux aarch64 under PRoot, not a native desktop Linux install
- `camoufox` supports arm64 browser binaries
- `python -m camoufox fetch` can download a very large archive and may time out in foreground shells
- `headless=True` worked successfully for a smoke test
- The browser path in this environment resolved to `/data/data/com.termux/cache/camoufox`

## Recommended steps

### 1) Create an isolated venv
```bash
python3 -m venv /tmp/camoufox-venv
. /tmp/camoufox-venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
```

### 2) Install Camoufox
```bash
python -m pip install 'camoufox[geoip]'
```

### 3) Check package status
```bash
python -m camoufox version
python -m camoufox path
```

Expected:
- package version is shown
- browser is not downloaded yet until fetch runs
- `path` should print the cache path

### 4) Download the browser
```bash
python -m camoufox fetch
```

If the foreground shell is too short, run it in the background and poll until complete.

### 5) Verify a smoke test
```bash
python - <<'PY'
from camoufox.sync_api import Camoufox

with Camoufox(headless=True) as browser:
    page = browser.new_page()
    page.goto('https://example.com', wait_until='domcontentloaded', timeout=30000)
    print('TITLE:', page.title())
    print('URL:', page.url)
PY
```

Expected:
- title: `Example Domain`
- URL loads successfully

## Helpful checks
```bash
python -m camoufox version
python -m camoufox path
```

If `version` says the package is installed but the browser is not downloaded, run `fetch` again.

## Common pitfalls

### Download timeout
The browser archive is huge. If `fetch` times out in the foreground, rerun it in the background and poll for completion.

### Slow network / quick-read fallback
On slow PRoot/Android links, `pip install "camoufox[geoip]"` can spend a long time downloading the GeoIP bundle, and the full browser fetch may be even slower. If Camoufox is already installed, use it immediately when content is blocked, then fall back to X mirrors (`fxtwitter`, `vxtwitter`, `r.jina.ai`) only after Camoufox confirms a login-wall/empty page. If Camoufox is not installed and setup would be lengthy, explain the setup blocker and use mirrors as a temporary fallback while preserving the rule that browser-backed extraction is preferred for blocked content.

### Wrong environment assumption
This workflow was validated in Linux aarch64 under PRoot. Don't assume native desktop Linux behavior.

### Headless launch issues
If headless launch fails, check whether the environment is missing required display/browser dependencies. In the observed environment, plain headless mode worked.

### GeoIP extra
`camoufox[geoip]` adds useful locale/timezone/geo alignment support, but it also downloads extra data. Keep that in mind if you only need a minimal install.

## Interactive login via VNC/noVNC

Use this when the user needs to log into a site themselves (for example X/Twitter articles) and the shell has no graphical display (`DISPLAY` empty). Do **not** ask for or handle the user's password/2FA code; provide a local browser session and let the user type credentials directly.

### 1) Install a lightweight visible desktop
```bash
DEBIAN_FRONTEND=noninteractive apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y \
  tigervnc-standalone-server tigervnc-common fluxbox xterm novnc websockify dbus-x11
```

### 2) Configure TigerVNC startup
TigerVNC may use `~/.config/tigervnc/xstartup` rather than `~/.vnc/xstartup`. Keep the startup script alive by `exec`ing the window manager; if it exits quickly, VNC kills the session.

```bash
mkdir -p ~/.config/tigervnc ~/.vnc ~/.hermes/state ~/.camoufox-profiles/x-login
cat > ~/.config/tigervnc/xstartup <<'SH'
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
xrdb "$HOME/.Xresources" 2>/dev/null || true
xsetroot -solid '#202020'
exec fluxbox
SH
chmod +x ~/.config/tigervnc/xstartup
```

### 3) Set a temporary local VNC password
TigerVNC passwords are limited to 8 effective characters.

```bash
PASS=$(python3 -c "import secrets,string; a=string.ascii_letters+string.digits; print('X'+''.join(secrets.choice(a) for _ in range(7)))")
printf '%s\n%s\n\n' "$PASS" "$PASS" | vncpasswd
mkdir -p ~/.hermes/state
printf '%s' "$PASS" > ~/.hermes/state/x-vnc-password
chmod 600 ~/.hermes/state/x-vnc-password ~/.vnc/passwd 2>/dev/null || true
```

### 4) Start VNC and noVNC
```bash
vncserver -kill :1 >/tmp/vnc_kill.log 2>&1 || true
vncserver :1 -geometry 1280x800 -depth 24 -localhost yes
```

Start noVNC as a tracked background process (do not shell-background with `&` in foreground mode):

```bash
websockify --web=/usr/share/novnc/ 127.0.0.1:6080 127.0.0.1:5901
```

Use the terminal tool's `background=true` for the `websockify` command, then verify `http://127.0.0.1:6080/vnc.html` returns HTTP 200.

### 5) Launch Camoufox into the visible display with a persistent profile
Create a small script, then run it with `DISPLAY=:1` as a background process:

```python
from camoufox.sync_api import Camoufox
from pathlib import Path
import time

profile = Path('/root/.camoufox-profiles/x-login')
profile.mkdir(parents=True, exist_ok=True)

with Camoufox(
    headless=False,
    persistent_context=True,
    user_data_dir=str(profile),
    window=(1280, 760),
    locale='en-US',
    args=['--no-remote'],
) as context:
    page = context.pages[0] if context.pages else context.new_page()
    page.goto('https://x.com/login', wait_until='domcontentloaded', timeout=60000)
    while True:
        time.sleep(5)
```

Command pattern:

```bash
DISPLAY=:1 DBUS_SESSION_BUS_ADDRESS= python3 /root/.hermes/scripts/x_camoufox_login.py
```

### 6) Hand off to the user
Open or send the local noVNC URL:

```bash
termux-open-url 'http://127.0.0.1:6080/vnc.html?autoconnect=true&resize=scale'
```

Give the user only the local noVNC URL and temporary VNC password. Ask them to log in themselves and reply when complete. After they confirm, verify with the same persistent profile by opening a previously blocked article and checking that the body is not login/signup chrome.

### Pitfalls from field use
- VNC startup fails with “Session startup ... exited too early” if the startup script backgrounds everything and exits; use `exec fluxbox`.
- `vncpasswd` rejects passwords longer than 8 characters.
- `~/.vnc/xstartup` may be ignored by TigerVNC on this distro; use `~/.config/tigervnc/xstartup`.
- Use `terminal(background=true)` for long-lived `websockify` and Camoufox login scripts; foreground commands containing `&` are rejected by tool policy.
- Keep VNC bound to localhost (`-localhost yes`, `127.0.0.1:6080`) unless the user explicitly asks for remote access and understands the risk.
- X/Twitter can reject fresh Camoufox/VNC login attempts with “Suspicious login prevented.” If this appears, stop the Camoufox login process and noVNC/websockify immediately; do not retry in a loop because repeated attempts can extend the account block.
- For X after a suspicious-login block, prefer an already trusted browser session on the user's device (for example Comet/Chrome) via ADB visual control, or a user-provided authorized session cookie if they explicitly choose that route. Do not extract, display, or store saved passwords.

## Verification target
A successful run should prove all of these:
- package installs cleanly
- browser binary downloads
- `python -m camoufox version` reports the installed browser version
- a headless Playwright smoke test loads `example.com`
- for interactive auth, noVNC loads locally, Camoufox opens in display `:1`, and the persistent profile preserves login state

## When to reuse this skill
Use this for any future Camoufox setup on:
- Android PRoot
- Termux-like Linux
- aarch64/arm64 shells
- constrained environments where browser downloads need background polling
