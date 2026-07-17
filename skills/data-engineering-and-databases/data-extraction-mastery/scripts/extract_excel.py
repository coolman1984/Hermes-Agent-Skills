#!/usr/bin/env python3
import argparse, csv, json, sys, datetime
from pathlib import Path
import openpyxl

def find_header(rows):
    best=(0,-1)
    for i,row in enumerate(rows[:20]):
        score=sum(1 for c in row if c not in (None,''))
        if score>best[1]: best=(i,score)
    return best[0]

def extract(path,out):
    out=Path(out); out.mkdir(parents=True, exist_ok=True); p=Path(path)
    wb=openpyxl.load_workbook(p, data_only=True, read_only=False, keep_vba=p.suffix.lower()=='.xlsm')
    manifest=[]
    for ws in wb.worksheets:
        rows=[[cell for cell in row] for row in ws.iter_rows(values_only=True)]
        hi=find_header(rows); header=[str(x).strip() if x is not None else f'col_{j+1}' for j,x in enumerate(rows[hi])]
        records=[]
        for ridx,row in enumerate(rows[hi+1:], start=hi+2):
            if not any(x not in (None,'') for x in row): continue
            first=str(row[0]).lower() if row and row[0] is not None else ''
            if 'total' in first or 'الإجمالي' in first: continue
            rec={header[j] if j<len(header) else f'col_{j+1}': row[j] if j<len(row) else None for j in range(max(len(header),len(row)))}
            rec.update({'_source_file':str(p),'_source_sheet':ws.title,'_source_row':ridx,'_extracted_at':datetime.datetime.utcnow().isoformat()})
            records.append(rec)
        fp=out/(p.stem+'__'+ws.title.replace('/','_')+'.jsonl')
        with fp.open('w',encoding='utf-8') as f:
            for r in records: f.write(json.dumps(r,ensure_ascii=False,default=str)+'\n')
        manifest.append({'sheet':ws.title,'rows':len(records),'output':str(fp),'hidden':ws.sheet_state!='visible','merged_ranges':[str(r) for r in ws.merged_cells.ranges]})
    (out/'manifest.json').write_text(json.dumps({'file':str(p),'type':'excel','sheets':manifest},ensure_ascii=False,indent=2),encoding='utf-8')
    return manifest
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('file'); ap.add_argument('--out',required=True); a=ap.parse_args(); print(json.dumps(extract(a.file,a.out),ensure_ascii=False,indent=2))
