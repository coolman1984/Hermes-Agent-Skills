#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from urllib.parse import urljoin
import httpx
from bs4 import BeautifulSoup

def discover(src,out):
    out=Path(out); out.mkdir(parents=True,exist_ok=True)
    if src.startswith('http'):
        html=httpx.get(src,timeout=20,follow_redirects=True,headers={'User-Agent':'HermesDataAcquisition/1.0'}).text; base=src
    else:
        html=Path(src).read_text(encoding='utf-8'); base='file://'+str(Path(src).resolve())
    soup=BeautifulSoup(html,'html.parser')
    links=[]
    for a in soup.find_all('a',href=True): links.append({'text':a.get_text(' ',strip=True),'url':urljoin(base,a['href'])})
    (out/'links.json').write_text(json.dumps(links,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'links':len(links),'out':str(out/'links.json')},indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('source'); ap.add_argument('--out',required=True); a=ap.parse_args(); discover(a.source,a.out)
