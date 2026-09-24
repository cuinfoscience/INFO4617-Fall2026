#!/usr/bin/env python3
"""Build a handout's companion notebook from its .qmd source.

    python common/make_notebook.py week-06/oscars-cards-to-rows.qmd

writes week-06/oscars-cards-to-rows.ipynb next to the source. Prose becomes
Markdown cells (a new cell at each `##` step), ```python blocks become code
cells with no outputs, and the parts that only make sense on paper are left
out:

  ```{.out} blocks and ::: {.out} tables   the outputs; the PDF shows them
  ```{=latex} blocks, ::: {.pdf-only}      layout for the PDF
  fences of .columns, .column, .caption,   kept as plain Markdown
  .legend, .notebook-only

An ::: {.alertblock title="..."} becomes a quoted paragraph. Figures are
embedded in their cells as attachments, so the notebook works on its own
(Colab, JupyterHub, or a laptop). Markers ① to ⑦ stay as characters.

The output is deterministic: rebuilding without changing the .qmd gives a
byte-identical notebook, which is what the GitHub check relies on.
"""

import base64
import json
import re
import sys
from pathlib import Path

FENCE_CODE = re.compile(r"^(`{3,})\s*(.*)$")
FENCE_DIV = re.compile(r"^(:{3,})\s*(\{[^}]*\})?\s*$")
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)(\{[^}]*\})?")
KEEP_DIV_FENCES = {"columns", "column", "caption", "legend", "notebook-only"}
DROP_DIVS = {"pdf-only", "out"}


def front_matter(text):
    """Split YAML front matter from the body; read simple `key: "value"` pairs."""
    meta = {}
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return meta, text
    for line in match.group(1).splitlines():
        kv = re.match(r'^(\w+):\s*"(.*)"\s*$', line)
        if kv:
            meta[kv.group(1)] = kv.group(2)
    return meta, text[match.end():]


def div_classes(attrs):
    return set(re.findall(r"\.([\w-]+)", attrs or ""))


def div_title(attrs):
    match = re.search(r'title="([^"]*)"', attrs or "")
    return match.group(1) if match else ""


def markdown_line(line):
    """Pandoc-only spelling -> what Jupyter's Markdown renders."""
    line = re.sub(r"(?<=\S) --- (?=\S)", " — ", line)   # em dash
    line = line.replace(r"\ ", " ")                      # non-breaking space
    return line


class Builder:
    def __init__(self, qmd_path):
        self.qmd = qmd_path
        self.cells = []
        self.md = []            # Markdown lines of the cell being built
        self.attachments = {}   # attachments of that cell

    def flush(self):
        text = "\n".join(self.md).strip("\n")
        text = re.sub(r"\n{3,}", "\n\n", text)
        if text:
            cell = {"cell_type": "markdown", "metadata": {}, "source": text}
            if self.attachments:
                cell["attachments"] = self.attachments
            self.cells.append(cell)
        self.md, self.attachments = [], {}

    def code(self, source):
        self.flush()
        self.cells.append({"cell_type": "code", "execution_count": None,
                           "metadata": {}, "outputs": [], "source": source})

    def image(self, match):
        alt, src, attrs = match.group(1), match.group(2), match.group(3) or ""
        fig_alt = re.search(r'fig-alt="([^"]*)"', attrs)
        if fig_alt:
            alt = fig_alt.group(1)
        path = self.qmd.parent / src
        name = path.name
        data = base64.b64encode(path.read_bytes()).decode("ascii")
        self.attachments[name] = {"image/png": data}
        return f"![{alt}](attachment:{name})"

    def build(self):
        meta, body = front_matter(self.qmd.read_text(encoding="utf-8"))
        body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
        lines = body.split("\n")
        stack = []              # open divs: (classes, title)
        i = 0
        while i < len(lines):
            line = lines[i]
            fence = FENCE_CODE.match(line)
            if fence:
                ticks, info = fence.group(1), fence.group(2).strip()
                j = i + 1
                while j < len(lines) and not lines[j].startswith(ticks):
                    j += 1
                block = "\n".join(lines[i + 1:j])
                dropped = any(c & DROP_DIVS for c, _ in stack)
                if info == "python" and not dropped:
                    self.code(block)
                # ```{.out}, ```{=latex}, and anything inside dropped divs: skip
                i = j + 1
                continue
            div = FENCE_DIV.match(line)
            if div:
                attrs = div.group(2)
                if attrs:                       # opening fence
                    classes = div_classes(attrs)
                    stack.append((classes, div_title(attrs)))
                    if classes & {"alertblock", "block", "exampleblock"}:
                        self.md.append(f"> **{div_title(attrs)}.**")
                        self.md.append(">")
                elif stack:                     # closing fence
                    stack.pop()
                    self.md.append("")
                i += 1
                continue
            if any(c & DROP_DIVS for c, _ in stack):
                i += 1
                continue
            if line.startswith("## "):
                self.flush()
            line = markdown_line(line)
            line = IMAGE.sub(self.image, line)
            if any(c & {"alertblock", "block", "exampleblock"} for c, _ in stack):
                line = "> " + line if line.strip() else ">"
            self.md.append(line)
            i += 1
        self.flush()

        header = (
            f"*Companion notebook for the handout* **{meta.get('title', '')}** "
            f"*({meta.get('subtitle', '')}), INFO 4617 Web Data Science, "
            "University of Colorado Boulder.*\n\n"
            f"*Generated from `{self.qmd.name}` by `make` in `handouts/`: edit the "
            "`.qmd`, not this notebook. The code cells are not run yet. Run them "
            f"in order and compare what you get with the outputs in "
            f"`{self.qmd.with_suffix('.pdf').name}`.*"
        )
        cells = [{"cell_type": "markdown", "metadata": {}, "source": header}] + self.cells
        for n, cell in enumerate(cells, start=1):
            cell["id"] = f"cell-{n:02d}"
            text = cell["source"]
            # nbformat stores sources as lists of lines with trailing newlines
            cell["source"] = [l + "\n" for l in text.split("\n")[:-1]] + [text.split("\n")[-1]]
        # put "id" first, as Jupyter writes it
        cells = [{"id": c.pop("id"), **c} for c in cells]
        return {
            "cells": cells,
            "metadata": {
                "kernelspec": {"display_name": "Python 3", "language": "python",
                               "name": "python3"},
                "language_info": {"name": "python"},
            },
            "nbformat": 4,
            "nbformat_minor": 5,
        }


def main(argv):
    if len(argv) < 2:
        sys.exit("usage: make_notebook.py week-NN/name.qmd [...]")
    for arg in argv[1:]:
        qmd = Path(arg)
        notebook = Builder(qmd).build()
        out = qmd.with_suffix(".ipynb")
        out.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n",
                       encoding="utf-8")
        print(f"wrote {out} ({len(notebook['cells'])} cells)")


if __name__ == "__main__":
    main(sys.argv)
