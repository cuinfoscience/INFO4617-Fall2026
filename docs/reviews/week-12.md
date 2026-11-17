# Review: week 12, Social and Media Platform APIs

**What was reviewed:** week 12's lab (`labs/week-12/lab-12.ipynb`, with its key), deck (`slides/week-12/week-12.tex`) and chapter 12's Recommended Exercises, as students meet them.
- **Course repository:** `main` at `efc1e36711c1f2e4ae3fcbf00c4cfa78cd3709ac`, with week 12's revision (#199) merged.
- **Textbook:** `ch-12-social.qmd` and its companion notebook at `main`, `3f9cf2cef801181236c9cceaf71f3b63c3ad2491`.

**When:** 2026-11-17. The week was taught on November 2, 4 and 6. The lab was rebuilt on 2026-11-10 and revised on 2026-11-16 (the key's own note), so this is a review of the version kept for the next offering, not of the one the class used.

**Method:** five anonymous composite personas, each a kind of student this course has, reviewed the week independently ([`README.md`](README.md) has the method in full). Each read the chapter and the slides, typed and ran its own code for the lab's steps from the students' copy, made the mistakes its background makes, attempted the Recommended Exercises, and opened the key only after an honest try. Each review is a **steel man**: it first makes the strongest case for the materials as designed, and only then says where they fall short for that student. This document puts the five together. Every ranked finding was then checked against the repository and the textbook, and is marked **verified** (with how) or **reported, not verified**.

Two limits on the method this week:
- **Part 3 (YouTube) was read and judged, not run, by all five.** The review machine has no YouTube key. What is said about Part 3 comes from its cells, its frames and the chapter.
- **A, D and E finished in a second sitting**, from their own saved runs of Parts 1 and 2 made earlier the same day, and C reused its saved six-month table instead of running Step 6's loop again. Their numbers are from those runs.

## Who reviewed

| | Degree and major | Python and data background | Interest | Skill |
|---|---|---|---|---|
| A | BS senior, Information Science | One intro Python course; spreadsheets | Qualitative and design: online communities, UX | Minimal |
| B | BA junior, Journalism and Communication | No Python before this course; strong with public records and Excel | Data journalism, local government | Minimal |
| C | BS senior, Business Analytics | Excel, some SQL, a little pandas | Quantitative analytics: markets, customer data, dashboards | Minimal to moderate |
| D | MS first year, Data Science (BA in Statistics) | Fluent in R, moderate pandas; regression and sampling | Quantitative: measurement and validity | Moderate |
| E | MS first year, Information Science (BS in Computer Science) | Moderate Python, git; little data analysis | Design and tools: automation, APIs, building things | Moderate |

## What each completed

The lab has Steps 0–11 and seven microsprints: two in Part 1, three in Part 2, two in Part 3. Every persona finished Parts 1 and 2 against the live API, and none could send Part 3's requests (see "Environment blocks").

| | Lab steps finished | Blocked | Recommended Exercises | Needed the slide or the key for |
|---|---|---|---|---|
| A | 0–7, with their five microsprints; Part 3's setup cell | 8–10: code written from the prompts, not sent; Step 11 not attempted | Steps 1–5 run, Step 6 written; the Weather Service and the Library of Congress | Nothing to unblock; compared three cells of Steps 3 and 6 with the key afterwards |
| B | 0–7, with their five microsprints; Part 3's made-up-key microsprint | 8–10: read, not typed | Steps 1–5 run, Step 6 written; the Weather Service and the Federal Reserve | Nothing in Parts 1 and 2 |
| C | 0–7, with their five microsprints (Step 6's loop from its saved table); the made-up-key microsprint | 8–10: code written, not sent | Steps 1–5 run, Step 6 written; the same two accounts | Nothing in Parts 1 and 2; compared its Part 3 code with the key |
| D | 0–7, with their five microsprints | 8–10: code written, not sent; Step 11 read | Steps 1–5 run, Step 6 in outline; the same two accounts | Nothing |
| E | 0–7, with their five microsprints; the made-up-key microsprint | 8–10: code written, not sent; Step 11 not written | Steps 1–5 run, Step 6 written; the same two accounts | Nothing |

All five got the same September table for the Weather Service: 88 posts, 92 percent with an image or a video, median reposts 16.5. The lab's saved `nws_posts.csv` gives the same numbers.

**Estimated time for a real student of that background, in minutes** (the lab's own step minutes in the last row). Part 3's column is a guess from reading, for all five.

| | Getting the key | Part 1 | Part 2 | Part 3 | Exercises |
|---|---|---|---|---|---|
| A | 15–30 | 50, and about 10 over with mistypes | 55–60 | 35 | 135 |
| B | 20–30 | 70 | 75 | 55; 15–30 more if the key reads `MISSING` | 150–180 |
| C | 15–20 | 60 | 65 | 45 | 120 |
| D | 15 | 50 | 55 | 40 | 120, most of it deciding what to count |
| E | not given | 50 | 65 | 40 | 90–120 |
| **The lab** | **15, before class** | **50** | **53** | **41** | none given |

## Environment blocks

These come from the review machine, not from the materials. They are kept apart so that none is read as a flaw in the week. Where a block exposed a missing way round it, that is a finding below (item 4), and says so.

- **No YouTube key (all five).** Step 8's key cells, Steps 9 and 10, and Step 9's microsprint were written from the prompts and not sent. Nobody saw a channel, a playlist or a video's statistics. B, C and E ran the one Part 3 request that needs no key, the made-up-key microsprint, and got what the key shows: 400, `API key not valid. Please pass a valid API key.`, reason `badRequest`.
- **Nothing was refused.** Bluesky answered every request from all five, with no 429, and GitHub served both checkpoints.
- **Notebook state was lost between sittings** (C, E). C collected the exercise's posts again as a script; E ran its exercise code again because the outputs hadn't been saved.
- **The numbers moved in a week.** The key ran on 2026-11-10 and the personas on 2026-11-17. The Weather Service had 64,694 to 64,706 followers against the key's 63,392; the misspelled filter let in 19 replies of 100 against the key's 21; Step 6's loop read 595 posts, back to March, against the key's 495, back to April 28, before keeping the same 472. That is the platform changing, not the lab (item 10 is about saying so).

## The strongest case for the week as designed

**Every request starts small, and starts with proof that something came back.** All five said so. Step 1 has students type the address, the parameters, the request, `print(status, .get("message"))`, `.keys()`, and only then one field, and the same order repeats in Steps 3, 5 and 6. A misspelled `followerCount` right after printing the keys, looked up, and saw `followersCount`. C's `"actor"` for `"actors"` in Step 3 came back as `Missing required key "actors"`: "That message told me exactly what was wrong." For D, who thinks in R, it is `str()` and `names()` carried over: "look before you read". For E, "the first thing I learn is how this API says no, and I learn it on a request that works". Three items before 25, one page before six months, and three uploads before 50 meant each persona knew what one row looked like before a given cell made a table of them (C).

**"A 200 doesn't mean it worked" is something students cause on purpose.** The microsprints were the part every persona named. Seven handles asked for and six back, with status 200 and `message` `None`. `"Limit"` with a capital L: 200, and 50 items for a request for 3. `"posts_no_reply"`: 200, and 19 replies among 100 items. `"Cursor"`: page one again. B, D and E reproduced all four on 2026-11-17 and the Discuss boxes' claims held. C compared it to a silent row drop in a SQL join. D called them "the kind of thing that corrupts a dataset without an error, and the lab makes me cause it on purpose".

**Monday asks who is posting before anything is counted, and then breaks its own easy rule.** Step 2 gives two proofs, the domain handle and the check, and the frame "Step 2: is it really the agency?" puts an impostor beside them. The given NOAA Fisheries cell has a `.gov` handle and no check. The `noaa.gov` microsprint answers `400 Profile not found`, and the same account by its `did` comes back as `handle.invalid`. A: "'official' is something you check, not something you assume". B, the journalist, would take Step 2 to a newsroom: "a name can stop resolving while the record stays". D called it "a real lesson in what a measurement instrument can and cannot claim". A and B rated the week's motivation 5 of 5.

**The given cells hold what a beginner can't write yet, each straight after one case typed by hand.** A, B and C listed the same ones: the loop that builds the accounts table, the `while True` loop over the cursor, the `elif` labels, the `groupby`. Students type page two by hand, watch the cursor change, and then read the loop. B: "By the time I read the six-month loop, I knew what each line did." For E the given cells "hide less than I feared": the decisions (the repost skip, the stop on a date, the conversion to Eastern time) are typed or named in a comment and a Discuss question. Each part starts from a saved table, and B, C, D and E each report the key's numbers from their own runs: 472 posts from May through October, 395 with images, Friday the busiest day with 109, 10 a.m. Eastern and 14:00 UTC the busiest hour. The slides and the lab agreed on every cell A compared, in Steps 1 to 7.

**The care for people is in the code, and the validity checks are in the course's own words.** Reposts are skipped to keep other people's posts, "perhaps private people's", out of the table, and the given counting cells count reposts and replies "without printing whose posts they are". B: "a rule I could apply to my own project", and it "taught me to report counts instead of names". No output saved in the key holds a handle or an ID other than the agencies' and Bluesky's own. Step 7's hour microsprint shows in one line what a forgotten time zone does to a conclusion (C, D), and saving `collected` with every table makes the date part of the data (D).

## Where it falls short, ranked

Privacy and wrong-result problems come first. No persona found a privacy problem this week, so the list opens with the two findings where a student gets a wrong result and nothing says so. After them, items are ranked by how many personas hit each, how badly, and whether it stopped A or B. Cell numbers are the key's (`labs/week-12/lab-12-key.ipynb`); the students' copy is made from it and has the same prompts.

1. **Step 7's weekday count gives a wrong picture when it is carried to the exercise, in two ways.**
   - **Who:** A, B, C (a day with no posts); D (the month's calendar).
   - **What happened:** the typed cell 73 is `by_day = day_names.value_counts().reindex(days)`. The Weather Service posts on all seven days, and the lab's six months hold 26 or 27 of each weekday, so the lab's table never shows either problem. Step 11's list then sends students to "Step 7's time zone, weekdays" for the exercise's two accounts and one month.
     - **A day with no posts becomes `NaN`.** The Library of Congress (A) and the Federal Reserve (B, C) posted nothing on a Saturday or Sunday in September. `reindex(days)` gave `NaN` for both days and turned the other counts into decimals (`2.0, 7.0, 6.0, 4.0, 3.0, NaN, NaN` for A). The bar chart left the two days out without a word, and the comparison table showed `NaN`. A: "'NaN' reads to me as 'something broke'." A reached `.fillna(0)` "only by guessing", and B says a student like B would get there no other way.
     - **A month isn't a whole number of weeks.** September 2026 has five Tuesdays and Wednesdays and four of every other day. The Weather Service's highest raw count is Wednesday, with 19 posts. For each calendar day it is Friday: 4.25 posts a day against Wednesday's 3.80. A's exercise answer names Wednesday as the busiest day.
   - **Why it matters:** "this agency posts nothing on weekends" is the finding, and it arrives looking like a missing value. The busiest weekday is the first thing a student reports in exercise Step 6, and the lab's method gives the wrong day for this month. A and B can't tell either from a mistake of their own.
   - **Proposed fix:**
     - Lab key, cell 73 and Step 7's text; deck, "Step 7: count by day"; chapter, "When an Agency Posts": `.reindex(days, fill_value=0)`, and one sentence: "without it, a day with no posts shows as `NaN`". The line is the chapter's, so the three change in one pass.
     - Chapter, exercise Step 3: one sentence, "September 2026 has five Tuesdays and Wednesdays: divide each weekday's count by how many of that day the month has". Lab key, Step 7's Discuss: one question on it. The counting line is `pd.Series(pd.date_range("2026-09-01", "2026-09-30").day_name()).value_counts()`; whether it is a given cell is the instructor's decision.
   - **Status:** verified. September's posts in `labs/week-12/data/nws_posts.csv`: 88, with Monday 16, Tuesday 15, Wednesday 19, Thursday 11, Friday 17, Saturday 5, Sunday 5; for each calendar day, 4.00, 3.00, 3.80, 2.75, 4.25, 1.25, 1.25. The six months have 26 or 27 of each weekday, and Friday leads both ways. The `NaN` was reproduced from C's saved Federal Reserve table (62 posts, none on a weekend): `reindex(days)` gives `NaN` and decimals, and `reindex(days, fill_value=0)` gives whole numbers and zeros. A's Library of Congress numbers are reported, not verified.

2. **Two typed cells can go wrong with no error, before the lab has warned about it.**
   - **Who:** C (the filter); D (the cursor's dictionary); A met the second as an error.
   - **What happened:**
     - Cell 44: C typed `"filters"` for `"filter"`. Status 200, 25 items, a normal-looking page, and the replies were still in it. "I only caught it by comparing counts." The lab's two warnings, Step 5's Discuss on `"Limit"` and Step 6's microsprint on `"posts_no_reply"`, come after the cell.
     - Cell 57: the prompt says "`feed_params`'s three keys and values, plus `"cursor"`". D wrote `second_params = feed_params` and added the key. No error: `feed_params` now held the cursor too, and D saw it only by printing both. A read the same prompt as `feed_params + {"cursor": ...}`, because Monday's microsprint had just said "`+` joins two lists", and got `TypeError: unsupported operand type(s) for +: 'dict' and 'dict'`. The key and the slide type all four keys out.
   - **Why it matters:** it is the week's own lesson, happening unplanned and unseen. C "would have kept replies in my September table without noticing", and replies are what the lab says it never collects.
   - **Proposed fix:**
     - Lab key, cell 51 (given): count the items that have a `"reply"` key and print it beside the count it already prints, so a wrong filter shows as a number that isn't 0. One sentence in Step 5's text: "if a parameter changes nothing, suspect its name".
     - Lab key, cell 57: "type the dictionary again, with a fourth key, `"cursor"`", as the frame "Step 6: page two, by hand" does. Or one sentence in Step 6's text that `second_params = feed_params` is the same dictionary under two names, and `dict(feed_params)` is a copy, which is the pattern week 13's lab uses for its headers.
   - **Status:** verified that the prompts read as quoted, in the key and the students' copy, and that both warnings come after cell 44. The key's own cell 67 shows a misspelled value answered with 200 and 21 replies. C's 200 with `"filters"` and A's error text are their own runs; D's shared dictionary is how Python assigns one.

3. **The Recommended Exercises ask for things the lab never shows.**
   - **Who:** A, B, C, D, E.
   - **What happened:** Step 11's list maps each exercise step to a lab step. Four things fall between the two:
     - **Replies** (A, B, C, E). Exercise Step 2 says to keep "likes, reposts, replies, and embed type". The lab's given loop (cell 61) keeps likes, reposts and `embed`. B: "The only 'reply' I met in the lab is a thing we filter out", so is it the replies the account wrote, or the replies each post got? They found `replyCount` in the chapter's loop (A, B) or by guessing and printing the keys (C).
     - **A share** (A, B). Exercise Step 3 asks for "the share of posts with an image or a video". The lab's cell 77 gives a count and a median for each kind. A divided `value_counts()` by the length and added two rows by eye, then found `.isin([...]).mean()` after "a long search". B: "I'd guess I would copy the counts into a calculator." Step 11's list says "the median reposts is one more column" and doesn't mention the share.
     - **The month's end** (C). "Keep the posts created in September" needs an upper date. The lab's cell 62 does it for six months, and nothing says the exercise needs the same.
     - **Two accounts on one chart** (A, E). The lab's plot draws one Series. A's first plot put both accounts on one axis with no legend; E's drew one account's bars over the other's in one colour. The way that works, one DataFrame with a column for each account, is in neither the lab nor the chapter.
   - Two smaller gaps. A student who opens the companion notebook at the exercises gets a `NameError`, because nothing says which of the 11 code cells above them to run (B). And C, D and E wrapped the loop in a function for the second account, which the lab never types; A copied the loop.
   - **Why it matters:** this is the graded part of the week, done at home. A estimates 2 hours 15 minutes and B up to 3, with "nobody to ask on a weekend". The chapter promises that "everything you need appears in this chapter or an earlier one", and for A and B the lab is the teaching.
   - **Proposed fix:**
     - Lab key, cell 61: add `"replies": one_post["replyCount"]`, as the chapter's loop has, and say in one line that it counts the replies a post got. This adds a column to the saved `nws_posts.csv`, so the checkpoint is saved again with it.
     - Lab key, Step 7, after cell 77: one typed line, `print(nws["embed"].isin(["app.bsky.embed.images", "app.bsky.embed.video"]).mean())`, which gives 0.953 on the saved six months.
     - Lab key, Step 11's list: for Step 2, "keep the month between two dates, as Step 6's given cell does"; for Step 3, name the share; for Step 5, "one DataFrame, a column for each account, then `.plot.bar()`".
     - Chapter, "Recommended Exercises": one sentence before Step 1, "run the notebook's first code cell, which has the imports, `HEADERS` and `bsky_base`; you don't need the cells between".
     - Whether a student should write a function for the second account is the instructor's decision (see "Disagreements"); week 13's review raises the same question in its item 9.
   - **Status:** verified. The key holds no `replyCount`, `isin`, `fillna` or `def`. The chapter's loop keeps `replies`; the chapter has `isin(` once, in its Reddit section, and no `fillna`, `.mean()` or `def`. The companion notebook's first code cell holds exactly the imports, `HEADERS` and `bsky_base`, and three of the eleven cells above the exercises need a YouTube key. The 0.953 was computed from `nws_posts.csv`. The personas' first tries are their own runs.

4. **Part 3 has nothing to fall back on: no saved table, no outputs in the key, and no way to tell a bad key from a typing mistake.**
   - **Who:** A, B, C, D, E. All five judged it from reading.
   - **What happened:** the missing key is an environment block. What it exposed is the lab's:
     - Parts 1 and 2 each have a saved table and a commented cell that loads it. Part 3 has neither. `videos.csv` is written only by the student's own last given cell.
     - In the key, 23 of Part 3's code cells have no output. "Fall behind? Copy the cell from the key" gives code and nothing it printed. The only expected result on the page is Step 8's "You should see `None`, then `NOAA`". The key's Step 11 answer says "Part 3 wasn't run for this key".
     - With the variable missing, the typed cell 85, `youtube_key = os.environ["YOUTUBE_KEY"]`, stops with a bare `KeyError: 'YOUTUBE_KEY'` (B, C). The given `getpass()` cell above it is the way round, and the error doesn't point there.
     - With a key that is set but wrong (restricted to the wrong API, not enabled yet), Step 8 prints an `error`, and the next typed cell stops at `test["items"]`. The made-up-key microsprint, which comes next, "would look exactly the same as my real failure" (A).
   - **Why it matters:** the key is the hardest thing asked of A, B and C all week: Google's console, a restriction, an environment variable and a restart of Jupyter. A: "I can't tell 'my key is wrong' from 'I typed something wrong'." A student whose key fails does nothing on Friday, and Step 10's table and Step 11's questions about YouTube are out of reach. D and E can't say whether the given cells of Step 10 work, because nobody has seen them run.
   - **Proposed fix:**
     - Run Part 3 once from a laptop with a key, and commit the key with its outputs (the plan of 2026-11-16 collects these runs in issue #197).
     - From that run, save `videos.csv` in `labs/week-12/data/`, and add a given, commented cell after cell 113 that loads it, like cells 29 and 64. Agencies' videos only, as the lab already keeps.
     - Lab key, cell 85's prompt: "if this stops with `KeyError`, run the given cell above it".
     - Lab key, Step 8's text: one sentence on what a real key's failure looks like. The made-up key's `reason` is `badRequest`, and the specific word, `API_KEY_INVALID`, is under `details` (C); the microsprint could ask for that one.
   - **Status:** verified that `labs/week-12/data/` holds only `accounts.csv` and `nws_posts.csv`; that cells 84–88, 93–97, 99 and 102–113 are tagged `not-run-live` and have no outputs; that the students' copy doesn't say so; and that cell 90's saved output has `badRequest` and `API_KEY_INVALID` where C says. Whether Steps 8 to 10 run as written is **not verified**: no key.

5. **Several prompts can be followed exactly into an error that doesn't point at the cause.**
   - **Who:** A, C, D, E.
   - **What happened:** most prompts give the line nearly whole, so personas trusted them to be complete.

     | Cell | The prompt says | First try, and what it gave | What it needed | Who |
     |---|---|---|---|---|
     | 7, then 8 | `keep its .json() in profile`, then `Print the status code` | `profile = requests.get(...).json()`. The next cell: `AttributeError: 'dict' object has no attribute 'status_code'` (D), or `NameError: name 'profile_response' is not defined` (E) | the response kept under its own name, as the slide does | D, E |
     | 25, 41, 45, 58, 66 | `keep its .json() in …; print the status code` | the same wording; D and E kept the response from then on | the same | D, E |
     | 57 | `feed_params's three keys and values, plus "cursor"` | item 2 | all four keys typed out | A, D |
     | 60 | `since = "2026-05-01", until = "2026-11-01"` | typed as one line: `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?` | two lines | A |
     | 70 | `local: nws["created"].dt.tz_convert("America/New_York")` | without `.dt`: `TypeError: index is not a valid DatetimeIndex or PeriodIndex` | `.dt`, which the prompt has | C |

   - **Why it matters:** the slide for Step 1 names `profile_response`, so a student who copies the slide succeeds and one who follows the prompt doesn't (D). The error lands on the cell after the one that caused it. At home, with the notebook alone, A and C read only an error's last line, and none of these last lines names the fix.
   - **Proposed fix:** lab key. Cell 7: "keep the answer in `profile_response`, and its `.json()` in `profile`"; the same two names in cells 25, 41, 45, 58 and 66. Cell 60: the two assignments on two comment lines. Step 7's text: "a column needs `.dt` first; 'not a valid DatetimeIndex' means it is missing".
   - **Status:** verified: each prompt read in the key and in the students' copy, and the frame "Step 1: send it" has `profile_response`. The error texts are the personas' own.

6. **Part 3 is over Friday's time by the lab's own minutes, and Step 11 gets three of them.**
   - **Who:** B; A, B and C on pace generally.
   - **What happened:** Part 3's step headings add up to 41 minutes, for the 35 that Friday has before the portfolio checkpoint, and its 39 typed lines sit at the limit of 40. Step 11 gives 3 minutes to four questions that each want a few sentences, and the deck has no frame for it. B: the reflection "is where a journalist like me learns what the numbers mean, and it's the cell most likely to get skipped". For Parts 1 and 2, A, B and C estimate up to 22 minutes over. D and E say both fit, though E's own estimate for Part 2 is 65 minutes against 53.
   - **Why it matters:** Friday also carries the key. The lab says to make it before class; the frame "Today: Part 3" offers four frames that make one in class, on the day with the least time.
   - **Proposed fix:** lab key, Step 11: say that its answers are the first draft of exercise Step 6, so the work is done once, and give it 5 minutes or move two of the four questions to the Discuss boxes they belong to. Whether the four key frames are shown on Friday, and the minutes themselves, are the instructor's decision.
   - **Status:** verified: the headings sum to 50, 53 and 41 minutes, 144 in all against `labs/AUTHORING.md`'s 135 (50, 50 and 35), with "Before Step 8" a further 15 before class. Typed lines are 28, 45 and 39 against limits of 55, 55 and 40, so the lab is within its typing budget in every part. Friday's section has 25 frames, none for Step 11.

7. **The chapter's first table of accounts can't be reproduced, and its pattern for the check fails on one of the lab's five.**
   - **Who:** B, D; C in passing.
   - **What happened:** the chapter's `getProfiles` example asks for `noaa.gov` and prints it with `verified` `valid` and 41,938 followers. Since then the handle has stopped resolving: asked for alone it answers `400 Profile not found`, and in a list it is left out without a word, so the chapter's cell would now print six rows where its table shows seven. The lab explains it; the chapter doesn't. The same cell reads `p["verification"]["verifiedStatus"]` directly, and exercise Step 1 says "print each handle, its `verifiedStatus`". NOAA Fisheries, one of the lab's five accounts, has no `verification` field: `fisheries["verification"]` gave B `KeyError: 'verification'`. The chapter's "five federal accounts had a `.gov` handle" also leaves out NOAA Fisheries, which the lab's five include.
   - **Why it matters:** B reads the chapter first: "When its output differs from my own, I assume I did something wrong." A student who picks Fisheries for the exercise stops at Step 1, unless they remember the lab's `.get()`.
   - **Proposed fix:** chapter, "Several Accounts at Once": take `noaa.gov` out of the list or add two sentences on `handle.invalid`, read the check with `p.get("verification", {}).get("verifiedStatus", "none")`, and count the `.gov` handles again. Chapter, exercise Step 1: point to that line, or say "pick accounts with a check".
   - **Status:** verified in the chapter, and in the key's saved outputs: cell 19 shows `400 Profile not found`, cell 20 `handle.invalid`, cell 32 "7 asked for, 6 came back", and cell 17 that Fisheries has no `verification`. That the chapter's own cell prints six rows today is inferred from those, not run.

8. **"Which one is missing?" has no method.**
   - **Who:** A, E; D noticed it.
   - **What happened:** Step 3's microsprint asks students to share "which one is missing" of seven handles. The typed cell prints the two counts. A printed every handle that came back and compared the two lists by eye. E used a set difference, which the lab never shows. The answer is `noaa.gov`, for the reason the microsprint before it gives, and nothing connects the two: "a student who doesn't connect them has no way to learn that" (A).
   - **Why it matters:** "nothing warned you" is the point of the step, and it is easy to miss when finding the answer is a puzzle.
   - **Proposed fix:** lab key, after cell 32: a given cell with a short `for` loop that prints each handle in `more_agencies` that isn't among the profiles' handles. These are agencies' handles, the ones the student just typed.
   - **Status:** verified: cell 30's Share and the frame "Microsprint: two more handles" both ask which one, and cell 32 prints only "7 asked for, 6 came back".

9. **The exercise leaves four of its measures to the student, and doesn't ask them to say what they chose.**
   - **Who:** A, B, D, E.
   - **What happened:**
     - **The month's edges** (B, E). The lab cuts its window in UTC (cell 62) and then counts by Eastern day (cell 70). A post at 9 p.m. Eastern on August 31 is already September 1 in UTC. B: "A grader sees different numbers from two honest students."
     - **"An image or a video"** (D). The lab's table has a fifth kind, `recordWithMedia`, a quoted post that carries media: 4 of the 472. Nothing says whether it counts.
     - **"Median reposts"** (D). The Federal Reserve's is 0 and the Weather Service's 16.5, so the one number nearly erases one account.
     - **"Whether the handle is a domain"** (A). The exercise's text says that; its code cell says "whether the handle ends in .gov". The Library of Congress's `.bsky.social` handle is a domain too.
   - **Why it matters:** each is a choice that changes a number, and the week's own rule is to say which choice you made.
   - **Proposed fix:** chapter, "Recommended Exercises": Step 1, "ends in `.gov`" in both places; Step 2, "say which time zone you cut the month in"; Step 3, say what to do with a quoted post that carries media. Lab key, cell 62: a comment that the window is cut in UTC.
   - **Status:** verified: the exercise's text and its cell differ as A says; `recordWithMedia` is 4 of 472 in `nws_posts.csv`; the Federal Reserve's median of 0 is in C's saved table. One check went the other way: cutting in UTC or in Eastern time gives the same 472 posts for the lab's window and the same 88 for the Weather Service's September, so the edge is a risk that these data don't show.

10. **The same counts appear with three different values, and nothing says which to expect.**
    - **Who:** A, B, C, D.
    - **What happened:** the chapter's weekday plot is titled "April–October 2026" and has 495 posts, 412 with images and Friday at 111; the lab's is "May–October 2026", with 472, 395 and 109. The Weather Service's followers are 63,022 in the chapter, 63,392 in the saved table and about 64,700 live. The Discuss boxes quote the key's run ("21 replies"), and B, D and E saw 19.
    - **Why it matters:** C: "there is no instruction on which table to trust". B assumes the mistake is B's. A sees "a good teaching moment, but only if a reader is told why it differs".
    - **Proposed fix:** lab key, Step 4's text: "your numbers will differ from the slide's and from the saved table's: that is what the `collected` column is for". Lab key, cell 61's comment: "the chapter's loop stops at five pages, so its window starts in April".
    - **Status:** verified: the chapter's numbers and its five-page stop, the key's outputs, and `accounts.csv`. The Discuss boxes already say "in the key's run". The live values are the personas' own.

11. **"Nothing here is turned in" sits beside graded work due Sunday.**
    - **Who:** A; B, C and D as a small thing. E found the dates consistent.
    - **What happened:** the lab's first cell says "Nothing here is turned in", and the frame "This week, every class is live coding" says "Nothing to submit". The Recommended Exercises, "due Sunday", are named only at the end of Friday's Step 11, and the checkpoint in the last cell. A: "I read the first line, relaxed, and almost treated the lab as optional."
    - **Proposed fix:** lab key, cell 0, and the frame: "Nothing in this notebook is turned in. The chapter's Recommended Exercises, which it sets up, are due Sunday."
    - **Status:** verified in the key's cells 0 and 115 and in the deck.

12. **The given loop has two failures a project would meet, and "the agency's posts" is a narrower set than it sounds.**
    - **Who:** D, E; B on the wording.
    - **What happened:** read, and probed by E. If an account's first page holds no posts of its own, `nws_rows[-1]` stops with `IndexError: list index out of range`. If any request fails, `page["feed"]` stops with `KeyError: 'feed'`, which doesn't mention the status; Step 6's Discuss asks about exactly this. "Until its posts are older than `since`" reads as if the loop stops at May 1; it stops after the page that crosses it, which is why it read 595 posts in the personas' runs (B). Separately, the filter and the repost skip also leave out the threads an agency writes as replies to itself, and `postsCount` counts more than the loop finds (D).
    - **Proposed fix:** no code, by the lab's own rule. Lab key, Step 6's Discuss: one more question, "what would `nws_rows[-1]` do for an account whose first page is all reposts?". Step 6's text: "it may read some older posts; the next cell drops them". Chapter, exercise Step 6: ask what the filter leaves out.
    - **Status:** verified by reading cell 61 and cell 68. E's probes are its own.

### Corrections

Claims in the reviews that turned out wrong or inexact, and what this document does with them:
- **C: the Weather Service's September has "a Friday peak of 17".** C's own saved table has Wednesday at 19. Friday leads only for each calendar day, which is D's point. Item 1 uses the checked counts.
- **C: the Federal Reserve "posts Tuesday to Friday only".** C's saved table has four Monday posts. It has none on a weekend, which is what item 1 uses.
- **D: on a page of reposts the loop's last row "would be stale, and the loop would … stop wrongly".** The last kept row is unchanged and still newer than `since`, so the loop goes on correctly. Only an account with no posts of its own so far raises the `IndexError`. Item 12 is worded that way.
- **D: older posts have had longer to collect reposts, so age confounds the comparison.** The range D gives is right (median reposts by month run from 16.5 to 25), but October, the newest month, has the highest median, so the saved table doesn't show it. Dropped as a finding.
- **A: a given cell should explain the reasons `keyInvalid`, `accessNotConfigured` and `forbidden`.** The key's saved output shows an invalid key's reason is `badRequest`, with `API_KEY_INVALID` under `details`. Item 4's fix uses those.
- **A: the saved tables are dated 2026-11-10, after the class of November 2 to 6.** Right, and not a mismatch: the lab was rebuilt after the week was taught.
- **A, E: "all three microsprints" of Part 1; A: Part 2 "holds four".** Part 1 has two and Part 2 three.
- **B: Part 1 has "about 25 typed cells", and Part 3 leans on the key for 14.** Part 1 has 15 typed cells and 7 given. Part 3 has 18 typed, and 17 of them need the key.
- **E: the takeaway "since 2024" and the frame's two dates are "two different dates for one claim".** Both dates, November 2025 and February 2026, are after 2024. What does differ is the chapter's takeaway, which says "since 2023". Kept as a small thing.

## Disagreements

- **Pace.** A, B and C rate it 3 and estimate Parts 1 and 2 at up to 22 minutes over. D and E rate it 4 and say both fit. The lab is inside its typing budget in every part, so the difference is typing speed and mistypes, not length. That suggests the fix for A, B and C is fewer cells that fail obscurely (items 2 and 5), not fewer cells.
- **How much they learned.** A, B and C rate it 4; D and E rate it 3. D: "The measurement lessons were mostly mine to draw." E: "the rest I would have found in the docs." What D and E added on their own (weekdays for each calendar day, the loop's edge cases, the month's edges) is where items 1, 9 and 12 come from.
- **Error handling.** C "would not trust my own error handling: the lab gives none by design". E wants a given variant of the loop with `raise_for_status()`, "after you've seen it fail", and calls it "not urgent for this audience". D wants a Discuss question "rather than code". The lab's rule is D's, and item 12 follows it.
- **A function for the second account.** C, D and E wrote one, and C and E want the lab or the exercise to say so. A copied the loop. The lab gives every loop and types no function. Week 13's review found the same edge from the other side: its exercise asks for a function the lab never had students write.
- **What the week is for.** A and B rate motivation 5: the people behind the accounts, and a check they could put in a story. C asks "why a business analyst would look at a federal agency's weekday pattern". E finds "the link from Part 3 to my own project is thin". D wants the frame, what "own posts" means, stated earlier.
- **Stale numbers.** For D they are "dated, so fine". For A they are a teaching moment if explained. B and C read a difference as their own mistake. One sentence (item 10) serves all four.
- **Difficulty.** A, B and C rate it 3 and D and E 2. All five could do the typed cells. The spread is in the exercise (items 1 and 3), which A and B call "a step up" and "a big step up".

## Ratings

Each on a scale of 1 to 5. For difficulty, 5 is hardest for that persona's background.

| | A | B | C | D | E | Mean |
|---|---|---|---|---|---|---|
| Clarity of motivation | 5 | 5 | 4 | 4 | 4 | 4.4 |
| Pace | 3 | 3 | 3 | 4 | 4 | 3.4 |
| Difficulty for my background | 3 | 3 | 3 | 2 | 2 | 2.6 |
| How much I learned | 4 | 4 | 4 | 3 | 3 | 3.6 |
| Confidence I could do this on my project | 3 | 3 | 3 | 4 | 4 | 3.4 |

What holds the confidence down: A could run the loop again with another handle and dates, but not build a comparison table or a share without looking things up. B isn't sure a key would survive the terminal restart, or what to do about a 429 in the middle of a long loop. C would not trust its own error handling. A, B and C each note that they never ran the YouTube part. D and E would add handling for a 429 and a retry before running a loop for an hour.

## Small things

Deck (`slides/week-12/week-12.tex`):
- "Friday's last 15 minutes": "saves the raw data(`.py`) is fine" has lost a space and some words (A).
- "Key takeaways" says Reddit and Spotify have closed much of their APIs "since 2024"; the chapter's takeaway says "since 2023" (E, and see "Corrections").
- "Step 6: six months, given" shows only `since` and `until`. The loop is in the notebook alone, so students watching the screen don't see it (E).
- "Step 2: the check" asks "Who verified the account?" and its code prints `verifiedStatus`. The answer, `issuerDisplayName`, is in the field printed one line earlier (B).
- "Three ways to page" names EIA's `offset`, from chapter 11. Week 11's lab didn't use EIA, so the reference is unexplained (A).
- The section dividers repeat the slide number of the frame before them: "1 of 74", "24 of 74" and "49 of 74" each appear twice (C; not verified, the deck wasn't built).
- "Daily note questions" answers two questions about keys, which reads as unrelated to Monday's Bluesky (D).
- Found while verifying: "This week at a glance" says the exercises and the checkpoint are "Graded on good-faith attempt to complete". `docs/course-facts.md` gives the Notebook Labs a 10-point rubric whose criteria include "each step does its task". Week 13's review found the same sentence in its deck.

Lab (`labs/week-12/lab-12-key.ipynb`):
- Step 1's Discuss quotes the error as `Missing required key "actor"`. B's full message was `Invalid app.bsky.actor.getProfile params: Missing required key "actor"`.
- Cell 71: `day_names.head()` prints index labels 16 to 20 in the key (30 to 34 for B), not 0 to 4, because the table was filtered. Nothing says so (B).
- Step 3's text explains `[:10]` several cells before the given cell that uses it (D).
- Step 2 says "no one else can post as `nws.noaa.gov`". One more sentence would finish it: `.endswith(".gov")` checks only the handle Bluesky reports, and `.gov` covers cities, states and tribes as well as federal agencies (D).
- Step 3's Discuss asks which agencies a `.gov`-only study would never see. The chapter's answer, the Census Bureau and NASA, isn't in the lab (B).
- Step 5 says "a pinned post isn't in the feed", and nothing prints one to check (E).
- The lab's `agencies` has no `librarycongress.bsky.social`, which the chapter's list has and the exercise invites. A looked the handle up in the chapter.
- Part 3's setup cell loads `nws_posts.csv` and never uses it; only `accounts` comes back, in Step 9's microsprint. It adds a request to the day with the most to go wrong (C, E).
- Step 9's microsprint asks students to share a channel's subscribers beside the agency's Bluesky followers. They count different things, and YouTube rounds its count to three figures; the Share could say so (D).
- The lab links Bluesky's API directory at `bsky.network/docs/…` and its methods at `endpoints.bsky.app`; the chapter links `docs.bsky.app` for both (B).
- The last cell and the frame give the checkpoint as "due Sunday, November 8", and Step 11 the exercises as "due Sunday". Both are right, and easy to read as one deadline (B, C).

Chapter and companion notebook:
- The exercise says to pick two accounts "from this chapter's list". The list of seven includes `noaa.gov`, which doesn't resolve (C; see item 7).
- Exercise Step 5 says only "plot one comparison you find informative"; item 3's sentence on one DataFrame would go here too (A, E).
- Exercise Step 4 could say "the same code, for the second account", whichever way the function question is decided (C).

## Suggested next step

**Fix first.** Each is small, and none changes what the week teaches:
1. **Item 1:** `reindex(days, fill_value=0)` in the lab, the deck and the chapter together, and the sentence on September's five Tuesdays and Wednesdays in exercise Step 3. It is the one finding where the lab's own method gives a wrong answer on the exercise.
2. **Items 2 and 5:** the prompts. Name `profile_response` in cell 7 and the five cells like it, "type all four keys" in cell 57, two comment lines in cell 60, and a count of replies in the given cell 51.
3. **Item 3, the cheap half:** the share as one typed line in Step 7, three clauses added to Step 11's list, and the sentence in the chapter on which cell to run before the exercises.
4. **Item 4:** run Part 3 from a laptop with a key, commit its outputs, and save `videos.csv` with a commented cell that loads it (issue #197 already tracks the run).
5. **Item 7:** in the chapter, `.get()` for the check, and `noaa.gov` out of the list or explained.

**Needs the instructor's decision:**
- **Replies in the given loop** (item 3). One more column in cell 61 brings the lab to the chapter's loop, and changes the saved `nws_posts.csv`. The alternative is a clause in the exercise saying where `replyCount` is.
- **Weekdays for each calendar day** (item 1). A sentence in the exercise, or a given cell and a Discuss question in Step 7, which adds minutes to Part 2, already 3 over.
- **Friday's minutes** (item 6). 41 against 35, with Step 11 at 3. What moves out of Part 3, or whether Step 11 becomes the first draft of exercise Step 6.
- **A function for the second account** (item 3, "Disagreements"). Keep every function given and let students copy the loop, or have the exercise say "write one function and call it twice". The same question is open for week 13.
- **The exercise's definitions** (item 9). Which time zone cuts the month, and whether a quoted post with media counts as "an image or a video". Each is a sentence in the chapter.
- **"Nothing here is turned in" and "good-faith attempt"** (item 11, "Small things"). What the lab's first cell and the at-a-glance frame should say about what is graded. Each is a fact written in more than one place (`docs/course-facts.md`).
