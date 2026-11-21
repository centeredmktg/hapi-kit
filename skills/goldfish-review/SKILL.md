---
name: goldfish-review
description: Use when a spec, design doc, implementation plan, proposal, SOW, or any document drafted in this session needs review before it ships or gets built — "goldfish this", "review this with fresh eyes", "red-team this doc", "is this spec ready", "pressure test this proposal". Spawns fresh-context reviewer subagents that never saw the conversation, then resolves their findings in the main session.
---

# Goldfish Review

## Purpose

Never let the agent that wrote a document grade it.

- **Elephant** = this session. It holds the context, wrote the draft, and resolves findings.
- **Goldfish** = reviewer subagents spawned with **no conversation history**. They see only the document plus a reading list. Their blindness is the point: it exposes every assumption the Elephant forgot it was making.
- **The user** decides every contested finding and every trade-off.

A review run in the same context is not a goldfish review. If no subagent tool is available, stop and say so.

## When to use / not use

Use for: feature specs, implementation plans, architecture notes, proposals, SOWs, pitch pages, framework docs — anything where an unstated assumption is expensive later.

Skip for: short emails and posts (use `humanizer`), code diffs (use `code-review`), and first drafts still changing shape (finish drafting first).

## Step 1 — Configure (one message, then go)

Determine, without asking unless genuinely ambiguous:

1. **Target**: file path and scope (`full file` or a named section).
2. **Doc type** → default reviewer set:

| Doc type | Reviewers |
|---|---|
| Feature spec / design | design-critic, zoom-out, comprehension |
| Implementation plan | implementation-readiness, codebase-accuracy, zoom-out |
| Proposal / SOW / pitch | buyer-skeptic, comprehension, zoom-out |
| Framework / teaching doc | comprehension, design-critic |
| Stuck on a trade-off | add inventive-catalyst |

3. **Reading list**: source files, data, or prior docs the reviewers need to check claims. For URLs, save the page locally first; subagents may not fetch.

State the plan in one line ("Reviewing X with A, B, C against reading list Y") and start. Persona definitions live in `references/personas.md`.

## Step 2 — Spawn the swarm

Launch all reviewers in parallel with the `Agent` tool (`subagent_type: general-purpose`), one message, multiple calls. Each prompt contains ONLY:

- The persona block from `references/personas.md` (verbatim), including the universal mandates.
- The target path and scope.
- The reading list.
- The output contract below.

Never paste conversation context, your reasoning, or what you think the weak spots are. Handing a reviewer your hypothesis is how you get it confirmed.

**Output contract (each reviewer):**
```
FINDING <n>
severity: blocker | major | nit
location: <section heading or line range>
issue: <what is wrong or missing>
why: <the concrete consequence if shipped as-is>
```
Plus a final line: `REVIEWED: yes` (so silent failures are detectable).

A reviewer that errors or returns no `REVIEWED: yes` did not review. Retry once; then record it as **not run**. Never count it as zero findings.

## Step 3 — Resolve (Elephant)

Merge findings into one list with ids (`<reviewer>-r<round>-<n>`), dedupe same-issue-same-location. Classify each:

- **CONTEST** — the reviewer misread or lacked context. Cite evidence a reader could check (file + symbol, or a sentence in the doc). If the doc *should* have said it, it's not a contest: it's a fix.
- **FIX** — propose the exact text change.
- **DECIDE** — a real trade-off only the user can call. State both sides in one line each.

Write `goldfish-review-report.md` next to the target (findings, classification, proposed fixes, not-run reviewers). Then present to the user:

1. DECIDE items first, one at a time.
2. FIX items as a batch: "Apply all N fixes? (or name exceptions)".
3. CONTEST items as a short list for visibility; the user can overturn any.

Apply approved fixes with Edit.

## Step 4 — Loop until converged

Fresh reviewers sample differently every round, so zero findings is rare even on a good doc. Rules:

- **Settled** = contested, or accepted as known risk. Don't reopen if raised again at the same location.
- **Fixed ≠ settled.** Same issue at the same location after a fix means the fix failed: reopen.
- **Clean round** = no unsettled blocker/major, and every reviewer ran. Nits don't block.
- **Converged** = two consecutive clean rounds.
- **Cap** = 4 rounds. **Churn** = a new finding that reverting a fix would resolve.

On converge: report rounds run and residual nits. On cap or churn: list open findings by severity and ask one question: ship as-is, run past the cap, or back to drafting.

Wait for the user between rounds unless they said "run it to convergence".

## Rules

- Reviewers are read-only. They never edit.
- Spawn fresh reviewers each round; never reuse one (it stops being a goldfish).
- Cost scales with reviewers × rounds. Default 3 reviewers; say so before going above 5.
