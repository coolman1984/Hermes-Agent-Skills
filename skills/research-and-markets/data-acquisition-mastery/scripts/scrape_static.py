#!/usr/bin/env python3
import argparse, json
from io import StringIO
from pathlib import Path
import httpx, pandas as pd
from bs4 import BeautifulSoup
from common import now, sha256_bytes

def scrape(src,out):
    out=Path(out); out.mkdir(parents=True,exist_ok=True)
    if src.startswith('http'):
        r=httpx.get(src,follow_redirects=True,timeout=20,headers={'User-Agent':'HermesDataAcquisition/1.0'}); html=r.text; status=r.status_code; url=src
    else:
        html=Path(src).read_text(encoding='utf-8'); status=200; url=str(Path(src))
    raw=out/'page.html'; raw.write_text(html,encoding='utf-8')
    soup=BeautifulSoup(html,'html.parser'); title=soup.title.string if soup.title else ''
    tables=[]
    try:
        for i,df in enumerate(pd.read_html(StringIO(html)), start=1):
            fp=out/f'table_{i}.jsonl'; df['_source_url']=url; df.to_json(fp,orient='records',lines=True,force_ascii=False); tables.append({'index':i,'rows':len(df),'output':str(fp)})
    except Exception as e: tables.append({'warning':str(e)})
    manifest={'source_url':url,'status':status,'title':title,'fetched_at':now(),'bytes':len(html.encode()),'sha256':sha256_bytes(html.encode()),'cache_path':str(raw),'tables':tables,'legal_basis':'public/authorized by user'}
    (out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(manifest,ensure_ascii=False,indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('source'); ap.add_argument('--out',required=True); a=ap.parse_args(); scrape(a.source,a.out)
