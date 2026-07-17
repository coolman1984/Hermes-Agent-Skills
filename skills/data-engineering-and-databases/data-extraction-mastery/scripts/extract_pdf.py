#!/usr/bin/env python3
import argparse, json, datetime, subprocess, tempfile
from pathlib import Path
import fitz

def extract(path,out, ocr_lang='ara+eng'):
    out=Path(out); out.mkdir(parents=True, exist_ok=True); p=Path(path); doc=fitz.open(p)
    pages=[]
    for i,page in enumerate(doc, start=1):
        text=page.get_text('text').strip(); used_ocr=False
        if len(text)<10:
            last_error=''
            for scale in (2,1,3):
                pix=page.get_pixmap(matrix=fitz.Matrix(scale,scale)); img=out/f'{p.stem}_page_{i}_x{scale}.png'; pix.save(img)
                try:
                    text=subprocess.check_output(['tesseract',str(img),'stdout','-l',ocr_lang,'--psm','6'], text=True, stderr=subprocess.DEVNULL).strip(); used_ocr=True
                    if text: break
                except Exception as e:
                    last_error=str(e); text=''
            if not text and last_error: pages.append({'page':i,'error':last_error})
        pages.append({'page':i,'text':text,'chars':len(text),'used_ocr':used_ocr,'_source_file':str(p),'_source_unit':f'page:{i}','_extracted_at':datetime.datetime.utcnow().isoformat()})
    (out/(p.stem+'.json')).write_text(json.dumps({'file':str(p),'type':'pdf','pages':pages},ensure_ascii=False,indent=2),encoding='utf-8')
    (out/(p.stem+'.txt')).write_text('\n\n'.join(x.get('text','') for x in pages),encoding='utf-8')
    return {'pages':len(pages),'ocr_pages':sum(1 for x in pages if x.get('used_ocr')),'chars':sum(x.get('chars',0) for x in pages)}
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('file'); ap.add_argument('--out',required=True); a=ap.parse_args(); print(json.dumps(extract(a.file,a.out),ensure_ascii=False,indent=2))
