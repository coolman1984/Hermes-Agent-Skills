#!/usr/bin/env python3
import argparse, json
from urllib.parse import urlparse, urljoin
import urllib.robotparser

def check(url, ua='HermesDataAcquisition'):
    p=urlparse(url); robots=urljoin(f'{p.scheme}://{p.netloc}','/robots.txt')
    rp=urllib.robotparser.RobotFileParser(); rp.set_url(robots)
    try: rp.read(); allowed=rp.can_fetch(ua,url)
    except Exception as e: print(json.dumps({'url':url,'robots':robots,'allowed':None,'error':str(e)})); return
    print(json.dumps({'url':url,'robots':robots,'allowed':allowed}, indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('url'); a=ap.parse_args(); check(a.url)
