---
name: chart-qa
description: Use when a chart, graph, plot, or dashboard figure has been rendered and must be checked before anyone else sees it; when chart-build dispatches its review step; when deliverable-qa finds charts in a deliverable; or when the user asks "is this chart any good", "review this chart", or shares a chart image or chart code for critique.
---

# /chart-qa — Independent Chart Audit

## Purpose

Audit a rendered chart the way its reader will meet it: cold, with no knowledge of the code or the reasoning behind it. Grade every finding on a three-level scale, give a concrete fix for each, and return a ship / fix / block verdict.

**Separation rule:** whoever built the chart doesn't grade it. When `/chart-build` calls this skill, it runs as a fresh subagent that receives only the rendered image, the brief, and a data summary. When the user shares a chart directly, review the image first, and read the code only to confirm a suspected cause.

---

## Severity Scale

| Grade | Meaning | Verdict effect |
|---|---|---|
| **WRONG** | The chart misstates the data: math, encoding, or missing information means a reader gets a false or unrecoverable value | **Block.** Do not ship. |
| **BAD** | Accurate but readers will likely misread it, miss the point, or work too hard | **Fix** before shipping |
| **UGLY** | Readable but cluttered, cramped, or off-brand | Fix if cheap; ship otherwise |

Never polish a wrong chart. Report WRONG findings first, and don't bury them under cosmetic notes.

## Step 1 — Read the Chart Cold

Before opening the checklist, look at the image for five seconds as the intended audience would, and write down:
1. **The point you took away**, in one sentence.
2. **Where your eye went first.**
3. **Anything you couldn't read or work out.**

Compare (1) against the brief's intended title and point. If they don't match, that's a BAD finding ("the chart doesn't make its point") even if every individual rule passes.

## Step 2 — Run the Checklist

Go through `references/checklist.md` item by item. Every item gets pass / fail / n/a. Each item carries its default severity; raise it if the failure changes what a reader would conclude.

Check against the actual pixels. For example, "text legible at final size" means estimating rendered text height on the target canvas from the brief's medium (LinkedIn 1080 wide, deck 1600 wide, doc 6.5 in), not reading the font-size setting.

## Step 3 — Report

Return exactly this format:

```
## Chart QA: [chart title or filename]
**Verdict:** [BLOCK — n wrong | FIX — n bad | SHIP — ugly only or clean]
**Cold read:** "[the point you took away]" → [matches / doesn't match] intended: "[brief's point]"

### Findings
| # | Grade | Check | What's wrong (where on the chart) | Fix |
|---|---|---|---|---|
| 1 | WRONG | … | … | … |
| 2 | BAD | … | … | … |
| 3 | UGLY | … | … | … |

**Passed:** [count] of [applicable count] checks.
```

- Sort findings WRONG → BAD → UGLY.
- Every fix is concrete and executable ("add a light x-axis with ticks every 20 days from 0–100"), not advice ("improve clarity").
- If clean: `SHIP` with an empty findings table. Don't invent findings to look thorough.

## Step 4 — Loop Limit

When called from `/chart-build`: one fix pass, then one re-audit. If WRONG or BAD findings remain after that, return to the user with the chart and the open findings. Two failed passes means a judgment call (often the wrong chart form), so send it back to `/viz-advisor`. Don't keep patching.

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Reviewing the code instead of the image | Pixels first; code only to confirm a cause |
| Builder grading their own chart | Fresh subagent, image + brief + data summary only |
| Listing only cosmetic notes on a chart with an unreadable range | Run the "values recoverable" check every time |
| "Looks good" with no checklist pass count | Every item gets pass / fail / n/a |
| Vague fixes | Name the element, the change, and the value |
| Endless fix loops | One fix pass, then escalate |
