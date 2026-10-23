# After-Action Report: INFO4617-Fall2026, the live-coding lab sprint (2026-10-19 → 2026-10-22)

*Drafted 2026-10-21 and merged as #128; revised 2026-10-22 to cover #128–#135 and the measurements of all eleven restyled labs. The revision added §5.7, §5.8 and P1-3, and rewrote §7 and §9.*

## 1. Summary

In four days the course replaced its Wednesday notebook lab with live coding, at students' request. It piloted the format with week 10, then wrote conventions for it (`labs/AUTHORING.md`, two tools, and a new weekly structure in the syllabus). Eleven agents then wrote a lab for every chapter from 1 to 11. After the instructor taught week 10's lab live, the code style was rewritten, and the labs with it. Thirty-seven pull requests opened in the window (#99–#135). Thirty-six merged; #114 was closed, replaced by #134. Nothing was reverted, and the rules from the last AAR held (§2a).

The pattern that mattered most is that **the conventions were written for the key's run, not for the classroom.** The first lab conventions asked for code that survives a rate-limited cloud machine: a `get()` helper that honored `Retry-After`, `raise_for_status()` before every `.json()`, a retry rule on mwclient's session, and the chapter's helper functions copied "as they are". That code ran reliably from the cloud, but it was too long and too abstract to type in front of a class. Week 10's Step 3, a `continue` loop inside a function that called a helper, took more than 25 minutes and had to be refactored live. Every one of the eleven labs had been written to the old rules, so every one was rewritten the next day. The same lesson then came back from the other side: the new style changed how a refused request fails, and the tool that runs the keys no longer recognized it as a refusal (§5.7).

The three highest-leverage revisions:
1. **State the labs' goals and live-coding constraints at the top of `labs/AUTHORING.md`,** ahead of any mechanics, so the next rule written there is tested against the classroom first (P0-1, applied). The code-style rules themselves are now in place (#119).
2. **Check the labs mechanically.** There is no CI on `labs/`: of the four requests to merge `labs/` or `canvas/` changes "once CI passes", none could be met as asked. A small checker and workflow would also catch the style drift that remains in two labs (§5.8) and test the tools against the style (P0-2, still proposed).
3. **Make long agent runs restartable and bounded.** Agents waited without end on sites that refused them, and a container restart stopped six with their work uncommitted (P1-1, P1-2, both applied).

## 2. Scope reviewed

- **Window:** 2026-10-19 (the merge of #97) to 2026-10-22 14:47 UTC (the merge of #135): PRs #99–#135. The first draft stopped at 2026-10-21 21:59 UTC and #126.
- **Evidence:**
  - **Git:** 90 commits on `main` after #97's merge (48 not merges), +29,233/−7,012 lines summed over those 48 commits, and 17 files touched three or more times. The first draft counted 60 commits (33 not merges).
  - **Pull requests:** 37 opened, read through the GitHub tools, because `gh` isn't signed in here: 36 merged, and #114 closed unmerged.
  - **CI:** the slides and handouts workflows ran only on PRs touching `slides/` or `handouts/`. No workflow covers `labs/` or `canvas/`.
  - **Sessions:** 1 Claude Code session (this one), compacted at least nine times. At the first draft it had 81 human turns. The transcript collector counted 19 "corrections", but 17 of them are agent-completion notices it misreads as user turns. The real steering is the instructor's 20 or so requests up to the draft, and six after it, all read directly. Tool errors at the draft: 46, in 4 repeated patterns.
  - **Agents:** 23 subagent runs (11 in each wave, plus 6 restarts and 1 interrupted), seen through their final reports.
- **Earlier AAR:** `docs/aar/2026-10-16-weeks-06-09.md`.
- **Rigor:** standard. Course materials taught to a class of students, with a reviewing instructor, but no production users. Proposed tool checks are tested as far as noted.
- **Intent baseline:**
  - `AGENTS.md`;
  - `labs/AUTHORING.md`, in its first form from #102 and its revised form from #119;
  - `docs/course-facts.md`;
  - `slides/common/AUTHORING.md`;
  - the instructor's answers in three AMA rounds (2026-10-20, 2026-10-21 twice).

## 2a. Follow-up on earlier revisions

| ID | Applied? | Did the pattern recur? | Verdict |
|---|---|---|---|
| P0-1 `AGENTS.md` rules | Yes (#94) | **Rules restated by the instructor:** 0. **Rebases and force-pushes:** 0. `main` moved under an open branch five times (#117, #120, #122, an Overleaf push, and the restyled labs under #128), and `main` was merged in each time (#116, #119, #128). | Worked |
| P0-2 `docs/course-facts.md` | Yes (#94) | **Second requests to fix a copy:** 0. The weekly-structure change reached the syllabus, README, AGENTS and the slide docs in one PR (#102). Its Canvas copies were listed as "not yet changed" rather than missed. | Worked |
| P0-3 slide `AUTHORING.md` corrections | Yes (#94) | **Statements contradicted by the newest deck:** 0 found. The lab frame added to week 10 was written back into `AUTHORING.md` (#102, #119). | Worked |
| P1-1, P1-2 deck checks | Yes (#94) | `check_deck_readiness.py week-10` passed. The slides CI ran the checks as information. | Worked |
| P1-3 notebook regeneration (textbook) | Yes (textbook #264) | Not in this repo's window. Textbook #287 passed notebook sync. | Carry forward to the textbook's AAR |
| P2-1 attribution on hand-written merges | Yes (#94) | **Unattributed hand-written merges:** 0. | Worked |

## 3. What the agent was supposed to do (Q1)

- **The week** (`AGENTS.md`, "The week, and its lab", added in #102): from week 10, Monday is a lecture; Wednesday and Friday are one live-coding lab; Friday ends with a revision block; Notebook Labs grade the Recommended Exercises.
- **The lab** (`labs/AUTHORING.md`):
  - about 85 minutes of numbered steps;
  - 3–8 minute microsprints ending in a shared result;
  - collapsed Discuss boxes;
  - a reflection that maps the Recommended Exercises without solving them;
  - a revision block on Friday;
  - live data only;
  - the key as the only edited file, with the students' copy made from it.
- **The code** (`labs/AUTHORING.md`):
  - *as first written (#102):* "copy its helper functions as they are"; "honor `Retry-After`. Week 10's `get()` helper does both"; Step 0 "stops with a clear message if [a key] is missing".
  - *as revised (#119):* short, straight-line cells; a function only when reused, after its parts were shown, never nested; no error handling, acknowledged in a Discuss question; pagination in three moves.
- **Merging** (`AGENTS.md`): only when asked, after CI passes, with the full head SHA, `main` merged in if it moved, and the tree checked after.

## 4. What actually happened (Q2)

- **Day 1 (2026-10-20).**
  - Week 10 and 11 labs were written in a scratch script and run against live APIs. Wikimedia answered this machine with 429s for hours. FRED rejected a series ID that the chapter uses but FRED says doesn't exist.
  - The instructor narrowed the pilot to week 10 and asked for every request to send a policy-compliant User-Agent, then for the chapter's User-Agent to match (textbook #287).
  - To get a key that runs, the lab gained a `get()` helper with `Retry-After`, `raise_for_status()`, and a urllib3 retry rule mounted on mwclient (#99).
- **Day 2 (2026-10-21), morning.**
  - The labs moved to `labs/`, then to `labs/week-NN/`, gained Discuss boxes, and lost the outline table (#100, #101).
  - After a ten-question AMA, the new week and the lab conventions were written into the syllabus and the docs, with `make_student_copy.py` and `run_key.py` (#102).
  - Eleven agents wrote labs 1–11 in parallel worktrees.
  - Eight finished with keys run live. Three (weeks 3, 7 and 11) waited on the Wayback Machine and on FRED, which was down for maintenance, until the instructor asked to stop them and take stock. Their work was finished by hand and with cells flagged `not-run-live` (#112–#114).
  - One agent found a bug in `run_key.py`: it retried any cell whose code contained `timeout=`. The fix was pushed to #102's branch after the instructor had merged #102. It reached `main` twice, as #111 and #117.
- **Day 2, afternoon.**
  - Canvas links: written as tooling (#116), then extended by another session (#120, #122).
  - Key PDFs (#118). LuaLaTeX here lacked its font loader, and installing `texlive-luatex` fixed that.
- **Day 2, evening.**
  - After teaching week 10 live, the instructor wrote: "The code style for the labs needs to be much more concise and imperative; error handling and status checking should be minimized and acknowledged as a limitation; writing multiple functions feels out of scope; the get page revisions with continue parameter took upwards of 25 minutes and required me to refactor on the fly."
  - A four-question AMA followed, then the rules (#119) and a second wave of eleven agents.
  - A container restart stopped six of them mid-run, with their rewrites written but not committed. Their worktrees survived and they were finished by new agents.
  - The instructor asked for the rewrites to be merged as they landed, and for this AAR. The restyled labs merged as #121 and #123–#127 (weeks 2, 3, 4, 6, 8 and 9), then #129–#132 (weeks 5, 7, 10 and 1). The AAR merged as #128, with the definition-text revisions it proposed.
  - The week 1 agent found that the restyle broke `run_key.py`'s retries (§5.7). The fix, #133, merged with week 11's restyle, #134, on the instructor's "merge open PRs".
- **Day 3 (2026-10-22).**
  - On request, #114 (week 11's first-wave key, replaced by #134) was closed.
  - Week 1's key was rerun with #133: all 17 code cells ran, including the two flagged the day before, and one cell was retried twice before it got through (#135, merged on request).
- **Merges.** The instructor asked six times to merge once CI passed. Four of those covered only `labs/` or `canvas/` (#111, #103–#109, #112/#113/#115, #116), where no CI runs, and #118 was asked without the condition. Each time the agent explained, ran substitute checks, and merged. The two later requests ("merge open PRs", "merge 135") named no condition. The same substitute checks were run.
- **Tool errors:**
  - 10 edits before the file was read;
  - 4 shell-quoting failures;
  - 3 Python tracebacks in scratch scripts;
  - 2 merges refused because the expected SHA was given in short form.

## 5. Gap analysis (Q3)

### 5.1 The lab conventions served the key's run, not the classroom (severity: high)

**Observation.** All eleven first-wave labs followed the first conventions, and the conventions asked for robustness:
- week 10 had `get()` with `Retry-After`, `raise_for_status()` in every request function, and a urllib3 `Retry` on mwclient;
- week 5 wrapped requests in `get_with_backoff()`;
- week 2 had `responsible_get()` and `polite_get()`;
- week 8 had `make_options()` and three more helpers.

Each was a reasonable way to make a key run from a cloud machine that Wikimedia and others rate-limit. In class, the instructor had to type them. The 25-minute Step 3 was `get_revisions()`, a pagination loop that called `get()`, itself a loop. The second wave removed this code: weeks 2, 4, 6, 8 and 9 now average a median of six lines per code cell, have one or two functions each (each used three to thirteen times), and none handles a request's errors (§7).

**Root cause: novel, compounded by contradiction.** The first conventions had no notion of time-to-type. Worse, they *asked* for the wrapper: "copy its helper functions as they are", and "Week 10's `get()` helper does both". The constraint that mattered, that the code is typed live while 30 students follow, was known (it's why students asked for the format) but never written down, so the agent optimized for the constraint it could see: the key had to run.

**Why it matters next time.** #119 fixes the rules, but the next rule anyone adds to AUTHORING.md will again be tested against what's visible from the authoring machine. The goals have to come first in the file, and say whose time they protect.

### 5.2 No CI covers `labs/` or `canvas/`, so "merge once CI passes" can't be met (severity: medium–high)

**Observation.** Six merge requests in two days asked for CI. For four of them, covering 13 PRs that touched only `labs/` or `canvas/`, no workflow ran. Each time the agent said so and ran its own checks:
- `make_student_copy.py --check`;
- nbformat validation;
- scans for email addresses and keys;
- the tree match after merging.

Those checks caught nothing this time. They are also exactly the checks a reviewer can't see were run, and a missed one would expose a key. The style rules in #119 can't be checked by any tool yet: a reader has to grep, and a grep for `raise_for_status` flags week 8's reflection comment, which is fine.

**Root cause: missing (tool config).** `AGENTS.md` says to check CI, which assumes CI exists for every path.

### 5.3 Agents waited on refusing sites without a limit (severity: medium)

**Observation.** In the first wave, the week 3, 7 and 11 agents spent over an hour each polling the Wayback Machine and FRED. The instructor ended them ("I'm seeing the background tasks are all waiting on Wayback or FRED responses"). The second wave's prompts capped waiting at 30 minutes, and no agent hung.

**Root cause: missing.** AUTHORING.md said to flag cells a site keeps refusing, but not when to stop trying.

### 5.4 Uncommitted work at the mercy of the container (severity: medium)

**Observation.** A container restart stopped six second-wave agents. Each had a finished rewrite in its worktree, uncommitted, and was waiting on a live run. The worktrees survived, so nothing was lost, but only by luck: the rewrites existed only on that machine's disk. The restarted agents were told to commit first.

**Root cause: missing.** Nothing said to commit before a long live run.

### 5.5 Notes written before the run (severity: low–medium)

**Observation.** Three keys carried notes that didn't match their outputs:
- week 1's restyled key note said every cell ran when none had;
- week 11's held key said every cell from Step 0 to 8 ran when FRED's steps hadn't;
- textbook #287's description said mwclient's User-Agent was "seen printed" when it wasn't.

All were caught before merging, but only by reading every note against the outputs.

**Root cause: ambiguous.** AUTHORING.md says what a key note contains, not when to write it.

### 5.6 Small, mechanical repeats (severity: low)

- **Pushing to a merged PR's branch:** once, and it put the same fix on `main` twice (#111 and #117).
- **Short SHAs refused by the merge tool:** twice.
- **Editing before reading:** ten times, each harmless and corrected at once.

### 5.7 The style changed how a failure looks, and the runner kept the old idea of a refusal (severity: medium)

**Observation.** `run_key.py` retries a cell when its error looks like a rate limit. Its test matched `429` or "Too Many Requests" in the exception's text. That held under the first conventions, where `raise_for_status()` turned a 429 into an `HTTPError` naming the status. #119 removed `raise_for_status()`. Now a refused request returns the site's refusal page, and the cell fails one line later, at `.json()`, with `JSONDecodeError: Expecting value`. That message names no status, so the runner flagged those cells after one try. Three keys were run between #119 and #133 and have Wikimedia cells flagged while the runner couldn't retry them:
- week 1: 2 cells;
- week 5: Step 7's microsprint (2 cells);
- week 10: 16 cells.

The week 1 agent noticed it, and #133 added `JSONDecodeError` and "Expecting value" to the retry test. Rerun with the fix, week 1's key ran every cell (#135). Weeks 5 and 10 haven't been rerun. Their notes record refusals that lasted 12 and 30 minutes, so most of their flags are probably real. But a rerun with #133, like week 1's, may get some of those cells through.

**Root cause: missing.** Nothing tied a change to the labs' code to the tools that run it. The runner's test was written for the old style's errors. No one reread it when the style changed, and no check exercises it.

**Why it matters next time.** This is §5.1 from the other side. There, the tools' needs shaped the classroom code. Here, the classroom code changed and the tools didn't follow. Any later style change, such as dropping `.json()` for `pd.read_json()` or adding `timeout=` back, can do the same.

### 5.8 Residual drift that the prose rules didn't catch (severity: low)

**Observation.** All eleven labs on `main` were measured on 2026-10-22 (§7). Two cells sit outside "Code style":
- **Week 3, cell 24,** the key's answer to Step 4's 6-minute microsprint, has 25 lines. Most of them are a list of 13 dated events, where the prompt asks for five or more. Students are asked for less than the key shows, but anyone who falls behind and copies from the key gets the long version. The next-longest cells in any lab are 17 lines (week 6's Step 9 function, which gathers Step 8's lines) and 16 (week 10's given `get_revisions()`).
- **Week 7's `preprocess_document()`** is defined in Step 11 and called from one place, in a loop over the ten versions. "A function only when it's reused" doesn't say whether a loop counts. The function was kept because the chapter's Recommended Exercise names it.

**Root cause: ambiguous.** "About 3–8 lines" doesn't say whether a key's answer to an open-ended microsprint counts, and "reused" doesn't say whether a loop counts. Both are judgment calls, and so both belong to the instructor. Neither needs a new rule: one exception per rule across eleven labs is a good result. P0-2's warnings would put each on its pull request, where the call can be made before class.

## 6. Recommended revisions (Q4)

### [P0-1] Put the labs' goals, and who they serve, at the top of AUTHORING.md
- **Target:** `labs/AUTHORING.md`, a new "## What a lab is for" section before "## The week".
- **Root cause:** novel, compounded by contradiction (§5.1).
- **Medium:** definition text. Choosing a lab's code takes judgment, which no tool can make.
- **Evidence:** 11 of 11 labs rewritten within a day; Step 3 took over 25 minutes live.
- **Change:** add, after the opening paragraph:
  > ## What a lab is for
  >
  > Students asked to code *with* the instructor rather than work through a chapter's notebook alone. A lab is the script for that session, so it serves the person typing at the front of the room and the 30 people typing along, in that order:
  > - **Teach the chapter's core idea in about 85 minutes of typing,** on the chapter's own case, so the Recommended Exercises are within reach. Coverage is the chapter's job.
  > - **Keep everyone typing.** Short, plain cells mean a student who falls behind can catch up from the key in seconds.
  > - **Make room to think.** Microsprints and Discuss boxes are where students do and say something themselves. The code is short so that they have time.
  > - **Run honestly.** Every request is live, and a failure is something to discuss, not to hide behind a wrapper.
  >
  > When a rule here conflicts with getting the key to run from a cloud machine, the classroom wins: flag the cell `not-run-live`, and leave the code plain.
- **Why it works:** an agent reading the file meets the classroom's constraints before any mechanics. A future convention that would add code to make the key run, as `get()` did, now visibly conflicts with a stated goal.
- **Owner:** maintainer review.
- **Status:** Applied 2026-10-21 (#128).

### [P0-2] Check every lab with a script, and run it in CI
- **Target:** new `labs/tools/check_lab.py`, and new `.github/workflows/check-labs.yml`, on pull requests touching `labs/**`.
- **Root cause:** missing (§5.2), plus a prose rule a program can check (§5.1).
- **Medium:** tool config.
- **Evidence:** four "once CI passes" merge requests, covering 13 PRs on paths with no CI; each needed substitute checks run by hand.
- **Change:** a checker, standard library and nbformat only, that for each `labs/week-*/lab-*-key.ipynb`:
  - fails if `make_student_copy.py --check` fails;
  - fails if any notebook or PDF text contains an email address other than `your-email@colorado.edu`;
  - fails if a key note holds a placeholder (`PLACEHOLDER`, `to be written`);
  - fails if a cell is tagged `not-run-live` but the key note doesn't say "not run" or `not-run-live`;
  - fails if `run_key.py`'s retry test doesn't match a sample of each way a refused request fails in the current style (an `HTTPError` naming 429, and a `JSONDecodeError` "Expecting value"). The samples sit beside the style rules, so changing one is a reminder to check the other (§5.7);
  - warns, without failing, using Python's `ast` so that comments don't count:
    - `raise_for_status`, `try`, `timeout=`, or a retry adapter in code;
    - a function defined inside another;
    - a function called fewer than twice;
    - a code cell over 12 lines.

  The workflow installs `nbformat` and runs it. AGENTS.md's merge rule then names it: "CI for `labs/` is `check-labs`."
- **Why it works:** "merge once CI passes" becomes a real gate for labs. The checks that protect students (no keys, no real email, a student copy that matches its key) stop depending on someone remembering them. The style warnings show drift on the PR instead of in class.
- **Owner:** maintainer review. The tool isn't written yet, so this is a design, untested.
- **Status:** Proposed. Not built as of 2026-10-22.

### [P1-1] Bound every live run, and commit before it
- **Target:** `labs/AUTHORING.md`, "The key", and `AGENTS.md`, "The week, and its lab".
- **Root cause:** missing (§5.3, §5.4).
- **Medium:** definition text.
- **Evidence:** three first-wave agents waited over an hour and had to be stopped; six second-wave agents were stopped with uncommitted rewrites.
- **Change:** in AUTHORING.md, "The key", add:
  > Commit the key before you run it: a live run can take an hour, and a restart takes uncommitted work with it. Give a refusing site about 30 minutes in all (`run_key.py --retries 2 --wait 60`), then accept the `not-run-live` cells and move on. The instructor's laptop is a better place to run them than a cloud machine that sites rate-limit.
- **Why it works:** it turns two judgment calls that agents made badly, how long to wait and when to save, into defaults. The second wave, given these two lines in its prompts, neither hung nor needed more than a restart.
- **Owner:** auto-applyable.
- **Status:** Applied 2026-10-21 (#128).

### [P1-2] Write the key note last, from run_key's report
- **Target:** `labs/AUTHORING.md`, "The key".
- **Root cause:** ambiguous (§5.5).
- **Medium:** definition text, backed by P0-2's placeholder check.
- **Evidence:** three notes that described a run that hadn't happened.
- **Change:** in "The key", after the list of what the note says, add:
  > Write it last: after `run_key.py` finishes, from its report of which cells ran. Until then, leave the word `PLACEHOLDER`, which `check_lab.py` refuses.
- **Why it works:** the note describes what happened rather than what was planned.
- **Owner:** auto-applyable.
- **Status:** Applied 2026-10-21 (#128); the placeholder check waits on P0-2.

### [P1-3] Retry the refusals the new style produces, and say where the retry test lives
- **Target:** `labs/tools/run_key.py`, its `TRANSIENT` pattern; `labs/AUTHORING.md`, "Code style" and "The key".
- **Root cause:** missing (§5.7).
- **Medium:** tool config, with one line of definition text pointing at it until P0-2 can test it.
- **Evidence:** 20 cells, in weeks 1, 5 and 10, flagged after a single try. Week 1's two cells ran when rerun with the fix (#135).
- **Change:** in `run_key.py`, add `JSONDecodeError` and "Expecting value" to `TRANSIENT`, with a comment saying why (#133). In AUTHORING.md, at the end of "Code style", add:
  > `tools/run_key.py` decides whether to retry a cell from the error the cell raises, and that depends on this style: with no `raise_for_status()`, a 429 usually surfaces at `.json()`, as a `JSONDecodeError`. A change to these rules that changes how a refused request fails needs the same change to its `TRANSIENT` pattern, in the same pull request.
- **Why it works:** the runner gives a rate-limited cell its retries again. The sentence puts the dependency where the next person to change the style will read it, not only in the tool.
- **Owner:** auto-applyable.
- **Status:** Tool change applied 2026-10-21 (#133), and AUTHORING.md text applied 2026-10-22. Weeks 5 and 10 not yet rerun.

### [P2-1] Two lines for merging
- **Target:** `AGENTS.md`, "Merging" and "Branches and pull requests".
- **Root cause:** missing (§5.6).
- **Medium:** definition text.
- **Change:** in "Merging", change "with a merge commit and the expected head SHA" to "with a merge commit and the expected head SHA, all 40 characters". In "Branches and pull requests", add:
  > Before pushing to an existing pull request's branch, check that the pull request is still open. If it was merged, start a new branch from `main` for the follow-up.
- **Why it works:** it prevents the stranded fix (#111 and #117) and the refused merges.
- **Owner:** auto-applyable.
- **Status:** Applied 2026-10-21 (#128).

## 7. Strengths to sustain

- **AMA before building.** Three rounds settled the format before any build:
  - the grading change;
  - one lab across both days;
  - microsprints that never solve a Recommended Exercise;
  - the Discuss boxes;
  - three-move pagination.

  None of those was reversed. Only the code style was, and it was the one thing the AMA didn't ask about.
- **The key is the source.** `make_student_copy.py` reproduced the week 10 and 11 student copies exactly. Across 22 agent runs, no student copy drifted from its key.
- **Secrets never reached the repo.** An early FRED error printed the API key in a URL. The executed copy stayed in scratch, and `run_key.py` now refuses to write such a notebook.
- **Parallel agents without conflicts.** One folder per week let eleven agents work at once with no merge conflict between them.
- **Agents reported, not just delivered.** They found textbook bugs, among them:
  - chapter 6 scrapes two sites whose `robots.txt` disallows it;
  - chapter 11's FRED series doesn't exist;
  - chapter 9's outputs no longer reproduce.

  Agents also found two bugs in `run_key.py`: the `timeout=` misfire (#111) and the retries the restyle broke (#133).
- **The second wave kept to the style.** All eleven labs on `main` were measured on 2026-10-22. Each has 8–13 steps, 5–6 microsprints, and 83–85 minutes of planned time. Each has 17–28 code cells, except week 9 with 42 short ones. The median code cell is 5–7 lines. In nine of the eleven, the longest cell the class types is 9–11 lines. Week 6's is a 17-line function that gathers Step 8's lines, and week 3's is in §5.8. A lab has zero to three functions; weeks 3 and 5 needed none. Only two `try` blocks are left, each where the failure is the step's subject: week 4's broken-JSON microsprint and week 3's dead endpoints. The two exceptions to the rules are in §5.8.
- **Agents picked up where stopped ones left off.** After the restart, six new agents resumed from the old worktrees, committed first, and finished. None started over.
- **The last AAR's rules held,** across 37 PRs (§2a).

## 8. Revision actions — tracking table

| ID | Priority | Target | Medium | Change | Owner | Status | Evidence to check next time |
|---|---|---|---|---|---|---|---|
| P0-1 | P0 | `labs/AUTHORING.md` | definition text | "What a lab is for" first: who a lab serves, and the classroom over the cloud run | maintainer review | Applied 2026-10-21 (#128) | Labs rewritten after being taught, for style: 11 → 0 |
| P0-2 | P0 | `labs/tools/check_lab.py`, `.github/workflows/check-labs.yml` | tool config | Check keys, student copies, secrets, notes, style, and `run_key.py`'s retry test on every lab PR | maintainer review (untested design) | Proposed | Merge requests on `labs/` with no CI to wait for: 4 → 0; style exceptions found in class rather than on the PR: 2 → 0 |
| P1-1 | P1 | `labs/AUTHORING.md`, `AGENTS.md` | definition text | Commit before a live run; give a refusing site about 30 minutes | auto-applyable | Applied 2026-10-21 (#128) | Agents stopped by hand while waiting: 3 → 0; uncommitted work at a restart: 6 → 0 |
| P1-2 | P1 | `labs/AUTHORING.md` | definition text | Write the key note last, from `run_key.py`'s report | auto-applyable | Applied 2026-10-21 (#128; the placeholder check waits on P0-2) | Key notes that misdescribe the run: 3 → 0 |
| P1-3 | P1 | `labs/tools/run_key.py`, `labs/AUTHORING.md` | tool config, definition text | Retry a 429 that surfaces as a `JSONDecodeError`; tie the retry test to the style rules | auto-applyable | Tool applied 2026-10-21 (#133); text applied 2026-10-22 | Cells flagged after a single try on a rate limit: 20 → 0 |
| P2-1 | P2 | `AGENTS.md` | definition text | Full 40-character SHA; check a PR is open before pushing to its branch | auto-applyable | Applied 2026-10-21 (#128) | Refused merges: 2 → 0; fixes merged twice: 1 → 0 |

## 9. Resolution (updated 2026-10-22)

**Applied.**
- **#128 (2026-10-21)** applied the definition-text revisions:
  - **P0-1:** `labs/AUTHORING.md` opens with "What a lab is for".
  - **P1-1 and P1-2:** in "The key", commit before a live run, give a refusing site about 30 minutes, run flagged cells from a laptop, and write the note last. `AGENTS.md` repeats the first two.
  - **P2-1:** `AGENTS.md` asks for the full 40-character SHA, and a check that a pull request is still open before pushing to its branch.
  - The instructor also asked for the labs' common style, goals and implementation to be documented. So AUTHORING.md gained:
    - when a `try` is allowed;
    - a yardstick measured on the restyled labs;
    - a "How the pieces fit" section: one source, where students find a lab, one folder per week, and what the machine needs.
- **#133 (2026-10-21)** applied P1-3's tool change.
- **The 2026-10-22 revision** (this pull request):
  - added §5.7, §5.8 and P1-3 to this report;
  - added P1-3's sentence to AUTHORING.md;
  - re-measured AUTHORING.md's yardstick on all eleven labs;
  - in "The key", stated that the 30 minutes covers the whole run, not each cell;
  - told students, in `labs/README.md`, why some cells in a key have no output.

**Not applied.** P0-2, the checker and its workflow, is still a design. Until it exists, "merge once CI passes" can't be met for `labs/` or `canvas/`, and the substitute checks in §5.2 are run by hand.

**On `main`.** Eleven restyled labs, each with a key, a students' copy and a key PDF. Week 11's first-wave key (#114) was closed unmerged.

**Still to run from the instructor's laptop** (49 cells, each tagged `not-run-live` in its key):
- week 5: both cells of Step 7's microsprint (Step 10 ran, but its outputs show 429s, so it's worth rerunning too);
- week 7: 21 cells (the Wayback Machine refused the cloud machine);
- week 8: 1 cell, Step 10's Playwright run (no browser to match the library's version);
- week 10: 16 cells (Wikimedia 429s);
- week 11: 9 FRED cells, once FRED is back.

Weeks 5 and 10 were flagged before #133 (§5.7). A rerun from the cloud machine with the fix costs about 30 minutes each, and may clear some of their cells before class, as it did for week 1. Week 1 has nothing left to run (#135).

**Open choices for the instructor**, which the report leaves alone:
- week 3's 25-line microsprint answer: keep it, or cut the key's list to the five or more events the prompt asks for (§5.8);
- week 7's `preprocess_document()`, called from one place: keep it for the Recommended Exercise that names it, or inline it (§5.8);
- Canvas:
  - `canvas/migrate.py labs --apply` hasn't been run from this session. #120 and #122, from another session, may already cover it.
  - `canvas/course_spec.py` still describes a Wednesday notebook lab and a Friday revision workshop in its week modules and its `GROUPS` blurbs. `docs/course-facts.md` lists it as "Not yet changed", so it's known, not missed.
