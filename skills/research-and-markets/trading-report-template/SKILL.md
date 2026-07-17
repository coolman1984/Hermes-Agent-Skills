---
name: trading-report-template
description: Reusable template and workflow for producing concise, decision-oriented
  trading reports. Use when the user asks for a trading report, market review, trade
  setup, or wants a standardized report format that should be maintained over time.
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [trading, report, portfolio, markets, template, analysis]
---

# Trading Report Template

Use this skill to create or update a trading report that includes the portfolio, opportunities, and a clear action plan.

## Output modes
- Long report: full context, portfolio, opportunities, news, risks, and scenarios
- Signal report: short, sharp, execution-focused guidance with key levels only
- Portfolio monitoring report: recurring update for a live holdings list, prioritizing the positions with the largest portfolio impact and stating what needs action now vs simple monitoring
- If the user does not specify, prefer the short signal report for live trading questions and the long report for review or analysis requests

## Portfolio monitoring mode
Use this when the user shares current holdings, screenshots of open positions, or asks for recurring portfolio follow-up.
- First extract holdings from the screenshots: ticker, quantity, approximate current value, and visible P/L if shown
- Treat the extracted holdings as the active portfolio unless the user later sends an update
- Verify the arithmetic before analyzing: confirm total portfolio value equals the sum of positions, recalc each weight from the source values, and flag any mismatch or rounding drift
- Compute concentration metrics every time: top 3 weight, top 5 weight, count of positions above 5%, count below 2%, and whether the portfolio is really concentrated in a small core
- If the user’s own sector subtotal or summary is provided, check it for internal consistency and point out missing or misclassified names when detected
- Rank positions by portfolio impact, not just by daily P/L; the largest holding should usually be discussed first
- In recurring updates, explicitly identify:
  - the most important position now
  - the riskiest position now
  - the strongest position now
  - which names need action now versus only monitoring
- Keep the report short and focused, but rich in decision value
- Present each stock in its own mini-block
- Always include the Arabic company name next to the ticker when possible
- For each stock, include only the fastest decision-making fields: current stance, the most relevant news/catalyst, risk level, and the action now
- For each stock, also include practical trading numbers whenever they can be estimated or sourced: nearest support, nearest resistance, calm entry zone, breakout entry, first target, invalidation, and bearish confirmation/stop area
- Use expressive, helpful emoji that clarify the meaning instead of decorating only
- If exact average cost, cash, or open orders are missing, say so clearly and lower confidence where that affects the recommendation
- Separate structural analysis from full stock calls when the report freeze is active; if full stock reports are frozen, give a holdings-structure audit instead of a stock-by-stock recommendation set
- For hourly session updates, focus on what changed since the last view: news, disclosure, liquidity, unusual volume, breakdowns, breakouts, and whether the move is meaningful for the portfolio rather than for the stock in isolation

### Preferred portfolio report format for Mohamed
Use this exact style unless Mohamed asks for a change:

📂 متابعة المحفظة الآن
🕘 الوقت: {Cairo time}

🧭 نظرة سريعة على المحفظة
- النظرة العامة: ...
- أهم مركز: ...
- أقوى اسم أساسيًا: ...
- أكثر مركز يحتاج حذر: ...

Then list each stock in a separate compact block like this:

{sector_emoji} {ticker} — {Arabic company name}
{signal_emoji} النظرة: {brief stance}
📰 الأهم: {most relevant current news/catalyst}
💧 السيولة: {supported / weak / needs confirmation / accumulation-distribution note}
📍 الدعم: ...
📍 المقاومة: ...
✅ دخول هادئ: ...
🚀 دخول اختراق: ...
🎯 الهدف الأول: ...
⛔ إلغاء الفكرة: ...
❌ تأكيد السلبية: ...
✅ القرار: {hold / trim / add / exit / monitor} + {very short reason}

Close with:
📌 الخلاصة التنفيذية السريعة
- ...
- ...
- ...

Important style rules for Mohamed:
- Warm, human, useful tone
- Compact, clean layout
- Every stock on its own
- Arabic company name included
- Practical numbers are mandatory whenever reasonably estimable
- Use Cairo time explicitly
- This is a message to Mohamed, so optimize for rapid decision-making, not essay-like narration

### Signal report format (preferred when the user asks for the short version)
Use this structure exactly unless the user requests otherwise.
Formatting preference from Mohamed: remove extra blank lines, keep the layout tight and highly professional, and always show the analysis timestamp in Cairo time explicitly.
Tone preference from Mohamed: signal reports should feel warm, human, and useful — not stiff, robotic, or overly harsh.
When the report mentions news, do not say there is no news without checking. Research the nearest relevant company/stock news first and, when useful, include up to 3 recent items with a one-line impact summary for the stock.

🚦 إشارة اليوم على {ticker}

{signal_emoji} {signal_title}
{one_to_three_lines_of_plain_language_judgment}

درجة المخاطر:
{low_medium_high}

السعر العادل:
{value_or_not_available}

مضاعف ربحية الشركة:
{value_or_not_available}

مضاعف ربحية القطاع:
{value_or_not_available}

📰 تأثير الأخبار على السهم
{news_impact_or_no_confirmed_news}

🎯 إشارات الدخول والخروج الاحترافية

✅ دخول هادئ:
{support_entry_plan}

🚀 دخول اختراق:
{breakout_entry_plan}

🎯 الهدف الأول:
{target_1}

⛔ إلغاء الفكرة:
{invalidations_primary}

❌ تأكيد السلبية:
{bearish_confirmation}

🔮 السيناريوهات المتوقعة

السيناريو الإيجابي:
{bull_case}

السيناريو الأساسي:
{base_case}

السيناريو السلبي:
{bear_case}

🔻 الحكم الصريح

{explicit_judgment}

الخلاصة التنفيذية

- {action_line_1}
- {action_line_2}
- {action_line_3}

📌 الخلاصة النهائية:
{final_bottom_line}

📅 تاريخ التحليل: {timestamp}

## Purpose
- Summarize market state
- Review the portfolio and current exposure
- Identify opportunities and watchlist candidates
- State risk clearly
- Produce a report that can be reused and updated over time

## Analysis framework (mandatory before giving a trading judgment)
Evaluate the stock through these layers, in order:
1. Company fundamentals: latest results, EPS, revenue, margins, debt, cash flow, management quality, official disclosures
2. Egyptian macro: interest rates, EGP/USD, inflation, liquidity, debt and budget pressure
3. Sector/global drivers: raw material prices, energy costs, export conditions, Fed/global risk appetite
4. Political/regulatory drivers: CBE decisions, government policy, sector regulation, state ownership/institutional moves, credit-rating headlines
5. Technical/internal market behavior: support/resistance, unusual volume, foreign flows if known, accumulation/distribution, speculation risk

## Extra factors to check when available
- Free float and shareholder concentration
- Insider or major shareholder buying/selling
- Capital increases, stock splits, dividends, rights issues
- Receivables, inventory build-up, and cash conversion quality
- FX exposure: imported inputs, export revenue, dollar debt
- Legal/tax disputes and audit remarks
- Seasonality and one-off gains/losses
- Liquidity depth and slippage risk
- Fair value estimate, company P/E, and sector P/E comparison
- Daily liquidity behavior: value traded, unusual volume, share of market turnover, and whether price is supported by volume

## Valuation block (include whenever available)
- Fair value: use a credible source when available; if estimating directly, Graham-style shortcut may be used with EPS and BVPS, clearly labeled as an estimate
- Company P/E = share price / EPS
- Sector P/E: compare the company against its EGX sector multiple, and explain whether it looks cheap, fair, or expensive on that basis
- Do not present valuation figures as certain if source data is stale, partial, or unavailable

## Liquidity-reading block (mandatory for short trading signals when data is available)
Check:
- Total market turnover for the day
- The stock's share of market turnover
- Whether volume is above/below recent average
- Whether price rise is confirmed by strong volume or happening on weak volume
- Early-session liquidity behavior, especially the first 30 minutes when relevant

## Source hierarchy for Egyptian stock reports
Use sources in this order when possible:
1. Official EGX source for disclosures, financial statements, dividends, capital actions, and market statistics
2. Mubasher, ArabFinance, and Alborsa News for near-real-time company news and market color
3. TradingView and Investing for charts, ratios, comparative market data, gold, FX, and international market context
4. Asharq Bloomberg, CNN Arabic, Sky News Arabia, and Al Araby for political/regional/global developments that may affect Egyptian equities
5. For local gold and USD context, cross-check Egyptian-market pricing with local financial portals and global spot references

Practical rule:
- EGX settles facts
- Financial news sites explain the event
- Chart/data platforms confirm price, volume, and valuation context
- Political/global outlets explain external pressure on sentiment and flows

### EGX access fallback (important)
In some environments, direct fetch of EGX pages may fail (timeouts/connection reset/browser platform limits). If that happens:
1. Resolve each ticker to its EGX ISIN and use the official StocksData URL format:
   - `https://www.egx.com.eg/en/StocksData.aspx?ISIN={ISIN}`
2. Pull indexed EGX snippets via search when direct page extraction is blocked.
3. Extract only fields explicitly visible from EGX snippet text (e.g., `Close Price(date)` and `Traded Volume (Over The Period)`).
4. Label data clearly as EGX historical-snippet derived and include the date shown next to close price.
5. Explicitly warn that `Traded Volume (Over The Period)` is not necessarily current-session volume.
6. Provide direct EGX link per ticker so the user can verify quickly.
7. If `web_extract` on `NewsDetails.aspx` returns image/base64 placeholders or a generic wrapper (including meta-text like `Summary of Provided Content` / `no readable article text`), treat the article body as unavailable in this run. Do not quote that wrapper as a factual source; instead rely on EGX search snippets (headline/date/Reuters code) plus Mubasher/ArabFinance for the event context.

### Mubasher extraction fallback (important)
In many runs, Mubasher and some EGX pages are partially login-gated or return image-heavy/JS-heavy output in extract tools. Use this fallback path:
1. Try stock/profile pages first, because they often expose actionable quote blocks even when article pages are limited:
   - `https://english.mubasher.info/markets/EGX/stocks/{TICKER}/`
   - `https://english.mubasher.info/markets/EGX/stocks/{TICKER}/profile/`
   - Optional mobile variant: `https://english.mubasher.info/mobile/EGX/stocks/{TICKER}`
2. Parse only explicitly visible snapshot fields when available:
   - `Last update`, `Open`, `Previous Close`, `High`, `Low`, `Volume`, `Turnover`
3. For news when full article text is blocked, rely on headline-level facts from stock/news/announcements pages and label them as headline-derived.
4. Prioritize recent timestamped items (e.g., treasury stock releases, AGM/EGM invitations, board decisions, FY/Q results) over stale generic analysis pieces.
5. If one source is stale/blocked, triangulate with TradingView/Investing for price context and keep EGX/Mubasher as the fact anchor for disclosures.
6. Never invent exact intraday values for fields you could not verify in this run.
7. Data-quality guardrail: if extracted quote fields look malformed or truncated (e.g., implausible `Open` like `06` while the same page shows a much higher `Previous Close`), treat that field as unreliable and mark it `غير متاح` instead of using it.
8. Prefer `/volume-statistics` pages (Mubasher) for turnover/volume confirmation when stock/profile pages are partial; always keep each symbol’s `Last update` timestamp next to any quote-derived decision.
9. If Mubasher `news` pages are login-gated/image-heavy, rely on dated `announcements` lines + EGX NewsDetails snippets and label conclusions as headline-derived when article bodies are unavailable.
10. If a stock page extract returns mostly icons/menus/login text (little or no numeric quote block), immediately switch to `/announcements/` for that ticker and use its quote snapshot (`Last update`, `Open`, `Previous Close`, `High`, `Low`, `Volume`, `Turnover`) as the operational fallback.
11. Timestamp guardrail: accept `Last update` only when it clearly includes market-session time context (e.g., `AM/PM market time`). If `Last update` looks like a fundamentals date or stale metadata, mark it `غير موثوق` and downgrade confidence.

### Ticker identity guardrail (important)
- Some EGX symbols are easily confused across sources (example: `SAUD` may be indexed as different legacy/company aliases in search results).
- Before assigning any news/disclosure to a holding, verify at least one of:
  1. exact EGX Reuters code in the headline/snippet (e.g., `XXX.CA`), or
  2. company name match from a trusted profile page, or
  3. official EGX company/details page link tied to the same symbol.
- If symbol mapping remains ambiguous in this run, keep the position as `مراقبة` and explicitly say name/ticker confirmation is pending.
- Never merge disclosures from a similarly named but different ticker into the portfolio decision.

### Fast hourly-run query guardrail (important)
- Generic web search queries for ArabFinance/Alborsa are often noisy or off-topic in cron runs (cross-country/company-name collisions). Do not rely on broad queries alone for decision-critical updates.
- For hourly portfolio follow-up, prioritize deterministic endpoints first:
  1. `https://english.mubasher.info/markets/EGX/stocks/{TICKER}/announcements/`
  2. `https://english.mubasher.info/markets/EGX/stocks/{TICKER}/volume-statistics/`
  3. `https://english.mubasher.info/markets/EGX/stocks/{TICKER}/`
- Use EGX/Reuters-code anchored search only as confirmation (e.g., `PHDC.CA`, `ADIB.CA`) and label these as snippet/headline-derived when article bodies are unavailable.
- In short hourly reports, if time is limited, spend research budget on top-impact holdings first, and use announcement-headline deltas + liquidity snapshot rather than deep article parsing for every symbol.

### Confidence + disclosure rule for hourly portfolio updates
- When quote snapshots are mixed-date across symbols, explicitly state that data timeliness differs by ticker.
- If turnover/volume are available, compute each holding’s share of market turnover when possible to support liquidity judgment.
- If cash balance, average cost, or open orders are missing, state that clearly and reduce confidence in add/trim calls.

Rule: fundamentals tell you whether the stock deserves attention; technicals tell you timing; liquidity tells you whether the move is real enough to trust. If core fundamental or disclosure risk is unknown, say so explicitly and lower confidence.

## Report structure

# 📊 Trading Report: {portfolio_or_market}

## 1) 🧭 Executive Summary
- Market bias: bullish / bearish / neutral
- Main conclusion in 1-3 lines
- Overall posture: add / hold / trim / wait

## 2) 🧺 Portfolio Snapshot
- Total positions
- Largest position(s)
- Concentration risk
- Cash / dry powder if known
- Any positions that need review or cleanup

## 3) 🎯 Opportunities
- New opportunities worth watching
- Existing names that are near trigger
- Best risk/reward ideas
- Opportunities ranked by conviction

## 4) 🌍 Market Context
- Trend direction
- Key support and resistance zones
- Volume / volatility notes
- Relevant macro or catalyst context

## 5) 🛠️ Setup Analysis
For each opportunity:
- Entry idea
- Trigger condition
- Stop loss
- Take profit targets
- Risk/reward estimate

## 6) 🔮 Scenarios
- Best case
- Base case
- Worst case

## 7) ⚠️ Risks
- Invalidations
- News/event risk
- Liquidity or slippage risk
- Portfolio concentration risk

## 8) ✅ Action Plan
- What to watch next
- Confirmation needed
- When to enter, hold, reduce, exit, or rebalance

## 9) 🎚️ Confidence
- Confidence level: low / medium / high
- Why the confidence level is what it is

## Formatting rules
- Keep it concise but complete
- Use emoji in section headers for readability
- Separate fact from interpretation
- Do not overstate certainty
- If portfolio data is missing, say so explicitly
- Prefer numbered sections and bullets
- Keep the final report shorter and sharper than a full memo unless the user asks for depth

## Maintenance rule
- If the trading report format changes, update this skill immediately so the skill and the active template stay aligned.
- Treat this skill as the source of truth for the portfolio + opportunities trading report structure unless the user explicitly asks for a different format.

## Source note
- The original reusable report-template pattern was discovered in OpenClaw's memory-system setup flow; this skill adapts that pattern specifically for trading reports.
