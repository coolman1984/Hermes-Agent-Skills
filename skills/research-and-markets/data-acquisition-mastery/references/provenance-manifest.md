# Provenance Manifest

Every payload needs a manifest row: source_url, method, status, content_type, fetched_at, bytes, sha256, legal_basis, license, robots_allowed, cache_path, extractor_next_step, warnings.

This manifest is the contract between acquisition and extraction.

When to use: every acquisition. When it fails: missing legal basis or source identity. Watch: raw payload without metadata.

Usage image: acquire only what is authorized, save raw + manifest, then hand off to extraction.
