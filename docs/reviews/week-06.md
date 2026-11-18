# Review: week 06, Parsing Static Web Pages

**What was reviewed:** week 6's lab (`labs/week-06/lab-06.ipynb`, with its key), its deck (`slides/week-06/week-06.tex`), the lab's checkpoints (`labs/week-06/data/`) and chapter 6's Recommended Exercises, as students meet them.
- **Course repository:** the head of pull request #206, `21b478e12ff659012fe7733064c16752a0193a77`, which rebuilt week 6's lab and deck in three parts in the incremental style, for the next offering. It is open and not merged.
- **Textbook:** `ch-06-static-pages.qmd` and its companion notebook at `main`, `3f9cf2cef801181236c9cceaf71f3b63c3ad2491`.

**When:** 2026-11-18, the day after the key's run.

**Method:** five anonymous composite personas, each a kind of student this course has, reviewed the week independently. Each read the chapter and the slides, typed and ran its own code for every lab step from the students' copy, made the mistakes its background makes, attempted the Recommended Exercises on a Wikipedia table of its own choosing, and opened the key only after an honest try. Each review is a **steel man**: it first makes the strongest case for the materials as designed, and only then says where they fall short for that student. This document puts the five together. Every ranked finding was then checked against the repository and the textbook, and is marked **verified** (with how) or **reported, not verified**.

## Who reviewed

| | Degree and major | Python and data background | Interest | Skill |
|---|---|---|---|---|
| A | BS senior, Information Science | One intro Python course; spreadsheets | Qualitative and design: online communities, UX | Minimal |
| B | BA junior, Journalism and Communication | No Python before this course; strong with public records and Excel | Data journalism, local government | Minimal |
| C | BS senior, Business Analytics | Excel, some SQL, a little pandas | Quantitative analytics: markets, customer data, dashboards | Minimal to moderate |
| D | MS first year, Data Science (BA in Statistics) | Fluent in R, moderate pandas; regression and sampling | Quantitative: measurement and validity | Moderate |
| E | MS first year, Information Science (BS in Computer Science) | Moderate Python, git; little data analysis | Design and tools: automation, APIs, building things | Moderate |

## What each completed

The lab has Steps 0–14 and six microsprints: Part 1 (Monday) is Steps 0–4, Part 2 (Wednesday) Steps 5–9, Part 3 (Friday) Steps 10–14, then a 15-minute "from the lab to the textbook" block. All five finished every step. Every request was sent live; no persona needed a fallback cell (25, 41, 102, 111) to get past a refusal.

| | Lab steps finished | Read, not done | Recommended Exercises (their table) | Needed the key for |
|---|---|---|---|---|
| A | 0–13, all microsprints | Step 14's cell | Steps 1–7 (social platforms with 100 million users); Step 4 only by adapting Step 7's pattern | Nothing |
| B | 0–13, all microsprints | Step 14 and the Friday block | Steps 1–7 (counties of Colorado); Step 4's cleanup took three tries | Nothing |
| C | 0–13, all microsprints | Step 14 (answered in their head) and the Friday block | Steps 1–7 (largest U.S. companies; Steps 3, 4 and 6 redone on countries by population, because the first table needed no cleaning) | Nothing; looked at Part 3's saved outputs only to see whether any cell was `not-run-live` |
| D | 0–14, all microsprints | | Steps 1–7 (countries by population) | Nothing |
| E | 0–13, the microsprints | Step 14 (answered in their head) | Steps 1–6 in code (countries by population); Step 7 written in the review | Nothing |

**Estimated time for a real student of that background, in minutes** (the lab's own minutes in the last rows):

| | Part 1 | Part 2 | Part 3 | Exercises |
|---|---|---|---|---|
| A | 55–60 | 55–60 | 45–50 | 75, 30 of it on Step 4 |
| B | 80–90 | 70 | 55–60 | 150 |
| C | 50 | 50 | 55 | 90–120, plus 40–60 reading the chapter first |
| D | 55 | 55 | 45 | 75, 25 of it on checks the exercise doesn't ask for |
| E | 45 | 45 | 40 | 50 |
| **The lab** | **48** (39 in steps, 9 in microsprints) | **56** (46 in steps, 10 in microsprints) | **43** (35 in steps, 8 in microsprints) | none given |
| **The day** | **about 50** | **about 50** | **about 35**, then the 15-minute block | due Sunday |

## Environment blocks

These come from the review machine or from the pull request's state, not from the materials. They are kept apart so that none is read as a flaw in the week.

- **The checkpoints aren't on `main` yet (all five).** `DATA` reads `labs/week-06/data/` from `main` on `raw.githubusercontent.com`, and `main` has only the notebooks; the four files arrive when #206 merges. Every persona got `404` for `films.csv` and pointed `DATA` at local copies from the #206 branch. Step 5's given cell (47) is the only way into Part 2 for a student who missed Monday, so this is a merge-order item: see "Check right after merging".
- **No cell was held back.** The key tags no cell `not-run-live`, and no site refused the review machine: Wikipedia (English, French, Spanish, and the pinned revision), The Numbers, oscars.org, Rotten Tomatoes and quotes.toscrape.com answered every request, with no 429s. The only 403 was Step 3's intended one. Box Office Mojo and IMDb were never requested, as the lab says.
- **Rotten Tomatoes' grid moved.** The key saved 12 of 28 tiles with no Tomatometer on 2026-11-17; the personas saw 10 of 28 live. The lab says the grid changes weekly.

## The strongest case for the week as designed

**Every tool meets a few lines of HTML a student can read in full before it meets a real page.** All five said so, and named the same moments: the three-cell row in Step 2 (`1Aquaman`, then `['1', '', 'Aquaman']`), `tiny_html` in Step 4, the French-shaped `tiny_fr` in Step 9 (0 and 1, which predicted the real page's 0 and 2), and the one `<rt-text>` tile in Step 13. A said that made the real page's output "readable"; C compared it to reconciling a small case at work before the real one; D to "checking a function on a toy data set". E called it the reason each real page "costs one more cell, not a new idea".

**The failures are planted on purpose, and each has a cheap check beside it.** The Numbers refuses `WIKI_HEADERS` with a 403 and accepts `HEADERS`; both of its tables have 84 rows, so "take the biggest" can't choose; the phone table has 405 cells in its first data row under `html.parser` and 5 under `lxml`; `F8$1,238,764,765` becomes 81,238,764,765 and only the plot and the sort show it; `/js/` answers 200 with 0 quotes. B called these "the best teaching in the lab" and found "check the largest number against your own eyes" in Step 6's plot, "in a form I would not forget". C got "check your numbers" "at a gut level"; D called Step 6 "the best" validity moment; E took away that "you cannot trust a parser until you have counted something".

**Typing is where the thinking is, and given code arrives only after one case by hand.** Typed cells are one to four lines; the loops, `read_infobox()`, the Oscars loop and `parse_oscar_ceremony()` are given, each after the student has typed one pass of it. A and E singled out "Given: your last five cells, for every card" (cell 93) and "Find your lines in it" (Step 12): the given code doesn't read as a black box. B, with no Python before this term, finished every typed cell without the key.

**The order puts permission before technique.** Step 1 asks `robots.txt` first, on two lines the student writes, then on Wikipedia's real file, then for the chapter's six sites; Step 3's 403 follows. B said this "is where a journalist's instincts already are", and read the pinned `oldid` in Step 4 as "the same instinct as keeping a dated copy of a record"; E called it "a good reproducibility lesson". The ladder from `read_html` to `find_all` to `select` to cards to a page JavaScript builds "felt like one idea getting harder" (B), and matches the chapter's 2×2 (D).

**The Discuss boxes ask the questions these students care about.** Who reads the User-Agent, whether one request from a notebook is crawling, which edition is "the record of the film" (A); "25 winners for 24 categories" and a `film` column that holds a country or a song (D: "the unit of the data is not the unit you want to count").

## Where it falls short, ranked

No persona found a privacy problem, and the checkpoints carry only placeholder addresses (`your-email@colorado.edu` in The Numbers' saved page, two generic ones in Rotten Tomatoes'), verified by searching the four files for addresses. The wrong-result problems come first. After them, items are ranked by how many personas hit each, how badly, and whether it stopped A or B. Cell numbers are positions in `labs/week-06/lab-06-key.ipynb` at `21b478e`, counted from 0; a fix to the key means remaking the students' copy with `labs/tools/make_student_copy.py`.

1. **The chapter's cleanup, carried to a student's own table, gives wrong numbers with no error.**
   - **Who:** A, B (both minimal). Item 2 is the same bug in the lab's own table (C).
   - **What happened:** Exercise Step 4 says "Apply the chapter's cleanup patterns", and the chapter says `[^0-9]` "removes the $ and the stray footnote letters in one pass". On their own tables:
     - A, social platforms: `3.070 billion[1][2][3]` became 3070123 and `2.504 billion[4]` 25044 (the decimal point dropped, the footnote numbers kept).
     - B, Colorado counties: `4,773.27 sq mi (12,363 km2)` became 477327123632 (both units glued together). The dtype went from text to `int64`, which is exactly what Exercise Step 4 asks to show "to prove the conversion happened".

     A caught it on the plot, B by sorting; both said the habit came from Step 6. The lab's Step 7 fixes the gross column, but Step 14's hand-off (cell 119) points the exercise to "Steps 6–7's cleanup" and never says the pattern is specific to that column.
   - **Why it matters:** this is the week's own lesson (a number wrong by a pattern hides in a table), arriving on the exercise, at home, with no plot prompting the check. B: "a student who follows the exercise literally would hand in a dtype table as 'proof' and a wrong column."
   - **Proposed fix:**
     - Lab key, cell 119, the Step 4 bullet: "Step 7's `str.extract`, not Step 6's pattern: keeping every digit glues together decimals, footnote numbers and a second unit. Check the three largest values beside their raw text."
     - Lab key, Step 7's Discuss (cell 61): "What would `[^0-9]` make of `3.07 billion[1]`, or of `4,773.27 sq mi (12,363 km2)`?"
     - Chapter and companion notebook (textbook), Exercise Step 4: "show `dtypes`, and the three largest values beside their raw text, to prove the conversion is right"; and one sentence in "Cleaning Up read_html Results" that the pattern keeps every digit, including a footnote's.
   - **Status:** verified: running the key's `[^0-9]` on the three cell texts gives exactly 3070123, 25044 and 477327123632; the chapter's sentence and Exercise Step 4's wording at `3f9cf2c`; cell 119's bullet. The cells' text on the live pages is the personas'.

2. **Rank and Peak carry footnote letters too, and one of them cleans to a plausible wrong number.**
   - **Who:** C.
   - **What happened:** in `films.csv`, `Rank` holds `43JP` (The Dark Knight Rises) and `Peak` holds `24RK`, `23RK`, `5RK` and `4TS3`. The lab cleans only `Worldwide gross` and never says the other columns have the same markers. C found them only by running `str.fullmatch(r"\d+")` on every column, which isn't in the materials.
   - **Why it matters:** the `[^0-9]` pattern gives the right number for four of the five, which hides the fifth: Toy Story 3's `4TS3` becomes 43, a peak that looks possible (its rank is 47) and is wrong (it peaked at 4). And because of `43JP`, `Rank` reads back from `films.csv` as text, so sorting by it sorts as text. The lesson "this kind of bug lives in the whole table" is the one a student's project needs.
   - **Proposed fix:** lab key, Step 7: a given cell after cell 60 that lists the cells of `Rank` and `Peak` that aren't only digits (`films[~films["Peak"].astype(str).str.fullmatch(r"\d+")]`), and a Discuss bullet: "What would Step 6's pattern make of `4TS3`?" Deck: the same bullet on "Step 7: what changed?".
   - **Status:** verified on `labs/week-06/data/films.csv` at `21b478e`. C wrote that `43JP` would also become a wrong 43; it becomes 43, which is right (see "Corrections").

3. **"A factor of ten" is about 66.**
   - **Who:** D; A repeats the slip ("ten times above everything else").
   - **What happened:** Step 6's text (cell 49) says "a number wrong by a factor of ten hides in a table and stands out on a plot". The deck says it twice: "A number wrong by a factor of ten hides in a table" on "Step 6: plot it to check, given", and "a number ten times too big" in the "Error flavors" box of "This week, every class is live coding". The key's own output is 81,238,764,765 against 1,238,764,765.
   - **Why it matters:** the sentence states a number in the week whose point is to check numbers. D "looked for a tenfold error"; the real mechanism, a footnote's digit glued to the front, is the more useful one to name.
   - **Proposed fix:** "a number with a digit too many, 66 times too big" in cell 49, and the same on the two deck frames (`slides/week-06/week-06.tex`, the "Step 6: plot it to check, given" frame and the "Error flavors" block).
   - **Status:** verified: 81,238,764,765 ÷ 1,238,764,765 = 65.6 (cells 55 and 60); on the plot the point sits at 27.6 times the next-highest gross, $2,941,331,540. The three sentences are as quoted.

4. **The deck's first frame, and two of its last, describe fall 2026's one-day week.**
   - **Who:** A, B, C, D, E.
   - **What happened:** "This week at a glance" says Monday "Concepts & notebook intro", Wednesday "Notebook lab", Friday "No class again on Friday, still submit PRs and issues for Sunday", and "Bring a laptop: Wednesday is hands-on"; the title is dated "September 21 & 23, 2026". The next frame says "This week, every class is live coding", and Friday has its own section, Steps 10–14. At the end, "After the lab: work these, then show-and-tell" and "Improving Chapter 6 and others" ("Today we make the book better. Each of you opens a pull request") describe a Friday revision workshop, where the lab has a 15-minute "from the lab to the textbook" block (cell 121) (D).
   - **Why it matters:** it is the first content slide. A student who reads ahead skips Friday, which has Strategies 6–8 and the handout (all five said so).
   - **Proposed fix:** `slides/week-06/week-06.tex`: the at-a-glance frame's three daybands to "Part 1, Steps 0–4", "Part 2, Steps 5–9", "Part 3, Steps 10–14, and 15 minutes on the textbook", as the lab's opening cell says; drop "No class" and "Bring a laptop: Wednesday"; make "Improving Chapter 6" match cell 121. These are the instructor's frames, and the `\date` line needs the next offering's dates: see "Needs the instructor's decision".
   - **Status:** verified: the frames at `21b478e`. These frames are right for the week as taught this fall (`docs/course-facts.md`: through week 9, a Wednesday lab and a Friday revision workshop; week 6's lab "rebuilt in three parts on 2026-11-17, for the next offering"). They are wrong for the deck #206 rebuilt.

5. **Adapting a pattern is the largest jump in the week, and the lab gives no kit for it.**
   - **Who:** A, B, C.
   - **What happened:** Step 6 explains `[^0-9]`, and Step 7 explains `\$([\d,]+)` in one sentence; cell 58's comment says "`[0]` is the part in parentheses". Nothing says that `\.` is a real dot, what `+` does, or what `extract` returns for a cell with no match. A got to `([\d.]+)` only by copying Step 7's pattern; B wrote `([\d,]+\.\d+)` on the third try, after searching the web. C read `[0]` as possibly "the first row", and understood it only from having used `.extract()` before.
   - **Why it matters:** item 1's fix needs it. B: a student with less patience "would pick a table with no text in its number column", and skip the week's main lesson.
   - **Proposed fix:** lab key, Step 7: in cell 58's comment, a short kit (`\d` a digit; `[\d,]+` one or more digits or commas; `\.` a real dot; parentheses keep what they match), and show `gross_text.str.extract(AFTER_DOLLAR).head(3)` before taking `[0]`, so the one-column table is visible (C). Optional (B): a given cell that tries one pattern on `"1,182.29 sq mi"` and `"12.5%"` and on a cell with no match (NaN). That sets up the exercise without solving it.
   - **Status:** verified by reading cells 49, 57 and 58. The minutes and tries are the personas'.

6. **Exercise Step 2 asks for a file the lab never writes.**
   - **Who:** A, B, E.
   - **What happened:** Exercise Step 2 says to save `response.text` to a local file and read it back. Cell 119 points it to "this lab's checkpoints are saved pages, read like live ones; Step 4 fetched once and parsed the text it kept"; Step 4 kept it in a variable. B had to look up `with open(...)`. E flags that `open(path, "w")` without `encoding="utf-8"` can raise `UnicodeEncodeError` on Windows for a 1.4-million-character Wikipedia page.
   - **Why it matters:** A knew `open()` from an intro course; B, with no Python before this term, would have stopped here.
   - **Proposed fix:** lab key, Step 4: a given cell after cell 39 that writes `wiki_response.text` to `wiki-list.html` with `encoding="utf-8"` and reads it back (three or four lines), and cell 119's Step 2 bullet pointed to it.
   - **Status:** verified: no lab key in weeks 1–6 at `21b478e` writes text with `open()` or `.write()` (week 1 saves a DataFrame with `to_csv()`). E's Windows error is reported, not tested.

7. **Exercise Step 4 assumes a table that needs cleaning, and nothing warns about summary rows.**
   - **Who:** C, D, E.
   - **What happened:** C's first table (largest U.S. companies) arrived with every numeric column already `int64`, so "show `dtypes` before and after" had nothing to show; C redid three steps on a second table. D's and E's population table arrived with `Population` as `float64`; only `% of world` was text. D's table also had a "World" row above India and China, and an all-empty row, so Exercise Step 5's "top ten rows" puts World first.
   - **Why it matters:** the exercise's cleaning step is where the week's lesson is applied; a student whose table is already numeric writes a cell that does nothing, and one who ranks a table with a total row ranks the total.
   - **Proposed fix:** chapter and companion notebook (textbook), Exercise Steps 4 and 5: "check `dtypes` right after `read_html`, and clean whatever is still text"; "drop summary rows (a World, a Total, an empty row) before you rank". Lab key, cell 119: the same two sentences under Steps 4 and 5.
   - **Status:** verified: Exercise Steps 4 and 5 at `3f9cf2c` as quoted. The tables' dtypes and rows are the personas'.

8. **Parts 2 and 3 run over their days by the lab's own minutes, and the minimal personas run over Part 1 too.**
   - **Who:** A, B, C. B rates pace 2; A and C 3; D and E 4.
   - **What happened:** the headings add to 48 minutes for Part 1, 56 for Part 2 and 43 for Part 3, against about 50, 50 and 35. B needed 80–90 minutes for Part 1 without being stuck on any cell: between Steps 1 and 4 a student with no Python meets `RobotFileParser`, `urlparse`, a loop, `BeautifulSoup`, `find_all`, `class_`, a list comprehension, two parsers, `StringIO` and `read_html`. C notes that Steps 9 and 11 are chains of typed cells, so one early typo blocks the next four or five.
   - **Why it matters:** the deck's advice for falling behind is to copy from the key; B would do that by Step 3, where the decoy table, the week's main idea, arrives.
   - **Proposed fix:** the minutes are the instructor's decision. The personas' candidates:
     - Mark one microsprint a part "if time": B would choose Step 1's and Step 3's in Part 1; C would mark them all optional.
     - End Monday at Step 3 and open Wednesday with Step 4 (B). That moves 8 minutes into Part 2, which is already over.
   - **Status:** verified: the headings in the key sum to 39 + 9, 46 + 10 and 35 + 8; `docs/course-facts.md` gives about 50, 50 and 35 minutes. The persona estimates are their own.

9. **Step 2's empty cell and the chapter's printed outputs don't match what students get.**
   - **Who:** B, C, D, E.
   - **What happened:** Step 2 (cell 17) builds its row "as a box-office row with no previous rank would have". The live page's header is `Rank, Prev, Title, Gross, ...` and Aquaman's row starts `1, (1)`; the chapter prints `['Rank', '', 'Movie', 'Distributor', 'Gross', ...]` and `'$105,455,062'` where students get `$92,087,265`. The chapter's Wikipedia row 0 is `$2,925,713,609`; the lab's pinned revision gives `$2,941,331,540`. The chapter's Rotten Tomatoes count is 16 of 28; the key's 12; live, 10.
   - **Why it matters:** a student who reads the chapter first, as C and E did, thinks their own code is wrong at Step 3. The Friday block (cell 121) asks students to compare, which is good, and comes two days late.
   - **Proposed fix:** lab key: Step 3's text (cell 22), one sentence: "the chapter printed this page in October; your header (`Prev`, `Title`) and Aquaman's gross will differ, and Friday asks why"; Step 2's text, "a made-up row, to show the risk"; Step 4's text (cell 35), "the chapter's row 0 is from another revision than the one we pin". The chapter's printed outputs are for a textbook follow-up, which the Friday block already collects.
   - **Status:** verified: cells 17, 30 (its saved header and first row) and 40, and the chapter's lines at `3f9cf2c`.

10. **The Sinners microsprint gives two counts, and the lab doesn't say which to believe.**
    - **Who:** C, D; E noted it.
    - **What happened:** the given cell prints "Sinners 15 rows by film; 16 rows that mention it", and the Share asks for "its count both ways". The reason (Original Song puts the song's title in `film` and the film in `entity`) is in the Discuss box below, unconnected to the count. C "would write '15' in my notes". D checked that 16 is the number of nominations here, and that the table is one row per honoree block, which equals a nomination only when each nomination has one block.
    - **Why it matters:** it is a small, honest case of the unit of the data not being the unit you want to count (D), left one sentence short.
    - **Proposed fix:** lab key, cell 94's Share: add "Why do they differ, and which one counts nominations?", as the deck's frame already asks; and one sentence under Step 11 (cell 84): "our table has one row per honoree block, not per nomination".
    - **Status:** verified: cells 94, 96 (its output) and 97; the deck's "Microsprint: the most nominations" adds "Why do they differ?" and the lab doesn't. D's count of blocks per nomination is reported.

11. **The only check the week teaches is "look at the plot".**
    - **Who:** D, C.
    - **What happened:** Step 7's "how many rows changed? 1" shows the new cleanup differs from the old, not that it is right. D wrote a check of their own: after the fix, `gross_fixed` falls in rank order (`is_monotonic_decreasing` is `True`); before it, one value rises. C reconciled Step 3's table against the row the loop skipped: the 81 films' `Gross` adds to $342,738,718, the skipped row's total, and there are 81 of them, as it says. Neither check is asked for; the key's own Step 14 answer (cell 120) uses the second one.
    - **Why it matters:** "my project will have a column I cannot eyeball against a plot" (D). A student without C's habit answers the Step 3 Discuss question "was that right?" with "yes, it was junk".
    - **Proposed fix:** lab key: one typed line in Step 7, `print(films["gross_fixed"].is_monotonic_decreasing)`, and a Discuss bullet, "what second source of truth does your table have?" (D); in Step 3's Discuss (cell 34), "add up `Gross`: does it match the skipped row?" (C).
    - **Status:** verified: on `films.csv`, the fixed column is monotonic and the chapter's has one rise; cell 30's output has the skipped row and `(81, 9)`. The $342,738,718 sum is C's.

12. **Step 11's prompts say "print its text", and `.text` keeps the card's new lines.**
    - **Who:** A, B, E.
    - **What happened:** cells 88, 90, 91 and 92 say "print ... text"; the key answers with `get_text(strip=True)`, and so does the given loop (cell 93). A student who types `.text` gets `Michael B. Jordan` with blank lines around it, and no word on why the given loop's output is clean.
    - **Why it matters:** small, but it is the cell a student copies into a project, and Steps 8 and 9 had already used `get_text(strip=True)`.
    - **Proposed fix:** lab key, cells 88 and 90–92: "print its `get_text(strip=True)`".
    - **Status:** verified by reading the four prompts and the key's answers.

13. **Step 1's microsprint has nothing to share for one of its two crawlers.**
    - **Who:** D, E.
    - **What happened:** with `"GPTBot"`, the six answers are the same as for `CLIENT` (Box Office Mojo and IMDb `False`), so the Share, "which of the six pages it may fetch that we may not", is "none". With `"Googlebot"` both flip to `True`.
    - **Why it matters:** a pair that picks GPTBot finishes in 30 seconds, or thinks it typed something wrong, when the difference is the point: a site that names one crawler and not another (E).
    - **Proposed fix:** lab key, cell 13, and the deck's "Microsprint: another crawler": "try Googlebot, then GPTBot, and compare: why would a site name one and not the other?"
    - **Status:** the Googlebot half verified from cell 15's saved output (all six `True`). The GPTBot half is reported, the same by two personas.

14. **`get_text(strip=True)` glues words together, and Exercise Step 6 meets it unexplained.**
    - **Who:** C, D, E.
    - **What happened:** Step 8's Discuss asks where the space in `Productioncompanies` went, and the lab never answers. In Exercise Step 6, which asks students to compare their own header with `read_html()`'s, all three got `% ofworld` against `% of world`, and it "looks like a bug in my code" (C).
    - **Why it matters:** the exercise asks for exactly this comparison, and the explanation is one clause.
    - **Proposed fix:** lab key, cell 119's Step 6 bullet: "use `get_text(" ", strip=True)` for header text, as `read_infobox()` does for values"; Step 8's text (cell 62) or Discuss, one clause naming the cause.
    - **Status:** verified: cell 67's output and cell 68's Discuss; Exercise Step 6 at `3f9cf2c`. The `% ofworld` header is the personas'.

15. **Two silent slips have no expected value in front of the student.**
    - **Who:** B, C (`parse()`); A, B (`regex=True`).
    - **What happened:**

      | Slip | What comes back | Where the help is |
      |---|---|---|
      | `rp.parse("User-agent: *\nDisallow: /w/")`, a string for a list (C), or Wikipedia's file without `.splitlines()` (B) | `True` for every page, no error | Step 1's Discuss, after the six-site loop |
      | `str.replace(NOT_A_DIGIT, "")` without `regex=True` | nothing replaced (pandas 3 reads the pattern as text); then `to_numeric` makes every gross NaN | none; only the empty plot |

    - **Why it matters:** both look like success; A and B can't read a traceback, and here there is none to read.
    - **Proposed fix:** lab key, cell 8's comment: "expect `False`, then `True`"; Step 6's text (cell 49): "leave out `regex=True` and pandas looks for the characters `[^0-9]` themselves: nothing changes".
    - **Status:** verified by reading cells 8, 16, 49 and 51. The outputs are the personas'.

16. **Nothing in the week asks whether the data is already published.**
    - **Who:** B.
    - **What happened:** every example is movies. The chapter's Colorado legislators example, whose page now offers a downloadable directory, has no counterpart in the lab. B wanted one moment where the first move is "check whether the agency already publishes this".
    - **Why it matters:** B's interest is local government; B rates motivation 4 and confidence 3, and names this.
    - **Proposed fix:** one Discuss bullet in Step 11 (cell 97): "Where would you look for the Academy's own data file before scraping this page?" No new code.
    - **Status:** reported; a judgment about scope.

### Corrections

Claims in the reviews that turned out wrong or inexact, and what this document does with them:
- **C: `43JP` in `Rank` would become a wrong 43.** It becomes 43, which is the right rank. Only `Peak`'s `4TS3` cleans to a wrong number. Item 2 says so.
- **A: the Fate of the Furious point sits "ten times above everything else".** It sits 27.6 times above the next-highest gross; the error itself is 65.6 times. Item 3.
- **D: "the step budgets (50, 46 and 36 min plus sprints)".** The headings give 39, 46 and 35 minutes in steps, and 48, 56 and 43 with the microsprints (item 8).
- **E: "all four microsprints".** There are six; E's review reports the results of five.
- **E: the lab's one plot is a scatter, so the exercise's bar chart has no practice.** Week 3's lab draws bar charts with `barh`. Dropped from item 6.
- **A: Step 7's Discuss doesn't say what `†` means.** It does: "The titles still carry `†` for films in theaters" (cell 61). Dropped.
- **All five: the checkpoint 404.** Not a flaw in the materials: the files arrive with #206 (see "Environment blocks").

## Disagreements

- **Too slow, or about right.** B rates pace 2 and needed 80–90 minutes for Part 1; A and C rate it 3; D and E rate it 4, and E's three parts came to 130 minutes, under the lab's 147. Where they name the tight steps, they name the same ones: Step 3 (14 minutes, the decoy tables and the phone-table microsprint; A, E) and the chains of typed cells in Steps 9 and 11 (A, C, E). That suggests the "if time" marks belong on those steps' microsprints, not on cutting typed cells.
- **Cut, or add.** B and C would mark microsprints optional and shorten Part 1. D would add a typed check (item 11); E would add a status check to `oscars_2024` and would have taken "more, e.g. `select()` against `find()` side by side". Both are true for their students; the additions are one line each, and could go in Discuss boxes so a slow class can skip them.
- **What the given cells do.** D and E found them well placed and readable after the typed case. C found them "the hard part, only read, not explained", and understood the comprehension and the regex only from earlier pandas. The kit in item 5 serves C without typing more.
- **The plot, or a rule.** A, B and C valued Step 6's plot as the lesson they'd remember; D wants a rule to carry to a column "I cannot eyeball". Item 11's line adds the rule beside the plot, not instead of it.
- **Difficulty.** A, B and C rate it 3, D and E 2. The typed cells were fair for all five; the spread is in the exercises, where A, B and C each spent more than an hour on the cleanup step (items 1, 5 and 6).
- **What the week is for.** For A and B, permission and the people behind the data; for C and D, checking numbers; for E, the shape of a parser. B found the movies a thin bridge to a civic project (item 16), and A wanted one early sentence on why a UX or community researcher would scrape at all.

## Ratings

Each on a scale of 1 to 5. For difficulty, 5 is hardest for that persona's background.

| | A | B | C | D | E | Mean |
|---|---|---|---|---|---|---|
| Clarity of motivation | 4 | 4 | 4 | 4 | 4 | 4.0 |
| Pace | 3 | 2 | 3 | 4 | 4 | 3.2 |
| Difficulty for my background | 3 | 3 | 3 | 2 | 2 | 2.6 |
| How much I learned | 4 | 4 | 4 | 4 | 4 | 4.0 |
| Confidence I could do this on my project | 3 | 3 | 3 | 4 | 4 | 3.4 |

Three of the five took a point off motivation for the at-a-glance frame (item 4). What holds the confidence down: A, a messy numeric column or a page of cards without help; B, writing a pattern or saving pages without help; C, finding a card page's anchors alone, since the lab gives the class names; D, checking a column that isn't obviously wrong (item 11); E, status checks and retries, which the week names but doesn't have students type.

## Small things

Deck (`slides/week-06/week-06.tex`):
- "Step 6: plot it to check, given" says the cell counts the footnote markers, but shows neither the `footnote_count` line nor `set_title` (A, D).
- "Microsprint: the phone table, two parsers": the Share drops the lab's second half, how many rows the chapter's loop would keep, which is the interesting answer (E).
- The instructor's "Strategy 1" frame calls `boxofficemojo.com/weekly/2026W37/` "a perfect use case for `pd.read_html()`", and "Strategy 8" shows IMDb; Step 1 finds both disallowed, and the deck doesn't say so where the frames are. "Strategy 2" cites `weekend/2026/09/18`, where the lab uses `weekly/2018/12/28` (B, C). `docs/plans/2026-11-16-incremental-style-revisions.md` already lists the first.

Lab (`labs/week-06/lab-06-key.ipynb`):
- `CLIENT` is retyped in three setup cells (3, 46, 82); a student who updates only Monday's sends the placeholder on Wednesday and Friday (B, C, D).
- The microsprint prompts (cells 14, 32, 76, 104) read like code: `# Microsprint: sprint_agent: "Googlebot", or "GPTBot"` copied without the `#` is a `SyntaxError` (E).
- Step 3's prompt (cell 23) names the variable `refused` before the student sees the refusal (B).
- The four fallback cells (25, 41, 102, 111) word "only if" four ways (B).
- Step 3's "the second table they print is the chapter's `tables[1]`" is hard to parse on first reading (D, E).
- Wikipedia's `robots.txt` starts with a byte-order mark and comments, so cell 9's first 200 characters show no rule (C, E).
- quotes.toscrape.com has no `robots.txt` (404); Step 13 doesn't say so, though Step 1's message is "ask first" (A, B, E; reported).
- `weekly`'s last column is `Total\xa0Gross`, with a non-breaking space, so `weekly["Total Gross"]` raises `KeyError`; the chapter's Common Issues covers it, the lab doesn't meet it (D; reported).
- Step 10's Discuss (cell 83) asks which sites asked for the library's name; a student who joins on Friday has no `WIKI_HEADERS` to look at (A).
- The opening cell names the handout *Cards to rows* but not its path, `handouts/week-06/oscars-cards-to-rows.pdf` (A).
- Step 12's "Run it on one year by hand" reads as "type the function"; it means "call it" (B).
- Step 2: `print(tiny_row.text)` shows `1Aquaman`, which can read as a typo; `repr()` would show the string (B).
- The exercise is submitted from the companion notebook, whose `HEADERS` holds the student's address. A line in Step 0, "use an address you don't mind your instructor seeing in the file", would cover it (B).
- Cell 119 says to fetch Wikipedia with `WIKI_HEADERS`; the chapter's Exercise Step 1 says "your named `HEADERS`". D got 200 with plain `HEADERS` on the population page (D).

Chapter (`ch-06-static-pages.qmd` at `3f9cf2c`):
- Strategies 1 and 8 request pages whose `robots.txt` disallows unnamed crawlers; a student copying the chapter into the exercises sends requests the lab refused (A, C). The Friday block raises it.
- The printed outputs for The Numbers, the Wikipedia list and Rotten Tomatoes are out of date (item 9).

## Suggested next step

**Fix first, on the #206 branch, before it merges.** Each is small and changes none of what the week teaches:
1. **Item 3:** "a digit too many, 66 times too big" in cell 49 and the deck's two frames.
2. **Items 1 and 2:** in the lab key, cell 119's Step 4 bullet (Step 7's pattern, and check the largest values beside their raw text); a Discuss bullet in Step 7 on `3.07 billion[1]`; a given cell listing `Rank` and `Peak` cells that aren't only digits.
3. **Item 5:** the pattern kit in cell 58's comment, and the one-column `extract` shown before `[0]`.
4. **Item 6:** a given cell in Step 4 that saves `wiki_response.text` with `encoding="utf-8"` and reads it back.
5. **Items 10, 12 and 13:** one line each: the Sinners Share, "print its `get_text(strip=True)`", and "Googlebot, then GPTBot".

**Check right after merging #206.** Open `DATA` + each of `films.csv`, `oscars-2024-2026.csv`, `the-numbers-2018-12-28.html` and `rotten-tomatoes-in-theaters-2026-11-17.html` on `raw.githubusercontent.com` and confirm each answers 200, then run cell 47 once. Until then, Step 5's given cell fails for every student who starts on Wednesday.

**Needs the instructor's decision:**
- **The at-a-glance frame, the `\date` line, and the two closing frames** (item 4): they are the instructor's frames, and right for this fall's week; the wording for the next offering, and its dates, are the instructor's call.
- **The minutes** (item 8): 56 against about 50 on Wednesday and 43 against about 35 on Friday, and which microsprints become "if time".
- **The chapter's exercises** (items 1, 7 and 14): "the largest values beside their raw text" in Step 4, "check dtypes first" and "drop summary rows", and `get_text(" ", strip=True)` in Step 6. These are textbook changes, for a textbook pull request.
- **A civic example** (item 16): a Discuss bullet, or nothing this term.
