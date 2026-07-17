#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import httpx
from common import now, sha256_bytes, polite_sleep

def collect(url,out,paginate='none',max_pages=5):
    out=Path(out); out.mkdir(parents=True, exist_ok=True); rows=[]; next_url=url; page=1
    with httpx.Client(follow_redirects=True,timeout=20,headers={'User-Agent':'HermesDataAcquisition/1.0','Accept':'application/json,*/*'}) as client:
        while next_url and page<=max_pages:
            r=client.get(next_url); raw=out/f'page_{page}.json'; raw.write_bytes(r.content)
            rows.append({'source_url':next_url,'status':r.status_code,'content_type':r.headers.get('content-type'),'fetched_at':now(),'bytes':len(r.content),'sha256':sha256_bytes(r.content),'cache_path':str(raw),'legal_basis':'API/public or user-authorized','page':page})
            data=None
            try: data=r.json()
            except Exception: data=None
            if paginate=='next_url' and isinstance(data,dict): next_url=data.get('next') or data.get('next_url')
            else: next_url=None
            page+=1; polite_sleep()
    (out/'manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'pages':len(rows),'manifest':str(out/'manifest.json')},indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('url'); ap.add_argument('--out',required=True); ap.add_argument('--paginate',default='none'); ap.add_argument('--max-pages',type=int,default=5); a=ap.parse_args(); collect(a.url,a.out,a.paginate,a.max_pages)
