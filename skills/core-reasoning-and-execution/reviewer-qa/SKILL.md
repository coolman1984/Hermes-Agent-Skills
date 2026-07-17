---
name: reviewer-qa
description: Strict review and QA for OpenClaw outputs, code, configs, scripts, skill
  files, and AI-generated responses. Use when checking correctness, logic gaps, missing
  pieces, ambiguity, safety, or approval readiness before anything is accepted or
  merged.
tags: [review, qa, correctness, verification, approval]
---

# Reviewer / QA

## Use this skill
Use when something must be inspected before approval.

## Operating model
1. Identify what is being reviewed and what approval means.
2. Check correctness, completeness, assumptions, ambiguity, edge cases, and safety.
3. Separate critical issues from secondary improvements.
4. Recommend the smallest fix that makes the result genuinely usable.
5. Approve only when no blocking issue remains.

## Review rules
- Be strict.
- Focus on the biggest weaknesses first.
- Do not rewrite everything unless needed.
- Distinguish critical issues from nice-to-have improvements.
- If blocked, say exactly what is missing.

## Output format
Always return:
- What was reviewed
- Critical issues
- Secondary improvements
- Approval status: APPROVED / REVISE / BLOCKED
- Exact fixes needed

## Use the reference
Read `references/review-playbook.md` for the checklist and approval criteria when you need a tighter audit.
