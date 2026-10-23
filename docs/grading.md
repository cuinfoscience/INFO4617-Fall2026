# Grading rules, as applied in Canvas

The rules the instructor set while grading weeks 2–9 on 2026-10-23, so later
weeks are graded the same way. `course-facts.md` lists where each rule is also
written; when a rule changes, change it here and there in the same pull
request. Canvas comments are one sentence each; where a submission needs more
than one, they're joined into one comment.

Nothing is posted to Canvas until the instructor has seen the scores and the
comments and approved them. After posting, read every grade and comment back
from Canvas to confirm it was saved.

## Textbook Revisions (1 point a week)

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
optional. Five elements, each 2 (met), 1 (partly met), or 0 (not met):

| Element | 2 points | 1 point | 0 points |
|---|---|---|---|
| Valid HTML | Any HTML file, in any layout: a fresh notebook, a hand-built page, or two files | | Unreadable |
| Every required step attempted | Every code step has the student's own code | At least half the steps | Fewer than half |
| Run, with output | Any student code at all; unrun cells and tracebacks cost nothing | | |
| Interpretation in their own words | About the requested length and about their own results, wherever it is written: the prompt cell, comments, a new Markdown cell, or a `print()` | Present but thin (one to three sentences) or generic | Missing, or the placeholder left as is |
| Each step does its task | Each attempted step does what it asks, with the student's own choices | Some steps substitute something else | Unrelated to the steps |

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
when a setup failure stopped the work. Weeks 2 and 3 kept the instructor's own
scores.

## Commendations

Particularly strong work gets a short comment naming what was strong, at most
two or three per student across the semester. Commend only work whose code and
output are in the submission.

## Final Project: proposal (30 points)

Graded with the rubric attached to the Canvas assignment, which is
`PROPOSAL_RUBRIC` in `canvas/course_spec.py`: one criterion per bullet of the
assignment page, each Full 3, Mostly 2, Attempted 1, or Missing 0, with no
half points. Parts 1–3 are worth 9, 9, and 12.
