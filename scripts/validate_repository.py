#!/usr/bin/env python3
"""Check local inline Markdown links and GitHub-style heading anchors.

Uses only Python's standard library and Git. This repository deliberately uses
inline links, not reference-link definitions or HTML links. Fenced code is not
treated as Markdown. Remote URLs, Mermaid rendering, and secrets are not checked.
"""

from collections import Counter
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'!?\[[^\]\n]*\]\((<[^>\n]+>|[^\s)]+)(?:\s+"[^"\n]*")?\)')
HEADING = re.compile(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")


def prose_lines(content):
    """Preserve source line numbers, omitting fenced code blocks."""
    fence_char = None
    fence_length = 0
    for number, line in enumerate(content.splitlines(), 1):
        marker = FENCE.match(line)
        if marker:
            token = marker.group(1)
            if fence_char is None:
                fence_char, fence_length = token[0], len(token)
                continue
            if token[0] == fence_char and len(token) >= fence_length:
                fence_char = None
                continue
        if fence_char is None:
            yield number, line


def anchors(content):
    counts = Counter()
    found = set()
    for _, line in prose_lines(content):
        match = HEADING.match(line)
        if not match:
            continue
        title = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", match.group(1))
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        suffix = f"-{counts[slug]}" if counts[slug] else ""
        found.add(slug + suffix)
        counts[slug] += 1
    return found


def main():
    try:
        listing = subprocess.run(
            ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: run inside an initialized Git repository: {exc}", file=sys.stderr)
        return 2

    paths = sorted({ROOT / name for name in listing.split("\0") if name.endswith(".md")})
    if not paths:
        print("ERROR: no Markdown files found", file=sys.stderr)
        return 2
    documents = {path: path.read_text(encoding="utf-8") for path in paths}
    heading_index = {path: anchors(content) for path, content in documents.items()}
    checked = 0
    errors = []

    for source, content in documents.items():
        for number, line in prose_lines(content):
            for match in LINK.finditer(line):
                destination = match.group(1).removeprefix("<").removesuffix(">")
                parts = urlsplit(destination)
                if parts.scheme or parts.netloc:
                    continue
                checked += 1
                path_text = unquote(parts.path)
                target = (source.parent / path_text).resolve() if path_text else source
                label = f"{source.relative_to(ROOT)}:{number}: {destination}"
                if path_text.startswith("/") or not target.is_relative_to(ROOT):
                    errors.append(f"{label} — local link leaves repository")
                elif not target.exists():
                    errors.append(f"{label} — target does not exist")
                elif parts.fragment:
                    document = target / "README.md" if target.is_dir() else target
                    fragment = unquote(parts.fragment)
                    if document not in heading_index or fragment not in heading_index[document]:
                        errors.append(f"{label} — heading anchor does not exist")

    if errors:
        print("FAIL: internal Markdown links")
        print("\n".join(errors))
        return 1
    print(f"PASS: {checked} internal links across {len(paths)} Markdown files (paths and heading anchors).")
    print("Scope: inline Markdown links; remote URLs, Mermaid rendering, and secrets are not checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
