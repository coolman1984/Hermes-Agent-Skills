---
name: egyptian-sector-portfolio-audit
description: "Audit an Egyptian equity sector map or portfolio proposal against a disciplined constitution: sharia first, then universe and liquidity, then sector function, then company quality, valuation, sizing, exit, and review cadence."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [investing, egypt, portfolio-construction, audit, research]
---

# Egyptian Sector Portfolio Audit

Use this skill when the user gives a proposed Egyptian stock-market sector map, portfolio structure, or a list of candidate names and asks whether it really follows the investing constitution.

## Purpose
Do not judge the proposal by whether it sounds balanced or looks diversified. Judge it as a hierarchy of gates and functions.

## Mandatory hierarchy
1. Sharia filter first
2. Investable universe and liquidity gate
3. Sector function gate
4. Company quality gate
5. Valuation as a confirmation layer, not the first decision layer
6. Sizing and concentration rules
7. Exit and invalidation rules
8. Review cadence

## Core audit questions
- Does every sector add a distinct hedge or opportunity?
- Are there more than two sectors sharing the same main profit driver?
- Is there a cash fallback if clean names are not available?
- Does any suggested bank sleeve contain only Islamic banks?
- Is the external hedge actually FX or export exposure with low energy sensitivity, or just a mixed bag of names?
- Are highly energy-sensitive names being used as hedges by mistake?
- Is the stock-level analysis based on quality and liquidity, or only on analyst target prices?
- Are pass-through ability, cash flow, leverage, and governance checked?
- Are sector weights and stock weights capped clearly?
- Is there a clear exit rule when the thesis breaks?

## What to flag as missing
Flag any proposal that lacks one or more of these:
- investable universe definition
- minimum liquidity threshold
- cash fallback
- maximum weight per stock, sector, and shared driver
- explicit invalidation rule
- monthly and quarterly review cadence
- governance, political, and regulatory risk treatment where relevant
- low-energy requirement for any external hedge sleeve
- proof that the proposal does not force five sectors just to complete a template

## How to evaluate a sector map
For each sector, write:
- Function inside the portfolio
- Risk it protects against
- What helps it
- What hurts it
- When it outperforms
- Which other sleeve offsets it if it weakens
- Whether the main driver is truly different from the other sleeves

## How to evaluate a stock inside a sector
For each stock, check:
- Sharia compatibility
- Liquidity and tradability
- Ability to pass through cost inflation
- Debt burden
- Cash flow quality
- Management and governance quality
- Whether valuation is a confirmation or just an excuse
- Whether there is a real catalyst, not just a story

## Output style
Return three layers:
1. Verdict: fit, partial fit, or reject
2. What matches the constitution
3. What must be fixed before execution

Then add a short corrected interpretation of the proposal.

## Default bias
- Prefer cash over forced completion
- Prefer a smaller clean portfolio over a fuller weak one
- Prefer a genuinely low-energy external hedge over an emotionally appealing exporter list
- Prefer Islamic banks only when the bank sleeve is used
- Prefer sector-function thinking over sector-name thinking

## Practical note
If the user’s proposal is good at a macro level but violates the constitution at the stock or gating level, treat it as a strong draft, not a final implementation.
