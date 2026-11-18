# Review: week 14, Automating Data Collection

**What was reviewed:** week 14's lab (`labs/week-14/lab-14.ipynb`, with its key), its deck (`slides/week-14/week-14.tex`), the collector template (`labs/week-14/template/`), the course's series (`labs/week-14/data/forecasts.csv`) and chapter 14's Recommended Exercises, as students meet them.
- **Course repository, personas B to E:** the head of pull request #213, `576551b086a48cde83c9f9ed0a6e3f308590589e`, which rewrote the lab and deck to GitHub's real schedule: three or four runs a day, not every hour.
- **Course repository, persona A:** `main` at `efc1e36711c1f2e4ae3fcbf00c4cfa78cd3709ac`, before #213. Each of A's findings was checked against `576551b0`; the ones #213 already fixed are under "Corrections".
- **Textbook:** `ch-14-automation.qmd` and its companion notebook at `90fd7efd1957e510a734f3c2a18037160be7ce37`, the head of textbook pull request #310 (not merged).

**When:** 2026-11-17 and 18, the evening before Part 1 is taught.

**Method:** five anonymous composite personas, each a kind of student this course has, reviewed the week independently. Each read the chapter and the slides, typed and ran its own code for every lab step it could from the students' copy, made the mistakes its background makes, attempted the Recommended Exercises, and opened the key only after an honest try. Each review is a **steel man**: it first makes the strongest case for the materials as designed, and only then says where they fall short for that student. This document puts the five together. Every ranked finding was then checked against the repository and the textbook, and is marked **verified** (with how) or **reported, not verified**.

## Who reviewed

| | Degree and major | Python and data background | Interest | Skill |
|---|---|---|---|---|
| A | BS senior, Information Science | One intro Python course; spreadsheets | Qualitative and design: online communities, UX | Minimal |
| B | BA junior, Journalism and Communication | No Python before this course; strong with public records and Excel | Data journalism, local government | Minimal |
| C | BS senior, Business Analytics | Excel, some SQL, a little pandas | Quantitative analytics: markets, customer data, dashboards | Minimal to moderate |
| D | MS first year, Data Science (BA in Statistics) | Fluent in R, moderate pandas; regression and sampling | Quantitative: measurement and validity | Moderate |
| E | MS first year, Information Science (BS in Computer Science) | Moderate Python, git; little data analysis | Design and tools: automation, APIs, building things | Moderate |

## What each completed

The lab has Steps 0–12 and five microsprints: Part 1 (Wednesday) is Steps 0–6, Part 2 (Friday) Steps 7–12. No persona could make a GitHub repository (see "Environment blocks"), so Steps 4 and 5, the own-repository cells of Steps 6 and 10, and Step 11's break-and-fix were read, not done, by all five. Every persona also ran the template's `collector.py` locally, which the lab doesn't ask for (item 13).

| | Lab steps finished | Read, not done | Recommended Exercises | Needed the key for |
|---|---|---|---|---|
| A | 0–3, 7–10, 11's two cells, 12; all five microsprints. 6 and 10's own-series cell on a local file | 4, 5, 11 on GitHub | Steps 1–6; Step 5 written and parsed, not run | Nothing |
| B | 0–3, 7–12, 11's two cells; all five microsprints. 6 on a local file | 4, 5, 11 on GitHub | Steps 1–6; Step 5 written, not run | Nothing; compared Steps 1, 8, 10 and 12 afterwards |
| C | 0–3, 7–12, 11's two cells; Part 1's microsprints, Step 8's and Step 11's. 6 and 10's own-series cell on a local file | 4, 5, 11 on GitHub | Steps 1–6; Step 5 written, not run | Nothing |
| D | 0–3, 7–10, 11's two cells, 12; Part 1's microsprints and Step 11's | 4, 5, 11 on GitHub; skipped 6 and 10's own-series cell | Steps 1–4; Step 5 written and parsed; Step 6 answered | Nothing |
| E | 0–3, 7–10, 11's two cells, 12; Part 1's microsprints and Step 11's. 6 on the course's series | 4, 5, 11 on GitHub | Steps 1–5 (5 written, not run); Step 6 answered | Nothing |

**Estimated time for a real student of that background, in minutes** (the lab's own step and microsprint minutes in the last rows):

| | Part 1 | Of which GitHub's pages | Part 2 | Exercises |
|---|---|---|---|---|
| A | 55, plus the GitHub steps, which A couldn't judge | not estimated | 40 | 150, most of it on Step 4 |
| B | 85–100, plus 10–15 | 10–15 | 55–65 | 150–180 |
| C | 65–70 | 25–30 | 40–45 | 150 |
| D | 45 of reading and typing; "a class would take longer" | 20 of reading | 30 | 120 |
| E | 70 | 25–30 | 40 | 120 |
| **The lab** | **57** (50 in steps, 7 in microsprints) | 18 (Steps 4 and 5) | **46** (36 in steps, 10 in microsprints) | none given |
| **The day** | **50** | | **35**, then the 15-minute slides block | practice this week, not turned in |

## Environment blocks

These come from the review machine, not from the materials. They are kept apart so that none is read as a flaw in the week.

- **No GitHub repository could be made (all five).** Steps 4 and 5, Step 6's and Step 10's own-repository cells, and Step 11's break-and-fix were read and judged as instructions, not clicked through. Exercise Step 5's workflow was written and saved, and not run. As stand-ins, A, B and C read their local `forecasts.csv`, and E read the course's series.
- **D's first NWS calls were refused by the review machine's own permission check,** because they carried the instructor's address in the User-Agent. D sent a User-Agent that names no one, and the NWS answered 200 to everything after. D's runs differ from a student's in that one string.
- **No access to GitHub's API (E),** so E couldn't check that the template's `actions/checkout@v7` and `actions/setup-python@v7` exist. They do: the course's own collector workflow on `main` uses the same versions and has been committing data.
- **The series grew during the review.** The file at `576551b0` holds 19 runs; the key and the text were written at 18. Persona A, on `efc1e367`, read a 16-run copy in the repository and an 18-run copy at the raw address. That is the file doing what it's meant to, not a block, but it explains why the personas' numbers differ from the key's (item 7).
- **Nothing else.** The NWS and `raw.githubusercontent.com` answered every request from every persona, with no 429s.

## The strongest case for the week as designed

**The first requests are the smallest that teach something, and every answer can be checked by reading it.** All five said so. `/points` answers "Boulder", so B knew at once it had worked; the swapped-coordinates microsprint gets a 404 with the NWS's own words, "Must have a minimum value of -90", which taught A that "an error message can be read like data" and E that the API says "exactly what you did". Step 2 then asks how old the data are before anything is collected: `updateTime` against `generatedAt`, then `Last-Modified` and `Cache-Control`. B, D and E each got a gap of 9 hours 52 minutes on their own request. To D this is "the measurement-validity question … asked before any collecting happens"; to E it is what makes "ask every hour" look wasteful before any theory shows up; to B it turned "Last Update" on the forecast page into "a fact about a person".

**Step 3's given script is the right size, and names the right four things.** `collector.py` is read, not written, and the step names constants, append mode with the header written once, `raise_for_status()` and the `__main__` guard before students read the file. A, B, C and E each said they could not have typed it and could now say why each part is there; B called the append-and-timestamp habit "the same discipline as dating a records request". A broke the URL locally and saw the `404 Client Error` the lab promises. Printing the workflow from a given cell and pasting it, rather than writing YAML, was "the right call" for B, and the `collect.yml` frames read it line by line afterwards.

**Part 2 hands students a real week of data with a real defect in it, and makes them measure the defect.** D, C and E each called the course's series the best decision of the week. It doesn't wait for a student's own collector, and it carries the lesson that a schedule is not a sample: 19 runs where the schedule asked for about 115, gaps up to 10.6 hours. Step 8's sentence that forecasts divided by runs "would describe GitHub, not the forecast" was singled out by C ("a measurement-validity sentence I will reuse") and D ("the right denominator"). Step 10 takes its threshold from the data, the longest gap, instead of the nominal hour (C, D, E). E would have trusted a lecture on GitHub's unreliability much less than that one printed 10.6 hours; for B, the honest finding "taught me more about trusting a pipeline than any success would have".

**The loud-and-quiet-failure pair is the lesson every persona would take to a project.** The swapped coordinates fail with a 404; the swapped grid square `75,54` answers 200 with somebody else's weather and nothing to say so (all five). A called it "the most important lesson of the week", C "the data-quality lesson I care about", D "better than a paragraph could". The Discuss question, "a gap, or a month of Aurora's forecasts?", was quoted by A and C. The Discuss boxes about people (who else asks every hour, who keeps a forecast's history, what has to come with a cited forecast) were what A and B said they would remember.

**The Recommended Exercises extend the lab without repeating it.** Another place, one more column, a series check built on the chapter's `check_freshness()`, a workflow of one's own (B, C, E). B, who had no Python before this course, finished all six steps.

## Where it falls short, ranked

The privacy problem and the wrong-result problems come first. After them, items are ranked by how many personas hit each, how badly, and whether it stopped A or B. Cell numbers are positions in `labs/week-14/lab-14-key.ipynb` at `576551b0`, counted from 0; the students' copy is made from the key.

1. **Students put their own email address in a public repository before the lab says it will be public.**
   - **Who:** B, D, E.
   - **What happened:** Step 4, item 4 says to change `your-email@colorado.edu` in `HEADERS` "to your own address" and commit it, in a public repository. The warning comes afterwards, in Step 4's Discuss box ("the email in `collector.py` [is] public too"), and in the template's README, which students upload one item earlier without reading. Editing the address out later leaves it in the commit history. The deck's "Step 4: upload two files" frame says only "type your email address".
   - **Why it matters:** the address stays public, attached to a named GitHub account, for good. B, the journalism student, stopped at it; D "would not do that with a university address".
   - **Proposed fix:** lab key, Step 4 item 4, and the deck frame "Step 4: upload two files": say before the edit that the address will be public and stays in the history, and that any address the student checks will do. Say the same in Step 0, where the address is first asked for. (D also suggests a GitHub noreply address; that defeats the NWS's reason for asking, a way to reach whoever runs the program, so it isn't proposed here.)
   - **Status:** verified: cell 27 (Step 4, item 4), cell 29 (its Discuss), the deck frame, and the template's README ("This repository is public, so anyone can read that address").

2. **Step 9's plot shows a smooth drift that isn't in the data, and counts one forecast several times.**
   - **Who:** B, C, D.
   - **What happened:** the given cell (52) plots noon on November 18 with `ax.plot(..., marker=".")`, one point per run, against the time from the run (`collected_at`) to noon. At `576551b0` the file has 19 rows for that hour but only 13 distinct forecasts (`update_time`), so runs that found the same forecast are drawn as separate points, and diagonal lines join forecasts that in fact held and then jumped. B and C both read it as gradual: 49, 52, 55, 52, 49, 51. The chapter's own figure uses `ax.step(..., where="post")` for this reason. Neither the step nor its Discuss says that several runs share one forecast.
   - **Why it matters:** this is the plot Step 12 asks students to describe ("How far did the forecast for noon move?"). D: "I would report moves … as if they were 19 independent forecasts." C: "I would read the slope as a signal."
   - **Proposed fix:** lab key, cell 52, and the deck frame "Step 9: plot it": `ax.step(lead_hours, noon_rows["temperature"], where="post")`, as in the chapter. Add one typed line after it, `print(noon_rows["update_time"].nunique(), "forecasts")`, and one sentence in Step 9's text: "runs that found the same `update_time` repeat one forecast". Optionally say in the cell's comment that a forecast was made before the run that collected it, so the lead from its issue time is longer than the x-axis shows (see "Corrections").
   - **Status:** verified: cell 52 and the deck use `ax.plot`; the chapter uses `ax.step(..., where="post")`; the reviewed file has 19 noon rows and 13 distinct `update_time` values among them.

3. **"2.4 changes a day" and "one request in ten" are given as measurements, and they are lower bounds.**
   - **Who:** B, C, D; E for the exercise's version.
   - **What happened:** Step 8 computes 12 changes in 5.0 days, 2.4 a day, and the microsprint turns it into 67 of 672 requests, 0.1. The deck's "What a bot costs a server" says an hourly collector "would find a new forecast about one request in ten", and Step 12 asks "How many times a day did the forecast change?". The chapter says otherwise: one version (06:46 UTC on November 13) "came and went between two of the course's runs without leaving a row", so "13 is the least number of versions there were". None of Step 8, its microsprint, Step 12 or those frames says "at least". Exercise Step 4 asks for "the longest a forecast stood unchanged", where the 15.2 hours a student finds is the interval that hides that missed version (C, E).
   - **Why it matters:** B would quote "one in ten" in a story. D: "a result that is a lower bound should be called one before I carry '1 in 10' into a conclusion". C would set Exercise Step 4's threshold from the 15.2 hours and set it too loose.
   - **Proposed fix:** lab key, Step 8's text (cell 42): "at least 2.4 a day: a forecast that came and went between two runs isn't in the file"; the microsprint's Share line (cell 47): "about one in ten, or more"; Step 12's first bullet (cell 68): "at least how many times a day". Deck: the same two words in "Step 8: changes a day" and "What a bot costs a server". Chapter, Exercise Step 4: "the longest a forecast stood unchanged between the versions the series saw".
   - **Status:** verified: no "at least" or "least" in the key's Steps 7–12 or in those deck frames; the chapter's "Reading What It Collected" has the sentences quoted; the version gaps in the reviewed file run 1.1 to 15.2 hours.

4. **Exercise Step 3 can leave a file that reads back scrambled, with no error.**
   - **Who:** B, C.
   - **What happened:** both added a column to the dictionary in `writerow()` but not to `FIELDS`. The first `main()` stopped with `ValueError: dict contains fields not in fieldnames`, after writing the old eight-column header. Fixed and rerun, the new rows had nine values under eight names, and `pd.read_csv()` raised nothing: B got shape `(312, 8)` with timestamps in the index and the weather text in `wind_direction`; C got a shifted table with `start_time` holding a number. Both also first hit `NameError` because the step says to copy "the constants and `main()`" and the imports are neither.
   - **Why it matters:** this is the chapter's "quiet corruption", made by the exercise. B caught it only because the step asks to show the new column; "a student who skims the output would submit scrambled data".
   - **Proposed fix:** chapter, Exercise Step 3: "copy the imports too"; "a new column goes in both `FIELDS` and the row's dictionary"; and "if a run stops partway, delete your file before running again: the old header stays". The chapter's Common Issues already says "Start a new file whenever you change the columns"; the step should point to it.
   - **Status:** verified: `collector.py` opens the file and writes the header before the first `writerow()`, so a `ValueError` leaves a header behind; the step's wording is as quoted. The read-back shapes are the personas' own.

5. **Exercise Step 4's check can't show that it "catches what you broke".**
   - **Who:** A, B, C, D, E.
   - **What happened:** the step asks for three checks (a gap of more than two hours between runs, a run under 150 rows, a forecast over a day old), then to break a copy "(drop a run's rows, or set a column to empty)" and "show that it catches what you broke".
     - On the series as it is, all 18 gaps are over two hours, so the check fires 18 times before anything is broken. Dropping a whole run merges two flagged gaps into one, so the count goes **down** (C, D, E).
     - An empty column trips none of the three checks. `check_freshness()`, which the step says to build on, has an empty-column test, but the list leaves it out (A, B, C, D).
     - Only dropping some of a run's rows was caught, by all five.
     - Even with a 12-hour limit, dropping a run is caught only where the two gaps it joins add to more than 12 hours, and dropping the newest run is never caught, because the check compares runs only with each other (D).
   - **Why it matters:** it is the exercise's point. A spent 30 minutes checking a correct loop; B: "my function passed on your broken copy".
   - **Proposed fix:** chapter and companion notebook, Exercise Step 4: ask for the supported thresholds first and pass them as arguments (12 hours for the gap, as "Failures and Monitoring" suggests); add "a column empty in every row of a run" to the list; say "drop some of one run's rows"; and add a sentence that a stopped collector needs `check_freshness(series, now)`, since a series check can't see it.
   - **Status:** verified: the step's text at `90fd7ef`; the reviewed file's 18 gaps, all between 2.1 and 10.6 hours; and the sums of neighbouring gaps, which a dropped run would leave: 9.2 to 18.5 hours, 6 of 17 at 12 or under.

6. **Neither part fits its day by the lab's own minutes, and the GitHub pages are where the time goes.**
   - **Who:** A, B, C, D, E. B and C rate pace 2; A, D and E 3.
   - **What happened:** Part 1's headings add to 57 minutes against Wednesday's 50, and Part 2's to 46 against Friday's 35, before any Discuss box. Step 4 is five numbered items, each several clicks, in 12 minutes: unzip, a new repository, upload, edit a file in the browser, create a file with a dotted path and paste into it. C, D and E each put Steps 4 and 5 at 25 to 30 minutes for a first-timer. Step 1 is six typed cells and a Discuss box in 9 minutes, then its own 4-minute microsprint (D). B estimates Part 1 at 85 to 100 minutes and Part 2 at about an hour.
   - **Why it matters:** Step 5's first run is what makes Steps 6, 10 and 11 possible, and the GitHub steps are the ones a student like A or B can least rush. Step 11 also waits on GitHub's queue.
   - **Proposed fix:** the minutes are the instructor's decision. The personas' candidates:
     - Mark one microsprint a part as "if time": B and C would choose Part 2's midnight rows; C also the forecast's age in Part 1.
     - Make Step 10's last two cells (one's own series, the forecast's age) homework (B).
     - Give Step 4 20 to 30 minutes, or start Step 5 at a fixed clock time (C, E).
     - Make Step 1's "keys, then keys of properties" cell given (D).
   - **Status:** verified: the headings in the key sum to 50 + 7 and 36 + 10; `docs/course-facts.md` gives Wednesday about 50 minutes and Friday about 35 before its 15-minute block. The persona estimates are their own.

7. **The numbers in the text are the key's run, and the series has already moved on.**
   - **Who:** B, C, D, E.
   - **What happened:** the key was run at 18 runs and 2,808 rows; the reviewed file has 19 runs and 2,964 rows, and by Friday it will have more. The Discuss boxes of Steps 8 and 10 and the Step 12 answers do say "in the key's run", and Step 7 says the file is "still growing". But nothing tells a student that their own counts will therefore differ from what is projected, and the key's saved outputs (18 runs; noon from 137 hours ahead to 22, where the reviewed file gives 16) are what the instructor shows. The chapter's frozen copy (18 runs, its example at 3 p.m. on November 17) and the lab's live file (noon on November 18) also differ, so Exercise Step 6's answer is 5 in the chapter and 6 in the live file (C).
   - **Why it matters:** "When my number differs from the page's, I check my own code first" (D). B would assume the mistake was B's own, and spend the Friday minutes looking for it. The labels are there; a student with little Python doesn't connect them to their own screen.
   - **Proposed fix:** the instructor's decision between two:
     - B: run Steps 8 and 9 on a dated copy, as the book does with `data/ch-14/forecasts.csv`, and keep the live file for Step 10, where its growth is the point.
     - D and E: keep the live file and add one line to Step 7: "your counts will be a little larger than the key's, because the file grows".
   - **Status:** verified: the reviewed file has 19 runs, 13 forecasts, 2,964 rows, 19 noon rows from 136.6 to 16.1 hours ahead, and 6 runs that found the previous run's forecast; the key's saved outputs and labels are as quoted.

8. **Exercise Steps 3 and 5 don't fit together: the workflow they produce would fail.**
   - **Who:** B, D, E.
   - **What happened:** Step 3 says to change `FILE` "to a name of your own" and to work in a notebook cell. Step 5 says to write a workflow for "your collector" and "keep the commit step". The template's workflow runs `python collector.py` and commits with `git add forecasts.csv`. A student who keeps both lines gets a run that fails at `git add` with a pathspec error, after the collector has run, and has no `collector.py` to run in the first place (E). B saw it only on rereading the two answers side by side.
   - **Why it matters:** it is "the exact kind of silent coupling between three files" the chapter's Failures section is about (E), and nothing in either step names it.
   - **Proposed fix:** chapter, Exercise Step 5: "change `git add forecasts.csv` to your own `FILE`, and run your own script". Step 3: "save the cell's code as a file too, if you will run Step 5".
   - **Status:** verified: the two steps' text at `90fd7ef` and the template's commit step.

9. **The Recommended Exercises start with no setup cell, and the chapter and the lab disagree on whether they are turned in.**
   - **Who:** B, C.
   - **What happened:** in the companion notebook the exercises follow 45 cells of the chapter, and none of the exercise cells imports anything. Starting at the exercises gives `NameError: name 'requests' is not defined`; Step 3 needs `csv`, `os` and `datetime`, and Step 4 `pd`. Separately, the chapter's exercises open with "This guided exercise is the chapter's take-home assignment … submit the completed notebook"; the lab's opening says "Nothing here is turned in", and Step 12 says the exercises are "practice, not turned in".
   - **Why it matters:** the exercises are done at home. A student who read the chapter first would submit; one who read the lab would not.
   - **Proposed fix:** chapter: one given cell above Step 1 that sends nothing, with the imports and `HEADERS`. Lab key, Step 12 (cell 68): "the chapter says to submit; this term, don't". Whether the chapter's sentence should change is the instructor's call, since the book serves other terms.
   - **Status:** verified: the companion notebook at `90fd7ef` (imports only in the chapter's cells); `docs/course-facts.md`, "The week, and what Notebook Labs grade": week 14's Recommended Exercises "are practice, not turned in" (the instructor, 2026-11-13).

10. **Part 1 depends on a Canvas zip whose upload is not recorded as done, and nothing prints the README.**
    - **Who:** C, D.
    - **What happened:** the opening cell and Step 4 send students to "this week's Canvas module" for `boulder-forecast-template.zip`. `docs/course-facts.md`'s row for the template says "Canvas, week 14's module (the zip, uploaded by hand; not yet done)". Step 3's given cell prints `collector.py` and Step 4's prints the workflow from the course repository, but no cell prints `README.md`, so a student without the zip can paste two of the three files.
    - **Why it matters:** without the zip, Step 4 can't start as written. C adds that download, unzip, the Mac's hidden folder and replacing GitHub's README teach nothing.
    - **Proposed fix:** check the Canvas module before Wednesday, and update the course-facts row. Add a given cell to Step 4 that prints the template's `README.md`, so the zip becomes a convenience, not a dependency. Optional: make the template a GitHub template repository, so "Use this template" replaces most of Step 4 (C, D).
    - **Status:** verified: course-facts and the key at `576551b0`; the zip in the repository matches the template file for file. Whether it is on Canvas now is outside the repository: a check for the instructor, not verified either way.

11. **The template's README and workflow comment still say "every hour".**
    - **Who:** D.
    - **What happened:** the README students put in their repository is titled "Boulder's hourly forecast, collected every hour" and says it saves the forecast "once an hour"; `collect.yml`'s first line is "Run collector.py every hour on GitHub's computers". #213 changed the lab and deck to say the workflow is scheduled every hour and GitHub runs it three or four times a day; the template was left as it was.
    - **Why it matters:** Step 12's last question asks what a README must say so someone can tell "when and how your data were collected". The one students are handed answers it wrongly.
    - **Proposed fix:** `labs/week-14/template/README.md` (the title and "once an hour") and `collect.yml`'s first comment: "scheduled every hour; GitHub may run it far less often, so use `collected_at`". Then remake the zip, as course-facts says, and upload it again (item 10).
    - **Status:** verified at `576551b0`.

12. **The likeliest slips in Step 1 give errors that don't point at the fix.**
    - **Who:** B, C; A for a smaller one.
    - **What happened:**

      | Slip | What comes back | Where the help is | Who |
      |---|---|---|---|
      | `requests.get(points_url, HEADERS)`, headers as the second argument | 400, `detail` "Bad Request". The useful message is in `parameterErrors`: `Query parameter "User-Agent" is not recognized`, which the lab asks for only in the microsprint after Step 1 | nowhere in Step 1 | B, 8 minutes |
      | `.json` without `()` | `AttributeError: 'function' object has no attribute 'get'`, then `'method' object is not subscriptable`, then `NameError: name 'grid' is not defined`: four red cells from one slip | the slide's code | B, C |
      | `grid["relativeLocation"]["city"]` | `KeyError: 'city'` | the prompt names `properties`, which A skimmed | A, 2 minutes |

    - **Why it matters:** A and B can't read a traceback beyond its last line, and these last lines point elsewhere. C: "a minimal student would think the whole notebook was broken".
    - **Proposed fix:** lab key, cell 8: print `points.get("detail")` and `points.get("parameterErrors")` from the start. Step 1's text: "`headers=` has to be spelled out", and "if a later cell says 'function' or 'method' object, you left `()` off `.json`; fix it and run the cells below again".
    - **Status:** verified: the 400 and its `parameterErrors` text by sending the request with the headers as the second argument; the two error texts by running the slip. The minutes are the personas'.

13. **When a GitHub step goes wrong, or a student has no repository, the lab doesn't say what that looks like.**
    - **Who:** A, C; E for running the script first.
    - **What happened:**
      - A file saved as `github/workflows/collect.yml` (no dot) gives no workflow and no error. The chapter's Common Issues covers it; the lab's Step 5 doesn't (A).
      - Steps 6 and 10 read `https://raw.githubusercontent.com/<you>/…`. Before the first run finishes, or with the angle brackets kept, `pd.read_csv` raises `HTTPError: 404`, and only a Discuss box asks what that means (A, C).
      - Step 7 says a student who missed Wednesday can start there, but Step 10's third cell and Step 11's break-and-fix need a repository (C).
      - The script's first run is on GitHub's computer. The lab never runs `collector.py` locally, as the chapter's "Running It" does, so a typo made in the browser editor becomes a red X to read in a log (E).
    - **Proposed fix:** lab key: Step 5, "no workflow on the Actions tab? check that the file's path starts with `.github/`"; Steps 6 and 10, "a 404 means no run has finished yet, or the address has a typo: look at the Actions tab"; Step 10, a line for a student with no repository (check the course's series twice and go on to Step 11's first half). E's local run, a given cell after Step 3 that saves `collector` to a file and runs it once, costs about a minute and adds to item 6.
    - **Status:** verified by reading cells 30, 33, 38, 60 and 63 and the chapter's Common Issues. What GitHub shows for each slip is reported, not verified: no repository could be made.

14. **The template's workflow has no guard against two runs at once.**
    - **Who:** E.
    - **What happened:** the commit step runs `git pull --rebase` and `git push`, and the workflow has no `concurrency:` key. A student who presses Run workflow near a scheduled run gets two runs appending to the end of the same file; E expects the second rebase to conflict and the run to fail.
    - **Why it matters:** pressing the button in class at minute 17 is a realistic way to get it. The chapter's Common Issues explains a rebase conflict only as someone editing `forecasts.csv` by hand.
    - **Proposed fix:** template `collect.yml`: `concurrency: {group: collect, cancel-in-progress: false}`, with a comment; one line in the chapter's Common Issues. Remake the zip.
    - **Status:** the missing key is verified; the conflict is reported, not tested.

15. **Two given cells work for reasons the lab doesn't say.**
    - **Who:** E.
    - **What happened:** Step 8's given cell takes `min` and `max` of `collected_at` as text, which works because ISO 8601 times sort in time order. Step 9 matches `start_time == "2026-11-18T12:00:00-07:00"` as text, and its given plot needs `utc=True` because the two columns carry different offsets; the lab doesn't explain either, and a match on `-07:00` stops working when Boulder moves to `-06:00` in March.
    - **Why it matters:** E is the student who copies given cells into a project, and would copy the offset.
    - **Proposed fix:** lab key: one sentence in Step 8 ("ISO times sort as text, so `min` and `max` work") and in Step 9 ("the two columns have different offsets, hence `utc=True`; a fixed offset works only until the clocks change").
    - **Status:** verified by reading cells 44, 51 and 52.

16. **Nothing connects the week to sources that aren't a JSON API.**
    - **Who:** B.
    - **What happened:** the week's source is one JSON API with eight fixed columns. B's project uses council agendas, a county web page and PDFs, and B couldn't tell what `collector.py` would save for a page: all the text, a hash, a date. Step 12's last question asks students to describe how their own data were collected.
    - **Why it matters:** B's confidence rating (2) is held down by this alone.
    - **Proposed fix:** a short box in Step 12 or the chapter's "Committing Data Back: Git Scraping": "adapting this to a page that changes": save the page and a timestamp only when it differs from the last copy, what goes in `FIELDS`, and which of the four parts of `collector.py` change. No new typed code.
    - **Status:** reported; a judgment about scope, not checkable.

### Corrections

Claims in the reviews that turned out wrong, out of date, or inexact, and what this document does with them:
- **A's three main findings were fixed by #213.** A reviewed `efc1e367`, before #213. At `576551b0`:
  - "Every hour": the opening, Steps 5, 7 and 9, End of Part 1 and the deck say "scheduled every hour", then three or four times a day as GitHub runs it.
  - Step 8's arithmetic: the forecasts-over-runs microsprint (0.72, "520 of 720") is gone; Step 8 now computes changes a day (2.4) and the microsprint 67 of 672, which agrees with the chapter's "about 67 times, one request in ten" and the deck.
  - Step 10's 1.5-hour rule is gone; the longest gap is the yardstick.
  - Step 9's "up to about 156 times" now reads "a few times a day as GitHub runs ours".
- **A: the exercise "doesn't warn" that the gap check fires everywhere.** At `90fd7ef` it does: "Expect the first check to report many gaps". The empty-column half of A's finding stands (item 5).
- **A's chapter remarks** (`TODO(Tuesday refresh)` comments, a 6-run copy, "run it today: it reports 'no run since'") were made on an earlier draft. The chapter at `90fd7ef` has no TODO comments, uses the 18-run copy and explains the 2-hour limit. Dropped.
- **D: "the real lead of that forecast is shorter than the x-axis says".** Reversed: a forecast is issued before the run collects it, so measured from its issue time the lead is longer, by up to 10.8 hours in this series. Item 2's fix stands.
- **C and D: the Step 9 line "stops 16 hours short" of noon.** True of the file at the reviewed commit, whose newest run was 02:56 UTC on November 18. By Friday's class the file will hold that morning's runs, so the line will end within one gap of the hour. What remains is item 7: the key's "137 hours ahead to 22" won't match.
- **A, C, E: the template's `@v7` actions may not exist.** They exist; the course's own workflow uses them and has been committing. Dropped.
- **B: "Canvas lost the week-14 assignment".** The instructor deleted it on 2026-11-13, and course-facts says the exercises are practice. The lab is right; the chapter's generic "submit" is the mismatch (item 9).

## Disagreements

- **Too slow, or about right.** B and C rate pace 2 and estimate Part 1 at 65 to 100 minutes; D and E rate it 3 and call Part 2 "comfortable" and "well timed". On one thing they agree: C, D and E put Steps 4 and 5 at 25 to 30 minutes, not 18, and A and B, who couldn't time them, called 12 minutes for Step 4 tight. That suggests the time to find is in Step 4, not in the notebook, which is what the zip-free fixes of item 10 and the template repository would save.
- **What to cut.** B would make Step 10's last two cells homework and drop the Step 4 `permissions` question; C would mark microsprints "if time" and move Step 6 to Friday; D would keep Step 1's microsprint ("it was the microsprint that kept me thinking") and make a typed cell given instead; E would *add* a local run of `collector.py`, and budget 30 minutes for Step 4. They agree only that Step 4 needs more time.
- **A frozen copy or the live file.** B wants Part 2 on a dated copy, as the book does. E says keep the live file and add a line; D says label the key's numbers with their date. The live file is what makes Step 10 real, so the choice is about Steps 8 and 9 only (item 7).
- **Which address.** B: any address the student checks. D: a throwaway or a GitHub noreply address. E: a course or forwarding address. The NWS asks for a way to reach the program's owner, which rules out noreply, so item 1 proposes B's and E's wording.
- **Difficulty.** A, B and C rate it 3, D and E 2. The typed cells were fair for all five; the spread is in the exercises' Steps 3 and 4, "the hardest I've had in the course, with no cell given to start from" (B), which A, B and C each spent more than an hour on.
- **What the week is for.** For D the lesson is sampling (a schedule is not a sample plan); for E, tools; for A and B, provenance and the people who pay for the requests. D and E rate their confidence on a project 4; A and C 3; B 2, because nothing bridges to a page that isn't JSON (item 16).

## Ratings

Each on a scale of 1 to 5. For difficulty, 5 is hardest for that persona's background. A's ratings are of the version before #213.

| | A | B | C | D | E | Mean |
|---|---|---|---|---|---|---|
| Clarity of motivation | 4 | 4 | 5 | 5 | 5 | 4.6 |
| Pace | 3 | 2 | 2 | 3 | 3 | 2.6 |
| Difficulty for my background | 3 | 3 | 3 | 2 | 2 | 2.6 |
| How much I learned | 4 | 4 | 4 | 4 | 4 | 4.0 |
| Confidence I could do this on my project | 3 | 2 | 3 | 4 | 4 | 3.2 |

What holds the confidence down: A isn't sure it could debug a workflow that doesn't run; B can't see how to point the collector at a council page or a PDF, and fears the quiet corruption of item 4; C never did the GitHub steps in class; D can't yet choose a polling interval or say how much a schedule missed (items 2 and 3); E would lack retries and concurrency handling (item 14) and a way to test a workflow without pushing.

## Small things

Deck (`slides/week-14/week-14.tex`):
- "Other places to run a schedule" lists Val Town and not Amazon EventBridge or Render; the chapter's table lists those two and not Val Town (B, C, E).
- "cron on your own computer" shows `python3` without a full path; its note covers it, but the line as shown is the one that fails under cron for a conda student (B).
- "collector.py: constants at the top" splits `URL` across two strings; the file has one, and Step 11 says to edit `hourly` in `URL` (B).
- "Before Friday" says a run that never started leaves no line, but not what to do: press Run workflow again (B).
- The section dividers repeat page counts, "1 of 76" (C; reported, not verified).
- The daily-note placeholder comment is still in the source, as expected before class (E).
- Found while verifying: `run-workflow.png` ("Step 5: start the first run") and `failed-run.png` ("Step 11: break your collector") are still gray placeholders, per `img/IMAGES.md`; `check_deck_readiness.py week-14` reports both (#213 doesn't touch the images). It also reports no "good-faith attempt" sentence, which may not apply to a week with no graded lab.

Lab (`labs/week-14/lab-14-key.ipynb`):
- Step 1, cell 10: "(two levels down)" after "relativeLocation's properties" would have saved A's `KeyError` (A).
- Step 4, item 1: ".github … out of sight on a Mac": on Windows a student sees three items where the line says two (B).
- Step 8's microsprint (cell 48): "all rounded" doesn't say to how many places; the key rounds to 0 and 2 (B).
- Step 9, cell 51: the prompt could say "equal to (`==`)"; B typed `=` and Python's own message helped (B).
- Step 9's text calls noon on November 18 "our first class"; on Friday that hour has passed (D).
- Step 10, cell 59: the prompt doesn't repeat `tz="UTC"`, which the step text gives; without it, `TypeError: Cannot subtract tz-naive and tz-aware datetime-like objects` (B).
- Step 10, cell 61: the forecast's age has no yardstick in the lab; the chapter's "oldest forecast any run saved", 10 hours 45 minutes, is one (D).
- Step 7: `wind_direction` is empty in 364 of the reviewed file's 2,964 rows, every one where `wind_speed` is "0 mph", and the last rows `tail()` prints are among them. One line in Step 7 and in the data and template READMEs: "empty when the wind is calm" (A, D, E).
- `collected_at` is kept to the second, so two local runs in the same second count as one run; Exercise Step 3's "two runs" needs a pause between calls (A).
- The opening, Step 5 and End of Part 1 say "every hour as written … three or four times a day" three times in the first screens; once is enough (E).
- `your-email@colorado.edu` is typed in five places (Steps 0 and 7, `collector.py`, the chapter, the exercises); Step 7 could say "the same address as Wednesday" (E).
- The swapped grid's first temperature depends on the hour, so neighbours' "Share" answers won't match (D).

Chapter and companion notebook (`ch-14-automation.qmd` at `90fd7ef`):
- Exercise Step 5: "give each line of the `cron` expression's meaning": it is one line with five fields (C).
- "When Did the Runs Actually Run?": "The 16 scheduled runs asked between 12 and 54 minutes past it" is right, but the printed list has 18 values, the first two (6 and 14) the hand-started runs (E).
- Exercise Step 2 asks what the two products' update times suggest "about how they are made"; A couldn't tell what answer is wanted. For Grand Junction, `Last-Modified` equalled `updateTime`, unlike Boulder's top-of-the-hour value (A).
- The lab says `points`, `grid`, `hourly`; the chapter `point`, `forecast`. Copying between them breaks (C). The deck's Step 8 frame names a `runs` object that the chapter uses for something else (D).

## Suggested next step

**Fix first.** Each is small and changes none of what the week teaches:
1. **Item 1:** one sentence before Step 4's email edit, in the lab and the deck, and in Step 0: the address will be public for good; any address you check will do.
2. **Item 2:** `ax.step(..., where="post")` in Step 9's given cell and its frame, one typed `nunique()` line, and one sentence that runs repeat forecasts.
3. **Item 3:** "at least" in Step 8's text, its microsprint, Step 12's first bullet, two deck frames, and Exercise Step 4.
4. **Items 10 and 11:** check the Canvas zip; fix the template README's title and "once an hour" and the workflow's comment; remake and re-upload the zip; add a given cell that prints `README.md`.
5. **Items 4, 5, 8 and 9 (the chapter's exercises, one pass):** a setup cell; "copy the imports", "both `FIELDS` and the dictionary", "delete the file after a failed run" in Step 3; thresholds first, the empty-column check, and "some of one run's rows" in Step 4; "your own `FILE`" in Step 5. These are textbook changes, for #310 or the pull request after it.

**Needs the instructor's decision:**
- **The minutes** (item 6): 57 against 50 and 46 against 35, and what becomes "if time" or homework; the personas agree only that Step 4 needs more than 12 minutes.
- **A frozen copy for Part 2, or the live file with dated numbers** (item 7).
- **Whether the chapter's "submit the completed notebook" changes**, or the lab alone says "not this term" (item 9).
- **A template repository** in place of the zip (item 10), and a `concurrency:` key in the template (item 14), each of which means remaking the zip.
- **A bridge to non-JSON sources** (item 16): a box in the lab or the chapter, or nothing this term.
