# Review: week 08, Dynamic Web Pages with Selenium

**What was reviewed:** week 8's lab (`labs/week-08/lab-08.ipynb`, with its key and the checkpoints in `labs/week-08/data/`), its deck (`slides/week-08/week-08.tex`), the setup handout (`handouts/week-08/README.md`) and chapter 8's Recommended Exercises, as students meet them.
- **Course repository:** the head of pull request #203, `2cbbad7f1f3fadd46896e2b35d8a5748f6c81f46`, which rebuilt week 8's lab and deck in the incremental style, for the next offering: three parts, a small first call before each workflow, and one deck frame per typed cell. #203 is open and not merged, so every lab and deck fix below names a file on that branch and can be made there before merging.
- **Textbook:** `ch-08-dynamic-pages.qmd` and its companion notebook at `3f9cf2cef801181236c9cceaf71f3b63c3ad2491`, the textbook's `main`.

**When:** 2026-11-17 and 18.

**Method:** five anonymous composite personas, each a kind of student this course has, reviewed the week independently. Each read the chapter and the slides, typed and ran its own code for every lab step it could from the students' copy, made the mistakes its background makes, attempted the Recommended Exercises, and opened the key only after an honest try. Each review is a **steel man**: it first makes the strongest case for the materials as designed, and only then says where they fall short for that student. Reviewers were told to respect `robots.txt`. This document puts the five together. Every ranked finding was then checked against the repository and the textbook, and is marked **verified** (with how) or **reported, not verified**.

## Who reviewed

| | Degree and major | Python and data background | Interest | Skill |
|---|---|---|---|---|
| A | BS senior, Information Science | One intro Python course; spreadsheets | Qualitative and design: online communities, UX | Minimal |
| B | BA junior, Journalism and Communication | No Python before this course; strong with public records and Excel | Data journalism, local government | Minimal |
| C | BS senior, Business Analytics | Excel, some SQL, a little pandas | Quantitative analytics: markets, customer data, dashboards | Minimal to moderate |
| D | MS first year, Data Science (BA in Statistics) | Fluent in R, moderate pandas; regression and sampling | Quantitative: measurement and validity | Moderate |
| E | MS first year, Information Science (BS in Computer Science) | Moderate Python, git; little data analysis | Design and tools: automation, APIs, building things | Moderate |

## What each completed

The lab has Steps 0–13 and seven microsprints: Part 1 (Monday) is Steps 0–3, Part 2 (Wednesday) Steps 4–8, Part 3 (Friday) Steps 9–13, then the 15-minute revision block. Every persona ran Part 3 from a local copy of the checkpoints, because their address on `main` doesn't exist yet (see "Environment blocks").

| | Lab steps finished | Read, not done | Recommended Exercises | Needed the key for |
|---|---|---|---|---|
| A | 0–12, all microsprints; Step 13 and Step 11's paper microsprint as comments | Step 7's Wikipedia cells (60, 61, 64), for `robots.txt` | Steps 1–6, on `quotes.toscrape.com/scroll`, after two real sites refused | Nothing; compared afterwards |
| B | 0–12, microsprints but Step 11's | Step 7's Wikipedia cells (60, 61, 64), for `robots.txt`; Step 13; Step 11's paper microsprint | Steps 1–5 on `/scroll`, after a local-government site refused; Step 6 not written | Nothing; compared afterwards |
| C | 0–12, all microsprints; Step 7's search only on exact titles | Step 13 (answered in the review, not the cell) | Steps 1–5 on `/scroll`; Step 6 drafted | Nothing |
| D | 0–12, all microsprints, Wikipedia as written | Step 13, partly; `getpass()` (a literal password instead) | Steps 1–6 on `/scroll` | Nothing; compared afterwards |
| E | 0–13, all microsprints, Wikipedia as written; Step 13 and Step 11's paper microsprint as comments | none | Steps 1–6 on another practice site's infinite scroll | Nothing; compared afterwards |

**Estimated time for a real student of that background, in minutes** (the lab's own step and microsprint minutes, and the day's, in the last rows):

| | Part 1 | Part 2 | Part 3 | Exercises |
|---|---|---|---|---|
| A | 60 | 70 | 55 | 90 |
| B | 75 | 80 | 70 (Step 12 alone 20) | 90 |
| C | 70 | 75 | 55 | 90 |
| D | 40 | 55 | 50 | 45, plus 20–30 for the reading and the handout |
| E | 60 | 80 | 75, plus the 320 MB download | 90 |
| **The lab** | **57** (50 in steps, 7 in microsprints) | **62** (50 in steps, 12 in microsprints) | **44** (36 in steps, 8 in microsprints) | none given |
| **The day** | **50** | **50** | **35**, then the 15-minute block | due Sunday |

## Environment blocks

These come from the review machine or from merge order, not from the materials. They are kept apart so that none is read as a flaw in the week.

- **Part 3's checkpoints aren't on `main` yet (all five).** Step 9's setup cell (78) and the commented fallbacks in Steps 3 and 10 (cells 28 and 90) read `api_quotes.csv` and `scroll-page.html` from `raw.githubusercontent.com/.../main/labs/week-08/data/`. That folder exists only on #203's branch, so the address answers 404 until #203 merges. All five loaded the files from the branch instead. This is a merge-order item, listed under "Suggested next step"; what the cell does when a read fails is a separate design point (item 4).
- **Chrome needed `--no-sandbox` (all five),** because the review machine runs as root. The key's `LAB_CHROME_FLAGS` cell handles it, as the key note says. On a laptop it does nothing.
- **A stray `chromedriver` 147 on the machine's `PATH`,** against Chrome 153. With the lab's Step 4 settings it was ignored; without them (C and E in the exercises, D once in Part 2) Chrome wouldn't start. The error is the chapter's documented one; that the exercises don't set it is item 11.
- **Playwright's browsers were already installed,** so no persona could time the 320 MB download or see what Step 12 does without it (A, C, E).
- **No one could type into `getpass()`.** A and C set `QUOTES_PASSWORD`, which the cell reads first; D typed a literal password.
- **Wikipedia.** A and B sent nothing to Wikipedia's search, and C only exact titles, because of its `robots.txt` (item 1, a finding, not a block). C, D and E got no 429s. A reports 429s from Wikipedia on this machine; A sent no search, so this isn't verified.
- **Sites tried for the exercises.** One social site's `robots.txt` disallows everything (A), another answered a plain request with a 403 bot-challenge page, which may be specific to the machine's address range (A), and a local-government calendar answered a 200 with a 19-character error message (B). No persona worked around any of them. What the exercises say about this is item 6.
- **The key has no `not-run-live` cells.** Every cell ran live for the key on 2026-11-17, including the Wikipedia ones, so no persona had to read a saved output in place of a request.

## The strongest case for the week as designed

**Every workflow starts with a call whose answer the student can predict and check.** All five said so first. Step 1 asks for a prediction ("Week 6 counted 10 `div.quote`… predict this page's count") and then prints 0; A "had to explain that to myself before the lesson told me", and to D it is "a small, falsifiable prediction, and the surprise is the lesson". Step 5 loads the plain page and prints `driver.title` and the `<h1>`, which the student can read off a browser tab, before it loads `/js/`. D called this "calibrate the instrument on a known quantity first"; A trusted the browser's count "because I had just watched it get the easy page right". Step 2 goes down the JSON one level a cell, then page 2, then (Step 3) page 11, before any loop, so when the given `get_all_quotes()` arrives, A, B, C, D and E could each find their own Step 2 request inside it, as its comment asks.

**The split between typed and given cells fits the students with the least Python.** Every typed cell was one to four lines, and no persona needed the key to finish one. The regex (cell 8), the loop (24), the comprehension (26), the scroll loop (87) and the `%%writefile` scripts are given, each with a comment saying what it does; B, who had no Python before this course, "never had to write a `for` loop or a function". The slips the minimal personas made (`header=` for `headers=`, `.json` without parentheses, `"tag"` for `"tags"`, a stale element after a click) each produced a short traceback whose last line named the fix (A, B). E found the given cells hide "only boilerplate and syntax I'd otherwise copy blindly", not the ideas.

**The order is the argument, and the numbers carry it.** The week asks "do you need a browser?" and runs three free checks before any browser starts (B, C, D, E). The hidden API returns 100 quotes in about 13 seconds; the scrolled page holds the same 100; and the Step 10 microsprint prints `100 0 0`. A believed it "because I had made both tables"; D called it "a cross-validation of two collection routes, which I'd do anyway". C, who will be asked "why not just use the API?", found that honest. Step 8's ten-second page makes the case for waits with one number, 10.3 seconds, which every persona reproduced.

**The silent failures are shown with a number attached.** Page 11 answers 200 with an empty list; `"Page": 2` returns page 1; `"Humor"` returns nothing; `.//a` against `//a` gives 5 against 47; the transcript's `.text` is `''` while `textContent` holds it. D checked the first three and found them as described, and called the `.text`/`textContent` pair a validity lesson: "what a reader sees versus what the page contains". C trusts a lab more "when it shows me a silent failure with a number attached".

**The Discuss boxes keep the people in view, and the checkpoints keep Friday alive.** A and B, the personas who look for who is on the other end, singled out who the site thinks is visiting when Chrome drives (Step 4), what logging in changes "for the people whose posts you'd see" (Step 11), and the paper microsprint on who carries the risk; B called them "the ethics and records questions I care about, tied to actual lines of code". The saved `api_quotes.csv` and `scroll-page.html`, and each part's own setup step, mean a failed Monday doesn't sink Friday (A, B, C, D, E).

## Where it falls short, ranked

No persona found a privacy problem: nothing in the week prints personal contact details, and Step 11 prints cookie names, never values. The wrong-result problems come first. After them, items are ranked by how many personas hit each, how badly, and whether it stopped A or B. Cell numbers are positions in `labs/week-08/lab-08-key.ipynb` at `2cbbad7f`, counted from 0; the students' copy has the same numbering and is made from the key by `labs/tools/make_student_copy.py`.

1. **Step 7 says "Wikipedia welcomes automated access", and its search sends the browser to pages Wikipedia's `robots.txt` disallows.**
   - **Who:** A, B, C found it and held back; D and E ran the cells as written; E also found the microsprint's likely queries never reach a results page.
   - **What happened:** Step 7's text (cell 56), the deck frame "Step 7: find the box" and the chapter ("Typing and Searching": "Wikipedia's robots policy is permissive toward automated access") all say automated access is fine. Wikipedia's `robots.txt`, for `User-agent: *`, says `Disallow: /w/` and `Disallow: /wiki/Special:`. The portal's search form sends the query to `www.wikipedia.org/search-redirect.php`, which redirects to `en.wikipedia.org/wiki/Special:Search?search=...`; from there a vague query lands on a results page (the key's microsprint, cell 64, saved "headless browser scraping - Search results - Wikipedia | 9 results"), and an exact title on its article. So every search, the typed "Colorado Buffaloes" of cell 61 included, passes through a disallowed path. The next Discuss question (cell 65) asks whether `robots.txt` still applies "when a real browser does the requesting"; the chapter's "Automation Is Not a Loophole" says it does. Separately, E's first two queries of its own were article titles, so E saw "0 results" twice and no results page; the microsprint depends on seeing both.
   - **Why it matters:** B is "the student most likely to take the robots.txt lesson seriously", and would either stop with no explanation or conclude the instructions weren't checked. A: "it sets the opposite example from week 2". A student who doesn't check takes away the lab's sentence.
   - **Proposed fix:** the instructor has an open decision, raised on #212 (whose `robots.txt` table lists `en.wikipedia.org`'s `/w/` rule), on how strictly to read Wikipedia's `robots.txt`; this item needs it. The options the personas and this check found:
     - **Keep Wikipedia, and make the contradiction the lesson.** Lab key cell 56 and the deck's "Step 7: find the box": replace "Wikipedia welcomes automated access" with what the file says ("Wikipedia's `robots.txt` asks automated clients to stay out of `/w/` and `Special:` pages, which is where its search goes; its API is the route it offers"), and have students read the two lines before cell 60. Chapter: the same correction to the "Typing and Searching" sentence.
     - **Move the typing example to a page that allows it.** `www.scrapethissite.com/pages/forms/` has a plain search box (`name="q"`), and its `robots.txt` disallows only `/lessons/` and `/faq/`; Step 11 already types into the sandbox's login form. This changes cells 60–64, their frames, and the chapter's example.
     - "Use exact titles only" (A, B, C) doesn't fix it: an exact title passes through `Special:Search` too.
     - Whichever is chosen, the microsprint (cell 63) should name a vague query and an exact title, so students see both outcomes (E).
   - **Status:** verified: the two `Disallow` lines in `en.wikipedia.org/robots.txt` (read 2026-11-18; `www.wikipedia.org/robots.txt` redirects to it); the portal form's `action`; one request to `search-redirect.php`, not followed, which answered 302 to `/wiki/Special:Search?search=Colorado+Buffaloes&go=Go`; cells 56, 61, 64 and 65; the deck frame; the chapter's sentence at `3f9cf2c`. The results page's own address is the personas' report; no search was sent to check it.

2. **The key's saved output for Step 5's central cell is 0, where the step needs 10.**
   - **Who:** A, E.
   - **What happened:** cell 43 loads `/js/` and counts `div.quote` right after `driver.get()`. Its saved output is `0`. A got 10 on five fresh browsers, E on seven. The Discuss question (cell 45) asks "Why did one find quotes and the other none?", which assumes 10, and #203's own description says "predict 10". `driver.get()` returns at the page's load event and the quotes are built by a script, so a 0 is possible on a slow or cold start; Step 8's wait comes three steps later.
   - **Why it matters:** the instructor shows the key. A student who sees 0 on the screen, or gets 0 on a slow laptop, concludes Selenium fails the way `requests` did, the opposite of the lesson (E). A: "I would think my code was wrong."
   - **Proposed fix:** lab key, cell 43: rerun it and keep the saved 10, then regenerate the students' copy and the PDF. Add one sentence to Step 5's text (cell 39): "If it prints 0, run the cell again; Step 8 explains why." Or use Step 8's wait here, which moves `quote_locator` earlier.
   - **Status:** verified: the saved `0` in cell 43, and cell 45's question. Why the key got 0 (a race or an output left from an earlier version) is not known.

3. **The deck's "at a glance", "Before Wednesday" and Wednesday "Lab" frames describe the old week, and point to the wrong exercises.**
   - **Who:** A, C, D.
   - **What happened:**
     - "This week at a glance" says Monday "Concepts & notebook intro", Wednesday "Notebook lab: … xkcd, a Wikipedia search, and the Quotes to Scrape sandbox", Friday "Clearing the backlog", and "bring a laptop" Monday and Wednesday. The lab and the deck's own "Today: Part 2" and "Today: Part 3" frames describe three live-coding parts.
     - "Before Wednesday" says "Wednesday lab: Complete Recommended Exercises … upload to Canvas by Sunday".
     - "Lab: work these, then show-and-tell" lists the chapter's *Additional* Exercises 1–5 and the 5617 memo, numbered "6." (the chapter's 7; its 6, the login on paper, is left out), and says "Graded on good-faith attempt".
     - Monday still carries about 20 concept frames (Selenium Manager, headless mode, Playwright, logging in) after Part 1's lab frames (D).
   - **Why it matters:** a student who plans from the slides does the wrong list of exercises, and the Recommended ones are the grade (A, C). D "can't tell which of those is current".
   - **Proposed fix:** deck: rewrite "at a glance" from the lab's opening cell, one `\dayband` per part, and a laptop all three days; in "Before Wednesday", say the Recommended Exercises are in the companion notebook, after all three parts, due Sunday; retitle "Lab: work these" as optional extensions with the chapter's numbering, or remove it. #203 already proposed the "at a glance" edit and left it, and the move of Monday's concept frames, to the instructor, because they are the instructor's frames.
   - **Status:** verified: the three frames in `week-08.tex` at `2cbbad7f`; the chapter's Additional Exercises list; #203's "Your frames" section.

4. **Step 9's setup cell defines `quote_locator` after the line that loads Monday's table, so one failed read becomes NameErrors in Steps 10 and 11.**
   - **Who:** E; A, B, C and D hit the same 404 and went to a local copy before running on.
   - **What happened:** cell 78 sets `data_base`, runs `api_quotes = pd.read_csv(data_base + "api_quotes.csv")`, and only then `quote_locator = (By.CLASS_NAME, "quote")`. When the read raised `HTTPError: HTTP Error 404: Not Found`, `quote_locator` was never set, so cell 84 (Step 10's wait) and cell 100 (Step 11's) raised `NameError: name 'quote_locator' is not defined`, and the microsprint (cell 94) failed on `api_quotes`. The error a student sees in Step 10 is about a locator, not a file.
   - **Why it matters:** the checkpoint exists so Friday doesn't depend on Monday; as written, Friday depends on one download, and a network blip, a firewall or an offline laptop breaks Steps 10 and 11 as well (E). A minimal student won't look back at the first red cell.
   - **Proposed fix:** lab key, cell 78: move `quote_locator = ...` above `data_base`, or put the two `api_quotes` lines in a given cell of their own, with a comment: "A 404 here means the file isn't published yet: say so in class, and go on; only the microsprint needs it." (A `try`/`except` fallback, which C and D suggest, is ruled out in lab cells by `labs/AUTHORING.md`, "No error handling".) The deck's "Step 9: set up again" needs no change.
   - **Status:** verified: the order of lines in cell 78; `quote_locator` used in cells 84 and 100, `api_quotes` in 94; `git ls-tree origin/main labs/week-08/` lists no `data/`.

5. **Step 13 asks how many requests and seconds the scroll took, and Step 10 never measures either.**
   - **Who:** A, C, D.
   - **What happened:** Step 13's first bullet (cell 113): "How many requests and seconds did the API take, against the scroll's in Step 10?" The API's are printed (Step 3, 13.4 s; 10 pages). Step 10's given loop (cell 87) prints only "Stopped after scroll 9 at 15911 pixels". The key's own answer (cell 114) infers "at least 20 s" from the sleeps. C adds that both times are mostly the loops' own pauses (1 s a page, 2 s a scroll).
   - **Why it matters:** it is the comparison the week is about (D). A would have written "not sure"; D would be comparing "13.1 s measured with about 18 s inferred".
   - **Proposed fix:** lab key, cell 87 (given): `start = time.time()` before the loop, and `scroll_seconds = round(time.time() - start, 1)` printed with the scroll count. Cell 113: "both include their pauses". The deck's "Step 10: to the end, given" describes the loop in words and needs one more clause.
   - **Status:** verified: cells 25, 87, 113 and 114.

6. **The Recommended Exercises ask students to choose a JavaScript-heavy site, and the real sites they chose refused them.**
   - **Who:** A, B, C; D and E chose practice sites from the start.
   - **What happened:** Exercise Step 1 says "Choose a JavaScript-heavy site — a news site's live section, a social feed". A's first choice disallows everything in `robots.txt`; the second answered a bot-challenge page. B's local-government calendar answered 200 with a 19-character error message, and nothing told B whether that was a refusal or an empty page; the only fix B could think of was the spoofing week 5 warned against. C found a market-data site's terms restrictive. All three fell back to the sandbox's `/scroll`, which makes Steps 1–5 a repeat of Step 10 and answers Step 6 in advance (A, C). A also notes the lab never has students find a selector on a page whose answer they weren't told.
   - **Why it matters:** the exercises are the graded part. A: "The sites a UX or communities student would think of first are the ones that refuse." Confidence on a project is 3 for A, B and C, and each names this.
   - **Proposed fix:** chapter and companion notebook, Exercise Step 1: a short list of vetted sites that are JavaScript-heavy and allow a polite fetch (E used a second practice site's infinite scroll; C suggests `scrapethissite.com`'s AJAX page, whose `robots.txt` blocks only `/lessons/` and `/faq/`); one sentence that a refusal (`robots.txt`, a 403, a challenge page, a 200 with a few characters) is a finding to report in Step 6, not something to get around; and "print `len(response.text)` and its first 200 characters" (B). Optional, lab: one microsprint where students find a selector themselves with the Inspector (A).
   - **Status:** the exercise's text verified at `3f9cf2c`; no vetted list exists. What each site answered is reported, not verified.

7. **The exercises ask for measurements the lab never practises.**
   - **Who:** A, C, D.
   - **What happened:** Exercise Steps 1, 3 and 5 ask for `len(response.text)`, `len(driver.page_source)` and a DataFrame of "HTML length" and "element count" per stage; no lab cell prints a length (D). Step 1 says to check `robots.txt` first; no lab cell fetches one (D). Step 6 asks about "the speed difference you experienced", and Steps 1–5 never ask to time anything on the student's site (A, C); the lab's "Recommended Exercises ahead" points Step 6 to Step 8's timings, which were on the sandbox. Step 6's "how much of the page did the static request miss?" has two answers when the static count is 0 (D: 100% of the quotes, 92% of the characters).
   - **Why it matters:** A, with minimal Python, "won't go back and add timing code", and would write about speed from memory. A grader would see a table that doesn't support the paragraph.
   - **Proposed fix:** chapter, Exercise Steps 1–5: record `time.time()` around each fetch, and add a `seconds` column to Step 5's DataFrame; Step 6: "report the share of elements missed". Lab key: one typed line printing `len(js_response.text)` in Step 1 (cell 6 or 7) and `len(driver.page_source)` in Step 10 (cell 88), so both have been seen once (D).
   - **Status:** verified: the exercises' text; no `len(` of a page's text in the key, and no `robots.txt` request.

8. **Parts 2 and 3 don't fit their days by the lab's own minutes.**
   - **Who:** A, B, C, D, E. A, B, C and D rate pace 3; E 4.
   - **What happened:** Part 1's headings add to 57 minutes against Monday's 50, Part 2's to 62 against Wednesday's 50, and Part 3's to 44 against Friday's 35, before any Discuss box. A, B and C put Part 2 at 70–80 minutes; B and E put Part 3 at 70–75, with the Playwright install still to do. A took about 25 minutes for Step 6's 13 (item 15). D: "a student with little Python typing along will not finish Step 12".
   - **Why it matters:** Step 12 is the last step, and the Friday block follows it. The day that runs over is the one with the 15-minute revision block.
   - **Proposed fix:** the instructor's decision. The personas' candidates: say on Friday's "Today" frame and in Step 12 (cell 105) that its second and third scripts may be read together and run once (B, D); move Step 6's transcript pair (cells 51–52) to Step 7, or split Step 6 across Wednesday (A); mark one microsprint a part "if time".
   - **Status:** verified: the step and microsprint minutes in the key; `docs/course-facts.md` gives about 50, 50 and 35 minutes. The persona estimates are their own.

9. **Step 12 says Playwright's locators wait, and the one call students make, `count()`, doesn't.**
   - **Who:** B, E.
   - **What happened:** Step 12 (cell 105) says locators "wait on their own when you act on or read an element". `js_pw.py` prints 10 only because `/js/` renders at load. Pointed at `/js-delayed/`, the same `count()` printed 0, while `.first.inner_text()` waited and returned a name (B, E). The deck's "Step 12: your script" asks "Does `count()` wait?" with no answer in the lab; the first Discuss question (cell 112) asks which Selenium lines "the script did not need". The chapter ("Locators Wait for You") and Monday's deck frame "Locators wait for you" do show `count()` returning 0.
   - **Why it matters:** it is the same silent zero as Step 8's, in the one place a student takes the new library at its word. E would "put `count()` in a loop and trust it".
   - **Proposed fix:** lab key, cell 105: one sentence, "`count()` reports the page as it stands, and doesn't wait"; cell 112: "Run `js_pw.py` on `/js-delayed/`: why 0?" The deck frame can then answer its question.
   - **Status:** verified by reading cells 105, 108 and 112, the deck frames and the chapter. The 0 on `/js-delayed/` is the personas' run and the chapter's.

10. **Playwright's install isn't in the setup handout's environment, and nothing checks it before Step 12.**
    - **Who:** A, E; D notes the download.
    - **What happened:** the lab's opening (cell 0) says to use "`webdata`, or Anaconda's own". The handout says "You don't need the course's `webdata` environment" and installs only `selenium` and `selenium-manager`. End of Part 2 (cell 75) and the deck's "Before Friday: Playwright's browsers" say to run `python -m playwright install chromium` "with `webdata` active". In Anaconda's own environment the library isn't there, so the command can't work (A). A student who skipped the install finds out at cell 107, Step 12's first run, with the error the chapter lists under Common Issues (E).
    - **Why it matters:** it lands at the last step of the week, when time is shortest. A followed the handout's word that `webdata` wasn't needed.
    - **Proposed fix:** `handouts/week-08/README.md`: add `playwright-python` to the install line, or say that Step 12 needs it. Lab key, cell 75, and the deck's "Before Friday": "Skipped `webdata`? First run `%conda install -c conda-forge playwright-python`." Optional: a given cell in Step 9 that launches Playwright's Chromium and closes it, so the failure shows at the start of Friday (E).
    - **Status:** verified: the handout's text and install line (unchanged by #203), cells 0 and 75, the deck frame. What the command prints in Anaconda's own environment is reported, not tested.

11. **The companion notebook's exercises start with no setup cell.**
    - **Who:** C, E.
    - **What happened:** Exercise Step 2 says "Set up a headless Selenium driver following the chapter's setup code". In the companion notebook, `SE_SKIP_DRIVER_IN_PATH` is set in cell 16, 61 cells before the exercises (cell 77). After a restart, C and E started at the exercises and got `SessionNotCreatedException: This version of ChromeDriver only supports Chrome version 147`. The stray driver was the review machine's, but the chapter's Common Issues names Homebrew, conda and npm as places students get one.
    - **Why it matters:** the exercises are done at home, after the lab's notebook is closed, and they are the graded part. E recovered in five minutes from the Common Issues list; a minimal student wouldn't.
    - **Proposed fix:** companion notebook (textbook): one given cell above Exercise Step 1 with the imports, `HEADERS`, and the two `os.environ[...]` lines of "Before the First Browser", step 1.
    - **Status:** verified: the companion notebook at `3f9cf2c`, cells 16 and 77 onward.

12. **"Copy the rest of `hello_pw.py`'s cell" leads a minimal student to paste a second `%%writefile` line.**
    - **Who:** A.
    - **What happened:** cell 108 starts `%%writefile js_pw.py` and says "Copy the rest of hello_pw.py's cell here"; the deck's "Step 12: your script" says "Copy `hello_pw.py`'s cell". Copying the whole cell pastes `%%writefile hello_pw.py` into the script, and running it gives `SyntaxError: invalid syntax` on that line.
    - **Why it matters:** it is the last typed cell of the week, and the traceback points at a line the student didn't think of as code.
    - **Proposed fix:** lab key, cell 108, and the deck frame: "Copy everything after its first line".
    - **Status:** verified by reading cell 108 and the frame; the `SyntaxError` is A's run.

13. **Step 10's numbers differ from the key's, and the loop's message doesn't say whether it finished.**
    - **Who:** B, C; D on the set check.
    - **What happened:** after one scroll by hand (cell 86) the key saved 20 quotes and 3,554 pixels; B and C got 30 and 5,118. The loop (cell 87) stopped after scroll 9 in the key and A's and D's runs, after 8 in B's and C's. It stops when the height is unchanged after 2 seconds and prints "Stopped after scroll N" whether it broke or hit the cap of 20 (C). The final 100 is stable; nothing in the step says so, or what to do with fewer. D adds that the set microsprint (cell 94) compares texts as sets, so duplicates would hide; here `api_quotes` has 100 rows and 100 texts.
    - **Why it matters:** a student comparing screens thinks they did something wrong (B). On a slow connection the loop could stop early with fewer than 100 and say nothing (C).
    - **Proposed fix:** lab key, Step 10's text (cell 82): "How many quotes one scroll shows depends on timing; the API said 10 pages, so expect 100." Microsprint (cell 94): also print `len(scroll_quotes), len(api_quotes)` (D).
    - **Status:** verified: cells 86, 87 and 94, the key's saved outputs. The personas' counts are their runs.

14. **The slides show the full code for every typed cell, and some prompts give it verbatim.**
    - **Who:** A, E; C on the prompts.
    - **What happened:** each Step frame shows the cell's code, down to the microsprint's tag (`get_all_quotes(tag="humor")`) and the whole `js_pw.py`. Some prompts state the code (cells 40, 68, 72: "`WebDriverWait(driver, 15).until(...)`"), so C finished Part 2 without understanding the tuple, and first wrote a wait in the exercises.
    - **Why it matters:** the predict-first prompts are "one slide-flip away from being answered" (A). A also used the slides when stuck, and C calls the prompts a feature for minimal students.
    - **Proposed fix:** the instructor's decision; the one-frame-per-cell deck is the incremental-style plan's design. Candidates: keep the predict-first frames (Step 1's count, Step 5's `/js/` count) code-free until the room has answered (A, E); in Step 8 (cell 72) and Step 10 (cell 84), name what to do, not the code (C).
    - **Status:** verified: the deck frames and cells 40, 68, 72.

15. **Step 6 asks for four new ideas in a row.**
    - **Who:** A; B on the dot trap.
    - **What happened:** after two typed counts, a given cell shows link text, partial link text and an XPath parent at once (cell 49), then `.//a` against `//a` (50), then `repr()` of an empty string (51), then `get_attribute("textContent")` (52), then a three-locator microsprint. A took about 25 minutes for 13 plus 4, and understood the dot trap only from the Discuss box.
    - **Why it matters:** it is the densest step of Part 2, the part that runs most over (item 8).
    - **Proposed fix:** lab key: move the transcript pair (cells 51–52) to the start of Step 7, whose first cell already loads xkcd.
    - **Status:** verified: cells 46–54. The minutes are A's.

16. **The given API loop has no `raise_for_status()`, and its comment doesn't say so.**
    - **Who:** D, E.
    - **What happened:** `get_all_quotes()` (cell 24) has no status check; the chapter's loop has `response.raise_for_status()  # Stop on an error status rather than parse an error page`. A 429 would surface as a `KeyError` or `JSONDecodeError` far from its cause. The Discuss box (cell 31) asks what would break.
    - **Why it matters:** D and E would copy this loop into a project.
    - **Proposed fix:** lab key, cell 24's comment: "No error handling here: a 429 ends in a KeyError. The chapter's loop adds `raise_for_status()`." Adding the line itself, as D proposes, is ruled out by `labs/AUTHORING.md` ("No error handling").
    - **Status:** verified: cell 24, the chapter's loop, and the rule.

17. **The interpretation questions have no sample answer or definitions.**
    - **Who:** B; D on Step 6's ratio (item 7).
    - **What happened:** Exercise Step 6 asks for "static, partially dynamic, or fully dynamic"; "partially dynamic" appears in the chapter only in the exercises. Step 13 is four open questions in three minutes, answered as comments.
    - **Why it matters:** B, the student least practised at writing prose in a code cell, had numbers and no labels to put on them.
    - **Proposed fix:** chapter, Exercise Step 6: one sentence for each label. Lab key, cell 113: a one-line sample answer for the first bullet.
    - **Status:** verified: the chapter's uses of "partially dynamic".

18. **The timing comparisons are single runs.**
    - **Who:** C.
    - **What happened:** the Step 8 microsprint times `requests.get()` and the open browser once each (0.19 s against 0.13 s in the key), and the Discuss box explains the order. The first request pays for DNS and TLS. Exercise Step 6 then leans on "the speed difference you experienced".
    - **Proposed fix:** lab key, cell 74: one Discuss line, "One run each: would the order hold over five?"
    - **Status:** reported; a judgment about method.

### Corrections

Claims in the reviews, or in the notes this review started from, that turned out wrong, out of date, or inexact:
- **An exact-title search avoids the disallowed path (A, B, C).** It doesn't: the portal's form goes through `/wiki/Special:Search` before it redirects to the article. So C, who searched only exact titles to stay within the rules, sent three requests through it, and cell 61's typed "Colorado Buffaloes" does the same. Item 1 drops "exact titles only" as a fix.
- **C sent nothing to Wikipedia.** C did send exact-title searches (above); A and B sent none.
- **The lab's minutes (A, B).** A gives the lab's figure for Part 3 as about 50, B as 35. The headings say 36 in steps and 8 in microsprints, 44 in all, against Friday's 35 (item 8).
- **"No step asks me to time anything" (A).** The lab's "Recommended Exercises ahead" points Exercise Step 6 to Step 8's timings. The gap that stands is that the exercises' own Steps 1–5 don't time the student's site (item 7).
- **"The lab implies Playwright never needs a wait" (B).** Monday's deck frame "Locators wait for you" shows `count()` returning 0, as the chapter does. The lab's Step 12 is what leaves it out (item 9).
- **`raise_for_status()` in the given loop (D), `try`/`except` in Step 9's setup (C, D).** `labs/AUTHORING.md` rules both out of lab cells; items 4 and 16 propose a reorder and a comment instead.
- **"The lab intro says the key is for after an honest attempt" (D).** It doesn't; that was the reviewers' own instruction. The deck's "Fall behind? Copy the cell from the key" stands unopposed. Dropped.
- **A's Wikipedia 429s.** C, D and E got none; A sent no search. Kept under "Environment blocks" as unverified.

## Disagreements

- **Too slow or about right.** A, B and C put Parts 1 and 2 at 60–80 minutes each and rate pace 3; D put Part 1 at 40 and calls it "comfortable", and E rates pace 4, "each step fits its allotted minutes for the typed part". All five agree that Friday, with Step 12 and the install, is the squeeze. That suggests the minutes to find are in Part 2's Step 6 and Part 3's Step 12, not across the board (item 8).
- **Code on the slides.** A and E would hold the code back until the room has tried; A also used the slides to get unstuck, and B found their "common slip" notes enough. C, from the other side, wants two prompts to stop giving the code. The minimal personas need the code nearby; the moderate ones want to be made to write it once (item 14).
- **Where the exercises should happen.** A, B and C tried real sites, were refused, and fell back to the sandbox; D went straight to the sandbox and finished in 45 minutes; E chose another practice site and found a real difference (its `page_source` longer than the static HTML, unlike the chapter's warning). A sandbox makes the exercise a repeat of the lab; a real site is where the minimal personas get stuck. A short vetted list is the middle (item 6).
- **Wikipedia.** A, B and C stopped at `robots.txt`; D and E read the same week-2 lesson and ran the cells, since the lab says Wikipedia welcomes it. Students will split the same way unless the materials decide for them (item 1).
- **Difficulty.** A, B and C rate it 3, D and E 2. The typed cells were fair for all five; what A and B call hard is the vocabulary of one week (locator, XPath, tuple, explicit wait, `execute_script`, a script run as a separate program), and the long Selenium tracebacks. E would have liked a harder stretch cell.

## Ratings

Each on a scale of 1 to 5. For difficulty, 5 is hardest for that persona's background.

| | A | B | C | D | E | Mean |
|---|---|---|---|---|---|---|
| Clarity of motivation | 4 | 5 | 5 | 4 | 4 | 4.4 |
| Pace | 3 | 3 | 3 | 3 | 4 | 3.2 |
| Difficulty for my background | 3 | 3 | 3 | 2 | 2 | 2.6 |
| How much I learned | 4 | 4 | 4 | 4 | 4 | 4.0 |
| Confidence I could do this on my project | 3 | 3 | 3 | 4 | 4 | 3.4 |

What holds the confidence down: A, B and C each tried a real site for the exercises and were refused, and nothing says what to do next (item 6); B and C also name the Wikipedia contradiction (item 1), and C doesn't know how to check a `robots.txt` rule against a path. D and E would want error handling (`raise_for_status()`, `try`/`finally` around `quit()`) before a long run, which the lab leaves to the chapter by design (item 16).

## Small things

Lab (`labs/week-08/lab-08-key.ipynb`):
- Opening cell: "so that Chrome opened from chapter 8's notebook" is missing a word ("so that Chrome has opened", B). It also says Cells "that start with `# Given:`" are given, but the three `%%writefile` cells have it on their second line (B).
- Opening cell says to finish the handout "before class" and that Monday needs no browser; the handout's subtitle says "before Wednesday's lab", as does the deck's "Before Wednesday" (A). Pick one.
- Step 1's microsprint (cell 10): both answers are `False` and nothing says "Step 2 is where to look" (A).
- Step 2, cells 16 and 18: "look at its keys" lets a student type the whole object and get a wall of JSON; "print its keys" (D). Cell 19: quote both key names in the prompt; B typed `"tag"` (B).
- Step 3's link text "Write the scraper" points to `#check-3-watch-the-network-tab`; it lands on the right section, where "Write the scraper" is a bold paragraph, not a heading. The Discuss box (cell 31) could name `response.raise_for_status()` (A, B, E).
- Step 5, cell 44: `Image(filename="quotes-headless.png", width=640)` is the safer form (A). Its 0.5-second start is the key's warm server; the key note says so (B).
- Step 7's Discuss (cell 65): a redirect or a disambiguation page also gives 0 results (A, D).
- Step 8, cell 68: the prompt could give the exact line `quote_locator = (By.CLASS_NAME, "quote")` (B); A first passed two arguments and got a `TypeError`.
- Step 10: the chapter's function "stops after its tenth scroll"; the lab's loop says 9, because one scroll was by hand (A). Correct, but worth a clause.
- Step 9's Discuss and cells 28, 78, 90 date the checkpoints 2026-11-17, after the deck's October dates; #203 lists these among the dates to change for the next offering (E).
- Step 11: `getpass()` shows nothing as you type; "nothing appears as you type" (B). Cell 99's `"your-username"` reads like a placeholder to fill in (C).
- Step 13's "Recommended Exercises ahead" mixes exercise and lab step numbers ("Step 3, wait, then measure again: Step 8's `WebDriverWait`"); prefix the exercise's with "Exercise" (B).
- The opening says "Nothing here is turned in"; the Recommended Exercises are, by Sunday. Both right, but a student reading only the notebook could miss the second (C).
- The 320 MB warning appears three times in the notebook (E).

Deck (`slides/week-08/week-08.tex`):
- "Step 12: a first Playwright script" says "A given cell writes Monday's `hello_pw.py`"; it is Friday's (E).
- The closing activity frame uses `slides/week-08/img/is-this-a-pigeon.jpg`; every other frame uses `img/...` (A). It may build only from one folder (not checked).
- "Lab 8: the checks, in code" says "Open it … in the `webdata` environment"; the handout says `webdata` isn't needed (item 10).

Chapter and companion notebook (`ch-08-dynamic-pages.qmd` at `3f9cf2c`):
- Exercise Step 3's note that `page_source` can come out smaller than `response.text` holds for a page already complete; on an infinite scroll it was larger (D, E). "On a page that was already fully formed" says so, but a reader skims it.
- The regex in Check 1 (and the lab's cell 8) stops at the first `];`, so a quote containing `];` would cut the array short with no error (D; reported).

## Suggested next step

**Before merging #203.** Each is small and changes none of what the week teaches:
1. **Item 2:** rerun cell 43 and keep its 10; add "if it prints 0, run it again" to Step 5.
2. **Item 4:** move `quote_locator` above the `read_csv` line in cell 78, or give the read its own cell with a comment on what a 404 means.
3. **Item 5:** time the given scroll loop, and say in Step 13 that both times include their pauses.
4. **Items 9, 10 and 12, Step 12 in one pass:** "`count()` doesn't wait", the `/js-delayed/` question, "copy everything after its first line", and the `playwright-python` line for students without `webdata` (with the handout's install line).

**Right after merging #203:** check that `https://raw.githubusercontent.com/cuinfoscience/INFO4617-Fall2026/main/labs/week-08/data/api_quotes.csv` and `.../scroll-page.html` answer 200, since Step 9 and the fallbacks in Steps 3 and 10 read them.

**Needs the instructor's decision:**
- **Wikipedia in Step 7** (item 1): correct the sentence and teach the contradiction, or move the typing example to a page that allows it; and the same in the chapter. This waits on the open decision raised on #212 about how strictly to read Wikipedia's `robots.txt`.
- **The deck's day frames** (item 3): "at a glance", "Before Wednesday", the Wednesday "Lab: work these" frame, and where Monday's concept frames go. #203 left these to you as your frames.
- **The minutes** (item 8): what in Parts 2 and 3 becomes "read together" or "if time".
- **Code on the slides** (item 14): show it after the room has tried, or keep it as now.
- **The textbook's exercises** (items 6, 7, 11, 17), for a chapter pull request: a vetted list of sites and what a refusal looks like, timing and lengths in Steps 1–5, a setup cell, and definitions of the three labels.
