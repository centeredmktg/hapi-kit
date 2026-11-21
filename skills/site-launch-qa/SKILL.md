---
name: site-launch-qa
description: Use when a website is about to move from staging/preview to production, when someone asks "are we ready to launch", "what do we QA before go-live", "launch checklist", "cutover", "point DNS", or before any domain/DNS switch on a marketing or lead-gen site. Also use for re-launches, domain migrations, and platform moves (Squarespace/Webflow/WordPress → custom).
---

# Site Launch QA

## Core principle

A launch fails silently in three places: **leads that don't arrive, URLs that stop resolving, and email that stops sending.** Visual polish is the fourth priority, not the first. Gate order follows that.

Staging can't prove everything. Analytics, canonical-host logic, SSL, and some third-party embeds (domain-allowlisted widgets) only behave on the real domain. Those items belong in the **post-cutover** gate, tested in the first hour, not marked done on staging.

## How to run it

1. **Load the project overlay.** Look for, in order: `docs/cutover-checklist.md`, `docs/launch*.md`, the project `CLAUDE.md`, and project memory. Project-specific items (named integrations, owners, env vars, known-open exceptions) come from there. This skill is the spine; the overlay is the detail.
2. **Run the automated gate first.** Find the project's verify commands (`package.json` scripts, `docs/ci.md`, CI workflow). Run them against the build *and* against staging. Paste real output; a gate without output is not passed.
3. **Walk gates 1–7 below.** Each item gets PASS / FAIL / OPEN (with owner) / N/A (with reason). Don't mark an item PASS from reading code; mark it from observing behavior.
4. **Write the run report** to `docs/launch-qa-YYYY-MM-DD.md` in the project (format at bottom). Each run is a new dated file so regressions between runs are visible.
5. **Verdict:** GO only if gates 0–5 have no FAIL and every OPEN has a named owner who accepted it. Cutover itself (gate 6) is irreversible-ish and shared-state: always get the client's explicit go.

## Gate 0 — Release is what you think it is

- [ ] All intended branches/PRs merged to the deploy branch; nothing sitting in an unmerged feature branch (`git log origin/main..<branch>` for each open launch branch)
- [ ] Staging is running the exact commit you intend to promote (check the deploy's commit SHA)
- [ ] CI green on that commit; branch protection noted if absent (checks report but don't block)
- [ ] No QA-only switches left on: skip-required-fields flags, preview/draft toggles, "demo" ribbons, test-mode keys, `console.log` of PII. Grep for them.

## Gate 1 — Automated checks (run, don't read)

- [ ] Types + build + unit tests
- [ ] Link crawl: zero internal 404s, zero broken `#anchors`, one `<h1>` per page, valid JSON-LD
- [ ] Browser smoke at phone/tablet/desktop widths, Chromium + WebKit (Safari breaks differently)
- [ ] Production image boots from the real Dockerfile and passes the healthcheck (files missing from runtime `COPY` lists only fail here)
- [ ] Any project-specific verifier (punch lists, content rules) against **staging**, not only the local build

## Gate 2 — Lead capture (the money path)

For **every** form and every variant (each loan type / product / branch of a multi-step form):
- [ ] Submit a real test lead on staging; confirm it lands in **every** destination (CRM, DB, sheet, email notification) with all fields populated and mapped to the right properties
- [ ] Owner assignment / routing fires (round robin, workflow, notification). A lead with no owner is a lost lead
- [ ] Failure mode is safe: kill the CRM token in a test env, confirm the lead is still stored somewhere and the visitor isn't shown a false error (or a false success with nothing saved)
- [ ] Required fields actually required; validation messages readable on mobile
- [ ] UTM / attribution params survive the redirect chain and land on the record
- [ ] Spam handling: honeypot/captcha present; test domains (`example.com`, `test.com`) don't get silently dropped by CRM rules you didn't know about
- [ ] Production credentials are set in the **production** environment (not just staging), and a dry-run verifier against the prod CRM passes
- [ ] Delete test leads afterward, or tag them so the client's reporting isn't polluted

## Gate 3 — Content, claims, compliance

- [ ] Client's final copy approver has signed off (named person, date). Their tracker/punch list is the gate, not ours
- [ ] Zero placeholders: grep for `lorem`, `TODO`, `TBD`, `PARITY GAP`, `XXX`, `[placeholder]`, `example.com`, sample/demo data labels
- [ ] Legal pages (privacy, terms, disclosures) are client-supplied final text. **Never ship generated legal copy**
- [ ] Industry claims checked (rates, "guaranteed", licensing statements, regulated-industry disclaimers) against what the client confirmed in writing
- [ ] People: bios, titles, headshots current; no departed staff in testimonials or team pages
- [ ] Contact details correct everywhere: phone, email, address, footer, schema `Organization`
- [ ] Nothing that names a partner/vendor the client doesn't want public (check the overlay for "never name" rules)

## Gate 4 — SEO and URL continuity

- [ ] **Crawl the OLD live site's sitemap** (and top pages from Search Console / analytics) and confirm every old URL either resolves or 301s to the right new page. The redirect map you wrote is not proof you covered every URL
- [ ] Redirects are 301 (permanent), single hop, and preserve query strings
- [ ] Canonical host decided (apex vs `www`) and consistent across: server redirect, `<link rel=canonical>`, sitemap URLs, `robots.txt` Sitemap line, schema URLs, OG URLs. Mismatch here is the most common silent SEO bug
- [ ] Staging/preview hosts are noindex; production host is **not** noindex. Verify the mechanism will flip on the real host (header logic, env flag, meta tag)
- [ ] Sitemap includes every indexable page and excludes noindex/draft pages
- [ ] Titles/descriptions unique and within length; OG image + favicon on every template
- [ ] Rich Results Test on one page per schema type
- [ ] Intentional noindex pages (drafts, internal review pages, pending content) listed and confirmed as intentional with the client

## Gate 5 — Performance, accessibility, security

- [ ] Lighthouse (mobile) on home, top landing page, primary form page: note LCP/CLS/INP; fix anything red
- [ ] Keyboard-only pass through the primary form; labels on inputs; contrast on CTAs
- [ ] Security headers present; no secrets in client bundle (grep built JS for key prefixes); `/api/` not indexable
- [ ] 404 page is branded and returns HTTP 404
- [ ] Every env var the code reads is set in production. Diff the list of `process.env.*` / `import.meta.env.*` in the source against the production environment. Documented env tables drift

## Gate 6 — DNS cutover pre-flight (client go required)

- [ ] **Export the full current DNS zone first.** MX, SPF/DKIM/DMARC TXT, Search Console verification, CRM email-sending CNAMEs, and any other subdomains (app., mail., status.) must survive the change. Breaking email is worse than delaying the launch
- [ ] Lower TTL on the records you'll change 24–48h ahead
- [ ] Custom domain + SSL provisioned on the host for apex **and** `www`
- [ ] Domain registration: who owns it, auto-renew on, not tied to the old platform's subscription you're about to cancel
- [ ] Rollback plan written: old site stays live/paid until post-cutover passes; the exact DNS values to restore are in the run report
- [ ] Cutover window: weekday morning, both you and the client reachable, not before a holiday

## Gate 7 — Post-cutover (first hour, then day 1 and week 1)

First hour, on the real domain:
- [ ] Apex and `www` both resolve with valid SSL; non-canonical redirects to canonical
- [ ] Production host is indexable (no noindex header/meta); staging still noindex
- [ ] Re-run the link crawl and redirect verifier against production
- [ ] One real lead per form type lands in every destination with an owner
- [ ] Analytics/tag manager fires on page view and each key event (real-time view)
- [ ] Domain-allowlisted embeds (maps, widgets, booking tools) render
- [ ] Send and receive a test email on the domain (MX intact)

Day 1: submit sitemap in Search Console; request indexing on key pages; uptime monitor on the healthcheck; confirm the client's team got their lead notifications.
Week 1: Search Console coverage + 404 report; compare lead volume to pre-launch baseline; only now cancel the old platform.

## Common mistakes

| Mistake | Reality |
|---|---|
| "Tests pass, we're good" | Tests don't touch DNS, email records, prod env vars, or the client's CRM workflows |
| Testing one form variant | Multi-step forms branch; each branch maps different fields |
| Marking analytics PASS on staging | Tags scoped to the real domain don't fire on staging. It's a post-cutover item |
| Trusting the redirect map | Crawl the old site; the map only contains URLs someone remembered |
| Canceling the old platform at launch | That's your rollback. Wait a week |
| Treating cutover as an ops detail | Zone records beyond A/CNAME (mail, verification) are where launches break |

## Run report format

`docs/launch-qa-YYYY-MM-DD.md`:

```markdown
# Launch QA — <site> — YYYY-MM-DD
Commit: <sha> on <staging URL> · Verdict: GO / NO-GO / GO with named OPENs

## Blockers (FAIL)
- [G2] <item> — <evidence> — owner

## Open, accepted (owner + date)
- [G3] <item> — owner accepted <date>

## Gate results
| Gate | Pass | Fail | Open | N/A |
|---|---|---|---|---|

## Evidence
<command output, lead IDs, screenshots, URLs checked>

## Rollback values
<DNS records to restore>
```
