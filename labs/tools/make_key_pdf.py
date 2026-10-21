"""Make a PDF of a lab's key with pandoc, beside it.

    python labs/tools/make_key_pdf.py labs/week-NN/lab-NN-key.ipynb [more keys ...]

Writes labs/week-NN/lab-NN-key.pdf: the key's text, code, and outputs,
figures included, for reading or printing without Jupyter. Needs pandoc and
lualatex (TeX Live), and the DejaVu and Noto fonts. Rerun it whenever the key
changes. See labs/AUTHORING.md.

Before pandoc reads the key, a copy of it is prepared for print. Each
collapsed Discuss box becomes a labeled list, because LaTeX drops HTML. An
output that has both an HTML table and plain text keeps the text. Terminal
color codes are removed.
"""
import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import nbformat

ANSI = re.compile(r"\x1b\[[0-9;]*m")
DETAILS = re.compile(r"<details>\s*<summary>(.*?)</summary>\s*(.*?)\s*</details>", re.DOTALL)

HEADER = r"""
\usepackage{fvextra}
\fvset{breaklines, breakanywhere}
\DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,breakanywhere,commandchars=\\\{\}}
\RecustomVerbatimEnvironment{verbatim}{Verbatim}{breaklines,breakanywhere}
\directlua{luaotfload.add_fallback("labfallback", {
  "file:NotoColorEmoji.ttf:mode=harf;", "file:NotoSansArabic-Regular.ttf:mode=harf;",
  "file:NotoSans-Regular.ttf:mode=harf;"})}
\setmainfont{DejaVu Serif}[RawFeature={fallback=labfallback}]
\setsansfont{DejaVu Sans}[RawFeature={fallback=labfallback}]
\setmonofont{DejaVu Sans Mono}[Scale=0.85, RawFeature={fallback=labfallback}]
\usepackage{graphicx}
\setkeys{Gin}{width=\linewidth, height=0.42\textheight, keepaspectratio}
"""


def for_print(nb):
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            cell.source = DETAILS.sub(lambda m: f"**{m.group(1).strip()}**\n\n{m.group(2)}", cell.source)
            cell.attachments = cell.get("attachments", {})
        elif cell.cell_type == "code":
            for output in cell.get("outputs", []):
                if "text" in output:
                    output.text = ANSI.sub("", output.text)
                data = output.get("data", {})
                if "text/html" in data and "text/plain" in data:
                    del data["text/html"]
                if "text/plain" in data:
                    data["text/plain"] = ANSI.sub("", data["text/plain"])
                if output.get("output_type") == "error":
                    output.traceback = [ANSI.sub("", line) for line in output.traceback]
    return nb


def make_pdf(key: Path):
    if not key.name.endswith("-key.ipynb"):
        sys.exit(f"{key}: give a key, lab-NN-key.ipynb")
    key = key.resolve()
    target = key.with_suffix(".pdf")
    nb = for_print(nbformat.read(key, as_version=4))
    with tempfile.TemporaryDirectory() as scratch:
        scratch = Path(scratch)
        copy = scratch / key.name
        nbformat.write(nb, copy)
        (scratch / "header.tex").write_text(HEADER)
        subprocess.run(
            ["pandoc", str(copy), "--from", "ipynb", "--to", "pdf", "--pdf-engine=lualatex",
             "--include-in-header", str(scratch / "header.tex"),
             "--highlight-style", "tango",
             "-V", "geometry:margin=2cm", "-V", "colorlinks=true", "-V", "linkcolor=blue",
             "-V", "urlcolor=blue", "-V", "papersize=letter",
             "--resource-path", str(key.parent), "--output", str(target)],
            check=True, cwd=scratch)
    print(f"wrote {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("keys", type=Path, nargs="+")
    for key in parser.parse_args().keys:
        make_pdf(key)


if __name__ == "__main__":
    main()
