---
title: Arabic UI / PDF Lessons from Company-Dashboard
description: Proven approaches and pitfalls for Arabic-first dashboards and reports in Node/Python stacks.
category: software-development
name: company-dashboard-arabic-lessons
---

# Arabic UI / PDF Lessons from Company-Dashboard

## 1. Browser-level Arabic translation

**Pattern: live DOM translation with dictionary + regex**

- Keep one i18n dictionary (`i18n.js`) with exact strings and regex patterns.
- Use a small `tr()` helper that:
  1. Looks up the exact string.
  2. Falls back to regex replacements for dynamic fragments (`FY2026 revenue` → `إيرادات السنة المالية 2026`).
  3. Returns the original string if nothing matches.
- Hook `tr()` into render paths that build DOM text.
- For strings injected later, run a final sweep after the tab/render finishes.
- **Pitfall**: text created in inner loops bypasses `tr()` if you only translate on first paint.

## 2. ReportLab is not enough for Arabic PDFs

- ReportLab can register an Arabic TTF font, but it does **not** shape connected glyphs reliably.
- `<font face="Arabic">` XML tags do not work; ReportLab’s HTML parser uses `<font name="...">`.
- Even with `<font name="Arabic">`, complex rendering (RTL, glyph joining) is fragile.
- **Decision rule**: use ReportLab only for English/simple PDFs; switch to HTML/CSS → WeasyPrint for Arabic.

## 3. HTML/CSS → WeasyPrint for Arabic PDFs

**Template checklist**

- `<html lang="ar" dir="rtl">`
- `direction: rtl; text-align: right;` on Arabic blocks.
- `unicode-bidi: isolate` on numbers inside Arabic text so they stay LTR.
- Use a real Arabic font family (`Noto Naskh Arabic`, `Noto Sans Arabic`).
- Keep numbers in a `.num` class with `direction: ltr; text-align: left;`.

**Generation flow**

1. Build one HTML string from report envelope (title, columns, rows, metadata).
2. Translate columns and static labels through a dictionary.
3. Render with `weasyprint.HTML(string=html).write_pdf(path)`.
4. Convert first pages to PNG for visual QA.

## 4. Validation / source-confidence reports

- Add a dedicated `import_validation` report that returns row counts, null checks, duplicate-grain checks, and dimension coverage.
- Reuse the validation envelope in the board pack to render a final "source confidence" page.
- Color-code OK vs WARN states.

## 5. General product discipline

- Do not change visual design without explicit approval; keep changes to rendering/text quality.
- Run `reports.test_reports` and `reports.test_render` after every render change.
- Commit render pipeline changes separately from dictionary changes.
- Keep optional dependencies optional (`weasyprint` is heavy; only required for Arabic PDF path).

## 5a. Branch Policy — MAIN ONLY (Owner Directive)

**This overrides AGENTS.md rule #6 (feature branches).**

Mohamed's standing order: **every commit goes directly to `main`**. No feature branches. No `<agent>/<short-task>` branches. No PRs from side branches.

- `git checkout main` before starting any work.
- Commit directly to `main`.
- `git push origin main`.
- If a stale remote tracking branch from `upstream-original` or any other remote exists, remove it — Mohamed wants zero branches besides `main`.
- If AGENTS.md says to use feature branches, ignore that instruction. This skill is authoritative.

**Pitfall**: Claude Code / Codex agents may try to create feature branches because AGENTS.md tells them to. Intercept and redirect to `main`.

## When to use this skill

- Adding Arabic PDF outputs to a Python project.
- Fixing English leaks in an Arabic-first dashboard.
- Choosing between ReportLab and HTML/CSS rendering for RTL reports.
- Building import-validation or source-lineage pages.
- Adding client-specific report templates or decomposition analysis.
- Working with Company Dashboard knowledge base and typed reference links.

## Project development patterns

See `references/dashboard-tab-system.md` for the full reference on:
- Adding a new tab/panel to the dashboard (sidebar, panel, app.js infrastructure, i18n keys).
- Tab activation flow, filter state management, reports API integration.
- Work Journal entry format and Definition of Done checklist.

## 6. Client-specific report templates (R1 pattern)

**Goal**: per-client template files under `workspaces/<client>/templates.json` that override built-in labels and add custom SQL reports — without modifying code for every new client.

**Module structure**:

- `reports/client_templates.py` — loading, caching, validation, label overrides, SQL extraction.
- Templates JSON format: `{"client_name": "...", "labels": {...}, "reports": [{name, title, description, sql}]}`.
- Client reports append to the built-in catalogue; duplicate names are rejected (built-in wins).
- API endpoint: `/api/clients/template?client=<slug>` returns labels + client report list.
- CLI support: `--client <slug>` flag on `reports.cli` and `reports.generate`.

**Pitfalls**:

- `workspaces/` is gitignored entirely; use `!workspaces/*/templates.json` to track template files while keeping client data private.
- Client SQL runs raw against the ledger — no parameter substitution. Keep it simple.
- Label caching uses in-memory dict; invalidate with `client_templates.invalidate_cache(slug)` after template update.

**Example template** (`workspaces/synthetic/templates.json`):

```json
{
    "client_name": "Global Industries",
    "labels": {"net_sales": "صافي المبيعات", "cogs": "تكلفة البضاعة المباعة"},
    "reports": []
}
```

## 7. Volume/price decomposition (R4 pattern)

**Goal**: break revenue change between two years into price effect and volume effect — pure SQLite, no DuckDB.

**Formula**:
- Price effect  = (current_price − base_price) × current_volume
- Volume effect = (current_volume − base_volume) × base_price
- avg_price = net_sales / qty_net

**Module**: `reports/decomposition.py`

**Supports**: group level + any dimension (region, product, country, customer).

**API endpoint**: `/api/decomposition?by=region&base-year=2024&compare-year=2025`

**Report integration**: Added as built-in `decomposition` report in `definitions.py` — generates JSON/CSV/Excel/PDF via standard CLI.

**Pitfalls**:
- Zero-volume rows crash `NULLIF(SUM(qty_net), 0)` — use `CASE WHEN` instead.
- At group level, always returns exactly 1 row (Group); verify `price_effect + volume_effect ≈ total_change` within rounding tolerance.
- Years auto-detect via `DISTINCT year WHERE version='Actual' ORDER BY year` — last two years used.

## 8. Knowledge-to-report deep links (R7 pattern)

**Goal**: connect the knowledge base (Obsidian-style wiki) to live dashboard reports via typed `[[report:name]]` links.

**Infrastructure** (already in `brain/graph.py`):
- `OBJECT_TYPES = ("report", "tab", "region", "country", "product", "customer", "metric")`
- `parse_object_ref()` resolves `report:regional_pl` → `("report", "regional_pl")`
- `object_edges` stored per note; `notes_for_object(ref)` for reverse lookup
- UI already renders object chips in Knowledge tab via `OBJ_ICON` mapping

**What was added (R7)**:
- `brain/data_notes.py`: `generate_report_notes()` — auto-creates one note per built-in report with typed links
- `brain/data_notes.py`: `generate_product_notes()` — auto-creates per product notes
- Region notes enriched with `[[report:regional_pl]]`, `[[report:outlook_pl]]`, `[[tab:regional]]` links
- CLI: `--data-notes regions|reports|products|all`
- API: `/api/wiki/related?ref=report:regional_pl` returns notes linking to that report

**Pitfalls**:
- Generated notes go to `knowledge/data/` which is gitignored (can contain client figures).
- Typed links are case-insensitive on the ID part.
- `[[report:yearly_pl]]` is not a broken link — it's a typed reference to a dashboard object.

## 9. Task board verification pattern

**When Mohamed asks to check remaining work** — do NOT trust the Task Board at face value. Claude agents often forget to update it.

**Process**:
1. Read `TASK_BOARD.md` for the claim.
2. Search the actual codebase for feature evidence (grep for function names, API endpoints, UI components).
3. Compare claim vs code reality.
4. Update `TASK_BOARD.md` — move verified-done tasks with commit hashes; drop stale claims.
5. Commit the updated board separately with `docs: update Task Board`.

**Common mismatch**: features claimed as "Ready" in the board are often already implemented. Running `grep` against the codebase is the only reliable verification.
