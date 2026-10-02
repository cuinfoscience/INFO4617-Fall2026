# Run-of-show: the code-review standup, Friday, October 2

The first Friday standup from the
[code-review plan](2026-09-24-friday-code-review.md), run as the instructor
decided on October 1:

- 20–30 students, paired by chapter;
- a 15-minute standup, then 35 minutes of pair work;
- pairs record everything on GitHub;
- the instructor merges after class;
- a rule blocks commits straight to `main`.

The slides are week 7's Friday section, from "Find your chapter" to "After
class". The counts on them were taken on October 1: 51 open pull requests and
53 open issues on the textbook.

## Before class (about 20 minutes)

1. **Merge textbook #193** with a merge commit. It reverts the two commits made
   straight to `main` on September 25: a Scapy note in chapter 5 and a caching
   tip in chapter 6. Until it merges, every pull request's Notebook sync fails,
   because `main`'s chapter 5 and 6 notebooks don't match their chapters.
2. **Turn on the rule.** In the textbook repository, go to Settings, then
   Rules, then Rulesets, then New branch ruleset:
   - name it `main`, set Enforcement to Active, and target the default branch;
   - turn on "Restrict deletions", "Require a pull request before merging",
     and "Block force pushes";
   - add Repository admin to the bypass list, so you can still merge.

   This blocks direct commits, but anyone with write access can still click
   **Merge** on an open pull request. To block that too, set "Required
   approvals" to 1 and turn on "Require review from Code Owners". That also
   needs a `.github/CODEOWNERS` file containing `* @brianckeegan`.
3. **Close #171.** Its head is `main` and its base is the branch made for issue
   #170, so it can't put anything through review. When you close it, point its
   author to that branch for the caching tip.
4. **Optional: approve the forks' check runs.** GitHub waits for a maintainer
   before running checks on pull requests from some forks: in the Actions tab,
   **Approve and run** each one. Reviewers read the Markdown either way.
5. **Optional: answer the daily note.** `check_daily_questions.py` reports that
   week 7 has no "Daily note questions" frame. Add one if this week's notes
   asked anything.

## In class (50 minutes)

| Minutes | Slide | What happens |
|---|---|---|
| 0–4 | Find your chapter | Students sit with the chapter of their newest open pull request or issue. Anyone with nothing open joins chapter 2 or 3. Balance the groups against the Pairs column, then pair up within each chapter. |
| 4–15 | The standup | One minute per pair, in chapter order: 2, 3, 4, 5, 6, then 1, 7, and 11. Each pair says Done, Doing (2–4 numbers from its board, and a job), and Blocked. Write the Blocked items on the board. |
| 15–48 | The four job slides, then the chapter boards | Pairs work. Leave the chapter boards up, cycling through them. Go to the Blocked items first, then the conflicts and duplicates. |
| 48–50 | After class | What happens next. |

**Where to go first while pairs work:**

- **Conflicts with `main`:**
  - #52 (chapter 1);
  - #88, #89, and #93 (chapter 4);
  - #102 (chapter 4, and it also edits chapter 6).

  Only an author can push to a pull request from a fork. If the author is
  absent, the pair comments instead.
- **Duplicates and overlaps:**
  - #88 and #93 make the same change, a User-Agent on chapter 4's requests.
  - #130 and #188 make the same fix, Wikipedia's 403 in chapter 6, Strategy 3.
  - #50 (yours) and #79 change the same paragraph about Reddit's robots.txt.
  - #92 and #99 change neighboring rows of chapter 4's table.
  - #113 and #127 change the same steps in chapter 5's exercises.
  - #191 and #192 (chapter 7) both handle the Availability API's refusals.
    On September 30 that API answered 429 to every request, so neither one
    gets the notebook working.
- **Pull requests that edit only a generated notebook:** #62 (chapter 3),
  #108 (chapter 5), and #182 (chapter 6). The next regeneration overwrites
  them.
- **#180** regenerated the chapter 5 and 6 notebooks while the reverted
  changes were still on `main`. After #193 merges, those notebooks need
  regenerating again.
- **#86** (chapter 4, Step 5) sends students to Open-Meteo, whose robots.txt
  disallows every path. Raise in its review whether the step should say why an
  API client may still call it (chapter 2's distinction).

**Things to watch for:**

- **"Commit directly to the main branch"** in the browser editor. The rule
  refuses it; the editor then offers a new branch.
- **A student clicking Merge.** The slides say not to. Only the Code Owners
  setting in step 2 prevents it.
- **Pairs pushing to someone else's branch.** Only the author can push to a
  pull request from a fork, so a pair without its author comments instead.

## After class

1. **Merge the approved pull requests** with merge commits. Where two change
   the same lines, merge one; the other then conflicts, and its author resolves
   it next time.
2. **Regenerate the notebooks once.** With the rule on, this goes through a
   pull request: run `python tools/make_notebooks.py` on a branch, then merge
   the result.
3. **Close issues:**
   - the ones a merged pull request fixed without naming them;
   - the duplicates the triage pairs found (their comments say
     `Duplicate of #N`).
4. **Credit for reviews.** A pair submits one review, and the submitting
   partner names the other with `@handle`. Decide whether a pair's review
   counts toward both partners' "Reviews".
5. **Update the textbook's `docs/handoff.md`:** what merged, what is pending,
   and whether there is another standup.
