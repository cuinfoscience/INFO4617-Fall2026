# Review: week 13, AI APIs as Data Tools

**What was reviewed:** week 13's lab (`labs/week-13/lab-13.ipynb`, with its key), deck (`slides/week-13/week-13.tex`) and chapter 13's Recommended Exercises, as students meet them.
- **Course repository:** `main` at `efc1e36711c1f2e4ae3fcbf00c4cfa78cd3709ac`, with week 13's revisions (#195 and #202) merged.
- **Textbook:** `ch-13-ai-apis.qmd` and its companion notebook at `main`, `3f9cf2cef801181236c9cceaf71f3b63c3ad2491`.

**When:** 2026-11-17, the day after Part 3 was taught.

**Method:** five anonymous composite personas, each a kind of student this course has, reviewed the week independently ([`README.md`](README.md) has the method in full). Each read the chapter and the slides, typed and ran its own code for every lab step from the students' copy, made the mistakes its background makes, attempted the Recommended Exercises, and opened the key only after an honest try. Each review is a **steel man**: it first makes the strongest case for the materials as designed, and only then says where they fall short for that student. This document puts the five together. Every ranked finding was then checked against the repository and the textbook, and is marked **verified** (with how) or **reported, not verified**.

## Who reviewed

| | Degree and major | Python and data background | Interest | Skill |
|---|---|---|---|---|
| A | BS senior, Information Science | One intro Python course; spreadsheets | Qualitative and design: online communities, UX | Minimal |
| B | BA junior, Journalism and Communication | No Python before this course; strong with public records and Excel | Data journalism, local government | Minimal |
| C | BS senior, Business Analytics | Excel, some SQL, a little pandas | Quantitative analytics: markets, customer data, dashboards | Minimal to moderate |
| D | MS first year, Data Science (BA in Statistics) | Fluent in R, moderate pandas; regression and sampling | Quantitative: measurement and validity | Moderate |
| E | MS first year, Information Science (BS in Computer Science) | Moderate Python, git; little data analysis | Design and tools: automation, APIs, building things | Moderate |

## What each completed

The lab has Steps 0–14 (Step 14 optional) and five microsprints. Every persona typed Steps 1 and 2 but couldn't send them, and ran Steps 3–5 on the book's saved Markdown of the same report (see "Environment blocks").

| | Lab steps finished | Blocked | Recommended Exercises | Needed the slide or the key for |
|---|---|---|---|---|
| A | 0, 3–10, 12–14; all five microsprints | 1–2 (no Datalab key); 11 (Wikipedia 429; went on from the saved HTML) | Steps 1–6, on three saved leads as stand-ins | The slide for five typed cells; the key for Step 11's two outputs |
| B | 0, 3–14, Step 11 live; all five microsprints | 1–2 | Steps 1–6: one lead live, two saved leads as stand-ins | The slide for cells 11, 21, 89 and 100; nothing covers cell 114 |
| C | 0, 3–14 (Step 11 after one retry each); all five microsprints | 1–2 | Steps 1–6, on three saved leads; its function untested live | The slide or the key for cells 11, 21, 89, 100 |
| D | 0, 3–10, 12–14, with their microsprints | 1–2; 11's two requests (went on from the saved HTML) | Steps 1–6, on three saved leads; its function not run live | The key once, for `session.json`'s path |
| E | 0, 3–10, 12–14 | 1–2; 11's `parse` request (went on from the saved HTML) | Steps 1–5 run on three saved leads, Step 6 written; its function unverified | Nothing to unblock; compared cells 89, 104, 114 afterwards |

**Estimated time for a real student of that background, in minutes** (the lab's own step minutes in the last row):

| | Reading | Part 1 | Part 2 | Part 3 | Step 14 | Exercises |
|---|---|---|---|---|---|---|
| A | 105 | 65 | 65 | 55 | 20 | 105, of which 40 finding which cells to run |
| B | not given | 60 | 60–65 | 50 | 15 | 105; 75 without Wikipedia's refusals |
| C | not given | 55 | 52 | 50 | 12 | 70; 50 with Wikipedia answering |
| D | not given | 55; 40 with a working key | 70 | 75 | 15 | 120 with its own validity checks; 75 doing only what's asked |
| E | 50 | 35 with a working key | 60–70 | 75 | 20 | 90 live; 40 on stand-ins |
| **The lab** | | **58** | **54** | **44** | **13** | none given |

## Environment blocks

These come from the review machine, not from the materials. They are kept apart so that none is read as a flaw in the week. Where a block exposed a missing way round it, that is a finding below (items 7 and 8), and says so.

- **No Datalab key (all five).** Steps 1 and 2 were typed and not sent. Nobody saw a ticket, a status or a cost.
- **Wikipedia answered 429.**
  - In Step 11: refused A and D on both requests, twice each, and E's `parse` request twice; answered C on the second try, about 70 seconds later; answered B at once.
  - In the exercises: refused all five at least once (B: 4 of 8 requests answered). `retry-after` ran from 1 to 30 seconds. That is why the exercises ran on stand-ins from the lab's saved `leads.csv`, and why no persona's own `get_lead()` function ran to the end against Wikipedia.
- **`import pdfplumber` fails on the review machine** (A, C, D), so they commented it out of the companion notebook's first cell. The Wikipedia path of the exercises doesn't use it.
- **Notebook kernels died during pauses** (A once, B twice). Both rebuilt their variables without sending any model request again.
- **`getpass()` had no input box** in D's runner, so D skipped cell 4.
- **Waiting on shared free models.** OpenRouter never refused anyone. Dots took 59 to 122 seconds, which may be the day, not the lab. Each persona ran Part 2's two seven-report loops once only, by the review's rule.

## The strongest case for the week as designed

**Every big request is preceded by a small one whose answer the student can check by reading.** All five said so, in nearly the same words. Step 1 converts one page before fifteen. Step 8 sends one sentence whose answer is in the sentence, then asks for one field, then sends the page. Step 12 embeds three sentences before 116 leads. A, B and C each named the same ten lines as the best of the week: the sentence comes back as `'173908431'` in quotes, `plain_text == 173908431` prints `False`, and the one-field schema turns it into a number. A, B, C and D each wrote their own three sentences and got the split the step promises (0.75 to 0.96 for the paraphrase, 0.02 to 0.07 against the unrelated one), so the 116-lead table was believable before they saw it. For D, a known answer, then a check, then the harder task is "the order I would pick myself".

**The week's claim, that valid JSON can still be wrong, is something students watch happen.** The Step 3 microsprint prints Datalab's description of Chart 8, which calls \$1,262,688 the largest slice and then names a larger one. B called it the best five minutes of the week, and the frame "What Datalab read, and what its model wrote" gave B words for it that work on any document a model has touched. In Step 8, A, C, D and E got both totals right and the year 2025. In the Dots microsprint, A, C and D got the row above the totals. Then Step 10's second loop, with the schema in the instruction, turned each persona's table from three or four rows right in every field into seven of seven, in a third to a fifth of the time. To D, with the one change named, "it reads almost like an intervention with a control". The frames "One way it goes wrong" and "Same request, different answers" put the evidence on screen instead of asserting it.

**The given cells are placed where a beginner would have drowned, each straight after one case typed by hand.** A, B and C listed the same ones: the regular expression in `split_pages()`, the polling loop, `check_sums()`, `extract_totals()`, both loops, the scaling to length 1, the plot. The slides ask students to find in them the lines they just typed, and B could. The setup cells teach the pattern the typed cells need: `dict(HEADERS)` and one added key is what Step 1's `one_page` asks for, and B typed it without help. For E the given cells "hide only boilerplate", and for D the plain calls map straight onto `httr` and `jsonlite`. Printing `error` first caught B's missing brackets in plain English, and D's `data=` for `json=`.

**Each part starts fresh, from saved files, and that is the only reason the review got past two services that refused it.** The saved Markdown, `leads.csv` and `lead-vectors.npy` meant a missing key and Wikipedia's 429s cost two steps, not the week (A, C, E). The Discuss boxes prepare students for failures before they meet them: B recognised `JSONDecodeError: Expecting value` in the exercises because Step 11's box had asked what a plain-text 429 would do. The care for people is built in: keys are never printed, page 1 is never printed, and the first Discuss box of each part asks who sees what is sent (A).

**The exercise is the right size.** Three texts, one baseline, and a report that asks what the number can't show (A). It reuses `lead_text()` and `embed_text()`, so it asks for a small recombination, not something new (E). A called Step 13's list, which maps each exercise step to a lab step, the most useful paragraph in the notebook.

## Where it falls short, ranked

Privacy and wrong-result problems come first. After them, items are ranked by how many personas hit each, how badly, and whether it stopped A or B. Cell numbers are the key's (`labs/week-13/lab-13-key.ipynb`); the students' copy is made from it.

1. **The typed cell that keeps contact details off the screen is the one a beginner can't write.**
   - **Who:** A, B, C.
   - **What happened:** Step 3 says never to print page 1, and that Exhibit 3's note gives the tax office's contact details. Slicing page 15 from its first `|` is what skips that note. Cell 21's prompt says `exhibit: pages[14] from its first "|"` and names no method. All three first wrote `pages[14]["|":]` and got `TypeError: slice indices must be integers or None or have an __index__ method`. B's second try, `pages[14].split("|")` and printing the first pieces, printed the note, with a phone number and an email address. Only the slide's `exhibit_start = pages[14].index("|")` worked. Cell 11 (Step 1) has the same wording.
   - **Why it matters:** the lab's rule about contact details rests on a cell that fails in the direction the step warns against. The fallback a beginner reaches for, `print(pages[14])`, prints them too.
   - **Proposed fix:** lab key, cells 11 and 21: make the two slicing lines a given cell (`exhibit_start = pages[14].index("|")`, `exhibit = pages[14][exhibit_start:]`, with a comment saying this is what skips the note), and leave the printing typed. Cell 21 also has a `for` loop in a typed cell, which the lab's own rule gives. Deck: mark the matching lines of "Step 1: what came back" and "Step 3: a picture of a table" as given.
   - **Status:** verified. The prompts of cells 11 and 21 name no method, in the key and in the students' copy. In the book's saved 2024 Markdown, the 295 characters above page 15's first `|` match the patterns of an email address (twice) and a phone number (once), counted without printing them; so does the first piece of `split("|")`. From the first `|` on there are none. That Step 1's one-page Markdown starts with the same note is reported, not verified: no Datalab key.

2. **Step 10's table reads "True True" for a row whose year or month is wrong.**
   - **Who:** A, B, C, D, E.
   - **What happened:** both given loops (cells 73 and 75) add `prior_ok` and `current_ok` and nothing else. In each persona's first loop, rows with the right totals carried a wrong date: 2024 as 2025, and 2018 or 2020 as January of the next year. Read by its columns, the plain instruction scored 5 or 6 of 7; on all four fields it scored 3 or 4 of 7 (A: 6 against 3; B: 5 against 3; C: 6 against 4). B counted five reports right: "Two of those five would have put a wrong year in my story." The Discuss box (cell 76) then describes the key's run, "4 of 7 reports, 2021 to 2024", which matched nobody's table; the chapter says five of seven; and the box asks students to print a wrong report's summary page, which the loop doesn't keep.
   - **Why it matters:** this is the mistake the week is about, made by the week's own table. The step's finding, that the schema in the instruction fixes the year and month, is in fields the table doesn't flag: by the `_ok` columns the two loops differ by one report.
   - **Proposed fix:**
     - Lab key, cells 73 and 75: add `year_ok` (`report_answer["year"] == int(report[15:19])`) and `month_ok` (`== "December"`), and print how many rows are right in every field.
     - Lab key, cell 76: say "in your run" before "in the key's run", add "your wrong rows will differ", and give the one line that prints a report's summary page.
     - Deck: "Step 10: seven reports, given" says "check both totals".
     - Chapter: the "Seven Reports" loop has the same two columns, and its printed table has the same `2025 … True True` row. Change it in the same pass.
   - **Status:** verified. The key's own first table (cell 73's output) shows `revenue-report-2024-12  December  2025 … True  True`, and the chapter's printed table shows the same row. Cell 65 (Step 9) does print the year and month, but as bare values, with no `True` or `False`. Each persona's counts are from its own run and aren't reproducible.

3. **The similarity plot has no reference line, lead length drives much of it, and one saved lead carries a stray note.**
   - **Who:** C, D; E reached the same doubt in its exercise report.
   - **What happened:** C and D each scored the five current leads against each other: 0.39 (Trump and Harris) to 0.58 (Obama and Biden). The earliest leads of four of the five articles score 0.41 to 0.53 against their own article's current lead. So a 2005 lead is no closer to today's than one politician's biography is to another's: on this plot "unrelated" sits at about 0.4 to 0.6, not at 0. Within an article, similarity to today's lead tracks the lead's word count: a correlation of 0.90 for Obama, 0.94 for Trump, 0.86 for Biden, 0.74 for Clinton, 0.17 for Harris. Separately, the saved Trump 2006 lead begins "For the champion Australian racehorse, see: The Trump", 9 of its 35 words, a note the cleanup missed. C reports that without it the point moves from 0.407 to 0.449, which turns the plot's 2005–2006 dip into a rise.
   - **Why it matters:** someone reads 0.48 on a chart as "about half the same". The chapter's own exercise says "One similarity means little on its own" and asks for a baseline; the lab's plot is read without one. The Discuss box tells students the jumps aren't all events, and gives them no way to see it.
   - **Proposed fix:**
     - Lab key, after cell 99: one typed line, `print(round(today["Barack Obama"] @ today["Joe Biden"], 3))`, and a sentence that different people's current leads score 0.39 to 0.58. A dashed band in the given plot (cell 101) would show it.
     - Lab key, cell 103's microsprint: print the `words` of the two years beside the jump.
     - Data: `leads.csv`, here and in the textbook's `data/ch-13/wikipedia/`. Either remove the note from the Trump 2006 row and embed that one lead again, which changes `lead-vectors.npy` and one value in the chapter's table and plot, or keep it and name it in Step 11's Discuss as the answer to "what might still come from today". The instructor's decision.
   - **Status:** verified from `leads.csv` and `lead-vectors.npy`: the 0.389 to 0.584 range, the five correlations, the same-article and different-article medians D gives (0.729 and 0.343), and the Trump 2006 note, the only one of 116 leads that starts with one. One correction: Clinton's early leads score 0.58 to 0.69, above the range, so "no closer than another politician" holds for four articles of five. The 0.449 is reported, not verified: it needs an embedding request.

4. **The Recommended Exercises have no place to start: the functions they name live in cells that send their own requests.**
   - **Who:** A, B, C, D, E.
   - **What happened:** Step 2 says to use `lead_text()` and Step 3 `embed_text()`, as if they existed. In the companion notebook, 58 code cells sit above the exercises, and nothing says which to run.
     - Starting at the exercises gives `NameError: name 'os' is not defined`.
     - The cell that defines `lead_text()` ends with `lead = lead_text(html)`, and stops at `name 'html' is not defined`.
     - The cell that defines `embed_text()` ends with `vector = embed_text(lead)`, and stops at `name 'lead' is not defined`.
     - `EMBEDDER` is set in the middle of a cell that first asks Wikipedia for all of "Joe Biden". When Wikipedia answers 429 the cell stops before the line, so a refused chapter example blocks the exercise (A, E).
     - "Run All Above" would pay Datalab twice and send about 25 free-model requests, the two seven-report loops among them (B, D).
     - Pasting lab code gives `name 'API' is not defined`: the lab calls the address `API`, the chapter `wiki_api`. The two also write the revision request in two shapes, and mixing them gives `AttributeError: 'list' object has no attribute 'values'` (A, B, C).
   - **Why it matters:** this is the graded part of the week, done at home. A spent 40 minutes before embedding anything, and B 20. The setup is harder than the exercise.
   - **Proposed fix:**
     - Chapter, "Recommended Exercises": one given cell above Step 1 that sends nothing, holding the imports, `HEADERS`, the key check, `openrouter_headers`, `wiki_api`, `EMBEDDER`, `lead_text()` and `embed_text()`, with a line saying "run this, not the cells above".
     - Lab key, Step 13's list: point to that cell, and say that the lab's `API` is the chapter's `wiki_api` and that the chapter's request uses `formatversion=2`.
     - `docs/plans/2026-10-21-recommended-exercise-notebooks.md` proposes standalone exercise notebooks, which would settle this for every chapter.
   - **Status:** verified in the companion notebook at the reviewed commit. The helpers are in cells 7, 9, 64, 68, 74 and 80; cells 68 and 80 end with the calls quoted; cell 74 sets `EMBEDDER` after a request and `raise_for_status()`; 25 of the 58 code cells above the exercises contain a `requests.get(` or `requests.post(` (C counted 28, with the cells that call the chapter's functions).

5. **No part fits its day by the lab's own minutes, and Part 2 adds minutes of waiting that print nothing.**
   - **Who:** A, B, C rated pace 2 of 5; D and E rated it 3, for the waiting.
   - **What happened:** the step headings add up to 58 minutes for Part 1 and 54 for Part 2, with 17 typed cells and 34 frames. Part 2 ran on a Friday, which has 35 minutes before the checkpoint. On top of that, Step 8's page took 24 to 30 seconds (one of D's requests took 88), Dots 59 to 122 seconds inside a 4-minute microsprint, the first loop 163 to 250 seconds and the second 51 to 66. The loops print nothing until they finish. E "nearly interrupted it twice"; B says a student like B restarts the kernel at about 90 seconds and loses Part 2's variables.
   - **Why it matters:** A, B and C type slowly, and they said what gets cut is Step 10 (A, C) and the Discuss boxes (B), which is where the lesson is. In a room, with everyone on the same free model, the waits will be longer.
   - **Proposed fix:**
     - Lab key, cells 73 and 75: `print(report)` as each answer arrives. Step 10's text: say the first loop takes about three and a half minutes.
     - Lab key and deck, "Today: Part 2": say what to skip on a short day. The personas' candidates: the Dots microsprint (A, B), Step 8's one-field round as a given cell (A, C), and the first loop's table loaded from a saved file with only the second run live (C, E). They disagree, and D rates Dots above the loops: see "Disagreements".
     - The minutes themselves are the instructor's decision.
   - **Status:** verified: the headings sum to 58, 54 and 44 minutes, 156 in all against `labs/AUTHORING.md`'s 135 (50, 50 and 35), and 169 with the optional Step 14 and its microsprint. Part 2 has 17 typed cells and Friday's section 34 frames. In a week with no cancelled class Part 3 falls on the 35-minute Friday, 9 minutes over. The waits are each persona's own run, not reproducible.

6. **Several typed cells can be written from the slide but not from the notebook.**
   - **Who:** A, B, C, D, E.
   - **What happened:** most prompts name the method (`dict(settings)`, `splitlines()`, `json.loads()`, "use `str()`"), so personas trusted these to be complete. None of the error messages points at the fix.

     | Cell | The prompt says | First tries, and what they gave | What it needed | Who |
     |---|---|---|---|---|
     | 11, 21 | `from its first "\|"` | item 1 | `.index("\|")` and a slice | A, B, C |
     | 82 | `action=query, titles="Barack Obama", prop=revisions` | typed as written: `NameError: name 'query' is not defined` | quotes round every value | A |
     | 89 | `the "lead" of leads' row for "Barack Obama" and year "2009"` | `and`: `ValueError: The truth value of a Series is ambiguous`. `&` without parentheses: `TypeError: unsupported operand type(s) for &: 'str' and 'StringArray'`. Without `.iloc[0]`: a one-row Series, not `True` | two named conditions, `&`, `.iloc[0]` | A, B, C, D, E |
     | 93 | `how many numbers the first holds` | `len(small)` printed 6 | `small["data"][0]["embedding"]` | A |
     | 100 | `Make its index (the years) integers` | `int(table.index)`: `TypeError: int() argument must be … not 'Index'` | `.astype(int)` | A, B, C |
     | 104 | `leads' "year" holds text: use str()` | compared with a number: `IndexError: single positional indexer is out-of-bounds` | `str(y)`, which the prompt does name | E |
     | 114 | `the text of session.json's last message` | `session[-1]["text"]`: `KeyError: 'text'`. Nothing says where the file is or how to load it | `requests.get(cmcp + "session.json", …).json()`, then `[-1]["received"]["result"]["content"][0]["text"]` | A, B, C, D, E |

   - **Why it matters:** in class the slide saves the student. At home, catching up after a missed day, the notebook is all they have, and A, B and C each said they would be stuck there. D and E each lost four or five minutes on cells 89 and 114.
   - **Proposed fix:** lab key: name the method in each prompt, as the others do (`is_obama`, `is_2009`, `&` and `.iloc[0]`; `small["data"][0]["embedding"]`; `table.index.astype(int)`). Quote every value in cell 82's prompt. Make the `session.json` line given: the slides have no frame for it.
   - **Status:** verified: each prompt read in the key and in the students' copy; the slide has `.iloc[0]` and `.astype(int)`, and no frame mentions `session.json`. The error texts are the personas' own.

7. **A refusal from Wikipedia shows up as `JSONDecodeError`, and Step 11 has no way round it.**
   - **Who:** A, D, E were stopped; C got through on a retry; B met it in the exercises.
   - **What happened:** the refusals are an environment block. The shape of the failure is the lab's: forty lines ending in `JSONDecodeError: Expecting value: line 1 column 1 (char 0)`, with 429 nowhere on screen. The Discuss box explains it, after the step. Monday's "Errors" box says "A `429` means a free model is busy", which is not this. The given cleanup cells (86, 87) need `soup`, and cell 89 needs `lead`, so everything down to the saved leads is dead until both requests work. The saved HTML that would carry a student on, `html/Barack_Obama_2009.html`, is in the lab's data folder and named nowhere; A, D and E each found it by looking.
   - **Why it matters:** the notebook itself says a room on one network draws 429s. A can't read a traceback beyond its last line, and this last line doesn't say what happened. D estimates the two requests "can eat 15 minutes" of a 50-minute class.
   - **Proposed fix:** lab key, Step 11: one sentence before the cells ("If a cell ends in `JSONDecodeError: Expecting value`, Wikipedia refused you: wait and run it again, or use the saved copy below"), and a given, commented cell like cell 97's that reads `wiki + "html/Barack_Obama_2009.html"` into `html`. That is the lab's own checkpoint pattern. D's alternative, a given cell with a `try`, is against the lab's rule of no error handling.
   - **Status:** verified: the file is in `labs/week-13/data/wikipedia/html/`; neither notebook mentions `html/`; cell 97 is the pattern. The key's own run was refused the same way: cell 86 is `not-run-live`.

8. **Part 1 has no saved path for a student whose Datalab request fails, and the key shows no output for those cells.**
   - **Who:** A, B, C, E.
   - **What happened:** the missing key is an environment block. But from Step 3 on, Part 1 needs only `check["markdown"]`, and every persona wrote its own stand-in from the saved file to go on. The notebook offers that copy only to Part 2. In the key, the five cells that send to Datalab (9, 10, 11, 15, 16) have no output, so "Fall behind? Copy the cell from `lab-13-key.ipynb`" gives code and nothing it printed. Nobody could answer Step 1's Discuss questions on the ticket, the page marker or one page's cost (C). With a wrong key, cell 9 prints `{"detail": "Invalid API key or access token."}` and the next cell dies with `KeyError: 'request_check_url'` (E); Step 4's Discuss covers that, three steps later.
   - **Why it matters:** a sign-up that didn't work, a mistyped key or a spent allowance stops a student at Step 1 for the whole of Monday, including the week's two best moments, Chart 8 and the sums.
   - **Proposed fix:** lab key: after Step 2, a given, commented cell, `# check = {"markdown": requests.get(saved + "revenue-report-2024-12.md", headers=HEADERS).text}`, "only if Datalab didn't answer". Under cell 9, one sentence: "If this prints `detail`, your key is wrong: use the saved copy below." Paste one real ticket and one finished status into Step 1's text, or run the five cells from a laptop (the plan of 2026-11-16 collects those runs in issue #197).
   - **Status:** verified: cells 9, 10, 11, 15 and 16 are tagged `not-run-live` and have no outputs, and Part 1 has no cell like cell 97. The 401 and the `KeyError` are E's run, not verified.

9. **The exercise asks students to write a function, which the lab never had them do.**
   - **Who:** B; the other four wrote one that Wikipedia's refusals kept from running to the end.
   - **What happened:** exercise Step 4 says "Turn Step 2's code into a function". All week, functions were given cells. B's `get_lead(title)` had no `return`, and found out as `AttributeError: 'NoneType' object has no attribute 'split'`, which says nothing about `return`.
   - **Why it matters:** B had no Python before this course. This is the step where such a student is most likely to stop, at home.
   - **Proposed fix:** either lab key, after Step 11's two requests: one typed cell that wraps them in `def get_lead(title):`, ends with `return lead`, and calls it once; or chapter, exercise Step 4: give the function's first and last lines. Chapter, "Common Issues": add "`'NoneType' object has no attribute …`: your function has no `return`". Which of the two is the instructor's decision.
   - **Status:** verified that Step 4 asks for a function and that no typed cell of the lab defines one. B's error is its own run.

10. **The small embedding request only confirms that embeddings work.**
    - **Who:** D; A from the other side.
    - **What happened:** D added sentences of its own. A sentence against its negation scored 0.995; against the same sentence with a different dollar figure, 0.854; "will be inaugurated as the 46th president" against "is the 46th and current president", 0.792. The lab's three sentences can't show this, and the chapter states the limit only after the plot. A's version: the frame "What is a text embedding?" says embeddings "encode interesting and troubling biases", and nothing in Step 12 comes back to it. "That frame was the one that made me want to try something, and the lab gave me nowhere to try it."
    - **Why it matters:** a student leaves with "embeddings measure meaning".
    - **Proposed fix:** lab key, cell 92: make a fourth, given sentence the negation of the first, and add one Discuss question: change one word (a name, "he" to "she", "was" to "was not"), see how far the similarity moves, and say what that means for a study that compares leads about different people.
    - **Status:** reported, not verified: the scores need embedding requests. The frame's sentence is in the deck.

11. **Part 3 is titled "search by meaning" and never searches.**
    - **Who:** B.
    - **What happened:** the part's opening and its "Today" frame ask "how do we find the ones worth reading?" Steps 11 and 12 then compare each year's lead with today's. No question is embedded and no passage is found. The chapter does it in "Retrieval-Augmented Extraction", which the lab leaves out.
    - **Why it matters:** finding the passage worth reading is the use B has for this, in council minutes. A, C and D each called Part 3's motivation thinner than Parts 1 and 2 (A: "it isn't a question I'd have asked").
    - **Proposed fix:** either retitle the part and its opening ("how much did a text change?") in the lab key and the deck, or add one small step after Step 12: embed one question, take `vectors @ question_vector`, and print the three highest-scoring leads' titles and years. The instructor's decision; the second adds minutes to a part already over.
    - **Status:** verified in the key (cells 12, 78) and the deck ("Today: Part 3, search by meaning").

12. **Nobody sees a check fail.**
    - **Who:** C, D; A and E in passing.
    - **What happened:** `check_sums(pages[14])` prints "30 rows checked" and nothing else. C changed a digit to see it print a miss. D found the picture's gaps run from −\$2 to \$2 and the 2018 text table's are all exactly 0, which is the more convincing result and isn't shown. A tried to add the months by hand and got `ValueError: invalid literal for int()`: the cells are text with commas, and Step 4's "by hand" row never adds anything. E notes that rows with fewer than 17 cells are skipped without a word.
    - **Proposed fix:** lab key, cell 28: print the largest gap, as the chapter's `largest_gap()` does. Step 4's microsprint: change one digit of one row and run the check again. Step 4's text: say the cells are text, with commas.
    - **Status:** verified: cell 28 prints only the count; the gaps on page 15 run from −2 to 2, and a data row splits into 20 pieces. One correction: the chapter has no tolerance to disagree with the lab's \$5. Its code prints the largest gap, which is \$2.

13. **Step 7 prints the wrong part of the page.**
    - **Who:** B, C.
    - **What happened:** the frame asks "Read the start of that page. Where is the row we want?", and cell 44 prints `summary[:1000]`, which ends in the table's header. The row starts at character 2,861 of 4,902, just under a second total row, the one the model and Dots copied.
    - **Proposed fix:** lab key, cell 44, and the frame "Step 7: find the summary page": print the lines that contain "Total". That shows both rows, and sets up "One way it goes wrong".
    - **Status:** verified in the saved 2024 Markdown: the position, the length, and the two lines with "Total".

14. **Step 14's given cell hides its own lesson, and its `body` replaces Part 2's.**
    - **Who:** E; D saw the first half.
    - **What happened:** the model sent `"descriptive": true`; the given cell (113) dropped it and printed `True` for the value, with no sign a field was left out. Separately, cell 112 names its request `body`, the name `extract_totals()` reads from Part 2, so a later rerun of Step 10 would send the tools request, and whatever failed wouldn't point at the cause.
    - **Proposed fix:** lab key: print the parameters cell 113 sent, without the key; name Step 14's variable `tool_body`.
    - **Status:** verified: cell 71 reads the global `body`, cell 112 assigns it, and cell 113 builds its request from five of the model's six arguments, without `descriptive`.

15. **Step 8's warning about a paid key carries no number.**
    - **Who:** D.
    - **What happened:** "with `model`, OpenRouter answers from your account's default model, which may not be free". A student with credit on the account would find out by paying.
    - **Proposed fix:** lab key, Step 8: say what it could cost, and add a Discuss line to check OpenRouter's Activity page after class.
    - **Status:** reported, not verified. D didn't try it.

### Corrections

Claims in the reviews that turned out wrong or inexact, and what this document does with them:
- **E: "Step 9 checks only the totals."** Cell 65 prints the year and month too, as bare values. Item 2 says so.
- **C, D: every early lead scores no higher than different people's current leads.** True of four articles; Clinton's early leads score 0.58 to 0.69. Item 3 says four of five.
- **D: the chapter's "within \$2" against the lab's \$5.** The chapter's code has no tolerance: it prints the largest gap. Item 12 is worded that way.
- **D: 16 of Exhibit 3's 30 rows add up exactly.** A recount gives 17. The range, −2 to 2, is right.
- **E: a 503 at "Step 6" from `GET /api/v1/key`.** The lab has no such cell; it is the chapter's suggested check. Dropped.
- **E: the chapter pauses three seconds between its two Wikipedia requests.** It doesn't. That part of E's fix is dropped.
- **C: "all six microsprints".** The lab has five.
- **A: the Clinton microsprint "gives 2007, not the 2025 jump the Discuss box goes on to discuss".** Both are right: her biggest rise is 2007 (+0.096), and the box discusses 2025 (+0.049) as a rewrite without calling it her biggest. Kept as a small thing.

## Disagreements

- **Too fast for A, B and C; mostly waiting for D and E.** A, B and C rate pace 2 and would lose Step 10. D and E rate it 3, say Parts 1 and 3 fit, and object to the silent minutes. Yet D and E estimate Part 3 at 75 minutes, longer than A's 55: D spent it on validity checks nobody asked for, E on pandas conditions. That suggests the time isn't in the typing. Printing progress helps all five; cutting cells helps A, B and C only.
- **What to cut from Part 2.** A and B would drop the Dots microsprint. D calls it "better still" than the loops, because two models disagreeing on three of four fields answers "if they agree, are they right?" from the student's own screen. C and E would load the first loop's table from a saved file. A and B valued running the before and after themselves. Dots as "on your own" and the first table as a saved file can't both be the cut that keeps the lesson; it needs the instructor.
- **Different counts for the same loop.** The chapter says five of seven, the key four, and the personas got five or six. A: "good for the lesson, confusing for the questions". D wants a sentence under the table. E wants the key's run saved so everyone discusses one table. A sentence costs nothing and is in item 2; a saved table also solves part of item 5.
- **What Part 3 is for.** A came for the people and the bias frame, B for search, C and D for a number they could trust, and E found it "the best part for a tool-builder" as it is. Four of five (A, B, C, D) called its motivation thinner than Parts 1 and 2. One part can't be all four, but a baseline (item 3) and one changed word (item 10) would serve A, C and D with two short cells.
- **Given cells.** A, B and C say the given cells carry exactly what would have sunk them. E agrees for Parts 1 to 3, and says Step 14's given cell hides the one decision worth seeing. B points out the other edge: after a week of given functions, the exercise asks for one (item 9).
- **Difficulty.** A rates it 4 of 5, B and C 3, D and E 2. In class, with the slide, all five could do it. The spread is in what happens at home with the notebook alone (item 6) and the exercise's setup (item 4), which fall on A and B.

## Ratings

Each on a scale of 1 to 5. For difficulty, 5 is hardest for that persona's background.

| | A | B | C | D | E | Mean |
|---|---|---|---|---|---|---|
| Clarity of motivation | 4 | 4 | 4 | 4 | 4 | 4.0 |
| Pace | 2 | 2 | 2 | 3 | 3 | 2.4 |
| Difficulty for my background | 4 | 3 | 3 | 2 | 2 | 2.8 |
| How much I learned | 4 | 5 | 4 | 4 | 4 | 4.2 |
| Confidence I could do this on my project | 3 | 3 | 3 | 4 | 4 | 3.4 |

What holds the confidence down: A couldn't write the loops or functions around the requests, and never saw Datalab run; B isn't confident writing the function, or handling a 429 without the lab's cells to copy from; C and D don't know what to check a model against without a table like week 9's; E would have to design the checks, because only Step 9's totals are shown.

## Small things

Deck (`slides/week-13/week-13.tex`):
- "Week 13 Portfolio": "An script or analysis notebook" (A, B, C). The frame also differs from the lab's last cell and `docs/grading.md`: "a caption with an interpretation" and "Update your README to include methods and your figure", against "a one-sentence caption" and "the README's Methods section and your preliminary Findings"; and the lab has no script.
- "Final project": "At least one Jupyter notebook (.ipynb) or Python script (.py)". `docs/course-facts.md` says "at least one `.ipynb`" (A, C).
- "Final project presentation": "(final project, week 17)". Presentations are November 30 to December 4 and the project is due December 7 (B, C).
- "Check-in": "week 13 lab due by midnight" on Wednesday, where the lab says 11:59 p.m.; and "lab" where the Recommended Exercises are meant, while the lab's opening says "Nothing here is turned in" (B, D).
- "Step 13": "Graded on a good-faith attempt". `docs/course-facts.md` gives a 10-point rubric whose criteria include "each step does its task" (A, B, C).
- "This week", Errors box: "A `429` means a free model is busy". In Part 3 it means Wikipedia (A).
- "What is a lead on Wikipedia?": "should be a summary of that summary" has no full stop. "What is a text embedding?": "text that is close to other text in an embedding is more similar to each other" (A). The same frame says "hundreds or thousands of elements" and never connects to the lab's 2,048 (D).
- "Step 12: one small request" prints the vectors and their size; the cell's prompt also asks for `usage` (C).

Lab (`labs/week-13/lab-13-key.ipynb`):
- Step 1's Discuss says "Print `one_markdown[:60]`"; no prompt makes `one_markdown`, only the slide and the key (A, B, C).
- The opening says "You need two free keys, and Part 3 also needs week 11's", but only the optional Step 14 uses `CENSUS_KEY` (B, C).
- Cell 47's comment, "check OpenRouter's list … before class", reads as a note to the instructor (B).
- Step 7: `pages_series.contains(...)` gives `AttributeError: 'Series' object has no attribute 'contains'`; the prompt could say `.str` (E). Step 7's text doesn't say the phrase is on two pages; its Discuss does (E).
- Step 11: the cleaned lead begins "Barack Hussein Obama II (; born …". The pronunciation went and its brackets stayed. It matches the saved lead, and 6 of the 116 saved leads have it, but nothing says so (A, B, D, E).
- Step 12: the response's `model` comes back as `private/openrouter/nvidia/nemotron-3-embed-1b`, not the `EMBEDDER` ID. Exercise Step 6 asks which model was used (E).
- Step 12: the table matches the chapter's to three places; "yours should match the chapter's" would make that a check (D, E).
- The biggest-jump microsprint on Hillary Clinton gives 2007 (+0.096, the lead grew from 75 to 224 words); the Discuss box discusses her 2025 rewrite (A).
- Dots microsprint: the key's Dots got both totals right and the month wrong; A's, C's and D's Dots returned the row above. "Did Dots agree with week 9?" has a different answer on each screen (A, C, D).
- Step 14 links the MCP specification's 2025-06-18 version; the chapter links 2025-03-26, the one the Census server answered with (B).
- Found while verifying item 14: Step 14's Discuss says "in an earlier run the model also sent `descriptive`", but the key's saved output for cell 112 has it in this run.

Chapter and companion notebook:
- The lab's first Wikipedia request has no `formatversion` and reads `list(found.values())[0]`; the chapter's has `formatversion=2` and reads `["pages"][0]` (A, B, C). Within Step 11, the first request has none and the second has it.
- The chapter's `HEADERS` is "WebDataScience/1.0 (your-email@colorado.edu)" for every request, Wikipedia included; the lab's Part 3 says "Wikimedia asks for week 10's User-Agent, with the library and its version" (B, C).
- "Common Issues" says to send `"tool_choice": "required"`; the lab sends `"auto"` and says OpenRouter's documentation doesn't list `"required"` (C).
- The companion notebook's text shows raw cross-references, such as "chapter 9's sources (@sec-pdfs)": 9 Markdown cells have one (B).
- Exercise Step 5 asks "by how much?": say a difference, not a ratio (E). Exercise Step 2 says nothing about a 429: point to `retry-after` (E).
- Chart 9's grand total is \$1 off the sum of its parts, a rounding in the source (D; not verified).

## Suggested next step

**Fix first.** Each is small, and none changes what the week teaches:
1. **Item 1:** make the two slicing lines given in cells 11 and 21. It is the only finding where a beginner's mistake prints contact details.
2. **Item 2:** add `year_ok`, `month_ok` and a count of fully right rows to both loops, in the lab and the chapter together, and reword cell 76 to "in your run".
3. **Item 4:** one setup cell above the exercises in the chapter that sends nothing, and two lines in the lab's Step 13 list.
4. **Items 7 and 8:** the two commented checkpoint cells (the saved HTML in Step 11, the saved Markdown after Step 2), one sentence each on `JSONDecodeError` and on `detail`, and outputs for the key's five Datalab cells from a laptop run.
5. **Items 5 and 6, the cheap halves:** `print(report)` in both loops, and the method named in the prompts of cells 82, 89, 93, 100 and 114.

**Needs the instructor's decision:**
- **The minutes.** 58, 54 and 44 against 50, 50 and 35. What becomes given, saved or "on your own" in Part 2, where the personas disagree (Dots, the one-field round, the first loop), and what Part 3 gives up on a 35-minute Friday.
- **What Part 3 claims.** Whether to add a baseline and a sentence on length (item 3), a negation (item 10), and a search step or a new title (item 11). The first two are short; the third adds a step.
- **The Trump 2006 lead.** Clean it, which changes the saved vectors and one value in the chapter, or keep it as a Discuss example. The data are the chapter's, so both copies change together.
- **The exercise's function (item 9).** Teach one typed `def` in the lab, or give its first and last lines in the chapter.
- **The announcement frames.** Whether a `.py` script meets the Final Project's code requirement, what "week 17" should say, "good-faith attempt" against the rubric, and the checkpoint's wording. Each is a fact written in more than one place (`docs/course-facts.md`).
