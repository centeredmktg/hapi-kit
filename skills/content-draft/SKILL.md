---
name: content-draft
description: Draft a content piece from an approved brief, using the content type's template, then run the pre-publish checklist and optionally save it as a CMS draft (Webflow MCP), never published. Use when the user says "draft this", "write the post from the brief", "/content-draft", or hands over a brief from content-brief. Produces body copy plus the SEO title, meta description, slug, alt text and internal links the CMS needs.
---

## Context Check

On start, read `context/company.md` at the workspace root if it exists (positioning, category language, voice, words we use and don't). Confirm in one line: "Working from [company] context."

If there's no brief, offer to run `content-brief` first. Drafting without one is how thin and duplicate pages happen.

# Content Draft

## Purpose

Make drafting fast without making it sloppy. The draft arrives with every field the CMS needs filled in and the checklist already run, so review is about substance, not missing pieces.

**Input:** an approved brief (file path or pasted)
**Output:** `outputs/YYYY-MM-DD-draft-<slug>.md`, and optionally a CMS draft item

## Process

1. **Load the template** for the brief's content type from `references/content-types.md`. Follow its required parts and minimum length.
2. **Draft the body.**
   - Answer the target question in the first 2–3 sentences.
   - One idea per section. Use the company's category language exactly as written in `context/`.
   - Put proof where the claim is. Use only proof the brief marks *have*. Where proof is *need*, leave a visible `[NEED: …]` marker rather than inventing a number, quote or customer.
3. **Write the CMS fields:**
   - SEO title (≤60 characters, query near the front)
   - Meta description (≤155 characters: what the reader gets, no hype)
   - Slug (short, lowercase, no dates or suffixes)
   - Excerpt
   - Alt text for each image
   - Author and publish date from the brief
4. **Add internal links** from the brief, in the body (not only in a related-posts block). Use descriptive anchors.
5. **Edit:** run `humanizer` on the body. Run `fact-check` if the draft has statistics, product claims or named companies.
6. **Run the pre-publish checklist** below and show the results. Anything unchecked is listed as an open item, not hidden.

## Pre-publish checklist

- [ ] Body meets the type's minimum, and every required part is present
- [ ] No `[NEED: …]` markers left, or each is listed as an open item with an owner
- [ ] SEO title ≤60 and meta description ≤155, written by hand
- [ ] Named author (a person), and publish date set
- [ ] Slug clean; no existing page on the same topic (checked in the brief)
- [ ] 3+ in-body internal links
- [ ] Third-party material: rights confirmed, source named and linked
- [ ] Alt text on every image
- [ ] Expert reviewer named for technical or product claims

## Saving to the CMS (optional)

Only when the user asks, and only if a Webflow MCP (or another CMS connection) is available:

- **Create or update the item as a draft.** Never publish, schedule or delete. Publishing is a person's job.
- **Show the field mapping before writing:** CMS field → value. Field names come from the collection schema (list it with the MCP) or from `context/content-qa.json`.
- **After saving,** suggest running `cms-content-qa` in webflow mode to confirm the item passes before someone publishes it.

## Output format

```markdown
# Draft: [title]
**Fields:** SEO title · Meta description · Slug · Excerpt · Author · Date
**Checklist:** [n of 9 passed] · Open items: [list with owners]

---
[body]

---
**Alt text:** [image → alt]
**Internal links used:** [anchor → URL]
```
