# INFO 4617 — Web Data Science (Fall 2026)

Course materials for **INFO 4617: Web Data Science**, University of Colorado Boulder, Fall 2026.

- **Meets:** Mondays, Wednesdays & Fridays, 12:20–1:10 pm, CASE W262 (Aug 20 – Dec 4, 2026)
- **Instructor:** Brian Keegan, Ph.D. — <brian.keegan@colorado.edu>
- **Textbook:** the open-source [Web Data Science book](https://github.com/cuinfoscience/Web-Data-Science-Book), which we read and revise together
- **Canvas:** [course 143304](https://canvas.colorado.edu/courses/143304)

## Weekly rhythm

From week 10, at students' request:

| Day | Focus |
| --- | --- |
| **Monday** | Lecture: the week's concepts and textbook chapter |
| **Wednesday** | Live-coding lab: we write the chapter's code together in the week's [lab notebook](labs/), with microsprints and discussion after each step |
| **Friday** | The same lab, picked up where Wednesday stopped; then a 15-minute textbook-revision block |

Students submit the chapter's **Recommended Exercises** from its companion
notebook, due the Sunday after the lab. Through week 9, Wednesday was a
notebook lab on the companion notebook and Friday a textbook-revision
workshop.

Evaluation: Notebook Labs (30%) · Textbook Revisions (15%) · Attendance (15%) · Final
Project (40%). No exams. The lowest two lab scores are dropped.

## Layout

| Directory | Contents |
| --- | --- |
| [`syllabus/`](syllabus/) | LaTeX syllabus source and rendered `syllabus.pdf` |
| [`slides/`](slides/) | Weekly lecture decks (one folder per teaching week) — see [`slides/README.md`](slides/README.md) |
| [`handouts/`](handouts/) | Student-facing reference pages (see below) |
| [`labs/`](labs/) | Wednesday's live-coding lab notebooks and their solutions, from week 10 — see [`labs/README.md`](labs/README.md) |
| [`canvas/`](canvas/) | Canvas migration tooling — see [`canvas/README.md`](canvas/README.md) |

### Handouts

Mirrors `slides/`: shared pages live in `handouts/common/`, week-specific ones
under `handouts/week-NN/`.

| File | Purpose |
| --- | --- |
| [`handouts/week-01/setup.md`](handouts/week-01/setup.md) | Self-paced environment setup — Anaconda, Git, GitHub — done before the first notebook lab |
| [`handouts/week-04/rss-feeds.md`](handouts/week-04/rss-feeds.md) | Starter RSS feeds (news and podcasts), the feed-finding technique, and a directory to browse more — for Chapter 4's lab and take-home. |
| [`handouts/common/revision-framework.md`](handouts/common/revision-framework.md) | The framework for proposing textbook revisions: three families, seven types, the issue/PR skeleton, and how revisions are graded. Used every Friday. |
| [`handouts/common/pull-request-walkthrough.md`](handouts/common/pull-request-walkthrough.md) | The click-by-click mechanics: matching a bug to its file, editing in GitHub's web editor, opening the PR, writing the description, and what happens after it merges. |

## Building

**Syllabus** (`memoir`, `fbb`, `datenumber`; runs `bibtex` against `refs.bib`):

```bash
cd syllabus && latexmk -pdf syllabus.tex
```

**Slides** (Gotham beamer theme vendored in `slides/common/`; needs `biblatex` + `biber`):

```bash
cd slides && make            # every deck
cd slides/week-01 && latexmk -pdf week-01.tex  # just one
```

Each deck also compiles standalone from its own folder — no `TEXINPUTS` setup needed.

> **Note:** office hours in `syllabus/syllabus.tex` are still a `TBD` placeholder,
> and the images in `slides/week-*/img/` are labeled placeholders to be replaced
> with real screenshots (each folder's `IMAGES.md` says what belongs where).
