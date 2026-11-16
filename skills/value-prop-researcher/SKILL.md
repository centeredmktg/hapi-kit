---
name: Value Prop Researcher
description: This skill should be used when the user asks to "research a company's value prop", "map a website", "analyze what [company] sells", "deep dive a prospect's site", "extract value props from [URL]", or wants a structured breakdown of a company's products, features, benefits, personas, and differentiators from their website. 3-part stateful workflow with approval gates.
---

## Context Check

On start, read `context/company.md` at the workspace root if it exists (company, ICP, positioning, voice). Also read any other file in `context/` that matches this task.

If context exists:
- Load ICP, offer, voice rules, constraints, and engagement context silently
- Skip any intake questions already answered in `context/`
- Confirm loaded context in one line: "Working from [company] context."

If no context: run normally — prompt for inputs as usual.

# Value Prop Researcher

## Purpose

Deep value prop extraction from a company's own website. NOT competitive analysis — that's `/intel`. This skill produces a structured, quantitative, site-derived inventory of everything a company claims: products, features, benefits, verticals, personas, case studies, differentiators, resources, and pricing.

**Composes with `/intel`:** Run `/value-prop-researcher` for depth on a target, then `/intel` for the competitive lens.

---

## State Machine

```
current_part: 1 | 2 | 3
current_section: 1..9  (Part 3 only)
```

**Approval required at:**
- End of Part 1 → before starting Part 2
- End of Part 2 → before starting Part 3
- End of each Part 3 section → before next section

**Never skip an approval gate. Never combine parts in one response.**

---

## Trigger

User provides a company URL (or name). Begin immediately at Part 1.

---

## Part 1: Site Structure Map

**Goal:** Build a hierarchical map of the site using footer and top nav as primary sources of truth.

**Process:**
1. Browse the company site — start at the homepage, footer, and top nav
2. Follow major nav links to identify main sections and sub-pages
3. Output a hierarchical bullet list of all main pages and sub-pages

**Output format:**
- Opening sentence: *"The [Company Name] website is structured into several main sections and sub-sections…"*
- Hierarchical bullets: main sections → sub-pages
- Keep structural, not interpretive — list what exists, don't editorialize

**Then ask:** *"Does this structure look complete? Approve to proceed to Part 2 (Value Prop Inventory)."*

---

## Part 2: Value Prop Inventory

**Goal:** Classify everything found on the site into the 9-section taxonomy. Highly structured, minimal prose.

**Process:**
1. Browse the pages identified in Part 1
2. Classify each item into exactly one of the 9 sections (see taxonomy below)
3. Format as a structured list under each section header

**Formatting rules:**
- Most bullets = names only, no explanations
- Exception: Customer stories = *"[Customer Name]: 20–30 word success summary"*
- Exception: Pricing = concise descriptor if plans are named (e.g., "Starter / Pro / Enterprise — custom pricing")
- No fluffy marketing language, no hype verbs
- Do not interpret — classify and list

**Then ask:** *"Does this inventory look accurate and complete? Approve to proceed to Part 3 (Deep Expansion, one section at a time)."*

---

## Part 3: Deep Expansion (Section by Section)

**Goal:** Expand each Part 2 bullet with sourced detail — metrics, outcomes, scale figures, specifics.

**Process:**
- Work one section at a time
- Browse site again as needed to gather detail for that section
- Expand each Part 2 bullet: add percentages, hours saved, customer counts, ARR/ACV figures, case study outcomes, feature specifics
- Do not repeat source text verbatim — synthesize
- If information is unavailable on the site, say so explicitly
- After completing each section, ask for approval before the next

**Approval prompt after each section:**
*"Section [N] ([Section Name]) complete. Approve to continue to Section [N+1] ([Next Section Name])?"*

**After Section 9:** *"Deep expansion complete. All 9 sections expanded."*

---

## 9-Section Taxonomy

| # | Section | What belongs here |
|---|---------|-------------------|
| 1 | **Products / Platforms / Solutions / Services** | Named offerings — platforms, modules, products, service lines |
| 2 | **Features** | Capabilities, functions, technical components within products |
| 3 | **Benefits** | Outcomes, value delivered, business improvements enabled |
| 4 | **Industries / Verticals Served** | Industries or company types explicitly targeted |
| 5 | **Personas / Job Titles** | Roles, teams, stakeholders named on the site |
| 6 | **Customer Stories / Case Studies** | Named customers + outcome summaries |
| 7 | **USPs / Competitor Differentiators** | Superiority claims, comparison-page content, "why us" statements |
| 8 | **Other Resources** | Blog themes, whitepapers, reports, newsletters, news topics |
| 9 | **Pricing** | Plans, packaging, pricing model, enterprise/custom options |

---

## Content Classification Guide

Use this to resolve ambiguity:

- **Products** = named platforms, modules, solutions, service lines (e.g., "Salesforce Sales Cloud", "HubSpot CRM")
- **Features** = capabilities or technical components within a product (e.g., "AI-powered lead scoring", "email sequencing")
- **Benefits** = outcomes or value statements (e.g., "reduce churn by 30%", "close deals faster")
- **Verticals** = industries or company types named as targets (e.g., "Financial Services", "Mid-market SaaS")
- **Personas** = job titles or teams named as buyers/users (e.g., "VP of Sales", "Revenue Operations")
- **Customer stories** = named customers with an outcome (e.g., "Acme Corp: reduced onboarding time by 40%")
- **USPs** = direct comparison claims or "why us" differentiators (e.g., "only platform with X", "vs. Competitor Y")
- **Resources** = blog categories, report titles, whitepaper topics, newsletter names
- **Pricing** = plan names, pricing model type (seat-based, usage-based), any visible pricing

**When in doubt:** Features describe *what it does*. Benefits describe *what the customer gets*. Products are named things. Keep them separate.

---

## Global Rules

- Do not invent facts — only use site-derived information
- If a page is unavailable or gated, note it and move on
- Avoid fluffy language: no "revolutionize", "seamless", "game-changing"
- Distinguish products / features / benefits / personas / verticals carefully — do not conflate
- Stay objective and customer-centric
- Include quantitative details wherever available (metrics, scale, percentages)
- Never skip an approval gate
- Never combine parts in a single response
