#!/usr/bin/env python3
import argparse, json, email, datetime, subprocess, sys
from email import policy
from pathlib import Path

def extract(path,out):
    out=Path(out); out.mkdir(parents=True, exist_ok=True); p=Path(path)
    raw=p.read_bytes()
    msg=email.message_from_bytes(raw, policy=policy.default)
    body=[]; attachments=[]
    for part in msg.walk():
        disp=part.get_content_disposition(); ctype=part.get_content_type()
        if disp=='attachment':
            name=part.get_filename() or 'attachment.bin'; ap=out/'attachments'/name; ap.parent.mkdir(exist_ok=True)
            ap.write_bytes(part.get_payload(decode=True) or b'')
            attachments.append({'filename':name,'path':str(ap),'bytes':ap.stat().st_size})
        elif ctype in ['text/plain','text/html'] and disp!='attachment':
            try: body.append(part.get_content())
            except Exception: pass
    manifest={'file':str(p),'subject':msg.get('subject'),'from':msg.get('from'),'to':msg.get('to'),'date':msg.get('date'),'body_chars':sum(len(x) for x in body),'attachments':attachments,'_extracted_at':datetime.datetime.utcnow().isoformat()}
    (out/'email_body.txt').write_text('\n\n'.join(body),encoding='utf-8')
    (out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    return manifest
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('file'); ap.add_argument('--out',required=True); a=ap.parse_args(); print(json.dumps(extract(a.file,a.out),ensure_ascii=False,indent=2))
