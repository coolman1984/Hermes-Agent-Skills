# Docling Installation on aarch64 PRoot (2026-06-27)

## Summary

Docling (IBM's document parser) was installed on the system, but the full pipeline requires heavy ML dependencies (torch, transformers, docling-ibm-models, torchvision) that make imports hang or timeout on aarch64 PRoot environments.

## What works

- `docling-core` (v2.85.0) — imports fine, provides `DoclingDocument` type system
- `docling-parse` (v7.0.0) — PDF parsing backend, imports fine
- `docling-slim` (v2.107.0) — the lightweight package without ML models
- Individual backends: PDF (docling-parse), Markdown (marko), DOCX (python-docx), PPTX (python-pptx), LaTeX (pylatexenc)

## What hangs/timeout

- `from docling.document_converter import DocumentConverter` — this triggers the full pipeline import which loads:
  - `torch` + `torchvision` (installed but slow to import on PRoot)
  - `transformers` (AutoProcessor fails with torchvision compatibility issues)
  - `docling_ibm_models` (installed, heavy)
  - Granite Vision model (requires transformers AutoModelForImageTextToText)

The import hangs for 30+ seconds and may timeout.

## Dependencies installed

```
docling-core==2.85.0
docling-slim==2.107.0
docling-parse==7.0.0
docling-ibm-models==3.13.3
torch==2.12.1+cpu (from pytorch CPU wheel)
torchvision==0.27.1
transformers==5.12.1
pylatexenc==2.10
marko==2.2.3
python-pptx==1.0.2
python-docx (already present)
Rtree==1.4.1
pymupdf==1.27.2.3
```

## Practical approach for aarch64

1. Use `docling-core` types for document representation
2. Use Company-Dashboard's existing extractors (pdfplumber + tesseract) for actual PDF/DOCX parsing — they work reliably
3. Use `docling-core`'s `DoclingDocument` as the unified output format
4. Only use full Docling on a proper x86_64 server with GPU when available

## GBrain status (already installed)

```
GBrain 0.9.0 at /root/.local/bin/gbrain
3 pages, keyword search working
Embeddings not yet generated (run: gbrain embed refresh)
```

## Hindsight MCP status

```
hindsight-mcp@1.1.3 installed globally
Requires HINDSIGHT_API_TOKEN (hosted cloud service)
Not a local-first tool — needs account on hindsight-ai.com
```

## Lesson

On aarch64 PRoot/Termux:
- Docling full pipeline is too heavy for practical use
- docling-core works fine for type handling
- GBrain is local and works
- Hindsight is cloud-only and needs an API token
- Prefer existing Company-Dashboard extractors for actual file parsing