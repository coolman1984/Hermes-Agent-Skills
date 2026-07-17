---
name: deepseek-alt
description: Free AI research assistant using ByteDance Dola Seed model through KiloCode
  (no API key needed)
tags: [ai-assistant, deepseek, no-api-key, free, cli]
---

# DeepSeek Alternative Skill

A free AI assistant that works without API keys — uses ByteDance Dola Seed model via KiloCode.

## Usage

### Ask a Question
```bash
python3 ~/.hermes/scripts/deepseek_alt.py "your question"
```

### Interactive Mode
```bash
# Just run without arguments and type questions
python3 ~/.hermes/scripts/deepseek_alt.py
```

### Examples
```bash
# Basic question
python3 ~/.hermes/scripts/deepseek_alt.py "What is machine learning?"

# Research question
python3 ~/.hermes/scripts/deepseek_alt.py "latest AI trends in 2026"

# Code question
python3 ~/.hermes/scripts/deepseek_alt.py "how to use Python requests library"
```

## Available Models

| Model | Description | Cost |
|-------|-------------|------|
| fast | ByteDance Dola Seed 2.0 Pro | Free |
| chat | Kilo Auto Free | Free |

### Switch Model
```bash
python3 ~/.hermes/scripts/deepseek_alt.py "question" --model fast
python3 ~/.hermes/scripts/deepseek_alt.py "question" --model chat
```

## Capabilities

- ✅ General knowledge Q&A
- ✅ Code assistance
- ✅ Research summaries
- ✅ Writing help
- ✅ Translation
- ✅ Problem solving

## Limitations

- Max 2000 tokens per response
- No tool use / function calling
- Knowledge cutoff varies by model

## File Location

- Script: `~/.hermes/scripts/deepseek_alt.py`
