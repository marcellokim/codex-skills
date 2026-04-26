#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Install a skill from this repository into a local Codex skills directory.

Usage:
  scripts/install.sh [skill-name] [--target DIR] [--dry-run]

Defaults:
  skill-name: portfolio-polisher
  target:     ~/.codex/skills

Examples:
  scripts/install.sh
  scripts/install.sh portfolio-polisher --target ~/.agents/skills
  scripts/install.sh --dry-run
USAGE
}

skill="portfolio-polisher"
target="${HOME}/.codex/skills"
dry_run=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help)
      usage
      exit 0
      ;;
    --target)
      [[ $# -ge 2 ]] || { echo "error: --target requires a directory" >&2; exit 2; }
      target="$2"
      shift 2
      ;;
    --dry-run)
      dry_run=1
      shift
      ;;
    --*)
      echo "error: unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
    *)
      skill="$1"
      shift
      ;;
  esac
done

if [[ ! "${skill}" =~ ^[a-z0-9-]+$ ]]; then
  echo "error: skill name must use lowercase letters, numbers, and hyphens only" >&2
  exit 2
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_dir="${repo_root}/${skill}"
dest_dir="${target}/${skill}"

if [[ ! -f "${source_dir}/SKILL.md" ]]; then
  echo "error: skill not found: ${source_dir}/SKILL.md" >&2
  exit 1
fi

echo "Skill:  ${skill}"
echo "Source: ${source_dir}"
echo "Target: ${dest_dir}"

if [[ "${dry_run}" -eq 1 ]]; then
  echo "Dry run only; no files copied."
  exit 0
fi

mkdir -p "${target}"
rm -rf "${dest_dir}"
cp -R "${source_dir}" "${dest_dir}"

echo "Installed ${skill} to ${dest_dir}"
echo "Start a new Codex session or reload skills if your client supports it."
