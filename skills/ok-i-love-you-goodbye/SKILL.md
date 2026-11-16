---
name: ok-i-love-you-goodbye
version: 3.0.0-lite
description: Use when the user says "ok I love you goodbye" or runs /ok-i-love-you-goodbye to close a session. Appends one short worklog entry recording what shipped, the decision behind it, and its impact. With "week" as the argument, rolls the week's entries into a weekly update draft instead.
---

# Session Close (lite)

A short written record of contributions, cheap enough to run every session. The user says goodbye and walks away, so write first and never wait for a reply.

## Close (default)

1. **Decide if there's anything to record.** A session that only answered a question or explored writes nothing. Print `Nothing shipped — no entry.` and stop.
2. **Append one entry** to `worklog/YYYY-MM.md` at the workspace root. Create the file and folder if they're missing. Append with the shell (`>>`); never rewrite the file, since other windows write to it too.

```markdown
### YYYY-MM-DD · {short topic}
- Shipped: {what exists now that didn't, with path or link}
- Decision: {what was decided} — {why, one clause}
- Impact: {effect on a tracked metric or a person's work} {mark "(to verify)" if not yet measured}
- Open: {next action, owner if not the user}
```

Rules:
- At most 6 lines. Use a second Decision line only if a second decision really mattered.
- Impact is concrete: accounts, pipeline, adoption by sales, time saved, a metric on the scorecard. Never adjectives. If there's no measurable effect yet, say what would show it and mark "(to verify)".
- Never invent numbers. A number comes from the conversation or a file, or it isn't written.
- Keep confidential detail at the level of the company's own internal norms. This log is a company record.

3. **Print:**

```
Logged → worklog/YYYY-MM.md · {topic}
Next session: {one-line paste-ready prompt built from Open}
```

That's the whole close. Nothing else is read or written.

## Week (`/ok-i-love-you-goodbye week`)

Read this week's entries (Mon–today) from `worklog/`. Draft a weekly update in `outputs/YYYY-MM-DD-weekly-update.md`:

- **Scorecard:** each metric that an entry's Impact touched, with the number if one exists.
- **Shipped:** 3–6 bullets, highest impact first.
- **Decisions worth knowing:** the ones a manager would want to hear about, with the why.
- **Issues:** Open items that are blocked or need someone else's call.
- **Unverified:** every "(to verify)" impact still unmeasured, so it gets checked rather than forgotten.

Present the draft and stop. The user edits and sends it.

## Common mistakes

| Mistake | Fix |
|---|---|
| Writing an entry for a session that shipped nothing | Skip it; an empty session isn't a contribution |
| Overwriting the month file | Append with `>>` only |
| Impact written as "improved messaging" | Name the thing it changed, or mark (to verify) |
| Asking questions before writing | Write first; this skill asks nothing |
