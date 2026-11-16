---
name: roi-business-case
description: Use when a client or operator needs to justify a major investment
to a CFO, board, or executive team. Works for AI tools, software platforms,
service deployments, operational infrastructure, or any significant capex
decision. Produces a board-ready financial model.
---

# /roi-business-case — Investment Business Case Builder

## Purpose

Build a financially rigorous business case for any major investment —
AI tools, software platforms, service deployments, operational infrastructure,
or capex decisions. No CFO funds a project because it sounds cool.
You need hard math, a clear payback period, and a pitch that survives scrutiny.

Output: a board-ready financial model with ROI projections, hidden cost
exposure, payback period, risk factors, and a 2-sentence executive pitch.

---

## Trigger

Invoked with /roi-business-case

The client provides:
- What they're investing in (tool, service, infrastructure, headcount)
- Current baseline cost of the problem being solved (hours × rate, or direct spend)
- Estimated cost to implement (one-time)
- Estimated ongoing cost (monthly or annual)
- Expected efficiency gain or revenue impact (%)

If any of these are missing, ask. Do not build a model on assumptions.

---

## Process

### Step 1 — Gather Inputs

Confirm all five inputs are present and specific enough to calculate.
If efficiency gain is expressed as a vague range ("20-40%"), push for
a conservative single number. Models built on ranges mislead executives.

### Step 2 — Calculate Hard ROI

Annual value generated = baseline cost × efficiency gain %
(or projected revenue impact if this is a growth investment)

Show the math clearly. Do not round aggressively. Conservative estimates
build credibility; optimistic ones destroy it in the Q&A.

### Step 3 — Surface the Hidden Costs

Identify 3–4 implementation costs the client likely didn't account for.
These vary by investment type — examples:

- Software: API usage at scale, user training, data migration, integration eng
- Services: internal coordination overhead, change management, ramp time
- Infrastructure: compliance reviews, ongoing maintenance, documentation
- Headcount: recruiting cost, onboarding lag, productivity ramp (typically 90 days)

Be specific to the investment described, not generic.

### Step 4 — Calculate Payback Period

Payback (months) = Total implementation cost ÷ (annual value ÷ 12)

If hidden costs materially change the payback, recalculate with them included
and flag the difference.

### Step 5 — Identify Risk Factors

The top 2 financial risks that could destroy this ROI.
Not theoretical risks — specific, plausible scenarios based on the
investment type and client context.

### Step 6 — Write the Executive Pitch

2 sentences. CFO-grade. Financial metrics and time-to-value only.
No adjectives. No enthusiasm. Just math and timeline.

---

## Output Format

```
# Investment Business Case
Client: [name]
Investment: [what they're buying / building / deploying]
Date: [today]

## The Math

Current annual cost of problem: $[x]
Expected efficiency gain: [x]%
Annual value generated: $[x]
Implementation cost (one-time): $[x]
Ongoing cost (annual): $[x]
Net annual benefit (Year 1): $[x]
Net annual benefit (Year 2+): $[x]

## Hidden Costs

1. [Specific cost]: ~$[x] or [x] hours
2. [Specific cost]: ~$[x] or [x] hours
3. [Specific cost]: ~$[x] or [x] hours
4. [Specific cost]: ~$[x] or [x] hours

## Payback Period

[x] months to break even (excluding hidden costs)
[x] months to break even (including hidden costs)

## Top Financial Risks

1. [Risk]: [How it destroys the ROI and by how much]
2. [Risk]: [How it destroys the ROI and by how much]

## Executive Pitch

[2 sentences. Numbers and timeline only.]
```

---

## Rules

- Conservative estimates only. If the client inflates the efficiency gain,
  push back with a lower number and explain why.
- Show math at every step. Executives will challenge the model —
  make it auditable.
- Payback period must be calculated twice: with and without hidden costs.
- The executive pitch is exactly 2 sentences. Not 3.
- Do not build a model until all five inputs are confirmed.
