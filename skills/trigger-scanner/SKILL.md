---
name: trigger-scanner
description: >-
  Use before drafting outreach for a named prospect or company. Scans for active buying signals across 37 trigger categories — company growth, personnel changes, competitive signals, intent signals, and event signals. Surfaces the top firing triggers and produces prioritized outreach hooks with timing recommendation per trigger. Run after /intel, feeds /draft-cold-email.
---

# /trigger-scanner — Sales Trigger & Buying Signal Scanner

## Purpose

Timing is the difference between a reply and a delete. Most outreach fails
not because the offer is wrong but because it arrives when nothing has changed
— no reason to act, no urgency, no hook.

This scans a target company for active buying signals and surfaces the ones
worth building outreach around.

Output: top firing triggers + one outreach hook per trigger + timing recommendation.

---

## Trigger

Invoked with /trigger-scanner

The user provides:
- Target company name (required)
- Available intel about the company (optional — paste /intel output if run)
- Their offer or product category (optional — sharpens trigger relevance scoring)

If no intel is provided, ask: "Do you have any existing research on this
company? Paste it here, or I'll work from what's publicly accessible."

---

## The 37-Trigger Taxonomy

All 37 triggers are evaluated for each target. Grouped by signal type:

### Company Growth Signals
| Trigger | What it means |
|---|---|
| Employee Growth | Headcount expansion = new budget, scaling pains, new vendor needs |
| New Office / Expansion / Relocation | Growth phase = new operational needs |
| Fundraising | Investor influx = new budget, new priorities, urgency to deploy |
| New Product Launch | Operations shift = new tool and vendor needs |
| Major Customer Win | Growth mode = new capacity and infrastructure needs |
| Sales Increase/Decrease | Revenue change = spending capacity signal |
| Marketing Budget Change | Budget shift = vendor opportunity or churn signal |

### Personnel Signals
| Trigger | What it means |
|---|---|
| Job Changes / Role Changes | New role = new priorities, new budget authority |
| Contacts Who Joined/Left | New person in account = new buying opportunity |
| Management Change / Leadership | Strategy shift = new vendor relationships opening |
| Hiring / Job Listings | Hiring pattern reveals direction and pain points |
| Layoffs | Cost reduction mode = efficiency solution opportunity |

### Competitive & Market Signals
| Trigger | What it means |
|---|---|
| Dissatisfaction with Current Solution | Active unhappy = switching intent |
| Technology Usage / Stack | Tech adopted reveals priorities, pain points, budget |
| Merger & Acquisition / Partnerships | Consolidation = new buying cycles |
| Shift in Sales Channel Strategy | GTM shift = new tool needs |
| Customer Base Change | Customer change signals business trajectory |
| Customer Data | Supply chain and relationship dynamics |

### Intent & Engagement Signals
| Trigger | What it means |
|---|---|
| Account Engagement | Engagement activity = intent signal |
| Online Activity / Intent | Actively seeking solutions = high intent |
| Website Visitors | Visiting your site = highest-intent inbound signal |
| Keywords | Tracking branded/generic keywords for search intent |
| Product Usage | Usage patterns reveal high-potential accounts |
| Quarterly Performance | Tough quarter = urgency for efficiency solutions |

### Reputation & Review Signals
| Trigger | What it means |
|---|---|
| Increase in Positive/Negative Reviews | Recurring issues = buyer signal |
| Employee Reviews | Company culture and health signal |
| Product Reviews | Market sentiment and switching intent |
| Press Coverage | Company in spotlight = timely outreach window |
| News & Updates | Newsworthy activity = outreach hook |

### Event & Change Signals
| Trigger | What it means |
|---|---|
| Event Announcement | Organizing event = engagement signal |
| Major Industry Event | Industry shift = context for timely outreach |
| New Website / Major Redesign | Change signal = engagement opportunity |
| Branding | Repositioning or growth signal |
| Marketing Change | Promotional strategy shift = new vendor opportunities |
| Legal Matters / Legal Disputes | Compliance penalty = compliance solution opportunity |
| LinkedIn Publications | Content engagement = priority signal |

---

## Reply-Rate Priors (industry standard, 2026)

When multiple triggers fire, use these priors to break ties on which to lead with.
Higher prior = higher expected reply rate. Apply only to Hot/Warm-rated triggers
— a prior on a stale signal is meaningless.

| Tier | Reply rate | Trigger categories |
|---|---|---|
| **S** | 65–70% | Dissatisfaction with Current Solution · Job Changes (0–6 mo) · Online Activity / Intent (pain-articulating posts) · Quarterly Performance (tough quarter) |
| **A** | 55–65% | Hiring / Job Listings · Fundraising · Employee Growth · Management Change · Contacts Who Joined/Left · Major Customer Win |
| **B** | 45–55% | New Product Launch · Tech Stack Change · M&A / Partnerships · Marketing Change · Customer Base Change · New Office / Expansion |
| **C** | 35–45% | Competitor Engagement · LinkedIn Publications · News & Updates · Press Coverage · Industry Event · Account Engagement |
| **D** | <35% | Website Visitors (alone) · Keywords (alone) · Reputation / Reviews · Legal Matters · Branding · Marketing Budget Change |

**Stacking rule:** when 2+ triggers fire on the same account in the same window,
add their tier values (S=5, A=4, B=3, C=2, D=1) and lead with the highest sum.
A B-tier + D-tier stack (3+1=4) outranks a single A-tier (4), tie broken by
recency.

---

## Process

### Step 1 — Gather Intel

Review available company information against the 37-trigger taxonomy.

Sources to check (use what's available):
- News and press releases (funding, M&A, leadership changes, expansion)
- Job listings (hiring patterns, direction, pain points)
- LinkedIn (leadership changes, headcount growth, company posts)
- G2/Capterra reviews (satisfaction signals, competitor gaps)
- Website (recent redesign, new product pages, messaging shifts)
- Tech stack tools (BuiltWith, Wappalyzer for technology signals)

Present what was pulled and where it came from. Let the user confirm or
add context before scoring.

### Step 2 — Score Active Triggers

For each trigger with evidence, rate signal strength:
- **Hot** — clear, recent evidence (within 90 days). Outreach now.
- **Warm** — indirect evidence or older signal (90-180 days). Outreach soon.
- **Watch** — circumstantial or unconfirmed. Monitor.

Only surface Hot and Warm triggers in the output.

### Step 3 — Generate Outreach Hooks

For each Hot/Warm trigger, produce:
- One-line outreach hook that uses the trigger as the opening angle
- Timing recommendation (outreach now / within 2 weeks / monitor)
- What NOT to say (the obvious angle everyone else will use)

---

## Output Format

```
TRIGGER SCAN
Company: [name]
────────────────────────────────────────────────
ACTIVE TRIGGERS:

[Trigger Name] — [Hot / Warm]
Signal: [What was found and where]
Hook: "[One-line outreach opener using this trigger]"
Timing: [Now / Within 2 weeks / Monitor]
Avoid: [The obvious angle — what every other rep will send]

[repeat for each active trigger]

────────────────────────────────────────────────
PRIORITY ORDER:
1. [Highest-leverage trigger] — Tier [S/A/B/C/D] + recency + [stacking note if applicable]
2. [Second trigger]
3. [Third trigger]

RECOMMENDED FIRST TOUCH:
Lead with [trigger] because [one sentence reasoning].
Feed this to /draft-cold-email with the hook above as the opening angle.

────────────────────────────────────────────────
SIGNALS NOT FOUND:
[List trigger categories with no evidence — optional, keeps the scan honest]
```

---

## Rules

- Pull signal data first, show sources, confirm before scoring.
  If the user has better intel, incorporate it before finalizing.
- Only surface Hot and Warm triggers — Watch signals go in a footnote,
  not the main output.
- Each hook must use the trigger specifically. "I noticed you're growing"
  is not a hook. "You added 14 engineers in Q1" is.
- The "Avoid" line is mandatory. It prevents the lazy obvious angle.
- Priority order is required. Don't make the user guess which trigger to use.
- Composes with /intel (run first) and feeds /draft-cold-email (run after).
- Use the reply-rate priors only for prioritization, not for excluding triggers.
  A D-tier firing trigger still beats a non-firing A-tier. Recency + firing
  status always outrank prior alone.
