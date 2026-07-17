#!/usr/bin/env python3
import argparse, json, subprocess, sys, datetime, sqlite3
from pathlib import Path
from detect_and_route import route

def run(cmd):
    return subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)

def batch(folder,out):
    folder=Path(folder); out=Path(out); out.mkdir(parents=True, exist_ok=True)
    report=[]
    for p in sorted(x for x in folder.iterdir() if x.is_file()):
        item={'file':str(p),'route':None,'status':None,'warnings':[]}
        try:
            r=route(p); item['route']=r; target=out/'items'/p.stem; target.mkdir(parents=True, exist_ok=True)
            if r=='excel': run([sys.executable, str(Path(__file__).with_name('extract_excel.py')), str(p), '--out', str(target)])
            elif r=='pdf': run([sys.executable, str(Path(__file__).with_name('extract_pdf.py')), str(p), '--out', str(target)])
            elif r=='email': run([sys.executable, str(Path(__file__).with_name('extract_email.py')), str(p), '--out', str(target)])
            elif r=='webtext': run([sys.executable, str(Path(__file__).with_name('scrape_page.py')), str(p), '--out', str(target)])
            else: raise ValueError('unsupported or unknown type')
            item['status']='ok'; item['output']=str(target)
        except Exception as e:
            item['status']='needs_review'; item['error']=str(e)[:500]
        report.append(item)
    db=out/'extraction_report.sqlite'
    con=sqlite3.connect(db); con.execute('create table if not exists extraction_report(file text, route text, status text, error text, extracted_at text)'); con.execute('delete from extraction_report')
    for x in report: con.execute('insert into extraction_report values(?,?,?,?,?)',(x.get('file'),x.get('route'),x.get('status'),x.get('error'),datetime.datetime.utcnow().isoformat()))
    con.commit(); con.close()
    (out/'extraction_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    return {'files':len(report),'ok':sum(1 for x in report if x['status']=='ok'),'needs_review':sum(1 for x in report if x['status']=='needs_review'),'db':str(db)}
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('folder'); ap.add_argument('--out',required=True); a=ap.parse_args(); print(json.dumps(batch(a.folder,a.out),ensure_ascii=False,indent=2))
