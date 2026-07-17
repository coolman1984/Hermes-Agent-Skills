# Mobilerun Routing Checklist

## Integration steps
- Install the Droidrun Portal APK on the phone.
- Obtain a Mobilerun API key from mobilerun.ai.
- Add `skills.entries.mobilerun.enabled = true` in `openclaw.json`.
- Inject the API key through `skills.entries.mobilerun.env.MOBILERUN_API_KEY` using an environment reference.
- Confirm `adb` is installed and available on the host that runs OpenClaw.
- Restart or start a new session so the skill is loaded.

## Suggested tests
1. Ask the agent to identify the foreground app.
2. Ask the agent to list visible buttons.
3. Ask the agent to tap a harmless control.
4. Ask the agent to type into a known text field.
5. Ask the agent to take a screenshot or dump the UI tree if supported.

## Fallbacks
- If the Mobilerun portal is unavailable, use Termux:API and ADB-based automation instead.
- If `MOBILERUN_API_KEY` is missing, do not expose the skill as enabled.

## Safety
- Use explicit user confirmation before external or destructive actions.
- Keep secrets out of chat and logs.
