# scripts/patch_jupyterbook_typst.py
import jupyter_book
from pathlib import Path

target = Path(jupyter_book.__file__).parent / "dist" / "jupyter-book.cjs"
src = target.read_text(encoding="utf-8")

PATCHES = [
    {
        "name": "grid/grid-item typst handlers",
        "marker": 'grid(node3, state) {\n    const cols = node3.columns',
        "anchor": (
            "  table: tableHandler,\n"
            "  tableRow: tableRowHandler,\n"
            "  tableCell: tableCellHandler,\n"
            "  image(node3, state) {"
        ),
        "patched": (
            "  table: tableHandler,\n"
            "  tableRow: tableRowHandler,\n"
            "  tableCell: tableCellHandler,\n"
            "  grid(node3, state) {\n"
            "    const cols = node3.columns ?? [1];\n"
            "    const n = cols[cols.length - 1] || 1;\n"
            "    state.ensureNewLine();\n"
            "    state.write(`#grid(columns: ${n}, gutter: 1em,\n"
            "`);\n"
            "    state.renderChildren(node3);\n"
            "    state.write(\")\\n\\n\");\n"
            "  },\n"
            "  \"grid-item\"(node3, state) {\n"
            "    state.write(\"[\\n\");\n"
            "    state.renderChildren(node3);\n"
            "    state.write(\"\\n],\\n\");\n"
            "  },\n"
            "  image(node3, state) {"
        ),
    },
    {
        # tab-item headings rendered near-invisible: 9pt on a luma(250)
        # (near-white) fill. Bump size/weight/fill so it reads as a real
        # heading in print, not just body text with a faint background.
        "name": "tab-item heading size/contrast",
        "marker": 'luma(235))[#text(13pt, weight: "bold")[#heading]]',
        "anchor": (
            'title = block(width: 100%, inset: (x: 8pt, y: 4pt), '
            'fill: luma(250))[#text(9pt, weight: "bold")[#heading]]'
        ),
        "patched": (
            'title = block(width: 100%, inset: (x: 10pt, y: 6pt), '
            'fill: luma(235))[#text(13pt, weight: "bold")[#heading]]'
        ),
    },
]

applied = 0
for patch in PATCHES:
    if patch["marker"] in src:
        print(f"already applied, skipping: {patch['name']}")
        continue
    if patch["anchor"] not in src:
        raise SystemExit(
            f"jupyter-book internals changed for patch {patch['name']!r} — "
            "anchor string not found, patch needs updating for this "
            "jupyter_book version"
        )
    src = src.replace(patch["anchor"], patch["patched"])
    print(f"applied: {patch['name']}")
    applied += 1

if applied:
    target.write_text(src, encoding="utf-8")
    print(f"wrote {target} ({applied} patch(es) applied)")
else:
    print("nothing to do, jupyter-book.cjs already fully patched")