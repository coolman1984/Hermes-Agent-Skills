from typing import Optional
try:
    from fastapi import FastAPI, Header, HTTPException, Query
    from fastapi.testclient import TestClient
    from pydantic import BaseModel
except Exception as exc:
    raise SystemExit(f'Missing dependency: {exc}')

app = FastAPI()
ITEMS = [{'id': i, 'name': f'item-{i}'} for i in range(1, 26)]

class Page(BaseModel):
    items: list[dict]
    limit: int
    offset: int
    total: int

@app.get('/items', response_model=Page)
def list_items(authorization: Optional[str] = Header(None), limit: int = Query(10, ge=1, le=20), offset: int = Query(0, ge=0)):
    if authorization != 'Bearer test-token':
        raise HTTPException(status_code=401, detail='invalid token')
    return {'items': ITEMS[offset:offset+limit], 'limit': limit, 'offset': offset, 'total': len(ITEMS)}

if __name__ == '__main__':
    c = TestClient(app)
    assert c.get('/items').status_code == 401
    r = c.get('/items?limit=5&offset=5', headers={'Authorization':'Bearer test-token'})
    assert r.status_code == 200 and len(r.json()['items']) == 5 and r.json()['total'] == 25
    print('PASS backend secure endpoint', r.json())
