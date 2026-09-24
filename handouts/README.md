# Handouts

Markdown handouts (`common/*.md`, `week-01/setup.md`, `week-04/rss-feeds.md`)
are read on GitHub as they are. Code handouts are written once in Quarto
markdown and built two ways:

- a **PDF** in the style of the slide frames (`common/handout.cls`: CU-gold
  frame bars, the decks' blocks and colors), with every output printed;
- a **companion notebook** with the same text and code, the code cells not
  yet run, for students to run step by step.

| Source | Built from it |
|---|---|
| `week-06/oscars-cards-to-rows.qmd` | `week-06/oscars-cards-to-rows.pdf`, `week-06/oscars-cards-to-rows.ipynb` |

## Build

```
cd handouts
make            # every PDF and notebook (Quarto, pdfLaTeX, Python 3)
make check      # rerun each handout's code against the live pages
make figures    # rebuild annotated screenshots from img/*_annotated.tex
```

Commit the `.qmd` together with the PDF and notebook built from it. On
every pull request that touches `handouts/`, GitHub rebuilds both
(`.github/workflows/build-handouts.yml`) and fails if a committed notebook
or PDF is out of date. `make check` fetches the real pages, so it runs on
your machine, not on GitHub.

## Writing a handout

Copy the front matter of `week-06/oscars-cards-to-rows.qmd` (the `format`
and `filters` lines point at `common/`). Then write markdown. `##` starts a
frame. The filter (`common/handout.lua`) handles these pieces:

| Write | PDF | Notebook |
|---|---|---|
| `## Step 1 --- Title` | a gold frame bar | a heading, new cell |
| a `python` code block | a code cell (gold bar) | a code cell, not run |
| a `{.out}` code block after it | the output (gray bar) | left out |
| `{.out markers="4:1 5:2"}` | output with marker ① beside line 4, ② beside line 5 | left out |
| `::: {.out}` around a pipe table | a DataFrame, as Jupyter shows it | left out |
| `①` to `⑨` | a numbered marker | the same character |
| `:::: {.columns align="T"}` with `::: {.column width="60%"}` | side-by-side columns | one after the other |
| `::: {.alertblock title="…"}` (also `.block`, `.exampleblock`) | the decks' block | a quoted paragraph |
| `::: {.legend}` around a list of `① text` items | a two-column key | the list |
| `::: {.caption}` | a small caption | a paragraph |
| `::: {.pdf-only}` / `::: {.notebook-only}` | kept / left out | left out / kept |
| `![](img/x.png){fig-alt="…"}` | the figure; `img/x.pdf` if it exists | the image, embedded |

Outputs are typed in, not computed when you build: copy each one from a
real run, then let `make check` confirm them. An annotated screenshot is a
small TikZ file next to the image (`img/*_annotated.tex`, with the marker
styles from `common/handoutmarkers.sty`); `make figures` turns it into a
PDF for the handout and a PNG for the notebook.

The class also works on its own for hand-written LaTeX handouts; its header
lists the commands (`frame`, `columns`, `block`, `\alert`, and the rest).
