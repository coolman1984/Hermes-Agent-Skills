#!/usr/bin/env python3
"""Production QA and finishing helper for PDF book builds.

Runs structural checks, optional PDF/A validation, linearization, compression
variants, and page rendering/contact sheet for visual review.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], timeout: int = 240) -> dict:
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    return {
        'cmd': cmd,
        'returncode': proc.returncode,
        'stdout': proc.stdout[-8000:],
        'stderr': proc.stderr[-8000:],
    }


def need(name: str) -> str | None:
    return shutil.which(name)


def ghostscript_variant(src: Path, dst: Path, setting: str) -> dict:
    return run([
        'gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.7',
        f'-dPDFSETTINGS=/{setting}', '-dNOPAUSE', '-dQUIET', '-dBATCH',
        f'-sOutputFile={dst}', str(src),
    ], timeout=600)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('pdf')
    parser.add_argument('--out', default=None)
    parser.add_argument('--pdfa', action='store_true', help='Run veraPDF validation. This is expected to fail unless the PDF is authored as PDF/A.')
    parser.add_argument('--render', action='store_true', help='Render pages and contact sheet using render_review.py')
    args = parser.parse_args()

    pdf = Path(args.pdf).expanduser().resolve()
    out_dir = Path(args.out).expanduser().resolve() if args.out else pdf.with_suffix('').parent / (pdf.stem + '-finish')
    out_dir.mkdir(parents=True, exist_ok=True)

    report = {
        'input': str(pdf),
        'exists': pdf.exists(),
        'size': pdf.stat().st_size if pdf.exists() else 0,
        'tools': {name: need(name) for name in ['qpdf', 'gs', 'verapdf', 'tesseract', 'pdftoppm', 'prince', 'typst']},
        'checks': {},
        'outputs': {},
    }

    if not pdf.exists():
        (out_dir / 'finish-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 2

    if report['tools']['qpdf']:
        report['checks']['qpdf_check'] = run(['qpdf', '--check', str(pdf)])
        linearized = out_dir / (pdf.stem + '-linearized.pdf')
        report['checks']['qpdf_linearize'] = run(['qpdf', '--linearize', str(pdf), str(linearized)])
        if linearized.exists():
            report['outputs']['linearized'] = str(linearized)

    if report['tools']['verapdf'] and args.pdfa:
        report['checks']['verapdf'] = run(['verapdf', '--format', 'text', str(pdf)], timeout=600)

    if report['tools']['gs']:
        for setting in ['ebook', 'printer', 'prepress']:
            dst = out_dir / f'{pdf.stem}-{setting}.pdf'
            report['checks'][f'ghostscript_{setting}'] = ghostscript_variant(pdf, dst, setting)
            if dst.exists():
                report['outputs'][setting] = str(dst)

    if args.render:
        helper = Path(__file__).with_name('render_review.py')
        if helper.exists():
            render_dir = out_dir / 'visual-review'
            report['checks']['render_review'] = run([sys.executable, str(helper), str(pdf), '--out', str(render_dir)], timeout=600)
            if (render_dir / 'contact-sheet.png').exists():
                report['outputs']['contact_sheet'] = str(render_dir / 'contact-sheet.png')

    report_path = out_dir / 'finish-report.json'
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'report': str(report_path), 'outputs': report['outputs'], 'qpdf_ok': report.get('checks', {}).get('qpdf_check', {}).get('returncode')}, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
