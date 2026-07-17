#!/usr/bin/env python3
import argparse, json, subprocess, sys, datetime
from pathlib import Path

def batch(sources,out):
    out=Path(out); out.mkdir(parents=True,exist_ok=True); script=Path(__file__).with_name('fetch_url.py'); rows=[]
    for i,line in enumerate(Path(sources).read_text().splitlines(), start=1):
        src=line.strip()
        if not src or src.startswith('#'): continue
        target=out/f'source_{i}'; target.mkdir(exist_ok=True)
        try:
            if src.startswith('file://'):
                p=Path(src[7:]); raw=target/p.name; raw.write_bytes(p.read_bytes()); rows.append({'source':src,'status':'ok','cache_path':str(raw),'bytes':raw.stat().st_size})
            elif src.startswith('http'):
                subprocess.check_output([sys.executable,str(script),src,'--out',str(target)],text=True,stderr=subprocess.STDOUT); rows.append({'source':src,'status':'ok','cache_dir':str(target)})
            else: raise ValueError('unsupported source scheme')
        except Exception as e: rows.append({'source':src,'status':'needs_review','error':str(e)[:500]})
    (out/'batch_manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'sources':len(rows),'ok':sum(1 for r in rows if r['status']=='ok'),'needs_review':sum(1 for r in rows if r['status']=='needs_review'),'manifest':str(out/'batch_manifest.json')},indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('sources'); ap.add_argument('--out',required=True); a=ap.parse_args(); batch(a.sources,a.out)
