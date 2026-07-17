#!/usr/bin/env python3
import argparse, json, datetime
from io import StringIO
from pathlib import Path
import pandas as pd
import requests
from bs4 import BeautifulSoup

def extract(src,out):
    out=Path(out); out.mkdir(parents=True, exist_ok=True)
    if src.startswith('http'):
        html=requests.get(src,timeout=20).text; source=src
    else:
        html=Path(src).read_text(encoding='utf-8'); source=str(Path(src))
    soup=BeautifulSoup(html,'html.parser')
    text=soup.get_text('\n',strip=True)
    tables=[]
    try:
        for i,df in enumerate(pd.read_html(StringIO(html))):
            fp=out/f'table_{i+1}.jsonl'; df['_source_url']=source; df['_source_table']=i+1; df.to_json(fp,orient='records',lines=True,force_ascii=False); tables.append({'index':i+1,'rows':len(df),'cols':len(df.columns),'output':str(fp)})
    except Exception as e: tables.append({'error':str(e)})
    (out/'page_text.txt').write_text(text,encoding='utf-8')
    (out/'manifest.json').write_text(json.dumps({'source':source,'text_chars':len(text),'tables':tables,'_extracted_at':datetime.datetime.utcnow().isoformat()},ensure_ascii=False,indent=2),encoding='utf-8')
    return {'text_chars':len(text),'tables':tables}
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('source'); ap.add_argument('--out',required=True); a=ap.parse_args(); print(json.dumps(extract(a.source,a.out),ensure_ascii=False,indent=2))
