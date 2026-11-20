---
name: cms-content-qa
description: Check a CMS-driven website's content for publish-blocking defects (empty titles or meta descriptions, empty or thin bodies, placeholder text, duplicate titles, working-copy slugs, missing authors or required fields, empty alt text). Use when the user says "content QA", "check the CMS", "pre-publish check", "what's broken on the blog", "/cms-content-qa", before a publishing push, or on a weekly schedule. Works on any site with a sitemap; checks Webflow CMS items (including drafts) through the Webflow Data API.
---

## Context Check

On start, read `context/company.md` at the workspace root if it exists, and `context/content-qa.json` if it exists (the site's collections and required fields). Confirm in one line which site and mode you're using.

# CMS Content QA

## Purpose

A publishing gate that doesn't depend on anyone remembering a checklist. Every check is a rule, so a script does the checking and Claude does the parts that need judgment: reading the report, deciding what to fix first, and writing the fixes.

**Input:** a site URL (sitemap mode) or a Webflow config (webflow mode)
**Output:** `outputs/YYYY-MM-DD-content-qa.md` + `.json`, and a prioritized fix list

## Run the checks (don't re-check by hand)

Use the bundled script. Never re-implement the checks by fetching pages one at a time in the conversation. That spends usage and gives inconsistent results.

**Sitemap mode** checks what search engines see on the live site. Scope it to content collections, because landing pages will trip the word-count check.

```bash
python3 -I <skill-dir>/scripts/cms_qa.py sitemap https://www.example.com \
  --include /blog/ --include /integrations/ --config context/content-qa.json
```

**Webflow mode** checks CMS items before they're live, drafts included. It needs a `WEBFLOW_TOKEN` with CMS read scope, set in the environment. Never paste the token into the conversation.

```bash
WEBFLOW_TOKEN=... python3 -I <skill-dir>/scripts/cms_qa.py webflow --config context/content-qa.json
```

The script exits with code 1 if any page has a blocking issue, so it can gate a scheduled job or CI.

## Config (`context/content-qa.json`)

If the file is missing, offer to create it. Find collection IDs with the Webflow MCP (list sites → list collections) or in Webflow's collection settings.

```json
{
  "min_words": 300,
  "body_selector": "rich-text",
  "collections": [
    {
      "id": "<collection id>",
      "label": "Blog",
      "url_prefix": "/blog/",
      "title_field": "name",
      "body_field": "post-body",
      "author_field": "author",
      "required": ["seo-title", "meta-description", "post-body", "author", "publish-date"],
      "min_words": 400
    }
  ]
}
```

`body_selector` is the class on the rich-text wrapper. It gives sitemap mode a cleaner word count than the whole page.

## What each check means

| Check | Severity | Usual cause | Fix |
|---|---|---|---|
| Empty title / meta description | block | CMS SEO fields not bound in the collection template | Bind them to CMS fields with a fallback to the item name, then hand-write the important ones |
| Thin body | block | Published before the body was written, or a "news" stub | Write the body, or unpublish / noindex it |
| Placeholder text | block | Template filler (lorem ipsum, "Author 1", "Meta Title:") | Replace it |
| Duplicate title | block | The same piece entered twice | Keep one, 301 the other |
| Required field missing | block | No required-field rule in the CMS | Fill it in, then make the field required in the collection settings |
| Suspect slug (`-2`, hash suffix, "draft", "copy") | warn | Duplicate items or leaked working copies | Check for a twin; merge or rename |
| Missing author | warn | Bylines left to the company name | Add a named author with a bio |
| Title > 60 / description > 160 | warn | Too long for the search result | Tighten |
| Empty alt text | warn | Alt never written | Describe the image; logos get the company name |
| Page didn't load | warn | Rate limiting or timeouts | Re-run with `--workers 1`; if it repeats, check hosting and CDN rules |

## After the run

1. **Lead with the count of blocking pages and the pattern behind them.** "120 pages, one cause" beats a list of 120 pages. When many pages fail the same way, it's a template or field-settings fix, not page-by-page work.
2. **Rank the fixes:** blocking checks on the pages that matter most first (customer stories, integration pages, money pages), then fixes that clear many pages at once, then warnings.
3. **Offer to write the fixes:** titles, meta descriptions and alt text drafted in the site's voice (read `context/`). Run `humanizer` on anything longer than a sentence.
4. **Applying fixes through the Webflow MCP: drafts only.** Update CMS items as drafts or staged changes. Never publish or delete items. Show the exact field changes and get a yes before writing. A person publishes.
5. **Suggest prevention.** Make the failing fields required in the CMS and schedule the script weekly (`/schedule` or cron), so the report shows a trend instead of a one-off.

## Boundaries

- This only reads the site. Changes to the CMS happen only through step 4, with confirmation.
- Respect rate limits: keep `--workers` at 3 or below on shared hosting.
- Content judgment (is it good, is it on-message) is not this skill's job. Use `fact-check` for claims and `humanizer` for voice.
