# Review: week 09, Extracting Data from PDFs

**What was reviewed:** week 9's lab (`labs/week-09/lab-09.ipynb`, with its key), its deck (`slides/week-09/week-09.tex`), the lab's checkpoints (`labs/week-09/data/summary.csv` and `totals.csv`) and chapter 9's Recommended Exercises, as students meet them.
- **Course repository:** the head of pull request #204, `50192aab9ce2cf2367076542ea25895fb090ceb9`, which rebuilt the lab in three parts and the deck in small cells, for the next offering. It is open and not merged, so every fix below names the file on that branch.
- **Textbook:** `ch-09-pdfs.qmd` and its companion notebook at `3f9cf2cef801181236c9cceaf71f3b63c3ad2491`, the book's `main`.

**When:** 2026-11-17 and 18.

**Method:** five anonymous composite personas, each a kind of student this course has, reviewed the week independently. Each read the chapter and the slides, typed and ran its own code for every lab step it could from the students' copy, made the mistakes its background makes, attempted the Recommended Exercises, and opened the key only after an honest try. Each review is a **steel man**: it first makes the strongest case for the materials as designed, and only then says where they fall short for that student. This document puts the five together. Every ranked finding was then checked against the repository and the textbook, and is marked **verified** (with how) or **reported, not verified**. Cell numbers are positions in `labs/week-09/lab-09-key.ipynb` at `50192aab`, counted from 0; the students' copy has the same 125 cells.

## Who reviewed

| | Degree and major | Python and data background | Interest | Skill |
|---|---|---|---|---|
| A | BS senior, Information Science | One intro Python course; spreadsheets | Qualitative and design: online communities, UX | Minimal |
| B | BA junior, Journalism and Communication | No Python before this course; strong with public records and Excel | Data journalism, local government | Minimal |
| C | BS senior, Business Analytics | Excel, some SQL, a little pandas | Quantitative analytics: markets, customer data, dashboards | Minimal to moderate |
| D | MS first year, Data Science (BA in Statistics) | Fluent in R, moderate pandas; regression and sampling | Quantitative: measurement and validity | Moderate |
| E | MS first year, Information Science (BS in Computer Science) | Moderate Python, git; little data analysis | Design and tools: automation, APIs, building things | Moderate |

## What each completed

The lab has Steps 0–14 and five microsprints: Part 1 (Monday) is Steps 0–4, Part 2 (Wednesday) Steps 5–10, Part 3 (Friday) Steps 11–14, then Friday's 15-minute revision block. Step 6, the city's portal, is run by the instructor in class; three personas read it and two ran it once, as the step says students may at home.

| | Lab steps finished | Read, not done | Microsprints | Recommended Exercises | Opened the key for |
|---|---|---|---|---|---|
| A | 0–14, Step 6 run once (two requests, the 30-second pause) | none | all five | Steps 1–7 | cells 14 and 100, afterwards |
| B | 0–5, 7–14 | 6 | all five | Steps 1–6; Step 7 sketched | nothing; compared afterwards |
| C | 0–5, 7–14 | 6 (see "Environment blocks") | all five | Steps 1–7 | cells 73 and 100, afterwards |
| D | 0–5, 7–13; Step 14 answered, not written | 6 | all five | Steps 1–6; Step 7 answered, not written | nothing; compared afterwards |
| E | 0–14, Step 6 run once | none | all five | Steps 1–6; Step 7 written | cells 22 and 100, afterwards |

**Estimated time for a real student of that background, in minutes** (the lab's own minutes in the last rows):

| | Part 1 | Part 2 | Part 3 | Exercises |
|---|---|---|---|---|
| A | 55–65 | 90–100 | 60–70 | about 120, 20 of it on Step 3's function |
| B | 55–70 | about 90 | about 60 | about 120, most on Steps 3 and 7 |
| C | about 45 | about 80 | about 50 | about 120, plus 90 reading the chapter |
| D | about 55 | about 75 | about 55 | about 120 |
| E | 35–40 | 60–70 | 35–40 | 90–120 |
| **The lab** | **35** (30 in steps, 5 in a microsprint) | **64** (50 in steps, 14 in microsprints) | **40** (35 in steps, 5 in a microsprint) | none given |
| **The day** | about 50, which also holds about 10 minutes of concepts and the 10-minute exercise by hand (#204's description) | about 50 | about 35, then the 15-minute revision block | due the Sunday after |

## Environment blocks

These come from the review machine, not from the materials. They are kept apart so that none is read as a flaw in the week.

- **The machine's own pypdf and pdfplumber stopped on import (all five)**, with a panic from a broken `cryptography` build. Each persona made a virtual environment, which gave pypdf 7.1.0, pdfplumber 0.11.10 and Tesseract 5.3.4: the versions the key was run with. pypdf 7.1.0 counts a few characters fewer than the chapter's 6.20.1 on some pages (2,278 against 2,279 on page 2 of the December 2024 report), and Step 12 parsed 29 of Exhibit 3's 30 rows and set 1 aside, as the key's Friday cell says 5.3.4 does. These differences are versions, not mistakes.
- **Part 3's checkpoints are not on `main` yet (all five).** Cell 92 reads `summary.csv` from `https://raw.githubusercontent.com/cuinfoscience/INFO4617-Fall2026/main/labs/week-09/data/`, and cells 77 and 118 point at the same folder. On `main` that address answers 404, because the files exist only on #204's branch; from the branch they answer 200. Cell 92 stops with `HTTP Error 404: Not Found`, and a fresh Friday kernel then has no `summary_df` (cell 104 raises `NameError`). Each persona read the files from the branch and went on. This is a merge-order item, not a flaw: see "Check right after merging #204", under "Suggested next step".
- **The city's portal (C):** its `robots.txt` didn't answer the review machine, so C sent nothing and read Step 6. A and E found `robots.txt` answering 404 (no rules) and ran Step 6 once each; E needed the machine's own certificate authority beside the book's bundle, which a student's laptop won't. Step 6 is the instructor's in class, so none of this bears on a student.
- **Nothing else.** GitHub's raw files answered every request, with no 429s.

## The strongest case for the week as designed

**The week makes one idea physical: a PDF is drawing instructions, and everything else is inferred from position.** All five said so. Step 2's bare `cover_text[:20]` shows six runs of a space and a new line before "REVENUE REPORT"; Step 3 shows that the page's first character is a space and that "City" arrives one letter at a time, at `x0` 54.0. By Step 7, when pypdf writes "P age 1" and "M / ayor", A "was not surprised", because "I had already seen a page is a heap of letters at coordinates." C called the order of Steps 1–4 (bytes, then pages, then one word, then characters and images per page) "the right mental model"; for E it is how one debugs an unknown library anyway: "smallest call, read the output, widen."

**A number typed on Monday pays off on Wednesday.** Step 3's `found[0]["top"]` is 380.18; Step 9's `tables[0].bbox` ends at 375.24. B, D and E singled this out: "That gap is the whole bug, found with two numbers and no explanation from anyone" (D); "the best moment in the week, and it only works because the number is typed on Monday and recalled on Wednesday" (B). The Step 9 microsprint then shows the 2018 report's finder stopping six points short too (523 against 529), which D read as "a replication on a second unit" and E as proof that "one file is not the corpus."

**The checks are a hand routine made repeatable, and they are real checks.** Monday's exercise has students copy the summary table into a spreadsheet and sum five sources against the subtotal; Step 10 does the same sum in code. B, who retypes records clerks' PDFs for a living, "never felt the code was a different kind of work"; C called it "an audit habit, not a PDF trick." Step 10's roll call, precision 1.0 and recall 0.56, is "exactly the lesson that precision alone hides a recall problem" (D), and its Discuss line, that the sums show faithful copying, not correct figures, is "the correct distinction between fidelity and validity" (D). Step 12 closes the loop: OCR's 2024 total, 173,908,431, matches the text page's to the dollar (C, D, E), and the one-row crop reads `7,608,759` where the whole picture reads `7,608.759`, so students see the OCR error before any given cell catches it (B, C, E).

**The typed and given cells are split where they should be.** Every typed cell is one to three lines and names the variable to make; every loop, regular expression and DataFrame build is given, after one case typed by hand (A, B, C, E). Given cells carry a one-line gloss of their odd syntax ("`\d` is any digit, `+` is one or more", "`&` keeps what two sets share"), so A and B could read code they couldn't have written. E saw "nothing given was a surprise, because every one had a hand-typed one-case version nearby": Step 13's four typed lines are the body of the given seven-report loop.

**The records and their people stay in view.** Council minutes, a records portal, a picture of a table as "soft enclosure", Step 13's "what would you need before calling that a pandemic effect?" (B), and Step 6's `verify=False` question, "the best ethics question of the week" (B). The microsprint on joins prints counts, not words, because the other joins are members of the public's names. Motivation is the highest-rated part of the week (mean 4.2).

## Where it falls short, ranked

No persona found a privacy problem: the one output that joins a name to something (Step 8's microsprint, "A-F" and a council member's surname) names a public official, and the microsprint deliberately prints counts for the rest. The wrong-result problems come first. After them, items are ranked by how many personas hit each, how badly, and whether it stopped A or B.

1. **"Line 5" in Step 12 is the sixth line, and the wrong one looks right.**
   - **Who:** A, C, D and E typed `ocr_lines[4]` first; B typed `[5]` and flagged it.
   - **What happened:** cell 100 says "print how many lines, and line 5, 2021's". Counting from 1 gives `ocr_lines[4]`, which prints 2020's row (`2020 7,761,028 7,370,943 …`), a plausible row with nothing to flag it. The key's `ocr_lines[5]` is 2021's. The deck's "Step 12: line by line" says "Line 5 is 2021's row again", and cell 110's Discuss says "line 5 is the same row". Step 4's microsprint had just numbered pages "from 1".
   - **Why it matters:** the step's point is comparing the same row read twice; with 2020's row the `7,608.759` misread isn't there to find, and a student concludes OCR was fine (C).
   - **Proposed fix:** lab key cell 100: "`ocr_lines[5]`, the line at index 5 (the sixth, since lists count from 0), 2021's"; the same words in the deck frame "Step 12: line by line" and in cell 110's Discuss. (C's alternative, a filter on lines that start with "2021", returns five lines, one per category, so it needs "the first of them" too.)
   - **Status:** verified: the prompt, the frame and the Discuss as quoted; OCR of Exhibit 3 with Tesseract 5.3.4 and `--psm 6` gives 43 lines, `[4]` 2020's row and `[5]` 2021's; lines starting "2021" are at 5, 13, 21, 29 and 37.

2. **The lab's join repair does nothing, or harm, on the files students pick for the exercises.**
   - **Who:** B, D, E; C used both December 2022 files and reported that its function "works": it misses the same breaks there.
   - **What happened:** Exercise Step 3 asks for a cleanup function and a passage "before and after". Students build it from Step 8's four given repairs (cell 60). The second repair, `\b([A-Z]{1,2})\n(?=[A-Za-z])`, rejoins words split after one or two capitals ("M" / "ayor"), the way the December 2024 minutes break. Other years break differently:
     - in both December 2022 minutes, words split after several lowercase letters ("Counci" / "l Members present"), and the repair leaves them; on 2022-12-15, page 1's before and after differ only in spaces (B, E). B, C and E each chose a December 2022 file from the book's folder.
     - on the December 3, 2019 minutes, a stray "I" on its own first line becomes "ICITY OF BOULDER" (D).
   - The Step 8 microsprint checks the repair on 2023-12-07, which breaks the same way as 2024, so it passes quietly (E).
   - **Why it matters:** a student submits a before/after that shows nothing changed, or a new error, and can't tell why. B: "I would have submitted a cleanup that visibly does nothing." This is the week's lesson (check a repair on the next file) failing on the graded work.
   - **Proposed fix:** lab key, Step 8's microsprint (cells 63–65): offer `council-minutes-2022-12-15.pdf` as a second `check_file`, so that a class sees the repair miss; and one line in cell 66's Discuss: "on some years the break comes mid-word, after lowercase letters; pdfplumber (Step 7) doesn't break these words, so changing tool can beat patching the pattern" (B). Optional, chapter: the same sentence in "Cleanup Strategies".
   - **Status:** verified by running cell 60's four repairs on the book's copies (hashes checked against its manifest): "Counci\nl" survives in 2022-12-01 and 2022-12-15 and in neither 2023 nor 2024 file; 2022-12-15's page 1 is unchanged apart from spaces; 2019-12-03's page 1 starts `'I\nCITY'` and becomes `'ICITY'`; pdfplumber reads "Council Members present" whole on both 2022 files.

3. **The exercises ask for functions the lab never shows as functions, and a source the lab never shows how to find.**
   - **Who:** A, B, C, E.
   - **What happened:** chapter Exercise Step 3 says "Write a cleanup function"; Step 6 says "use `page_profile()`". The lab wrote both as straight lines (cell 28's loop, cell 60's repairs), and its only function is the given `get_saved_copy()`. A's first `def` had no `return` and failed with `TypeError: 'NoneType' object is not subscriptable`; C and E had to find `page_profile()` in the chapter. Exercise Step 1 says "find three PDF documents from one government source"; the lab downloads only from the book's folder, and none of A, B or C could tell whether the book's copies count. All five used them. Cell 122's map from exercises to lab steps says "Step 8's repair by hand and the four given repairs" for Step 3, which is the straight-line version.
   - **Why it matters:** the exercises are the graded part, and Step 3 is the first `def` a minimal student writes this week (A).
   - **Proposed fix:** lab key, cell 122: "Step 3's function is cell 60's four lines under `def clean_text(text):`, ending `return text`; Step 6's `page_profile()` is Step 4's loop as a function, in the chapter's 'What Kind of PDF Is It?'"; and "the book's `data/ch-09` minutes are a fine 'government source' for Step 1; to use another city's, read its `robots.txt` first". E would add a 3-minute given cell that wraps Step 4's loop in `def page_profile(path)`.
   - **Status:** verified: the chapter's exercise text at `3f9cf2c`; the key has one `def` (cell 9, repeated in the setup cells); cell 122's wording.

4. **Step 6's given download cell would send a class's requests to the city.**
   - **Who:** none ran it in class; found while checking A's note on cells 46 and 47.
   - **What happened:** cell 42's comment says "in class, only the instructor runs this step", and cell 41 says to write the cells and run them at home. But cell 47, the given download, depends only on cell 42 (also given), not on the typed cells 43–45, and doesn't repeat the warning. A student who runs the given cells by habit, as every other step asks, waits 30 seconds and then requests the December 2024 report from the city's portal. Cell 41 says the server stopped answering after 13 to 17 requests in a row. (A expected cell 47 to stop with a `NameError`; it doesn't, if cell 42 ran.)
   - **Why it matters:** forty students pressing Shift-Enter is the load the book's copies exist to avoid, and the city sees it.
   - **Proposed fix:** lab key, cells 46 and 47: start each comment with "In class, only the instructor runs this", as cell 42 does; or tag cells 42–47 so the students' copy leaves their code commented out. Deck: the Step 6 frames say the same.
   - **Status:** verified by reading cells 41–47.

5. **Parts 2 and 3 don't fit their days by the lab's own minutes.**
   - **Who:** A, B, C (pace 2); D and E found it about right for themselves (pace 4).
   - **What happened:** Part 2's headings add to 50 minutes of steps and 14 of microsprints, 64 against Wednesday's 50; Step 6, 5 of them, is the instructor's. Part 3's add to 40 against Friday's 35, before the 15-minute revision block. Monday holds about 10 minutes of concepts, the 10-minute exercise by hand and Part 1's 35, about 55. Part 2 is where the first regular expressions, the first POST, the first set arithmetic and the table settings arrive (A); B's Step 9 took 20 minutes, not 15.
   - **Why it matters:** when time runs out, the typed cells and the checks go first (B, C), and those are the parts that teach. A student behind at Step 8 meets Step 9 rushed, and is told to copy from the key (A).
   - **Proposed fix:** the minutes are the instructor's decision. The personas' candidates:
     - Cut Part 2's three microsprints to one, keeping Step 9's "another year" (B); or drop Step 8's (C). Item 2 argues for keeping Step 8's with a better file.
     - Show Step 6 in 2 minutes, or move it to "at home" in the step and on the slide (A, C).
     - Make the `--psm` microsprint take-home (B, C).
     - Say in each part's opening which cells are "if time" (A), and that Friday's revision block goes first (B).
   - **Status:** verified: the headings in the key sum to 30 + 5, 50 + 14 and 35 + 5; `docs/course-facts.md` gives about 50, 50 and 35; #204's description puts Monday's concepts at about 10 minutes. The personas' times are their own.

6. **"As Python stores them" doesn't say how.**
   - **Who:** A, B, C, D; E for cell 22.
   - **What happened:** cell 14 says "Look at its first 20 characters as Python stores them: `"\n"` is a new line". Every cell before it used `print()`, and `print(cover_text[:20])` shows blank lines, the same as cell 13. The key's cell is the bare expression `cover_text[:20]`, whose notebook output is `' \n \n \n \n \n \nREVENUE '`; `repr()` first appears in given cell 23. The deck's "Step 2: as Python stores it" shows the bare expression without saying why. Cell 22 has the same trap: `print(summary_page.chars[0]["text"])` prints a space that looks like nothing (E).
   - **Why it matters:** the Discuss question ("six runs of a space and a new line") needs the `\n` visible; a beginner who printed "learns nothing from the cell and thinks it is a repeat" (C). D got there only via R's `dput`.
   - **Proposed fix:** lab key, cell 14: "…type `cover_text[:20]` alone on the cell's last line, with no `print()`: Jupyter then shows it as Python stores it, quotes and `\n` included". The same note in the deck frame, and in cell 22's comment ("its text is a space: look at the whole dictionary").
   - **Status:** verified: cells 13, 14, 22 and 23 and the deck frame as quoted.

7. **The deck's week-level frames still describe the old week.**
   - **Who:** A, B, C, D, E.
   - **What happened:** "This week at a glance" gives the Monday exercise 20 minutes (its frame says 10), Wednesday "Steps 3 and 4 in Python … OCR on a picture of a table", and Friday "Finish the notebook, from OCR on"; the lab's Wednesday is Steps 5–10 and OCR is Friday's Step 12. Friday's "Today" says "Pick up where Wednesday stopped" and "Work in pairs, through both case studies". "After the lab" asks for `roll_call()` and `row_words()`, which only the companion notebook defines. "Chapter 9 pull requests are still open" says "No revision workshop this week", while the lab ends with one.
   - **Why it matters:** the at-a-glance is the frame a student plans the week from (C, E), and a student who starts from the lab looks for functions it never wrote (A, B, C, D).
   - **Proposed fix:** these are the instructor's frames, and #204's description already proposes wording for the at-a-glance and Friday's "Today". Add: "After the lab" names the companion notebook as where `roll_call()` and `row_words()` live; "Chapter 9 pull requests" matches the lab's revision block. "Due Sunday, Oct 18" and October 25 are this term's dates, which #204 lists for the next offering.
   - **Status:** verified in `slides/week-09/week-09.tex` at `50192aab`; `docs/course-facts.md` lists the at-a-glance and Friday's "Today" as "not yet changed".

8. **Step 9's count check compares nine with nine after four rows were dropped unseen.**
   - **Who:** C, D; E for the DataFrame cell.
   - **What happened:** cell 74 prints "12 rows before, 13 after"; Step 10 then says "the page shows nine" and `len(summary_df)` prints 9. The four rows in between (three header rows and a blank spacer) are removed by `dropna()` inside given cell 75, with `iloc[:, [1, 3, 4]]` picking columns from rows the student never sees. A reader of 12 and 13 "would think the fix added a row, not that it recovered one" (D).
   - **Why it matters:** C, from Excel, would look at the raw table before deleting rows; "a check that compares nine with nine after I deleted the rows that did not fit is weaker than it looks."
   - **Proposed fix:** lab key: one typed line before cell 75, `print(len(fixed_rows), "rows;", fixed_rows[0])`, so students see the header row and the eleven columns (C, E); and a given line after it, `print(len(fixed_rows) - len(summary_df), "rows dropped")`.
   - **Status:** verified from the key's outputs: `fixed_rows` has 13 rows and `summary_df` 9.

9. **`table_bottom = 395` is handed over, though the deck says "You choose".**
   - **Who:** C, D, E.
   - **What happened:** cell 73's prompt gives the number. Cell 70 prints only the totals row's top (380.2). The window that works is narrow and nothing prints its edges: the totals row's `bottom` is 391.2 and the footnote's top 397.7; 385 and 389 return 12 rows, silently dropping the totals row again, and 392 to 397 return 13.
   - **Why it matters:** the one decision a person makes in the table fix is made for them, and the microsprint's other year needs it made again (C, D, E). D's and E's confidence ratings both name it.
   - **Proposed fix:** lab key cell 70: also print `found[0]["bottom"]`; cell 73: "table_bottom: a number between that bottom and the footnote's top, about 397". Deck: the same on the Step 9 frames.
   - **Status:** verified by rerunning cells 71–74 with 385, 389, 392, 395 and 397, and reading the words below the totals row.

10. **Step 14 asks how the tax changed from 2019 to 2024, and nothing frames the answer.**
    - **Who:** C, D.
    - **What happened:** the series is nominal dollars, its "Total" row includes audit revenue ($2.9 million of 2024's $173.9 million), and 2024 is printed only once, so it hasn't yet been restated by a later report. The lab never computes 2019 to 2024; C did: about +22.5%. Step 14 asks "what lets you trust the figures enough to put eight years side by side?", and the lab supports only the printings check. The key's own answer (cell 123) ends "not adjusted for inflation", but the question doesn't ask for it.
    - **Why it matters:** C "would put this chart in a deck"; a statistician reads "trust" as "comparable across years", not "copied right" (D).
    - **Proposed fix:** lab key, cell 122's third bullet: ask for the 2019-to-2024 change and one sentence on what the series can't say (nominal dollars, audits included, 2024 not yet restated); cell 121's Discuss: "What would you divide by before saying sales tax rose in real terms?" (D).
    - **Status:** verified: 173,908,431 / 141,954,650 is +22.5%; 2,259,170 + 643,062 = 2,902,232 in cell 75's output; cell 119 lists 2018–2023 as printed twice.

11. **The checks are never shown failing.**
    - **Who:** D; B and C on the one-dollar gap.
    - **What happened:** cell 84 prints `{'ytd_2023': 0, 'ytd_2024': 1}` with no tolerance, so a student decides by eye that 1 passes; B and C wondered whether it was a missing row. The chapter's `check_summary(table, tolerance=5)` runs on the default table too and prints `['expected 9 rows of figures, found 8', "no row labeled 'Total Sales and Use Tax'"]`; the lab dropped that run.
    - **Why it matters:** "run it on the broken table and see it fail" is how D would trust a check before a hundred reports.
    - **Proposed fix:** lab key, Step 10: one given line that counts `default_rows` beside the fixed table (or the sums on it), so the check goes red; and in cell 84's comment, "a gap of a dollar or two is the report's rounding".
    - **Status:** verified: cell 84 and the chapter's "Checking an Extraction".

12. **Small given steps hide the cause behind a number.**
    - **Who:** A, B, D.
    - **What happened:**
      - Step 10's roll call reports recall 0.56 and four names missed, but the cause, the members' list wrapping onto a second line, is never printed (A).
      - Step 12's row crop holds only the year and four of fifteen figures, which the step doesn't say, so "does every figure match?" checks a quarter of the row (B).
      - Step 13's given loop uses `page.search(r"(20\d\d) +(20\d\d)")[0]["groups"]`, which no typed cell shows (A).
      - The Step 9 microsprint gives each student one year; the class's answer is only the sum of what pairs share (D).
    - **Proposed fix:** lab key: a typed line in Step 10 printing the two lines after `present:` in `plain_text`; "the crop holds the year and the first four figures" in Step 12's text; one typed line before cell 117 printing the `groups` on the 2024 page; optionally a given loop over the five years after the Step 9 microsprint.
    - **Status:** verified by reading cells 51, 86, 97–98, 117 and 80.

13. **A scanned text layer undercounts a topic word, and nothing asks how much.**
    - **Who:** D; B saw it on the same file.
    - **What happened:** counting "housing" for Exercise Step 4, D and B got 0 on the December 3, 2019 minutes, a scan whose text layer holds the word only as a fragment. D's own Tesseract run found it once, and "motion passed" five times where the layer has it once.
    - **Why it matters:** an exercise that counts a word per document gets a number biased by the document type, and Exercise Step 7 asks whether the PDF or the regex is the culprit.
    - **Proposed fix:** lab key: a Discuss question in Step 12 after cell 109, or a 5-minute microsprint: OCR one page of the 2018 minutes and count one common word in both texts. Item 5's minutes argue for the Discuss question.
    - **Status:** partly verified: the 2019 text layer has no "housing" and one "Housi" fragment. The OCR counts are D's.

14. **`get_saved_copy()` would cache an error page as a PDF for good.**
    - **Who:** E.
    - **What happened:** cell 9's function (repeated in cells 39 and 92) drops the chapter's `timeout=60` and `raise_for_status()`, and doesn't check `%PDF-`. A failed download is saved as the `.pdf` and reread on every later call; `PdfReader` then fails with a message that doesn't name the cause. Cell 10's Discuss asks about exactly this, and cell 48's admits the missing `raise_for_status()`.
    - **Proposed fix:** lab key, cells 9, 39 and 92: add `response.raise_for_status()` before `write_bytes`, as the chapter does. One line; it makes Step 1's "look first" a habit.
    - **Status:** verified: the three cells and the chapter's `get_saved_copy()`.

15. **Step 13's first prompt says "page 2", where Step 3 said `pages[1]`.**
    - **Who:** B.
    - **What happened:** cell 112: "page 2 of `pdfplumber.open(report_2024)`". B typed `pages[2]`; the cell printed `False`, which B read as "print and move on", and cell 113 stopped with `IndexError` on `search(...)[0]`, which names no page. Step 3's cell 19 says "its pages[1], the second page".
    - **Proposed fix:** lab key, cell 112: "`pages[1]`, the second page; it should print `True`".
    - **Status:** verified: cells 19 and 112.

### Corrections

Claims in the reviews that turned out wrong or inexact, and what this document does with them:
- **A: "Part 1 has slack" (35 minutes of headings in a 50-minute class).** Monday also holds about 10 minutes of concepts and the 10-minute exercise by hand, so Monday is about 55 minutes, a little over. D's "Part 1 is a little slow" is about D's own speed. Item 5 keeps the over-time days, not a slack one.
- **A: cells 46 and 47 would stop with `NameError` without the typed cells.** Cell 46 would (`folder`); cell 47 would not, since it needs only given cell 42, and it sends a request to the city. That became item 4.
- **"One or two characters" between pypdf versions (B, C, E).** Mostly, but page 14 of the 2018 report is 3,952 against the chapter's 3,964, twelve fewer. Still versions, not mistakes; see "Small things" for a line in Step 4.
- **B's 98 and E's 34 "breaks inside words".** B's count (a lowercase letter, a new line, a lowercase letter) also counts ordinary wrapped lines: the December 2024 minutes, where the repair is right, give 48 by the same count. Item 2 rests instead on the specific breaks that survive and on page 1 being unchanged.
- **C's fix for item 1, a filter on lines starting "2021",** returns five lines, one per category; it needs "the first".
- **E: the exercises' map says "Step 6's `%PDF-` check", and the check is Step 1's.** Partly: Step 6's given cell 47 also prints the download's first five bytes. "Step 1's and Step 6's" would be exact (Small things).
- **D: "Rec MJ Additional 3.5%" is "a new item in the base".** Not checked across years; dropped from item 10, which rests on nominal dollars, audits and the unrevised last year.
- **The checkpoint 404 (all five)** is reported by all as a block, and it is one until #204 merges: it is under "Environment blocks" and "Check right after merging #204", not ranked.

## Disagreements

- **Too slow, or about right.** A, B and C rate pace 2 and put Part 2 at 80–100 minutes; D and E rate it 4 and put it at 60–75. All five agree Part 2 is the full one. The split follows typing speed and regular expressions: E "never had to design anything", while A "could run but not explain" Steps 9 and 13's given cells. The microsprints are where the two groups part: A, B and C would cut them; D and E would *add* one each (a third file for the join repair; an OCR-against-layer count). Item 5 leaves the choice with the instructor; item 2's file and item 13's Discuss question are the cheap versions of D's and E's additions.
- **How much to give.** A and B are content with the given cells ("I could not have written the loop in Step 4 … and the lab never pretends I could", B). E finds Steps 9, 10 and 12 leave "a student typing one line per cell" and would have students choose `table_bottom` and look at `fixed_rows[0]` before the `iloc`. C and D want the same two things for a different reason, to see what the checks compare. Items 8 and 9 add two typed lines that serve both.
- **Fixing "line 5".** A, B, D and E would say "index 5"; C and D would rather find the row by its year, "a better habit" (D). Saying the index is the smaller change, and keeps the slide's code.
- **What to do with a failed repair.** B: change tool (pdfplumber), not the regex. D: measure the repair's error rate before a hundred files. E: give a microsprint file where it fails. Item 2 does E's and B's; D's is the Discuss question already in cell 66.
- **Difficulty.** A, B and C rate it 3, D and E 2. The typed cells were fair for all five; the difficulty is in the exercises (a first `def`, choosing a source) for A and B, and in reading given cells for C.

## Ratings

Each on a scale of 1 to 5. For difficulty, 5 is hardest for that persona's background.

| | A | B | C | D | E | Mean |
|---|---|---|---|---|---|---|
| Clarity of motivation | 4 | 5 | 4 | 4 | 4 | 4.2 |
| Pace | 2 | 2 | 2 | 4 | 4 | 2.8 |
| Difficulty for my background | 3 | 3 | 3 | 2 | 2 | 2.6 |
| How much I learned | 4 | 4 | 4 | 4 | 4 | 4.0 |
| Confidence I could do this on my project | 3 | 3 | 3 | 4 | 3 | 3.2 |

What holds the confidence down: A can't yet find PDFs politely or write the cleanup alone; B can't find a table in an unseen PDF or fix a cleanup that does nothing (item 2); C couldn't adapt the table fix or the regex repairs without the chapter (item 9); D would need to derive `table_bottom` and handle tables whose rules change by year; E isn't confident on a second, different PDF, "because the repairs and the table fix were each written for one file."

## Small things

Lab (`labs/week-09/lab-09-key.ipynb`):
- Cell 31 calls the Step 4 microsprint "a short version of Additional Exercise 5", the graduate extension; an INFO 4617 student can't follow it (C).
- Cells 77 and 118 say "the table the key's run saved on 2026-11-17"; "the saved copy of the table" is enough for a student (C).
- Cell 77 has two commented lines; removing the `#` from only the second gives `NameError: name 'data_base' is not defined` (A).
- Cell 59: "is "P age 1" in each of them?" doesn't name the two (D).
- Cell 67: "The fix, given: the column edges yourself" reads as a fragment (E).
- Cell 33: a page with no characters and no image would be routed "born-digital"; one sentence (E).
- Step 4's text: one line that a newer pypdf counts a few characters differently from the chapter (C, E).
- Cell 81's Discuss asks which Step 10 check would catch `table_bottom = 385`; the count cell uses the 395 table, so a student can't run it without redoing the cells (A).
- Cell 82 links precision and recall but never defines them in a line (A).
- Cells 46 and 47 need a "skip if you didn't run 43–45" (A); item 4's fix covers it.
- Cell 41: one sentence of why, "how a reporter would fetch a whole folder of a city's records" (B).
- Cell 4's Discuss ("who reads this one, now that the request goes to GitHub?") has no answer in the lab; the honest one is "nobody" (E).
- The email address is typed in three setup cells (3, 38, 91); "the same address as Monday" (D, E).
- Cell 122's map: "Step 1's and Step 6's `%PDF-` check" (E; see "Corrections").
- Cell 120's title says 2017–2024 from seven reports; 2017 appears only as the 2018 report's earlier year (D).
- Cell 2 names only `ModuleNotFoundError`; a damaged install fails another way (B; this machine's problem, noted for completeness).
- Cell 11: "double-click it in Jupyter's file browser" opens a tab, not a viewer, on some machines (C; not tested).
- Found while verifying: the key's opening note compares pypdf 7.1.0 with "6.21.2", where the chapter prints 6.20.1, and says "one or two characters", where the 2018 report's page 14 differs by twelve.

Deck (`slides/week-09/week-09.tex`):
- "Four steps" ends "Wednesday and Friday: steps 3 and 4 in Python", the pathway's steps, beside a lab whose Steps 3 and 4 are Monday's (found while verifying).
- Case study frames say "the chapter's `roll_call()` reads both"; item 7 covers where it lives.

Chapter (`ch-09-pdfs.qmd` at `3f9cf2c`):
- Exercise Step 4: a hint, "if you get 0 on the first document, search the PDF in a viewer before changing the pattern"; C and E both picked dollar amounts first and got 0 in most of their files (C).

## Suggested next step

**Fix first, on #204's branch.** Each is small and changes none of what the week teaches:
1. **Item 1:** "`ocr_lines[5]`, the line at index 5 (the sixth)" in cell 100, the deck's "Step 12: line by line" and cell 110's Discuss.
2. **Item 4:** "in class, only the instructor runs this" on cells 46 and 47, or keep Step 6's code out of the students' copy.
3. **Item 6:** "on the last line, without `print()`" in cell 14 and its frame; the same note in cell 22.
4. **Items 3 and 2, the exercises' bridge:** cell 122 says what Step 3's function and Step 6's `page_profile()` are, and that the book's minutes are an acceptable source; Step 8's microsprint offers `council-minutes-2022-12-15.pdf`, and cell 66 says pdfplumber doesn't break those words.
5. **Items 8, 9 and 15, three lines:** print `fixed_rows`' length and first row before cell 75; print the totals row's `bottom` in cell 70 and let students choose `table_bottom`; "`pages[1]`" in cell 112.

**Check right after merging #204.**
- `https://raw.githubusercontent.com/cuinfoscience/INFO4617-Fall2026/main/labs/week-09/data/summary.csv` and `…/totals.csv` answer 200 (today: 404 on `main`, 200 on the branch), then run Part 3's setup (cells 91–92) in a fresh kernel.
- Optional (C, D): a comment in cell 92, "a 404 here means the file isn't published yet; run Wednesday's Step 9 cells instead".

**Needs the instructor's decision:**
- **The minutes** (item 5): 64 against Wednesday's 50 and 40 against Friday's 35, and which microsprints or steps become "if time" or homework.
- **The week-level frames** (item 7): the at-a-glance, Friday's "Today", "After the lab" and "Chapter 9 pull requests", which are yours; #204's description has proposed wording for the first two.
- **How much more to type** (items 8, 9, 12): the personas split on given against typed; the lines above are the smallest version.
- **The series' framing** (item 10) and **a check shown failing** (item 11): a sentence each, but they change what Step 14 asks.
