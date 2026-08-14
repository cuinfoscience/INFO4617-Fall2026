# INFO 4617 — Web Data Science (Fall 2026)

Course materials for **INFO 4617: Web Data Science**, University of Colorado Boulder, Fall 2026.

- **Meets:** Mondays, Wednesdays & Fridays, 12:20–1:10 pm, CASE W262 (Aug 20 – Dec 4, 2026)
- **Instructor:** Brian Keegan, Ph.D. — <brian.keegan@colorado.edu>
- **Textbook:** the open-source [Web Data Science book](https://github.com/cuinfoscience/Web-Data-Science-Book), which we read and revise together
- **Canvas:** [course 143304](https://canvas.colorado.edu/courses/143304)

## Weekly rhythm

| Day | Focus |
| --- | --- |
| **Monday** | Introduce a new concept and its companion notebook |
| **Wednesday** | Notebook Lab — work through and share the exercises |
| **Friday** | Textbook Revisions — propose and peer-review pull requests to the book |

Evaluation: Notebook Labs (30%) · Textbook Revisions (30%) · Final Project (40%). No exams.

## Layout

| Directory | Contents |
| --- | --- |
| [`syllabus/`](syllabus/) | LaTeX syllabus source and rendered `syllabus.pdf` |
| [`slides/`](slides/) | Weekly lecture decks (one folder per teaching week) — see [`slides/README.md`](slides/README.md) |
| [`handouts/`](handouts/) | Student-facing reference pages (see below) |
| [`canvas/`](canvas/) | Canvas migration tooling — see [`canvas/README.md`](canvas/README.md) |

### Handouts

| File | Purpose |
| --- | --- |
| [`handouts/setup.md`](handouts/setup.md) | Self-paced environment setup — Anaconda, Git, GitHub — done before the first notebook lab |
| [`handouts/revision-framework.md`](handouts/revision-framework.md) | The framework for proposing textbook revisions: three families, seven types, the issue/PR skeleton, and how revisions are graded. Used every Friday. |

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
