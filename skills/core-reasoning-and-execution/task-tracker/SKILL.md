---
name: task-tracker
description: Track task outcomes for self-optimizing agent recommendations
tags: [task-tracking, metrics, self-optimization, outcomes, cli]
---

# Task Tracker Skill

Track task outcomes for self-optimizing agent recommendations.

## Simple Usage (Recommended)

### Record a task outcome:
```bash
python3 ~/.hermes/scripts/task_tracker.py record <type> "<description>" <skills> <agents> <outcome>
```

Example:
```bash
python3 ~/.hermes/scripts/task_tracker.py record coding "fix login bug" developer,systematic-debugging Developer success
```

### Get analytics:
```bash
python3 ~/.hermes/scripts/task_tracker.py stats
```

### Get recommendation:
```bash
python3 ~/.hermes/scripts/task_tracker.py recommend <type>
```

## Task Types

- `coding` - writing or implementing code
- `research` - searching, gathering info
- `writing` - creating content, drafting
- `planning` - designing, architecting
- `review` - reviewing, QA, debugging

## Outcome Values

- `success` - task completed as expected
- `partial` - task done but with issues
- `failed` - task not completed

## Auto-Tracking Setup

To auto-track from skills, add tracking call at end of skill execution.

## File Locations

- Script: `~/.hermes/scripts/task_tracker.py`
- Data: `~/.hermes/task_tracker.json`
