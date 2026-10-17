#!/usr/bin/env python3
"""Check that every **Next:** link in the guide resolves to an existing file.

A **Next:** entry starts at a line beginning with `**Next:**` and runs to the next blank
line. Both markdown links `[text](path.md)` and backticked paths (`path.md`) are checked,
relative to the file that contains them. Anchors (#...) are stripped. External links are skipped.

Usage: python3 scripts/check_next_links.py   (exit 1 if any link is broken)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
TICK_PATH = re.compile(r"`([^`\s]+\.md)`")


def next_blocks(text):
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].startswith("**Next:**"):
            start = i
            block = []
            while i < len(lines) and lines[i].strip():
                block.append(lines[i])
                i += 1
            yield start + 1, " ".join(block)
        else:
            i += 1


def main():
    checked = broken = 0
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        for lineno, block in next_blocks(md.read_text(encoding="utf-8")):
            targets = MD_LINK.findall(block) + TICK_PATH.findall(block)
            for t in targets:
                if re.match(r"[a-z]+://", t) or t.startswith("mailto:"):
                    continue
                path = t.split("#", 1)[0]
                if not path:
                    continue
                checked += 1
                if not (md.parent / path).resolve().is_file():
                    broken += 1
                    print(f"BROKEN {md.relative_to(ROOT)}:{lineno} -> {t}")
    print(f"{checked} Next link(s) checked, {broken} broken")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
