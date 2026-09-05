# scripts/render_mermaid.py
import platform
import subprocess
from pathlib import Path

npx_prefix = ["cmd", "/c", "npx"] if platform.system() == "Windows" else ["npx"]
script_dir = Path(__file__).parent
mermaid_config = script_dir / "mermaid-config.json"

extra_args = ["-c", str(mermaid_config)]
if platform.system() != "Windows":
    # Sandboxed CI runners (and some locked-down Linux desktops) need this;
    # your Windows/Chrome puppeteer-config.json handles the local case separately.
    puppeteer_config = script_dir / "mermaid-config-ci.json"
    extra_args += ["-p", str(puppeteer_config)]

for mmd in Path("content").rglob("*.mmd"):
    svg = mmd.with_suffix(".svg")
    subprocess.run(
        [*npx_prefix, "--yes", "@mermaid-js/mermaid-cli",
         "-i", str(mmd), "-o", str(svg), "-b", "transparent",
         *extra_args],
        check=True,
    )
    print(f"rendered {svg}")