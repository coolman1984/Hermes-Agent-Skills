---
name: agentic-workflows-do-framework
description: Build production AI workflows using Directive-Orchestration-Execution
  pattern — separates probabilistic reasoning from deterministic execution.
tags: [workflow, determinism, sop, orchestration, do-framework]
category: software-development
---

# Agentic Workflows: DO Framework

## Core Principle

**Problem:** LLMs are probabilistic (stochastic outputs, variable quality) but business workflows need determinism (consistency, predictability, reliability).

**Solution:** Use the `DO` framework to separate concerns:

```
Directive       → SOP/instructions (markdown, natural language)
Orchestration   → LLM decides, plans, adapts, handles edge cases
Execution       → Deterministic scripts/tools (sorting, parsing, API calls, validation)
```

## Why This Works

| Without DO | With DO |
|------------|---------|
| LLM does everything → compound error | LLM only decides → lower error rate |
| Unpredictable outputs | Deterministic execution layer |
| Hard to debug/reuse | Clear separation of concerns |
| Token-inefficient | Token-efficient directives |

## Implementation Steps

### 1. Create Workspace Structure

```bash
mkdir -p /root/.hermes/workspaces/main/{directives,execution}
```

### 2. Write Directive (SOP in Markdown)

Create `directives/<task-name>.md`:

```markdown
# Task: Lead Generation Outreach

## Objective
Find 5 meal-prep companies in Vancouver, extract emails, send outreach.

## Inputs
- City: Vancouver
- Industry: meal prep
- Output format: CSV with company, email, source_url

## Steps
1. Search for meal-prep companies in Vancouver
2. For each company:
   - Extract name, website, email
   - If email not found, expand search (LinkedIn, contact page)
3. Validate email format
4. Save to CSV
5. Send outreach email

## Edge Cases
- If <3 companies found, expand to nearby cities
- If email validation fails, skip and log
- If API rate limit hit, wait 60s and retry

## Definition of Done
- 5 companies with valid emails in CSV
- Outreach emails sent
- Results logged in change_log.md
```

### 3. Write Execution Scripts

Create `execution/<task-name>.py`:

```python
# Deterministic: sorting, parsing, API calls, validation
# NO LLM logic here — pure functions only

def validate_email(email: str) -> bool:
    import re
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def save_to_csv(data: list, path: str):
    import csv
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
```

### 4. Add Guardrails

Add these rules to workspace-level `README.md` or task directive:

```markdown
## Guardrails (MANDATORY)

1. **Cost Threshold**: If total token cost > $0.50, ask for confirmation before continuing.
2. **Least Privilege**: Only use tools required for this task. No write access to credentials.
3. **Secrets**: Never read/output `.env` contents. Use environment variable references only.
4. **Self-Modification Logging**: Any change to directives/scripts must be logged in `change_log.md`.
5. **No Credential Modification**: Never modify authentication tokens or passwords automatically.
```

### 5. Enable Self-Annealing

Add to directive:

```markdown
## Self-Improvement Protocol

After each run:
1. Check for errors or failures
2. If error is repeatable:
   - Diagnose root cause
   - Fix directive or script
   - Log change in `change_log.md` with timestamp and description
3. If output is incomplete:
   - Update "Definition of Done"
   - Add missing edge cases
```

### 6. Create Change Log Template

`change_log.md`:

```markdown
# Change Log

## 2026-04-19
- Added email validation to lead-generation directive
- Fixed CSV path bug in execution script
- Added rate-limit retry logic (60s backoff)

## YYYY-MM-DD
- [Description of change]
- [Files modified]
- [Reason/trigger]
```

## Testing Protocol

### Before Deployment:
1. **Test with real data** (not synthetic)
2. **Fresh instance test** (new context/session)
3. **Run 10-15 times** to catch edge cases
4. **Monitor first runs manually**

### After Deployment:
1. **Add hooks/notifications** (Telegram for Hermes)
2. **Review first 10 runs**
3. **Enable human-in-the-loop** for sensitive outputs (proposals, invoices)

## Parallelization (Advanced)

For high-throughput:

```bash
# Run 3 approaches in parallel, pick best
agent-1 --directive=approach-a
agent-2 --directive=approach-b
agent-3 --directive=approach-c
```

**Subagents:**
- **Reviewer subagent**: Reviews code/scripts with fresh eyes
- **Document subagent**: Syncs directives/docs with execution code

**Rule:** Use least privilege — each subagent gets only required tools.

## Cloud Deployment (Advanced)

**Do NOT upload full orchestrator!** Instead:

1. Build + test locally first
2. Extract deterministic execution scripts
3. Deploy to cloud (Modal, trigger.dev, etc.)
4. Use webhooks/schedules for triggers
5. Add logging/observability

## Pitfalls

| Pitfall | Solution |
|---------|----------|
| LLM does execution → unreliable | Move to deterministic scripts |
| No guardrails → runaway costs | Add cost thresholds, privilege limits |
| No logging → can't debug | Require change_log.md for all modifications |
| All sequential → slow throughput | Use parallel agents for independent tasks |
| Upload stochastic to cloud → chaos | Only deploy deterministic execution |
| No testing → production failures | Test with real data + fresh instances |

## When to Use

✅ **Use DO Framework for:**
- Business workflows requiring consistency
- Repeated tasks (daily/weekly)
- Multi-step processes with tools
- Tasks needing audit trails

❌ **Don't use for:**
- One-off creative tasks
- Simple Q&A
- Brainstorming sessions

## Tools Integration

- **MCP**: Use for standardized integrations but be aware of token cost
- **Skills**: Package directives + scripts + assets for reuse
- **Terminal scripts**: Best for lightweight deterministic execution

---

## Quick Reference

```
DO = Directive (markdown SOP) + Orchestration (LLM) + Execution (scripts)
Guardrails = cost limits, least privilege, logging, no credential changes
Self-Annealing = error → fix → log → improve
Test = real data + fresh instance + 10-15 runs
Deploy = only deterministic execution to cloud
Scale = parallel agents + subagents (reviewer/document)
```
