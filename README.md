# hapi-kit

A Claude Code plugin with 20 skills (18 original, 2 vendored MIT) for an embedded B2B marketer: messaging, ABM, sales enablement, content QA, weekly review, and a lightweight session worklog.

The 18 originals are Danny Cox's prior inventions, listed on Schedule B of his employee agreement. Bringing them into company work grants the company a non-exclusive license to use them as incorporated (clause (c)). Ownership stays with Danny.

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
git clone --branch v1.2.0 git@github.com:centeredmktg/hapi-kit.git ~/hapi-kit
claude plugin marketplace add ~/hapi-kit   # or point a local marketplace at it
claude plugin install hapi-kit
```

Then copy `workspace-template/` into the company-owned workspace repo and fill in `CLAUDE.md` and `context/company.md`. Copy `profile/about-danny.md` into that repo as `about-me.md`; the template CLAUDE.md imports it, so every session starts with it. The skills read `context/`, write to `outputs/`, and the session close writes to `worklog/`.

## Building infrastructure

`brainstorming` → `writing-plans` covers design and planning. For execution (TDD, debugging, subagent-driven builds), install the public superpowers plugin at project scope in the company workspace: `claude plugin install superpowers@claude-plugins-official --scope project`. It's public open source, so it needs no disclosure. Its session-start hook adds roughly 2K tokens to every session, so turn it on only in repos where you build.

## Token notes

- At rest, each skill costs only its description, about 1.5K tokens total for 20 skills.
- When a skill runs, its body loads: about 500–1,400 words. `humanizer` loads its full 4K-word pattern catalog only for long documents.
- `/ok-i-love-you-goodbye` here is the lite version: one appended worklog entry and nothing else.
