# Plan: a Friday code-review standup for students' pull requests

**Status:** Proposed on 2026-09-24. It carries out the maintainer's decision
that students' pull requests on the textbook merge after a code-review
standup in class on a Friday (the textbook's
[`docs/decisions.md`](https://github.com/cuinfoscience/Web-Data-Science-Book/blob/main/docs/decisions.md),
2026-09-24). The date of the first session is the instructor's call.

## 1. Goal

Review the open student pull requests on the textbook together, in class,
and merge the approved ones there:

- the backlog gets decided: about 40 are open, the oldest from August 28;
- students practice the review that the revision framework grades
  ("Reviews": specific, kind, must-fix apart from nice-to-have, a clear
  verdict);
- everyone sees what a merge does: the book republishes, and the issue
  closes.

## 2. When

- **Proposed: week 7's Friday, October 2**, the first Friday after this plan
  (week 6 is left as it is). Or a later Friday the instructor picks.
- After that, a short standup on later Fridays, as often as the backlog
  needs.
- The week's deck gets a frame for the session once the date is set.

## 3. Before class

Prepare a review table: one row per open student pull request, grouped by
chapter.

| PR | Author | Chapter and section | Issue it fixes | Checks (Render, Notebook sync) | Conflicts with `main`? | Overlaps with | Suggested verdict |
|---|---|---|---|---|---|---|---|

What was known on 2026-09-24:

- **Conflicts with `main`**, since textbook #149 and #152 merged: #52
  (chapter 1), and #88, #89, and #93 (chapter 4).
- **Overlaps:** #88 and #93 make the same change, a User-Agent on chapter
  4's requests. #50 and #79 both revise the description of Reddit's
  robots.txt (issue #43).
- **Pull requests that fix an issue without naming it** are linked from the
  issue: #120←#121, #105←#106, #18←#54, #17←#56, #43←#79, #60←#80,
  #68←#95. #92 names its issue, #90.
- **Pull requests made in the browser** fail Notebook sync. After merging
  them, the instructor regenerates the notebooks, as the textbook's
  `CONTRIBUTING.md` describes, unless the Notebook sync decision in its
  hand-off note changes that.
- **#62** puts "Python Version 3.11.9" in chapter 3's generated notebook
  title. The next regeneration overwrites it, and the book now recommends
  Python 3.14.

An agent can build the table the day before without touching any student's
branch. It lists the open pull requests, fetches each one's head read-only
(`refs/pull/N/head`), test-merges it against `main` in a scratch worktree,
and reads its checks. It doesn't comment on, edit, or merge a student's pull
request.

Share the table before class, so that authors can prepare and each student
knows which two pull requests to review.

## 4. In class (about 50 minutes)

1. **How to review (5 minutes).** The pull request template's parts
   (location, problem, why, change). A review says what must change and what
   would be nice, and ends with a verdict: approve, request changes, or
   close.
2. **The standup (about 30 minutes)**, in chapter order. For each pull
   request:
   - the author says what it fixes and where, in a sentence or two;
   - an assigned reviewer gives a verdict, with at most two points;
   - the instructor decides: merge now, changes needed (the author pushes to
     the same branch), or close with thanks (a duplicate, or out of scope).

   For a duplicate, the class keeps one; the other author reviews it, which
   counts as a review.
3. **Resolve one conflict live (10 minutes).** Take a conflicting pull
   request, such as #89, and resolve it with its author in GitHub's conflict
   editor. Everyone sees how `main` moved under the branch, and how to catch
   up: merge `main` into the branch, and never force-push.
4. **Merge and watch (5 minutes).** Merge the approved pull requests with
   merge commits, watch the book's publish run, reload a chapter, and see
   the issue close.

## 5. After class

- If browser-made pull requests merged, regenerate the notebooks on `main`
  once (`python tools/make_notebooks.py`) and commit.
- Re-run the render and `tools/shots/run check`, and fix anything the merges
  broke.
- Close issues that a merged pull request fixed without naming.
- Update the textbook's `docs/handoff.md`: what merged, what is pending, and
  the date of the next standup.

## 6. Grading

Presenting and reviewing at the standup can count toward the revision
framework's "Reviews" criterion. Its rule stands: students are graded on the
proposal and the review, not on whether the pull request merges.

## 7. Questions for the instructor

- Which Friday, and how much of the session.
- Whether reviewers are assigned beforehand, two pull requests each.
- Whether pull requests made in the browser merge before the Notebook sync
  decision, with the notebooks regenerated afterwards.
