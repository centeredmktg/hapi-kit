# hapi-kit

A Claude Code plugin catalog: one plugin of 26 skills, plus pinned references to two public plugins, for an embedded B2B marketer: messaging, ABM, sales enablement, content QA, weekly review, developer checks, and a lightweight session worklog.

The 18 original skills are Danny Cox's prior inventions, listed on Schedule B of his employee agreement. Bringing them into company work grants the company a non-exclusive license to use them as incorporated (clause (c)). Ownership stays with Danny. Skills added to the kit later, and third-party skills included under their own license, are listed separately in `MANIFEST.md`.

## The boundary (read before adding anything)

| Belongs in this repo | Belongs in a company-owned repo |
|---|---|
| Generic method: skills that work for any B2B company | Anything company-specific: context, ICP, account lists, scoring weights, messaging, scripts against company systems |
| Changes made on personal equipment, on personal time | Any change made on company equipment, company accounts, or company time |

- **This repo flows one way.** Changes made inside company work stay in the company's repo, as a fork or copy. They never get merged back here.
- **No company data here, ever.** No customer names, metrics, roadmap, credentials or exports.
- **New skills need notice first.** Before using a skill that isn't in `MANIFEST.md` for company work, add it to the manifest and give the company written notice.

## Install

Install into a company workspace from a pinned tag, so what's in use matches what was disclosed:

```bash
git clone --branch v1.6.0 git@github.com:centeredmktg/hapi-kit.git ~/hapi-kit
claude plugin marketplace add ~/hapi-kit
claude plugin install hapi-kit@hapi-kit                        # all kit skills, user scope
claude plugin install superpowers@hapi-kit --scope project     # only in repos where you build
claude plugin install seo-suite@hapi-kit --scope project       # only in a site/SEO repo
```

## Public plugins (pulled from upstream)

`superpowers` and `seo-suite` aren't copied into this repo. The catalog points at each upstream GitHub repo, pinned to a commit that has been reviewed:

| Entry | Upstream | Pinned | Always-on cost |
|---|---|---|---|
| superpowers | github.com/obra/superpowers | v7.0.2 · 22f0b46 | ~2K tokens/session (session-start hook) plus skill list |
| seo-suite | github.com/AgriciDaniel/claude-seo (listed as seo-suite because names starting with "claude-" are reserved) | v2.4.2 · 4b99de2 | ~4.5K tokens/session |

To upgrade one: read the upstream diff since the pinned commit, then bump the `sha` in `.claude-plugin/marketplace.json` and tag a new version. Never point at a branch, because an unpinned upstream can change what runs on a company machine without anyone looking.

Known issue in superpowers 7.0.2: the brainstorming "visual companion" (an optional local mockup server) had two medium findings in security review, a token-file reuse and a predictable /tmp path. Decline the offer to open a browser tab, or review upstream for a fix before using it.

Then copy `workspace-template/` into the company-owned workspace repo and fill in `CLAUDE.md` and `context/company.md`. Copy `profile/about-danny.md` into that repo as `about-me.md`; the template CLAUDE.md imports it, so every session starts with it. The skills read `context/`, write to `outputs/`, and the session close writes to `worklog/`.

## Building infrastructure

Use superpowers at project scope in the company's build repos: `brainstorming` → `writing-plans` → `executing-plans`, with TDD and systematic debugging alongside.

## Token notes

- At rest, each skill costs only its description, about 2.2K tokens total for the 26 skills.
- When a skill runs, its body loads: about 500–1,400 words. `humanizer` loads its full 4K-word pattern catalog only for long documents.
- `/ok-i-love-you-goodbye` here is the lite version: one appended worklog entry and nothing else.
