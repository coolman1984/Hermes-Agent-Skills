---
name: prototype-client-readiness-polish
description: Turn a working prototype into a presentable pilot-ready product for a
  friendly client demo.
tags: [prototype, client, demo, qa, polish, delivery]
title: Prototype Client Readiness Polish
category: software-development
---

# Prototype Client Readiness Polish

## When to use this skill

- A prototype works but needs to be shown to a non-technical client.
- You need to build trust, reduce setup friction, and make the value obvious.
- You want a repeatable demo script and artifacts the client can take away.

## The five deliverables

1. **No-visible-defects QA**
   - Run the product end-to-end in the demo language.
   - Fix any untranslated labels, console errors, or broken exports.
   - Take screenshots of the key screens.

2. **A demo script**
   - Write a narrative in the client's language.
   - Cover: input → extraction → flags → dashboard → reports → source defence.
   - Keep each section short enough to deliver in 30–60 seconds.
   - Add presenter notes and fallback paths if something breaks.

3. **Take-away artifacts**
   - One PDF report that looks professional when printed.
   - One Excel file with readable formatting.
   - One validation / source-confidence summary that defends the numbers.

4. **Source traceability**
   - Add a report that shows row counts, null checks, duplicates, and coverage.
   - Surface source metadata (database, generated time, row count) on every artifact.
   - Show how a challenged number can be traced back to its source.

5. **Scope statement**
   - Document what is supported and what is not yet guaranteed.
   - This protects both you and the client from unrealistic expectations.

## Demo script structure

```markdown
# سكريبت العرض التجريبي

## 1. ما الذي ترفعه
- File formats accepted.
- Where to place files.

## 2. ما الذي يستخرجه النظام
- Capture → Map → Validate → Load.

## 3. ما الذي يتم تحديده
- Validation report contents.

## 4. لوحة المعلومات
- Key tabs and what they answer.

## 5. التقارير المستخرجة
- Board pack contents.

## 6. كيف ندافع عن رقم واحد
- Source → row → validation status.
```

## Checklist before the demo

- [ ] Product starts from a clean state in under 60 seconds.
- [ ] Demo data is synthetic or anonymised.
- [ ] No console errors on load.
- [ ] Exported PDFs and Excel files open correctly on the client's machine.
- [ ] Demo script has been rehearsed once end-to-end.
- [ ] A "not yet supported" list is ready if asked.

## Pitfalls to avoid

- Do not demo with real client data unless explicitly authorised.
- Do not promise timelines for unsupported features during the demo.
- Do not skip the validation/source section; it is what builds trust.
- Do not change the visual design during the polish phase unless the owner asks.

## After the five deliverables: what comes next

The five deliverables are Phase 1 (pilot-ready polish).  The next phase
is typically a per-client import-run workspace (per-run folders,
backups, import history, rollback) — the smallest unit that lets a
second operator repeat the import from docs alone and defends every
number to source.  See
[`references/phase-progression-company-dashboard.md`](references/phase-progression-company-dashboard.md)
for a worked example and the pitfalls that surfaced.
