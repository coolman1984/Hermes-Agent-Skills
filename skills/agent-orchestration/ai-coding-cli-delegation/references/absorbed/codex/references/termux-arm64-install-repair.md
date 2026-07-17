# Codex CLI on Termux / Android arm64: install repair pattern

Use this reference when `codex` exists but exits before showing help/version with a missing platform package error, especially on Mohamed's Android/Termux/PRoot environment.

## Symptom

`codex --help` or `codex --version` fails with:

```text
Error: Missing optional dependency @openai/codex-linux-arm64. Reinstall Codex: npm install -g @openai/codex@latest
```

## Root pattern

Codex is installed through npm and expects a platform-specific optional dependency alias such as:

```text
@openai/codex-linux-arm64 -> npm:@openai/codex@<version>-linux-arm64
```

In Termux/PRoot, global npm prefix can point somewhere different from the running `codex` executable. Then `codex doctor` may report:

```text
npm install -g @openai/codex would update a different install
running package root .../usr/lib/node_modules/@openai/codex
npm package root /usr/local/lib/node_modules/@openai/codex
```

## Repair sequence

Prefer installing into the prefix that owns the running executable:

```bash
which -a codex
readlink -f /data/data/com.termux/files/usr/bin/codex || true
npm root -g
npm config get prefix
npm install -g --prefix /data/data/com.termux/files/usr @openai/codex@latest
```

Then align npm's global prefix with the running Termux install so future `codex update` and `npm install -g` target the same package root:

```bash
npm config set prefix /data/data/com.termux/files/usr
npm config get prefix
```

## Verification

```bash
codex --version
codex --help | sed -n '1,80p'
codex doctor --summary
```

Expected install result:

```text
runtime npm
install consistent
updates update configuration is locally consistent
```

## Auth follow-up

If `codex doctor` still reports incomplete credentials, the binary is fixed but auth is stale. Use one of:

```bash
codex login --device-auth
# or, if using an API key
printenv OPENAI_API_KEY | codex login --with-api-key
```

Device auth prints a browser URL and one-time code. After the user completes it, verify with a tiny git-backed smoke test:

```bash
TMP=$(mktemp -d)
cd "$TMP"
git init -q
codex exec "Do not modify files. Reply with exactly: OK"
```

## Do not overlearn

Do not encode this as "Codex does not work on Termux." The durable lesson is the prefix/optional-dependency repair and the need to separate binary install health from authentication health.
