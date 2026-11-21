---
name: setup-pre-commit
description: Use when a TypeScript/JavaScript repo has no pre-commit gate and needs one — "add pre-commit hooks", "block commits that fail typecheck", "set up husky", "stop broken commits", or when a repo with a test suite has shipped a commit that failed typecheck or tests. Installs Husky + lint-staged so typecheck and tests run before every commit.
---

# Setup Pre-Commit Gate

## Purpose

Put typecheck and tests in front of every commit, so "tests pass in review, broken on main" stops being possible from a local commit.

## Step 1 — Detect (don't ask)

- **Package manager**: `pnpm-lock.yaml` → pnpm, `yarn.lock` → yarn, `bun.lockb`/`bun.lock` → bun, else npm. Use it everywhere below.
- **Existing hooks**: `.husky/`, `lefthook.yml`, `.pre-commit-config.yaml`, or `git config core.hooksPath`. If one exists, extend it; don't replace it.
- **Scripts**: find the typecheck command (`typecheck`, `check`, `tsc`, or `astro check` / `svelte-check` for those stacks) and the test command (`test`). If no typecheck script exists, add `"typecheck": "tsc --noEmit"` only when a `tsconfig.json` is present.
- **Formatter**: does the repo already use Prettier or Biome (config file present, or listed in devDependencies)?
- **Suite runtime**: run the test command once and time it.

Report findings in two or three lines, then proceed.

## Step 2 — Install

```bash
<pm> add -D husky lint-staged     # npm: npm i -D husky lint-staged
npx husky init                    # creates .husky/ and "prepare": "husky"
```

## Step 3 — Write `.husky/pre-commit`

```
npx lint-staged
<pm> run typecheck
<pm> run test
```

Adapt:
- **Slow suite (> ~30s)**: don't put the full suite in front of every commit. People route around a slow hook with `--no-verify`, which is worse than no hook. Use the runner's changed-files mode instead (`vitest related --run` via lint-staged, or `jest --findRelatedTests`) and leave the full suite to CI. Say which you chose and why.
- **No test script**: omit the line and tell the user.

## Step 4 — `.lintstagedrc`

- **Repo already uses Prettier/Biome** → format staged files:
  ```json
  { "*": "prettier --ignore-unknown --write" }
  ```
- **Repo has no formatter** → do NOT add Prettier by default. First-time formatting rewrites every touched file and buries real diffs in noise. Use lint-staged only for the related-tests hook (or an existing linter), and offer Prettier as a separate, single "format everything" commit the user can approve.

## Step 5 — Verify

- [ ] `.husky/pre-commit` exists and is executable
- [ ] `package.json` has `"prepare": "husky"`
- [ ] `npx lint-staged` runs clean on an empty stage
- [ ] Make a deliberate type error in a scratch file, try to commit: the hook must block it. Revert.

Don't claim it works until the blocked-commit test is observed.

## Step 6 — Commit

On a feature branch (never main), commit `chore: add pre-commit gate (husky + lint-staged)`. The commit itself runs the new hook as a smoke test. Open a PR following the repo's conventions.

## Notes

- Worktrees share the repo's hooks via `core.hooksPath`; one setup covers every worktree.
- Husky v9+ needs no shebang in hook files.
- `--no-verify` exists. The hook is a guardrail for honest mistakes, not a security control. CI is still the real gate.
