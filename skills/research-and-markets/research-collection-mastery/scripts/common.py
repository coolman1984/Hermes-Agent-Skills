import hashlib, json, time, random, datetime
from pathlib import Path

def now(): return datetime.datetime.utcnow().isoformat()+'Z'
def sha256_bytes(b): return hashlib.sha256(b).hexdigest()
def sleep_polite(base=0.2, jitter=0.2): time.sleep(base + random.random()*jitter)
def write_json(path,obj): Path(path).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
