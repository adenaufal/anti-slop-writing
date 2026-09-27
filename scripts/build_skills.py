#!/usr/bin/env python3
"""Validate and package the English and Indonesian anti-slop writing skills."""

from __future__ import annotations

import argparse
import ast
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
RELEASE_VERSION = "v4.1"
LANGUAGES = (("english", "en"), ("indonesian", "id"))
ADAPTERS = ("AGENTS.md", "GEMINI.md", "system-prompt.md")


class ReleaseError(Exception):
    """A concise, user-correctable release validation error."""


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise ReleaseError(f"Cannot read {path.relative_to(ROOT)}: {exc}") from exc


def split_frontmatter(path: Path) -> tuple[str, str]:
    content = read_text(path)
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)(.*)\Z", content, re.S)
    if not match:
        raise ReleaseError(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
    metadata, body = match.groups()
    for key in ("name", "description"):
        field = re.search(rf"^{key}:\s*(\S(?:.*\S)?)\s*$", metadata, re.M)
        if not field:
            raise ReleaseError(f"{path.relative_to(ROOT)}: frontmatter needs a non-empty {key}")
    return content, body


def body_version(path: Path, body: str) -> str:
    versions = set(re.findall(r"(?:\bv|\bvers(?:i|ion)\s+)(\d+\.\d+)\b", body, re.I))
    current = {version for version in versions if version != "4.0"}
    if current != {RELEASE_VERSION[1:]}:
        found = ", ".join(f"v{x}" for x in sorted(versions)) or "none"
        raise ReleaseError(
            f"{path.relative_to(ROOT)}: expected current body version {RELEASE_VERSION}; found {found}"
        )
    return RELEASE_VERSION


def markdown_links(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for raw in re.findall(r"(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)", text):
        target = raw.strip().split(maxsplit=1)[0].strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith("//"):
            continue
        filename = unquote(parsed.path)
        if not filename:
            continue
        resolved = (path.parent / filename).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken local link {target}")
    return errors


def validate_sources() -> dict[tuple[str, bool], tuple[str, list[tuple[Path, str]]]]:
    errors: list[str] = []
    bundles: dict[tuple[str, bool], tuple[str, list[tuple[Path, str]]]] = {}

    for language, short in LANGUAGES:
        folder = ROOT / language
        full_path = folder / "SKILL.md"
        lite_path = folder / "SKILL-lite.md"
        bodies: dict[Path, str] = {}
        for path in (full_path, lite_path):
            try:
                _, body = split_frontmatter(path)
                bodies[path] = body
                body_version(path, body)
            except ReleaseError as exc:
                errors.append(str(exc))

        if full_path in bodies:
            for adapter in ADAPTERS:
                path = folder / adapter
                try:
                    if read_text(path) != bodies[full_path]:
                        errors.append(f"{path.relative_to(ROOT)}: must exactly match SKILL.md body after YAML")
                except ReleaseError as exc:
                    errors.append(str(exc))

        references = sorted((folder / "references").glob("*.md"))
        for lite, skill_path in ((False, full_path), (True, lite_path)):
            if skill_path not in bodies:
                continue
            try:
                content, _ = split_frontmatter(skill_path)
                frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---", content, re.S)
                name_match = re.search(r"^name:\s*(\S(?:.*\S)?)\s*$", frontmatter.group(1), re.M) if frontmatter else None
                if not name_match:
                    continue
                name = name_match.group(1).strip().strip("'\"")
                entries: list[tuple[Path, str]] = [(skill_path, "SKILL.md"), (folder / "LICENSE", "LICENSE")]
                if not lite:
                    entries.extend((folder / filename, filename) for filename in ADAPTERS)
                entries.extend((ref, f"references/{ref.name}") for ref in references)
                for source, _ in entries:
                    if not source.is_file():
                        errors.append(f"Missing archive source: {source.relative_to(ROOT)}")
                bundles[(language, lite)] = (name, entries)
            except (OSError, IndexError) as exc:
                errors.append(f"{skill_path.relative_to(ROOT)}: cannot determine archive name: {exc}")

    maintained_markdown = list(ROOT.glob("*.md"))
    for directory in (ROOT / "english", ROOT / "indonesian", ROOT / "evaluations"):
        if directory.is_dir():
            maintained_markdown.extend(directory.rglob("*.md"))
    for path in maintained_markdown:
        try:
            errors.extend(markdown_links(path, read_text(path)))
        except ReleaseError as exc:
            errors.append(str(exc))

    install_path = ROOT / "INSTALL.md"
    try:
        install = read_text(install_path)
        examples = re.findall(r"```python\s*\n(.*?)\n```", install, re.S)
        for index, source in enumerate(examples, 1):
            try:
                ast.parse(source, filename=f"INSTALL-example-{index}")
            except SyntaxError as exc:
                errors.append(f"INSTALL.md: Python example {index} is invalid: {exc}")
    except ReleaseError as exc:
        errors.append(str(exc))

    if errors:
        shown = errors[:20]
        if len(errors) > len(shown):
            shown.append(f"... and {len(errors) - len(shown)} more validation error(s)")
        raise ReleaseError("\n".join(shown))
    return bundles


def payload_for(bundle: tuple[str, list[tuple[Path, str]]]) -> dict[str, bytes]:
    prefix, entries = bundle
    return {f"{prefix}/{target}": source.read_bytes() for source, target in entries}


def check_archive(path: Path, expected: dict[str, bytes]) -> None:
    if not path.is_file():
        raise ReleaseError(f"Missing release artifact: {path.name}")
    try:
        with zipfile.ZipFile(path) as archive:
            corrupt = archive.testzip()
            if corrupt is not None:
                raise ReleaseError(f"Corrupt ZIP member in {path.name}: {corrupt}")
            names = archive.namelist()
            if len(names) != len(set(names)) or set(names) != set(expected):
                raise ReleaseError(f"{path.name}: entries differ from current source")
            for name, data in expected.items():
                if archive.read(name) != data:
                    raise ReleaseError(f"{path.name}: {name} differs from current source")
    except (OSError, zipfile.BadZipFile) as exc:
        raise ReleaseError(f"Cannot verify {path.name}: {exc}") from exc


def build_archive(path: Path, expected: dict[str, bytes]) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in expected.items():
            archive.writestr(name, data)
    check_archive(path, expected)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and build the four portable .skill releases.")
    parser.add_argument(
        "--check", action="store_true",
        help="validate existing artifacts against current source without writing files",
    )
    args = parser.parse_args()
    try:
        bundles = validate_sources()
        for (language, lite), bundle in bundles.items():
            _, short = next(item for item in LANGUAGES if item[0] == language)
            suffix = "-lite" if lite else ""
            path = ROOT / f"anti-slop-writing-{short}{suffix}.skill"
            expected = payload_for(bundle)
            if args.check:
                check_archive(path, expected)
            else:
                build_archive(path, expected)
            print(f"PASS {path.name}: {len(expected)} entries, exact source contents")
    except (ReleaseError, OSError, zipfile.BadZipFile) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
