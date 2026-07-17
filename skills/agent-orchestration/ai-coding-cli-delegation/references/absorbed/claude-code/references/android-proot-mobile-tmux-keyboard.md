# Claude Code on Mohamed's Android PRoot + Termux

Use this when Claude Code launches but mobile keyboard input, tmux, or interactive TUI behavior is unreliable in Mohamed's Android/PRoot setup.

## Durable pattern

Claude Code can work normally on this setup, including authenticated Claude Pro and Opus high-effort interactive sessions, but the launch path matters.

## Known-good layers

- Run Claude through the safe wrapper:

```bash
/root/.local/bin/claude-safe
```

- Use tmux from inside the Ubuntu/PRoot distro:

```bash
/usr/bin/tmux
```

Do not rely on Termux tmux for launching Linux/glibc binaries inside the Ubuntu environment; it can start the wrong environment and cause loader errors such as `invalid ELF header`.

## Mobile keyboard fix

Edit Termux properties:

```text
/data/data/com.termux/files/home/.termux/termux.properties
```

Recommended lines:

```text
enforce-char-based-input = true
extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
```

Reload settings:

```bash
termux-reload-settings
```

If the keyboard still behaves oddly, force-stop Termux from Android settings and reopen it.

## tmux config

Create or keep `/root/.tmux.conf` with mobile/TUI-friendly settings:

```tmux
set -g default-terminal "tmux-256color"
set -ga terminal-overrides ",xterm-256color:Tc"
set -as terminal-features 'xterm*:extkeys'
set -g allow-passthrough on
set -s extended-keys on
set -g xterm-keys on
set -sg escape-time 10
set -g focus-events on
set -g mouse on
set -g history-limit 50000
set -g prefix C-a
bind C-a send-prefix
```

## Useful wrapper pattern

Use three helper concepts:

- `claude-mobile <session> <project>`: start or attach a Claude Code tmux session using `/usr/bin/tmux`, `opus`, and high effort.
- `claude-send <session> "prompt"`: paste a prompt into the Claude Code TUI and press Enter. This bypasses mobile keyboard problems for long prompts.
- `claude-screen <session>`: capture recent tmux output for monitoring.
- `claude-trust <session>`: send Enter for the initial trust prompt when the keyboard cannot confirm it.

## Verification

1. Non-interactive smoke test:

```bash
cd /tmp && /root/.local/bin/claude-safe -p 'Return exactly OK' --model opus --effort high --max-turns 1 --output-format text
```

2. Interactive tmux smoke test:

```bash
claude-screen claude-test /tmp
claude-trust claude-test
claude-send claude-test 'Say exactly TMUX_OK and do not run tools.'
claude-screen claude-test
```

Expected result includes `TMUX_OK` and the Claude Code header showing Opus high effort.

## Non-blocking doctor issue

MCP servers may show authentication warnings, for example Microsoft 365 needing auth. Treat that as non-blocking for core Claude Code operation unless the user specifically needs that MCP server.
