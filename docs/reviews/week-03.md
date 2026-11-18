# Review: week 03, The Post-API Age

**What was reviewed:** week 3's lab (`labs/week-03/lab-03.ipynb`, with its key `lab-03-key.ipynb`), its checkpoints (`labs/week-03/data/access.csv` and `servers.csv`), its deck (`slides/week-03/week-03.tex`) and chapter 3's Recommended Exercises, as students meet them.
- **Course repository:** the head of pull request #212 (branch `claude/style-week-03`), `e136c6995783c3182a644f1b94c25f8110786721`, which rebuilt the lab in two parts (Wednesday and Friday) in the incremental style and added deck frames for its typed cells. #212 is open and not merged, so every fix below names the file on that branch it would change.
- **Textbook:** `ch-03-post-api.qmd` and its companion notebook at `main`, `3f9cf2cef801181236c9cceaf71f3b63c3ad2491`. (The key cites d9306b7; #212 says chapter 3 hasn't changed since.)

**When:** 2026-11-18.

**Method:** five anonymous composite personas, each a kind of student this course has, reviewed the week independently. Each read the chapter and the slides, typed and ran its own code for every lab step it could from the students' copy, made the mistakes its background makes, attempted the Recommended Exercises, and opened the key only after an honest try. Each review is a **steel man**: it first makes the strongest case for the materials as designed, and only then says where they fall short for that student. This document puts the five together. Every ranked finding was then checked against the repository and the textbook, and is marked **verified** (with how) or **reported, not verified**.

The reviews ran on a cloud machine under the rule the key followed for its own run: read a host's `robots.txt` first, and send nothing to a path it disallows to automated clients or to named AI crawlers. Cells the key tags `not-run-live` were read from the key's saved output or the checkpoints, not sent. That rule is why much of Part 1 was read rather than run; it is listed under "Environment blocks", not counted as a flaw. Whether students' requests should follow the same strict reading is a separate question, and the instructor's (items 4 and 5).

## Who reviewed

| | Degree and major | Python and data background | Interest | Skill |
|---|---|---|---|---|
| A | BS senior, Information Science | One intro Python course; spreadsheets | Qualitative and design: online communities, UX | Minimal |
| B | BA junior, Journalism and Communication | No Python before this course; strong with public records and Excel | Data journalism, local government | Minimal |
| C | BS senior, Business Analytics | Excel, some SQL, a little pandas | Quantitative analytics: markets, customer data, dashboards | Minimal to moderate |
| D | MS first year, Data Science (BA in Statistics) | Fluent in R, moderate pandas; regression and sampling | Quantitative: measurement and validity | Moderate |
| E | MS first year, Information Science (BS in Computer Science) | Moderate Python, git; little data analysis | Design and tools: automation, APIs, building things | Moderate |

**Method notes.**
- **B saw the key first.** While checking which cells were tagged `not-run-live`, B printed the key's code and saved outputs before typing its own cells, and says so. B wrote its cells from the prompts and added three beginner's mistakes by hand. B's "I got unstuck by myself" findings (item 14) carry less weight than A's and C's.
- **E sent one request a `robots.txt` disallows.** Testing a likely mistype, E asked `hacker-news.firebaseio.com/v0/item/1` (no `.json`) once. Hacker News's `robots.txt` allows only paths ending in `.json`. E reported it and didn't repeat it. #212's own table of mistypes tried live lists the same request.
- **B read OpenSecrets's `robots.txt` differently from the others.** Its `User-agent: *` group says `Allow: /`; a list of named AI crawlers is disallowed `/`. B read the `*` group and sent one request (exercise Step 6); A, C, D and E read the named list as covering the review machine and sent nothing. Both readings of the file are accurate; they differ on which group applies.

## What each completed

Part 1 (Wednesday) is Steps 0–5 and three microsprints; Part 2 (Friday) is Steps 6–10 and two microsprints. Cell numbers below are positions in the key at `e136c69`, counted from 0; the students' copy has the same 77 cells.

| | Lab: run live | Lab: read, or run on the checkpoints | Recommended Exercises | Needed the key for |
|---|---|---|---|---|
| A | 0, 1 and its microsprint, 3's `VERDICTS`, 5's HN cell, 6, 7 (loop without the Twitter row), 8 and its microsprint, the timeline | 2, 3's Wikipedia and X cells, 5's Reddit and default-User-Agent cells, 9's typed cells; loops 4, 5, 9 replaced by checkpoints; 10 planned | 1–5 and 7; 6 on Sunlight only (failed at TLS, nothing sent) | Saved outputs of the not-run-live cells |
| B | 0, 1 and its microsprint, 4 (HN and Bluesky rows), 6, 7 (Pushshift), 8, the timeline | 2, 3's Wikipedia and X, the rest of 4, 5's Reddit and default cells, 7's other rows, 9 (plot from `servers.csv`); 10 answered | 1–6; 7 weakened (one Step 6 target) | Printed the key before typing (see Method notes) |
| C | 0, 1 and its microsprint, 3's `VERDICTS`, 4's microsprint on the saved table, 5's HN cell, 6, 7 (Pushshift), 8 and its microsprint, the timeline | The nine `not-run-live` cells; loops 24, 36, 48, 69 from saved output; 9's plot from `servers.csv`; 10 in its head | 1–5 live; 6 not done (no host sendable); 7 drafted | Saved outputs of the loops only |
| D | 0, 1 and its microsprint, 7 (Pushshift and `CAUSES`), 8 and its microsprint | 2–5 on checkpoints and stand-ins built from the chapter's printed values (2 of 8 hosts asked live in 4), 9 typed not sent, plot drawn; 10 answered | 1–5 and 7; 6 typed, not sent | Nothing |
| E | 0, 1 and its microsprint, 3's `VERDICTS`, 4 (cut down; microsprint on the checkpoint), 5's HN half, 6, 7 (Pushshift), 8 and its microsprint, the timeline | 2, 3's Wikipedia and X, 5's Reddit and default cells, 7's other rows, 9 typed (plot from the checkpoint); 10 in its head | 1–5 live; 6 written, not sent; 7 from partial evidence | Nothing |

**Estimated time for a real student of that background, in minutes** (the lab's own minutes in the last rows):

| | Part 1 | Part 2 | Exercises |
|---|---|---|---|
| A | 75–85 | about 60 | about 180, an hour of it finding Step 4's endpoints |
| B | 75–85 | 60–70 | 120–150, "plus the chance of a 429 on the anchor" |
| C | 60–75 | 45–55 | 120–150 |
| D | about 55 | about 45, then the Friday block | about 90, most of it reading `robots.txt` files |
| E | about 50 (35 typing, 15 reading) | about 40 | about 120, 40 of it choosing endpoints and reading `robots.txt` |
| **The lab** | **61** (48 in steps, 13 in microsprints) | **43** (35 in steps, 8 in microsprints) | none given |
| **The day** | **about 50** | **about 35**, then the 15-minute revision block | due Sunday |

## Environment blocks

These come from the review machine, not from the materials. They are kept apart so that none is read as a flaw in the week.

- **Hosts not asked, by the review rule (all five).** Reddit, `api.twitter.com`, `export.arxiv.org`, `graph.facebook.com` and Wikipedia's `/w/` disallow the lab's paths to every client; mastodon.social and mastodon.online disallow named AI crawlers. So Step 2, Step 3's two requests, Step 5's Reddit and default-User-Agent cells, Step 7's Twitter v1.1 row, all of Step 9's requests and most of the Step 4 and 5 loops were read, not sent. The key's nine `not-run-live` cells have no saved output, so for those the personas had only the chapter's printed values and the checkpoints (item 9 is about what that means for a student).
- **Unreadable `robots.txt` files.** `api.crowdtangle.com` (a proxy error from the review machine, which is also the chapter's CrowdTangle finding), `api.census.gov` (a "Request Rejected" page, C, D, E) and, for B only, `api.worldbank.org` (a 502). Whoever couldn't read a file sent that host nothing.
- **OpenAlex's keyless budget was spent (all five).** The budget is per IP address, and all five reviewers shared one. A, B, D and E got 429 on the anchor; C got a 200 with 4 of 1,000 credits left, then a 429 seconds later. This is the review machine, but it is also what the chapter predicts for a campus network (item 13). One 429 body carried instructions for getting a key by a request; no reviewer acted on it.
- **The Wayback Machine.** E got a 429 on its fourth probe, three seconds apart, so couldn't retest the `"time"` mistype. A and B got a 200 whose body said the archive's own lookup timed out (item 1); whether a laptop would see it is unknown.
- **Federal Register** answered A once with a 403 `text/plain` and with 200 a minute later.
- **The checkpoints' raw address on `main` 404s** until #212 merges; every persona read the CSVs from the branch instead. That is a merge-order item, not a block: item 6.

## The strongest case for the week as designed

**Every service gets one small request whose answer can be predicted, printed before it is parsed.** All five named this first. Step 1 asks what item 1's `type` will be, and tells students the line they should see (`"title":"Y Combinator"`), so the first request has a right answer: B "could tell whether I typed it correctly", C predicted it and got it, and D, who would "normally reach for a tidy table first", called printing the status and the raw text before `.json()` "the right habit". The three parts of a `Response` (status, `content-type`, start of the body) are then reused on Reddit in Step 2, so its `403 text/html` reads as a comparison with Hacker News's `200 application/json`, not a surprise (C, D, E). A's own slip, `r.json["title"]`, "made sense only because the step before had me look at the raw text first". E checked the Discuss claim that `item/0.json` answers `200 null` and found it right: a "status code won't warn you" lesson that doesn't depend on a flaky host.

**One case by hand, then the given loop that repeats it, works for this audience.** "Find your two requests in the loop before you run it" was singled out by A, B, D and E: for B, the Step 4 loop was "what I did twice, done eight times … the first time a loop in this course made sense to me instead of being a block I copied". The typed cells are one to four lines, and the given cells carry what a minimal student would botch: `.items()`, `.split(";")[0]`, the one `try` ("the error is the finding"), the plots and the bookkeeping (A, B, C). E, who expected given cells to hide too much, found that each repeats a request just typed and does one job.

**Step 8 is the best-paced step of the week.** C, D and E each called it their favourite: the params dict, the whole body, then one level down at a time, then an address nobody archived that answers `200` with `"archived_snapshots": {}`, and only then a loop using `.get("closest", {})`, "by then motivated" (E). D: it "teaches the difference between 'the request worked' and 'the question was answered', which is the validity point I care most about". B would use it on a story, to show what a page said on a date. (Item 1 is about what its microsprint can and can't conclude.)

**The week treats measurement honestly, and asks about the people on the other side.** `AUDIT_DATE`, the chapter's table as a dated snapshot, Step 4's "platform changed, or something on our side?" and Step 5's "rule out the boring explanation" were what D valued; A called Step 5 "the one piece of this week I would use on my own project". The Discuss boxes on who reads a User-Agent, what `robots.txt` is for and "who paid" for Cambridge Analytica, and Step 1's instruction to print a story's field names but not its author, are what A and B said they'd remember. The checkpoints mean a refusal doesn't end anyone's class: B used them four times "with no friction", and Step 6 lets a student start Friday cold (A, C, E).

**The lab leads straight into the exercises.** It is the chapter's audit run live, so the Recommended Exercises ask for the same moves on new hosts (E), and Step 10's "Recommended Exercises ahead" maps each exercise step to a lab step. C and D called the resulting exercises "a much better fit than a bare 'probe some APIs' task".

## Where it falls short, ranked

No persona found a cell that prints a private person's contact details: Step 1's microsprint keeps a story's author off the screen, and Step 9 prints only the start of a post. The wrong-result problems come first (items 1–3). After them, items are ranked by how many personas hit each, how badly, and whether it stopped A or B.

1. **Step 8's microsprint can "confirm" the chapter's CrowdTangle claim for the wrong reason.**
   - **Who:** A, B, D, E; C read it as confirmation, which is the risk.
   - **What happened:** the microsprint asks whether the archive "ever handed you one from after 14 August 2024". The given loop (cell 63) prints only `nearest.get("timestamp")` and `nearest.get("status")`. Two things hide behind it:
     - For `20241201`, A and B got `20241201 -> None status None`. The body was a 200 with `"archived_snapshots": {}` and an `"error"` whose code was `timeout`; the loop never prints `"error"`. "None" reads as "no capture near December 2024", the claim being tested (B: "a journalist would write 'the archive has no capture' on the strength of that printout").
     - When it works, every answer has `status 200`, and `20241201` and `20250601` both return the 14 August capture. D and E: the availability API appears to return only captures that answered 200, so later captures that record a redirect could never appear; the result would look the same if they existed or not. The deck's "Step 8: read into it" frame says `status` "is the code the archive received that day", and the Friday block asks "Did the availability API show you what the chapter describes?" Honest answer: it can't. C's review says the claim was "confirmed by me, in four short lines".
   - **Why it matters:** the lab's own lesson is that a 200 isn't an answer; here the given loop turns an error into a finding.
   - **Proposed fix:** lab key, cell 63: add `print("   error:", dated.json().get("error"))` to the given loop (one given line). Step 8's text (cell 54) or the microsprint (cell 61): "this API returns the closest capture that answered 200, so it can't show you a redirect: what it can show is that none after 14 August answered 200". Deck, "Step 8: read into it, one level at a time": the same correction to the `status` sentence. The Friday block's "sentence to check" (cell 76) could point to the chapter's @fig-crowdtangle-last-capture, which shows the captures to 12 December 2024. (D and E suggest the CDX API for the real test; that is week 7's tool, so a pointer is enough.)
   - **Status:** the loop, the microsprint, the deck sentence and the key's saved output (`20241201 -> 20240814023608 status 200`) verified by reading. The timeout body is reported by A and B, identically. That the API skips redirect captures is reported, consistent across A, C, D and E, not verified.

2. **The lab's Step 7 loop and the chapter's `autopsy()` label an expired certificate "host does not answer", and a web page "still open".**
   - **Who:** A, B, C, D, E.
   - **What happened:** exercise Step 6's three retired endpoints don't fail like the chapter's three, which is the exercise's point, but the chapter's tool mislabels two of them:
     - Sunlight's host answers with an expired TLS certificate. `requests` raises `SSLError`, a subclass of `ConnectionError`, so both the chapter's `autopsy()` (which catches `RequestException`) and the lab's Step 7 loop (which catches `ConnectionError`) print "host does not answer". A got exactly that. D: "a student who runs it on Sunlight will write 'gone' for a server that is still up."
     - OpenSecrets's old API address answers `200` with its website, `text/html`. `autopsy()` classifies by status code alone, so B got `still open`, with `<!DOCTYPE html>` as evidence.
   - **Why it matters:** these are the wrong answers to Step 6 and to Step 7's "is there anyone left to negotiate with", produced by the chapter's own function. The chapter's Step 5 says to read the content type first, but `autopsy()` doesn't.
   - **Proposed fix:** chapter and companion notebook, exercise Step 6: one hint, "`autopsy()` reports the exception's name: an `SSLError` means the host answered with a certificate it couldn't prove; print `str(error)[:100]`. If it says 200, check the `content-type` before believing it." Optionally, add `content_type` to `autopsy()`'s row. If `autopsy()` changes, the lab's Step 7 loop (cell 48), which mirrors it, should follow (`docs/course-facts.md`, "Facts that live in more than one place").
   - **Status:** verified: the chapter's `autopsy()` at `3f9cf2c`, the lab's cell 48, and `requests.exceptions.SSLError`'s bases in requests 2.34.2; Sunlight's expired certificate by reading its `robots.txt` (`certificate has expired`). The OpenSecrets 200 page is reported by B.

3. **The `verdict` column is one request's status code, and the lab doesn't say what it can't support.**
   - **Who:** C, D; A and E for the `rate_limit` column.
   - **What happened:**
     - `VERDICTS` (cell 20, and the chapter) maps `429` to "rate-limited" beside "open" and "gated". In the exercises OpenAlex, an open nonprofit API, was a 429 because the review machine's shared budget was spent: C's table "would conclude something false about OpenAlex".
     - `400` isn't listed, so Meta's refusal and D's FRED probe (a missing key, in JSON) both read "other", while the chapter calls Meta "refusing outright". A `200` reads "open" even when the body is a cap or a page.
     - The eight targets were chosen "to span" institutions to platforms (cell 17), and each is asked once, from one place, at one moment. Step 10 asks "How many of the eight endpoints were open?", and Step 4's Discuss asks what the open services have in common, which D notes is the selection rule read back.
     - `rate_limit` reads `x-ratelimit-limit`, which is requests per window for Mastodon (`300`) and credits for OpenAlex (`1000`); the chapter says OpenAlex's headers "state the budget in U.S. dollars" (`X-RateLimit-Limit-USD`). A would have written "OpenAlex gives 1000 requests a day".
   - **Why it matters:** the verdict column is the one students quote. D and C would put the table in a deck or a project and couldn't say what it measured.
   - **Proposed fix:** lab key, Step 4's Discuss (cell 30), one bullet: "these eight were chosen, not sampled, and each was asked once: what claim can the table support?" Step 3's text (cell 16): "`verdict` is a first guess from the status code; `content_type` is the check on it." Chapter, exercise Step 3: "if a row is 429, record the budget headers and mark it unknown, not closed", and "`x-ratelimit-limit` has different units on different hosts". Whether `VERDICTS` itself changes (429 as "busy, retry") is the instructor's decision: it is code copied from the chapter into the lab and the deck.
   - **Status:** verified: cells 16, 17, 20, 30 and 74; the chapter's `VERDICTS`, "Five open, two gated, one refusing outright", and its anchor paragraph. The OpenAlex and FRED answers are reported.

4. **The lab sends students' requests to hosts whose `robots.txt` disallows them, and never says why.**
   - **Who:** A, B, C, D, E.
   - **What happened:** read on 2026-11-18, five of the eight `TARGETS` disallow the lab's path to every client: `www.reddit.com`, `api.twitter.com`, `export.arxiv.org` and `graph.facebook.com` (`User-agent: *`, `Disallow: /`), and `en.wikipedia.org` (`Disallow: /w/`, which covers `api.php?action=query`). Students send to them in Step 2 (Reddit), Step 3 (Wikipedia, X), the Step 4 loop (all five, including arXiv, Meta Graph and X, which no typed cell asks), Step 5 (Reddit; the microsprint asks Wikipedia with no User-Agent, against its User-Agent policy, on purpose; the given loop asks Wikipedia and Reddit twice each) and Step 7 (Twitter v1.1). The students' copy mentions `robots.txt` only in three Discuss boxes: Hacker News's `.json` rule (Step 1), Reddit's (Step 2) and the two Mastodon servers (Step 9: "Our loop asked their APIs anyway"). Step 3, Step 4 and the deck say nothing. The key's note does explain why its own run skipped these hosts; that note isn't in the students' copy.
   - **Why it matters:** week 2 taught students to read `robots.txt` first. D "did not want to start the course by ignoring it" and could run 2 of 8 targets "with a clear conscience"; E: a lab that "tells me nothing while I send it to a `Disallow: /` host teaches the opposite of week 2"; C wants to show a client that the site's terms were followed. A one-shot, named, measured request may well be defensible, but the lab doesn't say so, or who decided.
   - **Proposed fix:** the instructor's decision first (see "Suggested next step"). Then, lab key, Step 3's text (cell 16) or Step 4's (cell 23), two or three sentences: five of the eight disallow automated clients; we ask each once, named, to measure access, not to collect; collecting would be different; the instructor made that call for this measurement. One Discuss bullet at Step 4 (cell 30) naming arXiv, X and Meta. Optional, for C: a given cell before the loop that prints each target's `robots.txt` rule, which is a measurement in its own right. Deck, "Step 4: all eight, in one table": one line.
   - **Status:** verified by reading the eight hosts' `robots.txt` files (and nothing else) on 2026-11-18, and the students' copy at `e136c69` for every mention of `robots`.
   - **The open decision.** #212's description raises this and leaves it open: "that most of the eight targets disallow automated clients is worth a word in class, and Step 9's last Discuss question raises it". The key's own run read the files strictly (no request to a path disallowed to automated clients or to named AI crawlers), and #197 lists the nine cells waiting for a laptop. The same question is open for week 4 (NASA POWER, raised on #197). The instructor's call is which reading governs students' requests, and so whether the lab explains the exception, changes targets, or follows the strict reading.

5. **The exercise menu and Step 6 send students to hosts a careful student can't send to.**
   - **Who:** A, B, C, D, E.
   - **What happened:** reading `robots.txt` first, as week 2 taught:
     - **PubMed E-utilities** (`eutils.ncbi.nlm.nih.gov`): `User-agent: *`, `Disallow: /`.
     - **ProPublica Congress API** (`api.propublica.org`): `robots.txt` answers `403 {"message":"Forbidden"}`, so there is no rule to read.
     - **Sunlight Congress API**: the TLS certificate has expired, so `robots.txt` can't be fetched without turning verification off.
     - **OpenSecrets** (`www.opensecrets.org`): `User-agent: *` is `Allow: /`, with `Content-Signal: ai-train=no`; named AI crawlers are disallowed `/`. A student's named client may send; a strict reader stops (see Method notes).
     - So a strict reader can send to none of Step 6's three, and a reader of OpenSecrets's `*` group to one: A, C, D and E sent nothing that reached a server, and B sent to OpenSecrets. The exercise text never says to read `robots.txt` before Step 4's endpoints "of your own" either; A, C, D and E did, and spent 40 minutes to an hour of their exercise time on it.
   - **Why it matters:** "a student like me who checks robots.txt gets stuck on the Step 6 menu, and one who doesn't gets a mislabelled row" (E; item 2).
   - **Proposed fix:** chapter, exercise menu and Step 6: one sentence telling students to read each host's `robots.txt` first, and say which menu hosts disallow automated clients (PubMed) or can't be read (ProPublica, Sunlight); or give the menu a `robots.txt` column (D). Consider replacing PubMed. For Step 6, say that an unreadable `robots.txt` (ProPublica) or an expired certificate (Sunlight) is itself a finding a student may report without sending. These are textbook changes; the lab's Step 10 (cell 74) could add one line under "Recommended Exercises ahead".
   - **Status:** verified by reading those four `robots.txt` files on 2026-11-18. Census's "Request Rejected" page (C, D, E) is reported, not verified.

6. **Every checkpoint 404s until #212 merges.**
   - **Who:** A, C, D, E.
   - **What happened:** `DATA` (cells 3 and 41) is `https://raw.githubusercontent.com/cuinfoscience/INFO4617-Fall2026/main/labs/week-03/data/`. `main` has `labs/week-03/` but no `data/` folder, so Step 6's unguarded `pd.read_csv(DATA + "access.csv")` (cell 42) and the fallback cells of Steps 4 and 9 (26, 71) raise `HTTPError: HTTP Error 404: Not Found`.
   - **Why it matters:** the checkpoints are the lab's safety net, and the student who needs one most, starting Friday cold, meets the 404 first.
   - **Proposed fix:** a merge-order item, nothing to edit: #212 adds the data folder with the notebook, so merge it before the class that uses it, then load `DATA + "access.csv"` once in a browser. E's suggestion, a CI check that fetches each lab's `DATA` files, is for later.
   - **Status:** verified: `git ls-tree origin/main labs/week-03` lists no `data/`; #212's tree has it.

7. **Neither part fits its day by the lab's own minutes.**
   - **Who:** A, B, C; D and E found the pace right for themselves.
   - **What happened:** Part 1's headings add to 48 minutes, plus 13 in microsprints, against Wednesday's about 50; Part 2's to 35, plus 8, against Friday's about 35 before the 15-minute block, before any Discuss box. Step 1 alone is four typed cells, a Discuss box and a 4-minute microsprint in 9 minutes. A and B estimate Part 1 at 75–85 minutes; C at 60–75. The deck's Friday section also holds the instructor's "slower on-ramp" to issues and pull requests.
   - **Why it matters:** "when I fall behind I will 'copy the cell from the key', as the slide says, and then I learn nothing from the step" (B).
   - **Proposed fix:** the minutes are the instructor's decision. The personas' candidates: mark one microsprint a part "if time" (C); make Step 1's `ids` cell or Step 8's `no_params` cell given (B); say in the lab which steps the exercises need, Steps 1–5 for exercise Steps 1–5 (C); a "go further" line for students who finish early, such as running the Step 4 loop twice ten minutes apart (D).
   - **Status:** verified: the headings at `e136c69` sum to 48 + 13 and 35 + 8; `docs/course-facts.md` gives Wednesday about 50 and Friday about 35. The persona estimates are their own.

8. **Step 4's save and fallback cells invite a mislabelled table, and its microsprint is empty on the fallback.**
   - **Who:** A, C for the order; A, B, C, E for the microsprint.
   - **What happened:** cell 25 says "Skip this cell if the loop above stopped" and stamps `AUDIT_DATE`; cell 26, after it, loads the checkpoint "only if the loop above stopped". A ran 25 first and got `NameError: name 'access' is not defined`; running 26 and then 25 stamps today's date on the 21 October table, the provenance error the chapter warns about (A, C). The microsprint (cell 29) then compares the table with `CHAPTER`, and the checkpoint's statuses equal the chapter's, so it prints `0 of 8 rows` and an empty frame: the Share question has nothing to share, and B "could not tell whether it had worked or I had made an error".
   - **Why it matters:** the fallback path is the one a student on a refused request takes.
   - **Proposed fix:** lab key: put the fallback cell before the save cell, or merge them into one given cell (`if "audit_date" not in access: …`). Cell 27 or 29: "if you loaded the saved table, expect 0: it is the key's run, which matched the chapter. Change one status by hand, `access.loc[5, "status"] = 200`, and run it again to see a difference" (B, E). The same order in Step 9 (cells 70, 71).
   - **Status:** verified: cells 25, 26, 29, 70 and 71, and `access.csv`'s eight statuses against `CHAPTER` (cell 28).

9. **A refused single request leaves nothing for the cells after it.**
   - **Who:** C, D, E.
   - **What happened:** the checkpoints are tables, not responses. If Step 2's or Step 3's request raises instead of answering, `reddit`, `wiki` or `x_twitter` don't exist, and cells 21, 33 and 35 stop with `NameError`. Cell 25 says "skip this cell if the loop above stopped"; the single-request cells have no such line. The key's nine `not-run-live` cells also have no saved output, so the instructor projecting the key has nothing to show for them until the laptop run (#197), and the key's answer to Step 10's second question says Step 5's Reddit cell "wasn't run".
   - **Why it matters:** for D a few minutes; for a student with little Python "a `NameError` in Step 5 is a stop". On a campus laptop most of these requests will answer (a 403 is still a response), so this mostly bites when a host times out or resets.
   - **Proposed fix:** lab key: "if the cell above stopped, skip this one" in the comments of cells 21, 33 and 35. After the laptop run, keep its outputs in the key. D's alternative, a small `responses.json` checkpoint, is more than this needs.
   - **Status:** verified: the tags and empty outputs of cells 14, 18, 19, 21, 33, 35, 66–68, and the names cells 21, 33 and 35 use.

10. **Wednesday's slides announce Friday's work, and the deck doesn't say what is due when.**
    - **Who:** A, B, D, E.
    - **What happened:** "Wednesday: measure it, then take it home" lists "Run dead-endpoint forensics: autopsies of Pushshift, CrowdTangle, and Twitter v1.1"; "Three ways web data dies" sits in the Wednesday section; the lab does both on Friday (Step 7). "This week at a glance" gives Friday as "Textbook revisions" only, and lists two things due Sunday (the exercises' HTML and an issue or comment URL) in separate blocks, while the lab says "Nothing here is turned in". E notes a student starting the exercises on Wednesday night reaches exercise Step 6, the autopsy, before Step 7 has been taught.
    - **Why it matters:** B and E plan their week from the slides; B "would not know whether two things are due, or whether Friday's lab is optional".
    - **Proposed fix:** deck: the at-a-glance and Wednesday frames, "Friday: Lab 03, Part 2 (retired endpoints, the Wayback Machine, Mastodon), then textbook revisions", and one line, "Due Sunday: the exercises notebook as HTML; your issue or comment URL"; move "Three ways web data dies" after "Step 7: one retired endpoint by hand". On "A guided audit in seven steps": "Steps 1–5 after Wednesday; 6–7 after Friday". These are the instructor's frames; #212 proposes the first and third edits already ("Your frames", items 2 and 5).
    - **Status:** verified in `week-03.tex` at `e136c69`.

11. **Step 5 teaches attribution on the one easy case, and the exercise's refusal is a harder one.**
    - **Who:** D, E; A met the same refusal.
    - **What happened:** the lab's case is Reddit: `snooserv`, its own software, and `1.1 varnish`, its cache. In exercise Step 5, A, D and E diagnosed OpenAlex's 429: `server: cloudflare`, `via: None`. The chapter's `diagnose()` prints 120 characters of the body; the sentence that attributes the refusal (the budget is shared by everyone on the IP address) begins after them (E). The exercise offers "the institution itself, a gateway in front of it, or something between you and it", and nothing in the lab says where a CDN fits.
    - **Why it matters:** D: "the validity question in miniature, and the course trains me on the wrong half of it."
    - **Proposed fix:** lab key, Step 5's Discuss (cell 37), one bullet: "if `server` says `cloudflare`, who refused? A `server` header names the last software that spoke, not who decided; the body does." Chapter, exercise Step 5: print `text[:400]`, or the `message` field when the body is JSON.
    - **Status:** verified: cells 31–37 and `diagnose()` at `3f9cf2c`. The OpenAlex body's wording is reported.

12. **Three versions of `probe()`: the slide's, the chapter's and the lab's.**
    - **Who:** A, C, D.
    - **What happened:** "Claims you can check --- the access matrix" computes `verdict` with an inline conditional (429 is "other"), keeps the `content_type`'s charset, and has no `rate_limit`; the chapter's uses `VERDICTS` (429 is "rate-limited"), `.split(";")[0]`, `rate_limit` and `Int64`; the lab's loop (cell 24) has no function and no `timeout=`. The exercises say "run the chapter's `probe()` (or your own version)"; a student who copies the slide gets different verdicts.
    - **Proposed fix:** deck: park the frame, as #212 proposes ("Your frames", item 1), or replace its listing with the chapter's function, labelled as the chapter's.
    - **Status:** verified: the frame, the chapter, cell 24.

13. **The exercises' anchor is the endpoint likeliest to fail for a whole class.**
    - **Who:** B, C; A, D and E hit the same 429.
    - **What happened:** on a shared address OpenAlex's keyless budget runs out (Environment blocks). The chapter says so, twice, and says a 429 is a measurement, not a failure. But Step 3 then has an anchor row that says nothing about OpenAlex, and a student "might not know whether to retry, and the exercise says 'do not retry in a loop'" (C). The 429 body is long and includes instructions for getting a key; B worried a student would follow them.
    - **Proposed fix:** chapter, exercise Step 2, one sentence at its top: "If the answer is 429, that is your result: record the `X-RateLimit` headers, write what they say, and go on to Step 3." The lab never asks OpenAlex, so the deck's "A guided audit in seven steps" could add "the anchor often answers 429 on campus" (B).
    - **Status:** the chapter's anchor paragraph and Common Issues verified; the class-wide failure is reported, from the review machine.

14. **The likeliest first slips aren't named.**
    - **Who:** A, B, C.
    - **What happened:**

      | Slip | What comes back | Who |
      |---|---|---|
      | `requests.get(HN + "item/1.json", HEADERS)`, headers as the second argument | `200`, and the User-Agent goes into the address as `?User-Agent=…`: no error, an unnamed client | A |
      | `hn_item.json["title"]`, no `()` | `TypeError: 'method' object is not subscriptable` | A, B, C |
      | Only the second comment line of cell 6 typed, not `HN = …` | `NameError: name 'HN' is not defined`; the same with `WAYBACK` in Step 8 | B |
      | No `f` before `"item/{ids[0]}.json"` | a 400 JSON error, not an exception | A |
      | `item/1` without `.json` (E's slip) | `200` with an HTML sign-in page, then `JSONDecodeError` | E |

      The prompt's first line, `# HN: "https://hacker-news.firebaseio.com/v0/"`, read to B as a note rather than a line to type.
    - **Why it matters:** A and B can't read a traceback beyond its last line. Each was fixed in about two minutes, from the traceback's last line and the prompt or the step text (B's weight: see Method notes).
    - **Proposed fix:** lab key, opening cell (0): "a comment of the form `# NAME: "text"` means: write `NAME = "text"` first". Step 1's text (cell 5): "`headers=` has to be spelled out" and "a 'method' object error means `()` is missing after `.json`". Optional, A: a given `print(hn_item.request.headers["User-Agent"])` in cell 6.
    - **Status:** the first slip verified with `requests.Request(..., params=...)` and `requests.get`'s signature (the second argument is `params`); the `TypeError` text is Python's. B's `NameError`s are reported.

15. **The exercises' Steps 4 and 7 ask for things nothing shows how to find.**
    - **Who:** A, C, D.
    - **What happened:** Step 4 asks for "two endpoints of your own" and says nothing about finding an API address; A spent most of an hour there and picked two it already knew. Step 7 asks "which of your rows was a refusal wearing a success code". C's six rows had none, and C found only a 403 behind a shared gateway; D found no way to look for one among the 200s; and the menu says "at least one answers `200` with something other than data" without saying how to look for it among the 200s.
    - **Proposed fix:** chapter, exercise Step 4: a recipe ("search for `<city> open data API`, look for an address that ends in `.json`") and one worked example, plus the `robots.txt` line from item 5. Step 7: "if none of your rows is one, say so, and say what you'd have to check".
    - **Status:** the steps' text verified at `3f9cf2c`; the personas' rows are their own.

16. **Several typed cells are copying, not writing.**
    - **Who:** A; E from the other side.
    - **What happened:** cell 29's prompt is its code; cells 7, 9, 20, 47, 57 and 58 are close to it, and the deck's step frames then show the finished cells. A "never got stuck in the lab itself" but came out able to type what is on the screen, and first wrote a request unprompted in the exercises. E, who knows Python, would have liked to write `probe()` and `autopsy()`.
    - **Why it matters:** the jump to the exercises is where A, C and E say the difficulty appears.
    - **Proposed fix:** a judgment for the instructor, against `labs/AUTHORING.md`'s "By hand, then given": A's suggestion is one or two cells a part whose prompt gives only the goal ("request the Mastodon instance and print the status"), with the frame after the cell.
    - **Status:** cell 29's prompt verified; the rest is a judgment.

17. **Step 9's plot labels a 422 "needs a login".**
    - **Who:** A, B, D.
    - **What happened:** `servers.csv` has `422` for three servers. Cell 72's legend says "public timeline needs a login" for everything that isn't 200; 422 is "Unprocessable Entity", and no cell prints a 422's body. The Step 9 Discuss raises the 422 itself.
    - **Proposed fix:** lab key, cell 69: print one closed server's `public.text[:80]` in the given loop; or label the legend "answered something other than 200". The deck's Step 9 frames don't show the legend.
    - **Status:** the legend and the file verified; what the servers' 422 bodies say is not verified (nothing was sent to them).

### Corrections

Claims in the reviews that turned out wrong, out of date, or inexact, and what this document does with them:
- **C: "the chapter's menu lists Congress.gov, while `docs/course-facts.md` says `DATAGOV_KEY` was dropped with Congress.gov".** The course-facts row is about week 11's lab and chapter 11. Chapter 3's menu keeps Congress.gov and NASA, behind the `api.data.gov` gateway, as rows that answer with "a request for a key", on purpose ("Some answer with data, some with a request for a key"). Not a mismatch; dropped.
- **OpenSecrets "disallows AI clients" (A, C, D, E) and "allows `*`" (B).** Both are true of the file (item 5); neither is the whole of it.
- **E: "four of the eight hosts disallow every path".** Four disallow `/`, and Wikipedia disallows `/w/`, which covers the lab's path: five of eight, as E's own count says.
- **C's strongest case: the four-date microsprint is "the chapter's 14 August 2024 claim, confirmed by me".** It confirms only that no capture after that date answered 200 (item 1). The rest of C's praise of Step 8 stands.
- **B: the Step 7 text doesn't explain what `except requests.ConnectionError` catches.** Step 7's text says what it catches and links its documentation; the Discuss (cell 53) and the Friday block raise the missing `timeout=`. Dropped. E's point that a `ReadTimeout` isn't a `ConnectionError` is right, and is the Discuss box's own question.
- **E: the title slide still says "August 31, September 2 & 4, 2026".** True, and #212 lists it under "Dates to change for the next offering". Not repeated below.

## Disagreements

- **Too slow, or about right.** A and B rate pace 2–3 and put Part 1 at 75–85 minutes; C at 60–75. D finished Steps 1–3 in about 10 of their 24 minutes and rates pace 4; E calls Part 1 "tight but fine". All five agree the microsprints and Discuss boxes aren't in the minutes. That suggests "if time" markers, not cuts: the by-hand cells that D could skip are the ones A and B need (item 7).
- **What the robots.txt gap means.** E wants a sentence saying who made the call and that measurement isn't collection; D wants a stated course policy, or a `robots.txt` column as data; C wants a given cell that reads the files first; A and B ask only that the exercise text say to read them. All five read the files themselves. B read OpenSecrets's `*` group and sent; the others read the named list and didn't. The reviewers agree the lab should say something; what it says is the instructor's decision (items 4, 5).
- **How to fix the verdicts.** C wants repetition (ask twice, a minute apart) and a "busy" label for 429; D wants a Discuss question about what a chosen set of eight can support, and a body check on every 200; A wants the units of `rate_limit` stated. They are compatible; D's costs the least (item 3).
- **How to fix Step 8.** A and B: print the `"error"` the loop hides. D and E: say the API can't show a redirect, and point elsewhere for the test. Both are needed: one is a given line, the other a sentence (item 1).
- **Difficulty.** A, B and C rate it 3: the lab gentle, the exercises steep (finding endpoints, reading an unlisted `robots.txt`). D and E rate it 2: "too easy in code, appropriately hard in judgment" (D); E wanted to write the functions. Both groups locate the real difficulty in the exercises (items 15, 16).
- **What the week is for.** For D, measurement validity; for C, a data-quality checklist; for E, tools and their silent failure modes; for A and B, the people on both sides of a refusal. D and E rate their confidence 4, A, B and C 3; what holds A and B down is finding and vetting an endpoint on their own (item 15), and for B, that `autopsy()` "can call a web page 'still open'" (item 2).

## Ratings

Each on a scale of 1 to 5. For difficulty, 5 is hardest for that persona's background.

| | A | B | C | D | E | Mean |
|---|---|---|---|---|---|---|
| Clarity of motivation | 5 | 4 | 5 | 4 | 4 | 4.4 |
| Pace | 3 | 2 | 3 | 4 | 4 | 3.2 |
| Difficulty for my background | 3 | 3 | 3 | 2 | 2 | 2.6 |
| How much I learned | 4 | 4 | 4 | 3 | 3 | 3.6 |
| Confidence I could do this on my project | 3 | 3 | 3 | 4 | 4 | 3.4 |

What costs motivation a point: the Wednesday and Friday slides disagreeing (B), the lab never saying what a table of eight chosen services can support (D), and the `robots.txt` gap (E). D and E rate "how much I learned" 3 because the code was easy and the measurement's limits weren't taught; E "learned more from the exercise than the lab".

## Small things

Deck (`slides/week-03/week-03.tex`):
- "The golden age of web data access": "the web was a mostly open that was easy(ish) to retrieve" is missing a noun (E).
- "Myths": "If data is publicly, collecting it is permitted" is missing "visible" (E).
- "Popular web data sources": "content-type `text/html` a block page" is missing a dash or a verb (E).
- "A revision menu for Chapter 3": "Add a figure. The chapter still has none"; the chapter at `3f9cf2c` has four (D).
- "Step 8: read into it, one level at a time": the `status` sentence (item 1).

Lab (`labs/week-03/lab-03-key.ipynb`):
- Step 0 calls `HEADERS` "chapter 2's form"; the lab adds ` python-requests/<version>` and the chapter's and exercise Step 1's `HEADERS` don't, so two User-Agents are in play without a sentence saying so (B, E).
- Step 3's Discuss: "`TARGETS["Twitter"]` stops with a `KeyError`", but the mistype a student would make is in `TARGETS["X (Twitter)"]` itself (E). `application/problem+json` is used before it's explained (D).
- Step 4: "Find your two requests in the loop" while the loop's variable is `response`, not `wiki` or `x_twitter` (B). The checkpoint's `rate_limit` prints `300.0` or `NaN` where the loop prints `"300"` or `None`; `data/README.md` says so, the step doesn't (A, C, D).
- Step 3's text: "expect 200" from Wikipedia, while the key's Step 5 loop shows Wikipedia's named request answered 429 (the cloud machine's address, as the key note says); a reader of the key can't tell which to believe (C).
- Step 5: nothing says what to conclude from Hacker News's `nginx` with no `via` (D), or that `None` there is the answer, not an error (B).
- Step 5's microsprint sends Wikipedia a request without a User-Agent, which its policy asks clients not to do; one line saying why one request is fine (A; see item 4).
- Step 6 loads the key's `access.csv`, never the student's own from Wednesday, so the save-with-a-date habit isn't used again (E).
- Step 7's timeline: a duplicate `MY_EVENT` is drawn twice without complaint (A); the chapter gives dates for few events, so "another event from the chapter" sends students elsewhere for a date (C); the 2021 Academic Research track fits no pressure label (E).
- Step 9: `/api/v1/instance` is deprecated and the given loop reads `["stats"]["user_count"]` with no `.get` (E). `AUDIT_DATE` is set when the setup cell runs, not when each request goes (D).
- The last cell, "Your answers here, as comments", and "Nothing here is turned in" leave some students unsure which notebook to submit; the deck's "Submitting" means the exercises' (B, C, D).

Chapter and companion notebook (`ch-03-post-api.qmd` at `3f9cf2c`):
- "Five open, two gated, one refusing outright", while its own `VERDICTS` calls Meta's 400 "other" (D).
- The anchor paragraph: the headers "state the budget in U.S. dollars"; `X-RateLimit-Limit` is in credits, and the dollar figures are in `X-RateLimit-*-USD` (A, E; item 3).
- Exercise Step 3, "Remember the `Int64` dtype": the lab never produces a `None` status in its table, so nothing there needs it (D).
- Exercise menu note: "a 200 whose `content-type` is `text/html`" is offered for Step 5, but the lab's Step 5 shows only a 403 (B).

## Suggested next step

**Fix first, on #212's branch before it merges.** Each is small and changes none of what the week teaches:
1. **Item 1:** one given `"error"` line in cell 63, one sentence in Step 8 or its microsprint that the availability API can't show a redirect, and the same correction on the deck's Step 8 frame.
2. **Item 8 (and 9):** reorder or merge Step 4's and Step 9's save and fallback cells; one line in Step 4's microsprint for the all-matching case; "if the cell above stopped, skip this one" in cells 21, 33 and 35.
3. **Item 10 and 12:** the deck edits #212 already proposes for the instructor's frames: Friday's lab on the at-a-glance and Wednesday frames, "Three ways web data dies" after Step 7's frame, the slide's `probe()` parked, plus one "Due Sunday" line and the three typos.
4. **Items 3, 11, 14 and 17, as one pass of sentences:** what `verdict` can't say (Step 3, Step 4's Discuss), the CDN bullet in Step 5's Discuss, the `# NAME:` sentence and the two slips in Step 1, and one printed 422 body.
5. **Item 6:** merge #212 before the class that uses it, and load the `DATA` URL once afterwards.

**For the textbook** (chapter 3's exercises, one pass): the `SSLError` and content-type hint in Step 6 (item 2), the `robots.txt` line and PubMed in the menu (item 5), the 429 sentence at the top of Step 2 (item 13), the units of `x-ratelimit-limit` (item 3), and a recipe for Step 4 (item 15).

**Needs the instructor's decision:**
- **Which `robots.txt` reading governs students' requests** (items 4 and 5): #212 raises it, the key's run read strictly, and week 4's NASA POWER question on #197 is the same one. The answer decides whether the lab explains a one-shot measurement, changes targets, or follows the strict reading, and whether the exercise menu keeps PubMed.
- **The minutes** (item 7): 61 against about 50 and 43 against about 35, and what becomes "if time".
- **Whether `VERDICTS` changes** (item 3): 429 as "busy", not a verdict. It is the chapter's code, copied into the lab and the deck, so every copy changes together.
- **Whether `autopsy()` gains a content-type column** (item 2), with the lab's Step 7 loop following it.
- **Whether any typed cell becomes goal-only** (item 16).
