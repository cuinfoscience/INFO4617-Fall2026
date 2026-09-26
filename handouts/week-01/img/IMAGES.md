# Images for the week-01 setup handout

Two figures from the textbook's chapter 1. `setup.md` shows figure 1.1,
`jupyter-new-menu_annotated.png`, under "Start your workspace", where
`anaconda_jupyter.png` stood until 2026-09-25; figure 1.2,
`jupyter-cells_annotated.png`, is offered and not placed. They were captured
on 2026-09-24 by `tools/shots` in the textbook repo (recipes in
`tools/shots/recipes/ch-01.yml`, provenance in `images/ch-01/provenance.json`
there, and notes on retaking them in `images/ch-01/IMAGES.md`), from a real
Jupyter Notebook 7.6 server set up with the handout's own commands. To refresh
one, retake and promote it in the textbook, then copy it here with the
textbook's `tools/shots/run sync`. The numbered markers are drawn by the
toolkit, not painted into the screenshots.

| File | Shows | Book figure | In `setup.md` |
|---|---|---|---|
| `jupyter-new-menu_annotated.png` | Jupyter's file list with the chapter 1 companion notebook (1), and **New** (2) open at its first item, **Python 3 (ipykernel)** (3), which makes a new notebook | Figure 1.1 | Under "Start your workspace", after `jupyter notebook`, with its caption there |
| `jupyter-cells_annotated.png` | The companion notebook: a Markdown cell (1), the first code cell run, with its prompt `[1]:` (2) and output (3), and the kernel's name, Python 3 (ipykernel) (4) | Figure 1.2 | Not placed. It would fit "Check that it works", or the `ModuleNotFoundError` item in Troubleshooting |

Jupyter Notebook 7's **New** menu names the kernel, **Python 3 (ipykernel)**,
where older versions said **Notebook**; the textbook's chapter 1 now says so.
Started from the `webdata` environment, that kernel is `webdata`'s Python.

A caption for figure 1.2, if it is placed: "A notebook's cells: text in a
Markdown cell (1), and a code cell that has run (2), with its output below it
(3). The kernel's name (4) is the Python the notebook runs."

Both show things that change: file ages, "Last Checkpoint", and Jupyter's look
from version to version.

## Copied by tools/shots

<!-- shots:begin: copies from the textbook's tools/shots, generated from shots.json; edits between these markers are replaced -->
Copied here by the textbook's `tools/shots/run sync`; `tools/shots/run synced` checks them.

| File | Copy of | Captured | Source | How |
|---|---|---|---|---|
| `jupyter-cells_annotated.png` | `ch-01/jupyter-cells` (images/ch-01/jupyter-cells_annotated.png, textbook `3ec4346`) | 2026-09-24 | http://localhost:8888/notebooks/ch-01-introduction.ipynb | tools/shots: Google Chrome for Testing 154.0.8037.57, 800×600 at 2× |
| `jupyter-new-menu_annotated.png` | `ch-01/jupyter-new-menu` (images/ch-01/jupyter-new-menu_annotated.png, textbook `3ec4346`) | 2026-09-24 | http://localhost:8888/tree | tools/shots: Google Chrome for Testing 154.0.8037.57, 824×600 at 2× |
<!-- shots:end -->
