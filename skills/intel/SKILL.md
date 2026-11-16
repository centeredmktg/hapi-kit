# /intel — Company Intelligence Agent

## Context Check

On start, read `context/company.md` at the workspace root if it exists (company, ICP, positioning, voice). Also read any other file in `context/` that matches this task.

If context exists:
- Load ICP, offer, voice rules, constraints, and engagement context silently
- Skip any intake questions already answered in `context/`
- Confirm loaded context in one line: "Working from [company] context."

If no context: run normally — prompt for inputs as usual.

## Intel Caching

Before fetching any external source, check `outputs/intel/` for an existing file from the same source dated within 30 days. If found, use it — do not re-fetch.

When fetching new content, save the full raw text to:
`outputs/intel/YYYY-MM-DD-[source-slug].md`

Required header:
```
source: [full URL]
date: YYYY-MM-DD
type: homepage | sitemap | web-search | linkedin | competitor | other
```

## Purpose
Research any company and extract a structured intelligence profile that can be 
used to inform content, outreach, positioning, or competitive analysis.

## Trigger
Invoked with /intel followed by a company URL or name.
Example: /intel https://somecompany.com

## Process
Step 1: Find the sitemap or site structure. Start at /sitemap.xml. If unavailable, 
crawl the main nav to identify key pages.

Step 2: Read the following pages in priority order:
- Homepage
- About / Our Story
- Services or Products
- Case Studies or Customers
- Blog (scan headlines only, read 1-2 recent posts)
- Careers (signals culture and growth stage)

Step 3: Extract and structure the following:

### Value Proposition
What do they claim to do and for whom? What's the core promise?

### Target Audience
Who are they clearly selling to? Any secondary audiences? What pain points do 
they address explicitly?

### Brand Voice
How do they write? Formal or casual? Technical or accessible? What words and 
phrases do they repeat? What's the emotional tone?

### Competitive Positioning
How do they differentiate? What do they claim competitors can't do? Any explicit 
or implicit comparisons?

### Proof Points
Customer logos, case studies, stats, testimonials — what social proof do they use?

### Signals & Observations
Anything notable: gaps in messaging, opportunities, contradictions between what 
they say and what they show, tech stack clues, growth indicators.

Narrative vs Operational Signal
  • Does their positioning match the real complexity of what they sell?
  • Are they selling simplicity on top of a structurally complex product?
  • Do their public claims match what customers report?

## Incentive Structure
- How does this company make money?
- Where are margin pressures likely?
- What behaviors are incentivized internally?
- What might they optimize for at the expense of something else?

## Organizational Maturity Signals
- Operator-led vs marketing-led?
- Product depth vs brand polish?
- Systems-forward or personality-forward?
- Specialist niche or expansionist generalist?

## Strategic Implications
If I were:
- A competitor → what would I attack?
- A partner → where is alignment?
- An internal operator → what would I double down on?
- A marketer → what would I build next?

End with:
- 1 structural strength
- 1 structural risk
- 1 actionable opportunity

## Output Format
Save as structured markdown to: profiles/[company-name].md

Use this structure:
---
# [Company Name] Intel Profile
Date: [today's date]
URL: [url researched]

## Value Proposition
## Target Audience  
## Brand Voice
## Competitive Positioning
## Proof Points
## Signals & Observations
---

## Rules
- Be specific. Vague observations are useless.
- Quote their actual language where relevant — exact words matter for voice matching.
- If a page is behind a login or paywalled, note it and move on.
- Flag any messaging that feels inconsistent or off-brand.
- Do not editorialize excessively — capture what's there, then add 1-2 sharp 
  observations at the end.