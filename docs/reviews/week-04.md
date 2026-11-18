# Review: week 04, Data Formats: XML and JSON

**What was reviewed:** week 4's lab (`labs/week-04/lab-04.ipynb`, with its key and its two checkpoints in `labs/week-04/data/`), its deck (`slides/week-04/week-04.tex`), the RSS handout (`handouts/week-04/rss-feeds.md`) and chapter 4's Recommended Exercises, as students meet them.
- **Course repository:** the head of pull request #208, `7d62e42daf985f987a52d4b59d2ce3a760b7e24f`, which rebuilt the lab in three parts and the deck one frame per cell. #208 is open and not merged, so every proposed fix below names the file on that branch, to be made before it merges.
- **Textbook:** `ch-04-data-formats.qmd` and its companion notebook, `notebooks/ch-04-data-formats.ipynb`, at `main`, `3f9cf2cef801181236c9cceaf71f3b63c3ad2491`. Chapter fixes go to the textbook repository, not to #208.

**When:** 2026-11-18, the day after the key's run.

**Method:** five anonymous composite personas, each a kind of student this course has, reviewed the week independently. Each read the chapter and the slides, typed and ran its own code for every lab step it could from the students' copy, made the mistakes its background makes, attempted the Recommended Exercises, and opened the key only after an honest try. Each review is a **steel man**: it first makes the strongest case for the materials as designed, and only then says where they fall short for that student. Reviewers respected `robots.txt`, and were told not to send requests to NASA POWER while the instructor decides how the course reads its `robots.txt` (see "Environment blocks"). This document puts the five together. Every ranked finding was then checked against the repository and the textbook, and is marked **verified** (with how) or **reported, not verified**.

## Who reviewed

| | Degree and major | Python and data background | Interest | Skill |
|---|---|---|---|---|
| A | BS senior, Information Science | One intro Python course; spreadsheets | Qualitative and design: online communities, UX | Minimal |
| B | BA junior, Journalism and Communication | No Python before this course; strong with public records and Excel | Data journalism, local government | Minimal |
| C | BS senior, Business Analytics | Excel, some SQL, a little pandas | Quantitative analytics: markets, customer data, dashboards | Minimal to moderate |
| D | MS first year, Data Science (BA in Statistics) | Fluent in R, moderate pandas; regression and sampling | Quantitative: measurement and validity | Moderate |
| E | MS first year, Information Science (BS in Computer Science) | Moderate Python, git; little data analysis | Design and tools: automation, APIs, building things | Moderate |

## What each completed

The lab has Steps 0–16 and seven microsprints: Part 1 (Monday) is Steps 0–4, Part 2 (Wednesday) Steps 5–10, Part 3 (Friday) Steps 11–16. No persona sent a request to NASA POWER, so every POWER cell ran on a stand-in or was read from the key's saved output (see "Environment blocks"). All five ran Step 2 live against the Clerk, and got the same November 3, 2026 roster as the checkpoint.

| | Lab steps finished | Run on a stand-in, or read from the key | Recommended Exercises | Needed the key for |
|---|---|---|---|---|
| A | 0–14 | 9–10 on three days cut from the year file; Step 10's microsprint and Step 15 typed, results from the key; 16 read, not written | 1–4 live (BBC News front page, 31 items); 5–6 written and tried on made-up data; 7 not written | POWER's outputs only |
| B | 0–8, 11, 13, 14, 16 | 9–10 on a three-day slice; 12 from the checkpoint; Step 10's microsprint and Step 15 read only | 1–4 live (a local news site's feed); 5 not sent; 6 on a hand-made stand-in; 7 written | Nothing; compared afterwards |
| C | 0–8, 11–14, 16 | 9, 10, 12 on slices of the year file; Step 10's microsprint and Step 15 typed, results from the key | 1–7, with BBC News Business and a live Open-Meteo forecast (see "Environment blocks") | POWER's outputs only |
| D | 0–16, all 42 typed cells, no errors of its own | 9, 10, 12 on a stand-in; Step 10's microsprint, Leadville and Grand Junction from the key | 1–4 live (BBC News, 31 items); 5–6 on a synthetic stand-in; 7 drafted | Nothing |
| E | 0–16 | 9, 10, 12 and Boulder's part of 15 on the checkpoint; Step 10's microsprint, Leadville and the third place from the key | 1–4 live (Planet Money, 355 items); 5–6 written, not sent, tried on a hand-made dictionary; 7 written | Nothing; its cells matched the key's but for `print` formatting |

**Estimated time for a real student of that background, in minutes** (the lab's step headings, which include microsprints and discussion, in the last rows):

| | Part 1 | Part 2 | Part 3 | Exercises |
|---|---|---|---|---|
| A | 55 | 75 | 45 | 90 |
| B | 55 | 60 | 45 | about 120 |
| C | 45 | 60 | 40 | 75, plus 15 to choose a feed |
| D | 30 | 40 | 35 | 90 ("double all of that" for less Python) |
| E | 35–40 | 55–60 | 35 | 90–120 |
| **The lab** | **35** | **51** | **35** | none given |
| **The day** | **50** | **50** | **35**, then the 15-minute revision block | due Sunday |

A's and B's estimates are for a student working alone at home, not at the pace of a class that is typing along with the instructor.

## Environment blocks

These come from the review machine and the review's rules, not from the materials. They are kept apart so that none is read as a flaw in the week.

- **No requests to NASA POWER (all five).** POWER's `robots.txt` disallows `/api/` for every user agent, and the whole site for six named AI crawlers (read on 2026-11-18). Reviewers were told not to contact it while the instructor decides. Steps 9, 10 and 12 ran on stand-ins cut from the lab's own `power-boulder-2025.json`; Step 10's microsprint (the longitude without its minus sign) and Step 15's Leadville and third place have no saved file, and were read from the key's saved output. No cell of the key is tagged `not-run-live`: the key's note says every cell ran live from the cloud machine on 2026-11-17, about 45 requests to POWER by #208's count. Whether that should continue is item 3's decision.
- **The checkpoint address answers 404 until #208 merges (all five).** `DATA` reads `https://raw.githubusercontent.com/cuinfoscience/INFO4617-Fall2026/main/labs/week-04/data/`, and `main` has no `labs/week-04/data/` folder yet; it still carries the older one-day `lab-04.ipynb` and key. Every persona served the two checkpoint files locally. This is a merge-order item: #208 has to merge before Wednesday's class. That the failure surfaces as an unrelated `TypeError` is a design point, item 9.
- **Open-Meteo (Exercise Step 5).** A, B, D and E read `https://api.open-meteo.com/robots.txt` (`User-agent: *`, `Disallow: /`) and did not send the forecast request; they tried their Step 6 code on hand-made data. **C sent requests to `api.open-meteo.com` without reading its `robots.txt` first:** C's attempt to read that file reset the connection twice, C went on, one forecast request reset and a retry returned the forecast. C's Exercise Steps 5–6 therefore ran on real data that the host's `robots.txt` disallows. C also ran the companion notebook top to bottom by accident, which sent the chapter's own requests (the Clerk, `jsonverse.dev`, Open-Meteo) without a User-Agent. Both are the reviewer's method, not the materials', but the second shows what any student's "Run all" does (item 3).
- **A simulated a 429 for Step 12's year request** to try the lab's fallback; cell 89 recovered as designed.
- **Nothing else.** The Clerk (no `robots.txt`, 404) and the feeds the personas chose answered every request.

## The strongest case for the week as designed

**Every new tool gets a first call on something a student can read whole, and that is what made the real files unsurprising.** All five said so. Step 1's two-member `house_raw` comes before the 441-member roster, `Counter(["D", "R", "D"])` before the party count, one JSON object before the round trip, three days before 365, and `two_days` before the year. A, "the student who freezes when a cell is blank", "never faced a blank cell without an answer shape", and when the 557 KB roster arrived "already knew which three moves I was making". C called it "the difference between 'it ran' and 'I know what it did'"; E found that Step 1 had already shown "root with `publish-date`, a hyphenated tag, a postal-code attribute". The prompts to predict ("Say what each cell will print before you run it", "Three January highs in Boulder, in °C: what should they look like?") were the first time a course had asked A to predict before running.

**"Look before you parse" is taught by the data, not asserted.** Step 2 prints the status, `Content-Type`, `roster.encoding` and the first bytes, and Step 3's microsprint then pays it off: five last names garbled by `roster.text`, Sánchez as "SÃ¡nchez", with no error (B, C, D, E; positions 59, 65, 143, 282 and 345 verified on the checkpoint). B recognized "the habit I already have from public-records work, opening the document and reading the header before trusting the spreadsheet". E, the API-minded student, called it "the right transferable habit"; the same check returns in Step 9 (status and 200 characters) and Step 12 (fill value and units).

**Step 4 is the best moment of the week for four of the five.** Count, then read the count: `Counter` shows two blank parties, the given loop prints FL20 and TX23 with their footnotes, and a blank becomes a vacant seat rather than a parsing bug; the `('I', 'R')` pair turns "who counts as a Republican?" into a question about the research design (A, B, C, D, E). B: "any reporter has been burned by a count that quietly mixed 'entries' and 'people'". D: "for someone who thinks about construct validity, that is the right lesson". A, whose interest is people rather than numbers: "data work as interpretation, which is where I live". `publish-date`, the checkpoint and Step 16's "which would you save beside your DataFrame?" give the provenance habit that C and D said they would reuse.

**The given cells hide what students couldn't write yet and leave them what they should type.** Step 6 types one record key by key and gives the loop ("your record, for every member"); Step 8 types two broken strings and gives the `try` loop; Step 15 calls `get_daily` once by hand before the given loop (A, B, C, E). B, with no Python before the course, typed every cell without needing the key; D typed all 42 without an error. Step 8's planned errors meant that by Step 10 `KeyError` and `JSONDecodeError` had "already been seen and read" (C).

**The checkpoints and the deck make a missed day cheap.** The roster checkpoint is byte for byte the live file (557,204 bytes, November 3, 2026; D, E), so Wednesday's numbers can't drift, and the year file ran Steps 12–14, plot included, with no network (D, E). E checked every code frame against the key and found differences only in line wrapping, so the deck is "a faithful companion for someone who falls behind". Step 14's closing Discuss, whether a grid cell at 1,801 m lets you write "Boulder had this many freezing nights", was named by C and D as the validity question they care about.

## Where it falls short, ranked

No persona found a privacy problem. Nothing in the lab prints a private individual's contact details: the roster checkpoint carries members' House office rooms and telephone numbers, which are public officials' official contacts (#208 asks whether to trim it), and Step 4's given cell prints footnotes naming members who resigned, also public officials (B). The wrong-result problems come first. After them, items are ranked by how many personas hit each, how badly, and whether it stopped A or B. Cell numbers are positions in `labs/week-04/lab-04-key.ipynb` at `7d62e42`, counted from 0; the students' copy is made from the key by `labs/tools/make_student_copy.py`.

1. **"29 of 56 have both" counts non-voting delegations as states.**
   - **Who:** A, B, C, D.
   - **What happened:** Step 6's microsprint (cells 49–50) builds `table = pd.crosstab(serving["state"], serving["party"])` and the given cell prints `29 of 56 have both`. The 56 rows are the 50 states plus American Samoa, DC, Guam, the Northern Mariana Islands, Puerto Rico and the Virgin Islands, each one member who cannot vote and cannot be split. Six states with one member each (AK, DE, ND, SD, VT, WY) can't be split either. The microsprint's Share line asks for "the number of split delegations", and nothing says what the 56 is. The same mix sits in Step 4: cell 34 prints 439 "serving", which is 433 voting members and 6 delegates. The file marks them: `<district>` reads `Delegate` (five) or `Resident Commissioner` (Puerto Rico).
   - **Why it matters:** it is the number a student carries into a sentence. B "would put 29 of 56 in a sentence without thinking, and the lab's own Step 4 teaches me not to"; D "would put it in a paper". The chapter already explains 441 against 435; the lab doesn't carry it over.
   - **Proposed fix:** lab key, cell 50: drop the six first, `states = table.drop(index=["AS", "DC", "GU", "MP", "PR", "VI"])`, and print `29 of 50 states have both`; or keep the cell and add to the microsprint's Do (cell 48): "The table's 56 rows are the 50 states, DC and five territories, whose one delegate can't vote. Which rows could never be split?" Step 4 (cell 33 or a new given cell): count `district` values `Delegate` and `Resident Commissioner`, so 441, 439 and 435 reconcile. Deck: the frame for Step 6's microsprint, the same change. Step 16's first bullet and its answer (cell 115) can then say "433 voting members and 6 delegates".
   - **Status:** verified on `labs/week-04/data/MemberData-2026-11-03.xml`: 56 rows, 29 with a D and an R; the 50 state rows also give 29; six `<district>` values are `Delegate` or `Resident Commissioner` (AS, DC, GU, MP, PR, VI); 12 rows have one serving member; 439 serving, 433 of them voting. The key's saved output of cell 50 is `29 of 56 have both`.

2. **The lab's Step 6 loop, reused for Exercise Step 4 as the lab says, crashes on a starter feed.**
   - **Who:** E; A, C and D used feeds where every item had a `<link>`, and B a local feed.
   - **What happened:** Step 16's "Recommended Exercises ahead" tells students to reuse "Step 6's record by hand, and its list-of-dictionaries loop" for Exercise Step 4. That loop (cell 46) is the chapter's without its `if m.find(...) else None` guards, which Step 6 drops on purpose because every member has every tag. On Planet Money, a starter feed in both the chapter and the handout, three of 355 items (positions 35, 135 and 142, promotions for other shows) have no `<link>`, and `it.find("link").text` stops at item 35 with `AttributeError: 'NoneType' object has no attribute 'text'`. The guard appears only on the deck's "A missing tag: `None`, and the chapter's guard" frame and in the Friday revision box; Step 6's Discuss asks what would happen, but nothing runs it.
   - **Why it matters:** the first time the guard matters is the first take-home step, after the lab has said it isn't needed. E fixed it in a minute; A or B reads the last line of the traceback, sees nothing about feeds, and may think the feed is broken.
   - **Proposed fix:** lab key, Step 16's Exercise Step 4 bullet (cell 114): "Real feeds leave tags out: Planet Money has items with no `<link>`, and Step 6's loop stops there. Use the chapter's `if ... else None`, from the deck." Step 6's Discuss (cell 51): make its first question runnable, with a given line such as `print(first.find("nosuchtag"))`, which prints `None`. Optionally, `handouts/week-04/rss-feeds.md`: one line under Starter feeds that some items lack a tag.
   - **Status:** verified on E's saved copy of the feed (fetched 2026-11-18): 355 items, no `<link>` at 35, 135 and 142; the unguarded loop stops after 35 rows with that error. The key's cells 46 and 114 read as quoted.

3. **Both of the week's JSON sources disallow automated clients in `robots.txt`, and the exercise's Step 1 tells students to check first.**
   - **Who:** A, B, D, E stopped at Exercise Step 5; C sent the request without checking (see "Environment blocks").
   - **What happened:** Exercise Step 1 (chapter) says to "check the site's `robots.txt` permits fetching it", the habit week 2 teaches. Step 5 then fetches `https://api.open-meteo.com/v1/forecast?...`, whose host's `robots.txt` is `User-agent: *` / `Disallow: /`. The lab's own JSON source is the same case: POWER's `robots.txt` disallows `/api/` for every user agent, and Step 9's Discuss (cell 69) asks "Are we a crawler?" and leaves it open. Neither the lab, the deck nor the chapter says how the course reads a `Disallow` on a documented API endpoint. The chapter's Open-Meteo code (and the companion notebook's cell 40) sends no User-Agent, so a student who runs the notebook from the top sends it anyway.
   - **Why it matters:** Steps 5 and 6 are two of the exercise's seven steps, in a graded notebook. A, the conscientious student, "stopped", and would "hand in an unfinished, graded notebook with no way to know whether that is acceptable"; D: "a less careful one learns that the robots check is decoration". B: "a journalist is going to ask whether we are allowed to do this". Every persona's confidence rating mentions it or the missing-tag case.
   - **Proposed fix:** the instructor's decision first (see "Suggested next step"), then one statement where students read it:
     - **If the course treats a single documented API request as not crawling:** say so, with the reason, in lab Step 9's Discuss (cell 69) and in Step 16's Exercise Step 5 bullet (cell 114), and in the deck's Step 9 frame. The chapter's Exercise Step 5 should say it too, and its Open-Meteo code should send `headers=HEADERS` (textbook).
     - **If not:** save a forecast in `labs/week-04/data/` (or the textbook's `data/ch-04/`) and point Exercise Step 5 at it; or switch the exercise to a host whose `robots.txt` permits it (E). Either is a chapter change.
     - Either way, the companion notebook could say above the exercises "run only the Step cells" (C).
   - **Status:** verified: both `robots.txt` files read on 2026-11-18 (`api.open-meteo.com`: `User-agent: *`, `Disallow: /`; `power.larc.nasa.gov`: `Disallow: /api/` for `*`, `Disallow: /` for six named AI crawlers); `open-meteo.com`, the project's main site, answers `Allow: /`. The chapter's Steps 1 and 5, and its `requests.get(url, params=params)` with no headers, at `3f9cf2c`; the companion notebook's cell 40; cell 69's Discuss.

4. **Only two of the lab's POWER requests have a checkpoint.**
   - **Who:** A, C, E; B and D in passing.
   - **What happened:** `labs/week-04/data/` holds the roster and Boulder's year. Step 12 (cell 89) has a "Given, only if the cell above didn't print 200" loader. Step 9's three days (cell 67), Step 10's microsprint (cell 78), Leadville (cell 108) and the three-place loop (cell 112) go straight to POWER with nothing to fall back on. If POWER answers 429 to a room of thirty, Steps 9–10 and the microsprint can't be done on Wednesday, Step 15 can't be done on Friday, and Step 16's third bullet (Leadville and your place) can't be answered. #208's own note counts about 90 POWER requests a minute from Step 15's loop.
   - **Why it matters:** A "wouldn't know whether I'd done it wrong or the site was down". These are the cells whose result a student would put in a table (C), and the places most likely to hit a rate limit.
   - **Proposed fix:** data: save the key's three answers to `labs/week-04/data/` (`power-boulder-2025-01-01-to-03.json`, `power-east-2025-01-01-to-03.json`, and Leadville's and Grand Junction's years). Lab key: a "Given, only if" loader after cells 67, 78 and 108, as cell 89 does; or, for Step 9, a given cell that slices the year checkpoint (C). For Step 15, `get_daily` could take an optional saved file, so the loop still makes rows for the two saved places (A). If the instructor decides POWER isn't called from class at all (item 3), these files become the lab's source, not its fallback.
   - **Status:** verified: the folder at `7d62e42` holds two files and README; only cells 15 and 89 load from `DATA`.

5. **The fill-value step never shows a fill value.**
   - **Who:** C, D, E.
   - **What happened:** Step 12 asks for `fill_value` (-999.0) and Step 13's given cell (98) replaces it with `NaN` and prints `weather.isna().sum()`: 0, 0, 0. Boulder's 2025 has no missing day, so the cell that protects the mean visibly does nothing, and Step 12's Discuss ("what would it do to a plot of the lows, and to their mean?") has nothing to look at. D: "a zero count is what a broken replace would print too."
   - **Why it matters:** "replace the fill value" is one of the lab's validity claims, and it is the one students copy into a project without seeing it work. "The checks I trust are the ones I have seen catch something. Step 4's vacancies are real; the fill value is not" (E).
   - **Proposed fix:** lab key, Step 13: give `two_days` (cell 93) one `-999.0` in `low`, so `pd.DataFrame(two_days)` shows it; add a given cell that runs `.replace(-999.0, float("nan"))` on it and prints `.mean()` before and after. Optionally print `(weather == fill).sum()` before cell 98's replace, so the zero count is a visible check. Deck: the frames for Step 13.
   - **Status:** verified: `power-boulder-2025.json` has 365 values for each of the three variables and none equals -999.0; the key's saved output of cell 98 is 0, 0, 0.

6. **The exercises ask for two shapes the lab never has students write: a loop that fills a list, and a DataFrame from parallel lists.**
   - **Who:** A, E; B and C for `pubDate`.
   - **What happened:** Exercise Step 4 asks for a loop that builds a list of dictionaries; in the lab that loop (cell 46) is always given. Exercise Step 6 builds a DataFrame from parallel lists (`time`, `temperature_2m_max`); Step 13's `two_days` is a dictionary of dictionaries, the opposite shape, and parallel lists appear only in Step 13's text and Step 16's bullet. A finished both "only because I can copy" (cell 46's shape, the chapter's `pd.DataFrame({...})`). Exercise Step 4's `pubDate` comes back as `Wed, 18 Nov 2026 05:04:31 +0000`; the lab teaches `pd.to_datetime` only with `format="%Y%m%d"` (B, C, E). C first typed `pubdate`, got the `NoneType` error, and found nothing in the lab saying XML tag names are case-sensitive.
   - **Why it matters:** the lab rule says it "sets up the Recommended Exercises but never solves them"; here two steps are set up only in prose. A minimal student can copy, but whether that is learning "is the instructor's call" (A).
   - **Proposed fix:** lab key, Step 13: after cell 94, a given `two_lists = {"date": ["20250101", "20250102"], "high": [5.1, 7.3]}` and a typed `pd.DataFrame(two_lists)` with "which became the rows?" (A, E). This produces a DataFrame, not the exercise's answer, so it passes AUTHORING's "never a Recommended Exercise" test. Step 13's text: one sentence that `pd.to_datetime()` with no `format` reads most written dates. Step 3's text: "tag names are case-sensitive: `MemberData`, not `memberdata`" (C). For the loop, A's suggestion is a two-line typed `for` loop in Step 6's microsprint (print the first three last names); D's and E's view (item 7) points the same way.
   - **Status:** verified: cells 46, 93, 94, 96 and 114; the chapter's Exercise Steps 4 and 6.

7. **Most typed cells hold their own answer, so finishing the lab says little about writing it.**
   - **Who:** B, D, E; A, at the other end, wants more hints (see "Disagreements").
   - **What happened:** of 42 typed cells, D counts about 29 whose comment spells out the expression, such as `# Print the text of the first "lastname" tag: small_soup.find("lastname").text`. B typed "all 30-plus typed cells with no errors"; D's 42 ran with none; E's matched the key's but for `print` formatting. The thinking is in the Discuss boxes, which are collapsed, unanswered in the key, and not turned in. E adds that given and typed cells carry new pandas with no gloss: boolean masks (`df[df["party"] != ""]`), `&` and `.sum()` on booleans, `.iloc[0]`, `.groupby().size()`.
   - **Why it matters:** "as written I could finish the whole lab without deciding anything" (D); B is "still not sure I could write `find("state")["postal-code"]` on my own from a blank cell, which is what the Recommended Exercises ask". The week is otherwise well paced, so this is where the learning is thinnest.
   - **Proposed fix:** lab key: in a few later cells, state the goal and not the expression, such as cell 74, "get the dictionary of daily highs, then the value for January 2" (D); or make the last typed cell of Steps 3, 6 and 10 a "no hint" repeat on another member or variable (B). Put a one-line answer to each Discuss question in the key, for students working alone (B). Step 6's microsprint text: "a comparison on a column gives one True or False per row; in brackets, it keeps the True rows" (E).
   - **Status:** the count of 42 typed cells is verified (cells with `prompt_lines` in the key); D's 29 is reported, not recounted.

8. **The deck's first two frames describe another week.**
   - **Who:** A, B, C, D, E.
   - **What happened:** "This week at a glance" says "Monday: Labor Day --- no class", "Wednesday: Concepts & notebook lab ... Congress, tweets, and weather", "Friday: Textbook revisions"; the lab is three parts, Monday to Friday, with no tweets. The title reads "September 9 & 11, 2026". "Daily note questions" answers questions about GitHub issues and pull requests from week 3.
   - **Why it matters:** it is the frame students plan the week from; D "would have skipped Monday".
   - **Proposed fix:** deck, "This week at a glance", title and "Daily note questions". These are the instructor's frames; #208's description proposes text for the first (Monday: concepts, then Part 1; Wednesday: Part 2; Friday: Part 3, then revisions), which matches what the personas asked for.
   - **Status:** verified at `7d62e42`; the deck's header comment and #208's "Your frames" already flag both as fall 2026's, so this confirms a known item rather than finding one.

9. **A missing checkpoint fails three lines later, as an unrelated `TypeError`.**
   - **Who:** A, B, C, D, E all met it (see "Environment blocks"); B and C name the design point.
   - **What happened:** with the checkpoint address answering 404, Step 5's given cell (41) prints `404 b'404: Not Found'` and then stops at `soup.MemberData["publish-date"]` with `TypeError: 'NoneType' object is not subscriptable`. Step 12's loader (89) fails the same way one cell later, at `.json()`. Neither says "the file is missing".
   - **Why it matters:** Step 5 exists for the student who missed Monday, the one least able to read that traceback. The 404 itself goes away when #208 merges; a moved or renamed file next term would bring it back.
   - **Proposed fix:** lab key, cells 41 and 89 (and any new loaders from item 4). Cell 41 already prints the status first, so the step text (cells 39 and 85) can say "if the first number isn't 200, stop and tell me: the saved file didn't load" (B); or a given `assert saved_roster.status_code == 200, "checkpoint not found"` (C). AUTHORING's "no error handling" rule allows the first; the second is the instructor's call.
   - **Status:** verified by reading cells 41 and 89, and `main` at `91944dc` has no `labs/week-04/data/`.

10. **The likeliest slips give errors that don't point at the fix, or no error at all.**
    - **Who:** A, B, C; E for the Discuss wording.
    - **What happened:**

      | Slip | Cell | What comes back | Who |
      |---|---|---|---|
      | `roster["Content-Type"]`: the one Monday prompt that names a header but not `.headers` | 14 | `TypeError: 'Response' object is not subscriptable` | A |
      | `'{'state': 'Colorado'}'`, single quotes outside and in | 58 | `SyntaxError: invalid syntax`, Python's error, in the step about JSON's | A |
      | `first.state-fullname.text` | 22–23 | `NameError: name 'fullname' is not defined`; the explanation is in Step 3's Discuss, after the cell | B, C, E |
      | `first.find("state").text` for the postal code | 45 | no error: `'Alaska'`, a plausible value, where the loop below gives `AK` | C |
      | `print(weather.shape)` and then guessing "its rows and columns" | 95 | B typed three things for one | B |

    - **Why it matters:** A and B can't read a traceback beyond its last line; C's silent `'Alaska'` would join wrongly to anything keyed on postal codes.
    - **Proposed fix:** lab key: cell 14's prompt, "print `roster.status_code`, then `roster.headers["Content-Type"]`"; cell 58's prompt, the whole line, and "the outer quotes are Python's; the inner ones are what JSON refuses"; Step 3's text (cell 19), "Python reads `state-fullname` as `state - fullname`"; cell 45's prompt, "print `len(record["state"])`: what should it be?"; cell 95's prompt, "Print `weather.shape`, the number of rows and of columns".
    - **Status:** verified: the prompts as quoted; `first.find("state").text` on the checkpoint's first member is `'Alaska'`, and on `house_raw` `'\nColorado\n'`. The error texts are the personas'.

11. **Part 2 is the densest part, and Monday has room.**
    - **Who:** E; A and B by their times; D finds all three comfortable.
    - **What happened:** the step headings add to 35, 51 and 35 minutes against days of about 50, 50 and 35 (`docs/course-facts.md`). Part 2 has 18 typed cells, 42 typed lines, three microsprints and 17 Discuss questions; Part 1 has 15 typed cells and 27 lines, 15 minutes under its day. The personas' Part 2 estimates are 40 to 75 minutes, and A's and B's Part 1 estimates (55) fit Monday only with its slack.
    - **Why it matters:** if Wednesday runs over, Steps 9–10, the week's first live API request, are what get cut, and they are what the exercises' Step 5 builds on.
    - **Proposed fix:** the instructor's decision. Candidates: make cell 75 (`geometry`, `parameters`, `.get("messages")`) given (E); move Step 8's microsprint to Friday's revision block (E); or start Part 2 on Monday with Step 6's record by hand, since Monday has 15 minutes spare. Each touches the lab key, the deck's day sections, and Step 5's setup.
    - **Status:** verified: headings and typed lines counted in the key (typed lines within AUTHORING's 55, 55 and 40); the persona minutes are their own.

12. **Step 3's microsprint hard-codes position 59.**
    - **Who:** A, B, D.
    - **What happened:** cell 27 prints `ours[59], theirs[59]`. Today 59 is Sánchez, because the live roster is still the November 3 edition. When the Clerk adds or drops a member before position 59, the cell prints two matching names, and a student thinks they typed it wrong. The checkpoint, served as UTF-8 by GitHub, garbles nothing at all.
    - **Proposed fix:** lab key, cell 27's prompt: "print both spellings at the first position the cell above printed" (the comment's "then try another" is already there), and the deck frame to match; or have cell 26 print `len(...)` of the positions as well (B), which also answers the Share line's "how many".
    - **Status:** verified: positions 59, 65, 143, 282, 345 on the checkpoint; cell 26 prints positions, not a count.

13. **`get_daily()` depends on two names it doesn't take, and checks nothing that comes back.**
    - **Who:** E; A for the `NameError`.
    - **What happened:** the given function (cell 107) reads `year_params` (Step 12) and `NAMES` (Step 13) from the notebook. A student who runs Step 15 after a restart, or skipped Step 12's typed dates, gets a `NameError` or a request with no dates; a 422 or 429 becomes `KeyError: 'properties'` three lines later. Step 15's Discuss names the missing error handling; it doesn't name the hidden inputs.
    - **Why it matters:** it is the one given cell a CS student copies into a project (E).
    - **Proposed fix:** lab key, cell 107: a comment line, "uses `year_params` and `NAMES` from Steps 12 and 13: run them first"; optionally `def get_daily(latitude, longitude, params=year_params)`. The Discuss's "what would you have to change" question can name it.
    - **Status:** verified by reading cell 107; #208's mistype table records the `KeyError: 'properties'`.

14. **A starter feed's site says, in its `robots.txt`, not to make datasets from it.**
    - **Who:** E; A, C and D built their exercise DataFrames from BBC feeds without remarking on it.
    - **What happened:** the feed host, `feeds.bbci.co.uk`, has no relevant `Disallow`. But `www.bbc.co.uk/robots.txt` opens with a comment that the BBC's terms mean "No scraping, crawling, or systematic extraction of content" and "No creating datasets from BBC content". BBC News is second in the chapter's and the handout's news list, and is the feed in their figure. The chapter flags only The Changelog; the handout lists The Changelog with no note.
    - **Why it matters:** Exercise Step 1 teaches students to check `robots.txt`; a student who reads the BBC's main site gets a terms signal the starter list doesn't mention. It is a judgment about terms of use, not a `Disallow`.
    - **Proposed fix:** the instructor's decision whether BBC stays on the list. Either way, `handouts/week-04/rss-feeds.md` (on #208's branch) could add a "`robots.txt`, checked on" column and The Changelog's note; the chapter's table likewise (textbook).
    - **Status:** verified: both BBC `robots.txt` files read on 2026-11-18; the handout and chapter tables as described.

15. **The weather half has no question behind it.**
    - **Who:** A, B. C and D, by contrast, found Step 14's grid-cell question the week's best (see "Disagreements").
    - **What happened:** Steps 9–15 are seven of sixteen steps about highs, lows and frost, with no person or decision in them. A, whose interest is online communities, couldn't tell whether "peel the onion" would help with a social-media API; B, a journalist, saw "a convenient API" with no policy question.
    - **Proposed fix:** lab key, Part 3's opening cell (81): one reporter's question (the growing season, the last spring frost for a Boulder County farm) (B); Step 16: a bullet, "name a source you might use for your project; is it XML or JSON, and what does it say about itself?" (A). No new code.
    - **Status:** reported; a judgment about motivation, not checkable.

16. **The grid-cell caveat is named but can't be sized.**
    - **Who:** C, D.
    - **What happened:** Step 14's Discuss says POWER's point sits about 150 m above the town in a grid cell tens of kilometres across; the key's Grand Junction cell is about 500 m above its town. Nothing gives a station's count to compare with Boulder's 115 freezing nights, and `PRECTOTCORR` is loaded and never looked at (C).
    - **Proposed fix:** lab key, Step 14's Discuss: one station's 2025 count for Boulder from NOAA, as a comparison (D); or a town-elevation column in Step 15's table (D). Optional.
    - **Status:** reported; the key's outputs (115, 1,801 m, 1,904 m) are verified, a station count is not.

### Corrections

Claims in the reviews that turned out wrong, out of date, or inexact, and what this document does with them:
- **"Cells the key tags `not-run-live`."** No cell of the key is tagged; the key's note says every cell ran live on 2026-11-17. The POWER blocks are the review's rule, not the key's flags, and are reported as such.
- **A: cell 14 is "the one typed cell with no code hint".** Inexact: cells 23, 45, 67 and 88 also name the task without the expression. Cell 14 is the first, and the one A tripped on (item 10).
- **B: Part 2 "nominal 59" and Part 3 "nominal 45" minutes.** The headings add to 51 and 35 (item 11).
- **B: "Print weather.shape, its rows and columns" asks for three things.** The key prints only `weather.shape`; the phrase describes what `shape` holds. The wording is still ambiguous for a minimal student, so it stays in item 10 as a rewording.
- **D: the lab is "Monday lecture, Wednesday and Friday labs".** The rebuilt lab is three parts, Monday to Friday; D's point, that the at-a-glance frame contradicts it, stands (item 8).
- **B and others: POWER's `robots.txt` "disallows AI clients".** More exactly: it disallows `/api/` for every user agent, and the whole site for six named AI crawlers. Item 3 uses the exact reading.
- **C: "`open-meteo.com/robots.txt` says `Allow: /`".** True, and kept as context; the exercise's request goes to `api.open-meteo.com`, which disallows everything.

## Disagreements

- **How much the typed cells should give away.** A wants more: cell 14's expression and cell 58's whole line spelled out. B, D and E want less: goal-only prompts in some cells, "no hint" repeats, answers to the Discuss boxes in the key. Both are right for their students. Spelling out the first cell of each new tool (A) and stating only the goal for its later repeats (D) would serve both; item 10 and item 7 are written that way.
- **Pace.** A, C, D and E rate pace 4, B 3, but A runs 20 to 40 percent over every part. D finishes Part 2 in 40 minutes, A in 75. The spread is in Part 2 (item 11), and Monday's 15 spare minutes are where the minimal personas' extra time would come from.
- **What the weather is for.** For A and B it is the half of the week with no people in it (item 15); for C and D it holds the week's best validity question, the grid cell (item 16). A question behind Part 3 would serve A and B without losing what C and D valued.
- **What to do at Exercise Step 5.** A, B, D and E stopped; C sent. A, B and D would accept either a stated course reading or a saved forecast; E would switch the exercise to a host that permits it. All five agree only that the materials must say something (item 3).
- **Difficulty.** A, B, C and E rate it 3, D 2 ("too easy to type"). The typed cells were fair for all five; the difficulty they report is in what the lab doesn't type: the exercise's loop and parallel lists (A), unnamed shapes and `NoneType` errors (B), dates and case (C), pandas masks (E).
- **Confidence.** All five rate it 3, each for a different reason: nested lists in an API and error handling (A); a host whose `robots.txt` disallows the API (B, D, E); a missing value or a date format not yet seen (C); missing fields on a messy source (E).

## Ratings

Each on a scale of 1 to 5. For difficulty, 5 is hardest for that persona's background.

| | A | B | C | D | E | Mean |
|---|---|---|---|---|---|---|
| Clarity of motivation | 3 | 3 | 4 | 4 | 4 | 3.6 |
| Pace | 4 | 3 | 4 | 4 | 4 | 3.8 |
| Difficulty for my background | 3 | 3 | 3 | 2 | 3 | 2.8 |
| How much I learned | 4 | 4 | 4 | 3 | 3 | 3.6 |
| Confidence I could do this on my project | 3 | 3 | 3 | 3 | 3 | 3.0 |

What holds motivation down: the weather half for A and B (item 15), the at-a-glance frame for C and D (item 8), and the take-home's host and feed choice for E (items 3 and 14). D and E learned least because the typing was transcription (item 7).

## Small things

Deck (`slides/week-04/week-04.tex`):
- One roster, four dates: "The roster in Chrome in September 2026" (the Step 2 frame), the chapter's figure "October 2026", the chapter's printed `publish-date` "September 2, 2026", and the checkpoint's November 3, 2026 (A).
- "After the lab: work these" numbers the Additional Exercises 3–5; the chapter numbers them 1–3, and the lab's Step 14 microsprint cites "Additional Exercise 3", which is the deck's item 5 (B).
- "A revision menu for Chapter 4" says "Open-Meteo dates roll forward"; Open-Meteo is the exercises' source now, not the lab's (A).

Lab (`labs/week-04/lab-04-key.ipynb`):
- Step 0: "`HEADERS` sends the book's User-Agent", but `CLIENT` holds a placeholder, which students replace in three setup cells (3, 40, 83); Steps 5 and 11 could say "the same address as Monday" (B).
- Step 1's Discuss: `small_soup.find("state").text` prints `'\nColorado\n'`, the full name between two line breaks; worth one line in the key (B, E).
- Step 2: "Open that address in Chrome first"; another browser shows the file differently (B).
- Step 3's Discuss: `soup.member-info` gives a `NameError`, not a syntax error; the question could say so (E).
- Step 3's microsprint Share asks how many names differ; the given cell prints positions, to count by eye (B; item 12).
- Step 3's given cell prints three top-level blocks, `title-info`, `members` and `committees`; the chapter names two blocks to ignore. The Friday box asks about it, so it is deliberate (A, B).
- Step 15: Leadville "at about 3,100 m"; its grid cell is 3,234 m in the key's table. Consistent with the lesson, but say "the town is at about 3,100 m, and its grid cell is higher" (A, B, C, E).
- The opening says "Nothing here is turned in", and Step 16 asks for written answers; "not graded" would be clearer (E).
- Leaving out `"xml"` prints `XMLParsedAsHTMLWarning` but still counts two members; Step 0 covers only the misspelled `"XML"` (E).
- Step 16's recap asks how "your place" compares, and the loop shows it only in the table (C).

Chapter and companion notebook (`ch-04-data-formats.qmd` at `3f9cf2c`):
- "Why 441 rather than 435? The file includes the six non-voting delegates and resident commissioner": the file has five delegates and one resident commissioner, six in all; "six non-voting members (five delegates and a resident commissioner)" is exact. Found while verifying item 1.
- The roster and Open-Meteo code send no User-Agent, while Exercise Step 1 asks for `HEADERS`; the lab's Friday box already asks this (A, C).
- "Without these checks, a single missing tag would crash your entire extraction loop": true, and the lab shows no crash, because the roster has no missing tag; item 2's feed is the case that shows it (A).
- The companion notebook's exercises follow the chapter's request cells, so "Run all" sends them (C; item 3).

Handout (`handouts/week-04/rss-feeds.md`, on #208's branch):
- It calls the BBC feed figure "The textbook's Figure 4.3" and the View Source figure "Figure 4.2"; in the chapter they are 4.4 and 4.3 (E).
- It lists The Changelog without the chapter's note that its `robots.txt` disallows all crawlers (E; item 14).

## Suggested next step

**Fix first, on #208's branch before it merges.** Each is small and changes none of what the week teaches:
1. **Item 1:** "29 of 50 states" (or the 56 explained) in Step 6's microsprint and its frame, and a given count of delegates in Step 4, so 441, 439 and 435 reconcile.
2. **Item 2:** Step 16's Exercise Step 4 bullet warns that feeds leave tags out and points at the chapter's guard; Step 6's Discuss runs `find("nosuchtag")`.
3. **Items 5 and 6, Step 13:** one `-999.0` in `two_days` with a before-and-after mean, and a given `two_lists` with a typed `pd.DataFrame(two_lists)`.
4. **Item 10 and item 12:** the five prompt rewordings (cells 14, 19, 45, 58, 95) and position 59.
5. **Merge order (item 9 and "Environment blocks"):** merge #208 before Wednesday's class, and check that `DATA` answers 200 from `main`; add "if this doesn't print 200, stop and tell me" to Steps 5 and 12.

**Needs the instructor's decision:**
- **NASA POWER** (items 3 and 4): whether class calls its `/api/`, which its `robots.txt` disallows for every user agent. If not, the three checkpoints of item 4 become the lab's data; if so, say why in Step 9's Discuss. The key's own runs from the cloud machine fall under the same decision.
- **A strict reading of `robots.txt` for API hosts** (item 3): whether Exercise Step 5's Open-Meteo request is in bounds. The answer goes in the lab, the deck and the chapter, or the exercise gets a saved forecast or another host (a textbook change).
- **BBC on the starter list** (item 14), given the terms comment in its main site's `robots.txt`.
- **"This week at a glance" and "Daily note questions"** (item 8): the instructor's frames; #208 proposes text.
- **Hints in typed cells** (item 7) and **Part 2's minutes** (item 11): how many cells state only the goal, and what moves to Monday or becomes given.
- **A question behind the weather** (item 15): a sentence in Part 3's opening, or nothing.
