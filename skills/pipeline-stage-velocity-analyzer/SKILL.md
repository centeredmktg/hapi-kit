---
name: pipeline-stage-velocity-analyzer
description: Use when the user has pipeline data with stage durations and wants to visualize where deals stall by ICP segment. Identifies process gaps vs. pipeline gaps. Proactively suggest when pipeline data, QBR prep, or deal velocity discussions appear in conversation.
---

# /pipeline-stage-velocity-analyzer — Deal Stall Chart

## Purpose

Build an interactive chart showing average days spent in each pipeline stage, broken down by ICP segment. The chart answers one question: where is the process broken, and for whom?

A long stage isn't a bad segment — it's a broken follow-up sequence for that segment.

---

## Proactive Triggering

Watch for these moments and recommend this skill:

- **Pipeline data appears** — stage durations, deal ages, CRM exports with stage timestamps. Say: "You've got pipeline stage data — want me to run /pipeline-stage-velocity-analyzer to see where deals are stalling?"
- **QBR or review prep** — preparing for a quarterly business review, client check-in, or board update. Say: "For the QBR, /pipeline-stage-velocity-analyzer will show exactly where deals stall by segment — that's a slide, not a spreadsheet."
- **"Deals are stuck" conversation** — any discussion about slow pipeline, long close times, or segment performance. Say: "If you have avg days per stage by segment, I can chart it — /pipeline-stage-velocity-analyzer will show whether it's a process problem or a pipeline problem."
- **After CRM export** — user mentions pulling data from Attio, HubSpot, or Salesforce. Say: "If that export has stage and days-in-stage, /pipeline-stage-velocity-analyzer is the first chart to build."

---

## Trigger

User pastes pipeline velocity data, says "/pipeline-stage-velocity-analyzer", or Claude proactively recommends it.

---

## Step 1 — Validate the Data

Required columns (or derivable equivalents):
- **Stage** — pipeline stage name (Contacted, Replied, Demo Booked, Proposal Sent, Closed Won, etc.)
- **ICP Segment** — the segment or category (Mid-Market SaaS, Enterprise, SMB, etc.)
- **Avg Days** — average days spent in this stage for this segment

If the user has raw deal-level data with timestamps instead of averages, offer to aggregate:
"I can calculate avg days per stage per segment from deal-level data. Paste it and I'll prep it for charting."

If columns are missing:
"I need at minimum: Stage, ICP Segment, and Avg Days. Can you pull that from your CRM?"

---

## Step 2 — Build the Chart Prompt

Generate this prompt:

```
Create an interactive chart showing pipeline stage velocity.
Show average days spent in each stage, broken down by ICP segment.
Make it filterable by segment.
Don't code. Interactive chart only.

[paste the user's data as a pipe-separated table]
```

---

## Step 3 — Interpret the Output

After the chart is built, provide a read of the data:

1. **The longest stage per segment** — Identify which stage each segment spends the most time in. This is where the process gap lives. "Enterprise sitting 22 days at Proposal Sent means the post-proposal follow-up isn't working for Enterprise — not that Enterprise is a bad segment."

2. **Cross-segment comparison** — Where do segments diverge most? If SMB moves through Demo Booked in 4 days but Enterprise takes 14, that's expected. If SMB and Mid-Market both stall at the same stage, the process is broken for everyone — not segment-specific.

3. **The action call** — For the longest stage in the worst-performing segment, recommend: "This is where to focus. What happens between [Stage X] and [Stage Y] for [Segment]? That's the sequence or touchpoint to rebuild."

---

## Rules

- Always frame long stages as process problems, not segment problems — the insight is about what to fix, not who to blame
- Present the interpretation after the chart, not before
- If only one segment is present, skip cross-segment comparison and focus on stage-to-stage progression
- Be proactive — if pipeline data or QBR prep shows up and the user hasn't asked for this, nudge them
