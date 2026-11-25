---
name: viz-advisor
description: Use when the user has data and a question and wants a chart, graph, plot, or visual of any kind; when they ask "how should I show this", "what chart should I use", or "visualize this"; when gtm-data-diagnostic hands off a top pick; or before any chart code is written. Applies to any domain (GTM, DSCR deals, job costs, class grades, survey results).
---

# /viz-advisor — Recommend the Chart, Teach the Why, Then Route

## Purpose

Decide the single best visualization for this data and this question, explain the reasoning so the user learns the principle (Miyagi: the lesson is embedded in the doing), confirm with the user, then hand off to `/chart-build`.

This skill never draws. It decides, teaches, gates, and routes. Building happens in `/chart-build`; grading happens in `/chart-qa`.

Upstream: `gtm-data-diagnostic` (GTM data quality and "what's worth charting") sends work here when the user is unsure which chart form fits. When the user picks one of its three recommendations, that pick is the gate and it goes straight to `/chart-build`. Downstream: `/chart-build <family>` → `/chart-qa` → `chart-to-client-delivery` when the chart is headed to someone else.

---

## Step 1 — Read the Data

Before recommending anything, profile what's actually there. For each column note:

- **Type:** continuous numeric · discrete numeric · unordered category · ordered category · date/time · text
- **Cardinality** for categories (how many distinct values)
- **Range** for numerics (does it span orders of magnitude? is it a ratio? are there impossible regions like negative counts?)
- **Row count** (n per group matters: violins and densities need enough points; sparse groups get raw points)

Also note what's missing that the question needs (e.g. the question is about spread but you only have averages; the question is about change but there's no time column). If something essential is missing, say so in Step 3 and recommend the best chart for the data you *do* have.

If no data is attached, ask for it, or for the column list and a few sample rows. Don't recommend from the question alone.

## Step 2 — Name the Question Type

Classify the reader's question into exactly one primary type:

| Type | Reader is asking |
|---|---|
| amounts | How big is each one? Which is biggest? |
| distributions | How are values spread? What's typical, what's an outlier? |
| proportions | What share of the whole is each part? |
| associations | Does X move with Y? |
| time-trends | How did it change over an ordered sequence? |
| geospatial | Where is it? How does it vary by place? |
| uncertainty | How sure are we? What's the range of outcomes? |

Play it back in one line: *"You're asking whether [metric] differs across [groups]: that's an amounts question."* If the question is really two questions, say so and recommend handling them as two figures.

Also capture: **audience** (expert / lay / executive) and **medium** (client deck, LinkedIn post, class slide, internal doc, dashboard). Both change the answer. If they aren't clear from context, assume and state the assumption.

## Step 3 — Recommend One Chart

Look up the question type + data shape in `references/chooser.md`. Pick the top-ranked option that fits. Then present the recommendation in exactly this shape:

```
**Recommendation: [chart form]** — [one-line description of what it will look like]

**Why this one:** [2–3 sentences tied to THIS data: the question type, the data shape, the audience]

**The principle:** [one teachable sentence the user can reuse next time — e.g. "Bars encode
value as length from zero, so when all your values sit between 60 and 80, bars make them look
identical; dots on a trimmed axis show the gap."]

**What I ruled out:** [the runner-up and the trap, one line each, with why]

**The point the title will make:** "[draft assertive title — a sentence, not a label]"

**Build this?** Or pick the runner-up, or change the question.
```

The block above is the whole reply's opening: the one-line question playback, then **Recommendation**. Data caveats (missing columns, small samples, a second question that needs its own chart) go *after* "Build this?", at most 3 bullets. Derived-metric tables go there too, only if needed.

Rules for the recommendation:
- **One** recommendation. A menu hands the decision back without the judgment. The runner-up goes in "ruled out", not as an equal option.
- The principle must be specific to a rule in `references/chooser.md` or the family reference, not generic advice ("keep it simple").
- If the data can't honestly answer the question, say so here. Don't paper over it with a chart.
- **Color scale choice belongs here** when color carries data: name the scale type (categorical / sequential / diverging / highlight) and why. Categorical caps at 8 (3–5 ideal); diverging needs a meaningful midpoint; continuous data is never rainbow.

## Step 4 — Gate

**Stop and wait for the user's answer.** The recommendation block ends with a question for a reason. Do not write chart code, open `/chart-build`, or render anything in the same turn.

**If the user's message already pre-authorizes the build** (explicit words like "don't ask, just make it", "go", "build whatever you think"): treat that as the gate's answer. Proceed to Step 5 in the same turn, and put the full recommendation block (why, principle, ruled out) at the top of the delivery so the lesson still lands. A deadline or urgency alone is *not* pre-authorization; ask.

Accept any of: yes / go / build it → proceed. Runner-up → swap and proceed. A changed question → return to Step 2. A pushback with reasoning → engage with it; if they're right, say so and update; if the rule holds, explain once and let them decide.

## Step 5 — Hand Off

Invoke `/chart-build` with this brief:

```
family: [amounts | distributions | proportions | associations | time-trends | geospatial | uncertainty]
form: [the confirmed chart form]
data: [file path or the inline table]
encodings: [x = …, y = …, color = … (scale type), facet = …]
title: "[assertive title]"
audience: [expert | lay | executive]
medium: [deck | linkedin | slide | doc | dashboard] → drives size + export
brand: [company | other brand | neutral]
```

If overplotting is likely (thousands of points, rounded data), add `overlap: true` so `/chart-build` also loads its overlap reference.

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Recommending three charts "so they can choose" | One pick, runner-up under "ruled out" |
| Choosing by data type ("it's numeric, so bar") instead of question | Question type first, data shape second |
| Mean ± error bars to show spread | Spread is a distributions question → box/violin/jittered points |
| Pie because it's "parts of a whole" when the reader must compare parts | Side-by-side bars; pie only for few slices / simple fractions |
| Skipping the gate because the choice is "obvious" | The gate is the lesson. Ask anyway; it takes one turn |
| Teaching a generic principle | Tie the principle to this data's shape |
