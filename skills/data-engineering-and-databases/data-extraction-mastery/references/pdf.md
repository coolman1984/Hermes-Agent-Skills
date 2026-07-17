# PDF Text and Tables

Use PyMuPDF for fast text, page images, metadata, and rendering. Use pdfplumber for tables and coordinate-aware extraction. Use pypdf for splitting/metadata/forms. Test whether text exists before OCR.

Sources: https://pymupdf.readthedocs.io/ ; https://github.com/jsvine/pdfplumber ; https://pypdf.readthedocs.io/

Hard cases: multi-column pages, spanning tables, rotated pages, password protection, forms, image-only pages.

When to use: searchable PDFs and tables. When it fails: scanned images, bad layout, table borders missing. Watch: page-by-page provenance.

Usage image: detect, preserve structure, validate, and only then normalize/load.
