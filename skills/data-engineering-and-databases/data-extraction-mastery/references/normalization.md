# Normalization

Normalize after extraction, never before preserving raw. Standardize encodings to UTF-8, parse dates with explicit formats when possible, normalize Arabic digits if needed, preserve original text, parse numbers with locale-aware separators, and keep null reason when known.

Arabic rules: try utf-8/cp1256; preserve RTL text; do not reverse strings manually unless a rendering artifact is proven.

When to use: before loading to DB. When it fails: ambiguous dates, mixed locales, OCR noise. Watch: silent type coercion.

Usage image: detect, preserve structure, validate, and only then normalize/load.
