# Project documentation

Process artifacts for this repo that aren't course content: after-action
reports, and the plans that come out of them.

**Screenshots and the textbook's tools live in the textbook repo.** On
2026-09-24 the screenshot AAR, the screenshot-toolkit plan, and the chapters
1–5 back-fill plan moved to the textbook repository's
[`docs/`](https://github.com/cuinfoscience/Web-Data-Science-Book/tree/main/docs),
beside the toolkit's code (`tools/shots/`). That folder also holds:
- the AAR on the toolkit sprint for chapters 5, 7, and 8;
- the decision log, `decisions.md`, which records how pull requests merge;
- the hand-off note, `handoff.md`, which says where the screenshot work stands.

Start there for anything about screenshots, including the slide copies of
book figures.

- `aar/` — after-action reports, one file per review, named
  `YYYY-MM-DD-<scope>.md`. Each report compares what the written rules (such as
  `slides/common/AUTHORING.md`) and the shipped work say should happen against
  what actually happened. It root-causes any gap and turns findings into
  concrete revisions with a tracking table. When a finding gets
  resolved, update that report's tracking table and add a dated resolution
  note rather than deleting or rewriting the original findings — the report
  is a record of what was decided and why, and a later AAR checks it to see
  whether a revision actually stopped the pattern from recurring.
- `plans/` — plans for larger pieces of work that an AAR recommends, named
  `YYYY-MM-DD-<topic>.md`. Each plan names the AAR revision it implements. A
  plan records a proposal and the decisions behind it; once work starts,
  progress goes in the AAR's tracking table, not in the plan.

The repository root's `AGENTS.md` says how coding agents work here, and
`course-facts.md`, in this folder, lists the facts that are written in more
than one file (grade weights, due dates, the `webdata` command) and every
place each one lives. Both came from the 2026-10-16 AAR.

Current contents:

| File | What it is |
|---|---|
| `aar/2026-09-21-week-06-slides.md` | Slide-authoring contract vs. weeks 04–05; week-06 expansion |
| `course-facts.md` | Facts written in more than one file, with every place each one lives. Change them all in one pull request. |
| `grading.md` | The grading rules set while grading weeks 2–9 (2026-10-23): Textbook Revisions credit, the Notebook Labs rubric (in Canvas from week 11), late work and comment wording, commendations, the portfolio checkpoints for weeks 11–14, and the three Final Project rubrics. |
| `aar/2026-10-16-weeks-06-09.md` | Weeks 06–09: facts that drift between syllabus, Canvas, slides, and the textbook; Claude's standing rules with no file of their own; `AUTHORING.md` vs. the new Fridays. Follows up the 09-21 report. |
| `aar/2026-10-21-live-coding-labs.md` | The live-coding lab sprint (2026-10-19 to 10-22, #99–#135, with notes to 10-23 on #137's doc links and the reruns of weeks 5 and 10): conventions written for the key's run rather than the classroom, so every lab was rewritten after week 10 was taught; a restyle that broke `run_key.py`'s retries; no CI for `labs/`; agents waiting on refusing sites; a container restart. Lists the cells still to run from the instructor's laptop. Follows up the 10-16 report. |
| `plans/2026-09-24-friday-code-review.md` | A Friday code-review standup for students' textbook pull requests: preparation, the session, and what follows. Scheduled: the first standup is week 7's Friday, October 2, and that Friday's slides are built from its review table. |
| `plans/2026-09-24-friday-code-review-table.md` | That plan's review table: the textbook's 39 open pull requests on 2026-09-24, by chapter, with their checks, conflicts, and overlaps. It's rebuilt the day before class. |
| `plans/2026-10-02-standup-run-of-show.md` | Week 7's Friday: the backlog standup, its three activities and handouts, and the steps before and after class. |
| `plans/2026-10-09-backlog-sprint-run-of-show.md` | Week 8's Friday: the backlog sprint in three groups; the textbook's chapter and status labels; how to make the "Textbook backlog" project; and the queries behind the slides' counts. |
| `plans/2026-10-21-recommended-exercise-notebooks.md` | A recommendation, not yet built: standalone notebooks of each chapter's Recommended Exercises, generated from the chapter by the textbook's notebook script so they can't drift, and the questions to settle first. |

Moved to the textbook repo's `docs/` (2026-09-24):

| File there | What it is |
|---|---|
| [`aar/2026-09-24-screenshots.md`](https://github.com/cuinfoscience/Web-Data-Science-Book/blob/main/docs/aar/2026-09-24-screenshots.md) | Screenshots, editing, and annotation in ch-07–08, weeks 07–08, and the week-06 handout |
| [`plans/2026-09-24-screenshot-toolkit.md`](https://github.com/cuinfoscience/Web-Data-Science-Book/blob/main/docs/plans/2026-09-24-screenshot-toolkit.md) | A screenshot toolkit for the textbook repo (`tools/shots/`) |
| [`plans/2026-09-24-screenshot-backfill-ch01-05.md`](https://github.com/cuinfoscience/Web-Data-Science-Book/blob/main/docs/plans/2026-09-24-screenshot-backfill-ch01-05.md) | Using the toolkit to back-fill chapters 1–5, their slides, and handouts |
