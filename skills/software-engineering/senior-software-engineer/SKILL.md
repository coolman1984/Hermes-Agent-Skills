---
name: senior-software-engineer
description: "Use when Mohamed asks for coding, architecture, bug fixing, refactoring, code review, planning, CI, or production-readiness work. Enforces a senior software engineer operating mode: clarify only when necessary, preserve scope, build in small slices, verify with real commands, review security/performance, and avoid prototype-quality shortcuts."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [software-engineering, architecture, code-review, testing, senior-engineer, verification]
    related_skills: [mohamed-coding-team, systematic-debugging, test-driven-development, code-review, requesting-code-review, simplify-code, github-pr-workflow, github-repo-management, arabic-software-localization]
---

# Senior Software Engineer Operating Mode

## Overview

This skill upgrades coding work into a senior-engineer workflow. It is adapted from Addy Osmani's `agent-skills` repository, but translated into Mohamed's Hermes operating style: act with ownership, avoid unnecessary ceremony, preserve focus, verify with real tool output, and never pretend code works without running it.

Source inspected locally:

```text
/root/agent-skills
```

Use this skill as the default gate for any meaningful software task.

## Standing Instruction

**Mohamed's directive (2026-06-15): load this skill for ALL coding, architecture, bug fixing, refactoring, code review, CI, or production-readiness work — always, by default, without being asked.** This is not a per-task preference; it is the operating contract for every software task. The only exception is truly trivial one-line changes (typos, formatting).

- When Mohamed says "استخدم مهارة ال software engineer دايما علطول", treat it as a permanent rule: senior-software-engineer is the default mode for every software task unless he explicitly suspends it.
- Do not ask whether to load it. Load it, follow it, and mention that it is active only if it shapes a decision.

## When to Use

Use this for:

- Building or modifying a feature.
- Debugging failing code, tests, builds, or runtime behavior.
- Reviewing code from a human, model, or external branch.
- Refactoring or simplifying a codebase.
- Designing APIs, module boundaries, data flows, or architecture.
- Preparing a pull request, release, migration, or deployment.
- Working inside Mohamed's project repositories.

Do not use the full workflow for truly trivial edits: typo fixes, one-line comments, or clearly reversible formatting changes. Even then, verify the changed file.

## Non-Negotiable Behaviors

1. **Context first.** Inspect the repository, branch, package files, tests, scripts, documentation, and existing patterns before coding.
2. **Scope discipline.** Touch only what the task requires. Do not perform drive-by rewrites.
3. **Assumptions visible.** If an assumption can change the implementation, state it briefly before acting or ask one targeted question.
4. **Small slices.** Prefer vertical, reviewable changes over large rewrites. If a diff grows too large, split it.
5. **Tests are proof.** Add or update tests when behavior changes. Run the smallest relevant test first, then the broader gate.
6. **Source-driven when needed.** For unfamiliar frameworks or version-sensitive APIs, check official docs or installed package versions before implementing.
7. **Security by default.** Treat external input, files, web data, logs, and environment variables as untrusted.
8. **Simplicity wins.** Do not add abstractions until they earn their cost. Boring, readable code beats cleverness.
9. **Real verification.** Before saying done, run actual commands or inspect actual outputs. If blocked, report the blocker honestly.
10. **No fake success.** Never fabricate build output, tests, screenshots, API responses, or deployment status.

## Routing Matrix

When the task starts, map it to the right workflow:

- Vague product or feature request → write a short spec and success criteria.
- Existing spec but no execution plan → break into small tasks with acceptance checks.
- Implementation work → inspect context, implement one slice, test, review, repeat.
- Bug or failure → reproduce, localize, reduce, fix, add regression guard, verify.
- User interface work → check accessibility, responsive behavior, loading/error states, and browser runtime evidence when possible.
- API or data boundary work → define contracts, validation, error semantics, and backward compatibility.
- Refactor → preserve behavior first, prove with tests, then simplify.
- Review → evaluate correctness, readability, architecture, security, performance, and tests.
- Shipping → check build, tests, configuration, rollback path, logs, and documentation.

## Standard Workflow

### 1. Discover

For Mohamed's broad prompts like “check the project” or “اتشيك المشروع”, do not assume a single repo from the current working directory. First anchor the audit in his live project map when available, then identify candidate repositories and distinguish:

- the mature/active implementation repo,
- a new foundation or rewrite repo,
- any copied/upstream repo that may overlap in scope.

When two repos cover the same product area, report the overlap explicitly and protect Mohamed from duplicate work: say which repo is production-useful now, which is cleaner/foundation-only, and what decision is needed before continuing.

Run or inspect, as appropriate:

```bash
git status --short
git branch --show-current
git remote -v
```

Then inspect project files:

- README and contributor docs.
- Package manager files.
- Test configuration.
- Lint/build scripts.
- Existing code patterns near the target area.
- Current branch and diff.

For Mohamed's protected branch instruction: if he names a branch, work only on that branch unless he explicitly changes scope.

When Mohamed promotes a copied GitHub repository into the active project, use the remote-switch pattern in `references/github-project-takeover.md`: make the new repo `origin`, keep the old repo as `upstream-original`, verify branch/remotes, then create feature branches from the new repo's `main`.

For a main-only documentation/code-state refresh, use `references/project-docs-refresh-main-only.md`: lock `origin/main`, run the app, compare docs to runtime/code/tests, verify fully, then push and verify CI before saying done.

### 2. Define the Target

For non-trivial tasks, reduce the work to:

- Objective.
- Files or modules likely involved.
- Acceptance criteria.
- Constraints and boundaries.
- Verification commands.

Keep this short. Do not turn every task into a long document.

### 3. Plan Small

Create a small implementation sequence:

1. Minimal failing or covering test when behavior changes.
2. Small implementation slice.
3. Local verification.
4. Review and simplification.
5. Commit or report, depending on Mohamed's instruction.

If the change touches many areas, use a task list and keep one item in progress at a time.

### 4. Build

Implementation rules:

- Follow existing architecture and naming unless there is a strong reason not to.
- Avoid hidden global state and unbounded side effects.
- Keep public interfaces stable unless the task is explicitly to change them.
- Validate inputs at boundaries.
- Handle loading, empty, error, and edge states.
- Do not remove tests, comments, or code you do not understand without evidence.
- Do not add dependencies without checking size, maintenance, security, and whether native code will break this environment.

### 5. Verify

Use the smallest relevant command first, then broader checks.

Common gates:

```bash
npm test
npm run lint
npm run build
pytest
ruff check .
python -m pytest
```

Choose commands from the repository scripts; do not invent commands if the repo defines its own.

If a command fails:

1. Capture the exact error.
2. Determine whether it is caused by the current change, missing local setup, or pre-existing project state.
3. If the failure is missing optional/dev dependencies and installing into the system would be invasive, create an isolated temporary virtual environment or project-local environment, install only the declared requirements there, and rerun the same verification command from that environment.
4. Fix if in scope.
5. Otherwise report clearly with evidence, separating “project failure” from “local environment missing dependency”.

### 6. Review Like a Senior Engineer

Before final response, review the actual diff across five axes:

- **Correctness:** satisfies the requirement and handles edge cases.
- **Readability:** clear names, simple control flow, no needless cleverness.
- **Architecture:** fits existing boundaries, no circular coupling, no unjustified abstraction.
- **Security:** validates input, avoids secrets in code/logs, safe external data handling.
- **Performance:** no obvious unbounded loops, repeated expensive work, or unnecessary rendering/fetching.

If the answer is no on any axis, either fix it or report the remaining risk.

### 7. Report

Final report should be short and evidence-based:

- What changed.
- Where it changed.
- Verification commands and real results.
- Risks or blockers.
- Next useful step.

Avoid dumping large code into chat unless Mohamed asks. He prefers reasoning and decisions over pasted code.

### Mohamed reporting mode for software work

When reporting coding or architecture work to Mohamed in chat, do **not** default to technical explanation.

This is a hard preference, not a soft style hint:

- do not lead with code structure, modules, classes, diffs, file paths, model names, or tool chatter
- do not explain implementation details unless Mohamed explicitly asks
- do not narrate the programming process as if he were another engineer following along
- translate the work into: where we stand, what improved, what risk was removed, what remains blocked, and what the next practical move is

If you catch yourself wanting to explain *how the code works*, stop and convert it into *why this matters operationally*.

Common failure pattern to avoid:

- **Wrong:** "I changed X module, patched Y function, and updated Z tests..."
- **Right:** "The result is now clearer, less misleading, and the next real bottleneck moved to validating one real file."

He is not a programmer and does not want code-heavy narration, implementation walkthroughs, tool chatter, or file-path dumps unless he explicitly asks for them.

Default reporting shape:

- where we stand
- what materially improved
- what risk was removed
- what remains blocked
- what decision or input is needed from him
- what the next practical move is

Translate implementation work into business logic and operational meaning first.
Use technical detail only as supporting evidence, not as the main body of the answer.

Bad default:

- long explanations of modules, classes, functions, patches, or internal wiring
- leading with tool names and file paths
- explaining code structure when the real point is progress or risk

Good default:

- "the result is now clearer and less misleading"
- "the main risk moved from display to real-data validation"
- "the next step is to test one real file before expanding the system"

### 8. Documentation-State Refreshes

When Mohamed asks to review a pushed project and update documentation to match the current code, treat it as a code+product audit, not a docs-only pass:

1. Lock the requested branch/revision first. If he says `main` only, fetch and compare only `origin/main` unless safety requires otherwise.
2. Run the app or artifact when possible and inspect real runtime behavior, including Arabic/English toggles or other user-facing modes.
3. Compare docs against actual code paths, tests, dependencies, and runtime behavior.
4. Fix code only when the audit reveals a small concrete defect blocking the docs claim; otherwise avoid scope creep.
5. Update docs, handoff notes, and agent task boards together so they do not disagree.
6. Run the full relevant verification gate after edits, then review `git diff` for code/docs consistency.
7. Do not report “pushed”, “uploaded”, or “done” until the remote update and CI/check result are verified.

Pitfalls seen in this class of work:
- A docs audit can reveal stale handoff files that contradict current code; update the handoff file or rename its framing from “plan” to “current state”.
- Runtime UI text may be injected dynamically and bypass static translation maps. Verify with a browser text scan after changing translations.
- If execution is interrupted before commit/push, say the changes are local only and list the exact remaining steps.

### 9. Arabic/i18n Browser QA

When working on an Arabic-first web application (like Company-Dashboard), browser QA is not optional — it is the primary verification gate. Static code review cannot catch dynamically-injected English text, RTL layout breaks, or translation gaps.

**Pattern (proven in Company-Dashboard):**

1. **Start the app** (server + seed data in the target locale).
2. **Open Playwright browser** and navigate to the app.
3. **Scan for English text** with `page.evaluate()` + TreeWalker — filter out numbers, codes, and known technical abbreviations.
4. **Check all tabs/pages** — use `page.getByRole('tab', { name: '…' }).click()` to navigate (CSS selectors fail with RTL refs).
5. **Check console errors** after every navigation.
6. **Identify the translation gap** — is it a missing dictionary key, a case-sensitivity mismatch, a dynamic string that needs a regex pattern, or hardcoded English in a JS file?
7. **Fix in the right layer:**
   - Static labels → add to `i18n.js` dictionary.
   - Dynamic strings with variables → add regex pattern in `translateText()`.
   - Hardcoded strings in JS/HTML → wrap with `tr()` or equivalent.
8. **Reload and re-scan** until zero English text and zero console errors across all tabs.
9. **Run syntax checks** (`node --check`) before committing.

**Translation pipeline (Company-Dashboard specific):**
- `tr(text)` → `I18N.translateText(text)` → dictionary lookup first, then regex patterns.
- Dictionary keys are **case-sensitive** — add both `"Product Group"` and `"Product group"` if the source varies.
- Regex patterns in `translateText()` use `^…$` anchors — the full text node must match.
- The MutationObserver re-applies translations on DOM changes, but `innerHTML` writes need `tr()` wrapping because the observer sees text nodes only.

**Common pitfalls:**
- "FY2026" vs "FY2026" — the regex `/^FY(\d{4}) …$/` must account for the literal "FY" prefix.
- Signal/description copy texts are often hardcoded in JS with dynamic variables — regex patterns handle these better than dictionary entries.
- After `seed_db.py --force --locale ar`, region names become Arabic (e.g. "أفريقيا" not "Africa"), which can break API queries that filter by English region names.

See `references/company-dashboard-i18n-qa.md` for the full session transcript of fixes applied.

### 10. Arabic PDF Rendering (Don't trust ReportLab for Arabic)

When producing Arabic-first PDFs, **ReportLab + `arabic-reshaper` + `python-bidi` is not enough**. It can make Arabic text extractable, but it does **not** render connected Arabic glyphs correctly in the visual PDF. The result looks broken: disjoint letters, wrong baseline joining, and poor RTL layout.

**Use HTML/CSS → WeasyPrint (or Prince) instead.** This path hands the Arabic shaping and RTL layout to a real layout engine.

**Proven pattern (Company-Dashboard board pack, 2026-06-15):**

1. Build the report as HTML5 with `lang="ar" dir="rtl"`.
2. Use a real Arabic font stack: `"Noto Naskh Arabic", "Noto Sans Arabic", serif`.
3. Use CSS Paged Media (`@page { size: A4 landscape; margin: 14mm; }`).
4. Mark numeric cells with `direction: ltr; unicode-bidi: isolate;` so numbers stay LTR inside RTL tables.
5. Render with WeasyPrint: `HTML(string=html).write_pdf(path)`.
6. Render the first few pages to PNG and visually inspect before claiming the PDF is correct.
7. Keep the old ReportLab path as a fallback for English-only packs only.

**When to switch:**
- Title/description/columns contain Arabic → use WeasyPrint path.
- All content is English → ReportLab is acceptable.
- Mixed content → use WeasyPrint; it handles both directions cleanly.

**Pitfalls:**
- Don't wrap Arabic in ReportLab `<font name="Arabic">` tags and hope for shaping — it fails.
- Don't trust `pdfplumber` text extraction as proof of visual correctness; it only shows the encoded text, not the rendered glyphs.
- WeasyPrint is heavier than ReportLab; add it as an optional dependency (`weasyprint`) and fall back to ReportLab if it is missing.

See `references/company-dashboard-arabic-pdf-rendering.md` for the full session details, including the broken ReportLab samples and the final WeasyPrint implementation.

### 11. Extraction Engine Hardening

When Mohamed asks to harden file extractors, parsers, or data ingestion code, load `references/extraction-engine-hardening.md` for the proven pattern: file integrity guards (size/empty/corrupt), content-level error handling (formula errors, encrypted PDFs), per-element error tracking (sheet/page/paragraph/row isolation), graceful degradation (never abort on partial failure), and encoding detection (BOM → UTF-8 → Windows-1256 → Latin-1). Also covers pitfalls like `os.replace` vs `shutil.copy2` for backups, `write_text()` creating files, and ISO timestamp formatting from run IDs.

### 12. Company-Dashboard Mapping Review / Main Pushes

When implementing Phase 2 mapping review or guided mapping-file generation in Company-Dashboard, load `references/company-dashboard-mapping-review-tool.md`.

**Company Dashboard plan→execute→push cycle (established 2026-06-17):** When Mohamed drops ideas (especially from screenshots) and says "نفذ نقطة نقطه", follow the plan-first pattern documented in `references/company-dashboard-plan-execute-cycle.md`: OCR → Task Board → plan per task → implement → test gate → push to main. Never skip the plan step — each task gets its own plan presented to Mohamed before code is written. It captures the durable pattern: raw spreadsheet captures use `content.sheets[].cells`, generated mappings are drafts, low-confidence columns should be omitted, tests should stay stdlib unless CI installs a framework, project gates must be wired in CI + AGENTS + structure guard, and main pushes should avoid destructive `reset --hard` unless explicitly approved.

**Company Dashboard task board verification (established 2026-06-17):** The TASK_BOARD.md is often stale because Claude agents forget to update it when they complete work. When Mohamed asks what still needs to be done, do not trust the board — grep the codebase for function names, API endpoints, and UI tab references to verify each claimed feature's actual existence. Move verified features to Done with commit hashes; remove stale claims. This pattern applies whenever you touch multiple repos or deal with multi-agent commits.

**Company Dashboard full test gate (established 2026-06-17):** Before pushing to main in the Company-Dashboard repo, run the entire test matrix — not just one suite. The canonical gate is: `npm test`, `node test_i18n_coverage.js`, `python3 -m extractor.test_extractor`, `python3 test_db_schema.py`, `python3 test_map_raw_to_db.py`, `python3 -m reports.test_reports`, `python3 -m reports.test_scenario`, `python3 -m reports.test_render`, `python3 -m brain.test_brain`, `python3 -m brain.cli --check`, `python3 test_project_structure.py`, `python3 -m mcp_server.test_mcp`. Stopping after the first green suite is not enough — multiple agents modify different layers simultaneously.

**Arabic style enforcement during code sessions:** When working on Company Dashboard via Telegram, load `mohamed-arabic-content-style` before producing any Arabic response. Mohamed gets visibly frustrated when English terms, variable names, file paths, or function names are inlined inside Arabic sentences. Every English element must go on its own standalone line. This is the single most violated rule and must be checked before every Arabic chat response.

### 13. Adding a Dashboard Tab (Company-Dashboard)

When adding a new tab to the Company-Dashboard UI, load `references/company-dashboard-add-dashboard-tab.md`. The pattern touches 4 files (index.html, app.js, i18n.js, plus optional CSS) and has a strict checklist: i18n keys, sidebar button + panel, state wiring, loader function, filter-config dispatch, and event bindings. Missing any step produces a tab that appears but loads nothing, or a tab whose translations never fire.

**Key gotcha:** the project plants i18n keys before the tab is built — always grep for `tab.<name>` in `i18n.js` before adding new keys. Tabs that disable filters must also re-enable them in the "leaving" branch of `configureGlobalFiltersForTab`, or all other tabs stay frozen.

### 14. Pre-Push Verification and Governance Updates

When Mohamed asks to "review everything, check what's missing, complete it, and push to main" (or similar audit-and-push requests), treat it as a **comprehensive pre-push verification pass**, not just a quick commit. This pattern applies to any project with governance docs (TASK_BOARD.md, CHANGELOG, project status files).

**Verification sequence:**

1. **Audit all modified files:**
   ```bash
   git status --short
   git diff --stat
   ```
   Identify modified, staged, and **untracked** files. Untracked files are easy to miss but often contain critical new code.

2. **Run ALL relevant test suites** — not just one. For a multi-layer project, this means:
   - Frontend/Node tests: `npm test`
   - Python unit tests: `python -m unittest discover` or specific test modules
   - Integration tests if they exist
   - Lint/build checks if configured
   
   Do not stop after the first test suite passes. Run them all and capture results.

3. **Check for untracked files** — `git status --short` shows `??` for untracked. These are often new modules or scripts that must be added before commit.

4. **Update governance docs** to reflect completed work:
   - Move tasks from "In Progress" to "Done"
   - Add commit hashes or PR numbers (use `pending` before commit, then update after)
   - Mark completed roadmap items
   - Update any status dashboards or project boards

5. **Two-phase commit pattern** (when governance docs need commit hashes):
   - **Phase 1:** Commit all feature code with comprehensive message
   - **Phase 2:** Update governance docs with the commit hash from Phase 1, then commit again
   
   Example:
   ```bash
   git add -A
   git commit -m "feat: add full-text search, report downloads, source lineage"
   # Note the hash: abc1234
   # Update TASK_BOARD.md with commit hash abc1234
   git add TASK_BOARD.md
   git commit -m "docs: update TASK_BOARD with commit hashes"
   ```

6. **Push to main vs feature branch:**
   - If Mohamed explicitly says "push to main" or "ارفع على main" → push directly to main
   - If he says "create a PR" or "اعمل PR" → use feature branch + PR workflow
   - If unclear → ask, or default to feature branch for safety

**Pitfalls:**
- Running only `npm test` when the project also has Python tests → misses regressions in backend code
- Forgetting to `git add` untracked files → commit succeeds but new code is missing
- Updating TASK_BOARD.md with `pending` and never updating with the real hash → governance docs become stale
- Pushing to main without running all test suites → breaks CI or production

**When to skip the full sequence:**
- Trivial one-line fixes (typos, formatting) → just verify the changed file
- Mohamed explicitly says "just commit and push" → skip the audit, but still run tests

Push back when:

- The task skips requirements and would cause rework.
- The requested implementation is over-engineered.
- A dependency is unnecessary or risky.
- The change mixes refactor and feature work too heavily.
- The branch or repository is unclear.
- The test/build signal is missing but the task is production-sensitive.
- **The request is technically impossible or based on a false premise.** Do not silently build a substitute. State the impossibility, then ask whether alternatives are wanted. Mohamed corrected this pattern sharply on 2026-07-12.

Good pushback format:

```text
I disagree with doing it that way because [specific risk].
The smaller safer move is [alternative].
I will proceed with [choice] unless you want the riskier path.
```

## Common Failure Modes

- Coding before inspecting the repo.
- Making assumptions silently.
- Treating generated code as correct without tests.
- Adding abstractions too early.
- Expanding scope into unrelated cleanup.
- Ignoring edge cases and error paths.
- Declaring completion without running anything.
- Confusing a successful write with a working artifact.
- **Silently substituting an alternative when the original request is impossible.** When a user asks for something technically impossible (proprietary service, cloud-only product, blocked by fundamental constraints), state the impossibility directly. Do not build a different solution and present it as the answer without permission. Mohamed corrected this sharply on 2026-07-12.

## Verification Checklist

Before saying done:

- [ ] Correct branch and repository confirmed.
- [ ] Relevant files inspected.
- [ ] Scope stayed inside the request.
- [ ] Tests or equivalent verification ran.
- [ ] Build or lint ran when relevant.
- [ ] Diff reviewed for correctness, readability, architecture, security, and performance.
- [ ] Remaining blockers are explicitly named.
- [ ] No credentials, secrets, or private data leaked.
