# Run-of-show: the backlog standup, Friday, October 2

The first Friday standup from the
[code-review plan](2026-09-24-friday-code-review.md), run as the instructor
decided on October 1:

- 20–30 students, paired by chapter;
- a 15-minute standup, then 35 minutes of pair work;
- pairs record everything on GitHub;
- the instructor merges after class;
- a rule blocks commits straight to `main`.

On October 2 the instructor narrowed the pair work to three named activities,
for this Friday and later ones. Each has a step-by-step handout with
screenshots, in [`handouts/week-07/`](../../handouts/week-07/):

| Activity | Difficulty | Handout |
|---|---|---|
| Triage an issue | easy | `triage-an-issue.md` |
| Review a pull request | medium | `review-a-pull-request.md` |
| Issue to pull request | hard | `issue-to-pull-request.md` |

Students don't resolve conflicts, merge, or close anything: the instructor
does all three after class.

The slides are week 7's Friday section, from "Daily note questions" to "After
class". Each chapter's board lists that chapter's work in three columns, one
per activity, with the instructor's items marked "For me". The counts and
boards were checked on October 2: 51 open pull requests from students and
the instructor, plus the instructor's #194, and 53 open issues on the
textbook.

## Before class (about 20 minutes)

1. **Textbook #193 is merged** (October 2, with a merge commit). It reverted
   the two commits made straight to `main` on September 25: a Scapy note in
   chapter 5 and a caching tip in chapter 6. Before it merged, every pull
   request's Notebook sync failed, because `main`'s chapter 5 and 6 notebooks
   didn't match their chapters.
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
5. **Fill in the daily note frame.** Friday starts with an empty "Daily note
   questions" frame. `check_daily_questions.py` flags it until it has
   questions.
6. **Optional: capture the signed-in screens.** The handouts reuse week 4's
   four web-editor screenshots, with numbered markers. Seven more screens
   appear only to a signed-in user; `handouts/week-07/img/IMAGES.md` lists
   them, and each handout marks the place for one with a comment.

## In class (50 minutes)

| Minutes | Slide | What happens |
|---|---|---|
| 0–4 | Daily note questions, Find your chapter | Students sit with the chapter of their newest open pull request or issue. Anyone with nothing open joins chapter 2 or 3. Balance the groups against the Pairs column, then pair up within each chapter. |
| 4–6 | Three activities | Name the three activities and their handouts. Each pair picks one. |
| 6–15 | The standup | One minute per pair, in chapter order: 2, 3, 4, 5, 6, then 1, 7, and 11. Each pair says Done, Doing (its activity and 2–4 numbers from its board), and Blocked. Write the Blocked items on the board. |
| 15–48 | The chapter boards | Pairs work from the handouts. Leave the chapter boards up, cycling through them. Go to the Blocked items first. |
| 48–50 | After class | What happens next. |

**Where to go first while pairs work:**

- **Conflicts with `main`**, which are yours to resolve (the boards list them
  as "For me"):
  - #52 (chapter 1);
  - #88, #89, and #93 (chapter 4);
  - #102 (chapter 4, and it also edits chapter 6).
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
  changes were still on `main`. Now that #193 has merged, those notebooks need
  regenerating again.
- **#194** (yours, opened October 2) replaces Scapy in chapter 5 with terminal
  commands run from the notebook, and puts every library the chapters import
  into chapter 1's `webdata`. #106 and #112 edit the Scapy text it removes, so
  they conflict with it; #111 adds a note about Scapy; and #180's chapter 5
  notebook conflicts with it too.
- **#86** (chapter 4, Step 5) sends students to Open-Meteo, whose robots.txt
  disallows every path. Raise in its review whether the step should say why an
  API client may still call it (chapter 2's distinction).
- **Triage questions on the boards.** A line like `#15 → #59?` asks whether
  pull request #59 fixes issue #15. Those pairs come from the issues' and pull
  requests' texts; a triage pair confirms each one in a comment.

**Things to watch for:**

- **"Commit directly to the main branch"** in the browser editor. The rule
  refuses it; the editor then offers a new branch.
- **A student clicking Merge.** The slides say not to. Only the Code Owners
  setting in step 2 prevents it.
- **Pairs pushing to someone else's branch.** Only the author can push to a
  pull request from a fork, so a pair without its author comments instead.

## After class

1. **Merge the approved pull requests** with merge commits. Where two change
   the same lines, merge one. Then resolve the other's conflict yourself, or
   close it with thanks.
2. **Resolve the conflicts** on the "For me" list: merge `main` into each
   branch, in GitHub's conflict editor, with no force-push. A branch on a fork
   needs its author, or "Allow edits by maintainers".
3. **Regenerate the notebooks once.** With the rule on, this goes through a
   pull request: run `python tools/make_notebooks.py` on a branch, then merge
   the result.
4. **Close issues:**
   - the ones a merged pull request fixed without naming them;
   - the duplicates the triage pairs found (their comments say
     `Duplicate of #N`).
5. **Credit for reviews.** A pair submits one review, and the submitting
   partner names the other with `@handle`. Decide whether a pair's review
   counts toward both partners' "Reviews".
6. **Update the textbook's `docs/handoff.md`:** what merged, what is pending,
   and whether there is another standup.
