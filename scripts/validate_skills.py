#!/usr/bin/env python3
"""Validate the repository's Codex skill folders without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9-]+$")
REQUIRED_OPENAI_FIELDS = (
    "display_name:",
    "short_description:",
    "default_prompt:",
)


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter start")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("missing YAML frontmatter end")

    raw = text[4:end]
    if len(raw) > 1024:
        raise ValueError("frontmatter should stay under 1024 characters")

    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, text[end + 5 :]


def validate_skill(skill_file: Path) -> list[str]:
    errors: list[str] = []
    rel = skill_file.relative_to(ROOT)

    try:
        fields, body = parse_frontmatter(skill_file)
    except ValueError as exc:
        return [f"{rel}: {exc}"]

    name = fields.get("name", "")
    description = fields.get("description", "")

    if not name:
        errors.append(f"{rel}: missing required 'name'")
    elif not NAME_RE.fullmatch(name):
        errors.append(f"{rel}: name must use lowercase letters, numbers, and hyphens only")

    if skill_file.parent.name != name:
        errors.append(f"{rel}: parent folder must match skill name '{name}'")

    if not description:
        errors.append(f"{rel}: missing required 'description'")
    elif not description.startswith("Use when"):
        errors.append(f"{rel}: description should start with 'Use when'")

    if len(description) > 500:
        errors.append(f"{rel}: description should stay under 500 characters")

    if body.count("```") % 2:
        errors.append(f"{rel}: unbalanced markdown code fences")

    openai_yaml = skill_file.parent / "agents" / "openai.yaml"
    if openai_yaml.exists():
        yaml_text = openai_yaml.read_text(encoding="utf-8")
        for field in REQUIRED_OPENAI_FIELDS:
            if field not in yaml_text:
                errors.append(f"{openai_yaml.relative_to(ROOT)}: missing interface.{field[:-1]}")
        if f"${name}" not in yaml_text:
            errors.append(f"{openai_yaml.relative_to(ROOT)}: default_prompt should mention ${name}")

    return errors


def main() -> int:
    skill_files = sorted(
        p for p in ROOT.glob("*/SKILL.md") if not any(part.startswith(".") for part in p.parts)
    )
    if not skill_files:
        print("No skill folders found.", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for skill_file in skill_files:
        all_errors.extend(validate_skill(skill_file))

    if all_errors:
        print("Skill validation failed:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skill_files)} skill(s):")
    for skill_file in skill_files:
        print(f"- {skill_file.parent.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
