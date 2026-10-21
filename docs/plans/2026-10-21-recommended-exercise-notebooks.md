# Standalone Recommended Exercise notebooks: a recommendation

*Flagged for follow-up on 2026-10-21, when the Notebook Labs grade (30%)
became the chapter's Recommended Exercises, submitted from its companion
notebook. Nothing here is built yet.*

## The problem

Students submit the Recommended Exercises, but they live at the end of each
chapter's companion notebook (`notebooks/ch-NN-*.ipynb` in the textbook),
after every cell of the chapter. To submit, a student downloads the whole
chapter, scrolls past it, and fills in the last few cells. A notebook of only
the exercises would be easier to download, fill in, and grade.

The risk is a second copy of the exercises that drifts from the chapter. The
textbook already shows how that goes: the notebook-sync check fails whenever
a notebook is edited by hand or regenerated late (see the textbook's
`CONTRIBUTING.md`, "When Notebook sync is red").

## Recommendation: generate them, never copy them

1. **One source.** The exercises stay in the chapter's `.qmd`, under
   `## Recommended Exercises`, where readers of the book see them. Nobody
   writes an exercise notebook by hand.
2. **The same generator.** Extend the textbook's `tools/make_notebooks.py` to
   also write `notebooks/exercises/ch-NN-*-exercises.ipynb` from just that
   section: the chapter's title and link, the section's text and empty code
   cells, and a first cell saying that the chapter is the authoritative
   version, with the source path. It is the code that already turns the whole
   chapter into a notebook, run on one section, so the two can't disagree
   about how a cell is made.
3. **The same check.** The textbook's notebook-sync workflow regenerates
   `notebooks/` and fails on any difference, so it covers
   `notebooks/exercises/` without changes, as long as the files sit under
   `notebooks/`.
4. **Self-contained setup.** An exercise notebook can't rely on cells it
   no longer has. Each exercise section should open with a short setup cell,
   imports and the `HEADERS` it needs, written in the `.qmd` like any other
   cell, so the full notebook and the exercise notebook both run.
5. **One link.** Canvas's lab assignments, the slides, and `labs/README.md`
   link the exercise notebook's GitHub page (or its "Download raw file"
   address), never a copy in this repository.
6. **Better still, stop committing notebooks.** This is step 4 of the
   notebook-sync roadmap from 2026-10-20: build every notebook in CI and
   publish them with the book, so there is no committed copy to drift. If
   that lands first, the exercise notebooks become one more build output.

## Open questions for the instructor

- **Grading the fill-ins:** should students submit the exercise notebook
  through Canvas (an upload) or GitHub (a repository or a pull request)?
- **Graduate exercises:** should they go in the same notebook, marked
  "INFO 5617", or in a separate one?
- **Chapters 1–9:** should they get exercise notebooks too, so future terms
  have them from week 1?
