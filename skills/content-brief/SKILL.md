---
name: content-brief
description: Turn a topic, search query, hub plan or SME conversation into a one-page content brief that a writer (person or Claude) can draft from without a meeting. Use when the user says "brief this", "content brief", "plan this post", "/content-brief", or is about to start drafting a piece with no brief. Names the content type, target question, the page it supports, required proof, internal links and the expert reviewer.
---

## Context Check

On start, read `context/company.md` at the workspace root if it exists (offer, ICP, positioning, category language, voice). Also read any content plan, hub/cluster plan or editorial calendar in `context/` or `plan/`. Confirm in one line: "Working from [company] context."

If no context: ask for the company, the audience and the topic, then proceed.

# Content Brief

## Purpose

Most content problems start before the draft: no clear reader, no target question, no proof, nobody to check the facts. A brief fixes that in one page, and it's the first gate in the publishing process. Drafting starts when the brief is approved.

**Input:** a topic, a target search, a hub/cluster plan entry, notes or a transcript from a subject expert, or a gap from a content QA or SEO report
**Output:** `outputs/YYYY-MM-DD-brief-<slug>.md`

## Process

1. **Name the job.** One sentence: what the reader should know, believe or do after reading. If you can't write it, ask before going further.
2. **Pick the content type** from `../content-draft/references/content-types.md`. The type sets the template, the required parts and the minimum length.
3. **Pin the target.**
   - The search query or reader question, in the reader's words.
   - Search intent: learn, compare or buy.
   - If web search is available, look at what currently ranks. Note the page types (guide, comparison, product page) and the gaps a better page could fill. Don't copy structure or wording.
4. **Check for an existing page first.** Search the site (sitemap, CMS or a `site:` search) for a page on the same topic. If one exists, the brief becomes an update brief, not a new page. Duplicates are the most common content-ops defect.
5. **List the proof the piece needs:** customer results with numbers, data, quotes, product facts. Mark each as *have* (with source) or *need* (and from whom). A brief with no proof becomes an opinion post, so say so.
6. **Plan the links:** 3+ internal links (product, integration, hub or money pages), and the one call to action that matches the intent.
7. **Assign the people:** named author (a person, not the company), subject-matter reviewer, and approver.
8. **Write the brief** in the format below. Keep it to one page.

## Brief format

```markdown
# Brief: [working title]

**Job:** [one sentence]
**Type:** [content type] · **Min length:** [from type] · **Intent:** learn / compare / buy
**Target:** "[query or reader question]" · **Supports:** [the page this feeds, e.g. a product or hub page]
**Existing page?** none / update [URL]

## Reader
[Who, what they already know, what they're trying to decide]

## Angle
[What this piece says that the current top results don't]

## Outline
[H2s with a line each. The first section answers the question directly in 2–3 sentences.]

## Proof
| Point | Have / need | Source or owner |

## Links
- Internal: [3+ URLs and the anchor idea for each]
- CTA: [one]

## People
Author: · Expert reviewer: · Approver: · Target publish date:
```

## Handoff

Offer to hand the approved brief to `content-draft`. If proof is marked *need*, list who to ask, and don't start drafting around the gaps.
