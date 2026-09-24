#!/usr/bin/env python3
"""Check a handout's printed outputs against the live pages.

    python common/check_outputs.py week-06/oscars-cards-to-rows.qmd

Runs every ```python block of the .qmd, in order, in a fresh Jupyter kernel
(so each page is fetched exactly as the handout fetches it), then compares
each result with the output written under the block: a ```{.out} block
(text; a markers="..." attribute is ignored) or a ::: {.out} pipe table
(a DataFrame, compared cell by cell with the index).

    pip install requests beautifulsoup4 pandas nbformat nbclient ipykernel

Exit status 0 means every printed output still matches.
"""
import csv
import io
import re
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

FENCE_CODE = re.compile(r"^(`{3,})\s*(.*)$")
FENCE_DIV = re.compile(r"^(:{3,})\s*(\{[^}]*\})?\s*$")


def blocks(qmd_text):
    """Yield ("code", src), ("out", text), and ("table", rows) in order."""
    lines = re.sub(r"<!--.*?-->", "", qmd_text, flags=re.S).split("\n")
    i, in_out_div, table = 0, False, []
    while i < len(lines):
        line = lines[i]
        fence = FENCE_CODE.match(line)
        if fence:
            ticks, info = fence.group(1), fence.group(2).strip()
            j = i + 1
            while j < len(lines) and not lines[j].startswith(ticks):
                j += 1
            text = "\n".join(lines[i + 1:j])
            if info == "python":
                yield "code", text
            elif re.match(r"^\{\.out\b", info):
                yield "out", text
            i = j + 1
            continue
        div = FENCE_DIV.match(line)
        if div:
            if div.group(2) and re.search(r"\.out\b", div.group(2)):
                in_out_div, table = True, []
            elif not div.group(2) and in_out_div:
                in_out_div = False
                yield "table", table
            i += 1
            continue
        if in_out_div and line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-+:?", c) for c in cells):   # skip |--:|
                table.append(cells)
        i += 1


def output_text(cell):
    parts = []
    for o in cell.outputs:
        if o.output_type == "stream":
            parts.append(o.text)
        elif o.output_type == "execute_result":
            parts.append(o.data.get("text/plain", "") + "\n")
        elif o.output_type == "error":
            parts.append(f"ERROR {o.ename}: {o.evalue}\n")
    return "".join(parts).rstrip("\n")


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: check_outputs.py week-NN/name.qmd")
    qmd = Path(sys.argv[1])
    items = list(blocks(qmd.read_text(encoding="utf-8")))

    # one cell per code block; after a DataFrame, one more cell that prints
    # it as tab-separated text for comparison
    cells, plan = [], []
    for n, (kind, value) in enumerate(items):
        if kind != "code":
            continue
        expected = items[n + 1] if n + 1 < len(items) and items[n + 1][0] != "code" else None
        cells.append(nbformat.v4.new_code_cell(value))
        plan.append(("code", expected))
        if expected and expected[0] == "table":
            cells.append(nbformat.v4.new_code_cell('print(_.to_csv(sep="\\t"), end="")'))
            plan.append(("csv", expected))

    nb = nbformat.v4.new_notebook()
    nb.cells = cells
    NotebookClient(nb, timeout=180, kernel_name="python3",
                   resources={"metadata": {"path": str(qmd.parent)}}).execute()

    checked = failed = 0
    for (role, expected), cell in zip(plan, nb.cells):
        got = output_text(cell)
        first = cell.source.splitlines()[0][:70]
        if got.startswith("ERROR") or "\nERROR " in got:
            print(f"ERROR in: {first}\n  {got}")
            failed += 1
            continue
        if expected is None or (expected[0] == "table" and role == "code"):
            continue
        kind, want = expected
        if kind == "out":
            ok = got == want
        else:
            header, *rows = want
            have = list(csv.reader(io.StringIO(got), delimiter="\t"))[1:]
            ok = rows == have
            want, got = str(rows), str(have)
        checked += 1
        if not ok:
            failed += 1
            print(f"MISMATCH after: {first}\n  handout: {want!r}\n  live:    {got!r}")

    print(f"{qmd.name}: {checked - failed} of {checked} outputs match the live page.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
