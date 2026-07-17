---
name: perplexity-terminal
description: Search Perplexity via terminal using your browser session cookies (no
  API key needed)
tags: [perplexity, terminal, cookies, no-api-key, search]
---

# Perplexity Terminal Skill

Use your logged-in Perplexity account through terminal — no API key needed.

## Setup (One Time)

### Step 1: Get Browser Cookies

1. Go to https://perplexity.ai and log in
2. Press **F12** → Developer Tools
3. Click **Application** tab
4. Expand **Cookies** → **https://perplexity.ai**
5. Find cookie named `perplexityai.sid` or `pplx.sid`
6. Copy its **value** (the long string, not the cookie name)

### Step 2: Save Session

```bash
python3 ~/.hermes/scripts/perplexity_helper.py setup
```

Paste your session token when prompted.

## Usage

### Ask a Question
```bash
python3 ~/.hermes/scripts/perplexity_helper.py ask "What are the latest AI trends in 2026?"
```

### Interactive Mode
```bash
python3 ~/.hermes/scripts/perplexity_helper.py
```

Then type questions directly. Type `quit` to exit.

### Test
```bash
python3 ~/.hermes/scripts/perplexity_helper.py test
```

## Focus Modes

You can specify search focus:
- `internet` - Web search (default)
- `academic` - Academic papers
- `writing` - Writing assistance
- `wolfram` - Wolfram calculations

Example:
```bash
python3 ~/.hermes/scripts/perplexity_helper.py ask "latest AI research papers"
```

## File Locations

- Session config: `~/.hermes/perplexity_config.json`
- Script: `~/.hermes/scripts/perplexity_helper.py`

## Troubleshooting

### "Session expired"
- Re-login to perplexity.ai in browser
- Get new cookie value
- Run `setup` again

### "Could not get response"
- Make sure you're logged in on web first
- Check cookie value is correct
- Try clearing and re-copying the cookie

### Cloudflare Blocking
If you get "Just a moment..." or 403 errors, Perplexity has strong Cloudflare protection. **Known limitations:**
- Cookie session method often blocked
- Direct API calls blocked
- Requires specialized scraper or API key

### Alternative: Use OpenRouter
If Perplexity cookies don't work, use DeepSeek or other models via OpenRouter:
```bash
# Test with DeepSeek (similar to Perplexity Sonar)
curl -X POST "https://openrouter.ai/api/v1/chat/completions" \
  -H "Authorization: Bearer YOUR_OPENROUTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "deepseek/deepseek-chat", "messages": [{"role": "user", "content": "Your question"}]}'
```

### Alternative: Use last30days Skill
For web research without API keys, use the `last30days` skill:
```bash
python3 ~/.hermes/skills/research/scripts/last30days.py "your topic" --quick
```
