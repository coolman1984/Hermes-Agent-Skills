# Documents

Use python-docx for docx/docm/dotx paragraphs and tables. It reads the zipped XML structure and handles tables better than plain text dumps. Legacy doc should go through LibreOffice headless or antiword when installed; RTF/TXT/MD/HTML use format-specific plain parsers.

Source: https://python-docx.readthedocs.io/

Preserve structure: paragraph order, table rows/cells, headings/styles, headers/footers where relevant, image placeholders.

When to use: contracts, reports, table-heavy Word docs. When it fails: tracked changes complexity, legacy binary doc without converter, embedded objects.

Usage image: detect, preserve structure, validate, and only then normalize/load.
