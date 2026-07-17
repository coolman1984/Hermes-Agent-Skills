# Fallback Search Patterns — Verified 2026-07-12

Complete code patterns that worked in a real constrained Hermes session where:
- `TAVILY_API_KEY` was not set → `web_search`/`web_extract` both failed
- Exa MCP was not configured (`mcporter list exa` → unknown)
- `x_search` failed (XAI credits exhausted)
- DuckDuckGo returned CAPTCHA challenges
- OpenAI pages were JS-walled (required cookies)

## Brave Search — The Reliable Primary Fallback

```python
import urllib.request, re, urllib.parse

q = urllib.parse.quote('your search query here')
req = urllib.request.Request(f'https://search.brave.com/search?q={q}&source=web', headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
    'Accept': 'text/html'
})
with urllib.request.urlopen(req, timeout=15) as r:
    body = r.read().decode('utf-8', errors='replace')

# Extract snippet divs (Brave's markup)
snippets = re.findall(r'<div[^>]*class="[^"]*snippet[^"]*"[^>]*>(.*?)</div>', body, re.DOTALL)
for s in snippets:
    text = re.sub(r'<[^>]+>', '', s).strip()
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'&#x27;', "'", text)
    text = re.sub(r'&quot;', '"', text)
    if len(text) > 40:
        print(text[:400])
        print('---')

# Also extract result URLs
urls = re.findall(r'href="(https?://[^"]+)"', body)
for u in urls:
    u = u.replace('&amp;', '&')
    # Filter to relevant domains
    if any(d in u for d in ['openai.com', 'theverge.com', 'techcrunch.com', 'github.com']):
        print(u)
```

### Rate Limiting
- Brave returns HTTP 429 after ~5 rapid queries
- Space queries 15+ seconds apart
- On 429: wait 30s, retry with a slightly different query

## Wikipedia API — Fast Factual Lookup

```python
import urllib.request, json

# Get article extract
url = 'https://en.wikipedia.org/w/api.php?action=query&titles=ChatGPT&prop=extracts&exintro=1&explaintext=1&format=json'
req = urllib.request.Request(url, headers={'User-Agent': 'python-urllib'})
with urllib.request.urlopen(req, timeout=15) as r:
    data = json.loads(r.read())
pages = data.get('query', {}).get('pages', {})
for pid, page in pages.items():
    print(page.get('extract', '')[:2000])
```

## OpenAI Desktop Page — Extract Download Links

```python
import urllib.request, re

url = 'https://openai.com/chatgpt/desktop/'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
})
with urllib.request.urlopen(req, timeout=15) as r:
    body = r.read().decode('utf-8', errors='replace')

# The page is JS-rendered but download URLs are in the HTML source
# Find Microsoft Store installer link
for m in re.finditer(r'(https?://get\.microsoft\.com/[^"]+)', body):
    print(m.group(1).replace('&amp;', '&'))

# Find Mac DMG link
for m in re.finditer(r'(https?://persistent\.oaistatic\.com/[^"]+\.dmg)', body):
    print(m.group(1))
```

## Direct File Download from CDN

```python
import urllib.request, hashlib

url = 'https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi'
out = '/sdcard/Download/Program Downloads/ChatGPT Installer.exe'

req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})
with urllib.request.urlopen(req, timeout=60) as r:
    data = r.read()

with open(out, 'wb') as f:
    f.write(data)

# Verify PE header
assert data[:2] == b'MZ', 'Not a valid PE executable'

# Create SHA256
sha = hashlib.sha256(data).hexdigest()
with open(out + '.sha256', 'w') as f:
    f.write(f'{sha}  {out.split("/")[-1]}\n')
```

## Microsoft Store App Package (full .msix/.appx)

Microsoft Store full app packages are NOT directly downloadable without authentication on non-Windows machines. The store ID for ChatGPT is `9NT1R1C2HH7J`, but the content delivery APIs require Windows Store authentication tokens.

What works:
- The ~1.4 MB `ChatGPT Installer.exe` from the direct Microsoft link triggers Store installation on Windows
- The full ~200-300 MB .msix package is downloaded by the Store at install time
- `store.rg-adguard.net` can generate direct links but may be blocked (403)

## Tool Failure Diagnostics

When all search tools fail, check:
```bash
echo $TAVILY_API_KEY          # empty → web_search/web_extract will fail
mcporter list exa 2>&1        # unknown → Exa MCP not configured
hermes tools list             # check which toolsets are enabled
```

The most reliable fallback in a constrained Hermes session is:
1. Brave Search via `terminal` + Python stdlib (no keys needed)
2. Direct curl to known CDN/API endpoints
3. Wikipedia API for factual content
