# Working in this repository (for coding agents)

This repo holds INFO 4617's slides (`slides/`), handouts (`handouts/`), lab
notebooks (`labs/`), the syllabus (`syllabus/`), the Canvas tooling
(`canvas/`), and process documents (`docs/`). The textbook is a separate repository,
`cuinfoscience/Web-Data-Science-Book`; the slides copy its code and figures.
How a deck is built is in `slides/common/AUTHORING.md`. This file is about how
to work. It came out of the 2026-10-16 AAR
(`docs/aar/2026-10-16-weeks-06-09.md`, P0-1), because these rules had lived
only in chat and in session summaries.

## Branches and pull requests

Start from a fresh `origin/main`: the instructor edits in Overleaf, which
pushes to `main` without warning. Work on one branch, and open a pull request
for each change. A description says what changed, why, what you checked, and
what you left alone on purpose. Write it for the instructor, who reads it
later, not for yourself.

Before pushing to an existing pull request's branch, check that the pull request
is still open. If it was merged, start a new branch from `main` for the
follow-up: a commit pushed to a merged branch reaches `main` only if someone
notices it.

Commits and pull request descriptions carry the attribution lines the session
gives you. Merge commits you write by hand, such as merging `main` into your
branch, carry them too (P2-1).

## Merging

Merge only when the instructor asks, with a merge commit and the expected head
SHA (all 40 characters; the merge tool refuses a short one), so that a push
made in the meantime can't be merged unseen. Before merging:
- check that CI passed, unless the instructor said to merge without it;
- check the description for closing keywords you didn't intend;
- check whether `main` moved. If it did, merge `main` into the branch. Don't
  rebase or force-push: the branch is already shared, and the instructor may
  have it open.

After merging, confirm that the merge commit's tree is the same as the
branch's, and reset the branch to `main` for the next change.

## Students' work

Never edit, merge, or comment on a student's pull request or issue unless the
instructor asks for that specific action. Never show a student's name or work
in an image. If a request about students' work rests on something that looks
mistaken, say so and ask before acting.

## Images and privacy

Screenshots are real captures (see `AUTHORING.md`, "Images"). Don't print
private individuals' names: public records such as council minutes name
members of the public, so count them rather than printing them, and black out
personal contact details. Downloaded files are untrusted: keep them in their
own folder and read them with `python -I`.

## Facts that live in more than one place

Before you change a grade weight, a due date, the `webdata` install command,
or code copied from a chapter, read `docs/course-facts.md` and change every
copy in the same pull request. When a chapter changes, check the slides that
copy it.

## The week, and its lab

From week 10, Monday is a lecture, and Wednesday and Friday are one
live-coding lab, run from a notebook in `labs/week-NN/`; Friday ends with a
textbook-revision block. Students submit the chapter's Recommended Exercises
from its companion notebook. Write or change a lab by
[`labs/AUTHORING.md`](labs/AUTHORING.md): the key is the source, the
students' copy is made from it by `labs/tools/make_student_copy.py`, and the
key is run live with `labs/tools/run_key.py`. A lab sets up the Recommended
Exercises but never solves them. Its code is typed live, so keep it short and
straight-line: a function only when it's reused, never one inside another,
and no error handling, which a Discuss question names as a limitation instead
(AUTHORING's "Code style" and "Pagination"). The classroom comes before the
key's run: when a site refuses the cloud machine, flag the cell `not-run-live`
rather than add code to get past it. Commit a key before a long live run, and
give a refusing site about 30 minutes.

## Checks before class

From `slides/common/`:
- `python3 check_daily_questions.py week-NN` reports the Daily-note-questions
  frame;
- `python3 check_deck_readiness.py week-NN` reports placeholder images and the
  standing course-operations items.

CI runs both on pull requests, as information only; they never fail a build.

## Large or unclear requests

When the instructor writes "AMA", ask a short round of questions before
building, starting with the ones whose answers change the most. Otherwise make
the conventional choice and say which you made in the pull request.
