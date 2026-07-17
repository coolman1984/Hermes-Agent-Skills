#!/usr/bin/env python3
"""Render a PDF into per-page PNGs plus a contact sheet for visual QA."""
from __future__ import annotations

import argparse
import math
from pathlib import Path
import fitz
from PIL import Image, ImageDraw


def render(pdf_path: Path, out_dir: Path, zoom: float = 1.4, thumb_w: int = 220) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(pdf_path))
    page_images = []
    for i, page in enumerate(doc, start=1):
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
        img_path = out_dir / f'page-{i:03d}.png'
        pix.save(str(img_path))
        page_images.append(img_path)

    thumbs = []
    for img_path in page_images:
        img = Image.open(img_path).convert('RGB')
        ratio = img.height / img.width
        img.thumbnail((thumb_w, int(thumb_w * ratio)))
        thumbs.append(img.copy())

    cols = min(5, max(1, len(thumbs)))
    rows = math.ceil(len(thumbs) / cols) if thumbs else 1
    cell_w = thumb_w + 40
    cell_h = int(thumb_w * 1.45) + 45
    sheet = Image.new('RGB', (cols * cell_w, rows * cell_h), 'white')
    draw = ImageDraw.Draw(sheet)
    for idx, img in enumerate(thumbs, start=1):
        col = (idx - 1) % cols
        row = (idx - 1) // cols
        x = col * cell_w + 20
        y = row * cell_h + 20
        sheet.paste(img, (x, y))
        draw.text((x, y + img.height + 8), f'page {idx}', fill=(0, 0, 0))

    sheet_path = out_dir / 'contact-sheet.png'
    sheet.save(sheet_path)
    print({'pdf': str(pdf_path), 'pages': doc.page_count, 'out_dir': str(out_dir), 'contact_sheet': str(sheet_path)})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('pdf')
    parser.add_argument('--out', default=None)
    parser.add_argument('--zoom', type=float, default=1.4)
    args = parser.parse_args()
    pdf = Path(args.pdf).expanduser().resolve()
    out = Path(args.out).expanduser().resolve() if args.out else pdf.with_suffix('').parent / (pdf.stem + '-review')
    render(pdf, out, zoom=args.zoom)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
