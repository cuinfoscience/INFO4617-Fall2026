# Review: week 10, Introduction to APIs: Wikipedia

**What was reviewed:** week 10's lab (`labs/week-10/lab-10.ipynb`, with its key), its deck (`slides/week-10/week-10.tex`), the saved copies in `labs/week-10/data/`, and chapter 10's Recommended Exercises, as students meet them. This is the lab rebuilt in three parts for the next offering; fall 2026's week 10 was taught in October in its earlier form.
- **Course repository:** the head of pull request #205, `ea4a699e3875af8e4a2ff08eb915d5ee8eaeba9b`, which gave each workflow a small first call and rebuilt the deck around the lab. #205 is open and not merged, so every fix below names the file on that branch.
- **Textbook:** `ch-10-wikipedia.qmd` and its companion notebook `notebooks/ch-10-wikipedia.ipynb` at `3f9cf2cef801181236c9cceaf71f3b63c3ad2491`, on `main`.

**When:** 2026-11-18.

**Method:** five anonymous composite personas, each a kind of student this course has, reviewed the week independently. Each read the chapter and the slides, typed and ran its own code for every lab step it could from the students' copy, made the mistakes its background makes, attempted the Recommended Exercises on an article of its own choosing, and opened the key only after an honest try. Each review is a **steel man**: it first makes the strongest case for the materials as designed, and only then says where they fall short for that student. This document puts the five together. Every ranked finding was then checked against the repository and the textbook, and is marked **verified** (with how) or **reported, not verified**.

## Who reviewed

| | Degree and major | Python and data background | Interest | Skill |
|---|---|---|---|---|
| A | BS senior, Information Science | One intro Python course; spreadsheets | Qualitative and design: online communities, UX | Minimal |
| B | BA junior, Journalism and Communication | No Python before this course; strong with public records and Excel | Data journalism, local government | Minimal |
| C | BS senior, Business Analytics | Excel, some SQL, a little pandas | Quantitative analytics: markets, customer data, dashboards | Minimal to moderate |
| D | MS first year, Data Science (BA in Statistics) | Fluent in R, moderate pandas; regression and sampling | Quantitative: measurement and validity | Moderate |
| E | MS first year, Information Science (BS in Computer Science) | Moderate Python, git; little data analysis | Design and tools: automation, APIs, building things | Moderate |

## What each completed

The lab has Steps 0–17 in three parts: Part 1 (Monday) is Steps 0–5, Part 2 (Wednesday) Steps 6–11, Part 3 (Friday) Steps 12–17, then the 15-minute portfolio cell. No persona wrote Step 17's answers into the notebook; all five answered them in notes. Every persona read the last cell and did nothing there, since it is a placeholder (item 8). "From the saved copy" means the step's commented checkpoint cell, used after Wikipedia refused the request (see "Environment blocks").

| | Lab steps finished | Blocked, so read from the saved copy or the key | Recommended Exercises (article) | Needed the key for |
|---|---|---|---|---|
| A | 0–14; 15's links and three backlinks by hand; 16, after installing mwclient | 15's backlinks loop (eight 429s in a row) | Steps 1–7 (*Reddit*) | Only to see why Step 13 printed `False` |
| B | 0–4, 6–14, 16 | 5 (`get_revisions()`); both of 15's loops | Steps 1–7 (*Marshall Fire*); Step 6 run in four pieces | Nothing; compared afterwards |
| C | 0–16, waiting out 429s with a retry of its own outside the lab's cells | none | Steps 1–6 (*Silicon Valley Bank*); Step 7 worked out, not written | Nothing |
| D | 0–14, 15's backlinks loop, 16 | 15's links (four tries) | Steps 1–7 (*Marshall Fire*); Step 6 with a script of its own that waits on `retry-after` | Outputs of cells it couldn't get live, after trying |
| E | 0–4, 6–14, 15's backlinks loop | 5; 15's links; 16 (`mwclient.Site()` refused twice) | Steps 1–7 (*Marshall Fire*); Step 6 after a `KeyError` (item 11) | The outputs of the three blocked cells |

**Estimated time for a real student of that background, on a network without 429s, in minutes** (the lab's own step and microsprint minutes in the last rows):

| | Part 1 | Part 2 | Part 3 | Exercises |
|---|---|---|---|---|
| A | 70–80 | 65–75 | 55–60 | 120–150 |
| B | 70–80 | about 55 | about 65 | 150–180, 45 of them working out what to copy (item 9) |
| C | 60–75 | about 50 | about 60 | 120–150 |
| D | about 30 | about 25 | about 30 | about 90 |
| E | about 75 | about 60 | about 65 | about 150 |
| **The lab** | **59** (52 in steps, 7 in microsprints) | **61** (52 + 9) | **50** (43 + 7) | none given |
| **The day** | **50** | **50** | **35**, then the 15-minute portfolio block | due the Sunday after (item 7) |

## Environment blocks

These come from the review machine, not from the materials. They are kept apart so that none is read as a flaw in the week.

- **Wikipedia answered with many 429s (all five).** The five personas shared one network address, and Wikimedia's rate limit counts requests by address. `retry-after` ran from 1 to 55 seconds; B counted about 58 refusals in its session. The lab's single requests went through after a wait. Its multi-request loops often didn't, which is where the blocks in the table above come from: Step 5's `get_revisions()`, Step 15's `page_list()` and backlinks loop, and Step 16's `mwclient.Site()`. C waited out the 429s with a retry of its own around `requests.get`, outside the lab's cells, and E wrapped it to retry once, so their runs differ from a student's in that respect. The load is environment. How a given loop *responds* to a 429 is a design question, and is ranked as item 5.
- **No cell was skipped for `robots.txt`.** The key tags no cell `not-run-live`, so nothing was read from saved output for that reason. The personas sent the lab's Action API requests to `en.wikipedia.org/w/api.php`, whose `robots.txt` disallows `/w/` for every user agent; C and D did so on the reading that Wikimedia's API policy, not `robots.txt`, governs API clients. That reading is the instructor's open decision (item 12). The pageview requests go to `wikimedia.org`, which serves no `robots.txt`.
- **mwclient.** `webdata` doesn't include it. A and C installed it with pip (0.11.0), C because the machine had no conda; the lab names conda-forge's 0.10.1. Step 16 worked the same on 0.11.0.
- **A notebook kernel died** once on its own during E's run; E switched to a plain Python runner.
- **The counts moved.** Wikimedia's pageview counts for closed months differed between the saved copies (2026-11-10), the key's second run (2026-11-17) and the personas' runs. That drift is not a block, but it explains why the personas' numbers differ from the key's (item 3).

## The strongest case for the week as designed

**Every workflow starts with a request small enough to check by eye.** All five said so. Step 1 prints the status and the first 200 characters before anything is read, and Step 2 goes down the JSON one level a cell, printing the keys first; by Step 11 B "had stopped being afraid of `data["query"]["pages"]`". #205's small first calls were singled out: three edits to compare with View history in a second tab (C, D), three days of pageviews before 2,099 (E), September by month against September by day (C: "13,933 each in my run"). E: "each given function is a thing I had already typed once as separate lines … a compression of something I have done."

**Step 4's two pages by hand make Step 5's loop readable.** A could "point at the `params.update(data["continue"])` line and say 'that's my second move'"; D knew what a `"continue"` token is "because I had added one to a dictionary myself"; E called Step 4 "the best-designed piece for someone who knows HTTP". The one line no minimal student could invent, `list(pages.values())[0]`, is given with the reason the page ID can't be known in advance, which B called "a good division of labor".

**Failure is shown on purpose, in a useful order.** Step 3 gives a 403 without a User-Agent, a 429 with `retry-after`, and a 200 with `Unrecognized parameter: title.` inside it. B called the last "the most useful thing I learned all week: an API can say 'OK' and still not do what you asked"; E called the three "the failure taxonomy I would otherwise have to learn by being bitten". Step 11 predicts `TypeError: Cannot join tz-naive with tz-aware DatetimeIndex` before students hit it, so the error reads as expected (B, C, D). And the Discuss question on `raise_for_status()` makes students say which of the day's failures it would catch (E).

**The checkpoints and the privacy handling are the week's quiet strengths.** Every part starts from saved copies, so "a refusing server costs me one cell, not the lesson" (E); B "would have given up in the middle of Step 5 without them". Step 5's given cell numbers the editors and drops names, addresses and summaries before saving, and Step 8 asks whether a ranking by name should be published; A, B, C and D each named this as how to publish a derived table. D checked the saved copies: all load from the raw address, carry no usernames, and `daily-views.csv` sums to the chapter's 1,367,292.

**Part 3's "a pageview is not a person" is the best data-literacy moment of the week** (B), and the numbers hold up. The agent split, the all-agents check and the Selenium question turn a footnote into something students run (C, D). D and E reproduced the Discuss boxes' figures: December 2006 with 61 edits, 16,767 views on 2023-09-17, 51% people in August 2026, 40 categories, 38 languages, 91 edits in 2023 both ways. "A course that quotes numbers and has them reproduce is a course I trust" (D).

## Where it falls short, ranked

The privacy problem and the wrong-result problems come first. After them, items are ranked by how many personas hit each, how badly, and whether it stopped A or B. Cell numbers are positions in `labs/week-10/lab-10-key.ipynb` at `ea4a699e`, counted from 0; the students' copy has the same cells.

1. **Exercise Step 4 asks students to print the top ten editors by name, which the lab has just taught them not to publish.**
   - **Who:** C, D; A for the bots among them.
   - **What happened:** the chapter's Exercise Step 4 says "Use `value_counts()` on the user column … and print the top ten." The lab's Step 5 numbers editors instead of naming them, and Step 8's Discuss asks whether publishing a ranking by name is fine. Step 17's hand-off says only "Your table will have the `user` column". C and D printed numbered ranks; nothing tells a student which to do. Several of A's top ten were bot accounts, which neither the lab nor the exercise mentions, so "a dedicated few" and "bots keep it tidy" read the same in the table.
   - **Why it matters:** the exercise is submitted (item 7), so a student who follows its words submits a ranking of private individuals' usernames, which the course's own privacy rule says to count rather than print.
   - **Proposed fix:** chapter, Exercise Step 4: "print the counts, numbered as the lab's Step 5 did; look at the names yourself if you need to, but don't paste them into the notebook". Add: "some of the top ten may be bots; their usernames usually end in 'bot'". Lab key, cell 134 (Step 17's Step 4 bullet): the same sentence. If the instructor decides public usernames are fine here, say so in both places instead.
   - **Status:** verified: the exercise's wording at `3f9cf2c`; cells 39, 63 and 134.

2. **The saved `backlinks.csv` has lost which pages are redirects, so the checkpoint path prints "3314 are redirects".**
   - **Who:** B, D.
   - **What happened:** B loaded Step 15's checkpoint (cell 126) after the 429s. Each record from `to_dict("records")` has a `redirect` key, so the given count in cell 125, `sum("redirect" in b for b in backlinks)`, returns 3,314, every row, where the live run gives 70. It is worse than the personas saw: the API marks a redirect with `"redirect": ""`, and pandas writes that empty string and a missing value the same way. The file's `redirect` column is empty in all 3,314 rows, so no code can recover the 70.
   - **Why it matters:** Step 15's Discuss and Exercise Step 6 both ask about redirects, and the checkpoint is the path a student takes when Wikipedia refuses them. `labs/week-10/data/README.md` says "`redirect` is set for those", which the file no longer shows.
   - **Proposed fix:** lab key, cell 125: save a True/False column, e.g. `pd.DataFrame(backlinks).assign(redirect=["redirect" in b for b in backlinks])`, and remake `backlinks.csv` on the laptop run #205 already asks for (#197). Cell 126: load it so that `redirect` is a column of True/False, and count with `sum(b["redirect"] for b in backlinks)`, or print the count in the checkpoint cell itself.
   - **Status:** verified: `backlinks.csv` at `ea4a699e` has 3,314 rows and no non-empty `redirect` value; loading it as cell 126 does and running cell 125's count gives 3,314.

3. **Step 13's check compares four live counts with exact equality, and printed `False` for four of the five.**
   - **Who:** A, B, C, D (D got `False` once and `True` once with the same code). E finished Step 13 and didn't report the check's result.
   - **What happened:** cell 105 prints `"Sum checks out:", (by_agent.sum(axis=1) == all_by_month).all()`. The four series come from four requests sent seconds or minutes apart. In the personas' runs, September 2026's `automated` count was 2,248 in one run and 2,263 ten minutes later (C, D), and September's `user` count was 13,933 when asked for September alone and 13,948 when asked for January 2024 to September 2026 on the same day (A, D). The key's saved run printed `True`, from requests sent on one day. Nothing in the students' copy says a closed month's count can change: the key's note explains it, but students don't see the key's note, and the one Discuss question about it is about 2025. The same drift moves Step 9's total (1,366,735 live against 1,367,292 in the chapter and the key) with no line saying so (A, B, C, D, E).
   - **Is the drift real?** Yes. Wikimedia's page-view reference and concepts pages say nothing about counts being final. Wikimedia has rewritten past months: its task T405667 backfilled the datasets for March 21 to August 31, 2025 after a bot-detection fix, which the chapter's "Social History" describes. And #205's own key records September 2026 changing from 14,000 to 13,960 between 2026-11-10 and 2026-11-17. So the drift is the data; what can be fixed is the check.
   - **Why it matters:** the cell reads as pass/fail. B "took `False` to mean I had typed something wrong"; C is "the student who runs a check and then stops believing the numbers when it fails"; D: "exact `==` on counts that a data provider is still revising is an unreliable check". A student who loaded `by_agent` from the checkpoint (cell 101) and sent `all_views` live is comparing 2026-11-10's counts with today's.
   - **Proposed fix:** lab key, cell 105: print the largest gap, `(by_agent.sum(axis=1) - all_by_month).abs().max()`, beside or instead of `True`/`False`. Step 13's microsprint, its Share line: "a gap of a few views is Wikimedia revising its counts between your requests, not your code". Step 9's text: "your total will differ a little from the key's: Wikimedia revises past counts". The deck's "Step 13: three agents" frames: the same sentence, if one quotes the check.
   - **Status:** verified: cell 105's code, the key's note and cells 97–100 (13,960 against 14,000); the provider's documentation and T405667 as above. The personas' live counts are their own.

4. **Pageviews follow a title, and a moved article splits its series; the exercise's "find the spike" can land on the wrong event.**
   - **Who:** B, D, E, each on the same article.
   - **What happened:** three personas chose *Marshall Fire*, a fire of December 30, 2021. `idxmax()` gave 2025-12-17 (5,051 views); 2021-12-31 had 707. The revision history starts 2021-12-31, and its busiest edit days are the fire's first two weeks. D found in the edit summaries that the page was moved to that title from an earlier one, so the first days' readers are counted under the old title. E suspected the same; B, finding no edits around the peak, couldn't say what the peak was. B and E would have written "the biggest day is an anniversary in 2025" into Exercise Step 7.
   - **Why it matters:** Exercise Step 1 asks for "an article … with at least one newsworthy moment since 2021", which makes recently created and renamed articles likely. Exercise Step 2's whole point is to connect the peak to an event.
   - **Proposed fix:** chapter, "Common Issues to Debug": "Pageviews belong to a title; edits belong to a page. If an article was moved, its earlier views are under the old title. Compare its first edit's date with your window before you trust a peak." Exercise Step 2: the same check, and "if the biggest day isn't the news you chose the article for, say so; that is a finding". Lab key, Step 10's Discuss (cell 82): one question on it.
   - **Status:** verified that neither "Common Issues to Debug" nor the exercise mentions moves or renames. The move itself is reported, not verified: checking it needs a request to the Action API, which this review didn't send (item 12).

5. **When a given loop gets a 429, the error doesn't say 429, the lab's recovery cell prints the wrong response, and the loop starts over.**
   - **Who:** A, B, C, D, E.
   - **What happened:**
     - A 429 from Wikimedia is an HTML page, not JSON. The lab's `get_revisions()` (cell 37), `get_pageviews()` (96) and `query_all()` (120) leave out the chapter's `raise_for_status()`, so the next line, `response.json()`, stops with `JSONDecodeError: Expecting value: line 1 column 1 (char 0)` (A, B, D, E). C reports `KeyError: 'query'` from the same cause. The chapter's versions stop with `HTTPError: 429 Client Error`, which D met in the exercises and found clearer.
     - Step 3's given cell (22) says "when a cell stops with JSONDecodeError or KeyError, print its response so (here, Step 1's)", and prints `info_response`: Step 1's answer, a 200. Inside a function the failed `response` is local, so it can't be printed afterwards. A ran cell 22 and got Step 1's 200, which "told me nothing"; B: "a student reading cell 22 literally sees '200, None' and concludes the site is fine and my code is broken". E and D had to edit or rerun a request by hand to see the 429.
     - The next cells fail too (`NameError: name 'first_page' is not defined`, `name 'revisions'`, `name 'links'`), which looks like a typo (A, D, E). Step 4 has no checkpoint: if page one or two is refused, cell 34 stops (D).
     - A rerun of a loop starts again from page one and spends more of the shared limit; D's `page_list(ARTICLE, "links", ...)` never finished in four tries. "Wait the `retry-after` seconds, and run the cell again" is on the deck's "Error flavors" block only, not in the notebook (A, D).
   - **Why it matters:** the lab itself says a room on one network can reach the limit together (Step 0's Discuss), so this is the likeliest failure in class, and A and B can read only a traceback's last line. B: "my background gives me no other way to diagnose it."
   - **Proposed fix**, within the rule that a lab has no error handling:
     - Lab key, cells 37, 96 and 120: one given line after `requests.get`, `print(response.status_code, end=" ")`, so a refusal shows as `200 200 429` above the traceback (B).
     - Cell 22: show any response, not Step 1's: "change `info_response` to the response that failed; for a loop, send one of its requests by hand" (A, D).
     - Step 5's and Step 15's text, and the checkpoint cells 40 and 126: "if the loop stops with `JSONDecodeError` or `KeyError: 'query'`, you were probably refused: wait, then use the saved copy below rather than running it again". Put the sentence before the loop, not after (C, D).
     - Step 4: a checkpoint for page one and page two, or say that cell 34 needs both.
     - The deck's "Step 3: when a cell stops" frame follows cell 22.
     - D and E would have the given loops wait on `retry-after`, or stop with the status in the message. Both add error handling, which `labs/AUTHORING.md` leaves out on purpose; that is the instructor's call (see "Disagreements").
   - **Status:** verified: cells 22, 31–34, 37, 96, 120; the deck frames "This week, every class is live coding" and "Step 3: when a cell stops"; #205's own description records that a 429 from the pageviews API is an HTML page. The error texts are the personas' runs.

6. **None of the three parts fits its day by the lab's own minutes.**
   - **Who:** A and E counted it; A, B, C and E estimate each part at 50 to 80 minutes. D alone would finish early.
   - **What happened:** the headings and microsprints add to 59, 61 and 50 minutes, against about 50, 50 and 35 (`docs/course-facts.md`, "The week"). Part 3 is 15 minutes over, before any Discuss box, and its last steps are mwclient (16) and "What did we learn?" (17). #205 flagged Part 3 itself, counting 43 without the microsprints.
   - **Why it matters:** what gets cut in practice is the end of the day: Step 16 and Step 17. A: "I would be doing [the exercises] without having seen `query_all()` run." A 429 adds 5 to 10 minutes a time (B).
   - **Proposed fix:** the minutes are the instructor's decision. The candidates:
     - #205: cut Step 13's microsprint (4 minutes) or Step 14's redirects microsprint (3). Cutting Step 13's also removes item 3's check.
     - A: make Step 16 read, not run, or drop the redirects microsprint.
     - E: mark Steps 15–16 "if time". But the exercises need `page_list()` and `query_all()`, which Step 15 introduces.
     - A: say in each part's opening which steps are optional "if you are behind".
   - **Status:** verified: the headings in the key sum to 52 + 7, 52 + 9 and 43 + 7. The persona estimates are their own.

7. **What is turned in, and when, is said four ways.**
   - **Who:** A, B, C, D, E.
   - **What happened:** the lab's first cell says "Nothing here is turned in." Step 17 (cell 134) says "Recommended Exercises ahead (in the chapter's companion notebook, due Sunday)". The deck's "This week, every class is live coding" says "Nothing to submit: the lab is practice"; its "This week at a glance" says "No lab notebook or GitHub submissions this week" and "Due Sunday, Oct 25: Final Project proposal". The chapter says the exercises are "the chapter's take-home assignment … submit the completed notebook".
   - **Why it matters:** B "would decide there is nothing due this week" from the deck, and think the exercises are due from the lab; D couldn't tell whether they are graded. Each statement is defensible alone (see "Corrections"), but students read them together.
   - **Proposed fix:** lab key, cell 0: "Nothing in this notebook is turned in; the chapter's Recommended Exercises are, from its companion notebook". Cell 134: the real due day and time, or "practice" if this week has none. The at-a-glance frame is the instructor's and was kept in fall 2026's form on purpose; for the next offering, #205's description already proposes three bands in its place.
   - **Status:** verified: cells 0 and 134; the two deck frames; the chapter at `3f9cf2c`; `docs/course-facts.md` ("The week", and "Weeks 10–14 of Textbook Revisions").

8. **The students' copy ends with a placeholder: "[the instructor names it here, with its due date]".**
   - **Who:** A, B, C, D, E.
   - **What happened:** cell 136, "Friday: your portfolio checkpoint", reads "This week's checkpoint is **[the instructor names it here, with its due date]**", followed by "In fall 2026, week 10 had no checkpoint". B "can't tell which sentence applies to me".
   - **Why it matters:** it is the last thing students read, and says nothing yet.
   - **Proposed fix:** the instructor's text: the next offering's week 10 checkpoint and its date, or "none this week; use the time on your proposal". Lab key, cell 136; the students' copy follows from `make_student_copy.py`. #205's description lists it among the dates to change.
   - **Status:** verified in both the key and the students' copy at `ea4a699e`.

9. **The exercises need four functions the companion notebook doesn't give in a usable form, and the lab's versions differ from the chapter's.**
   - **Who:** A, B, C, D.
   - **What happened:**
     - The exercises say to use "the chapter's `get_pageviews()`" and `get_revisions()`. In the companion notebook those are defined in the chapter's cells, and the cell that defines `get_revisions()` also calls it for the university (six requests). D had to run those requests or edit them out.
     - The lab's versions use a global `API` and `time.sleep`; the notebook defines neither. B got `NameError: name 'API' is not defined`, and D `NameError: name 'time' is not defined`.
     - The lab's versions leave out `raise_for_status()` and pause a second; the chapter's keep it and don't pause. C didn't know which to copy, or which a grader expects. A noted that the chapter's version has no pause, so on a shared network it is the likelier to stop on a 429.
     - B spent about 45 minutes "assembling pieces"; C 30 to 40.
   - **Why it matters:** the exercises are done at home, with no one to ask, and they are what is graded.
   - **Proposed fix:** lab key, cell 134: end the hand-off with "copy the Step 12 setup cell and the four functions (`get_pageviews`, `get_revisions`, `query_all`, `page_list`) into the top of the companion notebook", or name the chapter's as the ones to use. Chapter and companion notebook: one given cell above Exercise Step 1 with the imports, `HEADERS` and the four functions, and no request.
   - **Status:** verified: the companion notebook at `3f9cf2c` (cell 12 defines and calls `get_revisions()`; no `import time`; the functions use a local `url`); cells 37, 96, 120 and 121 in the key.

10. **Step 11's correlation is the lab's one inferential number, and one month decides it.**
    - **Who:** C, D.
    - **What happened:** cell 87 gives 0.21 for 69 months, and the Discuss asks "what can't a correlation say?" with nothing in the lab to find out. On the saved copies, Spearman's is 0.19, and dropping September 2023, the football month (97,904 views), raises Pearson's to 0.41. Monthly edits average 6, median 4. C's own article gave 0.999, almost all of it one month.
    - **Why it matters:** "one month decides whether the answer is 'weak' or 'moderate'" (D). For a validity-minded student it is the best teachable moment of the week, and the lab walks past it.
    - **Proposed fix:** lab key, after cell 87: a given cell of two lines, `monthly_views.corr(edits_since_2021, method="spearman")` and the same Pearson without `"2023-09-30"`, with the three numbers in the Discuss (D). Or one Discuss line asking what the correlation would be without the two biggest months (C). Chapter, Exercise Step 7: "one extreme month can drive a correlation".
    - **Status:** verified on `daily-views.csv` and `revisions.csv` at `ea4a699e`: 0.209 Pearson, 0.190 Spearman, 0.410 without September 2023.

11. **Exercise Step 6 asks for five language editions, and the lab never shows what one looks like.**
    - **Who:** C, E.
    - **What happened:** both printed `x["title"]` for all four lists, as Steps 14 and 15 taught, and got `KeyError: 'title'` on the languages: a `langlinks` entry holds `lang` and `"*"`. Step 14's given cell (113) prints only `len(cat_lang_page["langlinks"])`. The chapter's "Interlanguage Links" shows the keys once.
    - **Why it matters:** a predictable crash in the step that brings the lists together. Both recovered only by printing one item, as Step 2 taught.
    - **Proposed fix:** lab key, cell 113: also print `cat_lang_page["langlinks"][0]`. Or cell 134's Step 6 bullet: "a `langlinks` entry has `lang` and `*`, not `title`: print one first".
    - **Status:** verified: cell 113, and the chapter's `langs[["lang", "*"]]`.

12. **Step 0's Discuss asks why `robots.txt` doesn't contradict the API, and nothing answers it.**
    - **Who:** C, D.
    - **What happened:** Step 0's Discuss (cell 4) asks: "Wikipedia's `robots.txt` (week 2) disallows `/w/`, yet the API lives at `/w/api.php`. Why isn't that a contradiction?" The chapter doesn't mention `robots.txt`, and the deck mentions it only in the proposal's ethics bullets. Wikipedia's `robots.txt` (read 2026-11-18) has, for `User-agent: *`, `Disallow: /w/` and `Disallow: /api/`, with an `Allow` only for `/w/api.php?action=mobileview&` and `/api/rest_v1/?doc`. The lab's `action=query` requests and mwclient are under `/w/`. The pageview requests go to `wikimedia.org`, which has no `robots.txt`. The proposal checklist on Friday asks students to "read `robots.txt`".
    - **Why it matters:** students are asked a question the course has not yet decided. #212 (week 3) treated Wikipedia's `Disallow: /w/` as binding for requests from the course's cloud machine, and left those cells for a laptop run. #205's key and this review's personas sent the same kind of request, on the reading that the API's own policy (the User-Agent policy and the rate limits) governs API clients. Which reading the course takes is the instructor's open decision, and the Discuss answer depends on it.
    - **Proposed fix:** after that decision, one or two sentences in the chapter's "The Anatomy of an API Call", and the answer in the key under cell 4. On the second reading: "`robots.txt` tells crawlers which pages to fetch; the API documents its own rules, which are the User-Agent policy and the rate limits". On the first, the Discuss question should change.
    - **Status:** verified: cell 4; the chapter has no "robots" at `3f9cf2c`; Wikipedia's `robots.txt` as quoted; `www.wikimedia.org/robots.txt` answers 404; #212's description.

13. **"Restart the kernel" after installing mwclient is on the slide and not in the notebook.**
    - **Who:** A, C, E.
    - **What happened:** cell 0 and Step 16 give `conda install -n webdata -c conda-forge mwclient`, to run in a terminal. The deck's Friday "No mwclient?" block adds "Then restart the kernel"; the notebook doesn't. A student who installs with the notebook open gets `ModuleNotFoundError` at cell 129. C, who uses only notebooks, would want the chapter's `%conda install -y -c conda-forge mwclient`, which cell 0 mentions only in parentheses.
    - **Why it matters:** Step 16 comes at the end of a day already over time (item 6).
    - **Proposed fix:** lab key, cell 0 and Step 16's text (cell 128): "then restart the kernel". Step 16: the notebook form as the fallback.
    - **Status:** verified: cells 0, 128 and 129; the deck frame "Today: Part 3, what the counts count".

14. **The typed cells are transcriptions, so the exercises are the first place students choose a method.**
    - **Who:** B, C, E; D in passing.
    - **What happened:** a typical prompt holds its answer (`# top_ten: edit_counts.head(10); print their share, top_ten.sum() / len(revisions)`), and the deck shows the same lines. B, C and E matched the key "line for line". The exercises then ask students to pick an article, build a table, plot, find a peak, combine two series and print four lists, with no prompt and no slide.
    - **Why it matters:** "The lab felt easy, and the Recommended Exercises took much longer, because the exercises have no slide to copy" (C). B's mistakes in the exercises "were the ones the lab never let me make". A, on the other hand, valued that "I never had to invent anything".
    - **Proposed fix:** one typed cell or microsprint a part whose prompt names the goal but not the call, e.g. Step 8 "print how many different editors there are" (B), Step 10 "plot the 30 days around the peak" (E). Deck: for two or three such cells, the prompt on one frame and the code on the next (C).
    - **Status:** verified by reading the prompts in cells 50, 59, 66 and 86 and their deck frames. Whether students would manage it is the personas' judgment.

15. **Nothing in the lab lets a student read what an editor wrote, or says what a reporter would ask.**
    - **Who:** A, B.
    - **What happened:** the people behind the article appear as numbers and byte counts; Step 5's given cell drops the edit summaries, and Step 7's Discuss asks "what would you read to tell them apart?" without letting students read anything. A's first look at an edit summary was in the exercises, "the most interesting thing in the week for a community/UX student". B followed every step "and not know what I'd ask Wikipedia about my local government".
    - **Why it matters:** both rate motivation lower on this alone (B 3).
    - **Proposed fix:** the instructor's call, since the saved copy drops summaries on purpose (`data/README.md`: they "often name other editors or IP addresses"). A: add `comment` to Step 4's three-edit `rvprop`, so three summaries are printed live and none is saved. B: one line at the top of Part 2, e.g. "A reporter checking a city's page would ask who edited it the week of a vote, and how many people read it", and a Step 17 question asking for one such question for the student's project.
    - **Status:** reported; a judgment about scope. The data README's reason is verified.

### Corrections

Claims in the reviews that turned out wrong or inexact, and what this document does with them:
- **D: both endpoints the lab uses are under a disallowed `robots.txt` prefix.** Only the Action API is. The pageview requests go to `wikimedia.org`, whose `robots.txt` redirects to `www.wikimedia.org` and answers 404; C had this right. Item 12 says so.
- **B and D: the backlinks checkpoint gives every record a `NaN` redirect.** True, but the saved file is the cause, not the loading: its `redirect` column is empty in every row, so the 70 redirects are gone from it (item 2).
- **A, B, C, D: "Nothing here is turned in" and "due Sunday" contradict each other.** By the course's design they don't: from week 11, and in the next offering for which this lab was rebuilt, the lab is practice and the chapter's Recommended Exercises are graded, due the Sunday after (`docs/course-facts.md`). The at-a-glance frame is the instructor's, kept in fall 2026's form on purpose, as course-facts records. What remains is that the four statements read as a contradiction side by side (item 7).
- **A: the deck's "Download the new `lab-10.ipynb`; start at Step 6" contradicts the lab's one notebook.** It doesn't: a fresh copy carries any fixes, and the lab's own "start at that day's setup step" says the same. Dropped.
- **B: the deck's "Step 2: the same answer in a browser" has no lab cell.** It is the screenshot the lab's Step 2 links to in the chapter, and its narration says "in the notebook, we go down one level a cell". Dropped.
- **A, C, D: Step 11's correlation is 0.2096.** On the saved copies, and in the key, it is 0.2093; both round to the Discuss box's 0.21. The difference is item 3's drift.
- **A: the companion notebook's `get_revisions()` "would stop" on a 429.** It would, with `HTTPError: 429`, which is the clearer of the two failures (item 5). A ran it behind a retry of its own and didn't see it. Kept as a note in item 9.

## Disagreements

- **Too slow, or too fast.** D would finish each part in 25 to 30 minutes ("far too slow for me when it works") and rates pace 3; A rates it 2, and with B, C and E puts each part at 50 to 80 minutes against the day's 50, 50 and 35. C alone rates pace 4 ("each part fits its allotted time on a good day"). The lab's own minutes side with A, B and E (item 6). The spread suggests the cut should be in what everyone does, Part 3, not in the pace of the typing.
- **How to survive a 429.** D would have the given loops sleep for `retry-after` and send the request again; E would have them raise an error carrying the status; A would `break` with a message and keep the pages already fetched; B would add only one printed status per request; C would point to the checkpoint before the loop. B's and C's stay within the course's rule that a lab has no error handling, so item 5 proposes those; D's and E's are for the instructor to weigh against the rule. On one thing all five agree: the cell 22 they were given prints the wrong response.
- **Typed cells: transcription or composition.** B, C and E want one cell a part whose prompt names a goal but not the call (item 14); A valued never having to invent anything; D finds the typing trivial but expects less fluent students to copy from the slide. A no-recipe microsprint, alongside the existing ones, would serve both.
- **Showing what people wrote.** A wants edit summaries on screen; the course's saved copy drops them because they name other editors (item 15). Printing three live and saving none is the narrowest middle.
- **Correlation.** D wants a given cell that computes Spearman's and the Pearson without one month; C a Discuss line. Either makes the point; D's makes students see the numbers.
- **Difficulty.** A, B and C rate it 3, D and E 2. B rates the exercises 4, and C, D and E each said the exercises, not the lab, were where they first decided anything.
- **Motivation.** A, C, D and E rate it 4, B 3. A and B want the people behind the article; C wants a sentence on why an analyst would want an API in a pipeline; E a sentence on why this API over the alternatives.

## Ratings

Each on a scale of 1 to 5. For difficulty, 5 is hardest for that persona's background. B rated the exercises' difficulty 4 separately.

| | A | B | C | D | E | Mean |
|---|---|---|---|---|---|---|
| Clarity of motivation | 4 | 3 | 4 | 4 | 4 | 3.8 |
| Pace | 2 | 3 | 4 | 3 | 3 | 3.0 |
| Difficulty for my background | 3 | 3 | 3 | 2 | 2 | 2.6 |
| How much I learned | 4 | 4 | 4 | 4 | 4 | 4.0 |
| Confidence I could do this on my project | 3 | 3 | 3 | 4 | 4 | 3.4 |

What holds the confidence down: A doesn't know what to do when a request fails partway (item 5); B could get one record from an API but couldn't debug a 429 inside a function; C is unsure about rate limits in a longer loop and about a correlation with one extreme month (item 10). D and E rate it 4: D would write a loop that honours `retry-after` and check for moved titles; E is less sure about APIs that page by cursors or headers, since every pager here is `"continue"`.

## Small things

Lab (`labs/week-10/lab-10-key.ipynb`):
- Cell 0 calls mwclient "a client library that does the paging for us"; Step 16 says it "stops on a 429". Both are true; side by side they confuse (A).
- Step 1: no prompt to note the page ID, which Step 16 asks students to compare with (E).
- Step 1 or 2: one sentence that "keys and text values are in quotes; names like `ARTICLE` are not" would help with prompts such as cell 17's `ARTICLE + "|Talk:" + ARTICLE + "|" + a misspelled title` (A).
- Step 2's microsprint: the given cell's `.get("length", "missing")` isn't explained, and the Discuss asks what `["length"]` would have done (A).
- Step 2's Discuss on the talk page's length would be easier with a link to the talk page's archives (C).
- Step 4's Discuss says the three edits' `"continue"` "held a time"; `rvcontinue` is a time and a revision ID joined by `|`. "The part before the `|`" would do (C, E).
- Step 5's text says `get_revisions()` "leaves out the chapter's `raise_for_status()`" without saying why (A).
- Step 7: the `+00:00` in the printed index appears four steps before Step 11 explains it; one sentence that the `Z` in the timestamps makes them time-zone aware would let students predict Step 11's error (A, B, D, E).
- Step 8's microsprint: `temp` is 0.5% of the edits, the first in December 2025; "temporary accounts began in late 2025" would explain why the share is almost all `anon` (C).
- Step 11's `TypeError` text is pandas 3.1's; older versions word it differently (E).
- Step 15: "Its `sum()` adds one for each page that is a redirect" could say that it counts the `True`s (A).
- Step 17's answers cell gives no length; Exercise Step 7 asks for four to six sentences, and Step 17 could say it is the practice for that (C).
- Numbers that differ from the chapter's, because the article changed: 652 links (650), 3,314 backlinks (3,294), 95,029 bytes (95,273). The key's note gives these; the students' copy doesn't (A, B, D).

Data (`labs/week-10/data/README.md`): it says `editor` 0 is "an edit whose username Wikipedia has hidden"; `revisions.csv` has no such row (C; verified).

Deck (`slides/week-10/week-10.tex`):
- "This week at a glance" describes fall 2026's week (Monday concepts, Wednesday lab, Friday "continue the lab") against the following frames' three parts (A, B, C, D, E). Known and left on purpose; #205 proposes three bands.
- Friday's "Today" and the Final Project frames carry fall 2026's dates ("Proposal due Sunday, October 25", "Week 16, Nov. 30–Dec. 4") (A, D). #205 lists them among the dates to change.

Chapter and companion notebook (`ch-10-wikipedia.qmd` at `3f9cf2c`):
- The companion notebook's Exercise Steps 1 and 2 show raw cross-references, `(@sec-ethics)` and `(@sec-introduction showed you this)` (B; verified).
- Exercise Step 2 says to check edits "that mention it"; for A's article none near the peak did. "No edit mentions it" is a finding, and the step could say so (A).
- Exercise Step 5 needs Step 11's `tz_localize(None)`; Step 17 says so, the notebook doesn't (B).

## Suggested next step

**Fix first,** on #205's branch before it merges. Each is small and changes none of what the week teaches:
1. **Item 2:** save `redirect` as True/False in cell 125, count it that way after cell 126, and remake `backlinks.csv` on the laptop run #205 already asks for.
2. **Item 3:** cell 105 prints the largest gap; one sentence in Step 13's microsprint and in Step 9 that Wikimedia revises past counts.
3. **Item 5:** one `print(response.status_code, end=" ")` in each given loop; cell 22 made general; the checkpoint sentence before Steps 5's and 15's loops; Step 4's dependency named.
4. **Items 11 and 13 and cell 134:** print one `langlinks` entry in cell 113; "restart the kernel" in cells 0 and 128; Step 17's hand-off says to print counts, not names, and which four functions to copy (items 1 and 9).
5. **Items 1, 4 and 9 (the chapter's exercises, one pass):** counts, not names, and a word on bots in Step 4; the moved-title check in Step 2 and "Common Issues"; a setup cell with the four functions and no request. These are textbook changes, for the next textbook pull request.

**Needs the instructor's decision:**
- **The minutes** (item 6): 59, 61 and 50 against 50, 50 and 35, and what in Part 3 becomes "if time".
- **How strictly to read Wikipedia's `robots.txt`** (item 12), raised on #212: it decides Step 0's Discuss answer, and whether the Action API cells run from the course's machine or a laptop.
- **What is due, and the last cell's text** (items 7 and 8): the next offering's week 10 checkpoint, or none; whether the exercises are graded that week; and whether the chapter's "submit the completed notebook" stays.
- **Whether a given loop may wait on `retry-after`** (item 5, D and E), against the rule that a lab has no error handling.
- **Edit summaries on screen** (item 15), and a no-recipe cell a part (item 14).
