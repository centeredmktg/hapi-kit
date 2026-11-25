---
name: chart-build
description: Use when a chart form has been confirmed (usually handed off from viz-advisor with a brief) and it needs to be built as code, an image, an HTML/SVG chart, or a figure for a deck, LinkedIn post, slide, or document. If no chart form has been confirmed yet, use viz-advisor first.
---

# /chart-build — Build the Confirmed Chart to Spec

## Purpose

Turn a confirmed chart brief into a finished, honest, legible figure. Load the rules for the chart family, apply the universal rules every chart gets, render at final size, and send it to `/chart-qa` for an independent check before anyone sees it.

**Entry gate:** this skill expects a brief from `/viz-advisor` (family, form, data, encodings, title, audience, medium, brand). If it was invoked directly with no confirmed chart form, run `/viz-advisor` first. Skipping the recommendation step skips the reasoning the user signed off on.

---

## Step 1 — Load the Family Rules

Read `references/<family>.md` for the brief's family:

`amounts` · `distributions` · `proportions` · `associations` · `time-trends` · `geospatial` · `uncertainty`

If the brief says `overlap: true`, or n is in the thousands, or values are rounded so points stack, also read `references/overlap.md`.

## Step 2 — Set Up Style Before Content

- **Brand:** `company` → the company brand tokens (colors, fonts) from `context/company.md` or the brand guide it points to. Ask once if neither exists, then record them in `context/`. Another brand (a partner, a co-branded piece) → their tokens. `neutral` → the built-in `dataviz` skill's palette and mark specs if that skill is available; otherwise a colorblind-safe categorical palette (Okabe-Ito) with gray for de-emphasized series.
- **Content and design stay separate.** Data, transforms, and mappings in one place; colors, fonts, and grid in a theme. Restyling must never touch the data logic.
- **Reproducible:** generate from the raw data in a script (Python/matplotlib, Vega-Lite, D3, Recharts, whatever fits the medium). Seed any randomness (jitter, sampled draws). No hand-edited output in a pipeline.

## Step 3 — Build, Applying the Universal Rules

These apply to every chart regardless of family. The family reference adds to them.

**Honesty (violations are WRONG in `/chart-qa`):**
- Shaded area is proportional to value. Bars and filled areas start at 0 on a linear axis. On a log axis, bars mean ratios and start at 1. Otherwise use dots.
- Parts drawn as a whole sum to 100% with no double counting.
- Every scale is one-to-one. One shared scale across bars or panels being compared.
- Error bars or bands are labeled with what they are (SD, SE, 95% CI).
- A log axis is titled with the variable, not "log(x)".

**Encoding:**
- Most important variable on position. Size and color for secondary ones. Budget: x, y, plus one channel. Past that, facet.
- Unordered categories sorted by value. Ordered categories (age bands, stages, months) kept in natural order.
- Long category labels → horizontal bars. Never rotate tick text.
- Filled shapes, not outlines: bars and histograms lightly filled, points solid, densities semi-transparent fills.
- No 3D, ever, unless the subject is a real 3D object and the output is interactive.

**Color:**
- Color has a job (distinguish, encode value, or highlight) or it's removed.
- Categorical: 3–5 colors ideal, 8 max. Past 8, color by a coarser group and direct-label the points that matter.
- Sequential: monotonic light → dark. Never rainbow. Diverging only with a meaningful midpoint, both arms balanced.
- Highlight: everything gray except the focus.
- Avoid big areas of saturated color.
- Redundant coding: key distinctions also carried by shape, position, or a label, so the chart survives colorblindness and grayscale. Avoid red/green-only and blue/green-only contrasts.
- Same variable gets the same color in every panel and every figure in the set.
- When color is the main variable, give it large areas (tiles, fills), not thin lines or tiny points. Color discrimination drops as marks shrink.
- Colored text labels: use a darker shade of the hue for text and outlines, and a lighter one for fills. Thin text reads lighter than a fill of the same color.
- CVD-safe fallback palette if no brand applies: `#E69F00 #56B4E9 #009E73 #F0E442 #0072B2 #D55E00 #CC79A7 #000000`.

**Labels and annotation:**
- **Title states the point** as a short assertive sentence ("Referrals close 3x faster than any paid channel"), not a label ("Lead sources by close time"). Exactly one title: inside the image for social, standalone, and dashboard use; in the caption for documents. Never both.
- Every axis titled with units, unless self-evident (years, country names). Don't over-label.
- Direct labels beat legends: label lines at their ends and groups in place. If a legend stays, its order matches the visual order of the data, with one legend per variable.
- Print the actual numbers where area or angle is hard to judge (treemaps, mosaics, few-value bars, where the value axis can then be dropped).
- Data source credited in the caption, or in the image for standalone use.

**Ink and layout:**
- Drop frames, borders, and minor gridlines. Major gridlines light gray, perpendicular to the variable of interest (horizontal for vertical bars and time series, vertical for horizontal bars).
- Keep enough context that marks don't float. If the grid goes, add a reference line (index = 100, target, 50%).
- Small multiples share axis ranges, are ordered by a logical principle (magnitude, time, rank, never alphabetical by default) and get a light panel background.
- Compound panels: aligned, consistent colors and group order, small a/b/c labels in the figure's font.

## Step 4 — Render at Final Size

Text is too small by default. Size for the medium, then check at that size.

| Medium | Canvas | Starting text sizes (industry standard) |
|---|---|---|
| LinkedIn single / carousel | 1080×1350 px | title ≥ 44px · axis titles ≥ 30px · ticks ≥ 26px |
| Deck slide | 1600×900 px (16:9) | title ≥ 36px · axis titles ≥ 24px · ticks ≥ 20px |
| Document / report | 6.5 in wide | title 12–14pt · labels ≥ 9pt at print size |
| Dashboard tile | as placed | ticks ≥ 12px at actual tile size |

If text grows, grow points and line widths with it so marks and text stay balanced. Check legibility at final size: preview at roughly 3–5 inches wide on screen and confirm every label reads.

## Step 5 — Independent QA

Render a PNG, then dispatch `/chart-qa` as a **fresh subagent**. Give it only the PNG path, the brief (title, audience, medium, the question), and the data summary. Do **not** pass the chart code or this conversation's reasoning. The reviewer should see what the reader sees.

- **WRONG or BAD findings** → apply the fixes, re-render, and run `/chart-qa` once more.
- **Still failing after one fix pass** → stop and show the user the chart plus the open findings. Don't loop silently.
- **UGLY only** → apply the cheap fixes, then ship.

**The QA step is never skipped, and never done by the builder.** Not for deadlines, not for "simple" charts, not because you already looked at the render.

| Excuse | Reality |
|---|---|
| "User is short on time" | The QA subagent takes about a minute. A wrong chart in front of investors costs more than that |
| "I checked the render myself and it reads cleanly" | Self-review is the failure mode. The builder sees what it meant to draw |
| "It's a simple line chart" | Simple charts carry the classic WRONG errors: area fill on a trimmed axis, unrecoverable values |
| "The user said don't ask me anything" | That waives questions, not QA. QA asks the user nothing |

If the QA subagent genuinely can't run (no agent tool available), ship with a visible line: "Not independently reviewed." Never claim it was checked.

## Step 6 — Export

| Use | Format |
|---|---|
| Master copy | SVG or PDF (vector), fonts embedded; or PNG at 2x if the chart has huge point clouds |
| Web, Slack, LinkedIn | PNG (2x pixel density) |
| Print | PDF, or PNG at ~300 dpi at final print size |
| Never for charts | JPEG (compression artifacts around text and edges) |

Keep the master at full fidelity and convert down per channel. Name files `{YYYY-MM-DD}-{client-slug}-{artifact-type}.ext`.

## Step 7 — Hand Off

If the chart is headed to a client or stakeholder, recommend `/chart-to-client-delivery` (standalone HTML + an insight-led message). If it's part of a deliverable, `deliverable-qa` will see that `/chart-qa` already passed.

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Building before the form was confirmed | Run `/viz-advisor` first; its gate is the user's decision point |
| Grading your own chart | `/chart-qa` runs as a fresh subagent on the PNG only |
| Default text sizes | Size from the medium table, check at final size |
| Legend in alphabetical order | Direct labels, or legend in data order |
| Rainbow or 10+ categorical colors | Sequential scale, or coarser groups + direct labels |
| Bars on a trimmed axis to "show the difference" | Dots on a trimmed axis, or plot the change itself |
| A title that names the chart | A title that states the finding |
