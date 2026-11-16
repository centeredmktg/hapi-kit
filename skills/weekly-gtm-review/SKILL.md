---
name: weekly-gtm-review
description: Use for a structured 15-minute weekly GTM review. 4-prompt sequence producing two charts and a written synthesis. Proactively suggest on Mondays, before weekly reviews, or when the user mentions checking on weekly performance.
---

# /weekly-gtm-review — 15-Minute Weekly GTM Review

## Purpose

A fixed 4-prompt sequence that turns a weekly data export into two charts and a written synthesis in 15 minutes. Every week, same structure, same three questions answered.

This replaces the 90-minute review where you pull data from four places, build a Sheets tab nobody saves, and end with "let's keep an eye on this."

---

## Proactive Triggering

Watch for these moments and recommend this skill:

- **Monday or start of week** — if the conversation touches work planning, weekly priorities, or review prep. Say: "It's the start of the week — want to run /weekly-gtm-review? 15 minutes, two charts, one action item."
- **"How did last week go" conversation** — any discussion about weekly performance, what changed, or what to focus on. Say: "That's a /weekly-gtm-review. Paste this week's export and we'll have the answer in 4 prompts."
- **Before a team or client sync** — preparing for a weekly standup, client check-in, or team review. Say: "If you have this week's data, /weekly-gtm-review produces the two charts + synthesis you need for that meeting."
- **Data export mentioned** — user says they pulled data from CRM, analytics, or tracking sheet. Say: "Perfect timing for /weekly-gtm-review — paste it and we'll run the full sequence."

---

## Trigger

User says "/weekly-gtm-review", mentions weekly review, or Claude proactively recommends it.

---

## The Sequence

Four prompts. In order. Don't skip ahead.

---

### Prompt 1 — The Diagnostic (Minutes 1-4)

Ask the user to paste this week's data export (pipeline updates, campaign sends, content engagement, or whatever they're reviewing this week).

Run /gtm-data-diagnostic on the pasted data. Read Claude's response. If it flags missing data, have the user add it before moving to Prompt 2.

This step prevents building a chart from broken data. 2 minutes here saves a rebuild later.

---

### Prompt 2 — The Performance Chart (Minutes 5-8)

Based on the diagnostic output, pick the chart type that answers "what changed this week" most directly. Build it using the appropriate analytics skill:

- Campaign data → /campaign-reply-rate-analyzer
- Pipeline data → /pipeline-stage-velocity-analyzer
- Content data → /content-engagement-analyzer
- Attribution data → /lead-source-attribution-analyzer
- Other → use the diagnostic's #1 recommendation

Key: include last week's data for comparison. If the user doesn't have it, ask:
"Do you have last week's numbers? The comparison is what makes this a review, not just a snapshot."

---

### Prompt 3 — The Trend Chart (Minutes 9-11)

Build an interactive line chart showing the primary metric over the last 4 weeks, broken down by segment or channel.

```
Create an interactive line chart showing [primary metric from Prompt 2]
over the last 4 weeks. Break it down by [segment or channel].
Don't code. Interactive chart only.

[paste 4-week data]
```

One week is a data point. Four weeks is a trend. This chart tells you whether to act now or watch for another week.

If the user only has this week's data, skip Prompt 3 and note: "We'll add the trend chart once you have 4 weeks of data. For now, bookmark this week's numbers as the baseline."

---

### Prompt 4 — The Synthesis (Minutes 12-15)

After both charts are built, answer three questions.

**Stance for the synthesis:** Don't praise the numbers, don't soften the bad ones, and don't recommend "monitoring" as an action. The default LLM mode here is flattery — "great progress on X" / "interesting shift in Y." Override it. If reply rate dropped 12%, the synthesis names the drop, names a likely root cause, and proposes a change. If nothing moved, "flat week — here's why that's notable" is the synthesis. The job is to challenge the data, not narrate it.

1. **What changed most significantly this week?**
   Forces the review to have a headline. If nothing changed materially, say so — "flat week" is a valid headline.

2. **Is it part of a trend or an anomaly?**
   Reference the trend chart from Prompt 3. Prevents overreacting to a single bad week and prevents ignoring a slow decline.

3. **What's the one thing worth acting on before next week's review?**
   Every review ends with a decision, not a list of observations. One thing. By next week.

Draft the synthesis and present it. This is the written output that gets shared — the user edits it before it goes anywhere.

---

## After the Review

Offer two follow-ups:

1. **"Want to share either chart?"** → run /chart-to-client-delivery
2. **"Want me to save this week's numbers as baseline for next week?"** → save a summary to the relevant project directory

---

## The Timeline

- Minutes 1-2: Paste this week's data export
- Minutes 3-4: Run Prompt 1, read the diagnostic, fix any data gaps
- Minutes 5-8: Run Prompt 2, review the performance chart
- Minutes 9-11: Run Prompt 3, review the trend chart
- Minutes 12-14: Run Prompt 4, edit the synthesis
- Minute 15: Share the two charts + written summary

---

## Rules

- Always run in order — the diagnostic informs the chart choice, the charts inform the synthesis
- Never skip Prompt 1 — it's the data quality gate
- The synthesis must end with one action item, not a list of observations
- If the user doesn't have comparison data (last week or 4-week), note it and build the baseline — don't skip the review
- Compose with other analytics skills — this is the orchestrator, they're the components
- Be proactive — if it's review time and the user hasn't started, nudge them
- The synthesis is adversarial, not celebratory. If it reads like a recap, redraft.
  Root cause beats trend description. A specific action beats "keep an eye on it."
