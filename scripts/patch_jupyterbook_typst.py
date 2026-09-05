# scripts/patch_jupyterbook_typst.py
import jupyter_book
from pathlib import Path

target = Path(jupyter_book.__file__).parent / "dist" / "jupyter-book.cjs"
src = target.read_text(encoding="utf-8")

MARKER = 'grid(node3, state) {\n    const cols = node3.columns'
if MARKER in src:
    print("jupyter-book typst grid patch already applied, skipping")
    raise SystemExit(0)

ANCHOR = (
    "  table: tableHandler,\n"
    "  tableRow: tableRowHandler,\n"
    "  tableCell: tableCellHandler,\n"
    "  image(node3, state) {"
)
PATCHED = (
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
)

if ANCHOR not in src:
    raise SystemExit(
        "jupyter-book internals changed — anchor string not found, "
        "patch needs updating for this jupyter_book version"
    )

target.write_text(src.replace(ANCHOR, PATCHED), encoding="utf-8")
print(f"Patched {target}: added grid/grid-item typst handlers")