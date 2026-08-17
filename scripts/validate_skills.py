#!/usr/bin/env python3
"""Validate the repository's Agent Skill structure without third-party packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    try:
        block, _body = text[4:].split("\n---\n", 1)
    except ValueError as error:
        raise ValueError("SKILL.md has an unclosed frontmatter block") from error

    values: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        if not separator:
            raise ValueError(f"invalid frontmatter line: {line!r}")
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def yaml_value(text: str, key: str) -> str | None:
    match = re.search(rf"^\s*{re.escape(key)}:\s*[\"']?(.*?)[\"']?\s*$", text, re.MULTILINE)
    return match.group(1) if match else None


def validate_skill(directory: Path) -> list[str]:
    errors: list[str] = []
    name = directory.name
    skill_file = directory / "SKILL.md"
    agent_file = directory / "agents" / "openai.yaml"

    if not NAME_PATTERN.fullmatch(name):
        errors.append("directory name must use lowercase kebab-case")
    if not skill_file.is_file():
        errors.append("missing SKILL.md")
        return errors
    if not agent_file.is_file():
        errors.append("missing agents/openai.yaml")

    try:
        metadata = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
    except ValueError as error:
        errors.append(str(error))
        return errors

    if set(metadata) != {"name", "description"}:
        errors.append("frontmatter must contain exactly name and description")
    if metadata.get("name") != name:
        errors.append("frontmatter name must match the skill directory")
    description = metadata.get("description", "")
    if not 40 <= len(description) <= 1024:
        errors.append("description must contain 40 to 1024 characters")

    if agent_file.is_file():
        agent_text = agent_file.read_text(encoding="utf-8")
        display_name = yaml_value(agent_text, "display_name")
        short_description = yaml_value(agent_text, "short_description")
        default_prompt = yaml_value(agent_text, "default_prompt")
        if not display_name:
            errors.append("openai.yaml needs interface.display_name")
        if not short_description or not 25 <= len(short_description) <= 64:
            errors.append("short_description must contain 25 to 64 characters")
        if not default_prompt or f"${name}" not in default_prompt:
            errors.append(f"default_prompt must explicitly invoke ${name}")

    return errors


def main() -> int:
    if not SKILLS.exists():
        print("No skills directory yet; repository foundation is valid.")
        return 0

    directories = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    failures = 0
    for directory in directories:
        errors = validate_skill(directory)
        if errors:
            failures += 1
            for error in errors:
                print(f"ERROR {directory.name}: {error}")
        else:
            print(f"OK    {directory.name}")

    if failures:
        print(f"\n{failures} skill(s) failed validation.")
        return 1
    print(f"\nValidated {len(directories)} skill(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
