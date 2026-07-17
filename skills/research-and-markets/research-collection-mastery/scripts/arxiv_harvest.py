#!/usr/bin/env python3
import argparse, json, urllib.parse, xml.etree.ElementTree as ET
from pathlib import Path
import httpx
from common import now, write_json
ATOM='{http://www.w3.org/2005/Atom}'
def harvest(query,out,max_results=50,pdf_limit=5):
    out=Path(out); (out/'pdfs').mkdir(parents=True,exist_ok=True)
    url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':query,'start':0,'max_results':max_results})
    r=httpx.get(url,timeout=30,headers={'User-Agent':'HermesResearchCollection/1.0'})
    feed=ET.fromstring(r.content); papers=[]; pdfs=[]
    for e in feed.findall(ATOM+'entry'):
        pid=e.findtext(ATOM+'id'); title=' '.join((e.findtext(ATOM+'title') or '').split()); authors=[a.findtext(ATOM+'name') for a in e.findall(ATOM+'author')]
        pdf_url=None
        for link in e.findall(ATOM+'link'):
            if link.attrib.get('title')=='pdf': pdf_url=link.attrib.get('href')
        row={'id':pid,'title':title,'authors':authors,'pdf_url':pdf_url}; papers.append(row)
        if pdf_url and len(pdfs)<pdf_limit:
            pr=httpx.get(pdf_url,timeout=60,follow_redirects=True,headers={'User-Agent':'HermesResearchCollection/1.0'}); fp=out/'pdfs'/(pid.rsplit('/',1)[-1]+'.pdf'); fp.write_bytes(pr.content); pdfs.append(str(fp))
    write_json(out/'papers.json',papers); write_json(out/'manifest.json',{'source_url':url,'count':len(papers),'pdfs':pdfs,'legal_basis':'arXiv public API/open access','fetched_at':now()})
    print(json.dumps({'papers':len(papers),'pdfs':len(pdfs),'manifest':str(out/'manifest.json')},indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('query'); ap.add_argument('--out',required=True); ap.add_argument('--max-results',type=int,default=50); ap.add_argument('--pdf-limit',type=int,default=5); a=ap.parse_args(); harvest(a.query,a.out,a.max_results,a.pdf_limit)
