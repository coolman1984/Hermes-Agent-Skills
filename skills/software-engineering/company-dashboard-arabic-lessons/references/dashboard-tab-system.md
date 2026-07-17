# Company-Dashboard Tab System Reference

> How to add a new tab/panel to the dashboard. Derived from the Reports tab build (2026-06-16).

## Architecture overview

The dashboard uses a vanilla-JS tab system with no framework. Three files work together:

```
index.html   — sidebar tabs (.tab with data-tab) + panel sections (.panel with id="panel-{name}")
app.js       — activateTab(), loadActiveTab(), tabLoaded, pageMeta, configureGlobalFiltersForTab()
i18n.js      — tab.{name}, page.{name}.title, page.{name}.sub keys for Arabic + English
```

## Step-by-step: adding a new tab

### 1. index.html — sidebar tab button

Add inside `<nav class="tabs">`:

```html
<button class="tab" type="button" role="tab" id="tab-{name}"
  aria-selected="false" aria-controls="panel-{name}" data-tab="{name}">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">…</svg>
    <span data-i18n="tab.{name}">English label</span>
</button>
```

- `data-tab="{name}"` is the contract — `activateTab()` reads this.
- SVG icons use `stroke="currentColor"`, `stroke-width="1.8"` to match existing style.
- `data-i18n` handles Arabic/English toggle automatically.

### 2. index.html — panel section

Add before `</div>` (closing workspace div):

```html
<section class="panel" id="panel-{name}" role="tabpanel"
  aria-labelledby="tab-{name}" hidden>
    <div class="section-head">
      <div>
        <h2 data-i18n="{name}.sectionTitle">Section Title</h2>
        <p data-i18n="{name}.sectionDesc">Section description</p>
      </div>
    </div>
    <!-- panel content here -->
</section>
```

- `id="panel-{name}"` — must match `data-tab="{name}"` in the sidebar button.
- `hidden` attribute — removed by `activateTab()` on switch.
- Use `data-i18n` attributes on static text for bilingual support.

### 3. app.js — tab infrastructure (4 touch points)

**3a. Add to `tabLoaded`:**
```js
var tabLoaded = { overview: false, …, reports: false };
```

**3b. Add to `pageMeta`:**
```js
var pageMeta = {
    …
    {name}: ['English Page Title', 'English page subtitle']
};
```

**3c. Add loader to `loadActiveTab`:**
```js
var loader = {
    …
    {name}: load{Name}
}[activeTab];
```

**3d. Add case in `configureGlobalFiltersForTab`:**
```js
if (tabName === '{name}') {
    // Disable/hide filters as needed
    return;
}
```

Falling through to the default case re-enables all filters automatically.

### 4. app.js — load function

```js
function loadReports(force) {
    // 1. Show loading state
    // 2. Fetch data from API
    // 3. Render HTML
    // 4. Bind event listeners (button clicks, etc.)
    // 5. Set tabLoaded.{name} = true
    // 6. Handle errors gracefully
}
```

Key patterns:
- Use `fetchJson(API + '/api/…', { force: force })` — reuses the `requestCache`.
- Use `escapeHtml()` for any user/data content injected into innerHTML.
- Always set `tabLoaded.{name} = true` in both success and error paths.
- Bind event listeners with `el('…').addEventListener('click', handler)` or use `data-*` attribute selectors.

### 5. app.js — event binding (if needed)

Add in `bindEvents()`:
```js
el('{name}CloseBtn').addEventListener('click', close{Name});
```

Button-delegated events (like `[data-export-table]`) auto-bind via the existing loop.

### 6. i18n.js — translation keys

Add to both `ar` and `en` dictionaries:
```js
"tab.{name}": "Label",
"page.{name}.title": "Page Title",
"page.{name}.sub": "Page subtitle",
"{name}.sectionTitle": "Section Title",
"{name}.sectionDesc": "Section description",
```

The `page.{name}.title` and `page.{name}.sub` keys are used by `updatePageHeading()` — they MUST exist. The `{name}.sectionTitle` and `{name}.sectionDesc` are for `data-i18n` attributes in the panel HTML.

### 7. CSS

Add styles in `<style>` inside `index.html`. Follow existing conventions:
- Use `var(--surface)`, `var(--cyan)`, `var(--muted)`, `var(--ink)`, `var(--line)` for colors.
- Use `border-radius: 10px` for cards.
- Font sizes: 14px titles, 12px descriptions, 9-11px for metadata.

## Tab activation flow

```
User clicks tab button
  → activateTab(tabName)
    → sets activeTab
    → toggles .active class on tabs
    → toggles .active class + hidden on panels
    → updatePageHeading(tabName)  — reads pageMeta + I18N
    → configureGlobalFiltersForTab(tabName)  — disables/enables filters
    → if !tabLoaded[tabName]: loadActiveTab(false)
      → calls loader function from map
```

## Filter state management

- Reports tab disables ALL filters (`year`, `version`, `region`, `country`), hides Apply/Reset buttons.
- When leaving Reports: re-enables filters, restores buttons, removes executive option if present.
- The `applyFilters()` function clears `tabLoaded` for ALL tabs — this is fine because it forces a fresh load.

## Reports API (server.js)

```
GET /api/reports          → { reports: [{ name, title, description }] }
GET /api/reports/generate?name=X  → { report, title, description, columns, rows, row_count }
```

Reports are defined as SQL views in the REPORT_DEFINITIONS array at the top of server.js.

## Work Journal convention

Every change must log a Work Journal entry at the TOP of the journal section in AGENTS.md:

```markdown
### YYYY-MM-DD — Agent Name — `branch-name` (short description)
**Did:** What was built/changed.
**Why:** Business/product justification.
**Status:** ✅ test results, verification notes.
**Next:** What the next agent should pick up.
**Watch out:** Gotchas, limitations, things to be careful about.
```

## Definition of Done (from AGENTS.md)

- [ ] Full test gate green (new behaviour has a test)
- [ ] Docs updated (ARCHITECTURE.md, ROADMAP.md, relevant README, Agent.md)
- [ ] Task Board updated
- [ ] Work Journal entry at top
- [ ] No stale references / all internal doc links resolve
