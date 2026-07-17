# Operations / Cleanup Playbook

## Inspect for waste
- duplicate config blocks
- stale aliases or wrappers
- redundant files
- leftover logs and temp artifacts
- repeated documentation that can be consolidated
- hardcoded paths that should be centralized

## Preferred actions
- consolidate before deleting
- remove only after checking impact
- keep one canonical source of truth
- make reversible changes when possible
- log any meaningful cleanup or behavioral change

## Risk labels
- **Low**: reversible, clearly safe
- **Medium**: could affect workflows if misapplied
- **High**: affects startup, routing, data, or access
