# AI and Automation Reference

Use for LLM apps, RAG, agents, cron jobs, webhooks, scripts, CI/CD.

Top traps: using LLM for deterministic parsing, no evaluation set, vague prompts, hidden tool side effects, no cost budget, no human gate, recursive automation, prompt injection, no retry/idempotency, cron jobs without self-contained context.

Runnable example is in `scripts/human_gate_automation.py`.

Usage image: use when software should do repeated work with bounded autonomy.
