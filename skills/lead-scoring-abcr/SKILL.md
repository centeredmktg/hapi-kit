---
name: lead-scoring-abcr
description: Classifies leads into A/B/C/R tiers against ICP criteria so only qualified leads receive outreach. Optionally runs in continuous 0–100 mode (fit + intent, signal-weighted) for finer-grained gating. Every fact is tagged by provenance (observed / inferred / predicted / synthetic) and weighted accordingly, so scores separate evidence from hypothesis.
---

## Purpose

Prevents wasted outreach by forcing every lead through a structured qualification filter before a single message is written. Scoring is strict by design — a generous scorer wastes time, money, and sender reputation on leads that will never convert. When in doubt, score down.

## Trigger

`/score-leads` or when the user has a lead list (enriched preferred, raw acceptable) that needs to be qualified before sequencing.

## Process

1. **Get ICP criteria.** Pull from the output of `icp-developer` if available. If not, ask the user for: target role(s), company size range, industry/vertical, buying triggers, and hard disqualifiers. If criteria are vague or missing, push back before scoring — garbage criteria produce garbage scores.

2. **Get the lead list.** Enriched CSV is preferred. Raw lists are accepted but will produce lower-confidence scores. Note if enrichment data is absent.

3. **Tag provenance.** Every fact used in scoring gets one label, by source:
   - **observed** (1.0): first-party or verified data. CRM records, enrichment from a named provider, a conversation, the prospect's own published statement.
   - **inferred** (0.6): derived from observed facts by a stated rule. Seniority from title, size band from headcount.
   - **predicted** (0.4): research hypothesis or model estimate. "Likely evaluating X," LLM-estimated pain, first-touch research claims.
   - **synthetic** (0.1): placeholder or demo data. Never counts toward an A.
   If you can't say where a fact came from, it's predicted.

4. **Choose scoring mode.**
   - **ABCR mode (default)** — discrete tiers, fastest, best for batch qualification.
   - **Continuous mode (0–100)** — run when the user wants a sortable score, intends to tune cutoffs over time, or is gating a high-volume daily send list. Maps back to ABCR at the end.

5. **ABCR mode — score each lead against four criteria:**
   - **Role match** — exact target title vs. adjacent vs. wrong department
   - **Company match** — size, industry, stage alignment with ICP
   - **Signal match** — is there a recent buying trigger? (funding, hiring spike, product launch, pain indicator)
   - **Disqualifier check** — competitor, wrong geography, too small, too large, or other defined hard stops

   Classify into tier:
   - **A** — 3+ criteria match, no disqualifiers, at least one signal present → outreach immediately
   - **B** — 2 criteria match, no disqualifiers → outreach with adjusted messaging and lower urgency
   - **C** — 1 criterion match or signals are weak/absent → nurture list, do not outreach now
   - **R** — any disqualifier present OR 0 criteria match → remove from active list entirely

6. **Continuous mode — score each lead 0–100 (50 FIT + 50 INTENT):**

   **FIT (0–50)**
   - Company size in ICP band: +15
   - Target seniority (Director+ or named role): +15
   - Target industry/vertical: +10
   - Tech stack / context match: +10

   **INTENT (0–50)**
   - Signal type weight (use highest firing):
     - Pain complaint / "consolidating stack" / asked for recommendations: +20
     - Job change (0–6 months): +20
     - Hiring / funding / headcount growth: +15
     - Competitor engagement or named mention: +10
     - Content / topic engagement only: +5
   - Signal recency: 0–7 days +10 | 8–30 days +5 | 30+ days +0
   - Multi-signal stacking: +5 per additional firing signal (max +15)

   **Provenance weighting:** multiply each FIT and INTENT item's points by its provenance weight before summing. Round to the nearest integer.

   **Disqualifier override:** any hard disqualifier → score forced to 0, classified R, regardless of points.

   **Tier mapping:**
   - 80–100 → **A** (outreach immediately)
   - 60–79 → **B** (nurture / lower-urgency outreach)
   - 40–59 → **C** (skip for now)
   - <40 or disqualified → **R**

   **Evidence gate:** an A (either mode) requires at least one *observed* signal. A lead that scores A on inferred/predicted evidence alone is classified **A-predicted**. Sequence it at B urgency, with messaging that tests the hypothesis rather than asserts it.

7. **Self-check before output.** LLMs default generous. Before producing the list, audit:
   - Am I scoring up because the data is incomplete? (Score down instead.)
   - Did I flag every disqualifier I saw?
   - On a cold list, am I producing >60% A-tier? (If yes, the ICP is too broad — flag it.)
   - Did I name a specific signal for every A? (No signal = not an A.)
   - Is any A resting only on predicted or inferred signals? (Downgrade to A-predicted.)

8. **Output scored list** with tier, one-line reason, and named signal or disqualifier for every lead.

## Output Format

```
LEAD SCORING RESULTS
────────────────────────────────────────────────
Mode: [ABCR | Continuous 0–100]
ICP Criteria: [brief summary]
Total leads scored: [N]
A-tier: [N] | A-predicted: [N] | B-tier: [N] | C-tier: [N] | Rejected: [N]
Evidence mix: observed [N]% | inferred [N]% | predicted [N]% | synthetic [N]%
Self-check: [pass | flagged — reason]

────────────────────────────────────────────────
A-TIER — Outreach immediately
[Name] — [Company] — [Title]
  Score: [A | 87/100] | Reason: [one line]
  Signal: [what triggered the score]
  Evidence: [observed 3 · predicted 1]

[repeat for each A]

────────────────────────────────────────────────
A-PREDICTED — Strong fit, unverified signal. Test the hypothesis.
[Name] — [Company] — [Title]
  Score: [A-pred | 81/100] | Hypothesis to test: [one line]

[repeat for each A-predicted]

────────────────────────────────────────────────
B-TIER — Outreach with adjusted messaging
[Name] — [Company] — [Title]
  Score: [B | 72/100] | Reason: [one line]

[repeat for each B]

────────────────────────────────────────────────
C-TIER — Nurture only
[Name] — [Company] — [Title]
  Score: [C | 51/100] | Reason: [one line]

[repeat for each C]

────────────────────────────────────────────────
REJECTED
[Name] — [Company] — [Title]
  Score: [R | 0/100] | Disqualifier: [named reason]

[repeat for each R]
```

## Rules

- Be strict. Score down when in doubt, not up.
- Every A must have a named signal — no signal, no A.
- Every R must have a named disqualifier — "doesn't feel right" is not a disqualifier.
- If ICP criteria are missing or too vague to score against, stop and ask before producing output.
- Do not advance C or R leads to sequencing. They must be physically separated from A and B output.
- If the incoming list has no enrichment data, note this at the top of results and flag that scores may be lower confidence.
- If 60%+ of leads score A on a cold list, the ICP criteria are too broad — flag this to the user.
- In Continuous mode, always run the self-check before output. LLMs are generous by default.
- A disqualifier forces R regardless of point total. Disqualifiers are binary, not weighted.
- Synthetic facts never contribute to an A or A-predicted tier.
- Report the evidence mix on every run. Over an engagement, the observed share rising is the signal that the system is being installed, not just modeled.
