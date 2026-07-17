#!/usr/bin/env python3
import argparse, json, subprocess, sys
from pathlib import Path

def main(sources,out):
    out=Path(out); out.mkdir(parents=True,exist_ok=True); fetch=Path(__file__).with_name('fetch.py'); rows=[]
    for i,line in enumerate(Path(sources).read_text().splitlines(),1):
        src=line.strip()
        if not src or src.startswith('#'): continue
        target=out/f'source_{i}'; target.mkdir(exist_ok=True)
        try:
            if src.startswith('file://'):
                p=Path(src[7:]); raw=target/p.name; raw.write_bytes(p.read_bytes()); rows.append({'source':src,'status':'ok','cache_path':str(raw),'legal_basis':'user-provided local file'})
            elif src.startswith('http'):
                subprocess.check_output([sys.executable,str(fetch),src,'--out',str(target)],stderr=subprocess.STDOUT,text=True); rows.append({'source':src,'status':'ok','cache_dir':str(target)})
            else: raise ValueError('unsupported scheme')
        except Exception as e: rows.append({'source':src,'status':'needs_review','error':str(e)[:500]})
    (out/'run_manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'sources':len(rows),'ok':sum(r['status']=='ok' for r in rows),'needs_review':sum(r['status']=='needs_review' for r in rows),'manifest':str(out/'run_manifest.json')},indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('sources'); ap.add_argument('--out',required=True); a=ap.parse_args(); main(a.sources,a.out)
