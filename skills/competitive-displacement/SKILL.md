---
name: competitive-displacement
description: Use when a prospect is already using a competitor or has a DIY
solution in place and you need to surface the gaps without trashing what
they're using. Produces diagnostic questions that reveal whether the gaps
are costing them, and a ready-to-send reply for "our current solution works
fine." Has a DIY mode for "we'll just build it" / "I can do that myself."
Complements /objection-handler for the need-type objection.
---

# /competitive-displacement — Competitive Displacement Framework

## Purpose

Surface the gaps in what a prospect is currently using — without naming
or trashing the competitor — and let them draw the conclusion themselves.

Prospects defend their current solution when you attack it.
They abandon it when they discover its limits on their own.

Output: gap analysis, 3 diagnostic questions, and a 90-word reply
for the "works fine" deflection.

---

## Trigger

Invoked with /competitive-displacement

The user provides:
- The competitor or current approach the prospect is using
- What the prospect said about their current solution
- Your offer in one sentence

If the current approach is DIY (built in-house, "our engineers," Clay/Zapier
stack, "I can do that myself"), run **DIY Mode** instead of Steps 2–4.

---

## Process

### Step 1 — Gather Inputs

Confirm all three inputs. If what the prospect said is vague ("they said
they're happy with what they have"), ask for more context — any specific
language they used about how it works for them, what they value about it,
or why they're not looking to change.

### Step 2 — Identify the Gaps

Identify the gaps that typically exist in the competitor/current approach
for a company in their situation.

Not generic category weaknesses — gaps specific to the prospect's business
context based on what they've shared and what's known about the competitor.

3 gaps maximum. Each should be:
- Plausible without inside knowledge of their operation
- Relevant to the problem your offer solves
- The kind of thing they'd only notice if they were looking for it

### Step 3 — Write the Diagnostic Questions

Write 3 questions that reveal whether those gaps are actually costing them.

Rules:
- Do not name the competitor in any question
- Do not position your offer in any question
- Each question surfaces a specific symptom of the gap — not the gap itself
- The prospect should be able to answer honestly without feeling set up

The goal: if they answer honestly, they discover the problem themselves.
You don't have to tell them. They tell you.

### Step 4 — Write the "Works Fine" Reply

A 90-word reply for when they say their current solution "works fine."

This is not an argument. It is not a case for switching.
It is a question that opens the door without forcing it.

The reply should:
- Accept their framing without agreeing it's the end of the conversation
- Surface one specific scenario where "works fine" typically has an edge case
- End with a single soft question, not a pitch

### DIY Mode — When the Competitor Is "We'll Build It"

DIY is a competitor. Treat it like one, with one difference: you concede ground
first. Pretending it can't be built is how you lose credibility.

**1. The honest concession.** Name exactly which parts are easy to build.
"Yes, you can build this. The [enrichment / routing / v1 workflow] part is
straightforward." Then name the part that isn't: the part that carries
maintenance and ownership.

**2. Ownership diagnostics.** Replace the 3 gap questions with these (adapt the
wording, keep the target):
- "Has anyone on your team tried building this already? How far did it get?"
- "Who owns it 6 months from now?"
- "What happens the week that person is on PTO?"
- For founder/CEO builders: "If you're the one building it, what does that
  time come out of?"

These target maintenance and opportunity cost, not features. DIY usually wins
on features at month 1 and loses on ownership by month 6.

**3. The split offer.** If their answers show they CAN own a piece, don't fight
it. Offer the split: "Great, you focus on ___. We'll handle ___." Run
/build-vs-buy for the verdict and numbers if the deal warrants it.

**4. Forwardable one-pager.** The build question gets decided in an internal
thread you're not in. Give the champion something to forward:
- What's easy to build (honest)
- Month 1 vs. month 6 (what changes: APIs, owner, edge cases)
- True cost: tools + internal hours + maintenance + opportunity cost
- When building IS the right call
- The split option

---

## Output Format

```
COMPETITIVE DISPLACEMENT
Competitor / current approach: [what they're using]
────────────────────────────────────────────────

TYPICAL GAPS (for a company in their situation):

1. [Gap]: [Why this gap is structurally present in what they're using]
2. [Gap]: [Why this gap is structurally present in what they're using]
3. [Gap]: [Why this gap is structurally present in what they're using]

DIAGNOSTIC QUESTIONS:

1. [Question — surfaces symptom of Gap 1 without naming competitor]
2. [Question — surfaces symptom of Gap 2 without naming competitor]
3. [Question — surfaces symptom of Gap 3 without naming competitor]

"WORKS FINE" REPLY (under 90 words):

[Reply — accepts framing, surfaces one edge case scenario, ends
with a soft question. No pitch. No competitor mention.]

────────────────────────────────────────────────
SEQUENCING NOTE:
[One sentence on which question to lead with and why — the one
most likely to produce a candid answer given what the prospect
has shared so far.]

DIY MODE (if applicable)
────────────────────────────────────────────────
HONEST CONCESSION: [what's easy to build] / [what isn't, and why]

OWNERSHIP DIAGNOSTICS:
1. [Tried-it question]
2. [6-month owner question]
3. [PTO / founder-time question]

SPLIT OFFER: "You focus on ___. We'll handle ___."

CHAMPION ONE-PAGER: [5 sections above, ≤ 1 page, written for the
person who has to defend the decision internally]
```

---

## Rules

- Never name or trash the competitor in any output — questions, replies,
  or gap descriptions.
- Gaps must be specific to the prospect's situation, not generic category
  criticisms. "Limited integrations" is not a gap. "No API access for
  the workflow they described" is.
- Diagnostic questions do not contain your offer. Not even implicitly.
- The "works fine" reply is under 90 words. Hard limit.
- "Sequencing Note" is not optional — the order questions are asked
  matters as much as the questions themselves.
- In DIY Mode, always lead with the honest concession. Never claim it
  can't be built.
- Say when building is the right call (core to their product, or a team
  that will own it). Losing that deal honestly beats winning it dishonestly.
