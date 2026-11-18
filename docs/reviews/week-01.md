# Review: week 01, Introduction to Web Data Science

**What was reviewed:** week 1's lab (`labs/week-01/lab-01.ipynb`, with its key), its checkpoint (`labs/week-01/data/jan2026.json`), its deck (`slides/week-01/week-01.tex`), the setup handout (`handouts/week-01/setup.md`) and chapter 1's Recommended Exercises, as students meet them.
- **Course repository, all five personas:** the head of pull request #217, `a91f57fae4dc8ff9e06eca288184590514e5491f`, which rebuilt week 1's lab and added five Lab 01 frames to the deck in the incremental style. It is open and not merged. The lab is for the course's next offering.
- **Textbook:** `ch-01-introduction.qmd` and its companion notebook, `notebooks/ch-01-introduction.ipynb`, at `main`, `3f9cf2cef801181236c9cceaf71f3b63c3ad2491`.

**When:** 2026-11-18.

**Method:** five anonymous composite personas, each a kind of student this course has, reviewed the week independently. Each read the chapter and the slides, typed and ran its own code for every lab step it could from the students' copy, made the mistakes its background makes, attempted the Recommended Exercises in the companion notebook on an article of its own choosing, and opened the key only after an honest try. Each review is a **steel man**: it first makes the strongest case for the materials as designed, and only then says where they fall short for that student. This document puts the five together. Every ranked finding was then checked against the repository and the textbook, and is marked **verified** (with how) or **reported, not verified**. Every proposed fix names the file on #217's branch, or in the textbook, that it would change, so it can be made before #217 merges.

## Who reviewed

| | Degree and major | Python and data background | Interest | Skill |
|---|---|---|---|---|
| A | BS senior, Information Science | One intro Python course; spreadsheets | Qualitative and design: online communities, UX | Minimal |
| B | BA junior, Journalism and Communication | No Python before this course; strong with public records and Excel | Data journalism, local government | Minimal |
| C | BS senior, Business Analytics | Excel, some SQL, a little pandas | Quantitative analytics: markets, customer data, dashboards | Minimal to moderate |
| D | MS first year, Data Science (BA in Statistics) | Fluent in R, moderate pandas; regression and sampling | Quantitative: measurement and validity | Moderate |
| E | MS first year, Information Science (BS in Computer Science) | Moderate Python, git; little data analysis | Design and tools: automation, APIs, building things | Moderate |

## What each completed

Week 1 meets on Friday only, so the lab is one part: Steps 0–6 in class, Steps 7–9 after class, then Step 10 ("What did we learn?") and a last cell that points at the week's first-issue activity. No cell in the key is tagged `not-run-live`, so every persona ran every cell it could. No persona filed a GitHub issue (see "Environment blocks").

| | Lab steps finished | Blocked, read from the key's saved output | Recommended Exercises |
|---|---|---|---|
| A | 0–8, all microsprints; Step 9's first two cells; Step 10 | Step 9's microsprint (429 twice) | Steps 1–7, on `Reddit`, March 2024 |
| B | 0–9, all microsprints, after waiting out 429s; Step 10 | Nothing in the end; Step 8's loop and Step 9 needed reruns | Steps 1–6, on `Boulder,_Colorado`; Step 7 in part (no event found) |
| C | 0–9, all microsprints, after waiting out 429s; Step 10 | Nothing in the end | Steps 1–6, on `Tesla,_Inc.`, October 2025; Step 7 answered without an event |
| D | 0–2 and 4–7 live; 3's month from the checkpoint; 9's misspelled-title cells live; Step 10 | Step 3's day, Step 8's weekly cells, Step 8's and Step 9's microsprints | Steps 1–7, on `Sampling_(statistics)`, January 2026 |
| E | 0–9, all microsprints, after waiting out 429s; Step 10 | Nothing in the end | Steps 1–7, on `Application_programming_interface`, December 2025; Step 7 partial |

**Estimated time for a real student of that background, in minutes** (the lab's own minutes in the last row):

| | Steps 0–6, in class | Steps 7–10, after class | Exercises |
|---|---|---|---|
| A | 65–80 | 35–40 | 60–75 |
| B | 75–90 | 40–50 | about 75 |
| C | 75–85 | about 35 | about 40 |
| D | 35–40 ("a student with less Python would need the full 50") | about 25 | about 40 |
| E | 45–55 typing; 70–80 with the Discuss boxes | about 35 | about 25 |
| **The lab** | **50** in the headings, plus **13** in four microsprints and seven Discuss boxes | 22 in the headings, plus 10 in microsprints and Step 10's 5 | none given |

## Environment blocks

These come from the review machine, not from the materials. They are kept apart so that none is read as a flaw in the week.

- **Wikimedia's pageviews API answered 429 Too Many Requests in bursts (all five),** because the five reviewers shared one address. It hit Step 3's day request, Step 7's year, Step 8's four-university loop, Step 9's microsprint and the exercises' Step 3, in different runs. `Retry-After` was 7 to 42 seconds (C, E). Reruns after a wait got the intended answers, except where the table above says otherwise. What the lab gives a student who meets a 429 is a design point, and it is ranked (item 5).
- **The checkpoint URL answered 404 (B, C, D, E).** Step 0's `checkpoints` reads `labs/week-01/data/` from `main`, and that folder is only on #217's branch. D read `jan2026.json` from the branch instead. This is a merge-order item, not a flaw: it is fixed by merging #217 (see "Suggested next step").
- **No GitHub issue was filed (all five).** The last cell, "From the lab to the textbook", was read and not done.
- **Nothing was refused by a site.** `en.wikipedia.org/robots.txt` allows `/wiki/` pages for every agent, and `wikimedia.org` has no `robots.txt` (a redirect to a 404). Wikipedia answered every page request.

## The strongest case for the week as designed

**Every new request starts small enough to predict, and the prediction is checked.** All five said so. Step 1 asks for the status code and the first 200 characters before anything is parsed; Step 3 asks for one day, January 1, and prints the whole answer, one item with 657 views, before asking for the month. B, a reporter, called it "checking one record against the source before pulling the whole file"; C compared it to running a SQL query on one row first; D called it "a small check, run before the large one, that the address, the date format and the answer's shape are what you think they are". When the month came back with 31 items, E "believed it, because I had seen the shape of one item". C also found that printing the status and the whole text before `.json()` is what showed the 429 on its first run; a cell that only parsed would have shown just a `JSONDecodeError`. The deck's "Step 3: the address is the question" frame, one part of the address per line with its name, was singled out by A ("turn[s] the URL from a blob into a sentence"), C ("a set of filters, like WHERE clauses") and E.

**Step 1's microsprint makes the User-Agent a decision by the server, not a magic line.** The same address answers 200 with `headers` and `403 Forbidden` without them, with "Please set a user-agent and respect our robot policy" in the body (all five). For B it is "the records-request logic I already know"; A "understood why the header is in my code instead of treating it as a magic line to copy". E added Step 2's `http://` request, which ends at `https://` with a 301 in `.history`, as the moment the lab teaches HTTP and not just `requests`.

**The typed cells are the right size, and "By hand, then given" makes the function readable.** Typed cells are one to four lines, and the prompt names the variable to create (`day_url`, `month_response`, `busiest`), so no persona faced a blank cell; C wrote 30 cells with no syntax error. The parts a beginner couldn't invent are given: the `headers` cell, the weekday average, `get_daily_views`, the four-university loop with its `time.sleep(1)`. Because Steps 3 and 4 were typed first, Step 7's "find the lines you typed: only the article and the dates became parameters" worked for A, B, D and E; E called it "the best abstraction move in the week".

**Small steps carry real data lessons.** Step 6's microsprint shows that a CSV round trip brings `timestamp` back as a number and `date` as text, and that `parse_dates=["date"]` fixes the date: "a real data-integrity lesson in two lines" (D, and E in the same words). Step 9's misspelled title gets a 404 whose `detail` blames the dates or the project, then a `KeyError: 'items'` that names nothing; D "did not expect an intro lab to cover that", and E called it "the most useful ten minutes of the week". The weekday microsprint (Tuesday 739, Saturday 579) gave A and B a question about who reads the page; the Discuss boxes on bots, digital traces and what a saved copy can't tell you are the validity vocabulary C and D wanted.

**The Recommended Exercises are the lab again, on one's own article.** Step 10 maps each exercise step to the lab step that models it, and all five finished Steps 1–6 of the exercises, B and A with minimal Python. A ran the whole loop twice, "CU Boulder, then Reddit", and "could reuse it".

## Where it falls short, ranked

The privacy problem and the wrong-result problems come first. After them, items are ranked by how many personas hit each, how badly, and whether it stopped A or B. Cell numbers are positions in `labs/week-01/lab-01-key.ipynb` at `a91f57f`, counted from 0; the students' copy is made from the key and has the same positions.

1. **`requests.get(url, headers)`, without `headers=`, puts the student's email in the address and gets a 403 that carries on silently.**
   - **Who:** B.
   - **What happened:** cell 8's prompt says "request url, sending headers=headers". B wrote `requests.get(url, headers)`. The second positional argument of `requests.get` is `params`, so the dictionary was sent as a query string: no error, no User-Agent header, and `requests`' default User-Agent, which Wikipedia answers with 403 and "Please set a user-agent…". B went on into Step 2, where `Content-Type` was `text/plain` and `print(response.url)` (cell 15) printed the address with `?User-Agent=WebDataScience%2F1.0+%28` and B's email address in it, then `dir()` toured a failed response. B noticed only because the Step 1 microsprint's 403 "looked the same".
   - **Why it matters:** this is the likeliest slip for a student who has seen `requests.get(url)` and adds the dictionary. The intended 403 in the microsprint makes the wrong 403 look like the lesson. The email goes out in a URL, which servers log, and is printed on the student's screen and saved in the notebook's outputs.
   - **Proposed fix:** lab key, Step 1's text (cell 6) and cell 8's prompt: "spell out `headers=headers`: without `headers=`, `requests` puts your email in the address and Wikipedia answers 403". Step 1's microsprint Share (cell 10): "if Step 1 also gave 403, look for `headers=`". Deck, "Step 1: your first request": the same sentence in the narration.
   - **Status:** verified: `inspect.signature(requests.get)` in requests 2.34.2 is `(url, params=None, **kwargs)`; a request prepared with the header dictionary in that place has the User-Agent and email as a query string in its URL and no User-Agent header; the key's cell 11 shows the default User-Agent gets 403.

2. **A natural-looking title that is a redirect returns a clean 200 with tiny counts.**
   - **Who:** C.
   - **What happened:** in Exercise Step 3, C typed `article = "Tesla Inc"`. The request raised nothing, came back with 31 items, and every item's `article` was `Tesla_Inc`, with 18 views on October 1 and at most 34 in the month. The pageviews API doesn't follow redirects, so it counted the redirect page. The real article, `Tesla,_Inc.`, had 7,551 views on October 1. C noticed only because the number "looked tiny for Tesla". Step 9 and its Discuss teach that a misspelled title fails loudly; nothing says a real but non-canonical title succeeds quietly.
   - **Why it matters:** a student who only plots hands in a believable flat line. The same risk is in the lab: Step 8's microsprint (cells 59–60) has students type a university's title, and the given loop would sum a redirect's handful of views without complaint.
   - **Proposed fix:** lab key, Step 3's Discuss (cell 30): "A title that redirects returns its own, tiny counts with status 200. Where do you get the exact title?" Cell 59's text already says "as its title is spelled in the address bar"; add "after Wikipedia has taken you to the article". Chapter and companion notebook, Exercise Step 3: "copy the title from the address bar of the article itself, and print the first item's `article` and `views` before going on." (C suggests a worked redirect example in the lab; the instructor would check one first.)
   - **Status:** verified from C's saved run: the request's items name `Tesla_Inc` (18 views on the first day, a maximum of 34), and `tesla_oct2025.json` names `Tesla,_Inc.` (7,551 on October 1). That `Tesla_Inc` is a redirect page is C's report; it was not re-requested. #217's own table of mistypes found "spaces in the title" harmless, which holds only when the spaced name is the article's real title.

3. **The API leaves out days with no views, so a quiet article's "month" is short.**
   - **Who:** E.
   - **What happened:** E asked for `Norlin_Library`, December 2025, and got 26 items, not 31. Nothing in the lab or the chapter says that days with zero views are left out, and the lab's Step 3 teaches that a month gives 31 items. `ax.plot` then draws straight lines across the missing days, and a sum or mean over the items is a sum over the days that had views.
   - **Why it matters:** students pick their own article in the exercises, often a niche one. A student who notices 26 thinks the code is wrong; one who doesn't plots a month with invisible gaps.
   - **Proposed fix:** chapter and companion notebook, Exercise Step 3: "check `len(data["items"])`: a quiet article can return fewer days than the month has, because days with no views are left out." Lab key, Step 3's Discuss (cell 30): "Would every article give 31 items for January?" The lab's own case is unaffected: `jan2026.json` has all 31 days.
   - **Status:** verified: one request for `Norlin_Library`, 20251201 to 20251231, returned 200 and 26 items, without December 2, 3, 14, 19 and 26; the smallest day present had 1 view. `jan2026.json` has 31 items, January 1 to 31.

4. **In the companion notebook, a failed exercise request silently reuses the chapter's CU Boulder data under the student's title.**
   - **Who:** D.
   - **What happened:** the companion notebook's chapter cells define `headers`, `url`, `response`, `article`, `data` and `df` (cells 14, 20, 22 and 24), and the exercise cells reuse those names. D ran the notebook from the top; Exercise Step 3 set `article = "Sampling_(statistics)"`, got a 429, and stopped at `.json()` before `data` was assigned. Step 4 then built a 31-row DataFrame from the chapter's `data`; Step 5 drew University of Colorado Boulder's counts under the title "Wikipedia Pageviews: Sampling_(statistics)"; Step 6 saved them as `sampling_pageviews.csv`; Step 7 reported January 22 with 902 views, CU Boulder's busiest day, not D's article's (January 27, 518).
   - **Why it matters:** the output looks right and the plot's title makes it look checked. Any failure between setting the title and assigning `data` does it: a 429, a dropped connection, a typo in the `.json()` line.
   - **Proposed fix:** companion notebook and chapter, Recommended Exercises: a line above Step 1, "Restart the kernel and run only the exercise cells"; in Step 4, "print `df["article"].unique()`: it should be your article". Lab key, Step 10's "Recommended Exercises ahead" (cell 70): "start the companion notebook in a fresh kernel; you'll define `headers` again". Distinct names in the exercises (`ex_data`) would also work, but the chapter's prompts name `data["items"]`.
   - **Status:** verified: the companion notebook at `3f9cf2c` (its exercise prompts say "Convert `data["items"]`", and nothing resets the chapter's names); D's saved run shows Step 4's head as `University_of_Colorado_Boulder` and Step 7's 902 on January 22, the key's numbers.

5. **A 429 shows up as `JSONDecodeError`, and the one checkpoint covers only the month.**
   - **Who:** A, B, C, D, E.
   - **What happened:** a 429's body is plain text (or HTML), so the next `.json()` raises `JSONDecodeError: Expecting value: line 1 column 1 (char 0)`, which names no status code. In Step 3, D then got `NameError: name 'data' is not defined` in six cells in a row. Only cell 24 prints the status and text before parsing. Cell 27 prints the month's status, but cell 28 parses whatever came back; `get_daily_views` (cell 52) never looks at the status, so Step 7's year, Step 8's four-university loop and the exercises fail the same way. The only saved copy is January (`jan2026.json`), behind a commented cell (29) that says "only if the cells above stopped". The chapter's Common Issues lists 403 and `ConnectionError`, not 429 or `JSONDecodeError`. Step 7's Discuss asks the right question ("If Wikimedia answered 429…, which line would fail, and would its error say why?"), but after class.
   - **Why it matters:** the key's own run met 429s on and off for 30 minutes, and a class of thirty on one campus address sending the same first call may well do the same. A student with little Python reads `JSONDecodeError` as "I broke my JSON" and fixes the wrong cell. The 429s in this review came from reviewers sharing an address; the missing fallback is a design point.
   - **Proposed fix:**
     - Lab key, Step 3's text (cell 20): "If a status isn't 200, read the text and don't go on: 429 means wait the seconds in `Retry-After` and run the cell again, or use the saved copy below." (The lab's rule is no error handling in code, so this is a sentence, not a `try`.)
     - Lab key and `labs/week-01/data/`: a second checkpoint, the four universities' 2025 daily views (one file, as the given loop gets them), loaded by a commented given cell under Step 8's loop; Step 7's year is its first column.
     - Lab key, Step 9's Discuss (cell 69): "a 429's body isn't JSON: what does `.json()` say then?"
     - Chapter, Common Issues: a 429 line ("Too many requests: wait the `Retry-After` seconds; `.json()` on its body raises `JSONDecodeError`").
   - **Status:** verified: cells 24, 27–29 and 52; `labs/week-01/data/` holds only `jan2026.json` and its README; the chapter's Common Issues at `3f9cf2c`; the key's note on its own 429s. The `Retry-After` values are the personas'.

6. **"How many items" has two readings, and the wrong one prints the right answer for one day.**
   - **Who:** A, C, E.
   - **What happened:** cells 25 and 28 say "print how many items it has". A, C and E each first wrote `len(day_data)`, which is 1 because the dictionary has one key, `items`, and matches the one item they predicted. For the month, `len(data)` is also 1, which A read as "the request had only returned one day". Then `day_data["views"]` gave `KeyError: 'views'` (A, E) and `day_data["items"]["views"]` gave `TypeError: list indices must be integers or slices, not str` (C). The path is said in words only in the Discuss box after Step 3, and in code on the deck's "Step 3: read the day" frame.
   - **Why it matters:** the one-day check is the lab's main idea, and this slip passes it. A minimal student reads "items" as an ordinary word.
   - **Proposed fix:** lab key, cell 25's prompt: "print `len(day_data["items"])`, the number of days, and the first day's `"views"` (`["items"][0]`)"; cell 28: "how many items `data["items"]` has". Step 3's text (cell 20): "The answer is a dictionary with one key, `items`; its value is the list of days."
   - **Status:** verified: the day's body in cell 24's saved output has one top-level key; the prompts' wording; the deck frame's code.

7. **The lab's 50 minutes, and its microsprints, don't fit week 1's one 50-minute Friday.**
   - **Who:** A, B, C, D, E. A, B and C rate pace 2.
   - **What happened:** Steps 0–6's headings add to 50 minutes (5 + 8 + 7 + 11 + 8 + 5 + 6); the four microsprints add 13 more (3 + 3 + 3 + 4), and there are seven Discuss boxes. Step 3 is eight typed cells in 11 minutes. The class meets 12:20 to 1:10, and week 1's Friday also holds the orientation and lecture frames and the 20-minute first-issue activity ("Your turn": 7 + 2 + 1 + 5 + 5). The deck's "This week at a glance" says "Today is orientation and introduction to GitHub" and doesn't mention the lab. Persona estimates for Steps 0–6 alone: 65 to 90 minutes for A, B and C; 70 to 80 for E with the Discuss boxes; 35 to 40 for D.
   - **Why it matters:** if the lab runs over, the microsprints and Discuss boxes are cut, and they hold the 403, the type loss and the weekday question. A student whose environment fails is a spectator for the whole lab.
   - **Proposed fix:** the instructor's decision, raised in #217. The personas' candidates:
     - Say in the opening cell (cell 0) and the "Lab 01" frame what is cut first: microsprints and Discuss boxes, with Steps 0–4 the must-do (B, C).
     - Say whether a microsprint's minutes are inside its step's (A, E).
     - Move Steps 5 and 6 after class with 7–9 (none proposed it in these words; it follows from the arithmetic).
   - **Status:** verified: the headings and microsprints in the key; `syllabus/syllabus.tex` (`\starttime`, `\endtime`: 12:20 to 1:10 pm); the deck's "Your turn" and "This week at a glance". The persona times are their own.

8. **The lab says set up before class; the handout and the deck say before Monday, and nothing says how to get the notebook.**
   - **Who:** A, C; B in passing.
   - **What happened:** the lab's "Before class" (cell 0) says install Anaconda, make `webdata` and open this notebook. `handouts/week-01/setup.md` is headed "Do this before Monday, August 24"; the deck's at-a-glance alert block and its "Before Monday" frame say the same, with "Bring a laptop --- today included". The "Lab 01" frame says the notebook is "`labs/week-01/lab-01.ipynb` in the course repository"; the handout never mentions it or how to download one notebook, and Git is introduced the same day.
   - **Why it matters:** the student most likely to have failed the install, A or B, is the one who loses the whole lab.
   - **Proposed fix:** the instructor's decision with item 7. The personas' wording: one date in all three (lab cell 0, the deck's at-a-glance and "Before Monday" frames, the handout's first line); one line on getting the notebook (a link to the raw file); and a fallback for a student whose environment isn't ready ("share a neighbor's screen today, and set up before Monday").
   - **Status:** verified: cell 0, the handout's first line, both deck frames; the handout has no "lab-01".

9. **Step 10 is under "After class" but is about Steps 1–6, and "Steps 7–9" leaves it out.**
   - **Who:** A, B, C, D, E.
   - **What happened:** the opening cell and the "Lab 01" frame say Steps 0–6 in class and 7–9 after. Step 10, "What did we learn? (5 minutes)" (cell 70), comes after Step 9, under the heading "After class, on your own: Steps 7–9" (cell 50), and asks about Steps 1, 3, 4 and 6. Its exercise list also cites Step 9, which an in-class student hasn't done.
   - **Why it matters:** no student can tell whether to answer it in class or at home, and "5 minutes" after class reads as optional.
   - **Proposed fix:** lab key: move Step 10 above cell 50 and renumber (Step 7, then 8–10), or keep it last and say "Step 10, after class" in cell 0 and the deck's "Lab 01" frame. In its exercise list, "(after class)" before the Step 9 reference.
   - **Status:** verified: cells 0, 50 and 70; the deck frame.

10. **Questions about the busiest day ask for stories the data can't support.**
    - **Who:** D; A, B, C and E for the exercise.
    - **What happened:** Step 4's microsprint shares "the busiest and the quietest day of the week". Tuesday (739) beats Wednesday (736) by 3 views; each weekday's mean is of 4 or 5 days, the daily standard deviation is about 96, and the first ten days of January are winter break (D). Exercise Step 7 asks to "connect [the busiest day] to a real-world event". None of the five could do it without outside research; C's busiest day (9,161) was 0.3% above the next (9,132), a tie. The lab's Step 4 Discuss does say "The data says which day was busiest, not why"; the exercise doesn't give that permission.
    - **Why it matters:** a careful student writes a non-answer and fears the rubric; a less careful one writes a confident story. For D this is the week teaching students to read noise as findings.
    - **Proposed fix:** lab key, Step 4's microsprint Share (cell 36): "weekdays against weekends, and how many days are in each average" (or `.agg(["mean", "count"])` in the given cell 38). Chapter and companion notebook, Exercise Step 7: "the top three days and how far each is above the median; if they are close, say so. Can you connect the busiest to an event, or say what you would need to check?"
    - **Status:** verified from `jan2026.json`: Thursday to Saturday have 5 days each, Sunday to Wednesday 4; the means and the 95.9 standard deviation match the key's cells 34 and 38. C's Tesla numbers are from C's saved CSV.

11. **The checkpoint URL reads `main`, where the data folder doesn't exist until #217 merges.**
    - **Who:** B, C, D, E.
    - **What happened:** cell 4 sets `checkpoints` to `raw.githubusercontent.com/cuinfoscience/INFO4617-Fall2026/main/labs/week-01/data/`; uncommenting cell 29 today gets a 404 page and a second `JSONDecodeError`.
    - **Why it matters:** only if #217 isn't merged before the lab is taught. It is the fallback for item 5.
    - **Proposed fix:** merge #217 before it's needed, then request the URL once. Cell 29's comment could add "a 404 here means the saved copy isn't published yet: ask".
    - **Status:** verified: `origin/main` has no `labs/week-01/data/`.

12. **Two prompt conventions trip the minimal personas: "name: …" means assign, and an f-string needs its `f` and braces.**
    - **Who:** B, A.
    - **What happened:** cell 37 reads `# Microsprint: weekday, each date's day name: df["date"].dt.day_name()`. B read the name as part of a hint, typed only the expression, and got `NameError: name 'weekday' is not defined` from the given cell; "I learned this convention only by getting it wrong three times". In cell 22, B left off the `f` and A the braces; the cell runs, and the request two cells later stops with `MissingSchema: Invalid URL '{api_url}/…': No scheme supplied. Perhaps you meant https://…`, whose suggestion points the wrong way.
    - **Why it matters:** both slips are about the prompts, not Python, and the minimal personas lost several minutes each.
    - **Proposed fix:** lab key, cell 37: `# Microsprint: weekday: df["date"].dt.day_name()`, the shape of every other prompt; cell 0 or Step 0's text: "a name and a colon at the start of a prompt means: give the result that name with `=`". Cell 22's prompt: "then print `views_url`: it should start with `https://`".
    - **Status:** verified: the prompts of cells 22 and 37 and the given cell 38's use of `weekday`. The error texts are the personas'.

13. **Step 2's microsprint sends students to `help()`, which fails on the attribute they're most likely to pick.**
    - **Who:** A; C, D and E on the unreadable `dir()`.
    - **What happened:** cell 17 says list the attributes with `dir()`, skip the `_` names, pick one and "look it up with `help()` or the Response documentation". `print(dir(response))` is one line of 61 names, 23 without an underscore. A picked `elapsed` (the key's choice too); `help(requests.Response.elapsed)` raises `AttributeError: type object 'Response' has no attribute 'elapsed'`, because `elapsed` is set on each response, not on the class.
    - **Why it matters:** it is the first time the lab says "look it up", and the tool it names fails.
    - **Proposed fix:** lab key, cell 17: "look it up in the Response documentation" (drop `help()`), and name three safe picks (`reason`, `encoding`, `elapsed`). A given line that prints the names without underscores would make `dir()` readable, but it is a comprehension, which #217 took out on purpose; the instructor's call.
    - **Status:** verified offline: the `AttributeError`, and 61 and 23 names on a `Response` in requests 2.34.2.

14. **The deck says exercises are submitted on Fridays; the lab and course facts say Sunday.**
    - **Who:** B, C, D, E.
    - **What happened:** "A book built for this course" says "Notebook have exercises we will work on Wednesdays and you will submit on Fridays"; "The weekly rhythm" and Key takeaways #2 give Monday, Wednesday, Friday as concept, lab, revisions. The lab's Step 10 says the Recommended Exercises are "due Sunday", as `docs/course-facts.md` does.
    - **Why it matters:** students plan the week around the deadline, and on week 1's Friday the deck is what's on screen.
    - **Proposed fix:** deck, "A book built for this course": "Notebooks have exercises, due the Sunday after the lab". The rhythm frames are the instructor's and depend on the next offering's calendar; #217's "Your frames" already proposes these edits.
    - **Status:** verified: the frames; course-facts lists the at-a-glance and weekly-rhythm frames as "not yet changed (the instructor's)".

15. **The exercises send students to "any web page you choose" with no word about `robots.txt`.**
    - **Who:** A.
    - **What happened:** Exercise Step 2 says "retrieve any web page you choose". The lab only ever asked Wikipedia. A, whose interest is online communities, named Reddit as the site a new student would try, and Reddit refuses scripts. A checked `robots.txt` first, but nothing in the week said to.
    - **Why it matters:** the first request a student sends on their own is to a site the course hasn't prepared them for, a week before the ethics chapter.
    - **Proposed fix:** chapter and companion notebook, Exercise Step 2: "A Wikipedia article is a safe choice. For another site, read its `/robots.txt` first (chapter 2)." Lab key, cell 70's Step 2 line: the same, briefly.
    - **Status:** verified: the exercise's wording at `3f9cf2c`. That Reddit refuses scripts is A's report.

16. **The bot question is left for week 10, though it is one word away.**
    - **Who:** C, D.
    - **What happened:** Step 5's Discuss says the counts include crawlers and bots and asks which claims the plot can support. D changed `all-agents` to `user` in `views_url` and got 13,659 user views of 20,822 for January 2026, 66%, between 52% and 77% a day, with the peak still on January 22.
    - **Why it matters:** for C and D this is the week's central validity question, and the machinery is on screen. It is also more lab time (item 7).
    - **Proposed fix:** an after-class microsprint at Step 8, or Additional Exercise wording in the chapter: "change `all-agents` to `user` in `views_url`, rerun the month and compare the sums." Not in the Friday part.
    - **Status:** the 20,822 total is verified from `jan2026.json`; the user counts are D's, not re-requested. `user` is one of the API's documented agents, as #217's check of the specification lists.

17. **The motivation for a qualitative or journalism student stays in the Discuss boxes.**
    - **Who:** A, B.
    - **What happened:** the lab's opening says what it does, not why anyone would want a month of pageviews. B could find the busiest day of `Boulder,_Colorado` but had no way to tie it to an event; A found Reddit's IPO day only by searching the news.
    - **Proposed fix:** lab key, Step 4's Discuss (cell 39), the "real event" bullet: "search the date and the article's subject in a news archive, and look at the article's edit history that week (week 10)."
    - **Status:** reported; a judgment about scope.

18. **The given function hides what it depends on.**
    - **Who:** E.
    - **What happened:** `get_daily_views` (cell 52) reads `api_url` and `headers` from the notebook, has no `timeout=`, and never looks at the status. After a kernel restart, Step 7 alone raises `NameError`. E would copy it into a project as it is.
    - **Proposed fix:** lab key, cell 52: one comment line, "uses `api_url` and `headers` from Steps 0 and 3". E also proposes a given cell after Step 9 that calls the function with `raise_for_status()`; that is error handling, which `labs/AUTHORING.md` leaves out of a lab and names in a Discuss question instead, as Step 7's does. So it isn't proposed here.
    - **Status:** verified by reading cell 52.

### Corrections

Claims in the reviews that turned out wrong, out of date, or inexact, and what this document does with them:
- **A and B: the checkpoint's date, 2026-11-18, is "in the future" of the deck's August 21.** The lab was rebuilt for the course's next offering (course-facts, "Week 1's lab, for the next offering"), and 2026-11-18 is the date of the key's run. The deck's date is on #217's list of "Dates to change for the next offering". Dropped.
- **B: Step 8's microsprint doesn't say whether an underscore is needed.** Cell 60's prompt says "with underscores", and a title with spaces works (B's "Colorado College" returned 87,332 views; #217 found the same). What remains is a redirect title, item 2.
- **B: "the week asks for two different deliverables".** The lab not being turned in and the exercises being due Sunday agree with course-facts; the mismatch is the deck's "submit on Fridays", item 14.
- **C: an example redirect, `University_of_Colorado` or `CU_Boulder`.** Not checked; item 2 leaves the example to the instructor.
- **The checkpoint's 404 (B, C, D, E)** is the state of an open pull request, not a flaw; item 11 is a merge-order step.
- **C's difficulty rating, 4, "about right, a little easy".** On the scale, 5 is hardest; the rating is recorded as given, but C's words say easier than 4.

## Disagreements

- **Too slow or too fast.** A, B and C rate pace 2 and need 65 to 90 minutes for Steps 0–6; D rates it 4 and finished in 35 to 40, and wanted "a step with a real choice or a check". E sits between (3; 45 to 55 minutes typing, 70 to 80 with discussion). All five agree the Friday around the lab is the risk, not the lab's cells (item 7). The gap suggests marking what can be skipped for A and B, and giving D and E an after-class extension that asks a validity question (item 16), not more typed cells.
- **What to add, against what to cut.** B and C would mark microsprints and Discuss boxes "if time"; C and D would *add* a microsprint for `user` against `all-agents`; E would add `Retry-After` and timeouts. Each addition costs class minutes, which is why item 16 goes after class.
- **Error handling.** E wants `raise_for_status()` shown after Step 9; the lab's rules leave error handling out and name it in a Discuss question. B, C and D ask only for a sentence on what a 429 looks like (item 5), which fits the rules.
- **What the week is for.** For A and B it is provenance and the people behind the numbers, and they rate motivation 3; for C, D and E it is the loop and its validity, and they rate it 4.

## Ratings

Each on a scale of 1 to 5. For difficulty, 5 is hardest for that persona's background.

| | A | B | C | D | E | Mean |
|---|---|---|---|---|---|---|
| Clarity of motivation | 3 | 3 | 4 | 4 | 4 | 3.6 |
| Pace | 2 | 2 | 2 | 4 | 3 | 2.6 |
| Difficulty for my background | 3 | 3 | 4 | 2 | 2 | 2.8 |
| How much I learned | 4 | 4 | 4 | 3 | 4 | 3.8 |
| Confidence I could do this on my project | 3 | 3 | 4 | 4 | 4 | 3.6 |

What holds the confidence down: A wouldn't know how to handle a failed request or find the "why" behind a spike; B couldn't yet handle a 429 or a bad title, and doesn't know where to find numbers for local government; C fears the 429s and the redirect, "both [of which] would damage a deliverable"; D wants a rate-limit habit and a check that the data is what was asked for (items 4 and 5); E would add status checks and a timeout first.

## Small things

Lab (`labs/week-01/lab-01-key.ipynb`):
- Step 4's text (cell 31) gives `format` but not what `"%Y%m%d00"` means; the `00` is the hour, as a literal (B). `"%Y%m%d%H"` also parses it (E).
- Step 5, cell 41: "show it" led E to type `fig`, and the figure appeared twice; the key uses `plt.show()`. Name `plt.show()` in the prompt (E; reported, not tried).
- Step 4's given cell 38 groups by a Series, `df.groupby(weekday)`; one comment line, "groups the rows by the day names we just made" (E).
- Step 6's microsprint: `timestamp` came back as `int64`, which B didn't see as a change; the Share could say "two columns changed" (B).
- Step 8's Discuss asks why the first and last weeks are low, but the typed cell shows only `weekly.head()`; `weekly.tail()` is needed for the last week (C).
- Dtypes print `str` on pandas 3 and `object` on pandas 2; a student on an older environment will think something is wrong (A, C, D, E).
- `from bs4 import BeautifulSoup` in Step 0 isn't used until week 6 (E).
- Run All stops at Step 9's deliberate `KeyError` in the students' copy, because `make_student_copy.py` drops tags, so Step 9's microsprint never runs (C, E). Cell 63 could say "run the cells after it one at a time".
- The lab's User-Agent (`… python-requests/<version>`) differs from the chapter's and the exercises' (`WebDataScience/1.0 (your-email@colorado.edu)`); one sentence on why, and in Step 10 that the companion notebook needs it defined again (all five).

Deck (`slides/week-01/week-01.tex`):
- "A book built for this course": "Notebook have" should be "Notebooks have"; "Notebooks might have errors for you to fix or that the repo needs to fix" is unclear (C, D).
- "Step 1: your first request" builds the address from `wiki + …`, and the narration says the notebook writes it in one line; four personas noticed the difference. It is deliberate (#217: to fit the frame) and harmless.
- "Common sequence across topics" shows the instructor's `pageviews.pdf`, years of views with a spike near 17,500, and says students can make "this visualization" after the chapter; the lab's plot is one January of 500 to 900 a day (D, E; reported, the figure wasn't opened). A caption saying what it shows.

Chapter and companion notebook (`3f9cf2c`):
- The companion notebook shows Quarto references as text: `@sec-protocols`, `@sec-ethics`, `@sec-pdfs`, `@sec-data-formats`, `@sec-static-pages`, `[@wing2006computational]`, `[@lazer2009computational]` and more in Social History and Common Issues (C, E; verified in cells 4, 13, 17, 19, 21, 25 and 42–46).
- The companion notebook's Figure 1.3 caption says September 2026 (B); a dated figure, not an error.

## Suggested next step

**Fix first, on #217's branch or with the textbook.** Each is a sentence or a prompt, and changes none of what the week teaches:
1. **Item 1:** "spell out `headers=headers`" in Step 1's text, cell 8's prompt, the microsprint's Share and the deck's Step 1 frame.
2. **Items 2 and 3:** in Step 3's Discuss and the chapter's Exercise Step 3, the exact title from the address bar, a check of the first item's `article` and `views`, and that quiet articles return fewer days.
3. **Item 6:** name `["items"]` in cells 25 and 28, and one sentence in Step 3's text.
4. **Item 5:** one sentence in Step 3's text on reading a non-200 status and waiting out a 429; a 429 line in the chapter's Common Issues; and, if the instructor wants it, a 2025 checkpoint for Steps 7 and 8.
5. **Item 4:** in the companion notebook and chapter, "restart the kernel" above the exercises and `df["article"].unique()` in Step 4. This is a textbook change.

**Merge order:** merge #217 before the lab is taught, then request `labs/week-01/data/jan2026.json` at its `main` address once (item 11).

**Needs the instructor's decision:**
- **The Friday** (items 7 and 8): whether a 50-minute lab fits a 50-minute meeting that also holds orientation and the 20-minute first-issue activity, what is cut first, and the one setup date in the lab, the deck and the handout.
- **Your frames** (item 14): the deck's due day and rhythm frames, as #217's "Your frames" proposes.
- **Where Step 10 goes** (item 9): before "After class", renumbered, or labelled after class.
- **The busiest-day questions** (item 10): the chapter's Exercise Step 7 wording, which serves other terms too.
- **Extensions for D and E** (item 16): a `user` against `all-agents` comparison after class, or nothing this week.
