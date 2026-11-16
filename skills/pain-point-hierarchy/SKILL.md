---
name: Pain Point Hierarchy
description: This skill should be used when the user wants to "map pain points", "identify what keeps the ICP up at night", "build a pain point list", "rank customer problems", or needs to understand the emotional urgency behind an ICP's problems before writing copy, building campaigns, or stress-testing an offer. Requires an ICP as input.
---

## Context Check

On start, read `context/company.md` at the workspace root if it exists (company, ICP, positioning, voice). Also read any other file in `context/` that matches this task.

If context exists:
- Load ICP, offer, voice rules, constraints, and engagement context silently
- Skip any intake questions already answered in `context/`
- Confirm loaded context in one line: "Working from [company] context."

If no context: run normally — prompt for inputs as usual.

# Pain Point Hierarchy

## Purpose

Generate a ranked list of pain points for a given ICP — categorized by emotional depth and search intent. The hierarchy distinguishes surface pain (what people talk about) from deep pain (what actually drives decisions), and flags which pains are actively being searched for solutions vs. which haven't yet been articulated.

**Input:** ICP statement (from `icp-developer` or user-provided)
**Runs before:** `offer-stress-test`, `outbound-campaign-builder`, content briefs

---

## Process

1. Take the ICP as input — either from a prior `icp-developer` session or pasted directly
2. Generate 20 pain points across the ICP's work and professional life
3. Rank by emotional urgency (most pressing first)
4. Categorize each as surface or deep pain
5. Flag search intent for each

---

## Output Format

```
PAIN POINT HIERARCHY — [ICP Label]
────────────────────────────────────────────────────────
Input ICP: [one-line summary of the ICP]
────────────────────────────────────────────────────────

TIER 1 — DEEP PAIN (keeps them up at night, drives real decisions)

1. [Pain point]
   Type: Deep | Searching: Yes / Not yet articulated
   Notes: [Why this matters emotionally, not just practically]

2. [Pain point]
   Type: Deep | Searching: Yes / Not yet articulated
   ...

TIER 2 — SURFACE PAIN (what they talk about, complain about, mention in discovery calls)

6. [Pain point]
   Type: Surface | Searching: Yes / Not yet articulated
   ...

TIER 3 — LATENT PAIN (real but unrecognized — they don't know they have this yet)

16. [Pain point]
    Type: Latent | Searching: No
    Notes: [How to surface this pain in copy or conversation]

────────────────────────────────────────────────────────
COPY TARGETS (top 3 for messaging priority):
1. [Pain #N] — [one-line reason it's the highest-leverage pain to market against]
2. [Pain #N] — ...
3. [Pain #N] — ...
────────────────────────────────────────────────────────
```

---

## Classification Rules

- **Surface pain:** What they complain about in meetings, mention on discovery calls, list as goals in RFPs. Easy to acknowledge; competitive on this level.
- **Deep pain:** What drives the actual decision. Often unstated. Usually about identity, fear of failure, status, or loss of control. Win on this level.
- **Latent pain:** The ICP doesn't yet recognize this as a problem. Opportunity to create a category or shift awareness — but harder to use in direct response copy.

**Searching:** Mark "Yes" if this pain is actively searched for (Google, communities, LinkedIn). Mark "Not yet articulated" if it's real but the ICP hasn't found the words for it yet.

---

## Global Rules

- 20 pain points minimum — resist stopping at 10 where everyone else stops
- The best pain points are specific enough to use in a subject line or hook
- Deep pain beats surface pain for conversion; surface pain beats deep pain for search/discovery
- Save output to `outputs/YYYY-MM-DD-pain-points.md`
- If the result is approved as canonical, also update `context/pain-points.md` so other skills read it.
