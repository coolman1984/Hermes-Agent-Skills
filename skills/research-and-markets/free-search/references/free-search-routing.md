# Free Search Routing

## Preferred order
- `ddgr --json -n 5 "query"`
- `trafilatura -u "URL"`
- `curl` DuckDuckGo HTML fallback
- `curl` raw page fetch

## When to use
- general web search
- research tasks
- article extraction
- fact-finding without API keys

## When not to use
- when a richer backend is already configured and working
- when the requested tool is not installed in the environment

## Test plan
- search for a complex query
- open one result
- extract the page text
- compare the quality to a raw web fetch
