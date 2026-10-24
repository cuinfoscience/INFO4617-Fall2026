# Hand-off: weeks 11–14 and the Final Project

Written 2026-10-23, at the end of the session that graded weeks 2–9 and set
up Canvas for the rest of the semester. It's for the next agent or person who
grades, publishes, or edits anything from week 11 on. The rules themselves are
in [`grading.md`](grading.md); the facts written in more than one place are in
[`course-facts.md`](course-facts.md). The repository changes are in pull
request #140 (`claude/inspiring-cerf-wi8l7e`), which was open, not merged,
when this was written.

## What Canvas holds now

Course 143304. Everything below is unpublished except the proposal; the
instructor publishes each week.

| Canvas id | Assignment | Points | Due (Mountain) | Rubric |
|---|---|---|---|---|
| 2852043 | Week 11 Lab — Government data APIs | 10 | Sun Nov 1 | Notebook Lab |
| 2852044 | Week 12 Lab — Social & media platform APIs | 10 | Sun Nov 8 | Notebook Lab |
| 2852045 | Week 13 Lab — AI & language-model APIs | 10 | Sun Nov 15 | Notebook Lab |
| 2852046 | Week 14 Lab — Automating data collection | 10 | Sun Nov 22 | Notebook Lab |
| 2852056 | Week 11 Portfolio — Set up your project repo | 2 | Sun Nov 1 | Week 11 Portfolio |
| 2852057 | Week 12 Portfolio — Collect and clean your data | 2 | Sun Nov 8 | Week 12 Portfolio |
| 2852058 | Week 13 Portfolio — Analyze your data | 2 | Sun Nov 15 | Week 13 Portfolio |
| 2852059 | Week 14 Portfolio — Draft your write-up | 2 | Sun Nov 29 | Week 14 Portfolio |
| 2852060 | Final Project — Proposal (published) | 30 | Sun Oct 25 | Proposal |
| 2852061 | Final Project — Presentation | 60 | final week | Presentation |
| 2852062 | Final Project — Repository & Write-up | 150 | Mon Dec 7 | Repository & Write-up |

- **Week 10 has no lab or revision assignment.** The instructor decided this;
  don't create them or ask again. `NO_ASSIGNMENT_WEEKS` in
  `canvas/course_spec.py` keeps `migrate.py build` from creating them.
- **The portfolio checkpoints replace textbook pull requests in weeks 11–14.**
  Each student builds one public repository on their own GitHub account and
  submits its URL each week. There is no starter template.
- **Weights.** Canvas weights a group's assignments by their points:
  - The Final Project's 30 / 60 / 150 points give the syllabus's 5% / 10% / 25%.
    Change all three together or not at all.
  - In Textbook Revisions (15%), each checkpoint is about 1.9% of the course
    grade and each week 2–9 revision about 0.9%.
- **Every rubric is in `RUBRICS` in `canvas/course_spec.py`** and matches
  Canvas criterion by criterion. Each is attached for grading, and each total
  equals its assignment's points.

## Grading a week

`canvas/grading.ipynb` does steps 1, 2, and 4 for attendance, Textbook
Revisions, the portfolio checkpoints, and labs. In step 2 it scores only the
plain cases and prints the rest for you to grade by hand. Use it, and keep its
outputs out of the repository.

1. Download the submissions from Canvas, and keep the files in their own
   folder (they're untrusted; read them with `python -I`).
2. Score them by `grading.md`.
   - **Labs** use the five-criterion rubric. A blank scaffold or late work
     overrides its total.
   - **A portfolio checkpoint** is graded on what was pushed by the deadline.
     The repos are public on students' own accounts, so the GitHub tools in a
     session may not reach them. Clone anonymously instead, and check the
     state at the due time with `git rev-list -1 --before=<due> HEAD`.
3. Show the instructor the scores and every comment, and wait for an explicit
   approval before posting anything. List anything ambiguous separately,
   such as a link to someone else's work, a second GitHub account, or
   content that looks generated.
4. Post. For a rubric-graded assignment, prefer posting a
   `rubric_assessment` (points per criterion), so students see the
   breakdown; a bare `posted_grade` sets the score without filling in the
   rubric. Then read every grade and comment back from Canvas.

Don't put students' names, or anything that identifies their work, in this
repository.

## Open items

- **Proposals:** due Sunday, October 25. Grade them with the proposal rubric
  after the deadline. One had been submitted by October 23.
- **Labs held for the instructor:** two week 8–9 labs were held for the
  instructor to inspect. A third, week 8, waits on a resubmission once its
  author's Selenium driver works. One week 3 lab was resubmitted after it was
  graded. All four show as needing grading in Canvas's gradebook.
- **Slides:** `slides/week-11` to `week-14` still have Friday frames for
  textbook revisions. They should describe that week's portfolio checkpoint
  instead.
- **Syllabus:** `syllabus/syllabus.tex`, which the instructor edits in
  Overleaf, says three things Canvas no longer does:
  - that every week has textbook pull requests;
  - that revision credit reflects the substance of the revisions and the
    peer reviews;
  - nothing about late labs (its 1%-a-day rule covers revisions and the
    Final Project only).

  Propose those edits; don't make them unasked.
- **Publishing:** the week 11–14 labs and checkpoints, the presentation, and
  the write-up are unpublished. Publish only when the instructor says.
- **Drift that `build` reports but leaves alone:**
  - Attendance points: weeks 2–10 are 2–3 points in Canvas against the spec's 1.
  - Week 8's revision description, which `relabel_labs.py` flags.
  - Two typos on the proposal page, kept so the spec matches Canvas: "is is
    short" and "Is your collection is allowed?".
- **Pull request #140:** merge only when the instructor asks (see
  `AGENTS.md`, "Merging"). If it's merged before more changes, start a new
  branch from `main`.
