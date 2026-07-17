# Resources and Leads

| Library/spec | URL | Best for | Weakness |
|---|---|---|---|
| openpyxl | https://openpyxl.readthedocs.io/ | xlsx/xlsm structure | not xlsb/xls |
| pandas Excel | https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html | quick tabular reads | weak on report layout |
| PyMuPDF | https://pymupdf.readthedocs.io/ | fast PDF text/rendering | table semantics need help |
| pdfplumber | https://github.com/jsvine/pdfplumber | PDF tables/coordinates | layout tuning |
| pypdf | https://pypdf.readthedocs.io/ | split/metadata/forms | not best for tables |
| python-docx | https://python-docx.readthedocs.io/ | docx paragraphs/tables | legacy doc unsupported |
| Python email | https://docs.python.org/3/library/email.parser.html | eml/MIME | not Outlook msg |
| BeautifulSoup | https://www.crummy.com/software/BeautifulSoup/bs4/doc/ | HTML parse | no JS execution |
| Tesseract | https://tesseract-ocr.github.io/tessdoc/ | OCR incl Arabic language packs | quality depends on image |

Top traps: trusting extension; OCRing searchable PDFs; dropping attachments; ignoring hidden sheets; assuming first Excel row is header; no provenance; no counts; batch crash on corrupt file; Arabic encoding loss; treating extraction as analysis.

Usage image: detect, preserve structure, validate, and only then normalize/load.
