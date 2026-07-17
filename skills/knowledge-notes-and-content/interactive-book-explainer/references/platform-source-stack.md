# Interactive Book Platform Source Stack

Session learning from Mohamed's platform planning: when building the book platform, do not treat the interactive explainer page as an isolated artifact. It sits inside a richer product system:

- Website and UI quality: use Vercel agent-skills / web-design-guidelines as a reference for accessibility, UX review, and modern web quality.
- Document workflows: use Anthropic skills as reference material for PDF, XLSX, DOCX, and PPTX handling.
- PDF quality: use OpenAI PDF skill patterns for visual rendering checks with Poppler-style page previews, plus the local professional PDF book factory when producing final books.
- Office execution: evaluate OfficeCLI before adoption for DOCX/XLSX/PPTX automation; treat binaries as install-risk and vet first.
- Discovery: use large skill indexes such as VoltAgent only for discovery, not direct trust or installation.
- Video: video-db and ffmpeg-analysis skills are later-stage options for lecture/video workflows, not phase-one dependencies.

Operating rule:

1. Build one local book-platform prototype first.
2. Include homepage, book page, interactive chapter page, and resource page.
3. Pair every chapter idea with potential deliverables: interactive page, PDF section, XLSX exercise, DOCX solution/template.
4. Do not install external skills or binaries before source vetting.
5. Convert useful outside patterns into Mohamed-specific local skills/workflows instead of blindly copying upstream.

Vault references:

- `/root/Documents/Obsidian Vault/Knowledge Base/Agent Skills and Tools for Interactive Book Platform.md`
- `/root/Documents/Obsidian Vault/Knowledge Base/Interactive Book Platform - Source Vetting Report.md`
- `/root/Documents/Obsidian Vault/Knowledge Base/PDF-Book-Production-Reference-Links.md`
