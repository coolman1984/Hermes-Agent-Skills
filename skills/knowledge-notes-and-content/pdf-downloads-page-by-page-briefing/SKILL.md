---
name: pdf-downloads-page-by-page-briefing
description: Read PDFs from Android/Termux download folders and produce page-by-page Arabic explanations, summaries, or study notes. Use when a user asks to read a PDF from Downloads/CMA folders and explain it in a structured way.
---

# PDF Downloads Page-by-Page Briefing

## Use this skill when
- The user asks to read a PDF from a mobile download folder.
- The file lives under `/sdcard/Download`, `/storage/emulated/0/Download`, or a subfolder like `CMA/`.
- The user wants a study-style explanation, page-by-page walkthrough, or exam-focused notes.

## Workflow
1. Find the actual file path.
   - Check common mobile paths first:
     - `/sdcard/Download`
     - `/storage/emulated/0/Download`
     - `/mnt/shared/Download`
     - `/root/Downloads` only if the mobile paths do not exist.
   - List the download folder contents and locate the exact subfolder/file name.
   - Be alert for duplicated folder names like `CMA`, `CMA P1 2025 Units`, or mixed case.

2. Verify the PDF is readable.
   - Use Python PDF extraction first (`pypdf` is usually enough).
   - Confirm the file exists and print page count.
   - Extract a small sample from the first pages before doing the full pass.

3. If text extraction works, read in chunks.
   - For long PDFs, extract pages in blocks instead of all at once.
   - Keep outputs manageable to avoid truncation.
   - Capture headings, definitions, formulas, and examples.

4. Produce the final explanation in Arabic first.
   - If the user is Arabic-first, explain page by page in simple Arabic.
   - Focus on meaning, not literal translation.
   - Highlight exam-relevant definitions, rules, comparisons, and formulas.

5. Keep the structure consistent.
   - Page number
   - Main idea
   - What it means in plain language
   - Important exam takeaway

6. If the user asks for a specific format, adapt.
   - Quick summary
   - Study notes
   - Q&A
   - Page-by-page explanation
   - Comparison table

## Practical extraction pattern
- Use Python with `pypdf` to read text from the PDF.
- If the PDF is image-only or text extraction is weak, fall back to OCR/vision tooling.
- For very long documents, fetch pages selectively and summarize per section.

## Pitfalls
- PDF text output can be truncated if you try to dump the whole file at once.
- Some files in Downloads may have spaces, parentheses, or Arabic characters in the name.
- Mobile download folders may exist in more than one path; check all common variants.
- Some PDFs are scans; text extraction may return little or nothing.

## Good output style
- Direct and simple.
- No filler.
- Arabic first.
- Keep technical terms in English where helpful.
- If the document is long, tell the user you’re chunking it and continue until complete.
