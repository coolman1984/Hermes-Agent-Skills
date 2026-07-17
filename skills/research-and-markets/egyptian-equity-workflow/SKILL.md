---
name: egyptian-equity-workflow
description: "Master workflow for Egyptian stock conversations: snapshot, constitution, source hierarchy, text-only Camoufox, sector/stock gates, and review cadence."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [investing, egypt, stocks, sectors, workflow, research]
---

# Egyptian Equity Workflow

Use this skill whenever the conversation touches:
- Egyptian stocks
- sectors
- sector maps
- portfolio construction
- screening
- valuation
- bank sleeves
- FX/export exposure
- market context
- thesis review

## Canonical vault files
Read these before answering, in this order:
1. /root/Documents/Obsidian Vault/CURRENT-SNAPSHOT.md
2. /root/Documents/Obsidian Vault/egx_system/portfolio/rules.md
3. /root/Documents/Obsidian Vault/egx_system/playbook/investment_constitution.md
4. /root/Documents/Obsidian Vault/egx_system/playbook/sector_map.md
5. /root/Documents/Obsidian Vault/egx_system/playbook/workflow.md
6. /root/Documents/Obsidian Vault/Investing/EGX Portfolio Monitoring System.md
7. /root/Documents/Obsidian Vault/egx_system/portfolio/positions.csv
8. /root/Documents/Obsidian Vault/egx_system/portfolio/watchlist.txt
9. Legacy context if needed: /root/Documents/Obsidian Vault/Projects/دستور عملي لاختيار القطاعات المتكاملة في البورصة المصرية.md
10. Legacy context if needed: /root/Documents/Obsidian Vault/Projects/دستور قرار الاستثمار في البورصة المصرية.md
11. Legacy context if needed: /root/Documents/Obsidian Vault/Projects/منهج اختيار القطاعات المتكاملة.md
12. Legacy context if needed: /root/Documents/Obsidian Vault/Projects/سلم مصادر التحليل اليومي والساعة.md
13. Legacy context if needed: /root/Documents/Obsidian Vault/Projects/دليل التشغيل اليومي الأسبوعي الشهري للبورصة المصرية.md
14. Legacy context if needed: /root/Documents/Obsidian Vault/Projects/مشروع الاستثمار في البورصة المصرية.md

## Non-negotiable order
1. Review the snapshot and the latest project docs.
2. Apply the constitution.
3. Use the source hierarchy.
4. Then answer the stock or sector question.

## Hard rules
- Apply the acceptable-Sharia activity filter first: exclude blatant riba-heavy conventional banks/lenders, tobacco, alcohol, gambling, and clearly suspect core businesses.
- For the financial sleeve, prefer Islamic banks or clearly acceptable financial infrastructure; do not force broader conventional-bank exposure.
- Universe and liquidity gate before any sector call.
- Sector names are not enough; the function matters.
- Do not force five sectors if clean names do not exist; five is a target shape, not a quota.
- Prefer cash over filling a slot with a weak name.
- Distinct drivers matter more than broad diversification.
- Avoid mixed-energy names as fake hedges.
- When the user's mandate is fast capital growth, allow high-but-calculated risk and tighter concentration instead of over-diversifying.
- Full stock reports are frozen until the user explicitly lifts the freeze.
- Use Camoufox for text extraction only.
- No routine screenshots or image-based workflow.
- If a page is blank in text, move to an alternate text URL, disclosure, or PDF.
- If a referenced file is missing or renamed, resolve the closest canonical document by searching the vault before assuming it is absent.
- If no textual source exists, say so plainly.
- Refresh any date-specific example during the monthly review; treat dated numbers as examples, not permanent truth.
- Five sectors is a target shape, not a quota; do not force a full set when the clean universe is smaller.

## Source hierarchy
Official first:
EGX, company IR/filings, company disclosures, CBE, CAPMAS, FRA, and sector regulators
Local market tape second:
Mubasher, ArabFinance, Alborsa News
Interpretation third:
IMF, S&P PMI, World Bank commodities, EFG Hermes research
Timing and confirmation last:
Reuters, Reuters market pages, TradingView, Investing

## Portfolio mandate defaults
- Default objective: fast capital growth, with high but calculated risk.
- Prefer concentration over over-diversification when the user is optimizing a small-to-medium EGX portfolio.
- Treat tiny positions with no real portfolio function as capital-allocation mistakes to review aggressively.
- Use the acceptable-Sharia activity filter, not a rigid label-only "Sharia stocks" filter.

## Difficult-source rule
- For hard-to-extract links such as X/Twitter, Substack, and pages that fail normal extraction, go directly to Camoufox in text-first mode.
- Do not waste time repeating weak extraction paths when Camoufox is the cleaner route.
- If EGX or Mubasher blocks direct extraction, fall back in this order: indexed result snippets -> company IR page -> alternate text page/PDF -> explicit uncertainty note.

## Sector analysis template
For each sector:
- function
- risk it protects against
- what helps it
- what hurts it
- when it outperforms
- what offsets it if it weakens
- whether it truly adds a distinct driver

## Stock analysis template
For each stock:
- sharia fit
- liquidity
- governance
- leverage
- cash flow
- pass-through ability
- valuation as confirmation only
- real catalyst
- exit / invalidation rule

## Review cadence
- before market: Reuters, commodities, then EGX + CBE + FRA + sector regulator if relevant
- during market: EGX30, core holdings, short watchlist, and any fresh disclosure; do not chase
- after close: ask four questions — new EGX disclosure? macro/regulatory change? unexplained move? changed sector relations? — then write a 5-line memo
- weekly: CBE + CAPMAS + PMI + Reuters, then rank the actual sectors in play (up to 5), then stocks inside each sector, then next-week weights
- monthly: CBE + CAPMAS + PMI + IMF + World Bank + company results => new month map; if no clean sector is left, cash remains a valid output
- quarterly: financial statements and thesis reconciliation

## Output style
- concise
- decision-oriented
- state uncertainty
- do not invent blank data
- prefer clean answers over noisy ones

## If the user wants a quick answer
Give the shortest correct answer that still respects the constitution and source hierarchy.

## If the user wants a portfolio proposal
Treat it as a draft until it passes:
- sharia
- liquidity
- sector function
- company quality
- sizing
- exit
- review cadence

## If the user asks for a full stock report
Check the active memory and the current snapshot before generating it. If the report freeze is still active, do not produce a full report unless the user explicitly lifts it.
