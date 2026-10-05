# Handouts

Markdown handouts (`common/*.md`, `week-01/setup.md`, `week-04/rss-feeds.md`)
are read on GitHub as they are. Handouts that walk through screens are
written in LaTeX with `common/handout.cls` and built to a PDF only: week 7's
three Friday activities, `week-07/triage-an-issue.tex`,
`week-07/review-a-pull-request.tex`, and `week-07/issue-to-pull-request.tex`,
and week 8's `week-08/selenium-setup.tex`, whose code is chapter 8's and
whose figures are screenshots of it running. Code handouts are written once
in Quarto markdown and built two ways:

- a **PDF** in the style of the slide frames (`common/handout.cls`: CU-gold
  frame bars, the decks' blocks and colors), with every output printed;
- a **companion notebook** with the same text and code, the code cells not
  yet run, for students to run step by step.

| Source | Built from it |
|---|---|
| `week-06/oscars-cards-to-rows.qmd` | `week-06/oscars-cards-to-rows.pdf`, `week-06/oscars-cards-to-rows.ipynb` |
| `week-07/*.tex` (three) | a PDF each, no notebook |
| `week-08/selenium-setup.tex` | `week-08/selenium-setup.pdf`, no notebook (the cells are chapter 8's) |

## Build

```
cd handouts
make            # every PDF, and each .qmd's notebook (Quarto, pdfLaTeX, Python 3)
make check      # rerun each handout's code against the live pages
make figures    # rebuild annotated screenshots from img/*_annotated.tex
```

Commit the `.qmd` or `.tex` together with what is built from it. On
every pull request that touches `handouts/`, GitHub rebuilds both
(`.github/workflows/build-handouts.yml`) and fails if a committed notebook
or PDF is out of date. `make check` fetches the real pages, so it runs on
your machine, not on GitHub.

`make` also rebuilds a handout's PDF when an image in its `img/` folder
changes: a figure the textbook's `sync` copied there again, or an
`img/*_annotated.tex`, which it redraws first. The records (`shots.json`,
`IMAGES.md`) rebuild nothing. A notebook doesn't follow its images: after
one changes, rebuild it with `make -B week-NN/NAME.ipynb`. `make -B pdf`
redraws the `_annotated.tex` figures too, and their PDFs change only in
their dates, so restore them with `git checkout` rather than commit them.

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
PDF for the handout and a PNG for the notebook. Screenshots taken with the
textbook's `tools/shots` arrive with their markers drawn: its `sync`
command copies `NAME.png`, `NAME_annotated.pdf`, and `NAME_annotated.png`,
and records where each came from in `img/shots.json` (week 8). Retake or
re-mark those in the textbook, then sync them again; don't edit the copies.

The class also works on its own for hand-written LaTeX handouts; its header
lists the commands (`frame`, `columns`, `block`, `\alert`, and the rest).
