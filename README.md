# Codex Skills

[![Validate Skills](https://github.com/marcellokim/codex-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/marcellokim/codex-skills/actions/workflows/validate.yml)

Reusable Codex skills for making personal repositories easier to review, run, and reuse.

This repository currently publishes `portfolio-polisher`, a Codex skill for turning rough GitHub projects into portfolio-ready repositories with accurate README content, setup instructions, environment-variable documentation, deployment notes, security hygiene, and honest verification reporting.

## Overview

Portfolio repositories often fail for practical reasons: the README is vague, setup steps are stale, required environment variables are undocumented, tests are not clearly runnable, or deployment claims are unverifiable.

`portfolio-polisher` gives Codex a focused workflow for improving those reviewer-facing gaps while avoiding risky behavior such as fake badges, invented screenshots, secret exposure, broad rewrites, or unverified success claims.

## Included Skills

| Skill | Purpose | Invocation |
| --- | --- | --- |
| `portfolio-polisher` | Prepare a GitHub repository for portfolio, recruiter, interview, or submission review. | `$portfolio-polisher ...` |

## Tech Stack

- Skill format: Codex `SKILL.md` folders with YAML frontmatter
- Metadata: optional `agents/openai.yaml`
- Validation: dependency-free Python 3 script
- CI: GitHub Actions validation workflow
- Runtime services: none

## Repository Structure

```text
.
├── .github/
│   └── workflows/
│       └── validate.yml
├── README.md
├── portfolio-polisher/
│   ├── SKILL.md
│   └── agents/
│       └── openai.yaml
└── scripts/
    └── validate_skills.py
```

## Getting Started

### Prerequisites

- Codex CLI, Codex IDE extension, or Codex App for using the skill
- Python 3.10+ for running the local validator
- Git, if cloning this repository

### Install

Clone this repository and copy the skill folder into your Codex skills directory:

```bash
git clone https://github.com/marcellokim/codex-skills.git
mkdir -p ~/.codex/skills
cp -R codex-skills/portfolio-polisher ~/.codex/skills/
```

Then start a new Codex session, or reload skills if your client supports skill reloads.

For older Codex/agent setups that still scan `~/.agents/skills`, copy the same folder there instead:

```bash
mkdir -p ~/.agents/skills
cp -R codex-skills/portfolio-polisher ~/.agents/skills/
```

### Environment Variables

No environment variables are required for this repository or for `portfolio-polisher` itself.

If a future skill needs configuration, document safe placeholders in that skill's README or `.env.example`; do not commit real credentials.

### Usage

Apply mode:

```text
$portfolio-polisher 이 레포를 포트폴리오 제출용으로 정리해줘. README, 실행 방법, .env.example, Docker 가능성, 배포 방법, 검증까지 봐줘.
```

Audit-only mode:

```text
$portfolio-polisher 수정하지 말고 진단만 해줘. README, 실행 가능성, 환경변수, Docker 필요성, 배포 가능성, 보안 위험, 포트폴리오 임팩트를 기준으로 봐줘.
```

Minimal mode:

```text
$portfolio-polisher 최소 변경으로 README, 실행 방법, .env.example 중심으로만 정리해줘.
```

## Skill Behavior Summary

`portfolio-polisher` is intentionally conservative:

- improves README/setup/deployment documentation before cosmetic polish
- documents environment variables with safe placeholders only
- checks for obvious secret risks without printing secret values
- adds Docker only when it improves runability and can be reasonably verified
- reports every verification command as success, failure, or skipped
- does not commit, push, publish, deploy, or use external accounts unless explicitly requested

The skill metadata disables implicit invocation by default:

```yaml
policy:
  allow_implicit_invocation: false
```

Use `$portfolio-polisher` explicitly when you want the workflow.

## Testing and Verification

No package installation is required. Validate the skill files with:

```bash
python3 scripts/validate_skills.py
```

The validator checks:

- each top-level skill folder has a `SKILL.md`
- YAML frontmatter includes `name` and `description`
- frontmatter stays under 1024 characters
- skill names use lowercase letters, numbers, and hyphens
- skill folders match skill names
- descriptions start with `Use when`
- markdown code fences are balanced
- `agents/openai.yaml` default prompts mention the skill name when metadata is present

GitHub Actions runs the same validator on pushes and pull requests.

## Docker

Docker is not needed for this repository. The only executable path is the Python validator, which runs directly with the system Python interpreter.

## Deployment

There is no application service to deploy. The repository is published on GitHub for clone-and-copy installation:

```text
https://github.com/marcellokim/codex-skills
```

## Security Notes

Do not commit private project details, real API keys, tokens, passwords, `.env` files, or private verification logs to this repository.

The checked-in examples use placeholder values only. If a real credential is ever committed, rotate it immediately and remove it from history only with explicit intent.

## Extending the Skill Library

Add new skills as top-level folders:

```text
new-skill-name/
├── SKILL.md
└── agents/
    └── openai.yaml
```

Before publishing changes, run:

```bash
python3 scripts/validate_skills.py
```

Keep skills focused on one reusable workflow. Prefer instruction-only skills first; add `scripts/`, `references/`, or `assets/` only when they materially improve reliability or token efficiency.

## Roadmap

- Add more reusable Codex skills only after testing them on real prompts.
- Add optional reference files when `portfolio-polisher` needs stack-specific deployment guidance.
- Expand `scripts/validate_skills.py` only for checks that catch real authoring mistakes.

## License

MIT License. See [LICENSE](LICENSE).
