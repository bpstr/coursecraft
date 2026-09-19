#!/usr/bin/env python3
"""Check package integrity without running a model or calling an external API."""

import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    sys.exit("Missing development dependency: run python -m pip install -r requirements-dev.txt")


def local_path(base: Path, target: str, boundary: Path) -> Path:
    """Resolve a relative path, including symlinks, without leaving its boundary."""
    path = Path(target)
    resolved = (base / path).resolve()
    if path.is_absolute() or not resolved.is_relative_to(boundary.resolve()):
        raise ValueError(f"path escapes {boundary.name}/: {target}")
    return resolved


def references(text: str):
    """Read ordinary links and explicit supporting-file paths outside code fences."""
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence:
            continue
        targets = re.findall(r"`((?:references|assets|scripts|agents)/[^`\s]+)`", line)
        line = re.sub(r"(`+).*?\1", "", line)
        targets += re.findall(r"\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)", line)
        targets += re.findall(r"^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)", line)
        for target in set(targets):
            yield number, target.strip("<>")


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []

    def error(path, message):
        errors.append(f"{path.relative_to(root)}: {message}")

    def read(path, boundary=root):
        local_path(boundary, str(path.relative_to(boundary)), boundary)
        return path.read_text(encoding="utf-8")

    def mapping(path, loader, boundary=root):
        try:
            value = loader(read(path, boundary))
            if not isinstance(value, dict):
                raise ValueError("expected a metadata object")
            return value
        except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
            error(path, str(exc))
            return {}

    def required_text(metadata, field, path):
        value = metadata.get(field)
        if not isinstance(value, str) or not value.strip():
            error(path, f"{field!r} must be a nonempty string")
            return None
        return value

    manifests = {}
    for host in ("codex", "claude"):
        path = root / f".{host}-plugin/plugin.json"
        data = mapping(path, json.loads)
        manifests[host] = data
        for field in ("name", "version", "description"):
            required_text(data, field, path)
    for field in ("name", "version"):
        if manifests["codex"].get(field) != manifests["claude"].get(field):
            errors.append(f"Plugin manifests must agree on {field!r}")

    skill_roots = set()
    for host, data in manifests.items():
        path = root / f".{host}-plugin/plugin.json"
        declared = data.get("skills", "./skills/" if host == "claude" else None)
        declared = [declared] if isinstance(declared, str) else declared
        if not isinstance(declared, list) or not declared:
            error(path, "'skills' must specify a relative skill directory")
            continue
        for target in declared:
            if not isinstance(target, str) or not target.strip():
                error(path, "each skills path must be a nonempty string")
                continue
            try:
                directory = local_path(root, target, root)
                if not directory.is_dir():
                    raise ValueError(f"skill directory does not exist: {target}")
                skill_roots.add(directory)
            except (OSError, ValueError) as exc:
                error(path, str(exc))

    skill_files = set()
    for directory in sorted(skill_roots):
        found = set(directory.rglob("SKILL.md"))
        if not found:
            error(directory, "no SKILL.md files discovered")
        skill_files.update(found)
    for skill_file in sorted(skill_files):
        skill = skill_file.parent
        try:
            text = read(skill_file, skill)
            match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.DOTALL)
            if not match:
                raise ValueError("SKILL.md must begin with YAML frontmatter delimited by ---")
            metadata = yaml.safe_load(match.group(1))
            if not isinstance(metadata, dict):
                raise ValueError("frontmatter must be a YAML mapping")
            for field in ("name", "description"):
                required_text(metadata, field, skill_file)
        except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
            error(skill_file, str(exc))
        mapping(skill / "agents/openai.yaml", yaml.safe_load, skill)
        for document in sorted(skill.rglob("*.md")):
            try:
                content = read(document, skill)
                for number, target in references(content):
                    if "{{" in target and document.is_relative_to(skill / "assets"):
                        continue
                    url = urlsplit(target)
                    if url.scheme or url.netloc or not url.path:
                        continue
                    try:
                        destination = local_path(document.parent, unquote(url.path), skill)
                        if not destination.exists():
                            raise ValueError(f"missing referenced file: {target}")
                    except (OSError, ValueError) as exc:
                        error(document, f"line {number}: {exc}")
            except (OSError, UnicodeError, ValueError) as exc:
                error(document, str(exc))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    errors = validate(parser.parse_args().root)
    if errors:
        print("Package validation failed:\n" + "\n".join(f"- {item}" for item in errors), file=sys.stderr)
        return 1
    print("Package integrity checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
