---
name: build-vs-buy-page
description: >-
  Use when drafting a /vs/diy, /vs/build-in-house, or "build vs. buy" page for a company whose buyers ask "couldn't we just build this?" Treats DIY as a competitor in the /vs/ section. Pulls numbers from /build-vs-buy and the talk track from /competitive-displacement DIY Mode so page and sales stay aligned.
---

# /build-vs-buy-page — DIY Is a Competitor

## Purpose

If the site leaves "couldn't we just build this?" open, the question doesn't go
away. It moves into an internal thread you're not in. This page answers it
before anyone asks, honestly enough that the buyer's own engineer would nod.

Output: a page draft (sections + copy + FAQ schema-ready Q&As) and a one-line
sales hand-off pointing to the matching talk track.

---

## Trigger

Invoked with /build-vs-buy-page

Inputs:
- Company + product (what the buyer would otherwise build)
- The DIY stack buyers actually reach for (e.g. Clay + Zapier + a spreadsheet,
  an internal script, "our engineers")
- A /build-vs-buy output if one exists. If not, run it first or ask for: build
  hours, tool costs, maintenance load, product price.
- Who should build it anyway (honest ICP-exclusion)

---

## Page Structure

1. **Hero — say the question out loud.**
   "Can you build this yourself? Yes. Here's what that actually takes."
2. **What's easy to build (honest).** Name the specific parts. Credibility jumps
   when you stop pretending it's impossible.
3. **Month 1 vs. Month 6.** Two columns. Month 1: v1 works, looks cheaper.
   Month 6: what changed (APIs, owner changed teams, edge cases, scope creep).
4. **True cost to build.** Ledger on both sides: tools, internal hours,
   maintenance (itemized), opportunity cost. Numbers, not adjectives. Show the
   assumption chain so the reader can swap in their own numbers.
5. **When building IS the right call.** Core to your product, or a team that will
   own it at month 6. Say it plainly.
6. **The split.** "Build the part that's core to you. We run the part that
   breaks." Only if the product supports it.
7. **FAQ (AEO).** 4–6 questions in the buyer's own words, e.g.
   - Can we build this with [their DIY stack]?
   - Who owns it six months from now?
   - What happens when [upstream API] changes?
   - What does it cost if we build it?
   Answers are 40–80 words, self-contained, first sentence answers the question.
8. **CTA + forwardable.** Link to a one-pager the champion can send internally.

---

## Output Format

```
# [Product] vs. Building It Yourself
URL: /vs/[diy|build-in-house]
Title tag: [≤ 60 chars] | Meta: [≤ 155 chars]

[Sections 1–8 with draft copy]

## FAQ (schema-ready)
Q: ... / A: ...

## Assumptions
[every number on the page → its source or "assumption: change this if…"]

## Sales Hand-off
Talk track: run /competitive-displacement in DIY Mode with [DIY stack].
```

---

## Rules

- Lives in /vs/, not the blog. A blog post doesn't answer /vs/ intent.
- Never say it can't be built. Name what's easy first.
- Every number shows its assumption. No unsourced savings claims.
- Section 5 (when building is right) is not optional.
- Never name a competitor's product in a negative frame. The DIY stack can be
  named; it's the buyer's own tools, not a rival.
- Voice: client's brand voice, not a personal LinkedIn voice.
