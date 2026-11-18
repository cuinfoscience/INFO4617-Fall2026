# Review: week 11, Government Data APIs

**What was reviewed:** week 11's lab (`labs/week-11/lab-11.ipynb`, with its key), its deck (`slides/week-11/week-11.tex`), the four checkpoints in `labs/week-11/data/`, and chapter 11's Recommended Exercises, as students meet them. This is the version for the next offering; the term's week 11 was taught October 26–30.
- **Course repository:** the head of pull request #201, `1d3f270da6fae3661fa99d76e2dd9cc683b2ecea`, which revised the lab and rebuilt the deck in the incremental style. It is open and not merged, so every fix below names the file on that branch.
- **Textbook:** `ch-11-government.qmd` and its companion notebook, `notebooks/ch-11-government.ipynb`, at `main`, `3f9cf2cef801181236c9cceaf71f3b63c3ad2491`.

**When:** 2026-11-18.

**Method:** five anonymous composite personas, each a kind of student this course has, reviewed the week independently. Each read the chapter and the slides, typed and ran its own code for every lab step from the students' copy, made the mistakes its background makes, attempted the Recommended Exercises, and opened the key only after an honest try. Each review is a **steel man**: it first makes the strongest case for the materials as designed, and only then says where they fall short for that student. This document puts the five together. Every ranked finding was then checked against the repository and the textbook, and is marked **verified** (with how) or **reported, not verified**.

## Who reviewed

| | Degree and major | Python and data background | Interest | Skill |
|---|---|---|---|---|
| A | BS senior, Information Science | One intro Python course; spreadsheets | Qualitative and design: online communities, UX | Minimal |
| B | BA junior, Journalism and Communication | No Python before this course; strong with public records and Excel | Data journalism, local government | Minimal |
| C | BS senior, Business Analytics | Excel, some SQL, a little pandas | Quantitative analytics: markets, customer data, dashboards | Minimal to moderate |
| D | MS first year, Data Science (BA in Statistics) | Fluent in R, moderate pandas; regression and sampling | Quantitative: measurement and validity | Moderate |
| E | MS first year, Information Science (BS in Computer Science) | Moderate Python, git; little data analysis | Design and tools: automation, APIs, building things | Moderate |

## What each completed

The lab has Steps 0–14 and seven microsprints: Part 1 (Monday) is Steps 0–4, Part 2 (Wednesday) Steps 5–8, Part 3 (Friday) Steps 9–14, then the 15-minute portfolio checkpoint. All five finished every step and every microsprint live, against the Census and FRED APIs. None needed a checkpoint or the key. All five read Friday's portfolio checkpoint and didn't do it, and read the EIA "on your own" section without running it.

| | Lab steps finished | Their own slips, fixed | Recommended Exercises | Needed the key for |
|---|---|---|---|---|
| A | 0–14; all seven microsprints | 4: Step 1's `groups` cell, Step 3's DataFrame (item 4), Step 7's `margins(0)`, Step 10's `.get[...]` | Steps 1–6 (internet subscriptions by county, then a share) | Nothing |
| B | 0–14; all seven microsprints | 2: `.json` without `()` (cell 10), `=` for `==` (item 3) | Steps 1–6 (median gross rent, `COSTHPI`) | Nothing; compared afterwards |
| C | 0–14 (Step 14's answers drafted, not typed); all seven | 2: `os.environ("CENSUS_KEY")`, `sort_values()` without a column | Steps 1–5; Step 6 drafted (median home value) | Nothing |
| D | 0–14; every typed cell right the first time | None | Steps 1–5; Step 6 written (median household income) | Nothing |
| E | 0–14; all seven | 3: `.json` without `()`, Step 3's DataFrame (item 4), `str.contains` without `case=False` | Steps 1–6 (median gross rent, `COSTHPI`) | Nothing |

**Estimated time for a real student of that background, in minutes** (the lab's own step minutes, which `labs/AUTHORING.md` says include the microsprints and the discussion, in the last rows):

| | Part 1 | Part 2 | Part 3 | Exercises |
|---|---|---|---|---|
| A | 80–90 | 65–75 | 50–55 | 90–120 |
| B | 80–100, of which 20–40 for keys; about 50 if the keys work | 65 | 55 | 120 |
| C | 70 | 60 | 50 | 90–120, plus 30 for a variable that misbehaves (item 2) |
| D | 45 | 50 | 30 | 75 |
| E | 50–60 | 45 | 35, plus 5 for Step 14 | 60–75 |
| **The lab** | **51** | **51** | **38** | none given |
| **The day** | **50** | **50** | **35**, then the 15-minute portfolio checkpoint | due Sunday, November 1 |

## Environment blocks

These come from the review machine, not from the materials. They are kept apart so that none is read as a flaw in the week.

- **None stopped a request.** Census and FRED answered every request from every persona, with no 429s. The key has no cell tagged `not-run-live`, so no persona read a saved output in place of a live one, and none loaded a checkpoint.
- **Both keys were already set on the review machine.** So no persona signed up for a key, clicked the Census activation email, ran `conda env config vars set`, or restarted Jupyter, and the `getpass()` cells (4, 49, 82) ran and did nothing. Item 16 is a reading of those instructions, not a test of them.
- **No GitHub repository could be made,** so Friday's portfolio checkpoint was read, not done (all five).
- **`api.census.gov/robots.txt` answered the review machine with a "Request Rejected" page** (B, D), so its rules couldn't be read; the API itself answered normally, and the personas used only the documented keyed paths, as the lab does. FRED's `robots.txt` allows everything with a 2-second crawl delay, and the personas paced their calls 1 to 2 seconds apart.
- **Two live numbers differ from the key's text,** as expected of live data: Step 12's Discuss box says 1,356 months come back for the `observation_begin` typo, and E got 1,366; FRED's `realtime_start` and `realtime_end` show the day of each run (item 18).

## The strongest case for the week as designed

**Every new service starts with an answer the student can check by eye.** All five said so. Step 3 asks for Colorado's `NAME` alone and the step text says what to expect, `["NAME","state"]` and `["Colorado","08"]`; then Boulder County comes back as `"103994"` and `"2268"`, the website's \$103,994 ± \$2,268 from Step 1. Step 10's one year is `"103293"`, in quotes. Step 12's three months average to 310.358 on a calculator. For B, the records reporter, "I trust a source I can reconcile against something I've seen with my own eyes"; for D it is "have an expected value before you scale up"; for E "an API is a function you probe with the smallest input first". C called it "how an analyst audits a pipeline".

**The Step 4 microsprint teaches why a 200 isn't enough, by making students break the request.** All five ran the four mistakes and got what the lab promises: a 204 with an empty body, a 400 with `unknown variable 'B19013_01E'`, a 400 with `unknown variable ''`, and a 200 that is an HTML "Invalid Key" page. A called it "the most useful five minutes of the week"; D "the best single activity"; B said the Discuss question is "an actual lesson for someone who will someday cite a government number in print". The habit it builds, printing `status_code` and `text[:200]` before `.json()`, carried into the exercises for A, C and E. The 400 for the city without `in` (Step 4, cell 38), "ambiguous geography … specify a wildcard or full qualify it with state", taught B the geography rule "better than any paragraph".

**The typed and given cells are split where they should be.** Every typed cell was one to four lines, and no persona had to write a loop or a function (all five). Each given function arrives after its lines were typed by hand: `look()` is "the two lines you just typed", `census_get()` "Monday's by-hand cells, as one function", `fred_observations()` "Step 10's lines". A could find each of its own lines inside `census_get()`; C "never felt a function arrive from nowhere"; E, who would otherwise write the helper first, valued "being made to see the raw list-of-lists before it was hidden".

**The data-quality lessons land in the right order.** Step 8 shows Branson's `-666666666` in a table of two, then hides it in 482 places, where `describe()` gives a mean of −235 million, before `mask()` is introduced (A, B, C, D, E). A "felt the problem before I was told the cure"; C called it "the most memorable 'garbage in' moment of the term". Step 7's margin of a difference, 3,178 against 6,896, gave A, who doesn't think in statistics, a sentence to say. And Step 12's check, "look for a missing month before you trust a yearly average", found something real: October 2025 is `NaN`, so 2025's mean is of eleven months (C, D, E). The checkpoints exist and match the live counts (1,199 groups, 482 places, 132 months), which made the live hour safe for E.

**Step 14 maps each Recommended Exercise to the lab step that prepares it,** and all five ran Steps 1–5 and answered Step 6. B, who had no Python before this course, did all six.

## Where it falls short, ranked

The problem that can print a student's key comes first, then the ones that give a wrong result without an error. After them, items are ranked by how many personas hit each, how badly, and whether it stopped A or B. Cell numbers are positions in `labs/week-11/lab-11-key.ipynb` at `1d3f270d`, counted from 0; the students' copy has the same cells and is made from the key by `labs/tools/make_student_copy.py`, so every lab fix is made in the key and the copy regenerated.

1. **A failed request in the chapter's code prints the student's key, and the obvious fix to the lab's FRED function would too.**
   - **Who:** found while verifying items 5 and 12; no persona hit it, because the lab has no `raise_for_status()`. A and E point to the chapter's version of `fred_observations()` as the better one.
   - **What happened:** the Census and FRED APIs take the key in the URL (`key=`, `api_key=`). The chapter calls `response.raise_for_status()` after every request (its `fred_get()`, `fred_observations()`, and each Census call). On a 4xx, that raises `HTTPError: 400 Client Error: Bad Request for url: …&api_key=<the key>…`: the message holds the whole URL. A wrong series ID or a misspelled variable, the likeliest slips in Exercise Steps 2 and 5, is a 400. The Step 4 Discuss box (cell 45) points students to `raise_for_status()` without saying this.
   - **Why it matters:** the companion notebook is submitted, and Notebook Labs grade "run with output visible", so a failed cell left in hands the key to the grader, and to everyone if it reaches a public portfolio repository. The lab and chapter both say a key is never printed.
   - **Proposed fix:** chapter and companion notebook: replace `raise_for_status()` with a check that doesn't print the URL, e.g. `if not response.ok: raise RuntimeError(f"{response.status_code}: {response.text[:200]}")`, and add a line to "Common Issues": "a traceback from `raise_for_status()` holds the URL, and so your key: clear the output before you submit". Lab key, cell 45, second bullet: add "and what would its message print?". Item 5's fix to the lab avoids `raise_for_status()`.
   - **Status:** verified: the chapter's calls at `3f9cf2c`; the message format by raising `HTTPError` on a response with a placeholder key. That FRED answers a wrong ID with a 400 is reported (A saw `"error_code":400` in the body).

2. **`census_get()` leaves C-table variables as text, so a student's ranking comes out wrong with no error.**
   - **Who:** C, D; E.
   - **What happened:** the given function (cell 52) converts only columns whose names start with `B`. The catalog Step 1 searches holds 1,199 groups, 90 of them C-tables (D's own `find_groups("poverty status")` returned `C18130` and `C21007`). A C-table's columns stay strings, and `sort_values()` sorts them as text: `"9807"` comes before `"250000"`, which comes before `"10512"`. C tried `C18108_001E` for Colorado's counties and got Yuma County (9,807) first, ahead of larger counties. Step 6's text says the function converts "each name starting with `B`" without calling it a shortcut.
   - **Why it matters:** Exercise Step 2 says to browse the catalog for a variable, and Step 14 sends students to Steps 3 and 8's code. A student who picks a C-table, or copies `census_get()`, gets a plausible wrong ranking and hands it in.
   - **Proposed fix:** lab key, cell 52 and the deck frame "Step 6: Monday's cells, given": `if column not in ("NAME", "state", "county", "place"):` in place of `if column.startswith("B"):`. Step 6's text (cell 51): "turns every column but the name and the place codes into numbers". Optional: a Step 8 Discuss line, "How would you check that every number column is a number?" (`dtypes`).
   - **Status:** verified: cell 52; `lab11_groups.csv` has 1,109 B and 90 C groups; the text sort reproduced locally. C's Yuma County result is reported.

3. **Typing `=` for `==` in Step 8 overwrites the rent column, and the error points elsewhere.**
   - **Who:** B.
   - **What happened:** cell 72's prompt says "True where `B25064_001E` equals -666666666". B typed `no_estimate = places["B25064_001E"] = -666666666`. Python set every place's rent to −666666666 and `no_estimate` to that integer, then stopped on the next line with `AttributeError: 'int' object has no attribute 'sum'`. The ruined `places` isn't mentioned. The only repair is to rerun cell 69's request; the checkpoint (cell 70) is offered "only if the cell above stopped". The lab uses `==` nowhere before this cell; the deck's frame "Step 8: count the code" shows `==`, but the prompt doesn't.
   - **Why it matters:** a student who reads only the last line tries variations of `.sum` and carries a corrupted table into `describe()`, `mask()` and the chart. The same slip is open in cell 77 (`capped`).
   - **Proposed fix:** lab key, cells 72 and 77: "equals (`==`, two equals signs; one would overwrite the column)". Cell 70: "or if you changed `places` by mistake".
   - **Status:** verified: the prompt; the assignment and the `AttributeError` reproduced on `lab11_places.csv`.

4. **Leaving out `columns=` in Step 3 builds a wrong table silently, and the error comes a cell later.**
   - **Who:** A, E.
   - **What happened:** cell 32's prompt says "a DataFrame of `county_rows[1:]`, with `county_rows[0]` as its columns". Both typed `pd.DataFrame(county_rows[1:], county_rows[0])`. The second positional argument is the index, so pandas made a 5×5 table indexed by the column names, every row the same, with no error. Cell 34 then raised `KeyError: 'B19013_001E'`, which A read as the API renaming its variable. The deck's "Step 3: rows to a table" shows `columns=` on a line of its own, with "The notebook writes this call on one line".
   - **Why it matters:** it is Monday's first DataFrame, and the error points at the wrong cell for a student who reads only the last line.
   - **Proposed fix:** lab key, cell 32: "…with `columns=county_rows[0]`; show it, and check that it has one row".
   - **Status:** verified: the prompt and the deck frame; the 5×5 table and the `KeyError` reproduced.

5. **The given `fred_observations()` hides the error FRED sends, one step after the lab taught students to read it.**
   - **Who:** A, E; D on the missing status check.
   - **What happened:** Step 10 (cell 88) prints FRED's `error_message`. The given function in Step 11 (cell 99), reused in Steps 12 and 13 and the exercises, goes straight to `response.json()["observations"]`. A typed a wrong series ID in the exercise and got `KeyError: 'observations'`; the body said "Bad Request. The series does not exist." E got the same `KeyError` from a wrong ID (`CPIAUCNZ`) and from `units="chng"`. Step 11's text says the function is "as the chapter's does", but the chapter's has `timeout=30` and `raise_for_status()`.
   - **Why it matters:** Exercise Step 5 has students type a series ID they found themselves, so a typo there is the likeliest mistake of the take-home, and the error names pandas, not the ID.
   - **Proposed fix:** lab key, cell 99, and the deck frame "Step 11: Step 10's lines, given": `data = response.json()` and `if "observations" not in data: raise ValueError(data.get("error_message"))`, two lines, not `raise_for_status()` (item 1). Step 11's text (cell 98): "a shortened version of the chapter's". The same two lines in the chapter's function would serve item 1 too.
   - **Status:** verified: cells 88 and 99, and the chapter's function at `3f9cf2c`. The error bodies are reported.

6. **Step 8's chart ranks three places that are tied at the cap, and draws them as the most precise.**
   - **Who:** C, D.
   - **What happened:** the top three of the given chart (cell 75) are Altona, Sterling Ranch and Bow Mar, each at 3,501, "\$3,500 or more", in the order `sort_values` happened to leave them (cell 74). Their margins are the `-333333333` code, which the cell masks, so they have no whisker, and look more certain than the bars with one. The title is "Highest median gross rent". The Discuss box (cell 78) asks which of the ten could be ranked, but the chart is what a student would paste into a project.
   - **Why it matters:** the week's warning is in the text, and its own chart contradicts it (D). C would put the chart in a deck as it is.
   - **Proposed fix:** lab key, cell 75: draw the capped bars in another colour or label them "\$3,500+ (capped)", and add "top three tied at the \$3,500 cap" to the title. The deck frame "Step 8: the highest rents" shows the table, not the chart; its question could add "three are tied at the cap".
   - **Status:** verified: cells 74, 75 and 78.

7. **October 2025 is missing from the CPI, and nothing says why; the chapter says each year is "twelve months".**
   - **Who:** A, B, D; C and E found the gap and praised the check.
   - **What happened:** cell 111 shows one missing month, 2025-10-01. The Discuss box (cell 117) and the deck's "Step 12: a missing month" ask "Why might it be?", and neither the lab nor the chapter answers. The chapter's FRED section says `frequency="a"` turns "each year's twelve months into their mean", twice, and its "132 months" includes the empty one. Step 13's bars carry 2025 with no mark. `CPIAUCNS` isn't seasonally adjusted, so a mean that drops October isn't a neutral 2025 average (D).
   - **Why it matters:** A and B want the people and events behind the data, and a federal price index with a hole in it is the week's best example. Without the reason, "look for a missing month" is a pandas chore. The chapter's "Social History" section covers staff cuts and the firing of the BLS commissioner, but not this.
   - **Proposed fix:** lab key, Step 12's text (cell 105) or Discuss (cell 117): one sentence giving the cause with a link to the Bureau of Labor Statistics' notice. The likely cause is the lapse in federal appropriations of October–November 2025, during which October's prices weren't collected; no persona would guess it, so the instructor should confirm it and choose the citation. Chapter: "the months FRED has" for "twelve months", and the same sentence. Step 13's given cell (cell 119): mark 2025 ("2025*") on the axis.
   - **Status:** verified: cell 111's output and `lab11_cpi_monthly.csv` (132 rows, one `NaN`, 2025-10-01); no mention of October 2025 in the lab, the deck or the chapter. The cause is not verified here.

8. **Step 7 gives a margin of the difference but no way to decide.**
   - **Who:** C, D.
   - **What happened:** cells 63 and 64 print 3,178 and 6,896, and the text ends "A difference smaller than its margin may be no difference at all". It says the margins are at 90% confidence, but not that a margin divided by 1.645 is a standard error, what ratio counts as a real difference, or that the formula assumes the two estimates are independent (fine for two cities, not for a city and its county). C computed 0.46 margins; D 0.76 standard errors.
   - **Why it matters:** "so is it significant?" is the question C and D would ask, and the step is where they'd learn to say it. D would not write "differs" in a report without a rule.
   - **Proposed fix:** lab key, cell 64, a typed line `print(difference / margin_of_difference)`, and in cell 62: "Above 1, the difference is larger than its margin at 90% confidence; below 1, you can't tell. The rule assumes the two estimates are independent." Same in the deck's "Step 7: the difference's own margin".
   - **Status:** verified: cells 62–65.

9. **Exercise Step 5 needs a skill the lab never practises: finding a FRED series.**
   - **Who:** B, C, D, E; A's typed ID is item 5.
   - **What happened:** Step 14 (cell 121) says "find the series on FRED's website, as Step 10 did", but Step 10 hands students `MHICO08013A052NCEN`. The chapter says to search the website and read the ID off the page; the exercise's examples ("unemployment rate, home price index, per-capita income") give no IDs. C and D used FRED's `series/search` endpoint, which neither the lab nor the chapter teaches; B knew `COSTHPI` from the site, and E chose it too. D then mislabelled the axis "2024 dollars" for a series in 2025 dollars, caught only by printing `units`.
   - **Why it matters:** this is the graded part, done at home. B put about 20 minutes into finding a series; D and E said most of their exercise time went to choosing a variable and a series.
   - **Proposed fix:** lab key, Step 14's Step 5 bullet: "search fred.stlouisfed.org for 'Colorado unemployment', copy the ID from its page, and ask the `series` endpoint for its title, units and frequency, as Step 10 did", with two example IDs. Or a three-minute microsprint in Step 10 that does the same. Chapter, Exercise Step 5: "print the series' `units` and put them on the axis".
   - **Status:** verified: cells 85 and 121; the chapter's "Finding Series IDs" and Exercise Step 5 at `3f9cf2c`. The minutes are the personas'.

10. **No part fits its day for a minimal student, and Step 8 is the tightest.**
    - **Who:** A, B, C, D, E. A and C rate pace 2.
    - **What happened:** the headings add to 51, 51 and 38 minutes against the day's 50, 50 and 35; Friday's deck frame says "Steps 9–14, about 35 minutes". A estimates 80–90, 65–75 and 50–55; C 70, 60 and 50; D and E fit. Step 8 is 21 minutes for a given cell, seven typed cells, a chart, a microsprint and three Discuss questions (B, C, D, E); Step 1 is 11 for five typed cells, a microsprint and three questions (C). B's Monday risk is the keys (item 16).
    - **Why it matters:** behind by Step 3, C would copy from the key, which turns the day into watching. D: a student short of time skips Step 8's Discuss, which holds the week's best question.
    - **Proposed fix:** the minutes are the instructor's decision. The personas' candidates: mark one microsprint a part "if time" (A: Step 12's `groupby`; D: Step 8's `-333333333`); give Step 8 two minutes from Step 9's setup (D); or raise the headings to match.
    - **Status:** verified: the headings in the key; `labs/AUTHORING.md` says step minutes include microsprints and discussion; `docs/course-facts.md` gives 50, 50 and 35. The estimates are the personas'.

11. **The deck says "Nothing to submit" on Monday and "Due Sunday" elsewhere.**
    - **Who:** D, E; B and C noticed it.
    - **What happened:** the frame "This week, every class is live coding" says **Nothing to submit**, "The lab is practice". "This week at a glance" and "Step 14: what did we learn?" say the Recommended Exercises are due Sunday, "graded on good-faith attempt to complete rather than getting everything working". `docs/course-facts.md` says Notebook Labs (30%) grade the exercises on five criteria, one of which is "each step does its task" (E).
    - **Why it matters:** a student who skims Monday's deck may not see what is graded, or may read "good-faith" as "anything goes".
    - **Proposed fix:** deck, Monday's frame: "Nothing to submit from the lab; the chapter's Recommended Exercises, due Sunday, are graded". The "good-faith" sentence, here and in the glance frame, is the instructor's call against the rubric.
    - **Status:** verified: the three frames and the course-facts rows "The week, and what Notebook Labs grade" and "Notebook Labs rubric".

12. **The exercises start with no setup, and running the chapter's setup asks for a third key.**
    - **Who:** C, E.
    - **What happened:** in the companion notebook the exercises are cells 75–85 of 112, and none imports anything or defines `HEADERS`, `census_base` or `fred_observations()`. Running only them gives `NameError`. The chapter's setup (cell 5) prints `EIA_KEY: MISSING` for a student without one, and its `getpass()` cell (cell 7) opens a box for `EIA_KEY` too. Running everything above fails at cell 9, which opens `api_keys.json`. E's `county:*` without `in` then returned 3,222 counties with a 200; only printing `len(rows)` caught it.
    - **Why it matters:** this is the graded notebook, done alone.
    - **Proposed fix:** lab key, Step 14's exercise bullets: "first run the chapter's cell that sets `HEADERS` and the keys, and copy `fred_observations()` from today's lab (with item 5's two lines)", and "`EIA_KEY` isn't needed: press Enter if asked". Chapter: a setup cell above Exercise Step 1, and in Step 2, "print how many rows came back: Colorado has 64 counties".
    - **Status:** verified: the companion notebook at `3f9cf2c`, cells 5, 7, 9 and 75–85.

13. **The slides print the answer to every typed cell.**
    - **Who:** B, E.
    - **What happened:** the Monday frames ("Step 3: the smallest request", "send it", "rows to a table", the microsprint) show each typed cell's code, with the lab's variable names, and the opening frame says "Fall behind? Copy the cell from the key and keep going". B wrote every Part 1 cell right the first time and suspects transcription; E's three slips are ones the slide would have prevented.
    - **Why it matters:** the Recommended Exercises, with no slide, become the first place a student finds out what they can't do alone (B).
    - **Proposed fix:** the instructor's decision: in a live-coding room the code is on screen as it's typed anyway. The personas' candidates: one "same question, another place or variable" cell at the end of Steps 3, 10 and 11 with no slide code (B; Step 6's microsprint already works this way); or a prompt frame before each answer frame (E).
    - **Status:** verified: the frames at `1d3f270d`.

14. **The exercises don't warn that a count mostly ranks counties by size.**
    - **Who:** A.
    - **What happened:** Exercise Step 2 asks for "one ACS variable you care about"; A chose households with an internet subscription, a count, and Step 4's top 20 was Denver, El Paso, Arapahoe, Jefferson, Adams: the biggest counties. Only Wednesday's microsprint ("counts don't compare fairly; shares do", cell 59) made A compute a share, which changed the ranking.
    - **Why it matters:** Step 6 asks what pattern the ranking revealed; a count's answer is "population".
    - **Proposed fix:** lab key, Step 14's Step 2 bullet: "a median or a share compares counties fairly; a count mostly ranks them by size (Step 6's microsprint)". Chapter, Exercise Step 2: the same half-sentence.
    - **Status:** verified: cell 59 and the exercise's text. A's rankings are reported.

15. **Nominal and inflation-adjusted dollars sit side by side and nothing separates them.**
    - **Who:** C; D for the dollar year.
    - **What happened:** Step 2's variable is "in 2024 inflation-adjusted dollars"; Step 10's FRED series has units "Dollars". Step 11's microsprint has students find the years income "fell" (2001, 2002, 2009, 2010, 2012, 2020) from those dollars, and Steps 12–13 compute inflation, but no step connects the two.
    - **Why it matters:** "income fell in 2009" is the sentence a business-analytics student would quote, and a fall in dollars isn't a fall in purchasing power.
    - **Proposed fix:** lab key, Step 11's Discuss (cell 104): "Is this series adjusted for inflation? Where would you check, and what would the falls look like after adjusting?" Step 10's text (cell 85): one clause on the ACS's "2024 dollars" against FRED's "Dollars".
    - **Status:** verified: the labels in cells 21 and 89, and that no step or Discuss box raises it.

16. **Setting up the keys is the week's biggest risk, and gets the least help.**
    - **Who:** A, B.
    - **What happened:** the opening cell's route is five steps for a first-time terminal user: `conda env config vars set`, quit Jupyter, close the terminal, `conda activate webdata`, start Jupyter. Every failure looks the same, `MISSING`. The `getpass()` cell is introduced as a second choice.
    - **Why it matters:** it decides whether Monday's 50 minutes are spent coding (B). A: "the real hurdle before class".
    - **Proposed fix:** lab key, cell 2, and the deck's "Step 0: a missing key": "Using the `getpass` cell every class is fine this week; set the environment variable at leisure, before your project needs it."
    - **Status:** reported, not verified: the keys were already set on the review machine (see "Environment blocks").

17. **The first given cells are too dense for a minimal student to change.**
    - **Who:** A.
    - **What happened:** cell 55 has a list comprehension with `f"{line:03d}"`, a request and a dictionary comprehension with `.split("!!")[-1]`; cell 41 `.update()`, `[1][:3]` and `time.sleep`; cell 99 `**params`. The deck splits cell 55 over two frames ("Step 6: ten decades, given" and "a label for each code"); the lab doesn't.
    - **Why it matters:** A could run them but couldn't change `housing_vars` to another group, which is what a project needs.
    - **Proposed fix:** lab key: split cell 55 in two, as the deck does. Optional: a Step 6 microsprint that reruns `census_get()` on another group.
    - **Status:** verified: cells 41, 55 and 99, and the two frames.

18. **FRED's `realtime_start` and `realtime_end` appear in the first observation and are never explained.**
    - **Who:** D, E.
    - **What happened:** cell 92 shows both as the day of the run. Step 14's last question asks which numbers would change next week, and the key's answer says "unless FRED revises a series", but no step says these two fields are how FRED dates a revision.
    - **Why it matters:** E would build a scheduled pipeline, which needs the vintage beside every number; D would check it before citing.
    - **Proposed fix:** lab key, Step 10's text (cell 85): one sentence: "`realtime_start` and `realtime_end` say when FRED's data held this value; a revised series gets new dates".
    - **Status:** verified: cells 85, 92 and 122.

### Corrections

Claims in the reviews that turned out wrong, out of date, or inexact, and what this document does with them:
- **C: "the lab only ever uses `head()`, never `tail()`."** It uses `tail()` in cells 96, 112 and 116. Dropped.
- **E: `census_get()` would fail on Subject (`S1901`), Data Profile (`DP05`) and Comparison Profile tables.** Those are in other datasets (`acs/acs5/subject`, `/profile`, `/cprofile`), not at the lab's `census_base`; the catalog it searches holds only B and C groups. The C-table case stands (item 2).
- **B: the chapter's "Social History" covers "shutdown-era gaps".** It covers staff losses and the firing of the BLS commissioner, not a shutdown or the missing month (item 7).
- **D: Step 7 "never says that the ACS margins are 90% intervals".** It does, "at 90% confidence"; D's review also says so. What's missing is the conversion and a rule (item 8).
- **B: the step times "add up to about 50, 50 and 35".** They add to 51, 51 and 38 (item 10).
- **A and E's preferred fix for item 5, the chapter's `raise_for_status()`.** It would print the key on a 400 (item 1); item 5's fix uses FRED's `error_message` instead.
- **E: the exercises start at "cell 75 of 91".** At `3f9cf2c` it is cell 75 of 112.
- **A: is "Ch. 3, *The Post-API Age*" right?** It is: the file is `ch-03-post-api.qmd` (D checked).

## Disagreements

- **Too slow, or about right.** A and C rate pace 2 and estimate 60 to 90 minutes a part; D (3) and E (4) fit the minutes. B rates it 4 because the code fits, but puts Monday at 80–100 with the keys. The minimal personas' extra time is in reading and typing, not in errors: A got every typed cell right within two tries, and B fixed each slip in under five minutes. That points at the step text and Discuss boxes, not the code, as where time could be found (item 10).
- **What to cut.** A would make Step 12's `groupby` microsprint "if time"; D Step 8's `-333333333` one, though D also calls Step 1's microsprint worth keeping; C would mark two or three typed cells a part "skip if behind". They agree only that Step 8 is the tightest.
- **Code on the slides.** B and E want the answer kept off the slide until after students try; A used the slide's `columns=` line to catch its own slip, and the live demo shows the code anyway (item 13).
- **How to handle a failed request.** A would print FRED's `error_message`; E would raise it as an error; D would print the status. Any of the three works, as long as none prints the URL (items 1 and 5).
- **Keys.** B would make `getpass()` the way for this week; A wants a take-home estimate for the environment-variable setup. Both say the setup, not the code, is where a minimal student loses Monday (item 16).
- **Difficulty.** A, B and C rate it 3, D and E 2. D, who found it easy, wants one typed cell that makes a decision, such as whether to treat the capped rents as missing; E says the Python is easy and the Census's naming, margins and codes were what was new.
- **What the week is for.** For A and B, the people and events behind the numbers (items 7 and 14); for C and D, whether a number holds up (items 8 and 15); for E, whether a pipeline would fail quietly (items 2 and 5). All five name the same habit as the lesson they'd keep: look before you parse.

## Ratings

Each on a scale of 1 to 5. For difficulty, 5 is hardest for that persona's background.

| | A | B | C | D | E | Mean |
|---|---|---|---|---|---|---|
| Clarity of motivation | 4 | 4 | 4 | 4 | 4 | 4.0 |
| Pace | 2 | 4 | 2 | 3 | 4 | 3.0 |
| Difficulty for my background | 3 | 3 | 3 | 2 | 2 | 2.6 |
| How much I learned | 4 | 4 | 4 | 4 | 4 | 4.0 |
| Confidence I could do this on my project | 3 | 3 | 3 | 4 | 4 | 3.4 |

What holds the confidence down: A, a different API's error messages and given functions too dense to change (items 5 and 17); B, finding a new API's parameters alone, and the key setup (items 9 and 16); C, C-tables, choosing a FRED series, and deciding whether two estimates differ (items 2, 8 and 9); D, a rule of thumb for differences (item 8); E, would add the error check of item 5 first.

## Small things

Deck (`slides/week-11/week-11.tex`):
- "Public data by mandate" still lists "The Library of Congress publishes Congress's legislative record at Congress.gov"; the lab and course facts dropped Congress.gov (A, C, D, E).
- The PDF has 90 pages and its counter runs to 86, so the three day dividers repeat a page number (A).
- "Microsprint: break it on purpose" asks "Which mistake still gets a 200?"; the lab's Share line (cell 43) doesn't (B).
- "Microsprint: trust, but check once" names `years = monthly["date"].dt.year`; the lab's prompt doesn't, and the chapter uses `years` for a dictionary of dates, which clashes if both are in one kernel (D).
- "Key takeaways" names the census and the Federal Reserve's data; the first frames also name the EIA (C).

Lab (`labs/week-11/lab-11-key.ipynb`):
- Cells 28 and 38: the prompts don't say "with HEADERS", though cell 30's does and the key sends them (C).
- Step 4's microsprint (cell 43) says each mistake makes `.json()` stop with `JSONDecodeError`, but `look()` never calls `.json()`, so students take it on trust. "Then try `.json()` on it" would show it (C, D, E; B checked the claim holds).
- Step 7, cell 63: the subtraction relies on Boulder being row 0 and Longmont row 1; say so, or show `incomes["NAME"]` (A, B). Cell 64: "square brackets, as with a list"; A typed `margins(0)` and got `TypeError: 'Series' object is not callable`.
- Step 8 (cell 66): one sentence on `mask()`: "returns a copy with `NaN` wherever the test is True" (B).
- Step 8 and Step 14: the chapter's "83 of 482" is for income; the lab's 170 is for rent. A parenthesis would save the worry (A, B, D).
- Step 8's Discuss (cell 78): "3,222 counties" is right; `len(rows)` shows 3,223, with the header (B).
- Step 11, cell 101: `views` works only if cell 96 converted `income` in place; say "convert `income`'s columns in place" (B).
- Step 11's third Discuss bullet, "When is it worth asking the server…?", has no answer anywhere (D).
- Step 12's Discuss (cell 117): "1,356 when this lab was written"; E got 1,366. "Over 1,300" won't go stale (E).
- Step 1, cell 11: the catalog's first three rows are in no order; sorting by `name` would make `head(3)` mean something (C). The Step 1 microsprint's "how many groups matched" needs `len()`, which the cell doesn't prompt (D).
- Setup cells 3, 48 and 81: a forgotten placeholder address goes out silently; `print(HEADERS)` would show it (B).
- `show_estimates()` (cell 22) picks estimates by a name ending in `E`, a pattern, not the catalog's metadata (E).
- The Census loop sleeps a second (cell 41); the FRED calls in Steps 11–13 don't. FRED allows about 120 a minute, so it's harmless, but a reader notices (D).
- The opening says the exercises are "due Sunday" without a date; the portfolio checkpoint is due the same Sunday, November 1 (A, C).

Chapter and companion notebook (`ch-11-government.qmd` at `3f9cf2c`):
- Exercise Step 1 asks for each key's length; one line, "a key of the wrong length was cut off when pasted", would make the length mean something (C).

## Suggested next step

**Fix first,** on #201's branch before it merges. Each is small and changes none of what the week teaches:
1. **Items 2 and 5:** in `census_get()`, convert every column but the name and place codes; in `fred_observations()`, two lines that raise FRED's `error_message`. Both cells and their deck frames.
2. **Items 3 and 4:** "`==`, two equals signs" in cells 72 and 77, and "`columns=`" in cell 32's prompt.
3. **Item 6:** mark the three capped bars and retitle Step 8's chart.
4. **Items 9, 12 and 14 (Step 14's exercise bullets, one pass):** how to find and check a FRED series, which setup cell to run first, and that a count ranks by size.
5. **Item 1 (textbook):** replace `raise_for_status()` in the chapter's code, or say that its traceback holds the key; with items 7, 12 and 14's chapter lines, in one textbook pull request.

**Needs the instructor's decision:**
- **The cause of the missing October 2025 and its citation** (item 7), before a sentence goes in the lab and the chapter.
- **The minutes** (item 10): 51, 51 and 38 against 50, 50 and 35, and what becomes "if time".
- **"Good-faith attempt" against the five-criterion rubric** (item 11), and whether Monday's frame says the exercises are graded.
- **Whether the slides keep the typed cells' answers** (item 13).
- **Whether `getpass()` becomes the recommended way for this week** (item 16).
- **A decision rule in Step 7** (item 8) and a real-dollars question in Step 11 (item 15): each adds a line and a sentence to a full part.
