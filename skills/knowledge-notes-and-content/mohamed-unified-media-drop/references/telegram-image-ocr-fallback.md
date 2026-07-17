# Telegram Image OCR Fallback (when vision_analyze is unavailable)

## When to use

Mohamed sometimes sends screenshots from Telegram (task lists, plans, app screens) instead of links. If `vision_analyze` returns an error like `No LLM provider configured for task=vision`, fall back to OCR + color analysis.

## Step-by-step fallback

### 1. Get the image path
Telegram images land in `/root/.hermes/image_cache/img_*.jpg`.

### 2. Quick OCR with tesseract
```bash
tesseract /path/to/image.jpg /tmp/img_ocr -l ara+eng --psm 6
cat /tmp/img_ocr.txt
```

`--psm 6` (uniform block of text) works best for screenshots. The OCR will be noisy but extractable.

### 3. If color coding matters (e.g. "only the green parts")
Install pytesseract for bounding boxes:
```bash
pip install pytesseract --break-system-packages -q
```

Then run a Python script to:
- Get word-level bounding boxes from `pytesseract.image_to_data()`
- For each text line, sample the pixel region
- Mask green pixels: `(G > R + 25) & (G > B + 25) & (G > 70)`
- Flag lines with >2% green pixel density

### 4. Green detection numpy pattern
```python
green_mask = (box[:,:,1].astype(int) > box[:,:,0].astype(int) + 25) & \
             (box[:,:,1].astype(int) > box[:,:,2].astype(int) + 25) & \
             (box[:,:,1] > 70)
green_pct = np.mean(green_mask) * 100
```

Adjust thresholds if green is too faint (lower `+25`) or picking up noise (raise `+25`).

### 5. Present findings and confirm
OCR + color analysis is imperfect. After extracting the green-marked items:
1. Present the extracted list clearly.
2. Ask Mohamed to confirm before proceeding.
3. Never assume 100% accuracy from OCR alone.

## Pitfalls

- Tesseract Arabic+English mixed text is often garbled; read for gist, not exact words.
- Green detection thresholds may need tuning per-screenshot.
- `pytesseract` may not be installed; install it only when needed.
- The `vision_analyze` failure is an environment/setup issue — if fixed later, prefer it over OCR.
- Do NOT save pytesseract to memory or skills as a permanent dependency; install on demand.
