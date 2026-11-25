---
name: chart-to-client-delivery
description: Use after any chart has been built and needs to be shared with a client or stakeholder. Converts the chart to standalone HTML and drafts an insight-led delivery message. Proactively suggest after any charting skill produces output that's headed for someone else's eyes.
---

# /chart-to-client-delivery — Share-Ready Chart + Insight Framing

## Purpose

Turn a chart Claude just built into something you can drop into a client Slack or email in under 3 minutes. Two outputs: a standalone HTML file and a delivery message that leads with the insight, not the tool.

A screenshot of a Claude chat window is not a deliverable. A standalone interactive chart with a one-sentence read is.

---

## Proactive Triggering

Watch for these moments and recommend this skill:

- **After any charting skill produces output** — if a chart was just built using any analytics skill and the context suggests it's for someone else (client, stakeholder, team). Say: "That chart is share-ready. Want me to run /chart-to-client-delivery to package it + draft the delivery message?"
- **Client prep or QBR discussion** — charts being built for external consumption. Say: "When the chart is done, /chart-to-client-delivery will convert it to HTML and draft the message — lead with the number, not the tool."
- **"I need to send this" moment** — user mentions sharing, sending, presenting, or attaching a chart. Say: "Let me run /chart-to-client-delivery — standalone HTML + insight-led framing, 2 minutes."

---

## Trigger

User says "/chart-to-client-delivery", mentions needing to share a chart, or Claude proactively recommends it after a chart is built.

---

## Step 1 — Convert to Standalone HTML

Run this prompt on the chart that was just built (or ask the user to confirm which chart):

```
Convert this to a standalone HTML file I can download and share.
All styles and scripts embedded. No external dependencies. One file.
```

The output is a self-contained HTML file with all interactivity preserved — hover states, filters, toggles.

---

## Step 2 — Extract the Headline Number

Before drafting the delivery message, identify:

1. **The one number** — the single most important data point from the chart. Not a summary, not a range. One number. Examples:
   - "Enterprise is sitting 22 days at Proposal Sent"
   - "Referral converts at 31% contact-to-close vs. 1.8% for cold email"
   - "Step 1 voice note is running at 27% vs. 7% for cold email"

2. **The implication** — one sentence on what that number means for the decision at hand

---

## Step 3 — Draft the Delivery Message

Write a delivery message using this structure:

```
[One sentence with the headline number and its implication.]
[One sentence pointing to the chart as evidence.]
[Link placeholder.]
```

**What NOT to write:**
- "Here's a quick chart I made in Claude"
- "I ran some analysis — attached"
- "Let me know if this makes sense"

These make it sound provisional. The client anchors to "quick" and "let me know if" instead of the insight.

**What to write instead:**

Lead with the insight. The chart is evidence. You're the one drawing the conclusion — that's the value.

Examples:

> "Reply rate breakdown from last week's sends is below. Step 1 voice note is running at 27% vs. 7% for cold email Step 1. If we shift more volume to voice note in the next run, that gap compounds fast. [link]"

> "Ran the signal score vs. conversion data through a scatter chart. Clear cluster of converted contacts at signal score 8+ and under 100 employees. Below 6, no pattern at all. Attaching the chart — it makes the case for tightening the list criteria before the next campaign. [link]"

> "Lead source attribution chart is ready for the QBR deck. Referral is converting at 7x the rate of cold email from contact to close. That's the headline. [link]"

Pattern: **One specific number. One direct implication. One link.**

---

## Step 4 — Present for Review

Show the user the delivery message draft. Ask:
"Here's the message. Edit or approve — I'll finalize the HTML file on approval."

---

## Rules

- Never mention Claude, AI, or the tool in the delivery message — the insight is the deliverable, not the process
- Always lead with a number, never with "I attached a chart"
- The HTML file must be fully self-contained — no external CDN links, no dependencies
- One chart per delivery message — if multiple charts need sharing, draft separate messages
- Be proactive — if a chart was just built for external consumption, nudge toward this skill
