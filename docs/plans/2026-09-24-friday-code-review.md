# Plan: a Friday code-review standup for students' pull requests

**Status:** Scheduled. The first standup is week 7's Friday, October 2, as
the instructor decided on 2026-09-25. Its review table is ready:
[`2026-09-24-friday-code-review-table.md`](2026-09-24-friday-code-review-table.md).
The plan was proposed on 2026-09-24. It carries out the maintainer's decision
that students' pull requests on the textbook merge after a code-review standup
in class on a Friday (the textbook's
[`docs/decisions.md`](https://github.com/cuinfoscience/Web-Data-Science-Book/blob/main/docs/decisions.md),
2026-09-24).

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

- **Week 7's Friday, October 2** (decided 2026-09-25), the first Friday after
  this plan. Week 6 is left as it is. The standup takes that Friday's
  textbook-revisions session.
- After that, a short standup on later Fridays, as often as the backlog
  needs.
- Week 7's deck carries the session. Its Friday frames are built from the
  review table (§4, "Slides").

## 3. Before class

Prepare a review table: one row per open student pull request, grouped by
chapter. The table for October 2 is
[`2026-09-24-friday-code-review-table.md`](2026-09-24-friday-code-review-table.md),
built on 2026-09-24. Pull requests open and change during the week, so rebuild
it on Thursday, October 1. The shared copy leaves out the suggested verdicts,
which stay with the instructor.

| PR | Author | Chapter and section | Issue it fixes | Checks (Render, Notebook sync) | Conflicts with `main`? | Overlaps with | Suggested verdict |
|---|---|---|---|---|---|---|---|

What the table showed on 2026-09-24:

- **Conflicts with `main`**, since textbook #149 and #152 merged: #52
  (chapter 1), and #88, #89, and #93 (chapter 4).
- **Overlaps:**
  - #88 and #93 make the same change, a User-Agent on chapter 4's requests.
  - #50 and #79 both revise the description of Reddit's robots.txt (issue
    #43).
  - #92 and #99 edit adjacent rows of chapter 4's starter-feeds table.
  - #113 and #127 rewrite the same step of chapter 5's exercises.

  Each pull request in a pair merges on its own, but the second conflicts
  once the first is in.
- **Checks.** GitHub hadn't run the checks on 23 pull requests from forks. It
  waits for a maintainer to approve each run, so approve them before class
  and the results will show on GitHub. The table's checks were run locally.
  Every pull request that merges cleanly renders, and all of them but #113
  fail Notebook sync.
- **Some changes pass both checks and still render wrongly.** A heading or a
  callout that loses the blank line above it becomes plain text. A link with a
  space before its parenthesis shows its brackets. Neither check catches
  these, so a review has to read the Markdown itself.
- **Pull requests that fix an issue without naming it** are linked from the
  issue: #120←#121, #105←#106, #18←#54, #17←#56, #43←#79, #60←#80,
  #68←#95. #92 names its issue, #90.
- **Pull requests made in the browser** fail Notebook sync. After merging
  them, the instructor regenerates the notebooks, as the textbook's
  `CONTRIBUTING.md` describes, unless the Notebook sync decision in its
  hand-off note changes that.
- **#62 and #108 edit only generated notebooks.**
  - #62 puts "Python Version 3.11.9" in chapter 3's notebook title, and the
    book now recommends Python 3.14.
  - #108 adds a section on query parameters to chapter 5's notebook.

  The next regeneration overwrites both.

An agent can build the table the day before without touching any student's
branch. It lists the open pull requests and fetches each one's head read-only
(`refs/pull/N/head`). It test-merges each against `main` in a scratch
worktree and reads its checks, or runs them there when GitHub hasn't. It
doesn't comment on, edit, or merge a student's pull request. The table's "How
it was built" section lists the steps.

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

**Slides.** Week 7's deck carries the session, in the Friday section that now
covers textbook revisions. Build its frames from the table rebuilt on
October 1:

- **This week at a glance.** Friday's band becomes the code-review standup.
- **How to review (step 1).** The three verdicts and the limit of two points.
  The deck's "A good revision, and a good review" frame has most of it. Add
  that a review reads the Markdown, since the checks miss some rendering
  errors (§3).
- **The standup order (step 2).** The table's pull request numbers by chapter,
  with each overlapping pair side by side. Use one frame, or one per chapter
  if they don't fit.
- **One conflict, live (step 3).** #89 conflicts with `main`. Merge `main` into
  its branch in GitHub's conflict editor, with no force-push.
- **Merge and watch (step 4).** The publish run, and an issue closing.

Keep the chapter 7 revision menu for the next round of pull requests.

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

- How much of week 7's Friday the standup takes. The date is decided:
  October 2.
- Whether reviewers are assigned beforehand, two pull requests each.
- Whether pull requests made in the browser merge before the Notebook sync
  decision, with the notebooks regenerated afterwards.
- Whether merges wait for the standup. Students who can push branches to the
  textbook can also merge, and one merged #117 on 2026-09-24, before any
  review. A branch-protection rule on the textbook's `main` would make the
  standup the merge point, for example one that requires the maintainer's
  review.
