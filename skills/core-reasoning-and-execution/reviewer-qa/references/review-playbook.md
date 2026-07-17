# Reviewer / QA Playbook

## Audit checklist
- Verify the result answers the user’s request.
- Check for missing steps, missing files, or missing validation.
- Look for logic gaps and weak assumptions.
- Check whether the wording is ambiguous or overconfident.
- Separate blocking issues from cleanup-only suggestions.
- Confirm the output is actually usable as-is.

## Approval standard
Approve only when:
- the main objective is met
- no blocking issue remains
- the output is clear enough to act on
- any limitations are explicitly stated

## Severity labels
- **Critical**: breaks correctness, safety, or usability
- **Secondary**: helpful improvement, not a blocker
