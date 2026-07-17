# Telegram Typing Indicator Debugging Reference

## Symptom
Mohamed reported Telegram header shows "typing" indicator persistently even after the response is delivered.

## Investigation Summary
Root cause: `send()` in `telegram.py` calls `send_typing()` after every message (lines 2238 and 2466). Even the final response message triggers a fresh `sendChatAction("typing")` that persists for ~5 seconds.

## Code Flow

```
inbound message
  → _process_message_background()
    → _keep_typing() task starts — sends typing every 2s (base.py:3132)
    → handler runs, generates response
    → response sent via send() (telegram.py:2466 — re-triggers typing AFTER message)
      → This one-shot typing persists ~5 seconds after final message
    → finally: _stop_typing_task() cancels _keep_typing loop
```

## The Fix
`suppress_typing` metadata flag was added:
1. **base.py:4342** — Before sending the final response text, set `suppress_typing: True` in the metadata clone
2. **telegram.py:2240, 2468** — `send()` checks `metadata.get("suppress_typing")` and skips the `send_typing()` re-trigger

## Key Files
- `gateway/platforms/base.py` — `_process_message_background()`, `_keep_typing()`, `_stop_typing_refresh()`
- `gateway/platforms/telegram.py` — `send()`, `send_typing()`

## Verification
- Add logger calls before `send_typing()` calls to see when they fire
- Check gateway logs for `suppress_typing active` messages
- After fix: typing should disappear with the final response, not 5 seconds later

## Caveats
- Telegram's `sendChatAction("typing")` has no "stop" API — it always expires after ~5 seconds
- `send_multiple_images()`, `send_document()`, `send_image_file()` in telegram.py do NOT call `send_typing()` — no fix needed there
- The `_keep_typing` loop in base.py is properly cancelled by `_stop_typing_refresh`
