# INFO 4617 — Web Data Science (Fall 2026)

Course materials for **INFO 4617: Web Data Science**, University of Colorado Boulder, Fall 2026.

- **Meets:** Mondays, Wednesdays & Fridays, 12:20–1:10 pm, CASE W262 (Aug 20 – Dec 4, 2026)
- **Instructor:** Brian Keegan, Ph.D. — <brian.keegan@colorado.edu>
- **Textbook:** the open-source [Web Data Science book](https://github.com/cuinfoscience/Web-Data-Science-Book), which we read and revise together

## Weekly rhythm

| Day | Focus |
| --- | --- |
| **Monday** | Introduce a new concept and its companion notebook |
| **Wednesday** | Notebook Lab — work through and share the exercises |
| **Friday** | Textbook Revisions — propose and peer-review pull requests to the book |

Evaluation: Notebook Labs (30%) · Textbook Revisions (30%) · Final Project (40%). No exams.

## Building the syllabus

The syllabus is written in LaTeX (`syllabus.tex`) using the `memoir` class and the
bundled `mako-mem.sty` style. A rendered `syllabus.pdf` is committed for convenience.
To rebuild:

```bash
latexmk -pdf syllabus.tex
```

This requires a TeX distribution with the `memoir`, `fbb`, and `datenumber` packages
(e.g., a full TeX Live install, or [Overleaf](https://www.overleaf.com)). The build
runs `bibtex` against `refs.bib` to populate the in-line "Other resources" list.

## Files

| File | Description |
| --- | --- |
| `syllabus.tex` | Syllabus source |
| `syllabus.pdf` | Rendered syllabus |
| `mako-mem.sty` | Memoir style (adapted from Kieran Healy / Benjamin Mako Hill) |
| `refs.bib` | Bibliography for the resources list |

> **Note:** the Canvas course URL and office hours in `syllabus.tex` are placeholders
> (marked `PLACEHOLDER`/`TBD`) to be filled in before publishing.
