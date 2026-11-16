---
name: objection-handler
description: Use when a prospect pushes back and you need a calibrated reply.
Handles the five resistance types that kill most deals: Price, Timing,
Trust/Credibility, Need, and Authority. Paste the prospect's exact words —
do not paraphrase. Generic inputs produce generic replies.
---

# /objection-handler — Sales Objection Response

## Purpose

Produce a send-ready reply to a live prospect objection.
The five resistance types are distinct — wrong approach on the wrong type
is the most common reason follow-up sequences fail.

Paste the prospect's exact words. State the objection type.
Output is a reply under 120 words, calibrated to the specific resistance.

---

## Trigger

Invoked with /objection-handler [type]

Types: price | timing | trust | need | authority

If type is not specified, identify it from the prospect's words before
proceeding. Ask for confirmation if ambiguous.

---

## Inputs Required

For all types:
- Prospect's exact words (paste, do not summarize)
- Your offer in one sentence (outcome only, not a feature list)

Additional inputs by type — ask for these if not provided:

| Type | Additional Input |
|------|-----------------|
| Price | Your price + the specific outcome you deliver |
| Timing | The core problem you solve, in their language |
| Trust | 2-3 specific proof points — numbers, not adjectives |
| Need | The underlying problem they typically don't see yet |
| Authority | What you know about the decision-maker(s) involved |

---

## The Five Objection Types

### PRICE
*"It's too expensive." / "We don't have budget." / "Can you do it for less?"*

Price objections are value objections in disguise.
The prospect doesn't believe the outcome is worth the cost.

Response approach:
1. Reframe price as cost-per-outcome, not cost-per-month
2. Surface what they're currently paying (time or money) to not have
   this problem solved
3. Shift the conversation from price to ROI
4. Do not apologize for the price. Do not offer a discount.

---

### TIMING
*"Now isn't a good time." / "Let's revisit in Q3." / "We're in a freeze."*

Timing objections are almost always priority objections.
The prospect is avoiding a decision, not managing a calendar.

Response approach:
1. Acknowledge the timing concern without validating it as a reason to wait
2. Calculate what waiting costs them — in the specific language of the
   problem you solve
3. Create urgency without pressure tactics
4. Offer a specific, low-commitment next step that fits their timeline

---

### TRUST / CREDIBILITY
*"I've tried things like this before." / "How do I know this works?" /
"I don't know enough about you."*

Credibility objections require evidence, not enthusiasm.
Enthusiasm at this stage makes the skepticism worse.

Response approach:
1. Validate their skepticism — it's a reasonable response to being burned
2. Lead with the most concrete proof point, not the most impressive-sounding
3. Propose a low-risk way to experience a result before committing fully
4. Under 120 words. No overselling.

---

### NEED
*"We're already handling this." / "We have a solution for that." /
"We don't really have that problem."*

Arguing against a "no need" objection confirms you're just selling.
A single diagnostic question does more than a paragraph of persuasion.

Response approach:
1. Accept their framing without arguing
2. Ask one diagnostic question that reveals whether the underlying
   problem exists — constructed from the "underlying problem" input
3. Do not pitch. The goal is one question that gets them thinking.
4. Short. Curious. Non-confrontational.

---

### AUTHORITY
*"I'd have to run this by my partner." / "We decide as a team." /
"I need to check with [name]."*

Authority objections usually aren't a stall — they're telling the truth.
Become their ally in making the case internally.

Response approach:
1. Acknowledge without rushing
2. Offer to help them present it internally — give them a one-sentence
   summary they can use verbatim
3. Propose a short call with the relevant decision-maker(s) as next step
4. Under 80 words. Collaborative, not pushy.

---

## Output Format

```
OBJECTION RESPONSE
Type: [Price / Timing / Trust / Need / Authority]
Prospect said: "[their exact words]"
────────────────────────────────────────────────
[Reply — calibrated to resistance type, under stated word limit]
────────────────────────────────────────────────
WHY THIS APPROACH:
[One sentence on the psychology driving this resistance type
and why this response addresses the root, not the surface.]

WHAT NOT TO DO HERE:
[One sentence on the most common wrong move for this objection type.]
```

---

## Rules

- Paste exact words. Summaries produce generic replies.
- Identify the type before writing. Wrong approach = wrong reply.
- No apologies for price. No discounts in the reply.
- No "I totally understand" openers on any type.
- No fake urgency or pressure tactics.
- "Why This Approach" and "What Not To Do" are not optional —
  they build the user's pattern recognition, not just their reply queue.
