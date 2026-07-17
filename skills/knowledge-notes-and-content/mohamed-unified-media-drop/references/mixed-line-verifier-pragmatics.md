# Mixed Arabic/Latin Line Verifier — Practical Triage

## Problem

The `verify_media_note.py` script strictly flags every line containing both Arabic and Latin characters as a "mixed" violation. When the source content itself is about English-named products, protocols, or companies, this produces dozens of warnings — many of which are unavoidable for coherent prose.

## Triage Framework

After the verifier runs, classify each flagged line into one of three buckets:

### Bucket 1: Essential Proper Nouns (ACCEPT)
Lines where the English term is a proper noun with no widely-used Arabic equivalent. Do NOT fix these:
- Product names: Obsidian, Kimi K2.6, ChatGPT, Claude, Gemini, Notion
- Protocol/standard names: MCP, REST API, SQL, GraphQL
- Repository names: `dyerlab/Nooscope`, `sweir1/obsidian-brain`
- URLs (any line consisting of or dominated by a URL)
- Company names: Mem AI, Notion AI, Glean, Snowflake, Databricks
- Model names: Swan-Large, GATE-AraBERT-v1, Aya-8B, BGE-M3
- Pricing: "$12/mo", "$15/M tokens"

### Bucket 2: Technical Terms with Clear Arabic (FIX)
Lines where the English term has a straightforward Arabic equivalent and it sits inside Arabic prose. Fix these by replacing with the Arabic term or moving the English to a parenthetical on the same line:
- "framework" → use the Arabic context
- "workflow" → "سير العمل"
- "pipeline" → "خط الأنابيب"
- "embedding" → "تضمين" (use Arabic term in prose, English in parentheses)
- Generic adjectives: "real-time", "open-source"

### Bucket 3: Structural Mixing (FIX)
Lines where English is embedded inside Arabic prose for no good reason — the English token is not a proper noun and not necessary:
- `النظام يقدم compounding effect قوي` → fix: `النظام يقدم أثرًا تراكميًا قويًا`
- `هذا هو الـ killer feature` → fix: `هذه هي الميزة القاتلة`
- Avoid mixing in headings: `## 1) Source Metadata` → `## 1) مصدر المحتوى`

## Practical Rule

1. Run the verifier after writing.
2. If Bucket-1-only warnings remain (proper nouns), note in the delivery: "تحذيرات الخلط لأسماء منتجات ضرورية فقط."
3. Fix Bucket 2 and Bucket 3 before delivery.
4. Never globally search-replace English terms — fix line by line.

## When the Source IS About English Products

When the entire article is about English-named products (e.g., "Obsidian + Kimi K2.6"), the Arabic prose will unavoidably contain these names. The verifier will always flag them. This is acceptable. Do not:
- Move every product name to a separate line (destroys readability)
- Transliterate product names into Arabic script (creates confusion)
- Skip writing the note because verifier will complain

Instead: write natural professional Arabic prose that keeps proper nouns inline, run the verifier, acknowledge Bucket-1 warnings, and deliver.
