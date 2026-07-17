#!/usr/bin/env python3
import argparse, json, hashlib
from pathlib import Path
from urllib.parse import urlparse
import httpx
from common import now, sha256_bytes

def fetch(url,out,legal_basis='public/authorized by user', user_agent='HermesDataAcquisition/1.0'):
    out=Path(out); out.mkdir(parents=True, exist_ok=True)
    headers={'User-Agent':user_agent,'Accept':'*/*'}
    with httpx.Client(follow_redirects=True, timeout=20, headers=headers) as client:
        r=client.get(url)
    name=Path(urlparse(url).path).name or 'index.html'
    raw=out/name
    raw.write_bytes(r.content)
    row={'source_url':url,'method':'GET','status':r.status_code,'content_type':r.headers.get('content-type'),'fetched_at':now(),'bytes':len(r.content),'sha256':sha256_bytes(r.content),'legal_basis':legal_basis,'cache_path':str(raw),'warnings':[]}
    (out/'manifest.json').write_text(json.dumps([row],ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(row,ensure_ascii=False,indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('url'); ap.add_argument('--out',required=True); ap.add_argument('--legal-basis',default='public/authorized by user'); a=ap.parse_args(); fetch(a.url,a.out,a.legal_basis)
