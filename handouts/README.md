# Handouts

Markdown handouts (`common/*.md`, `week-01/setup.md`, `week-04/rss-feeds.md`)
are read on GitHub as they are. Handouts that walk through screens are
written in LaTeX with `common/handout.cls` and built to a PDF only: week 7's
three Friday activities, `week-07/triage-an-issue.tex`,
`week-07/review-a-pull-request.tex`, and `week-07/issue-to-pull-request.tex`.
Week 8's *Set up Selenium for chapter 8* is a page, `week-08/README.md`, and
the notebook it has students download and run, `week-08/selenium-setup.ipynb`
(see "A notebook students run" below). Code handouts are written once in
Quarto markdown and built two ways:

- a **PDF** in the style of the slide frames (`common/handout.cls`: CU-gold
  frame bars, the decks' blocks and colors), with every output printed;
- a **companion notebook** with the same text and code, the code cells not
  yet run, for students to run step by step.

| Source | Built from it |
|---|---|
| `week-06/oscars-cards-to-rows.qmd` | `week-06/oscars-cards-to-rows.pdf`, `week-06/oscars-cards-to-rows.ipynb` |
| `week-07/*.tex` (three) | a PDF each, no notebook |
| `week-08/README.md` and `week-08/selenium-setup.ipynb` | nothing: students read the page on GitHub, then download and run the notebook |

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

## A notebook students run

When the point of a handout is that students run code on their own
computers, such as setting up software, write it as a notebook, not as a
PDF of code to copy. Week 8 is the example: `week-08/selenium-setup.ipynb`,
and the page that goes with it, `week-08/README.md`. Each step of the
notebook is a markdown cell saying what it does, then a code cell that
fixes what it can and ends with a line starting **OK** or **FIX**, saying
what to do next.

- **A notebook can't tell students how to open it.** Pair it with a page
  that GitHub shows when they open the folder. Week 8's page takes a
  student from Anaconda as installed to the notebook, in clicks:
  - the words they'll meet;
  - GitHub's **Download raw file** button;
  - Jupyter from Anaconda Navigator, and finding the file in it;
  - running cells;
  - installing from a terminal, if the notebook can't;
  - chapter 8's own notebook;
  - a table of what to do when something goes wrong.
- **Start where students are.** Assume Anaconda as installed, nothing
  activated, and no terminal. Week 8's notebook installs Selenium in a cell
  of its own, `%pip install selenium`, and explains it there. `%pip`
  installs into whatever Python runs Jupyter, so the notebook works without
  the course's `webdata` environment, and in `webdata` too.
- **Say up front what won't work.** The first cell says what fails on a
  fresh computer, and why, before the first step.
- **Walk it as a student would.** Week 8's was tested in a real Jupyter in
  a browser, with the clicks the page describes, in a Python with only
  Jupyter. Then chapter 8's own notebook was run on the same Python, through
  "Starting the Browser".
- **Test the failures too.** Each FIX was tested by breaking that step on
  purpose. For week 8, those were no network for `pip`, Selenium Manager's
  downloads blocked, an old `chromedriver` on the `PATH`, and the browser
  started with the earlier steps skipped.
- **Commit it without outputs.** Edit it in Jupyter, then choose **Kernel →
  Restart Kernel and Clear Outputs of All Cells** before you save, so the
  file shows no one's paths. `make` doesn't build it, and CI doesn't check
  it.

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
