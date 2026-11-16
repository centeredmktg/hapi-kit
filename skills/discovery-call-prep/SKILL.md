---
name: discovery-call-prep
description: Use before a discovery or sales call to generate diagnostic
questions for a specific prospect. Produces questions that surface the cost
of the problem, reveal frustrations with their current solution, and get
them to articulate the consequence of inaction. Run after /intel for best
results. Not a question bank — outputs for a named prospect and context.
---

# /discovery-call-prep — Pre-Call Diagnostic Question Generator

## Purpose

Generate the questions you actually ask on a discovery call — not generic
curiosity questions, but diagnostic ones that surface cost, frustration,
and consequence of inaction.

Most founders ask product questions. The conversations that convert ask
pain questions. These are the ones that make a prospect think.

Output: 6 questions structured across three diagnostic layers.

---

## Trigger

Invoked with /discovery-call-prep

The user provides:
- Prospect's company and role
- The problem your offer solves
- Anything known about them (LinkedIn notes, prior emails, intel profile)

If intel was run on this prospect's company, reference it.
If nothing is known beyond company and role, proceed — but flag that
richer inputs produce sharper questions.

---

## Process

### Step 1 — Gather Inputs

Confirm you have:
- Who the prospect is (role, company, industry)
- What problem you solve
- Any prior context (optional but improves output)

### Step 2 — Generate the Six Questions

**Layer 1 — Cost of the Problem (3 questions)**
Questions that surface how much this problem is actually costing them —
in time, revenue, team capacity, or competitive position.

Not: "Do you have this problem?"
Yes: "What does it cost you when [specific version of problem] happens?"

Each question should be impossible to answer with a yes/no.
Each should make them calculate something they haven't calculated before.

**Layer 2 — Current Solution Frustrations (2 questions)**
Questions that reveal what they're using today and why it's failing them.

The goal is not to trash their current solution — it's to get them to
articulate the gap themselves. Their words become your positioning.

**Layer 3 — Consequence of Inaction (1 question)**
One question that gets them to project forward one year and name what
hasn't changed — or gotten worse.

This is the most important question on the call. It should be asked last,
after the first five have established the problem is real and costly.

### Step 3 — Flag the One to Watch

After delivering the six questions, identify the single question most
likely to open the conversation up — the one where the honest answer
changes the dynamic of the call.

---

## Output Format

```
DISCOVERY CALL PREP
Prospect: [name/role/company]
Date: [today]
────────────────────────────────────────────────

LAYER 1 — Cost of the Problem

1. [Question]
2. [Question]
3. [Question]

LAYER 2 — Current Solution Frustrations

4. [Question]
5. [Question]

LAYER 3 — Consequence of Inaction

6. [Question]

────────────────────────────────────────────────
THE ONE TO WATCH: Question [#]
[One sentence on why this question is likely to shift the conversation
and what a candid answer reveals about where they actually are.]
```

---

## Setup Call Script (Full Call Execution)

The questions above are your ammunition. This section is the playbook for running
the actual call. Reframes "sales call" as "setup call" — live account configuration
for the prospect. Reduces friction, lowers no-shows, arrives at the same outcome.

**Framing language (use in booking confirmation):**
"This isn't a sales call — I'll walk you through exactly how [system/offer] would
work for [their specific situation]. Think of it as a live configuration session.
If it fits, great. If not, you'll leave with [specific takeaway]."

### The 45-Minute Structure

**0–5 min: Rapport + Agenda Set**
- Open with something specific from their profile/content/prior conversation
- Set the frame: "Here's what I was thinking — I'll ask a few questions about
  [their situation], then show you how [system] would work for you specifically.
  Sound good?"
- Get verbal buy-in on the agenda before proceeding

**5–15 min: Discovery (use Layer 1-3 questions above)**
- Ask the 6 diagnostic questions from the prep above
- Listen for: specific numbers, named frustrations, emotional language
- Take notes on their exact words — you'll mirror these back in the demo
- Lead with THE ONE TO WATCH question when rapport is established
- If they're guarded, use the "poke the bear" technique: replace "Are you
  interested in X?" with "How are you currently thinking about X?"

**15–35 min: Live Setup / Demo**
- Do NOT present slides or a generic walkthrough
- Configure/demonstrate using THEIR inputs from discovery
- Mirror their language: "You said [their words] — here's how this handles that"
- Show 3 things max. Each one tied to a pain they named.
- After each: "Does that match what you were describing?" (micro-commitments)

**35–40 min: Concern Handling**
- Ask directly: "What would stop you from moving forward with this?"
- Don't preempt objections — let them surface
- For each concern, acknowledge → reframe → evidence:
  - "That makes sense. What I've seen is [reframe]. For example, [specific client
    with similar concern] — [what happened]."
- If price: "What's the cost of NOT fixing [the problem they described]?"
  (Layer 1 answers become your ammunition here)

**40–45 min: Next Step Close**
- Summarize in their words: "So the main thing is [their stated problem],
  and what you'd want is [their stated outcome]. Right?"
- One clear next step — not "think about it"
- If trial: "I can get you set up right now. Takes 3 minutes."
- If proposal: "I'll send you exactly what we discussed — expect it by [specific time]."
- If not ready: "Totally fine. What would need to be true for this to make sense?"

### Output Format (when generating a full call script)

```
SETUP CALL SCRIPT
Prospect: [name/role/company]
Date: [call date]
────────────────────────────────────────────────

OPENING (0-5 min)
Rapport hook: [specific observation from their profile/content]
Agenda frame: [customized version of the frame above]

DISCOVERY (5-15 min)
[6 questions from discovery-call-prep above]
One to watch: Question [#]

DEMO PLAN (15-35 min)
Show 1: [tied to Layer 1 pain — what to demonstrate]
Show 2: [tied to Layer 2 frustration — what to demonstrate]
Show 3: [tied to Layer 3 consequence — what to demonstrate]

LIKELY CONCERNS
[Top 2-3 predicted concerns based on prospect context + reframe for each]

CLOSE
Primary ask: [specific next step]
Fallback: [if not ready, what to propose instead]

────────────────────────────────────────────────
```

### Script Rules

- Never run the demo section without discovery first. The demo is useless
  without their words to mirror back.
- 3 demo items max. More than 3 = you're presenting, not configuring.
- The close is one sentence, one action. Not a menu of options.
- If using with /discovery-call-prep, generate the questions first, then
  build the script around them.

---

## Rules

- No yes/no questions. Every question requires calculation or reflection.
- Do not write softball questions. These should make them think.
- Questions must be specific to the prospect's context — not generic
  sales methodology repackaged.
- The consequence question (Layer 3) is always last. Sequence matters.
- If prior intel exists on the prospect's company, use it to make
  Layer 1 questions specific to their business model and signals.
- One output per prospect. This is prep for a named conversation,
  not a question bank to reuse.
