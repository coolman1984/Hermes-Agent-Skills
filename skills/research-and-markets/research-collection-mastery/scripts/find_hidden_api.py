#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path
import httpx
from bs4 import BeautifulSoup

def find(src,out):
    out=Path(out); out.mkdir(parents=True,exist_ok=True)
    html=httpx.get(src,timeout=20).text if src.startswith('http') else Path(src).read_text(encoding='utf-8')
    pattern = r"fetch\([\"']([^\"']+)[\"']|axios\.get\([\"']([^\"']+)[\"']|[\"']([^\"']+\.json(?:\?[^\"']*)?)[\"']"
    candidates=sorted(set(re.findall(pattern, html)))
    urls=[]
    for tup in candidates:
        for x in tup:
            if x: urls.append(x)
    (out/'hidden_api_candidates.json').write_text(json.dumps(urls,indent=2),encoding='utf-8')
    print(json.dumps({'candidates':urls,'count':len(urls)},indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('source'); ap.add_argument('--out',required=True); a=ap.parse_args(); find(a.source,a.out)
