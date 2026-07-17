#!/usr/bin/env python3
import argparse, json, mimetypes, subprocess, sys
from pathlib import Path

def signature(path):
    b=Path(path).read_bytes()[:8]
    if b.startswith(b'%PDF'): return 'pdf'
    if b.startswith(b'PK\x03\x04'): return 'zip-office'
    if b.startswith(b'\xd0\xcf\x11\xe0'): return 'ole'
    if b.startswith((b'From ', b'MIME')): return 'email'
    return 'text-or-binary'

def route(path):
    p=Path(path); ext=p.suffix.lower(); sig=signature(p)
    if ext in ['.xlsx','.xlsm','.xltx','.xltm','.csv','.tsv'] or (sig=='zip-office' and ext in ['.xlsm','.xlsx']): return 'excel'
    if ext=='.pdf' or sig=='pdf': return 'pdf'
    if ext in ['.eml','.msg'] or sig=='email': return 'email'
    if ext in ['.html','.htm','.xml','.json','.jsonl','.txt','.md','.rtf','.docx']: return 'webtext'
    return 'unknown'
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('file'); ap.add_argument('--out', default='/tmp/extracted')
    a=ap.parse_args(); print(json.dumps({'file':a.file,'signature':signature(a.file),'route':route(a.file)}))
