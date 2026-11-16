---
name: fact-check
description: Verify factual claims in a content draft before publishing. Use when the user says "fact-check this", "verify this", "is this accurate", "/fact-check", or before publishing content that contains statistics, product claims, company names, or technical assertions. Searches each claim against web sources, flags inaccuracies, and outputs a corrected draft.
---

## Context Check

On start, read `context/company.md` at the workspace root if it exists (company, ICP, positioning, voice). Also read any other file in `context/` that matches this task.

If context exists:
- Load ICP, offer, voice rules, constraints, and engagement context silently
- Skip any intake questions already answered in `context/`
- Confirm loaded context in one line: "Working from [company] context."

If no context: run normally — prompt for inputs as usual.

# Fact Check

## Purpose

Quality gate for content before it goes live. Extract every verifiable claim from a draft, check each against multiple web sources, and produce a corrected draft with a confidence-rated audit trail. This is not editing for voice — it's editing for truth.

**Input:** Draft file path, pasted text, or "check the last thing we wrote"
**Output:** Fact-check report + corrected draft (if changes needed)

---

## What Counts as a Claim

A claim is any statement that can be independently verified or falsified:
- Statistics, numbers, percentages, dates
- Product names, features, pricing, launch dates
- Company names, funding rounds, acquisitions
- Technical assertions ("X supports Y", "Z uses protocol W")
- Attribution ("according to X", "X said Y")
- Comparative statements ("fastest", "first", "only")

Not claims (skip these):
- Opinions, predictions, personal anecdotes
- Rhetorical questions
- Subjective assessments ("this is impressive")

---

## Process

### 1. Receive the draft

Accept via file path, pasted text, or reference to a file already in the conversation. Read the full content.

### 2. Extract claims

List every verifiable claim as a numbered inventory:

```
Claims identified:
1. "Moonshot AI launched Kimmy in March 2026"
2. "Open-source, available on GitHub"
3. "Processes 10x faster than GPT-4"
...
```

Show the list. If the operator wants to add or remove claims, adjust before proceeding.

### 3. Verify each claim

For each claim, search the web using 2-3 distinct queries to find corroborating or contradicting sources. Rate each:

| Rating | Meaning |
|--------|---------|
| Verified | 2+ credible sources confirm |
| Partially true | Core idea is right but details are wrong (date, number, attribution) |
| Misleading | Technically true but framed in a way that distorts |
| Unverified | Cannot find corroborating sources — may be true but risky to publish |
| False | Sources contradict the claim |

### 4. Present the report

```
Fact-check report for [draft name]:

✅ Verified (N claims)
  1. "Moonshot AI launched Kimmy in March 2026" — confirmed (TechCrunch, The Verge)

⚠️ Partially true (N claims)
  3. "Processes 10x faster than GPT-4" — benchmarks show 6-8x on specific tasks,
     not a blanket 10x. Recommend: "up to 8x faster on [specific benchmark]"

❌ False (N claims)
  ...

❓ Unverified (N claims)
  ...

Overall: [X/Y] claims verified. [N] corrections recommended.
```

### 5. Produce corrected draft

If any claims need correction:
- Generate a corrected version of the full draft
- Preserve the operator's voice exactly — only change the factual content
- Mark each correction inline with a brief note: `[corrected: was "10x", now "up to 8x per [benchmark]"]`
- Save corrected draft alongside the original: same path with `-factchecked` suffix

If all claims verified: confirm "All claims check out. Draft is clean."

### 6. Handle edge cases

- **Breaking news / very recent events**: If a claim is about something from the last 48 hours, flag it as "recent — verify before publish" even if one source confirms. Single-source confirmation on fresh news is not enough.
- **Self-referential claims**: If the draft references the author's own stats or experience (sessions, commits, revenue numbers), don't web-search those — flag them as "self-reported, operator to confirm."
- **AI boundary**: If web search returns conflicting information from equally credible sources, present both sides and let the operator decide. Don't pick a winner.

---

## Rules

- Never change voice, tone, or style — only facts
- Never remove a claim without flagging it first — the operator may have private knowledge
- Always show sources for corrections so the operator can verify your verification
- If the draft is clean, say so in one line. Don't pad the report.
- Apply CLAUDE.md AI Usage Boundaries — don't search for or surface confidential company details
