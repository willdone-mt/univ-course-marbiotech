#!/usr/bin/env python3
"""Inject the per-page PDF export block into every content page.

MyST has no project-level way to say "give every page its own PDF" -- the
`exports` key only ever applies to the file it is written in. This script
writes that block into each page for you, idempotently, so it can run in CI
before the build and contributors never have to touch frontmatter.

Usage:
    python scripts/inject_page_exports.py           # write
    python scripts/inject_page_exports.py --check   # exit 1 if out of date
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

# Files that should get their own single-page PDF.
PATTERNS = ["**/*-course.md", "**/*-teach.ipynb"]

TEMPLATE = "https://github.com/myst-templates/plain_typst_book.git"

# Export id of the whole-book PDF, declared in config/_myst-downloads.yml.
BOOK_ID = "full-book-pdf"
BOOK_TITLE = "Unduh Buku Lengkap (PDF)"
PAGE_TITLE = "Unduh Halaman Ini (PDF)"


def blocks_for(path: Path) -> tuple[list, list]:
    """Return the (exports, downloads) blocks for one page."""
    page_id = f"{path.stem}-pdf"
    exports = [
        {
            "id": page_id,
            "format": "typst",
            "template": TEMPLATE,
            "show_ToC": False,
            "papersize": "a4",
        }
    ]
    downloads = [
        {"id": page_id, "title": PAGE_TITLE},
        {"id": BOOK_ID, "title": BOOK_TITLE},
    ]
    return exports, downloads


def split_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter, body). Body keeps its original leading newline."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm = yaml.safe_load(parts[1]) or {}
    if not isinstance(fm, dict):
        return {}, text
    return fm, parts[2]


def dump_frontmatter(fm: dict) -> str:
    body = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False)
    return f"---\n{body}---"


def update_markdown(path: Path, check: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(original)
    exports, downloads = blocks_for(path)
    if fm.get("exports") == exports and fm.get("downloads") == downloads:
        return False
    fm["exports"] = exports
    fm["downloads"] = downloads
    updated = dump_frontmatter(fm) + body
    if not check:
        path.write_text(updated, encoding="utf-8")
    return True


def update_notebook(path: Path, check: bool) -> bool:
    nb = json.loads(path.read_text(encoding="utf-8"))
    meta = nb.setdefault("metadata", {})
    exports, downloads = blocks_for(path)
    if meta.get("exports") == exports and meta.get("downloads") == downloads:
        return False
    meta["exports"] = exports
    meta["downloads"] = downloads
    if not check:
        path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="report without writing")
    args = parser.parse_args()

    changed: list[Path] = []
    for pattern in PATTERNS:
        for path in sorted(CONTENT.glob(pattern)):
            handler = update_notebook if path.suffix == ".ipynb" else update_markdown
            if handler(path, args.check):
                changed.append(path)

    for path in changed:
        print(f"{'stale' if args.check else 'updated'}: {path.relative_to(ROOT)}")

    if not changed:
        print("all pages already carry the export block")
        return 0
    return 1 if args.check else 0


if __name__ == "__main__":
    sys.exit(main())
