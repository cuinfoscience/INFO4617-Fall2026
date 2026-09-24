"""Check the Oscars handout against the live page.

Runs every code block in oscars-cards-to-rows.tex, in order, in a fresh
Jupyter kernel (so the page is fetched once, exactly as the handout does it),
then compares each result with the output printed under it in the handout:
plain output blocks, the printed class counts in Step 4, and the two
DataFrame tables in Step 11.

    pip install requests beautifulsoup4 pandas nbformat nbclient ipykernel
    python check_outputs.py

Exit status 0 means every printed output still matches the live page.
"""
import csv
import io
import re
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

HERE = Path(__file__).resolve().parent
TEX = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "oscars-cards-to-rows.tex"


def latex_text(x):
    """The text of one LaTeX table cell, as pandas would print it."""
    x = x.replace("\\'e", "é").replace("\\_", "_")
    x = re.sub(r"\\(?:textbf|emph)\{([^}]*)\}", r"\1", x)
    return x.strip()


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
    body = TEX.read_text(encoding="utf-8").split("\\begin{document}", 1)[1]
    blocks = re.findall(
        r"\\begin\{(code|out|dfout)\}(\{[^\n]*\})?\n(.*?)\\end\{\1\}", body, re.S)

    # pair each code block with the output block that follows it (if any)
    pairs, code = [], None
    for kind, _arg, text in blocks:
        if kind == "code":
            if code is not None:
                pairs.append((code, None, None))
            code = text.rstrip("\n")
        else:
            pairs.append((code, kind, text.rstrip("\n")))
            code = None
    if code is not None:
        pairs.append((code, None, None))

    # one notebook cell per code block; after a DataFrame, one more cell
    # that prints the DataFrame as tab-separated text for comparison
    cells, plan = [], []
    for code, kind, expected in pairs:
        cells.append(nbformat.v4.new_code_cell(code))
        is_table = kind == "dfout" and "\\midrule" in expected
        plan.append((kind, expected, is_table, False))
        if is_table:
            cells.append(nbformat.v4.new_code_cell('print(_.to_csv(sep="\\t"), end="")'))
            plan.append((kind, expected, True, True))

    nb = nbformat.v4.new_notebook()
    nb.cells = cells
    NotebookClient(nb, timeout=180, kernel_name="python3").execute()

    checked = failed = 0
    for (kind, expected, is_table, is_csv), cell in zip(plan, nb.cells):
        got = output_text(cell)
        first = cell.source.splitlines()[0][:70]
        if got.startswith("ERROR") or "\nERROR " in got:
            print(f"ERROR in: {first}\n  {got}")
            failed += 1
            continue
        if kind is None or (is_table and not is_csv):
            continue
        if kind == "out":
            ok = got == expected
        elif not is_table:  # printed lines, typed in the handout as \ol|...|
            expected = "\n".join(re.findall(r"\\ol\|([^|]*)\|", expected))
            ok = got == expected
        else:
            rows = [r for r in expected.split("\\midrule", 1)[1].split("\\\\") if r.strip()]
            want = [[latex_text(c) for c in r.split("&")] for r in rows]
            have = list(csv.reader(io.StringIO(got), delimiter="\t"))[1:]
            ok, expected, got = want == have, str(want), str(have)
        checked += 1
        if not ok:
            failed += 1
            print(f"MISMATCH after: {first}\n  handout: {expected!r}\n  live:    {got!r}")

    print(f"{checked - failed} of {checked} outputs match the live page.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
