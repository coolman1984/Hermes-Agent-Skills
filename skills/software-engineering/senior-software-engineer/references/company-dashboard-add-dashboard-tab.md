# Company-Dashboard: Adding a New Dashboard Tab

Proven pattern for adding a feature tab to the Company-Dashboard UI. Touches 4 files; follow the checklist to avoid gaps.

## Checklist (in order)

### 1. i18n keys (if they don't already exist)

Check `i18n.js` for pre-existing keys — the project sometimes plants translations before the tab is built (e.g. `tab.reports` was there months before the UI). If missing, add:

- `tab.<name>` — sidebar button label
- `page.<name>.title` / `page.<name>.sub` — top-bar heading
- Any section-specific keys (e.g. `reports.sectionTitle`)

Add to BOTH `ar` and `en` dictionaries.

### 2. index.html — sidebar tab button

Add inside `<nav class="tabs" role="tablist">`:

```html
<button class="tab" type="button" role="tab" id="tab-<name>" aria-selected="false" aria-controls="panel-<name>" data-tab="<name>">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">…</svg>
    <span data-i18n="tab.<name>">Label</span>
</button>
```

Pick an SVG icon from the existing set or use a new one.

### 3. index.html — panel section

Add inside `<main class="main-shell">` before the closing `</div>`:

```html
<section class="panel" id="panel-<name>" role="tabpanel" aria-labelledby="tab-<name>" hidden>
    <div class="section-head"><div><h2 data-i18n="<name>.sectionTitle">Title</h2><p data-i18n="<name>.sectionDesc">Description</p></div></div>
    <!-- panel content -->
</section>
```

Use `data-i18n` attributes on static text so the MutationObserver translates them. Use the project's existing card/table patterns.

### 4. index.html — CSS (if new visual components)

Add styles in the `<style>` block. Use `var(--surface)`, `var(--muted)`, `var(--cyan)` for theme consistency. Keep selectors scoped (class-based, not ID-based).

### 5. app.js — state wiring

Add the tab name to these data structures:

```js
var tabLoaded = { …, <name>: false };
var pageMeta = { …, <name>: ['Title', 'Description'] };
```

### 6. app.js — loader function

Add to the loader map inside `loadActiveTab`:

```js
var loader = { …, <name>: load<Name> }[activeTab];
```

Write a `load<Name>(force)` function following the existing pattern:
- Set `tabLoaded.<name> = true` when done
- Handle loading, empty, and error states
- Use `fetchJson(API + '/api/…', { force: force })`

### 7. app.js — configureGlobalFiltersForTab

Add a case for the new tab. If the tab doesn't use filters, disable them and hide the apply/reset buttons:

```js
if (tabName === '<name>') {
    yearSelect.disabled = true;
    versionSelect.disabled = true;
    el('globalRegion').disabled = true;
    el('globalCountry').disabled = true;
    el('applyFiltersBtn').style.display = 'none';
    el('resetFiltersBtn').style.display = 'none';
    return;
}
```

Also update the "leaving" branch to re-enable everything:

```js
el('globalRegion').disabled = false;
el('globalCountry').disabled = false;
el('applyFiltersBtn').style.display = '';
el('resetFiltersBtn').style.display = '';
```

### 8. app.js — event bindings (if needed)

Add to `bindEvents()` for any custom controls (close buttons, action buttons). The generic tab-click and export-CSV bindings are automatic.

### 9. Verification

```bash
node --check app.js && node --check i18n.js && node --check server.js
python3 seed_db.py --force
npm test
```

Then browser QA:
1. Start server, open Playwright
2. Click the new tab — verify heading, content, filters disabled
3. Exercise all interactive elements (buttons, links)
4. Switch to EN, verify translations
5. Check console for errors

## Pitfalls

- **i18n keys exist but the tab doesn't**: the project has a habit of planting translations early. Always grep `i18n.js` for `tab.<name>` before assuming you need to add keys.
- **Filters must be re-enabled on exit**: when a tab disables filters, the "leaving reports mode" branch in `configureGlobalFiltersForTab` must re-enable them for all other tabs.
- **Don't hardcode English in the panel**: use `data-i18n` attributes on static text and `tr()` for JS-generated text. The MutationObserver handles the rest.
- **Tab ordering matters**: the sidebar nav has implicit groupings (Analytics). Place the new tab where it makes sense in the hierarchy.
- **Loader-map key must match `data-tab` value exactly**: the `activeTab` variable drives the dispatch — if they don't match, the tab loads empty.

## Files touched (reference)

| File | What changed |
|------|-------------|
| `index.html` | Tab button + panel section + CSS |
| `app.js` | `tabLoaded`, `pageMeta`, loader map, loader function(s), `configureGlobalFiltersForTab`, `bindEvents` |
| `i18n.js` | `ar` + `en` dictionary entries |
| — | No server changes needed if API already exists |

## Example commit (2026-06-16 — Reports tab)

```
feat: add Reports dashboard tab with download UI

- Sidebar: new Reports tab with document icon (after Portfolio)
- Panel: report list cards (6 reports) with View/CSV buttons
- View: inline table render with Export CSV + Back to list
- CSV: direct download from /api/reports/generate
- i18n: Arabic/English keys for section title/description
- Filters: disabled on the Reports tab (reports are not filter-dependent)
- CSS: .report-card, .report-list, .report-card-actions patterns
```
