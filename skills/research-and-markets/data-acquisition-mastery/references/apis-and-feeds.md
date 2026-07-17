# APIs and Feeds

API before scraping. Look for OpenAPI docs, official SDKs, CSV exports, RSS/Atom, JSON feeds, data dumps, pagination parameters, rate limits, auth scopes, and license. Capture schema and pagination state in the manifest.

Patterns: page/limit, cursor, next_url, Link headers, since/updated_after watermarks. For GraphQL, prefer persisted/documented queries and avoid introspection abuse.

When to use: official endpoints, data portals, feeds. When it fails: undocumented/private endpoints, auth scope missing, license forbids reuse.

Usage image: acquire only what is authorized, save raw + manifest, then hand off to extraction.
