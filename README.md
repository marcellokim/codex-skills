# Codex Skills

Reusable Codex skills for personal and portfolio/project workflows.

## Included Skills

### `portfolio-polisher`

Use this skill when preparing a GitHub repository for portfolio or submission review. It focuses on README quality, first-time setup, environment variables, local/Docker execution, deployment-readiness notes, security hygiene, and honest verification reporting.

## Install

Clone this repository and copy the skill folder into your Codex skills directory:

```bash
git clone https://github.com/marcellokim/codex-skills.git
mkdir -p ~/.codex/skills
cp -R codex-skills/portfolio-polisher ~/.codex/skills/
```

Then start a new Codex session or reload skills if your client supports it.

## Usage

```text
$portfolio-polisher 이 레포를 포트폴리오 제출용으로 정리해줘. README, 실행 방법, .env.example, Docker 가능성, 배포 방법, 검증까지 봐줘.
```

Audit-only example:

```text
$portfolio-polisher 수정하지 말고 진단만 해줘. README, 실행 가능성, 환경변수, Docker 필요성, 배포 가능성, 보안 위험, 포트폴리오 임팩트를 기준으로 봐줘.
```

## Safety Notes

The skill is configured for explicit invocation by default:

```yaml
policy:
  allow_implicit_invocation: false
```

This avoids accidental broad repo edits when the user only asked for a small README change.

Do not add private project details, real API keys, tokens, passwords, `.env` files, or private verification logs to this repository.
