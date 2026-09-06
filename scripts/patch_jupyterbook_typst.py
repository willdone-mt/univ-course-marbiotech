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
            'title = block(width: 100%, inset: (x: 8pt, y: 6pt), '
            'fill: luma(235))[#text(13pt, style: "italic")[#heading]]'
        ),
    },
    {
        # tablex was getting a bare integer for `columns`, meaning N
        # equal-width columns. Fine for a 2-column table with comparable
        # text on both sides; badly broken for e.g. a 5-column table
        # where one column (merged procedure text) is far longer than
        # the rest -- that column gets squeezed to one word per line and
        # the row balloons across pages. Size each column from its own
        # content instead of dividing the page evenly.
        "name": "table column widths sized to content",
        "marker": "function columnWidths(node3) {",
        "prelude_anchor": "var tableHandler = (node3, state) => {",
        "prelude": (
            "function cellTextLength(node3) {\n"
            "  if (!node3) return 0;\n"
            '  if (node3.type === "text" || node3.type === "inlineCode") {\n'
            '    return (node3.value || "").length;\n'
            "  }\n"
            "  return (node3.children || []).reduce((sum, c) => sum + cellTextLength(c), 0);\n"
            "}\n"
            "function columnWidths(node3) {\n"
            "  const rows = node3.children || [];\n"
            "  const maxLen = [];\n"
            "  rows.forEach((row) => {\n"
            "    (row.children || []).forEach((cell, i) => {\n"
            "      const len = cellTextLength(cell);\n"
            "      maxLen[i] = Math.max(maxLen[i] || 0, len);\n"
            "    });\n"
            "  });\n"
            "  const weights = maxLen.map((len) => Math.max(Math.sqrt(len || 1), 1.2));\n"
            '  return `(${weights.map((w) => `${w.toFixed(2)}fr`).join(", ")})`;\n'
            "}\n"
            "var tableHandler = (node3, state) => {"
        ),
        "anchor": (
            "  state.write(`${command}(columns: ${columns}, header-rows: ${countHeaderRows(node3)}, "
            "repeat-header: true, ..tableStyle, ..columnStyle,\n"
            "`);"
        ),
        "patched": (
            "  const widths = columns > 2 ? columnWidths(node3) : columns;\n"
            "  state.write(`${command}(columns: ${widths}, header-rows: ${countHeaderRows(node3)}, "
            "repeat-header: true, ..tableStyle, ..columnStyle,\n"
            "`);"
        ),
    },
]

applied = 0
for patch in PATCHES:
    if patch["marker"] in src:
        print(f"already applied, skipping: {patch['name']}")
        continue

    # A patch may need a one-time helper inserted ahead of its main anchor
    # (e.g. the column-width calculation used by the table patch below).
    if "prelude" in patch:
        if patch["prelude_anchor"] not in src:
            raise SystemExit(
                f"jupyter-book internals changed for patch {patch['name']!r} — "
                "prelude anchor not found, patch needs updating for this "
                "jupyter_book version"
            )
        src = src.replace(patch["prelude_anchor"], patch["prelude"])

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