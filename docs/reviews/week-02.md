# Review: week 02, Ethics, Law, and Responsible Data Collection

**What was reviewed:** week 2's lab (`labs/week-02/lab-02.ipynb`, with its key `lab-02-key.ipynb` and the saved checkpoints in `labs/week-02/data/`), its deck (`slides/week-02/week-02.tex`) and chapter 2's Recommended Exercises, as students meet them.
- **Course repository:** the head of pull request #214, `1c5971600ce0d39960684e0d3ec57c5f6ea27d74`, which rebuilt week 2's lab and deck in the incremental style. It is open and not merged. Per `docs/course-facts.md` ("Week 2's lab, for the next offering"), the rebuilt lab is for the course's next offering: Wednesday is Steps 0–5 in about 50 minutes, Friday Steps 6–10 in about 35, then the 15-minute revision block.
- **Textbook:** `ch-02-ethics.qmd` and its companion notebook, `notebooks/ch-02-ethics.ipynb`, at `main`, `3f9cf2cef801181236c9cceaf71f3b63c3ad2491`.

**When:** 2026-11-18.

**Method:** five anonymous composite personas, each a kind of student this course has, reviewed the week independently. Each read the chapter and the slides, typed and ran its own code for every lab step it could from the students' copy, made the mistakes its background makes, attempted the Recommended Exercises, and opened the key only after an honest try. Each review is a **steel man**: it first makes the strongest case for the materials as designed, and only then says where they fall short for that student. Reviewers were told to respect `robots.txt`: the three cells the key tags `not-run-live` (Step 8's requests to the Times's pages) were to be read, not sent. This document puts the five together. Every ranked finding was then checked against the repository and the textbook, and is marked **verified** (with how) or **reported, not verified**.

**One request that shouldn't have gone out.** Persona A's runner executed A's own typed versions of cells 71 and 74, so one request went to the Times's technology section. It answered 403, from DataDome. A disclosed this in its review, and its saved run confirms one request (cell 74 reuses cell 71's response) and no others; A's given loop (cell 72) was commented out. The other four personas executed none of the three cells.

## Who reviewed

| | Degree and major | Python and data background | Interest | Skill |
|---|---|---|---|---|
| A | BS senior, Information Science | One intro Python course; spreadsheets | Qualitative and design: online communities, UX | Minimal |
| B | BA junior, Journalism and Communication | No Python before this course; strong with public records and Excel | Data journalism, local government | Minimal |
| C | BS senior, Business Analytics | Excel, some SQL, a little pandas | Quantitative analytics: markets, customer data, dashboards | Minimal to moderate |
| D | MS first year, Data Science (BA in Statistics) | Fluent in R, moderate pandas; regression and sampling | Quantitative: measurement and validity | Moderate |
| E | MS first year, Information Science (BS in Computer Science) | Moderate Python, git; little data analysis | Design and tools: automation, APIs, building things | Moderate |

## What each completed

The lab has Steps 0–10 and seven microsprints: Part 1 (Wednesday) is Steps 0–5, with microsprints in Steps 1, 2 and 4; Part 2 (Friday) is Steps 6–10, with microsprints in Steps 6, 7, 8 and 9, then the revision block. No persona sent Step 8's three `not-run-live` cells (71, 72, 74) except A's one accidental request (above), so Step 8's microsprint and the last question of Step 10 were read, not done, by all five. All five loaded Part 2's checkpoint from a local copy, because its address returns 404 until #214 is merged (item 1).

| | Lab steps finished | Read, not done | Recommended Exercises |
|---|---|---|---|
| A | 0–5 (twice); 6, 7, 8's first cell; 9's five comment lines; microsprints in Steps 1, 2, 4, 6, 7 | Step 9's dating-app microsprint, 10, the revision block | Steps 1–6 |
| B | 0–5 with all three microsprints; 6, 7, 9; 8's first cell | 10, the revision block | Steps 1–5; Step 6 in rough form |
| C | 0–9, with every microsprint it could run; 10 answered from its own outputs | Step 8's request cells and microsprint | Steps 1–6 |
| D | 0–5; 6, 7, 9; 8's first cell | 10, the revision block | Steps 1–5; Step 6 drafted, not written |
| E | 0–5 with all three microsprints; 6, 7, 9, 10; 8's first cell | Step 8's request cells and microsprint; Discuss boxes read, not answered | Steps 1–6 |

No persona reports needing the key to finish a step. B and E compared their outputs with it afterwards.

**Estimated time for a real student of that background, in minutes** (the lab's own minutes in the last row; by `labs/AUTHORING.md`, a step's minutes include its microsprint and discussion):

| | Part 1 (Wednesday) | Part 2 (Friday) | Exercises |
|---|---|---|---|
| A | 75 | 55, plus 15 for the revision issue | 100, 25 of it on the Step 4 to Step 5 hand-off |
| B | 75–90, about 20 on new vocabulary and re-running after slips | 50–60, Step 9's comments the slow part | 90 |
| C | 65 | 50 | 50 |
| D | 45 | 40 | 35 |
| E | 55–65 | 45–50 | 60–75 |
| **The lab** | **50** (10 of it in microsprints) | **35** (16 of it in microsprints), then the 15-minute block | none given; due Sunday |

## Environment blocks

These come from the review machine, not from the materials. They are kept apart so that none is read as a flaw in the week.

- **Python 3.11.18 on every persona's machine.** The key ran on 3.14.6. All five treated the older Python as a student whose environment is out of date, which is why their Step 4 and Step 6 answers differ from the key's. That difference is a real problem for students too (item 2), but the reviewers' numbers are older-Python numbers.
- **Step 8's three cells were not sent** (by B to E; A sent one by mistake), as instructed: the key tags them `not-run-live` and holds no saved output for them. Step 8's microsprint and Step 10's last question were therefore judged from the text alone. That the students' copy says nothing about the result is item 4; the absence of a run is not a flaw.
- **Part 2's checkpoint address returns 404** because `labs/week-02/data/` exists only on #214's branch. This is merge order, not a flaw: it ends when #214 is merged. What the cell does with a 404 is a design point (item 1).
- **GitHub's `robots.txt` was refused by the review machine's network** (E; D's 403 from GitHub in the exercises is probably the same). E swapped in another site; D kept the row. What that row showed is item 3.
- **Nothing else.** Wikipedia's 403 to the header-less request in Step 1 is the lab's design. No site answered 429.

## The strongest case for the week as designed

**Every tool is met first on something small enough to predict.** All five said so. Step 1's httpbin echo turns "a server sees your request, not your code" into one line of JSON, `python-requests/2.34.2`, then the student's own User-Agent (A, B, D). Step 2's five-line `robots.txt` is typed by hand, and its three `can_fetch()` questions can be answered on paper first: C wrote False, True, False before running and was right; D used the ClaudeBot microsprint to test whether an unnamed crawler really falls to `*`. By the time the Times's 386-line file arrives in Step 3, it reads as "the same thing, bigger" (B), not a wall; A, C and E said the same in their own words. Step 4 does the same for the longest-match rule: three lines in `two_rules`, then the Times's `/svc/wordle`, with the microsprint printing the two lines behind the answer (70 and 75).

**The traps are shown, not warned about.** Step 5 lets `read()` fetch Wikipedia's file, prints `disallow_all` as `True` and `can_fetch()` as `False` for an ordinary article, then sends `urllib`'s own User-Agent through `requests` and gets the 403 that explains it. D called it "a clean causal demonstration"; E said the silent failure became "something I caused and saw, not a warning I took on trust"; B compared it to a source who answers confidently and wrongly. Step 4's version note turns the Python version into a variable that changes an answer, which D, the student who cares about measurement validity, singled out.

**Given cells sit exactly where a student with little Python would stall.** `crawler_check()`, the loop over six newsrooms, `timed_requests()` and the line-number printer are given; each typed cell is one to four lines and names the variable it makes (B, C, E). The typed lines add to 39 in Part 1 and 23 in Part 2, well inside `labs/AUTHORING.md`'s 55 and 40. The by-hand-then-loop order works: the Colorado Sun by hand, then six newsrooms (B, E). C noted that cell 50's prompt already names the likeliest slip ("not `sun.text` itself").

**The news examples carry the argument.** The Times's file opens with a legal notice a parser can't read, then names 75 crawlers one by one; Step 6's table shows which newsrooms let GPTBot in and which keep ClaudeBot out; Reddit's `Disallow: /` closes the site in two lines (A, B, C, E). B, a journalism student, called the table "the most interesting thing of the week", and the Colorado Sun made it local. Step 7 gives measurements a student can check by arithmetic: 2.0 s for a two-second sleep, a few tenths for a request, an average gap of about 2.3 s for a 2 s delay (A, C, D).

**The Recommended Exercises are prepared step by step.** Step 10's "Recommended Exercises ahead" maps each exercise step to the lab step that practised it, so B, D and E said the take-home felt like assembly from things already typed. B, with no Python before this course, finished Steps 1–5 in about 90 minutes without the key.

## Where it falls short, ranked

The wrong-result problems come first; no persona found a privacy problem. After them, items are ranked by how many personas hit each, how badly, and whether it stopped A or B. Cell numbers are positions in `labs/week-02/lab-02-key.ipynb` at `1c59716`, counted from 0; the students' copy has the same 84 cells in the same order and is made from the key with `labs/tools/make_student_copy.py`, so every lab fix below is made in the key on #214's branch. The deck is `slides/week-02/week-02.tex` on the same branch. The chapter and companion notebook are textbook changes.

1. **Part 2 starts from a checkpoint that isn't on `main` yet, and an empty parser answers "allowed" to everything.**
   - **Who:** A, C, E traced the silent result; B and D hit the same 404.
   - **What happened:** cell 48, the given cell every student runs on Friday, fetches `DATA + "nytimes-robots.txt"`, with `DATA` pointing at `main`'s `labs/week-02/data/`. Until #214 is merged that answers 404. The cell doesn't stop: it parses the one-line body `404: Not Found`, and prints `404 1 lines`. The parser `rp` then has no rules and allows every page to every agent. Nothing downstream looks wrong: Step 7's `rp.crawl_delay("*")` prints `None` and Step 8's `rp.can_fetch("*", tech_url)` prints `True`, the same answers the real file gives. The fallbacks in cells 24 (Step 3) and 55 (Step 6) read from the same address.
   - **Why it matters:** it is the failure Steps 4 and 5 teach against, inside the lab's own given cell. The worst case is Step 8's given loop (cell 72): with an empty `rp` it would request `/search?query=robots`, which the Times's file disallows, instead of skipping it. A student who skims the print line, as C says it does, carries on.
   - **Proposed fix:** first, merge #214 before the notebook goes to students, and open the raw address of `nytimes-robots.txt` once to see a 200. Second, the design point, in the lab key: cell 48's comment should say what it must print, "200 386 lines; anything else, stop and ask" (A); the same in cells 24 and 55. `AGENTS.md` and `labs/AUTHORING.md` keep error handling out of labs and leave it to a Discuss box; whether a checkpoint, which is the course's own file, may call `saved_robots.raise_for_status()` (C, E) is the instructor's decision.
   - **Status:** verified. `git ls-tree` shows no `labs/week-02/data/` on `main`; the raw address of the checkpoint returns 404 and that of `lab-02.ipynb` 200. Parsing `["404: Not Found"]` gives `can_fetch` `True` for all three of cell 72's pages and `crawl_delay` `None`; the saved file gives `False` for `/search?query=robots`.

2. **Answers depend on the Python version in more places than Step 4 says.**
   - **Who:** A, B, C, D, E (all ran 3.11.18).
   - **What happened:** Step 4's text and deck frame say the longest-match rule arrived in Python 3.14.5, and Step 0 prints the version, which A and D credited. But the same release changed something else the lab doesn't mention: a blank line no longer ends a group. The Wall Street Journal's file lists 26 crawlers, including `googlebot`, then blank lines, then more crawlers including `GPTBot`, and the rules only after all of them. On an older Python those crawlers get no rules and fall to `User-agent: *` (`Disallow: /`), so the WSJ row is all `False`; on the key's Python, `Googlebot` and `GPTBot` are `True`, as in `allowed.csv`. Step 10's first question then has two answers: three newsrooms let GPTBot in (the key's answer: the Post, the Journal, the Guardian, which it ties to licensing deals), or two. Step 2's text also states the old rule as fact: "a blank line ends a group". And the dividing line isn't only 3.14.5: 3.13.14 has both changes too.
   - **Why it matters:** the row that changes is the one the key's story rests on. A, B and D said they would suspect their own code first; C: "a less confident student would redo the cell". `python=3.14` in the setup command installs whatever 3.14 is current, so an environment built before 3.14.5 and never updated gives the old answers.
   - **Proposed fix**, lab key and deck:
     - Step 0's text (cell 2): "3.14.5 or later, or 3.13.14 or later, gives the key's answers; an older Python gives different ones in Steps 4 and 6", and whether to update is the instructor's call.
     - Step 2's text (cell 13): a group runs until the next `User-agent` line after its rules, as RFC 9309 says; Pythons before 3.14.5 end it at a blank line.
     - Step 4's text (cell 29) and the deck's "Step 4: when two rules match": "since 3.14.5 (and 3.13.14)", and what each version prints for `/svc/wordle` (A, D).
     - Step 6, after the table (cell 54) or in its Discuss (cell 58): "on an older Python the wsj.com row differs: its file puts blank lines inside a group". C and E would also add a given cell that prints where the live table differs from `allowed.csv`.
     - Step 10 (cell 81): ask about the saved table, `allowed.csv`, so everyone answers about the same file (A).
   - **Status:** verified by parsing the WSJ file the personas saved on 2026-11-18 and the five-line and three-line test files on Python 3.11.18, 3.12.3, 3.13.0, 3.13.13, 3.13.14, 3.13.18, 3.14.4, 3.14.5 and 3.14.6. The longest-match answer and the WSJ row change together, between 3.13.13 and 3.13.14 and between 3.14.4 and 3.14.5. On 3.14.5 and later the saved WSJ file gives exactly `allowed.csv`'s row, so the WSJ difference is the Python version, not a change to the file. The Colorado Sun row is not version-dependent (see "Corrections").

3. **A refused request is counted as a file with no rules, in the chapter's exercise and in `crawler_check()`.**
   - **Who:** D, E; A for the Step 6 microsprint.
   - **What happened:** in Exercise Step 4, D and E each picked GitHub as a second site, got a 403 (from the review machine's network; see "Environment blocks"), and the chapter's comparison code, which their loops followed, reported GitHub as 1 line, 0 `Disallow`, 0 `Allow`. Exercise Step 6 then asks which site is most restrictive, and D "would have written something false from the GitHub row". E caught it only by printing the status code. D's "daily" site for the Step 6 microsprint answered 418 with a five-line `Disallow: /` file, and D couldn't tell whether it was real; A made the same point about Reddit's all-`False` row.
   - **Why it matters:** the same wrong answer comes from a real site that refuses a client, and the exercise is the graded part of the week. The chapter's own first example calls `response.raise_for_status()` "if the site answers with an error, such as a 403 or a 404, instead of parsing its error page", and its comparison loop, three sections later, doesn't.
   - **Proposed fix:** chapter, "Comparing robots.txt Across Platforms": print `response.status_code` in the loop, or call `raise_for_status()` as the chapter's first example does; the companion notebook follows. Chapter, Exercise Step 4: "print each status code before you count; a 4xx page is not a rules file". In the lab, `crawler_check()` (cell 53) may stay as it is, since Step 6's third Discuss question names the limitation, as `AGENTS.md` asks.
   - **Status:** verified: the chapter's comparison loop and `crawler_check()` have no status check, and the chapter's first example has one. The 403s themselves came from the review machine.

4. **Step 8 sends the Times a scripted request just after Step 3 shows its notice forbidding one, and students see no expected result.**
   - **Who:** B and E named the conflict; A, B, C, D and E found Step 8's questions unanswerable without a result.
   - **What happened:** Step 3's given cell prints the Times's notice: use of any automated means "to data mine or scrape the content … is prohibited without prior written permission". Step 8 then has every student fetch the technology section with `requests.get` because `rp.can_fetch("*", tech_url)` is `True`. Neither Step 8's text (cell 69) nor the deck's "Step 8: ask first, then send" ("It says yes, so send it") mentions the notice, and the key's model answer for Step 9's Legality line (cell 77) says only "no Terms of Service accepted". Separately, the key tags cells 71, 72 and 74 `not-run-live` and holds no output for them; its opening explains why and records a 403 from DataDome on 2026-10-21, but that note is in the key only. The students' copy says nothing of what to expect, and Step 8's microsprint ("who answered, and what the page asks a visitor to do") and Step 10's last question assume a result.
   - **Why it matters:** B, who reads Terms of Service professionally, wrote "robots.txt allowed it" for Legality, then saw it didn't fit; a student who takes "`can_fetch` is True, so I may" into a project takes the wrong lesson. And a student whose request answers 200 from campus has no 403 page to read (A, E); `tech_page.headers["Server"]` would raise `KeyError` if the header is absent (E).
   - **Proposed fix:** whether students send this request at all is the instructor's decision. If they do: Step 8's text (cell 69) and the deck frame name the tension before the request (the notice says no; `robots.txt` says yes for `*`; which do we follow, and why is one request defensible here?), and the key's Step 9 Legality line (cell 77) mentions the notice. For the missing result, either one sentence in Step 8 ("from a cloud machine this answered 403 from DataDome; from campus it may answer differently", A) or a dated checkpoint in `labs/week-02/data/` with the status code, the `Server` header and the first 240 characters as the instructor's laptop saw them (B, C). Microsprint (cell 74): `tech_page.headers.get("Server")` (E).
   - **Status:** verified: cells 26, 69, 71, 72, 74 and 77 of the key, the students' copy (no mention of DataDome or `not-run-live`), and the deck frame.

5. **One missing `.text` in Step 3 leads to four `NameError`s and then a table of `False`s with no error.**
   - **Who:** A, B; C reproduced the first error.
   - **What happened:** cell 25's prompt is "lines: the text split into lines (splitlines())". A and B both typed `nyt_robots.splitlines()` and got `AttributeError: 'Response' object has no attribute 'splitlines'`. Cells 26, 27, 32 and 37 then failed with `NameError: name 'lines' is not defined`. Worse, cell 32 had already made `rp = RobotFileParser()` before failing at `rp.parse(lines)`, and an unparsed parser answers `False` to everything, so cell 33 and cell 34's table printed a Times that blocks every crawler from every page, with no error (A).
   - **Why it matters:** A and B read only a traceback's last line; five red cells look like a broken notebook, and the quiet table afterwards looks like a finding. The deck's Step 3 frame has `nyt_robots.text.splitlines()`; cell 50's prompt for the Colorado Sun names `sun.text.splitlines()`; only cell 25 leaves `.text` out.
   - **Proposed fix:** lab key, cell 25: "lines: `nyt_robots.text`, split into lines (`splitlines()`)". Deck, "Today: lab Part 1", Error flavors: "a `NameError` after an error means an earlier cell failed; fix that one first" (B).
   - **Status:** verified: the prompt as quoted, the deck frame, and `can_fetch()` on an unparsed `RobotFileParser`, which returns `False` on 3.11 and 3.14.6.

6. **The Wednesday deck still sends students to the old notebook and the old exercises.**
   - **Who:** A, B, C, D.
   - **What happened:** "First: get this week's notebook from GitHub" walks students to the companion notebook, `ch-02-ethics.ipynb`, not the lab (D). "Lab: work these, then show-and-tell" lists five tasks (a five-site comparison, a Terms of Service reading, the dating app, the 1 s and 2 s timing, a 300-word audit), which are the chapter's Additional Exercises; "Today: lab Part 1" says the Recommended Exercises are due Sunday, and "What to submit" says "Wednesday notebook exercises to bottom, save as HTML" (A, B, C). "Activity: survey a sector", "Which AI crawlers does this site block?", "Identify yourself, then slow down" and "`responsible_get()`: build it once" sit in Wednesday's section, though the lab does the AI crawlers in Friday's Step 6 and leaves `responsible_get()` for reading after class (A).
   - **Why it matters:** B would "follow the most recent, most specific instruction in class", which is the longer, ungraded list. A couldn't tell which of three User-Agent strings to copy.
   - **Proposed fix:** deck: retitle "Lab: work these" as the chapter's Additional Exercises, optional (A, B), or drop it; move or mark the AI-crawler and `responsible_get()` frames as Friday's or as reading. `docs/course-facts.md` already lists "First: get this week's notebook" and "What to submit" as the instructor's frames, not yet changed; "Lab: work these" isn't on that list.
   - **Status:** verified by reading the frames on #214's branch and the course-facts row.

7. **Exercise Step 5 needs a pattern the lab only gives, and nothing in the chapter imports pandas.**
   - **Who:** A, B, E; C for the crawl-delay column.
   - **What happened:** Exercise Step 4 says to count lines and rules "following the chapter's comparison code", which prints each site's counts and keeps nothing. Step 5 then wants one DataFrame for three sites with `crawl_delay("*")`, which needs a parser per site. A's first loop overwrote `lines` and kept only Wikipedia; B took 30 minutes, "the longest of any step"; E managed only because it knew dicts. The lab's dict-per-site pattern is inside a given cell (cell 54), which no one typed. Neither the chapter nor its companion notebook imports `pandas`, and the exercise cells import nothing, so A also hit a missing `import time`. Every persona's crawl-delay column came out `None` (shown as `NaN`), which A, B and C didn't know how to read; D's arXiv (15) and E's Hacker News (30) showed what a real value looks like.
   - **Why it matters:** this is the one exercise step where a minimal student hits a wall, at home, in the graded notebook.
   - **Proposed fix:** chapter, Exercise Step 4: "keep each site's text and its parser: Step 5 needs both". Step 5: "a dict for each site, then `pd.DataFrame(rows).T`; `None` means the site declares no crawl delay". Companion notebook: `import pandas as pd` and `import time` in a setup cell above Step 1. Lab key, cell 81's Step 5 hint: say that Step 6's dict-per-site was in a given cell, and point to it.
   - **Status:** verified: the chapter's comparison code; no `pandas` in `ch-02-ethics.qmd` or its notebook; the exercise cells hold only prompts. The minutes are the personas'.

8. **Wednesday is 50 minutes by the headings; students like A and B estimate 75 to 90.**
   - **Who:** A, B, C over; D and E within it. Pace ratings: B 2; A and C 3; D and E 4.
   - **What happened:** Part 1's headings add to 50 minutes with three microsprints inside; Part 2's to 35 with four. The typing is not the cost: 39 typed lines against a budget of 55, and 23 against 40. B puts the time in vocabulary (dictionary, list of strings, `RobotFileParser`, `parse()`, `can_fetch(agent, url)`, `set`, `disallow_all`) and in re-running after slips; A in Steps 4 and 5. Step 9's heading gives 4 minutes, and its dating-app microsprint alone is 5.
   - **Why it matters:** five Discuss boxes on Wednesday won't be used if students are still typing (B).
   - **Proposed fix:** the instructor's decision. Candidates: keep one Discuss question a step in class and the rest after (B); cut Step 2's ClaudeBot microsprint or Step 5's cell 43 (B; D would keep the microsprints). Fix Step 9's heading (cell 76) to at least its microsprint's 5 minutes, and take the minute from elsewhere.
   - **Status:** the headings and typed lines are verified from the key; the estimates are the personas'.

9. **Part 2's setup is a given cell that must be edited, and a missed edit sends the placeholder address.**
   - **Who:** C, E.
   - **What happened:** cell 47 is marked "Given" and holds `your-email@colorado.edu`; Step 6's text says to put one's email in it. A student who runs it as a given cell sends every one of Part 2's requests with the placeholder, which Step 0's Discuss ("every request you send this week carries your email") warns against. Nothing prints `HEADERS`.
   - **Proposed fix:** lab key, cell 47: end with `print(HEADERS)`, so the placeholder is on screen (E), or make the `HEADERS` line a typed cell, as in Step 0. (E's `assert` would be error handling, which the lab's rules leave out.)
   - **Status:** verified by reading cells 4, 46 and 47.

10. **"Step 3" means two things in Step 10's list.**
    - **Who:** C.
    - **What happened:** cell 81's "Recommended Exercises ahead" numbers the exercise steps "Step 1 … Step 6" and the lab steps the same way in the same line ("Step 3, parse it with `rp.parse()`: Steps 2 and 4 parsed a file"). The microsprints also say "Additional Exercise 3" and "4" without saying they are the chapter's.
    - **Proposed fix:** lab key, cell 81: "Exercise Step 3 … Lab Steps 2 and 4". Cells 56 and 66: "the chapter's Additional Exercise 4", with a link.
    - **Status:** verified.

11. **Three cells print two bare `True`/`False` lines.**
    - **Who:** B.
    - **What happened:** cells 20, 31 and 33 each print two answers with no label, so a student who predicted both can't tell which output belongs to which question.
    - **Proposed fix:** lab key, those prompts: `print("wordle:", …)`. Still one line, and a habit B wants for a project.
    - **Status:** verified.

12. **Step 4's microsprint helper matches plain prefixes only, and doesn't say so.**
    - **Who:** C, E.
    - **What happened:** cell 37 prints each rule whose path `path.startswith(rule)`. The Times's file has dozens of rules with `*` or `$`, which this ignores. It works for `/svc/wordle`; for a path such as `/section/technology?utm_source=x` a student could see no matching line and a `can_fetch()` answer it can't explain.
    - **Proposed fix:** lab key, cell 37: one comment line, "this matches plain prefixes only; the parser also handles `*` and `$`".
    - **Status:** verified: the cell, and 81 `Allow`/`Disallow` lines with `*` or `$` in the saved file.

### Corrections

Claims in the reviews, or in the brief for this document, that turned out wrong or inexact, and what this document does with them:
- **The Colorado Sun row did not change.** B says its `Google-Extended` was `False`, against `allowed.csv`'s `True`; E says it was `False` on a first run and `True` minutes later. Every saved table from all five personas, both of B's included, shows `True`, as does the saved file on every Python tested. The file names `Google-Extended` in three groups, `Allow: /` first and then twice `Disallow: /`, so the answer depends on which group a parser takes, and a copy served in a different order could flip it. E's first run wasn't saved: reported, not verified, and not listed as a version or day-to-day difference.
- **"3.11 and 3.13 versus 3.14.5"** is inexact. 3.13.0 through 3.13.13 give the old answers; 3.13.14 and later give the key's, like 3.14.5 and later. E's "on 3.13 they are True" holds for 3.13.18, not every 3.13.
- **D: the WSJ difference is "probably first-match versus longest-match … plus drift".** Neither: it is how blank lines end a group (item 2), and the file saved on 2026-11-18 gives the key's row on 3.14.5 and later, so there is no drift.
- **A: Wikipedia's count "is 712 with the chapter's way"; the numbers agree.** Right, and D got 712 / 460 / 4 too. Only the Times's line in the chapter is stale ("Small things").
- **E: cell 37 "counts the group's first `User-agent:` line as a rule".** The line is in the range the cell reads, but its value, `*`, never starts a path, so it never prints. Dropped.
- **C rated difficulty 4, "about right, a little easy".** On the scale used, 5 is hardest. The rating is kept as given; the comment suggests C meant about 2 or 3.

## Disagreements

- **Too slow, or about right.** A, B and C put Wednesday at 65 to 90 minutes; D (45) and E (55–65) say the minutes fit. The typed lines are well under budget, so the gap is reading and vocabulary, which is where A and B differ from D and E. That suggests saving time in Discuss boxes and microsprints, not in the code.
- **How fenced the cells should be.** C never had to debug ("the cells are so well fenced that … I did not learn to read an error") and would like to; A and B hit a five-cell cascade from one missing word (item 5). D and E want the status check shown as a habit; the lab's rules leave it to Discuss boxes. Both can hold: label what a slip looks like (item 5) and put the check in the chapter's exercise (item 3).
- **What to do about the Python version.** A and D want one sentence saying the old answer is expected; B wants students told to update; C and E want a given cell that compares the live table with `allowed.csv`. These combine (item 2).
- **Step 8.** B and C want a dated checkpoint of the result; A a sentence saying what to expect; B and E want the notice named before the request. Whether students send it at all is the instructor's call (item 4).
- **What to cut.** B would cut Step 2's ClaudeBot microsprint or Step 5's cell 43; D says the microsprints are what kept it thinking and would keep them.
- **Confidence.** E rates 5 ("I could write a polite fetch wrapper"); A, B and C 3. B is held back by the legal call (item 4), C by not knowing the steps for a site that isn't a news site, A by not knowing what to do after a 403 with a good User-Agent.

## Ratings

Each on a scale of 1 to 5. For difficulty, 5 is hardest for that persona's background.

| | A | B | C | D | E | Mean |
|---|---|---|---|---|---|---|
| Clarity of motivation | 4 | 4 | 4 | 4 | 4 | 4.0 |
| Pace | 3 | 2 | 3 | 4 | 4 | 3.2 |
| Difficulty for my background | 3 | 3 | 4 | 2 | 2 | 2.8 |
| How much I learned | 4 | 4 | 4 | 3 | 4 | 3.8 |
| Confidence I could do this on my project | 3 | 3 | 3 | 4 | 5 | 3.6 |

What held motivation at 4 for everyone: B and E took a point for Step 8 sending the request the notice forbids; A found the ethics thinner than the technique, and D the legal frames less tied to the code; C found nothing for a business reader on why a company cares about its own `robots.txt`.

## Small things

Lab key (`labs/week-02/lab-02-key.ipynb`):
- The User-Agent has four forms: the lab's `WebDataScience/1.0 (your-email@colorado.edu)`; the chapter's `(INFO 4617; your-email@colorado.edu)`; `responsible_get()`'s `(student-project; …)`; and the deck's `you@colorado.edu`. Exercise Step 1 asks for one that "names this course", which the lab's doesn't; Step 10 fixes it only for a student who reads Step 10 (A, B, C, D, E).
- Step 3 (cell 27) prints "76 User-agent lines, 75 different crawlers" without saying that `Googlebot` appears twice (C).
- Step 7's Discuss, "longer than four seconds of pauses", works because `timed_requests()` records the time before the last sleep; nothing says so (B, C).
- Step 7 times one run of five requests; one sentence that request times vary would help a student who reads them as measurements (D). The key's opening says they vary by a few tenths, but the students' copy doesn't.
- Step 6's microsprint (cell 57) on Reddit is all `False`; printing the status code would let a student tell a block from a refusal (A; see item 3).
- Step 6's table wraps in a narrow notebook, which makes the WSJ and Colorado Sun rows hard to read (B).
- Step 9's model answer counts "about thirty requests to eleven sites"; "eleven" appears nowhere else (E).

Deck (`slides/week-02/week-02.tex`):
- "Which AI crawlers does this site block?" lists `Applebot-Extended` and `Meta-ExternalAgent`; the lab's `AGENTS` doesn't (C).
- "Step 1: no headers at all" builds the address from `article`; the lab's cell 9 writes it in one line. The frame says so, and copying either works (A, B).
- The title's date is "August 24, 26 & 28, 2026"; for the next offering it will need the new dates (C).

Chapter and companion notebook (`ch-02-ethics.qmd` at `3f9cf2c`):
- The comparison's comment says "NY Times: 359 lines, 149 Disallow rules, 27 Allow rules"; the file saved on 2026-11-18 has 386, 149 and 38. The lab's revision block asks about the lines only (all five; B and C for the Allow count).
- The companion notebook shows `@sec-introduction` (three times) and `@fiesler2020no` unrendered, along with other cross-references, and its callouts come out as plain `##` headings (B, C). This is probably true of every companion notebook, not only this one.
- "Run all" in the companion notebook sends the chapter's requests, the Times's and Reddit's `robots.txt` among them, before the exercises (B).
- Exercise Step 2 prints the first 500 characters of Wikipedia's file: a byte-order mark and a comment block, not the `User-agent: *` rules that Step 3 tests (C, D).
- Exercise Step 4 counts with `startswith("Disallow")`, which misses a file written in lower case (C).

## Suggested next step

**Fix first,** on #214's branch before it is merged; each is small and changes none of what the week teaches:
1. **Item 1:** merge #214 before the notebook goes out and check the raw address once; say in cells 48, 24 and 55 what they should print.
2. **Item 2:** the version sentences in Steps 0, 2, 4, 6 and 10 and the deck's Step 4 frame: 3.14.5 or 3.13.14, the blank-line change, and the WSJ row.
3. **Item 5:** `nyt_robots.text` in cell 25's prompt, and the `NameError` line in the deck's Error flavors.
4. **Items 9 to 12:** `print(HEADERS)` in cell 47; "Exercise Step" and "Lab Step" in cell 81; labels in cells 20, 31 and 33; the prefix comment in cell 37.
5. **Items 3 and 7, in the textbook:** a status check in the chapter's comparison loop and Exercise Step 4; "keep each site's parser", the DataFrame hint and a setup cell with `pandas` for Step 5; and the Times's count.

**Needs the instructor's decision:**
- **Step 8** (item 4): whether students send the Times a request after reading its notice; if so, how the step names the conflict, and whether the course saves a dated result for them to read.
- **A status check in the checkpoint cells** (item 1), as an exception to the labs' no-error-handling rule.
- **Whether to ask students to update Python**, or only say what an older one prints (item 2).
- **The Wednesday frames** (item 6): "Lab: work these", "What to submit", "First: get this week's notebook", and where the AI-crawler and `responsible_get()` frames go.
- **The minutes** (item 8): which Discuss questions and microsprints move after class, and Step 9's heading.
