# Monitoring and Recurring Collection

Use ETag/Last-Modified, content hashes, and manifests to detect changes. Cron jobs should be quiet if no change. Store last successful source state.

When to use: recurring source monitoring. When it fails: sites without cache validators, changing timestamps with identical data. Watch: false positives from ads/layout.

Usage image: acquire only what is authorized, save raw + manifest, then hand off to extraction.
