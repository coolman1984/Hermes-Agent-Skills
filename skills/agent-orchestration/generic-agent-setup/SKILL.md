---
name: generic-agent-setup
description: Bootstrap and run GenericAgent (self-evolving autonomous agent) in Linux
  aarch64 PRoot/Android environments. Includes dependency triage, API config, and
  common pitfalls.
tags: [agent-framework, genericagent, termux, proot, self-evolving, setup]
---

# GenericAgent Setup Skill

GenericAgent is a minimal (~3K lines), self-evolving autonomous agent framework that grows skills from experience. This skill covers deployment in constrained PRoot/Android environments like Hermes/OpenClaw on Termux.

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/lsdefine/GenericAgent.git
cd GenericAgent

# 2. Install core dependencies
pip3 install --break-system-packages streamlit beautifulsoup4 lxml

# 3. Optional: browser support
pip3 install --break-system-packages camoufox

# 4. Create API config (see below)
cp mykey_template.py mykey.py
# Edit mykey.py with your API credentials

# 5. Run
python3 agentmain.py          # CLI mode
# OR
streamlit run launch.pyw      # Web UI (if pywebview works)
```

## API Configuration

GenericAgent uses variable naming conventions to determine API protocol:

| Variable Pattern | Session Type | Protocol |
|-----------------|--------------|----------|
| `native_oai_*` | NativeOAISession | OpenAI chat/completions with native tool calling |
| `native_claude_*` | NativeClaudeSession | Anthropic messages API with native tool calling |
| `oai_*` (no native) | LLMSession | OpenAI-compatible (text-based tools, deprecated) |
| `claude_*` (no native) | ClaudeSession | Anthropic-compatible (text-based tools, deprecated) |

### Example Config (OpenRouter)

```python
native_oai_config = {
    'name': 'openrouter',
    'apikey': 'sk-or-v1-...',
    'apibase': 'https://openrouter.ai/api/v1',
    'model': 'anthropic/claude-sonnet-4-20250514',
    'temperature': 0.7,
    'max_tokens': 8192,
    'max_retries': 3,
    'connect_timeout': 10,
    'read_timeout': 180,
}
```

## Critical Finding: Hermes .env API Keys

**Problem:** API keys stored in `/root/.hermes/.env` (like `OPENROUTER_API_KEY`) may return HTTP 401 "User not found" when used directly against external APIs.

**Root Cause:** Hermes gateway keys are often:
- Scoped/proxied through the Hermes gateway only
- Not valid for direct external API calls
- Bound to specific relay infrastructure

**Solution:** For GenericAgent, you need **direct API keys** from the provider:
- Get OpenRouter keys directly from openrouter.ai (not via Hermes)
- Get Anthropic keys directly from anthropic.com
- Or route GenericAgent through a local Hermes endpoint if available

## Dependencies in PRoot/Android

### Required
- `streamlit` - Web UI (works)
- `beautifulsoup4` - Web parsing (required for web tools)
- `lxml` - HTML parsing

### Optional (may fail)
- `pywebview` - Desktop app wrapper (often fails on aarch64 PRoot due to `proxy_tools` build error)
- `camoufox` - Browser automation (installable, useful for web tools)

### Installation Pattern
```bash
pip3 install --break-system-packages <package>
```

## Running Modes

### 1. CLI Mode (Most Reliable)
```bash
cd /root/GenericAgent
python3 agentmain.py
```
Wait for `> ` prompt, then type tasks directly.

### 2. Streamlit Web UI
```bash
cd /root/GenericAgent
streamlit run launch.pyw --server.address=0.0.0.0 --server.port=8501
```
Access via browser at `http://localhost:8501`

### 3. Bot Frontends (Optional)
- Telegram: `python frontends/tgapp.py` (needs `tg_bot_token`)
- WeChat: `python frontends/wechatapp.py` (QR login)
- QQ: `python frontends/qqapp.py`
- Feishu/Lark: `python frontends/fsapp.py`

## Architecture Notes

### 9 Atomic Tools
1. `code_run` - Execute arbitrary code
2. `file_read` - Read files
3. `file_write` - Write files
4. `file_patch` - Patch/modify files
5. `web_scan` - Perceive web content
6. `web_execute_js` - Control browser behavior
7. `ask_user` - Human-in-the-loop confirmation
8. `update_working_checkpoint` - Memory management
9. `start_long_term_update` - Memory management

### Layered Memory (L0-L4)
- **L0** - Meta Rules (core behavior constraints)
- **L1** - Insight Index (routing/recall)
- **L2** - Global Facts (stable knowledge)
- **L3** - Task Skills/SOPs (reusable workflows)
- **L4** - Session Archive (finished task records)

### Self-Evolution Loop
```
[New Task] → [Autonomous Exploration] → [Crystallize to Skill] → [Write to Memory] → [Direct Recall Next Time]
```

## Common Pitfalls

### 1. pywebuild Fails on aarch64
**Error:** `proxy_tools` setup.py fails with `ImportError: cannot import name 'setup' from 'setuptools'`

**Fix:** Skip pywebview. Use `streamlit run launch.pyw` instead for web UI.

### 2. API 401 "User not found"
**Cause:** Using scoped/proxy API keys (e.g., from Hermes .env)

**Fix:** Get direct API keys from the provider, or route through local gateway.

### 3. BeautifulSoup4 Missing Error
**Error:** `[Error] BeautifulSoup4 未安装`

**Fix:** `pip3 install --break-system-packages beautifulsoup4 lxml`

### 4. EOFError on stdin
**Error:** `EOFError: EOF when reading a line`

**Cause:** Running in non-interactive context (subprocess without stdin)

**Fix:** Run interactively or pipe input properly.

### 5. Python Version Compatibility
**Recommended:** Python 3.11 or 3.12
**Avoid:** Python 3.14 (incompatible with pywebview and some dependencies)

## Verification Checklist

After setup, verify:
- [ ] `python3 agentmain.py` starts without import errors
- [ ] API connection works (test with simple task like "list files")
- [ ] Web tools work (BeautifulSoup4 installed)
- [ ] Memory directory exists (`memory/` folder)
- [ ] Skills can be written (check write permissions)

## Performance Notes

- **Token Efficiency:** GenericAgent uses <30K context vs 200K-1M for other agents
- **Core Loop:** ~100 lines of code (`agent_loop.py`)
- **Self-Bootstrap:** The entire repository (including git commits) was created by GenericAgent itself

## When to Use GenericAgent vs Other Agents

| Use GenericAgent | Use OpenClaw/Hermes |
|-----------------|---------------------|
| Self-evolving skills from scratch | Pre-configured skill ecosystem |
| Minimal setup (<5 min) | Complex orchestration acceptable |
| Single-model focus | Multi-agent delegation needed |
| Token-efficient tasks | High-token budget available |
| Learning/adaptation priority | Stability/repeatability priority |

## Related Skills
- `hermes-agent` - Hermes-specific agent workflows
- `opencode` - OpenCode CLI agent alternative
- `claude-code` - Claude Code CLI agent
- `camoufox-article-browsing` - Browser automation for web tools
