#!/usr/bin/env python3
"""Scaffold a new ClankTeam business directory from the bundled templates.

Usage:
    python3 init_business.py <business-name> [--base-dir PATH]

Creates <base-dir>/<business-name>/ with business.yaml, memory/, approvals/,
and reports/, populated from templates/ next to this script. Refuses to
overwrite an existing business directory.
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = SCRIPT_DIR.parent / "templates"

FILES = {
    "business.yaml": "business.yaml.template",
    "memory/decisions.md": "decisions.md.template",
    "memory/learnings.md": "learnings.md.template",
    "approvals/pending.md": "pending.md.template",
    "approvals/approved.md": "approved.md.template",
    "approvals/rejected.md": "rejected.md.template",
}


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")
    if not slug:
        raise ValueError(f"'{name}' has no usable characters for a directory name")
    return slug


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("business_name", help="Human-readable business name")
    parser.add_argument(
        "--base-dir",
        default=".",
        help="Directory to create the business folder in (default: current directory)",
    )
    args = parser.parse_args()

    slug = slugify(args.business_name)
    base = Path(args.base_dir).resolve()
    business_dir = base / slug

    if business_dir.exists():
        print(f"Refusing to overwrite existing business directory: {business_dir}", file=sys.stderr)
        return 1

    today = datetime.date.today().isoformat()

    for rel_path, template_name in FILES.items():
        template_path = TEMPLATES_DIR / template_name
        if not template_path.exists():
            print(f"Missing template: {template_path}", file=sys.stderr)
            return 1
        content = template_path.read_text(encoding="utf-8")
        if rel_path == "business.yaml":
            content = content.replace('name: ""', f'name: "{args.business_name}"')
            content = content.replace('created: ""', f'created: "{today}"')
        dest = business_dir / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")

    (business_dir / "reports").mkdir(parents=True, exist_ok=True)
    (business_dir / "reports" / ".gitkeep").touch()

    print(f"Scaffolded '{args.business_name}' at {business_dir}")
    print("Next: fill in business.yaml (goals, audience, voice) before the first /clankteam run.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
