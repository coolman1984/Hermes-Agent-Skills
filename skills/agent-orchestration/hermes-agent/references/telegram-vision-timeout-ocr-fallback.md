# Telegram Vision Timeout OCR Fallback

## Context

A Telegram image reached Hermes successfully and was routed through native model vision, but the auxiliary vision call failed with a short internal timeout:

```text
Error analyzing image: Codex auxiliary Responses stream exceeded 30.0s total timeout
```

The global Hermes terminal timeout was higher, so this looked like an internal auxiliary/tool timeout rather than a normal command timeout.

## Discovery path

Useful checks:

```bash
hermes tools list --platform telegram | sed -n '/vision/Ip;/image/Ip;/browser/Ip'
hermes config path
hermes config env-path
hermes status --all
sed -n '/Cached user photo/Ip;/Image routing/Ip;/timeout/Ip' ~/.hermes/logs/gateway.log | tail -80
tesseract --list-langs
```

Avoid printing `.env` values or provider credentials. If status/config output contains secrets, redact them in user-facing summaries.

## Practical fallback

If the image is text-heavy and the native vision call fails:

1. Use any visible preview text if it is clear enough.
2. Locate the cached image path from gateway logs, usually under:

```text
~/.hermes/image_cache/
```

3. Run local OCR when Tesseract is available:

```bash
tesseract /path/to/image.jpg stdout -l ara+eng --psm 6
```

4. If a helper script exists, prefer it:

```bash
~/.hermes/scripts/image_ocr_fallback.sh /path/to/image.jpg
```

The helper used in this session tries Arabic plus English OCR and optionally uses ImageMagick/convert preprocessing when available.

## Known environment notes

In Mohamed's current environment, Tesseract is installed and has these languages:

```text
ara
eng
osd
```

Python image-processing libraries such as Pillow, OpenCV, pytesseract, EasyOCR, and numpy were not available, so shell-level Tesseract was the lowest-friction fallback.

## User-facing behavior

Do not pretend vision succeeded if it timed out. Say plainly that the primary vision tool failed, then use OCR fallback and label the OCR result as approximate if image quality is low.
