---
name: offer-stress-test
description: This skill should be used when the user wants to "stress test an offer", "find objections to my pitch", "pressure test my positioning", "role-play as my ideal customer", "find weaknesses in my offer", or wants to hear every objection before taking an offer to market. Requires an ICP and offer description as input.
---

## Context Check

On start, read `context/company.md` at the workspace root if it exists (company, ICP, positioning, voice). Also read any other file in `context/` that matches this task.

If context exists:
- Load ICP, offer, voice rules, constraints, and engagement context silently
- Skip any intake questions already answered in `context/`
- Confirm loaded context in one line: "Working from [company] context."

If no context: run normally — prompt for inputs as usual.

# Offer Stress Test

## Purpose

Role-play as the ICP and surface every real objection to an offer — not to be difficult, but because these are the exact objections that lose deals in real life. Then define what would need to be true for the offer to feel like a no-brainer to that buyer.

**Input:** ICP statement + offer description (what it is, what's included, what it costs, what result it delivers)
**Runs after:** `icp-developer`, `pain-point-hierarchy`
**Output used for:** Offer refinement, objection-handling content, sales collateral, landing page copy

---

## Process

### Step 1: Intake

Collect:
1. The ICP (paste or reference prior session)
2. The offer — full description including: what it is, what's included, what's excluded, price/investment, timeline, result delivered, proof points available

Once both are provided, proceed to Step 2.

### Step 2: Role-Play Mode

Adopt the ICP's perspective. State it clearly:

*"I'm now operating as [ICP description]. I've read your offer. Here are every objection I have — in order of the ones most likely to kill the deal."*

Generate a minimum of 10 objections. Categorize them:

**Category A — Price / ROI objections**
**Category B — Trust / credibility objections** (Do I believe you can deliver this?)
**Category C — Timing objections** (Not the right moment)
**Category D — Internal objections** (Need to convince someone else, budget cycle, procurement)
**Category E — Competitive objections** (Why not just do X instead?)
**Category F — Belief objections** (I don't think this will work for MY situation)

For each objection: state the objection as the buyer would voice it, then rate kill probability (High / Medium / Low).

### Step 3: No-Brainer Definition

After all objections, answer:

*"Here is what would need to be true about this offer — the proof, the framing, the risk reversal, or the delivery — for it to feel like an obvious yes to someone exactly like me."*

Structure this as a checklist:

```
NO-BRAINER CHECKLIST — [Offer Name]
────────────────────────────────────────────────────────
For this offer to feel like a no-brainer to [ICP]:

□ [What proof is needed]
□ [What risk reversal is needed]
□ [What framing shift is needed]
□ [What social proof format would move the needle]
□ [What the offer needs to include or exclude]
□ [What the delivery model needs to look like]
□ [What the guarantee or commitment needs to be]
────────────────────────────────────────────────────────
HIGHEST-LEVERAGE FIX:
[The single change that would most increase conversion for this ICP]
────────────────────────────────────────────────────────
```

---

## Global Rules

- Play it straight — surface the objections the buyer would actually have, not softened versions
- High kill probability objections get addressed first in all sales and marketing materials
- The no-brainer checklist becomes the brief for offer refinement, landing page copy, and objection-handling content
- If the offer has no credible answer to a high kill probability objection, flag it explicitly: "This objection currently has no good answer. You need to build proof here before going to market."
- Save output to `outputs/YYYY-MM-DD-offer-stress-test.md`
- If the result is approved as canonical, also update `context/offer.md` so other skills read it.
