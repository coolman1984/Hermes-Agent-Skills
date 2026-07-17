# Mobile call-recording ASR benchmark — Mohamed Android/PRoot — 2026-06-23

## Why this exists

Mohamed asked to test the mobile-friendly ASR workflow on the latest call recording of the day, then improve the skill library with the durable lesson.

This is not a general claim that local ASR is bad. It is a benchmark/pitfall for **Arabic phone-call recordings on mobile CPU**.

## Test file pattern

Call recordings were found under:

`/storage/emulated/0/Recordings/Call/`

Latest tested example:

`/storage/emulated/0/Recordings/Call/Call Mr. Abdullah Selim_260623_171841.m4a`

Observed characteristics:

- Duration: about 61.65 seconds
- Format: `m4a` / AAC
- Channels: mono
- Sample rate: 48 kHz
- Typical phone-call issues: compression, narrow speech band, possible low/uneven volume, colloquial Egyptian Arabic, silence/noise at the beginning

## Attempts and outcomes

### faster-whisper via `audio_transcribe_mobile.py`

Settings tried:

- `--quality balanced --language ar` → selected `base`
- `--quality fast --language ar --beam-size 1` → selected `tiny`
- with VAD and light ffmpeg preprocessing

Outcome:

- The pipeline executed and wrote Markdown/JSON outputs successfully.
- The transcript was not reliable: repeated phrases and hallucinated Arabic appeared, especially near the beginning.

### whisper.cpp

Command shape used:

```bash
ffmpeg -y -i "$AUDIO" -vn -ac 1 -ar 16000 \
  -af "highpass=f=80,lowpass=f=7600,dynaudnorm=f=150:g=15" /tmp/call.wav

whisper-cli -m /root/.local/opt/whisper.cpp/models/ggml-base.bin \
  -f /tmp/call.wav -l ar -t 6 -bs 5 -bo 5 \
  -otxt -osrt -oj -of "$OUTBASE" --suppress-nst --print-confidence -np
```

Outcome:

- Faster than the Python path on the same phone-class environment.
- Still not reliable on the tested call recording.
- Produced text/SRT/JSON, but with repeated/incorrect phrases.

## Durable lesson

For clean short clips, the local mobile path can work well. For compressed Egyptian-Arabic phone calls, tiny/base local models can produce plausible-looking but unreliable text.

Do **not** present such output as a faithful transcript when the result contains:

- repeated phrases across long spans;
- nonsensical Arabic;
- obvious filler loops after silence;
- no stable topical meaning across segments.

Label the result as **unreliable** and save a test summary rather than pretending the transcript is usable.

## Recommended escalation ladder for future calls

1. Start with `audio_transcribe_mobile.py --quality balanced --language ar`.
2. If repetitions/garbage appear, retry with:
   - `--quality fast --beam-size 1` for a quick sanity check;
   - no denoise / no VAD only if preprocessing seems to damage speech;
   - `whisper.cpp` base model for a faster alternate engine.
3. If all local outputs remain bad, stop local retry loops and escalate:
   - run a larger model on stronger hardware;
   - use a cloud ASR service with Arabic support;
   - use Gemini or another multimodal audio model after credentials are fixed;
   - manually inspect only short critical snippets.
4. For privacy-sensitive calls, ask before sending audio to any cloud service.

## Practical note

`whisper.cpp` is worth keeping as an alternate engine on mobile because it is faster and has quantized/mobile-friendly models. It is not automatically more accurate on poor Arabic call recordings.
