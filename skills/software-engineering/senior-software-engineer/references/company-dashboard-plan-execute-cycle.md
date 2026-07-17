# Company Dashboard Plan → Execute → Push Cycle

## When to use this pattern

When Mohamed drops a set of ideas (especially from an image/screenshot) and says:
- "نفذ نقطة نقطه"
- "أعمل بلان لكل نقطة الأول"
- "ارفع لل main بعد ما تخلص كل نقطة"

## The pattern

### Phase 0: Ingest
1. If the source is an image → use **tesseract OCR** + **PIL color analysis** to extract text and identify completed/highlighted items
   - `tesseract image.jpg output -l ara+eng --psm 6`
   - Use numpy to find green pixels (completed) vs white/black (text)
2. Add extracted ideas to the **Task Board** with appropriate naming:
   - `I1`–`In` for new initiatives (Insight Engine items)
   - Follow existing naming convention if one exists
3. Commit the Task Board update and push to `main`

### Phase 1: Plan (per task)
For each task, present a concise plan covering:
- **Files affected** — every file that will change
- **Schema changes** — new tables, columns, views
- **API endpoints** — new routes, methods, what they return
- **UI changes** — new tabs, buttons, translations
- **Implementation steps** — ordered, verifiable
- Keep it in Arabic, structured tables, no code dumps
- Wait for approval before executing

### Phase 2: Implement
1. Start with schema/data layer first
2. Then backend (API endpoints)
3. Then frontend (UI tab, translations)
4. Wire everything together
5. Run the full test gate (all suites, not just one)

### Phase 3: Push
1. Commit with descriptive message
2. Push directly to `main` (no feature branches, no PRs)
3. Move task to Done on the Task Board with commit hash
4. Then move to next task

## Pitfalls

- **Do NOT implement before plan approval** — Mohamed wants to see the plan first
- **Don't skip the Task Board update** — every new idea gets a row before implementation
- **Don't use feature branches** — Mohamed explicitly wants everything on `main`
- **When vision/OCR fails**: tesseract from terminal works; execute_code sandbox doesn't have pytesseract
- **Arabic in plans**: keep it professional, structured, no English mixed in Arabic lines

## Task naming conventions

| Prefix | Meaning | Example |
|--------|---------|---------|
| `R` | Report/Feature task | R1, R5 |
| `D` | Infrastructure/Dev task | D1, D17 |
| `I` | Insight Engine initiative | I1–I7 |

## Example: I1 ingestion flow

```
Mohamed sends screenshot → 
OCR extracts 7 features with "Completed" badge (green) →
Added I1-I7 to Task Board (Ready column) →
Mohamed confirms: "نفذ نقطه نقطه" →
For each I:
  Present plan → get approval → implement → test gate → commit → push to main
```
