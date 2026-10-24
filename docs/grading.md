# Grading rules, as applied in Canvas

The rules the instructor set while grading weeks 2–9 on 2026-10-23, and the
rubrics set up then for the rest of the semester, so later weeks are graded
the same way. `course-facts.md` lists where each rule is also
written; when a rule changes, change it here and there in the same pull
request. Canvas comments are one sentence each; where a submission needs more
than one, they're joined into one comment.

Nothing is posted to Canvas until the instructor has seen the scores and the
comments and approved them. After posting, read every grade and comment back
from Canvas to confirm it was saved.

`canvas/grading.ipynb` applies these rules: it proposes scores and comments
for a week, you review the table, and it posts and checks them. When a rule
here changes, change the notebook's Setup cell too (`COMMENTS`,
`OPTIONAL_STEPS`, `LATE_GRACE_HOURS`, and `LATE_CAP`; for attendance,
`LATE_CREDIT` and `LATE_DAYS` at the top of its section), and the scoring cell
it affects.

## Attendance (1 point per class held)

Attendance is the daily note, a Google Form students fill in at the end of
each class. It asks for the date (`Today is`) and a number announced in class.
The notebook reads the form's CSV; the CSV stays out of the repository. This is
how weeks 1–10 were graded in Canvas, and the notebook gives the same scores
for all of them:

- **One point per class held.** A class is held when it is a scheduled meeting
  day and its number was given. A cancelled class drops out of the week's
  points.
- **The number is the presence check.** Each day's number is the answer most
  of that day's responses give. A response with another number earns nothing.
- **The day the form was sent decides the class.** A wrong `Today is`, such as
  the wrong year, doesn't matter when the form was sent that day.
- **Late notes earn nothing.** A late note is sent on a later day but gives an
  earlier class's date and number.
- **One response per student per class counts.**
- **A response from an address other than `identikey@colorado.edu` counts once
  it is matched to a student.** Students used personal and school addresses
  for about one response in eight in weeks 1–10. The matches live in
  `email_aliases.csv` in the grading folder, never in the repository.

## Textbook Revisions, weeks 2–9 (1 point a week)

Week 10 has no revision (or lab) assignment. Weeks 11–14 are portfolio
checkpoints, below.

Credit or no credit. A submission earns 1 when its URL points at an issue, a
pull request, or a comment that the student made on GitHub. Any class
repository counts: the book, this repo, or the Missing Manual. So do a commit, a
compare page, or a pull request inside the student's own fork.

- A link to someone else's issue, where the student's work is a comment on it,
  earns 1, with this comment: "Full credit this week, but next time please
  submit the link to your own comment (click its timestamp to copy a URL ending
  in #issuecomment-…) rather than the link to the whole issue."
- The same work submitted for two weeks earns credit once, in the week it was
  made; the other week earns 0.
- No submission earns 0.

Match GitHub accounts to Canvas students by the author of the linked item (or
of the linked comment or review), and list any mismatch for the instructor
before scoring.

## Notebook Labs (10 points)

Students submit the chapter's companion notebook as HTML. Only its
Recommended Exercises section is graded; the Additional Exercises are
optional.

From week 11 the labs are graded with the "Notebook Lab (10 points)" rubric
attached in Canvas (`LAB_RUBRIC` in `canvas/course_spec.py`): five criteria,
each Met 2, Partly met 1, or Not met 0.

| Criterion | Met (2) | Partly met (1) | Not met (0) |
|---|---|---|---|
| Valid notebook HTML | An HTML file of the notebook, in any layout | | Missing or unreadable |
| Every required step attempted | Every code step has the student's own code; steps announced as optional count as done | At least half the steps | Fewer than half, or the blank scaffold |
| Run, with output visible | The student's code cells are run and their output shows; errors left visible still count | Some cells with the student's code are unrun | None was run |
| Interpretation in their own words | About the requested length and about their own results, in the prompt cell, comments, a Markdown cell, or a `print()` | Thin (one to three sentences) or generic | Missing, or the placeholder left as is |
| Each step does its task | Each attempted step does what it asks, with the student's own choices | Some steps substitute something else, such as the chapter's own example | Unrelated to the steps |

A blank scaffold and late work are applied by overriding the rubric's total, as
below.

Weeks 4–9 were graded before the rubric existed, with the same five elements
but one difference: unrun code got full credit and a reminder comment. Weeks 2
and 3 kept the instructor's own scores. None of weeks 2–9 has a rubric in
Canvas.

- **Optional steps**, done or not: week 5 Step 2; week 7 Steps 4 and 5. The
  instructor told students to skip them.
- **A blank scaffold** (no student code, no interpretation) earns 0, with: "This
  upload was the blank exercise scaffold, so please save your notebook after
  completing the exercises, export it to HTML, and upload that completed file."
- **Late work:** 24 hours' grace, then 1 point for every started day since the
  deadline, at most 5. Comment: "This lab was submitted N days late, past the
  24-hour grace period, so N points were deducted." Add "(the late penalty is
  capped at 5 points)" past five days.
- **No submission** earns 0, with no comment.

One-sentence comments, added where they apply:

- Code not run: "Please run every cell before exporting so that both your code
  and its output appear in the HTML you submit."
- A traceback in the student's own cells: "When you hit a traceback, check that
  the libraries you need are imported and that the cells defining your
  variables have been run first, in order."
- An interpretation citing results the notebook doesn't show: "Your
  interpretation reports results that don't appear in your notebook's output,
  so please run every cell before exporting so the evidence for your claims is
  visible." This replaces the "not run" comment.
- Week 9, the chapter's own PDFs instead of new ones: full credit, with "Full
  credit this week, but remember that Step 1 asks you to find three new PDFs
  from a government source rather than reusing the chapter's own files."

Hold a submission for the instructor, ungraded, when it looks produced by an
AI agent (notes addressed to a reader, results quoted that no output shows) or
when a setup failure stopped the work.

## Portfolio checkpoints, weeks 11–14 (2 points a week)

In weeks 11–14 the Textbook Revisions assignments build each student's Final
Project as a public portfolio: one repository on the student's own GitHub
account, updated weekly, graded on what is pushed by the deadline. Each has a
rubric in Canvas (`PORTFOLIO_RUBRICS` in `canvas/course_spec.py`) with two
criteria, each Met 1 or Not met 0:

| Week, due | Criterion 1 | Criterion 2 |
|---|---|---|
| 11, Sun Nov 1: set up the repo | A public repo with a README (title, name, summary of the question, placeholder sections) | `proposal.md`, plus placeholders for the notebook, the report, and `data/` |
| 12, Sun Nov 8: collect and clean | Collection code that runs politely and saves raw data, and a cleaning step that produces a tidy dataset | A data sample with a dictionary, and the README's Data section (source, date, count, what was kept out and why) |
| 13, Sun Nov 15: analyze | A notebook that runs top to bottom with output, with results that answer part of the question | A figure with title, axes, and caption, and the README's Methods and preliminary Findings |
| 14, Sun Nov 29: draft the write-up | A full draft of `report.md` or `report.pdf` using their own results, citing sources | All four required files current, and a README that lets someone reproduce the project |

Repos hold code and a small sample of the data; the full raw data stays out
where terms of service, size, or personal information make sharing unwise, and
the README says so. There is no starter template.

## Commendations

Particularly strong work gets a short comment naming what was strong, at most
two or three per student across the semester. Commend only work whose code and
output are in the submission.

## Final Project: proposal (30 points)

Graded with the "Final Project Proposal (30 points)" rubric attached to the
Canvas assignment, which is `PROPOSAL_RUBRIC` in `canvas/course_spec.py`: one criterion per bullet of the
assignment page, each Full 3, Mostly 2, Attempted 1, or Missing 0, with no
half points. Parts 1–3 are worth 9, 9, and 12.

## Final Project: presentation (60 points) and repository and write-up (150 points)

Both are graded with rubrics attached in Canvas (`PRESENTATION_RUBRIC` and
`WRITEUP_RUBRIC`). Each criterion is Full, Mostly, Attempted, or Missing, at
about 100, 67, 33, and 0 percent of its points, in whole points.

| Presentation (about five minutes plus questions) | Points |
|---|---|
| Question and who cares | 10 |
| Data and method | 10 |
| Findings that carry an argument (one or two visualizations) | 15 |
| Surprises and limitations | 10 |
| Delivery | 10 |
| Questions | 5 |

| Repository and write-up | Points |
|---|---|
| Required files: `README.md`, `proposal.md`, at least one `.ipynb`, and `report.md` or `report.pdf` | 10 |
| Reproducibility | 20 |
| Collection and cleaning | 20 |
| Analysis | 25 |
| The written report (about 2,000–3,000 words) | 30 |
| Claims match the evidence | 20 |
| Ethics | 15 |
| Portfolio practice (layout, commits through weeks 11–14, AI disclosure) | 10 |

The proposal, presentation, and write-up are 30, 60, and 150 points, the
ratio 5 : 10 : 25 that the syllabus's weights need.
