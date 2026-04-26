---
name: portfolio-polisher
description: Use when a user asks to make a GitHub repository portfolio-ready, submission-ready, recruiter-friendly, easier to run from README, or polished for project review, including README/setup/Docker/deployment-readiness requests.
---

# Portfolio Polisher

## Overview

Make the current repository portfolio-ready without breaking existing behavior. A reviewer should be able to understand the project, install it, configure it, run it, test/build it, and see what was actually verified.

Prioritize runability, accurate docs, security hygiene, and honest evidence over cosmetic polish.

## When to Use

Use for requests like:

- portfolio/submission/recruiter-ready repo polish
- README, setup, run, test, build, or deployment docs
- fresh-clone runability improvements
- environment variable documentation
- Docker/Docker Compose evaluation for easier local execution

Do not use for ordinary bug fixes, isolated features, algorithm problems, general code review, one-file wording edits, security-only audits, CI-only tasks, or broad refactors unrelated to portfolio readiness.

## Modes

| Mode | Trigger | Behavior |
| --- | --- | --- |
| Apply | default | Inspect, make safe edits, verify feasible commands, report evidence |
| Audit-only | "수정하지 말고", "진단만", "audit only" | Inspect and report only |
| Minimal | "최소 변경", "README 중심", "quick polish" | README, `.env.example`, `.gitignore`, run instructions only |
| Deployment | deployment explicitly requested | Add only confident docs/config; never deploy without explicit authorization |

## Non-Negotiables

- Do not stop at a plan when safe edits and verification are possible.
- Preserve existing behavior and architecture.
- Prefer small, reversible changes.
- Do not commit, push, publish, deploy, or use external accounts unless explicitly requested.
- Do not add dependencies unless they clearly improve runability or doc accuracy.
- Do not fake demo links, badges, screenshots, metrics, user counts, test results, or deployment status.
- Do not expose, print, copy, or commit secrets.
- Do not claim verification unless it was actually run or checked.
- Label inferred facts as inferred.
- Report failed or skipped verification honestly.

## Workflow

### 1. Reconnaissance

Inspect before editing. Check relevant files:

```text
README.md package.json pnpm-lock.yaml yarn.lock package-lock.json bun.lockb
pyproject.toml requirements.txt Pipfile poetry.lock uv.lock manage.py main.py app.py
pom.xml build.gradle gradlew mvnw go.mod Cargo.toml
Dockerfile docker-compose.yml compose.yml .env .env.example .gitignore
.github/workflows/ docs/
```

Determine project purpose, app type, stack, entry points, package manager, required services/env vars, install/run/test/build commands, deployment fit, docs accuracy, and obvious secret risks.

Run `git status --short` in git repos and do not overwrite unrelated user changes.

### 2. Scope

Choose the smallest useful change set:

1. Accurate project explanation
2. Fresh-clone run path
3. Environment variable docs
4. Test/build verification
5. Docker/local service setup only if useful
6. Realistic deployment docs
7. Repo hygiene

Do not add Docker, CI, Makefile, or deployment config just to look professional.

### 3. README Contract

Create or improve `README.md` with relevant sections only:

- project name and one-sentence description
- overview: what it does, who it is for, why it exists
- key features
- tech stack
- architecture or folder structure when useful
- prerequisites, install, environment variables, run locally
- test/build commands
- Docker only if present or added
- deployment recommendation/manual steps
- real screenshots only; otherwise say none are included yet
- implementation notes, troubleshooting, roadmap, license

README rules:

- Do not invent features or production readiness.
- Do not add fake badges, screenshots, demo URLs, scale, security, performance, or business claims.
- Keep the first screen strong: name, one-liner, overview, features, stack, run command.
- Use English unless the repo/user clearly prefers another language.

Useful one-liners:

```text
[Project] is a [type of app] that helps [target user] do [job] by [mechanism].
[Project] is a [stack] application for [problem], featuring [real strengths].
[Project] demonstrates [technical capability] through a working [domain] application.
```

## Environment Variables

Find env vars from source, config, tests, Docker, deployment files, and docs. Create/update `.env.example` with safe placeholders only.

Rules:

- Never copy real secrets.
- Include identifiable required variables; mark optional variables clearly.
- Ensure `.env` and local secret files are ignored.
- If a tracked secret is detected, do not reveal it; recommend rotation.
- Do not rewrite history unless explicitly requested.

Example:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/app_db
JWT_SECRET=replace-with-a-long-random-string
API_KEY=replace-with-your-api-key
```

## Repo Hygiene

Review `.gitignore`. Common entries:

```gitignore
node_modules/
.venv/
venv/
__pycache__/
.env
.env.*
!.env.example
dist/
build/
.next/
out/
target/
*.log
logs/
.DS_Store
```

Do not ignore lockfiles, source, migrations, config examples, needed fixtures, or docs.

## Run Setup

Prefer the simplest accurate path:

1. existing project-native command
2. existing package script
3. thin Makefile wrapper
4. Dockerfile
5. Docker Compose
6. deployment-specific setup

Use the package manager indicated by lockfiles. Prefer existing scripts. Add minimal scripts only when obvious and safe.

Common commands:

```bash
pnpm install && pnpm dev && pnpm test && pnpm build
npm install && npm run dev && npm test && npm run build
yarn install && yarn dev && yarn test && yarn build
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
python -m pytest
./gradlew test && ./gradlew bootRun
./mvnw test && ./mvnw spring-boot:run
```

Document database migrations only if the project actually needs them.

## Docker

Add Docker only when it materially improves runability: backend services, database/cache/queue, multi-service setup, fragile local setup, or useful consistent runtime.

Do not add Docker when the project is simpler without it, required services are unclear, ports/runtime are speculative, it cannot be reasonably validated, or it adds friction.

If adding Docker: never bake secrets into images, use lockfiles, add `.dockerignore`, expose correct ports, document dev vs production mode, and verify with `docker build`, `docker compose config`, or `docker compose up` when feasible.

## Deployment

Recommend the simplest realistic target:

| Type | Default |
| --- | --- |
| Static site | GitHub Pages, Netlify, Vercel |
| React/Vite SPA | Vercel, Netlify |
| Next.js | Vercel |
| Node/Python backend | Render, Railway, Fly.io |
| Full-stack with DB | Docker Compose locally; hosted only if requested |
| CLI/library | install and usage docs |
| Mobile | emulator/device setup and screenshots |

Do not deploy, use credentials, or create fake deployment status. Document required env vars and manual dashboard steps.

## Verification

Run feasible verification after edits. Prefer existing commands.

Priority: install, lint, test, build, local smoke check, Docker build, Compose config/startup.

Examples:

```bash
npm test
npm run build
pnpm test
pytest
python -m pytest
./gradlew test
./mvnw test
docker build .
docker compose config
```

For local servers, use timeout/background process, check expected localhost URL with `curl` or browser tooling, stop the process, and do not leave services running.

Report each command as success, failure, or skipped with reason. Never imply skipped or failed verification passed.

## Security Hygiene

Search for obvious secret risks: `.env`, API keys, tokens, private keys, passwords, database URLs with credentials, OAuth/JWT/cloud secrets.

Never print values. Mask references. Keep `.env.example` safe. Recommend rotation for exposed credentials.

## CI

Add GitHub Actions only when stable commands exist and do not require unavailable secrets. Good CI runs install, lint, test, and build when available.

## Final Report

After Apply Mode:

```markdown
**What Changed**
- Main improvement summary.

**Files Changed**
- `path` — reason

**How To Run**
```bash
primary command
```

**Deployment**
- Recommended target:
- Required manual steps:
- Required environment variables:

**Verification**
- `command` — success / failure / skipped

**Remaining Issues**
- Known limitation or manual check

**Portfolio Review Notes**
- Strongest point
- Weakest remaining point
- Highest-leverage next improvement
```

Audit-only mode should report project overview, current run method, problems by severity, recommended fixes, deployment recommendation, risk level, and next actions.

## Quality Bar

Success requires accurate README, identifiable run command, documented required env vars, setup matching actual files, no exposed secrets, honest verification, non-speculative Docker/deployment additions, and a final report covering changes plus remaining work.

## Common Mistakes

Avoid: ending with only a plan, broad rewrites, fake badges/screenshots/demo links/claims, claiming unrun tests passed, brittle Docker, ignoring lockfiles, removing lockfiles without reason, committing `.env`, printing secrets, hiding failures, or implying deployment is complete when manual external steps remain.
