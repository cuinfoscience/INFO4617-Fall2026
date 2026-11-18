# Review: week 05, Web Architecture and Protocols

**What was reviewed:** week 5's lab (`labs/week-05/lab-05.ipynb`, with its key), its deck (`slides/week-05/week-05.tex`), the lab's three checkpoints (`labs/week-05/data/`), and chapter 5's Recommended Exercises in its companion notebook, as students meet them. The lab and deck are the three-part rebuild for the course's next offering; fall 2026 taught the two-day version in September.
- **Course repository:** the head of pull request #211, `8ee384e65fbf440dfff9d8ba5bda564f79561b37` (open, not merged).
- **Textbook:** `ch-05-protocols.qmd` and `notebooks/ch-05-protocols.ipynb` at `main`, `3f9cf2cef801181236c9cceaf71f3b63c3ad2491`.

**When:** 2026-11-17 and 18.

**Method:** five anonymous composite personas, each a kind of student this course has, reviewed the week independently. Each read the chapter and the slides, typed and ran its own code for every lab step it could from the students' copy, made the mistakes its background makes, attempted the Recommended Exercises, and opened the key only after an honest try. Each review is a **steel man**: it first makes the strongest case for the materials as designed, and only then says where they fall short for that student. This document puts the five together. Every ranked finding was then checked against the repository and the textbook, and is marked **verified** (with how) or **reported, not verified**.

Two notes on how far each review can be trusted:
- **E's Part 2 was not fully blind.** To get the key's saved outputs for the cells it would not send, E printed the key's cells for Steps 4 to 7, code included, before typing them. Those cells are one to three lines, but E's Part 2 findings carry less weight than its Parts 1 and 3. E also read A's runner script, for its shape only.
- **Reviewers were told to read a host's `robots.txt` before sending it anything. Three didn't, at least once, and the lab's flow is what led them there.** In Step 5's microsprint ("a site you read"), A sent one `curl -I` to nytimes.com, B one to bouldercolorado.gov (which, read afterwards, allows it), and C one to nytimes.com; C also sent one request to ip-api.com in the same command that fetched its `robots.txt`. A also ran Step 7's three ip-api requests and Step 14's Action API call as the lab directs, without reading either file. Each recorded the slip in its notes and didn't repeat it. These are the requests a student following the lab would send; item 1 is about that.

## Who reviewed

| | Degree and major | Python and data background | Interest | Skill |
|---|---|---|---|---|
| A | BS senior, Information Science | One intro Python course; spreadsheets | Qualitative and design: online communities, UX | Minimal |
| B | BA junior, Journalism and Communication | No Python before this course; strong with public records and Excel | Data journalism, local government | Minimal |
| C | BS senior, Business Analytics | Excel, some SQL, a little pandas | Quantitative analytics: markets, customer data, dashboards | Minimal to moderate |
| D | MS first year, Data Science (BA in Statistics) | Fluent in R, moderate pandas; regression and sampling | Quantitative: measurement and validity | Moderate |
| E | MS first year, Information Science (BS in Computer Science) | Moderate Python, git; little data analysis | Design and tools: automation, APIs, building things | Moderate |

## What each completed

The lab has Steps 0–15 and seven microsprints: Part 1 (Monday) is Steps 0–2, Part 2 (Wednesday) Steps 3–8, Part 3 (Friday) Steps 9–15, then Friday's 15-minute textbook block. No persona had a browser, so the Inspector and Network-tab halves of Steps 1 and 2, and Step 2's microsprint counts, were read, not done, by all five (see "Environment blocks").

| | Lab steps finished | Read, not done | Recommended Exercises | Needed the key for |
|---|---|---|---|---|
| A | All typed cells of Steps 0–14, and every microsprint; Step 11's microsprint table from the checkpoint after two 429s; Step 15 in two comments | Browser halves of 1 and 2 | Steps 1–5; Step 6 drafted, not written | Nothing |
| B | 0–6, 8–13, Step 14 but the Action API cell (109) | 7 and 14's cell 109 (robots.txt); browser halves of 1 and 2 | Steps 1–6 | Cell 99's `.total_seconds()`; Step 7's outputs |
| C | 0–6, 8–14 but Step 11's live loop (checkpoint used after a 429) and Step 14's cell 109 (429) | 7 (robots.txt); browser halves of 1 and 2 | Steps 1–6 | Step 7's outputs |
| D | 0–6, 8–14 but cell 109, whose URL D built without sending it; fallback cells skipped | 7 and 109 (robots.txt); browser halves of 1 and 2 | Steps 1–6; one row of Step 5 substituted after a 429 | Step 2's microsprint counts; Step 7's outputs |
| E | 0–6, 8–14 but cell 109; Step 11's loop and Step 14's requests on a retry five minutes after 429s | 7 and 109 (robots.txt); browser halves of 1 and 2 | Steps 1–6 | Step 7's outputs; saw Steps 4–7's code early (above) |

**Estimated time for a real student of that background, in minutes** (the lab's own step and microsprint minutes in the last rows):

| | Part 1 | Part 2 | Part 3 | Exercises |
|---|---|---|---|---|
| A | 45 | 65 | 50, plus 15 for Step 15 and the textbook block | 90–120 |
| B | 45–55, about 15 of it in the developer tools | 70–80 | 75–90 | about 120; 180 with a snag in `diagnose_url()` |
| C | 40 | 55–60 | 55 | 75 |
| D | 35–40, mostly browser clicking | 50–55, plus Discuss | 40 | 90 |
| E | 40 (10 for the typed cells alone) | 45 | 55, plus 5–10 a 429 | 75 |
| **The lab** | **35** (27 in steps, 8 in microsprints) | **59** (49 in steps, 10 in microsprints) | **43** (37 in steps, 6 in microsprints) | none given |
| **The day** | **50** | **50** | **35**, then the 15-minute textbook block | due Sunday |

## Environment blocks

These come from the review machine, not from the materials. They are kept apart so that none is read as a flaw in the week.

- **No browser (all five).** The Inspector and Network-tab halves of Steps 1 and 2 were read, not done. Step 2's microsprint ran on placeholder counts (A, B, C, E) or the key's and the slide's counts (D).
- **No `ping` (all five).** The key tags Step 5's optional `ping` cell `not-run-live` for the same reason.
- **A proxy in front of every connection (all five).** `curl -v` narrates `* Connected to 127.0.0.1` and a `CONNECT en.wikipedia.org:443` before Wikipedia's answer; `head_lines[:3]` starts `HTTP/1.1 200 Connection Established`; `socket.gethostbyname()` gives 127.0.0.1; ipify reports the proxy's address. The key's note and Step 5's last Discuss question say so. D and E also saw ANSI bold codes around header names in `!curl`'s output.
- **Wikimedia's 429s on a shared address (all five).** The machine's one public address was shared by the five reviewers and other jobs. Wikimedia answered with 429s: Step 11's three-article loop (A, C, E), the month request (B), Step 14's requests (C, E), and the pageviews API in the exercises (D). Each worked on a later try, or from the checkpoint. A classroom behind one campus address may see the same; how the lab reports a 429 is item 4.
- **The checkpoints 404 until #211 merges (A, B, C, D).** `DATA` reads `labs/week-05/data/` from `main`, where the folder doesn't exist yet (verified: `main` at `91944dc` has only the key, its PDF and the students' copy in `labs/week-05/`). The personas read the three files from the branch. This is a merge-order item, listed under "Suggested next step", not a flaw.
- **Not an environment block: Step 7 and Step 14's cell 109.** B, C, D and E didn't send them because the hosts' `robots.txt` files disallow those paths. The key doesn't tag them `not-run-live`. That is item 1.

## The strongest case for the week as designed

**Every service gets a first call small enough to read in full, on an input the student can predict.** All five said so, with the same examples: one line of HTML (`Hello`) before the 768 KB article (Step 1), `one.one.one.one` before `en.wikipedia.org` (Step 6), `8.8.8.8` before Wikipedia's address (Step 7), one day of pageviews, `'views': 657`, before the month (Step 10). B, with no Python before this term, finished all three parts on that basis: "look at one row, then ask for the table." C called it how it debugs SQL already; E said that when Step 8's anonymous request came back `403 HAProxy`, it knew at once it was the designed failure, because it had already seen the same call succeed.

**The typed cells are short and the plumbing is given, so the time goes to reading what came back.** No persona was stuck on a typed cell's syntax; A, C and E typed whole parts with no traceback. The loops, the `curl` filter (Step 5), the plots and the three-article comparison (Step 11), the three User-Agents (Step 12) and the Session race (Step 13) are given cells that say in their first comment what they do. D's planted R-style slip, `requests.get(PAGE, HEADERS)`, which sends the headers as query parameters, was caught by Step 1's "look first" print (cell 8): `403 Please set a user-agent and respect our robot policy`. "Without that cell I would have seen `'NoneType' object has no attribute 'text'` two cells later and blamed the selector." The three setup cells mean a student who misses Monday can start on Wednesday (A).

**The designed failures teach that "no error" is not "correct".** Step 8's four requests (200, 404, the anonymous 403, the 301) are, to D, "a small designed experiment with a control". The `AC/DC` check in Step 14 gives the API's own `invalid route` 404 for a slash that Python accepts without a word (D, E). Step 2's `Content-Length` of 121,745 against 768,542 unpacked bytes was new to C, D and E. B, a records person, read each refusal as information: "the `Server` header and body tell me who refused."

**The Discuss boxes ask about people and validity, right after the output that raises the question.** A and B named Step 0's "who reads your email address", Step 4's decision not to print one's own address ("notebooks end up on screens and in repositories"), and Step 8's "who refused us here, and how do you know?". D named Step 13's "is this a fair race?", Step 11's "which claims can this plot support?", and Step 8's "which do you believe?" when ip-api says San Francisco and the `Server` header names a data center in Texas. The lab also names what its code leaves out, no `try`, no `timeout=`, no retry, rather than hiding it (A, C, E).

**The lab points straight at the graded exercises.** Step 15 maps each Recommended Exercise step to the lab step that rehearses it. E called it "the best piece of pointing in the course so far"; C wrote `diagnose_url()` by putting its Step 8 cells in a `def` and adding `timeout=10`, which is the intended path.

## Where it falls short, ranked

The `robots.txt` conflict comes first, then the wrong-result problems. After them, items are ranked by how many personas hit each, how badly, and whether it stopped A or B. Cell numbers are positions in `labs/week-05/lab-05-key.ipynb` at `8ee384e`, counted from 0; the students' copy has the same cells. Every fix names a file on #211's branch, so it can be made before merging, except those marked as the textbook's.

1. **The lab sends every student to two paths that the hosts' `robots.txt` disallows, and invites requests to sites nobody has checked.**
   - **Who:** A, B, C, D, E.
   - **What happened:**
     - Step 7 (cells 50, 51 and 55, and the microsprint) sends `http://ip-api.com/json/...`. ip-api.com's `robots.txt` is one group, `User-agent: *`, that disallows `/json/` (and `/json$`, `/csv/`, `/xml/`, `/php/`, `/line/`, `/batch/`).
     - Step 14's cell 109 sends `https://en.wikipedia.org/w/api.php?action=query...`. en.wikipedia.org's `User-agent: *` group disallows `/w/`, with `Allow` lines only for `/w/api.php?action=mobileview&`, `/w/load.php?` and a sitemap.
     - The key tags neither `not-run-live`; it sent both. Its only tagged cell is `ping` (cell 39). Step 7's own text says "this room shares one address", so 30 or more students send the disallowed request together.
     - Step 5's microsprint (cell 40) says to `curl -I` "a site you read", and the deck's "Microsprint: another site's headers" says the same, with no word on `robots.txt`. A and C picked nytimes.com and got `403`, `server: DataDome`; its `robots.txt`, read afterwards, forbids automated use. A's reply also printed several screens of `set-cookie` lines into the notebook.
     - Exercise Step 5 (chapter and companion notebook) asks for "a site known to restrict automated access (@sec-post-api showed you one)". That site is Reddit, and chapter 3 itself says "reddit.com's robots.txt now disallows every path". No step says to read `robots.txt` first. B, C, D and E each had to hunt (E for about 20 minutes) for a fifth site whose `robots.txt` allows the request; the four ended on three different sites (an archive API, `httpbin.org/status/403`, and, for D and E, a job site's challenge page).
   - **Why it matters:** week 2 teaches students to read `robots.txt` before the first request. B, C, D and E did, and found the lab asking for what the files disallow, with no sentence about it; D "got a worse lab for it". A, the student who follows the lab as written, sent everything. Either way the week teaches that `robots.txt` is read after the fact, if at all.
   - **Proposed fix:** first the instructor's decision (below), then:
     - **Step 7, lab key (cells 49–56) and the deck's four Step 7 frames.** Either tag the three requests `not-run-live` and add a fourth checkpoint, `labs/week-05/data/ip-api-2026-11-17.json`, with the key's three saved answers, loaded by a given cell; or keep the requests and add one sentence to the step and one Discuss question: "ip-api's `robots.txt` disallows `/json/` for every client; its documentation offers this endpoint for programs. Which governs?" The chapter's `geolocate_ip()` has the same question (textbook).
     - **Step 14, lab key (cell 109) and the deck's "Step 14: let `requests` build it".** Either tag it `not-run-live`, so students read the key's saved `info.url`, which carries the step's lesson without a request; or keep it with one sentence: "`robots.txt` disallows `/w/` for crawlers; Wikimedia's API rules invite this call with a User-Agent." (B, D and E cite Wikimedia's API etiquette for that; not checked here.)
     - **Step 5's microsprint, lab key (cell 40) and the deck frame:** "Open the site's `/robots.txt` first. If it disallows automated clients, pick another, or use `https://www.colorado.edu/`, as the key does."
     - **Exercise Step 5, chapter and companion notebook (textbook):** "Read the site's `robots.txt` first; if it disallows the path, choose another." Name one refusing endpoint that `robots.txt` allows, such as `https://httpbin.org/status/403` (C, D).
   - **Status:** verified. Both `robots.txt` files read on 2026-11-18 (those files only); the key's tags read at `8ee384e`; cell 40, the deck frame, the exercise text and chapter 3's sentence read at the commits above.

2. **The redirect lessons can leave a student with a quiet wrong answer in the graded exercise.**
   - **Who:** A, B, C, D, E.
   - **What happened:**
     - Step 8's microsprint (cells 63–65) asks for `CU_Boulder`. It answers `200 []`: Wikipedia redirects inside the server, so `.history` is empty. Step 8's other redirect (cell 62) uses `allow_redirects=False`, so it shows `Location` but no `.history`. The lab never shows a non-empty `.history`.
     - Exercise Step 4 then asks `diagnose_url()` to check `response.history` "and if it redirected, print where it ended up". A got "No redirect" for every URL until it tried `http://en.wikipedia.org/wiki/...`, which printed `[301]`.
     - The chapter's `diagnose_request()`, which students copy from, prints `Redirected from: response.history[0].url`: where the chain started, not where it ended (`response.url`). D copied that line first and printed the URL it had typed (D, E).
     - Step 8's Discuss (cell 66) and the key's answer (cell 114) say `CU_Boulder` showed "another article's title". The title that came back is `University of Colorado Boulder`, the article the lab has used all week; A, B, C and D each read the claim as wrong.
   - **Why it matters:** the exercise is graded. A student who copies the chapter's line answers a different question with no error, and one who tests only `https://` addresses reports "no redirect" for a page that redirected. A and B, who can't reason past what they've seen, depend on the lab having shown it.
   - **Proposed fix:**
     - Lab key, cell 65 and the deck's "Microsprint: an alias": add `print(alias.url)`; and in the given cell, request `http://en.wikipedia.org/wiki/CU_Boulder` once and print its `.history` and `.url`, so a real 301 chain is on screen before the exercise.
     - Cell 66 and cell 114: "under the article's real title, not the alias", and one sentence: "Wikipedia redirects inside the server, so there is no 301 to see."
     - Chapter, `diagnose_request()` (textbook): also print `Ended at: response.url`.
   - **Status:** verified. Cells 62, 65 and 66 and the key's output of cell 65 (`200 []`, `University of Colorado Boulder`); cell 114's wording; the chapter's `diagnose_request()` and Exercise Step 4's text at `3f9cf2c`. The `http://` 301 is A's and E's observation.

3. **The deck describes a different week and lists the wrong homework.**
   - **Who:** A, B, C, D, E.
   - **What happened:**
     - "This week at a glance": Monday "Concepts & notebook intro"; Wednesday "Notebook lab", with "ping and traceroute from a notebook cell, a live API call, curl/wget"; Friday "Textbook revisions"; "Monday and Wednesday are both hands-on". The lab is three coding days, has no traceroute or `wget`, and calls the API on Friday.
     - "Key takeaways", item 2: "Traceroute and `curl -v`, run from a notebook cell". Traceroute is in "More from the terminal", marked as not in the lab.
     - "After class: work these, then show-and-tell" says "Do these exercises from the chapter" and lists six: three of the chapter's Additional Exercises (1, 2, 3), `diagnose_url()` on five kinds of URL, a `curl -v` marking task the chapter doesn't have, and the 5617 memo (Additional Exercise 5). Its right column then says the Recommended Exercises are due Sunday. The six Recommended Exercise steps appear only in the lab's Step 15 and the chapter.
     - "Lab 5: one page, down the stack" says "Nothing to submit" (true of the lab) beside the "due Sunday" of the exercises (C, E).
   - **Why it matters:** a student who reads only the slides prepares the wrong days (B: "I walked into a different week") and could spend the weekend on the wrong exercises (A: "found the real one at 10 p.m. Sunday").
   - **Proposed fix:** `slides/week-05/week-05.tex`. The at-a-glance frame is the instructor's: #211 proposes a three-part wording, and `docs/course-facts.md` lists it as not yet changed. Key takeaways item 2: "`curl -v`, run from a notebook cell, makes the transport layer observable" (no traceroute). "After class": list the six Recommended Exercise steps by number, as Step 15 does, then the others as "optional". "Lab 5": "Nothing to submit from the lab; the chapter's exercises are due Sunday."
   - **Status:** verified: the four frames at `8ee384e`; #211's description says it left the at-a-glance frame, the Key takeaways and the "After class" list alone on purpose, so these are the instructor's calls.

4. **A 429 in Step 11's given loop shows up as a JSON error, then a `NameError`.**
   - **Who:** A, C, E; B and D met 429s elsewhere.
   - **What happened:** cell 88 calls `reply.json()` with no status check. On a 429, Wikimedia answers in plain text ("You are making too many requests"), and the cell stops with `JSONDecodeError: Expecting value: line 1 column 1 (char 0)`. Cell 90 then fails with `NameError: name 'compare' is not defined` (E). The only guidance is cell 89's comment, "only if the cell above stopped", and Step 10's Discuss question about a 429. Before #211 merges, the fallback itself 404s and fails the same way (B, D). Step 14's microsprint (cell 111) asks students to predict the raw `AC/DC` answer; A got a 429 in its place and couldn't tell what the server made of the slash.
   - **Why it matters:** a room behind one address is the likeliest place for a 429, and this is the week's commonest failure in the reviews. A and B read only a traceback's last line, and this one points at JSON. C knew what to do only because Step 10's Discuss had primed it; E had to print the status itself.
   - **Proposed fix:** lab key, cell 88: `print(title, reply.status_code)` after the request (still given). Cell 89's comment: "a `JSONDecodeError` above means the server sent text, not JSON: most likely a 429. Run this cell." Cells 37 and 79 the same. Step 14's microsprint text: "a 429? wait a minute and run it once more."
   - **Status:** verified: cells 88–90, 79 and 111 read at `8ee384e`. The 429 body and error texts are A's, C's and E's observations.

5. **Parts 2 and 3 don't fit their days by the lab's own minutes.**
   - **Who:** A, D (pace 2); B's estimates, 70–80 and 75–90 minutes, say the same.
   - **What happened:** Part 2's headings add to 59 minutes (49 in steps, 10 in microsprints) against Wednesday's 50, and Part 3's to 43 (37 and 6) against Friday's 35, before Friday's 15-minute block and before the 15 Discuss boxes. Part 1, at 35, is under Monday's 50 on purpose, since the instructor's concept frames share Monday. #211's description counts 49 and 37 against budgets of 55 and 40; that counts steps without microsprints, against budgets above `docs/course-facts.md`'s "about 50, 50 and 35".
   - **Why it matters:** the Discuss boxes, the part D values most, are what a running-late class cuts. A doesn't reach Step 8's status codes on Wednesday, the step the exercises use most.
   - **Proposed fix:** the instructor's decision. Candidates:
     - If Step 7 becomes a checkpoint (item 1), its 8 minutes and its 3-minute microsprint go, and Part 2 is 48.
     - Mark Step 8's microsprint or Step 6's `socket` cell (47) "if time" (D); make one of Step 8's typed cells given (A).
     - Part 3: one article in Step 13's race instead of three, or Step 14's `urlencode`/`info` pair "if time" (D).
     - Say in each part's heading which Discuss boxes to keep (D).
   - **Status:** verified: the headings in the key at `8ee384e`; course-facts at the same commit; #211's description.

6. **Step 13's typed cell asks for `elapsed` "in seconds" without saying how.**
   - **Who:** B, C.
   - **What happened:** cell 99's prompt ends "then first.elapsed, in seconds". `print(first.elapsed)` prints `0:00:00.114745`, a `timedelta`. Step 13's text explains `elapsed` but not `.total_seconds()`, which appears first in the given cell after it (cell 100).
   - **Why it matters:** it breaks "the prompt tells you everything" for the student with no Python (B), who either stalls or prints something that doesn't answer the prompt.
   - **Proposed fix:** lab key, cell 99's prompt: "then `first.elapsed.total_seconds()`"; or one clause in Step 13's text. The deck's "Step 13: one request with it" already shows the code.
   - **Status:** verified: cells 99 and 100 and Step 13's text.

7. **Step 13's race prints a number students will repeat, and it isn't a fair one.**
   - **Who:** C, D, E (E's is Part 3, written blind).
   - **What happened:** the given loop (cell 100) times `bare` first and `session` second for each article. The session's connection was already opened by cell 99, and the second request may also find the page in Wikimedia's cache that the first just warmed (D). The key prints `bare` 0.15 to 0.49 seconds against `session` about 0.026; the personas got 8 to 15 times. `elapsed` also stops at the headers. The Discuss box asks "is this a fair race?", but the printed ratio is what students remember: "sessions are 8 times faster" (E), "a number I'd put on a slide" (C).
   - **Why it matters:** C, D and E each named this as the claim they would carry into a project.
   - **Proposed fix:** lab key, cell 100, and the deck's "Step 13: bare against the session, given": print the labels as "bare (new connection)" and "session (connection already open)" (C), and swap the order on the second article so the session goes first (D). One sentence in Step 13's text: "one measurement each, in a fixed order".
   - **Status:** verified: cell 100's order and the key's output. The cache effect is D's reading of the `x-cache` headers, not tested.

8. **Step 8 says what `Server` names, but not the answer its own Discuss question needs.**
   - **Who:** B, D; E (Part 2, not blind).
   - **What happened:** Step 8's text says `Server` names "Wikimedia's cache (`ATS`), or a web server named for its data center". The 403 to the anonymous request comes from `HAProxy` (cell 61), and Step 8's Discuss asks "who refused us here, and how do you know?". The text never names HAProxy. B, D and E saw `mw-web.codfw...` and `HAProxy` and never `ATS`; D also asked for a half-line on `x-cache` (`cp2053 miss, cp2053 hit/10`) and `age`.
   - **Why it matters:** B "would have searched for ATS and found nothing"; the Discuss question's answer is a name the step never gives.
   - **Proposed fix:** lab key, Step 8's text (cell 57): "you may see `ATS`, a web server named for its data center, or `HAProxy`, Wikimedia's front door". Step 2's given cell comment (16): "`cp…` is a cache server; `hit/10` means it has served this copy 10 times".
   - **Status:** verified: cell 57's text, and the key's outputs: Step 8's article answered `ATS/9.2.16` and the anonymous request `403 HAProxy` (see "Corrections"). The `hit/10` reading is D's, not checked.

9. **Step 2 teaches `headers["Content-Length"]` before the safe form, and the exercise knows the header can be missing.**
   - **Who:** A, D, E; C as a small thing.
   - **What happened:** cell 15 reads `page_response.headers["Content-Length"]` with brackets; cell 16, given, uses `.get()` and says why. Exercise Step 3 asks for `Content-Length` "or the length of `response.content` if the header is absent". It worked for all five on Wikipedia (121,745), but a student who reuses the line on the microsprint's site or Exercise Step 5's URLs gets `KeyError: 'Content-Length'`.
   - **Why it matters:** the failure arrives in the graded exercise, far from the cell that taught it.
   - **Proposed fix:** lab key, Step 2's text (cell 13): "`[...]` raises `KeyError` when a header is missing; the given cell's `.get()` gives `None` instead." Leave cell 15 typed as it is.
   - **Status:** verified: cells 13, 15 and 16, and Exercise Step 3's text.

10. **The companion notebook's exercises start with no setup cell, and its text carries 21 raw cross-references.**
    - **Who:** B; C for the `@sec-post-api` pointer.
    - **What happened:** the exercise cells (48–59 of the notebook) import nothing and define no `HEADERS`; B had to work out `urlparse`, `dns.resolver`, `requests` and the header line. The notebook's text has 21 unrendered `@sec-…` references, among them Step 3's "(@sec-ethics)" and Step 5's "(@sec-post-api showed you one)", which C couldn't follow to a site.
    - **Why it matters:** the exercises are done at home, from a fresh kernel.
    - **Proposed fix:** textbook, companion notebook: one given cell above Step 1 with the imports and `HEADERS` (a placeholder address), and chapter names in place of `@sec-` references in the notebook's text.
    - **Status:** verified: `notebooks/ch-05-protocols.ipynb` at `3f9cf2c` (no imports in cells 48–59; 21 `@sec-` matches in its text).

11. **Step 11's microsprint asks for a cause of a "spike" that is barely above a month's noise.**
    - **Who:** D.
    - **What happened:** the microsprint asks which article had the biggest spike and "a guess at why"; the Discuss asks how to check. On the checkpoint's table, each article's biggest day is 2.4 (CU Boulder, 902 on Jan 22), 2.5 (Colorado State) and 2.7 (Denver) standard deviations above its January mean, where the largest of 31 normal draws is about 2.0 on average. CU Boulder's weekday mean runs 708 to 739 and its Saturday mean 579.
    - **Why it matters:** D: "I am the student who will write 'a spike on Jan 22, probably an event' and be satisfied." The lab gives no baseline to check against.
    - **Proposed fix:** lab key, cell 90 (given): print each article's mean and standard deviation with its biggest day, and ask in the Share line: "is the biggest day more than about two standard deviations above that article's mean?"
    - **Status:** verified: computed from `labs/week-05/data/pageviews-three-articles-2026-01.csv` at `8ee384e`.

12. **Step 2's microsprint counts can't be checked, and its filter names are Chrome's.**
    - **Who:** A, C, E.
    - **What happened:** the microsprint (cells 18–20) asks for counts under the **Doc**, **CSS**, **JS**, **Img** and **Fetch/XHR** filters, "the rest are Other". Nothing says to take Other as the total minus the five, or whether cached rows count; the given cell charts whatever is typed. The lab says Chrome, Firefox or Safari, and E expects Firefox and Safari to name the filters differently.
    - **Why it matters:** a miscount gives a clean chart and no signal (A, C).
    - **Proposed fix:** lab key, cell 18: "Other is the total, from the status bar, minus the five"; "turn on Disable cache"; one line naming Firefox's and Safari's filters, after checking each.
    - **Status:** reported, not verified: no browser on the review machine.

13. **Step 1's microsprint invites a long copied selector that may not match what `requests` gets.**
    - **Who:** E (Part 1, blind).
    - **What happened:** E wrote the selector Chrome's Copy selector would give for a paragraph, `#mw-content-text > div.mw-content-ltr.mw-parser-output > p:nth-child(6)`, and got `None`, then `AttributeError`. In the HTML `requests` gets, the paragraphs sit inside `<section>` elements. The key uses `#siteSub`, an `id`. The Discuss box suggests the cause is JavaScript; here it is a different structure.
    - **Proposed fix:** lab key, cell 10: "prefer an element with an `id`; a long copied chain with `nth-child` often fails in Python"; and one line in cell 12's Discuss.
    - **Status:** reported, not verified: whether Chrome's copied selector includes the `section` needs a browser.

14. **Steps 4 to 7 say what they do, not why a student would need it.**
    - **Who:** A.
    - **What happened:** A, whose project is about online communities, couldn't see when it would use a TTL, an IP geolocation or `curl` in its own collection; the link comes only in Step 15.
    - **Proposed fix:** lab key, Part 2's opening (cell 23): one sentence, "you won't do this by hand in a project; you'll recognise it when a collector fails", naming the failure each step explains (a name that won't resolve, Step 6; a site that thinks you are elsewhere, Step 7; a 403, Step 8).
    - **Status:** reported; a judgment about framing.

15. **Steps 2 and 8 produce numbers, then don't use them.**
    - **Who:** C.
    - **What happened:** Step 2 prints 121,745 and 768,542 and never asks for the ratio (about 6 to 1). Step 8 makes four requests but never puts status, type, server and size in one table, which Exercise Step 5 then asks for.
    - **Proposed fix:** lab key: one Discuss question in Step 2 ("how much smaller did gzip make it?"); optionally a given cell after Step 8 that builds the four-row table, `diagnose_url()` in miniature. It adds minutes to Part 2 (item 5).
    - **Status:** reported; the numbers are verified in the key's outputs.

### Corrections

Claims in the reviews that turned out wrong or inexact, and what this document does with them:
- **"Never `ATS`" (B, D, E).** The key's own run got `ATS/9.2.16` for Step 8's article (cell 59) and `mw-web.codfw…` for Step 2's: `Server` varies from run to run. Step 8's text is right as far as it goes; item 8 asks only that it name HAProxy too.
- **"The weekday pattern is larger than the spike" (D).** On the checkpoint, CU Boulder's Thursday mean is 708 and Jan 22 is 902, 194 above it; the weekday-to-Saturday gap is about 160. They are comparable, not one larger. D's z-scores are right. Item 11 uses them.
- **"16 unrendered cross-references" (B).** The notebook's text has 21 `@sec-` references. Item 10 uses 21.
- **Pace ratings.** B rates pace 4 but estimates Parts 2 and 3 at 70–80 and 75–90 minutes, well over the days; item 5 goes by the estimates and the lab's own minutes.
- **The deck's "After class" items "are the chapter's Additional Exercises" (A, B).** Mostly: items 1–3 are Additional Exercises 1–3 and item 6 is Additional Exercise 5, but item 4 is close to Recommended Steps 4 and 5, and item 5 (`curl -v`) is in neither list (E). Item 3 says so.

## Disagreements

- **Too slow, or about right.** A and D rate pace 2 and go by the lab's minutes: 59 against 50 and 43 against 35. B, C and E rate it 4, though B's own estimates are the longest of the five. C and E put the time in the browser steps and the waits for 429s, not the typing. That suggests the minutes are tight by the lab's own count before any student is slow, and that a 429 in a busy room, not the code, is what pushes a part over.
- **Too easy, or about right.** C, D and E rate difficulty 2. A wrote 4 with "comfortable … a little too easy to type without thinking", so on this scale A means about 2 as well; B, with no Python before, rates 3. E would like one step a part that asks students to change a given cell (a status check in cell 88, a warm-up in Step 13) rather than only read it. For A and B the transcription is the point; for D and E the concepts came "mostly from the Discuss boxes rather than the cells".
- **What to do about Step 7 and Step 14.** B and C would replace Step 7's requests with a saved response; D would show Step 14's built URL without sending it; E says ip-api's and Wikimedia's API terms may well allow both, and asks only that the lab say so. A sent them. Which one is right depends on the instructor's reading of `robots.txt` for documented APIs (item 1).
- **Which fifth site.** B chose an archive API that answered `403` from a CDN; C `httpbin.org/status/403`; D and E a job site that answered `401` with a challenge page; A reused its nytimes.com reply. Each was defensible; none came from the materials (item 1).
- **How to fix the race.** C would relabel the output; D would swap the order and print a median of three; E would add a warm-up request. Relabelling costs nothing and keeps the cell's length; item 7 proposes it with D's swap.
- **What the week is for.** For A and B, who sees what: the User-Agent, the masked address, the refusal's sender. For C and D, numbers to check: compression, timings, a baseline for the spike. For E, the tools: `curl`, `Session`, `quote()`. C, D and E rate confidence 4; A and B 3, because neither knows what to do on a site whose `robots.txt` disallows it, or that answers 200 with the wrong content.

## Ratings

Each on a scale of 1 to 5. For difficulty, 5 is hardest for that persona's background.

| | A | B | C | D | E | Mean |
|---|---|---|---|---|---|---|
| Clarity of motivation | 3 | 4 | 4 | 4 | 4 | 3.8 |
| Pace | 2 | 4 | 4 | 2 | 4 | 3.2 |
| Difficulty for my background | 4\* | 3 | 2 | 2 | 2 | 2.6 |
| How much I learned | 3 | 4 | 3 | 4 | 3 | 3.4 |
| Confidence I could do this on my project | 3 | 3 | 4 | 4 | 4 | 3.6 |

\* A's 4 comes with "comfortable … a little too easy", which on this scale reads as about 2; with 2, the mean is 2.2.

What holds the ratings down: the `robots.txt` contradiction (B, C, D, E: item 1); the deck's week and homework (A, B, E: item 3); the minutes (A, D: item 5). What holds confidence down: A and B don't know what to do on a site that disallows them or answers 200 with the wrong content; D wants a baseline for time series and "a clear rule on which hosts I may hit"; E would still have to add status checks, `timeout=` and backoff to a real collector.

## Small things

Deck (`slides/week-05/week-05.tex`):
- "Loading a web page, step by step": "debugging requires diagnoses each part" should read "diagnosing each part" (C).
- "ARPANET and the bomb" says Baran proposed packet switching to survive a nuclear attack; the chapter calls the ARPANET version of that story a "false rumor". The two are consistent only on a close reading; a half-line, "Baran, yes; ARPANET, no", would help (D).
- "A revision menu for Chapter 5": "The chapter still has zero diagrams". The chapter has four figures (D; verified).
- "Closing activity" (Monday) overlaps Step 2's microsprint (B); #211 already proposes trimming it.
- The title frame's date, September 14, 16 & 18, 2026, is left for the next offering on purpose (#211).

Lab (`labs/week-05/lab-05-key.ipynb`):
- Step 5's text: "The last cell is optional", but the `ping` cell (39) is followed by the microsprint (E; verified).
- Step 0's text: "Cells that start with `# Given:`"; several start `# Given, only if …` or `# Given, optional:` (E).
- Step 7 needs Step 6's `WIKI_IP`; a student who restarts mid-Wednesday at Step 7 gets a `NameError`. "Needs Step 6" at its top (C).
- Step 7's given cell 55 reads `sprint_location["country"]`; if ip-api answers `{"status":"fail"}`, that is a `KeyError: 'country'` with no hint (B).
- Step 13's text says Wednesday's `curl -v` narrated the TLS handshake; the narration shows one line of it, `* SSL connection using TLSv1.3 …` (C).
- Step 14: the step's text introduces `quote()` before `urlparse()`; the cells run the other way (A). `Boulder,_Colorado` worked unquoted in Step 11, a ready counter-example for Step 14's Discuss (E).
- Step 15's mapping says Exercise Step 3 asks why `Content-Length` and `len(response.content)` differ; the exercise asks for the second only when the first is absent (A, B).
- Step 1's microsprint key uses `#siteSub`, which is in the raw HTML but hidden by the default skin, so "Python found what the browser doesn't show" is a possible result the Discuss box doesn't expect (D).
- Step 12's Discuss question about the key `"UserAgent"` could be a one-line typed microsprint (D).
- Found while verifying: Step 0's setup prints `HEADERS` (cell 3), cell 99 prints `session.headers["User-Agent"]`, and Step 12's echo prints the User-Agent back, each with the student's email address, while Step 4 masks the public address because "notebooks end up on screens and in repositories". Printing `PAGE` and the statuses without the User-Agent would be consistent with Step 4.

Chapter and companion notebook (`ch-05-protocols.qmd` at `3f9cf2c`):
- `geolocate_ip("151.101.130.133")` reads as Wikipedia's address; in D's DNS answers it belongs to `www.colorado.edu`'s CDN, and Wikipedia's is `208.80.153.224` (D; reported, not verified).
- `geolocate_ip()` sends no User-Agent; the lab's Step 7 Discuss and its Friday list already raise it (E).
- The Network-tab figure counts 37 requests; the key's microsprint has 45. The lab's Friday list already asks about it (B, D).
- `diagnose_request()` catches only `ConnectionError` and `Timeout` and returns `None` otherwise, so a loop over its results must guard for `None` (E).

## Suggested next step

**Check right after #211 merges:** that `labs/week-05/data/curl-v-2026-11-17.txt`, `pageviews-cu-boulder-2026-01.json` and `pageviews-three-articles-2026-01.csv` answer 200 at the `DATA` address on `main`, since the three fallback cells (37, 79, 89) read them there.

**Fix first, on #211's branch.** Each is small and changes none of what the week teaches:
1. **Item 1, the parts that need no decision:** "read `/robots.txt` first" in Step 5's microsprint and its deck frame, with `colorado.edu` named as a safe choice.
2. **Item 2:** `print(alias.url)` and one `http://` request in cell 65 and its frame; "the article's real title, not the alias" in cells 66 and 114.
3. **Item 4:** a status print in cell 88, and "a `JSONDecodeError` means a 429" in the comments of cells 37, 79 and 89.
4. **Items 6 and 8:** `.total_seconds()` in cell 99's prompt; HAProxy in Step 8's text.
5. **Item 3, the frame #211 rebuilt:** "Lab 5", "Nothing to submit from the lab; the chapter's exercises are due Sunday".

**Needs the instructor's decision:**
- **How strictly to read `robots.txt` for a documented API** (item 1): ip-api's `/json/` and Wikipedia's `/w/api.php` are disallowed for every client, and both services document those endpoints for programs. Tag Step 7 and cell 109 `not-run-live` with a checkpoint, or keep them and say why in the step. The same reading decides the chapter's `geolocate_ip()`.
- **The deck's at-a-glance, "After class" and "Key takeaways" frames** (item 3), which #211 left alone on purpose; it proposes wording for the first.
- **The minutes** (item 5): 59 against 50 and 43 against 35, and what becomes "if time". Making Step 7 a checkpoint would close most of Wednesday's gap.
- **The textbook's exercise fixes** (items 1, 2 and 10): `robots.txt` and a named refusing endpoint in Exercise Step 5, `Ended at: response.url` in `diagnose_request()`, and a setup cell in the companion notebook. These go to the textbook repository, not #211.
