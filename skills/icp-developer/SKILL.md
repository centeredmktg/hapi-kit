---
name: icp-developer
description: >-
  This skill should be used when the user wants to "develop an ICP", "define ideal customer profile", "figure out who we're targeting", "build a customer profile", "identify our best customer", or needs to establish positioning before building campaigns, content, or outreach. Produces a single synthesized ICP statement from a structured 10-question intake. Optional outreach activation step adds LinkedIn-signal criteria, trigger events, and hard disqualifier.
---

## Context Check

On start, read `context/company.md` at the workspace root if it exists (company, ICP, positioning, voice). Also read any other file in `context/` that matches this task.

If context exists:
- Load ICP, offer, voice rules, constraints, and engagement context silently
- Skip any intake questions already answered in `context/`
- Confirm loaded context in one line: "Working from [company] context."

If no context: run normally — prompt for inputs as usual.

# ICP Developer

## Purpose

Build a precise, usable Ideal Customer Profile through structured interview.
Not a persona document — a single synthesized statement that goes into every
downstream agent system prompt, campaign brief, and content brief.

**Runs before:** `pain-point-hierarchy`, `offer-stress-test`,
`outbound-campaign-builder`, `content-repurposing`

---

## Process

Ask all 10 questions before synthesizing. Do not synthesize after 3 questions.
Do not skip questions — each one pulls out a different dimension of the ICP.

Collect answers conversationally. After all 10 are answered, synthesize.

---

## The 10 Questions

1. Who are your best clients — job title, seniority, company type, size,
   and revenue range?
2. What do they all have in common that makes them a great fit?
3. What specific problem did they come to you with? (Not the category —
   the precise pain.)
4. What had they already tried before working with you? Why didn't it work?
5. What result did they get from working with you? Be as specific as possible —
   numbers, timeframes, outcomes.
6. What did they have to believe was true before they were willing to work with
   you? (The required mindset shift.)
7. Where do they spend time professionally? (Conferences, communities,
   publications, LinkedIn groups.)
8. What triggers the moment they realize they have this problem and start
   looking for solutions?
9. Why you over alternatives — what's the actual differentiator, not the
   marketing version?
10. Who is NOT a good fit, and why? (Defines the boundary of the ICP.)

---

## Synthesis Format

After all 10 answers, produce:

```
ICP STATEMENT — [Company/Context]
────────────────────────────────────────────────────────
WHO:        [Job title(s), seniority, company type, size, revenue range]
PROBLEM:    [Precise pain — not a category, the specific friction]
TRIED:      [What they've already attempted and why it failed]
TRIGGER:    [The moment that makes them start looking for a solution]
RESULT:     [Specific, measurable outcome they get from working with you]
BELIEF:     [What they must believe to buy — the required mindset shift]
WHERE:      [Where they spend time professionally]
NOT FOR:    [Who this explicitly doesn't serve]
────────────────────────────────────────────────────────
SYNTHESIZED STATEMENT (for agent system prompts):
"[2-3 sentence ICP statement that combines who, problem, trigger, and required
belief into a single deployable definition. Specific enough to write copy against.]"
────────────────────────────────────────────────────────
```

After delivering the ICP statement, ask:
"Want the outreach activation layer? This adds LinkedIn-signal criteria,
buying trigger events, and a hard disqualifier for prospecting."

---

## Outreach Activation (optional)

If requested, produce the following from the ICP statement:

**1. LinkedIn Signal Criteria (5 filters)**
Specific, checkable attributes visible on a LinkedIn profile or company page
that confirm a prospect matches this ICP. Not job titles — observable signals:
keywords in bio, recent posts on a topic, company growth indicators,
tech stack clues, role change recency.

**2. High-Probability Industries (3)**
Industries where this problem is acute and conversion velocity is highest.
One sentence per industry explaining why the pain is structurally present there.

**3. Buying Trigger Events (3)**
External, observable signals that indicate a prospect is in an active
buying window right now. Must be researchable via LinkedIn, job postings,
press releases, or Google — no inside knowledge required.
Each trigger should complete: "I reached out because I noticed..."

**4. Hard Disqualifier (1)**
A single, specific criterion that disqualifies a prospect on sight —
before investing any outreach time. Not a soft filter. A definitive no.
Something checkable in under 60 seconds.

```
OUTREACH ACTIVATION — [Company/Context]
────────────────────────────────────────────────────────
LINKEDIN SIGNALS:
  1. [Observable signal]
  2. [Observable signal]
  3. [Observable signal]
  4. [Observable signal]
  5. [Observable signal]

HIGH-PROBABILITY INDUSTRIES:
  1. [Industry]: [Why the pain is structurally present]
  2. [Industry]: [Why the pain is structurally present]
  3. [Industry]: [Why the pain is structurally present]

BUYING TRIGGER EVENTS:
  1. [Trigger]: [What it signals + where to find it]
  2. [Trigger]: [What it signals + where to find it]
  3. [Trigger]: [What it signals + where to find it]

HARD DISQUALIFIER:
  [Single criterion. If this is true, skip them.]
────────────────────────────────────────────────────────
```

---

## Global Rules

- Do not generate a generic persona — every field must be specific enough
  to use in a headline or email subject line
- If an answer is vague, push back: "Can you give me a specific example?"
- The synthesized statement must pass this test: could you write a cold email
  subject line from it? If not, it's too vague
- The outreach activation layer is only as good as the ICP statement it draws
  from — do not skip the 10-question intake to get to it faster
- Save output to `outputs/YYYY-MM-DD-icp.md`; include outreach activation block if generated
- If the result is approved as canonical, also update `context/icp.md` so other skills read it.
