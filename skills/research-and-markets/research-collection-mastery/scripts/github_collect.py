#!/usr/bin/env python3
import argparse, json, os
from pathlib import Path
import httpx
from common import now, write_json
API='https://api.github.com'
def collect(repo,out,issues=False, stars=False):
    out=Path(out); out.mkdir(parents=True,exist_ok=True); headers={'User-Agent':'HermesResearchCollection/1.0','Accept':'application/vnd.github+json'}
    if os.getenv('GITHUB_TOKEN'): headers['Authorization']='Bearer '+os.getenv('GITHUB_TOKEN')
    with httpx.Client(headers=headers,timeout=30,follow_redirects=True) as c:
        meta=c.get(f'{API}/repos/{repo}'); meta.raise_for_status(); repo_data=meta.json(); write_json(out/'repo.json',repo_data)
        issue_rows=[]; star_rows=[]
        if issues:
            page=1
            while page<=3:
                r=c.get(f'{API}/repos/{repo}/issues',params={'state':'all','per_page':100,'page':page}); r.raise_for_status(); batch=r.json()
                if not batch: break
                issue_rows.extend(batch); page+=1
            write_json(out/'issues.json',issue_rows)
        star_warning=''
        if stars:
            r=c.get(f'{API}/repos/{repo}/stargazers',params={'per_page':100,'page':1},headers={**headers,'Accept':'application/vnd.github.star+json'})
            if r.status_code == 200:
                star_rows=r.json(); write_json(out/'stargazers_sample.json',star_rows)
            else:
                star_warning=f'stargazers endpoint returned {r.status_code}; use GITHUB_TOKEN for richer star history access'; write_json(out/'stargazers_sample.json',[])
    manifest={'repo':repo,'stars':repo_data.get('stargazers_count'),'issues_collected':len(issue_rows),'stargazers_sample':len(star_rows),'star_warning':star_warning,'rate_limit_remaining':meta.headers.get('x-ratelimit-remaining'),'legal_basis':'GitHub public REST API','fetched_at':now()}; write_json(out/'manifest.json',manifest); print(json.dumps(manifest,indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('repo'); ap.add_argument('--out',required=True); ap.add_argument('--issues',action='store_true'); ap.add_argument('--stars',action='store_true'); a=ap.parse_args(); collect(a.repo,a.out,a.issues,a.stars)
