# YouTube Extraction Notes

Session-derived notes for robust YouTube media-note generation.

## Metadata JSON

When using `yt-dlp --dump-single-json`, write stdout directly to a temp file, then parse the file:

```bash
mkdir -p /tmp/youtube_<id>
yt-dlp --dump-single-json --skip-download --no-warnings '<url>' > /tmp/youtube_<id>/full.json
python3 - <<'PY'
import json, pathlib
p = pathlib.Path('/tmp/youtube_<id>/full.json')
data = json.loads(p.read_text(errors='replace'))
print(data['title'])
PY
```

Reason: some tool wrappers truncate or transform large stdout strings, which can make `json.loads(captured_output)` fail with control-character or partial-JSON errors.

## Transcript API

Use `youtube_transcript_api` before browser fallbacks. List available transcripts, then fetch English generated transcript when Arabic is absent. Newer objects may expose transcript entries as objects rather than dicts, so normalize both forms:

```python
d = x if isinstance(x, dict) else {'text': x.text, 'start': x.start, 'duration': x.duration}
```

## Mohamed Output Rule

For Mohamed, a bare YouTube link defaults to the unified file-drop note workflow unless he explicitly asks for download, audio, formats, or quick chat-only summary.
