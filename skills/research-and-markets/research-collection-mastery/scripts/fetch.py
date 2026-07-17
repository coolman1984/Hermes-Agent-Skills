#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from urllib.parse import urlparse
import httpx
from common import now, sha256_bytes, sleep_polite, write_json

def fetch(url,out,legal_basis='public/authorized by user', retries=2):
    out=Path(out); out.mkdir(parents=True, exist_ok=True)
    headers={'User-Agent':'HermesResearchCollection/1.0','Accept':'*/*'}
    last=None
    for attempt in range(retries+1):
        try:
            r=httpx.get(url,follow_redirects=True,timeout=20,headers=headers)
            if r.status_code in (429,500,502,503,504) and attempt<retries:
                sleep_polite(0.5*(2**attempt),0.3); continue
            last=r; break
        except Exception as e:
            if attempt==retries: raise
            sleep_polite(0.5*(2**attempt),0.3)
    name=Path(urlparse(url).path).name or 'index.html'; raw=out/name; raw.write_bytes(last.content)
    row={'source_url':url,'status':last.status_code,'content_type':last.headers.get('content-type'),'fetched_at':now(),'bytes':len(last.content),'sha256':sha256_bytes(last.content),'legal_basis':legal_basis,'cache_path':str(raw)}
    write_json(out/'manifest.json',[row]); print(json.dumps(row,ensure_ascii=False,indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('url'); ap.add_argument('--out',required=True); ap.add_argument('--legal-basis',default='public/authorized by user'); a=ap.parse_args(); fetch(a.url,a.out,a.legal_basis)
