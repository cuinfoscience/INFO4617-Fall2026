# Images for the week-01 setup handout

Two figures from the textbook's chapter 1, offered to `setup.md` and not yet
placed in it. Replacing `anaconda_jupyter.png` (in `slides/week-01/img/`) is
the instructor's call. They were captured on 2026-09-24 by `tools/shots` in the
textbook repo (recipes in `tools/shots/recipes/ch-01.yml`, provenance in
`images/ch-01/provenance.json` there, and notes on retaking them in
`images/ch-01/IMAGES.md`), from a real Jupyter Notebook 7.6 server set up with
the handout's own commands. To refresh one, retake and promote it in the
textbook, then copy its `_annotated.png` here. The numbered markers are drawn
by the toolkit, not painted into the screenshots.

| File | Shows | Book figure | For |
|---|---|---|---|
| `jupyter-new-menu_annotated.png` | Jupyter's file list with the chapter 1 companion notebook (1), and **New** (2) open at its first item, **Python 3 (ipykernel)** (3), which makes a new notebook | Figure 1.1 | "Make a new notebook" in "Check that it works" |
| `jupyter-cells_annotated.png` | The companion notebook: a Markdown cell (1), the first code cell run, with its prompt `[1]:` (2) and output (3), and the kernel's name, Python 3 (ipykernel) (4) | Figure 1.2 | "Start your workspace", or the `ModuleNotFoundError` item in Troubleshooting |

Jupyter Notebook 7's **New** menu names the kernel, **Python 3 (ipykernel)**,
where older versions said **Notebook**; the textbook's chapter 1 now says so.
Started from the `webdata` environment, that kernel is `webdata`'s Python.

A caption for each, if placed:

- `jupyter-new-menu_annotated.png`: "Jupyter's file list. **New** (2) opens a
  menu whose first item, **Python 3 (ipykernel)** (3), makes a new notebook.
  To open a notebook you have, such as the chapter 1 companion notebook (1),
  click its name."
- `jupyter-cells_annotated.png`: "A notebook's cells: text in a Markdown cell
  (1), and a code cell that has run (2), with its output below it (3). The
  kernel's name (4) is the Python the notebook runs."

Both show things that change: file ages, "Last Checkpoint", and Jupyter's look
from version to version.
