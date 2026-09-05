# scripts/render_mermaid.py
import platform
import subprocess
from pathlib import Path

npx_prefix = ["cmd", "/c", "npx"] if platform.system() == "Windows" else ["npx"]
config = Path(__file__).parent / "mermaid-config.json"

for mmd in Path("content").rglob("*.mmd"):
    svg = mmd.with_suffix(".svg")
    subprocess.run(
        [*npx_prefix, "--yes", "@mermaid-js/mermaid-cli",
         "-i", str(mmd), "-o", str(svg), "-b", "transparent",
         "-c", str(config)],
        check=True,
    )
    print(f"rendered {svg}")