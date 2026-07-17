import hashlib, json, time, random, datetime
from pathlib import Path

def sha256_bytes(b): return hashlib.sha256(b).hexdigest()
def now(): return datetime.datetime.utcnow().isoformat()+'Z'
def polite_sleep(base=0.2, jitter=0.2): time.sleep(base + random.random()*jitter)
def write_manifest(path, rows):
    Path(path).write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf-8')
