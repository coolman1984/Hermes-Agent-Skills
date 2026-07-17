#!/usr/bin/env python3
import argparse, json, time, re
from pathlib import Path
from urllib.parse import urljoin
import httpx
from bs4 import BeautifulSoup

def collect(url,out,max_rounds=5):
    # Lightweight infinite-scroll style collector for authorized demo/API endpoints.
    # If Playwright is installed, this script can be upgraded to real browser interception.
    out=Path(out); out.mkdir(parents=True,exist_ok=True)
    html=httpx.get(url,timeout=20).text
    api=re.search(r"fetch\([\"']([^\"']+)[\"']", html)
    if not api: raise SystemExit('no fetch endpoint discovered; use Playwright/browser inspection')
    endpoint=urljoin(url,api.group(1)); items=[]; seen=set(); next_url=endpoint; rounds=0
    while next_url and rounds<max_rounds:
        data=httpx.get(next_url,timeout=20).json(); rounds+=1
        for item in data.get('items',[]):
            key=item.get('id',json.dumps(item,sort_keys=True))
            if key not in seen: seen.add(key); items.append(item)
        next_url=data.get('next')
        time.sleep(0.2)
    (out/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'items':len(items),'rounds':rounds,'endpoint':endpoint},indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('url'); ap.add_argument('--out',required=True); a=ap.parse_args(); collect(a.url,a.out)
