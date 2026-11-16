# Proposal: bringing weeks 1–13 to the incremental style

**Status:** a proposal, nothing applied. Written on 2026-11-16 at the instructor's request: "use the revised AUTHORING.md with more incremental coding style to propose revisions to previous slides and labs, working backwards from week 13". Every week's lab key and deck was read against:
- `labs/AUTHORING.md`, including the new rule 0 of "By hand, then given", **one minimal call first**;
- `slides/common/AUTHORING.md`, "Layout and density" and "Code shaped for reading".

The model is week 13's Part 3, as rebuilt on 2026-11-16 (#195):
- one notebook cell per slide frame;
- a small call students can predict (three sentences) before the pipeline (116 leads);
- typed cells of one to four plain lines, with loops and comprehensions in given cells.

These are revisions for the course's **next offering**. Weeks 1–9 were written to the earlier rules, and `labs/AUTHORING.md` says so.

## The weeks at a glance

| Week | Topic | Lab | Deck | Effort (lab / deck) | The main problem |
|---|---|---|---|---|---|
| 13, Parts 1–2 | Datalab, structured output | P1 | P2 | M / S | Students type a function and a seven-request loop; no small first call to Datalab or OpenRouter |
| 12 | Bluesky, YouTube | P2 | **P1** | S / L | All 9 code frames put code on the left; the deck teaches different code from the rebuilt lab; Part 3 never run live |
| 11 | Census, FRED | P2 | **P1** | S / L | Lab rebuilt 2026-11-10 and close to the rules; deck taught in the old style, code on the left in 11 of 12 code frames |
| 10 | Wikipedia APIs | P2 | **P1** | S–M / L | Deck is still lecture-plus-lab; four lab steps have no frame; listings of 13–19 lines |
| 9 | PDFs | **P1** | **P1** | L / M | 40 typed cells against 2 given, typed regex; 8 of 11 code frames put code on the left |
| 8 | Selenium, Playwright | P2 | P2 | M / M | Closest of weeks 1–9; typed cells of 7–11 lines to split |
| 7 | Wayback, CDX, gensim | **P1** | P2 | L / S–M | 21 cells `not-run-live`, no checkpoints, three typed functions |
| 6 | Static pages | **P1** | **P1** | L / L | Two typed functions; the deck fetches sites the lab's own `robots.txt` step disallows, and one frame doesn't run |
| 5 | Protocols | P2 | P2 | M / M | Typed request loops; the deck teaches the error handling the lab leaves out |
| 4 | XML, JSON | P2 | **P1** | M / S | Three code-left frames; the deck's JSON example (Open-Meteo) isn't the lab's (NASA POWER) |
| 3 | The post-API age | **P1** | P2 | L / M | Furthest from the rules: 7 typed request loops; the Wayback availability API now answers some sites with an empty result and an error |
| 2 | Ethics, robots.txt | **P1** | **P1** | L / M | Deck: code-left frames, a 15-line listing, output comments |
| 1 | Setup, first request | P2 | P2 | M / S | First API call should be one day before a month; the calendar (Friday only) needs deciding first |

## What the audit recommends, in order

1. **Rebuild the decks that contradict their labs, weeks 12, 11 and 10.** These weeks' labs were rebuilt on 2026-11-10 and are close to the rules. Their decks were taught in the old style, put code on the left, and no longer match the cells students type.
   - The work is mechanical: one frame per lab cell, as in week 13's Part 3.
   - It is the largest gain for the effort, because the labs are already right.
2. **Fix the decks that teach the wrong thing, cheaply, weeks 6, 4 and 2.**
   - Week 6's deck fetches Box Office Mojo and IMDb, which its lab finds disallowed by `robots.txt`, and its "Make it reusable" frame has a `return` outside a function.
   - Week 4's JSON example isn't the lab's.
   - Week 2 has four code-left frames, one more with code in both columns, and output comments.
3. **Add the minimal first calls to the labs that are otherwise close: weeks 13 (Parts 1–2), 12, 11, 10 and 8.** Each is one to three small typed cells. Every week's section below names the exact input and what students should see.
4. **Rebuild the labs furthest from the rules: weeks 9, 7, 6, 3 and 2.** That means three parts, checkpoints, typed loops and functions moved to given cells, and a fresh live run. It is the largest job, and it is best done a week at a time, ahead of each week next term.

## Patterns across the weeks

- **No week before 13's Part 3 makes a small first call** to a new service. Every week's section proposes them, and most proposals give the expected output.
  - **Checked live on 2026-11-16:** Census for Colorado alone, FRED, the Wayback availability API for `thefacebook.com`, gensim on three sentences, robots.txt parsing, and Hacker News item 1.
  - **Not checkable from the cloud machine:** Wikipedia (429), the Internet Archive's CDX server (connection reset), browsers, and Datalab's `page_range` page marker. These say so in their sections. Check them from a laptop.
- **Code on the left** appears in every deck before week 13's rebuild. `slides/common/AUTHORING.md` says this "can never happen again", so it decides the deck priorities above.
- **Decks and labs drifted apart** wherever the lab was rebuilt after the deck was taught: weeks 10, 11 and 12. A rebuilt lab should bring its deck with it in the same pull request, as #195 did.
- **Typed functions and request loops** remain in weeks 3, 4, 5, 6, 7, 9 and 13 (Parts 1–2). Moving each into a given cell, after one case typed by hand, is the single most common fix.
- **Weeks 1–3 have never been taught as labs.** Their decks point at the companion notebooks, so their deck work is mostly new frames. The instructor last edited every code frame in decks 2 and 3, so changes there need sign-off.
- **For weeks 2–3, a Monday lecture and a two-part lab** (week 10's form) may suit better than three parts, since their Mondays are law and policy.

## Decisions for the instructor

- **Order:** start with item 1 (the three decks), or with whichever week comes first next term?
- **Week 1's calendar:** Friday only, or Wednesday and Friday? It decides whether its lab is one part or two.
- **Weeks 2–3:** three-part labs, or a Monday lecture plus a two-part lab?
- **Live runs:** several proposals need a laptop run (Wikipedia, the Internet Archive, browsers, YouTube with a key). Who runs them, and when?

---

The sections below are the audit, week by week, from 13 backwards. Each gives the week's distance from the rules, its priority, the minimal first calls to add (with exact inputs), the top lab and deck revisions, mechanical counts, and the effort.

## Week 13, Parts 1–2 — Datalab document conversion; OpenRouter structured output

**Distance from the rules:** The lab is still on the pre-2026-11-10 rules. Each step is one or two dense typed cells. Students type a function (`extract_totals`, cell 47) and a loop that sends seven model requests (cell 48), and a 17-line microsprint retypes all of Steps 1–4 and pays Datalab again (cell 23). Neither part makes a small call before the full 25-page conversion or the full schema-plus-three-models request. The deck is already close to the target. Its frames are one listing each, code on the right, no outputs, and lines of 58 characters or fewer. In effect it is the blueprint the lab cells should be split to match: cell 38 alone covers seven frames.

**Priority:** P1. The lab breaks the hard rules: students type a `def` and a request loop, a microsprint retypes earlier steps, one prompt runs to 5 lines, and one typed cell is 12 lines. Neither new service gets a minimal first call. The deck is P2.

**Minimal first calls to add:**
- **Datalab `/convert`, new Step 1a (before the full report).** Submit the 2024 report with `"page_range": "14"` added. Per Datalab's Convert API page, `page_range` is 0-indexed, so `"14"` is only page 15, Exhibit 3, the image-only table that week 9's pdfplumber read as nothing. Poll it by hand twice with the same `request_check_url` cell. Students have page 15 of the PDF open and can predict the result before running it. They should see `status` `complete`, `page_count` 1, a cost of a few cents at most, and Markdown with one page marker followed by a `|` table whose rows start with years and carry 12 month columns and a total. Then run the full report, cached or with `skip_cache`. Before shipping, check live that the marker reads `{14}` under `page_range`. (A one-page course PDF of a 3-row table, January 100 / February 250 / Total 350, would be even more predictable, but it adds a file to make and host.)
- **OpenRouter `/chat/completions`, plain call, new Step 8a.** One user message, no schema, `"models": MODELS`, `temperature` 0, with this content: `"The 2024 report's Total Sales and Use Tax was $173,908,431. What is that total? Answer with the number only, without $ or commas."` Students should see `response.get("error")` print `None`, a model from MODELS, a small `usage` (about 50 prompt tokens), and `choices[0]["message"]["content"]` equal to the **text** `"173908431"`. That last one is a string, which sets up `json.loads`.
- **OpenRouter structured output, Step 8b (before the summary page).** Use the same one-sentence input with a one-field schema, `{"type": "object", "properties": {"total_current": {"type": "integer"}}, "required": ["total_current"], "additionalProperties": False}`, plus `response_format` and `provider.require_parameters` as in Step 8. Students should see content `'{"total_current": 173908431}'`, and `json.loads` of it should give a dict whose value equals `TRUTH["revenue-report-2024-12"][1]`. Only then send the 6-KB summary page and the four-field `SCHEMA`.

**Lab — top revisions**

| Step / cell | Rule | Now | Proposed |
|---|---|---|---|
| 0 [3], 6 [30] | Setup is given; Little Python (conditional expression) | Typed setup of 8 and 10 lines, with `"set" if … else "MISSING"` | A given setup cell as in Part 3 [55]/[56], where students type only their email. Define `datalab_headers` / `openrouter_headers` there, so `**HEADERS` leaves every typed cell. |
| 1 [8] | 1–4 lines; prompt ≤2; ** merge; give long dicts | 5 lines, a 3-line prompt, `**HEADERS`, lines up to 127 characters | Give the 5-key `data` dict with only the `"file_url"` value typed. Make the request a 4-line typed cell using `headers=datalab_headers`, one argument per line, then `print(job)`. |
| 1a (new) | By hand rule 0 | None | The `page_range: "14"` call above: 2 typed cells, then the poll cell [11] reused |
| 3 [15] | No regex in typed cells | Students type `re.split(r"\n*\{\d+\}-{10,}\n*", …)` | Give the split cell (explain the regex in the step text). Typed: `print(len(pages))` and `print(pages[1][:1200])`. |
| 4 [21] | 1–4 lines; no comprehension or regex; by hand, then given | 9-line loop with a list comprehension, `re.fullmatch` and a generator `sum`, under a 3-line prompt | By hand on one row: `row = exhibit.splitlines()[2]`, `cells = row.split("\|")`, `print(cells[2], cells[15])`. Then a given cell cleans and checks every row (the deck's three Step 4 frames already show that loop). |
| 4 microsprint [23] | Never retype a step; names left as found; ≤2 typed lines | 17 lines: resubmits a paid conversion, polls, splits, re-checks, and overwrites `job`, `check` and `data` | Read the book's saved `revenue-report-2018.md` (data/ch-13), set `check_page` to its page 14, and rerun Step 4's given check. That is 2 typed lines with no Datalab charge. |
| 7 [34] | No comprehension; no regex | `[page for page in pages if …][0]` and a typed `re.split` | Give the split. Typed: `pages_s = pd.Series(pages)`, `has_total = pages_s.str.contains("Total Sales and Use Tax", regex=False)`, `summary = pages_s[has_total].iloc[0]`, as in Part 3's `is_obama`. |
| 8 [38] | 1–4 lines; prompt ≤2; one cell per frame | 12 typed lines under a 5-line prompt, with `**HEADERS` and lines up to 128 characters | Split along the deck's seven frames. Give MODELS and `response_format`. Typed: `messages` (2–4 lines), `body` (with `...` parts given), the request (4 lines, `headers=openrouter_headers`), the three prints, then `content` and `answer` (2 lines). |
| 9 microsprint [44] | No ** merge; one name for one thing | `{**body, "models": [MODELS[2]]}` replaces `response` | `dots_body = dict(body)` and `dots_body["models"] = [MODELS[2]]`, then send into `dots_response` |
| 10 [47], [48] | Students never type a def or a loop that sends requests; no tuple unpacking or ** | Typed `def extract_totals` (8 lines), plus a typed 11-line loop with `for report, (prior, current)` and `**answer` that overwrites `summary`, `answer` and `pages` | Make both given, with the loop writing to `report_pages` and `report_summary`. Typed: one call `extract_totals(summary)` on the 2024 page, then the typed one-change cell [49] and the given rerun [50]. |

**Deck — top revisions**

| Frame | Rule | Now | Proposed |
|---|---|---|---|
| Step 1 (new, before "what to send") | By hand rule 0 | No small call | "Step 1: one page first": `data` with `"page_range": "14"`. Narration: "Which page is 14? What should come back?" |
| Step 2: wait for the result | Same behavior as the key | Prints only `status`, though the narration says "prints the pages and the cost" | Print what the key prints (status, error, page_count, total_cost), or change the narration |
| Step 0 | Lab–deck alignment | No frame for cell [5] (`datalab_key`, `datalab_base`, `book`) | Add "Step 0: the key and the book's address", splitting the long URL with string concatenation as Step 6 does |
| Steps 1, 2, 8, microsprint | Reading for novices | `{"X-API-Key": datalab_key, **HEADERS}` and an Authorization dict with `**HEADERS` in 4 listings | `headers=datalab_headers` / `openrouter_headers` from the given setup, which also shortens the Step 8 "send it" frame to 6 lines |
| Step 4 (3 frames) | One cell per frame; readable fragments | One 9-line loop shown in three overlapping fragments, the third starting at 12 spaces of indent | One frame per new cell: one row by hand (3 lines), then one frame for the given loop described in words |
| Step 5; microsprints of Steps 3 and 4 | Every typed cell has a frame | No frames | Add "Step 5: save the text" and a microsprint frame for each |
| Step 7 | Little Python | List comprehension across 2 lines | The `pd.Series(...).str.contains` version (3 lines) |
| Step 8 (new 8a, 8b, before "the shape of the answer") | By hand rule 0 | The full schema arrives first | "Step 8: one sentence, one answer" (plain call); "Step 8: one field, as JSON" (one-field schema). Ask "What number should come back? Is it a number or text?" |
| Step 8: the shape of the answer (11 lines); Step 10 def frames (11 and 12 lines); seven reports (12 lines) | About 8 lines of code | 4 listings of 9–10 code lines | Once [47]/[48] are given, use one frame per given cell that names its parts in narration and shows ≤8 lines with `...`. Split SCHEMA across 2 frames. |
| Microsprint: a different model | Little Python | `json={**body, "models": [MODELS[2]]}` | `dots_body = dict(body)` and `dots_body["models"] = [MODELS[2]]` (2 lines) |

**Mechanical counts:**
- Typed cells over 4 lines: 8 (7 of them over the hard maximum of 6: [3] 8, [21] 9, [23] 17, [30] 10, [38] 12, [47] 8, [48] 11).
- Typed cells with banned constructs: 12 (conditional expression 2, `**` merge 7, regex 5, comprehension 4, tuple-for 1, a typed def 1, typed loops that send requests 2).
- Prompts over 2 lines: 3 ([8] 3, [21] 3, [38] 5).
- Typed lines over 90 characters: 47, in 17 cells.
- Typed lines per part: P1 54 (budget 55), P2 53 (budget 55).
- Deck frames with more than one listing: 0. Listings over 8 code lines: 5. Listings over 12 printed lines: 0. Lines over 58 characters: 0. Frames with code on the left: 0. Printed outputs: 0.
- Lab steps with no frame: 1 (Step 5). Typed cells with no frame: 4 ([5], [18], [23], [26]).

**Effort:** M. The deck already holds the target cell shapes. The work is re-cutting about 10 lab cells to match it, moving 4 cells to given, adding 4 minimal-call cells and their frames, and one live rerun of Parts 1–2 (Datalab costs cents).

## Week 12 — Bluesky and YouTube social platform APIs

**Distance from the rules:** The lab was rebuilt on 2026-11-10 and is close to the rules: typed cells of 1–4 lines, 1–2-line prompts, no banned constructs typed, and repetition in given cells. Two gaps remain. YouTube's `playlistItems` and `videos` endpoints are introduced only in given 50-item cells. And Part 3 has never run live (every YouTube cell is `not-run-live`). The deck predates both the lab rebuild and the 2026-11-12 layout rules. All 9 code frames put the code on the left, with 10–14-line listings, printed outputs and result tables, and figures quoted in the narration. It also teaches different code from the lab: a getProfile loop instead of getProfiles, `indexedAt` instead of `record.createdAt`, a different agency list that includes the failing `noaa.gov`, and "up to five pages" where the lab pages to a date.

**Priority:** P1 for the deck: code on the left "can never happen again", and the deck contradicts the rebuilt lab. P2 for the lab: it needs minimal calls for YouTube's two list endpoints and a live run of Part 3.

**Minimal first calls to add:**
- **Bluesky `getProfile`, Step 1:** already minimal and predictable (`nws.noaa.gov`, compared against the bsky.app page). Keep it.
- **Bluesky `getAuthorFeed`, Step 5, before `limit` 25 plus `filter`:** send `{"actor": "nws.noaa.gov", "limit": 3}` and print `len(feed)` and each item's `post["record"]["text"][:60]`. Students should see 3 items matching the three newest posts on bsky.app/profile/nws.noaa.gov. getAuthorFeed leaves the pinned post out unless `includePins` is true, so tell them to skip a pinned post on the page. A repost there shows up as an item with `"reason"`. Then add `filter` and `limit` 25.
- **YouTube `channels`, Step 8:** the key test (`part=id`, `@NOAA`) is minimal but given, and reads the error through `.get("error", {}).get(...)`. Make it typed: `{"part": "snippet", "forHandle": "@NOAA", "key": youtube_key}`, print `.get("error")`, then `items[0]["snippet"]["title"]`. Students should see `None`, then `NOAA`, which is the name on the channel page.
- **YouTube `playlistItems`, Step 10, before the given 50:** typed `{"part": "contentDetails", "playlistId": uploads, "maxResults": 3, "key": youtube_key}`, then print the 3 `videoId`s. Students should see 3 IDs that match the three newest uploads on youtube.com/@NOAA. The uploads playlist mixes Videos and Shorts, so look at both tabs. Each ID is the `v=` part of a video's URL.
- **YouTube `videos`, Step 10:** typed `{"part": "statistics", "id": first_ids[0], "key": youtube_key}`. Students should see one item whose `viewCount` is a **string** and close to the view count on that video's page (YouTube rounds it there). Then the given comma-joined 50.

**Lab — top revisions**

| Step / cell | Rule | Now | Proposed |
|---|---|---|---|
| 5 [39]–[40] | By hand rule 0 | The first feed call already has `limit` 25 and `filter` | Add the `limit: 3` call, compared with the profile page, then add `filter` (the typo microsprint [61] then has a baseline) |
| 8 [81] | By hand; look before you read | The key test is given and reads the error with `.get().get()` | Make it typed (3 lines, part `snippet`), printing `.get("error")` then the title |
| 10 [95] | By hand, then given; rule 0 | The new endpoint appears only in a given 50-item cell | Typed: `first_params` with `maxResults` 3, the request, and printing the 3 `videoId`s. Then the given 50. |
| 10 [96]–[97] | Same | `videos.list` appears only in a given cell | Typed: one ID's statistics (3 lines). Then the given batch. |
| 8–10, all YouTube cells | Know what `run_key.py` skipped; check against the provider | 14 cells are `not-run-live`; the key's answers say "Part 3 wasn't run" | Run Part 3 from a laptop with a key. Try the mistypes `forhandle`, `NOAA` without `@`, and `maxResults` 51. Fill in the outputs and the Discuss numbers. |
| 6 [56] | Given cell under about 15 lines | 20 lines, `while True` / `break`, a nested `.get().get()` | Split it: a given `post_row(item)` function (flat), then a given 10-line loop. Or keep it and move the embed lookup to a named line. |
| 3 microsprint [31] | 1–4 lines | 5 lines | Give `more_agencies`, so students type only `more_params` and the request (4 lines) |
| 3 [27] | Code style in given cells | Six-key `rows.append({...})` on 3 packed lines | One key per line, as the deck rules show (given, so readability only) |
| Part 3 typing | Budget | P3 has 22 typed lines out of 40 | There is room for the 3 YouTube minimal calls (about 9 lines) without going over |

**Deck — top revisions**

| Frame | Rule | Now | Proposed |
|---|---|---|---|
| All 9 code frames | Code on the right, in a 0.6 column; narration in 0.37 | Code on the left in every one (0.4–0.56 columns) | Rebuild as 0.37 narration on the left and 0.6 code on the right, one frame per lab cell, titled "Step N: …" as week 13 does |
| From the website to the API | No printed output; one step per line | `requests.get(...).json()` chained, plus 2 `# output` lines | 4 frames: Step 1's URL and params, the request, the status/message, and the counts. Ask "Do they match the page's 63K?" instead of printing them. |
| Five agencies in one table | Same behavior as the key | A getProfile loop over a list including `noaa.gov` (which the lab shows fails), plus a results table | Step 3 frames: `agencies`, the `getProfiles` params, the request, and `len` came back. Show the given table cell in words. No result table. |
| What an agency posted this week | ≤8 lines; ≤2 chained calls; same behavior | 14 lines, `.json()["feed"]`, `indexedAt`, a reposts table | New "Step 5: three posts first" (limit 3), then one frame per typed cell ([39]–[45]) and a frame for the given rows cell. Drop the table. |
| More than one page: the cursor | No outputs; matches the lab | 12 lines with 2 `# 100 items…` outputs; `limit` 100; "five pages", "495 posts" | Step 6 frames: `second_params` (2 lines), send and print `cursor`, `since`/`until`, the given loop described in words. No figures. |
| When an agency posts | OO matplotlib; ≤2 chained; code right | `by_day.plot.bar(rot=0)` with no `ax`, a 3-method chain, code on the left, and narration quoting results | Step 7 frames for `local`, `day_names`, `by_day`, and the given plot with `fig, ax = plt.subplots()`. Keep the image on the right with 0.37 narration. |
| What travels | No printed output; ≤2 chained | A `groupby().agg().sort_values()` chain plus a 6-row results table and "412 of 495" | Name the steps (`embeds = …`, then `embeds.sort_values(...)`) and drop the table. Keep the Discuss questions. |
| Before Friday: your YouTube key | Line length ≤58; code right | A 59-character conda line on the left | Narration on the left; on the right, the conda line split with `\` |
| A channel by its handle / newest videos | ≤8 lines; one step per line; rule 0 | 10-line listings with `.json()["items"][0]` and packed params | "Step 8: test the key" (typed minimal), Step 9 one frame per cell, and "Step 10: three IDs first" plus "one video's statistics" before the given 50 |
| Concept frames (at a glance, This week…, Platforms share…, Before Friday) | About 40 words a frame | 120–177 words | Split, or cut to 40 words. Move the quota and policy detail to the lab's step text. |

**Mechanical counts:**
- Lab: typed cells over 4 lines: 1 ([31], 5 lines). Banned constructs in typed cells: 0. Prompts over 2 lines: 0. Typed lines over 90 characters: 0. Given cells over 15 lines: 1 ([56], 20). Cells `not-run-live`: 14.
- Typed lines per part: P1 29, P2 39, P3 22.
- Deck: frames with more than one listing: 0. Listings over 8 code lines: 6 (8 to 14). Lines over 58 characters: 1. Code-left frames: 9 of 9. Listings with output comments: 2 (4 lines). Frames with result tables or quoted figures: 5. Concept frames over 60 words: 9.
- Lab steps with no frame: 4 (0, 2, 4, 8). No frame names a step number, and about 40 typed cells map to 9 code frames.

**Effort:** L for the deck: a near-complete rebuild of about 35–40 frames from the lab's cells. S for the lab: about 5 new typed cells and one laptop run of Part 3 with a YouTube key.

## Week 11 — Government Data APIs (Census, FRED)

**Distance from the rules:** The lab (rebuilt 2026-11-10) is close. Every typed cell has 1–4 lines, no typed cell uses a banned construct, prompts are 1–2 lines, and the typing budget holds (35/23/33 typed lines against 55/55/40). What it lacks is rule 0: FRED's three new requests (`series/observations`, `units`, `frequency`) and the Census wildcard each go straight to a 36-row, 132-row or 482-row answer, with no small call students can check first. The deck (taught Oct 26–30) is far from the rules and has **diverged from the rebuilt lab**:
- its step numbers are stale (it says Steps 0–6 / 4–7 / 8–13; the lab is 0–4 / 5–8 / 9–14);
- it uses different variables and methods: the city's B25034 and B19013 at \$87,493 where the lab uses the county's B19013 at \$103,994; a low/high band where Step 7 uses a margin of difference; median income "83 of 482" where Step 8 uses rent "170 of 482";
- it ends with the revision block, where the lab now ends with the portfolio checkpoint;
- code sits in the left column in 11 of its 12 code frames.

**Priority:** P1. The next offering teaches the rebuilt lab, and this deck neither matches it nor meets the 2026-11-12/13 layout rules. The lab changes alone would be P2.

**Minimal first calls to add:**
- **Census data endpoint**, at the start of Step 3, before `county_params`: `{"get": "NAME", "for": "state:08", "key": census_key}`. Students should see `200 [["NAME","state"], ["Colorado","08"]]`: a header row, then one place, with the code returned as a column. Checked live 2026-11-16.
- **Census codes in place of numbers**, in Step 8, before `"place:*"`: set `rent_params["for"] = "place:07850,08345"` (Boulder city and Branson town). Students should see Boulder at `"2018"` / `"65"` and Branson at `"-666666666"` / `"-222222222"`. That puts the code on a row they can read whole, before `describe()` hides it in a mean. Checked live.
- **FRED `series/observations`**, in Step 10, before the full history: `income_params` with `"observation_start": "2024-01-01"` and `"observation_end": "2024-12-31"`. Students should see one row, `2024-01-01`, `"103293"` (a string). Ask: why isn't it Step 3's \$103,994? Checked live.
- **FRED `units`**, in Step 11, before `change` over 36 years:
  - first, levels for 2022–2024: `96584`, `97170`, `103293`;
  - then the same window with `units="chg"`. Students predict 2023 = 586 and 2024 = 6,123 by subtraction, and see 2022 = 6,257. FRED looked back past the window: a Discuss question.
  - Checked live.
- **FRED `frequency`**, in Step 12, before 132 months: `CPIAUCNS` for 2024-01-01 to 2024-03-31 gives `308.417, 310.326, 312.332`. Then the same with `frequency="q"` and `aggregation_method="avg"` gives one row, `2024-01-01`, `310.358`, which is their mean (a calculator check). Checked live.
- **No change:**
  - Step 1's `groups.json` is the catalog, and its size is the point;
  - Step 2's `groups/B19013.json` is already small (6 names);
  - Step 10's `series` request is already one predictable record (the title);
  - Step 13 (Denver) is given and reuses a known pattern.

**Lab — top revisions**
| Step / cell | Rule | Now | Proposed |
|---|---|---|---|
| Step 3, before cell 27 | Rule 0 | First data request has 3 variables for a county | Typed `state_params` NAME/state:08 + send/print (2–3 lines), as above |
| Step 8, before cell 64 | Rule 0 | One place → `place:*` (482 rows); code found via `describe()` min | Typed `rent_params["for"] = "place:07850,08345"` + `census_get` (2 lines) |
| Step 10, cells 85–87 | Rule 0 | First observations request returns 36 rows with `"."` gaps | Typed one-year window first; then widen `observation_start` (1 changed line) |
| Step 11, cells 91–93 | Rule 0 | `units="chg"` first seen on the 36-year series, mostly NaN | Typed 2022–24 levels, then `units="chg"` on the same window; Discuss the 2022 row |
| Step 12, cells 98–102 | Rule 0 | `frequency="a"` first seen on 132 months | Typed Jan–Mar 2024 monthly, then `frequency="q"` (one row = the mean) |
| Step 6, cell 53 (given, 17 lines) | Given ≤15 lines; one step a line | Comprehension, `{line:03d}`, catalog request, `.set_index()[...].rename().T`, plot in one cell | Split: (a) `housing_vars` + `labels` from the catalog, (b) request + table, (c) plot. One cell per deck frame |
| Step 4, cell 39 (given, 16 lines) | Given ≤15 lines | `requests.get(...).json()` chained inside the loop | Two lines (`geo_response`, `geo_rows`); move the explanatory comment into the step text |
| Step 1, cell 13 (typed) | Little Python (regex) | `str.contains()` is a regex by default; the given cell 14 adds `regex=False` | Add `regex=False` to the typed cell, or say in the step text that it doesn't matter for plain words |
| Step 7, cell 60 (typed) | One step at a line | `(margins[0] ** 2 + margins[1] ** 2) ** 0.5` on one line | Two lines: `squares = margins[0] ** 2 + margins[1] ** 2`, then `margin_of_difference = squares ** 0.5` |
| 18 typed prompts | Line ≈90 chars | Prompt lines of 91–111 chars (cells 8, 9, 11, 19, 28, 59, 60, 64, 67, 69, 83, 84, 88, 92, 99, 102, …) | Trim to ≤90, or split across the allowed 2 lines |

**Deck — top revisions**
| Frame | Rule | Now | Proposed |
|---|---|---|---|
| 2, 8, 15 (day openers) | Same as the lab | Steps 0–6 / 4–7 / 8–13; Friday revision block | Steps 0–4 / 5–8 / 9–14; portfolio checkpoint frame from `course-facts.md` |
| 5, 9–14, 16–19 | Narration 0.37 left, code 0.6 right | Code in the left or narration column at 0.36–0.56, in 11 frames | One cell per frame: narration 0.37, listing alone at 0.6 |
| 9, 10 (key setup) | One listing a frame | 2 and 3 listings (conda, `jupyter lab`, JSON, `getpass`) | Four frames (or one image of the terminal plus one `getpass` frame); lab Step 0 covers `getpass` |
| 7 "from the catalogs to a real place" | ≤8 lines; little Python; same as lab | 10 lines, a comprehension, `.apply`, 7 lines >58 chars, B25034 for the city | Replace with lab Step 3's cells: minimal NAME call → `county_params` (one entry a line) → send/print → `.json()` → DataFrame → `to_numeric` |
| (none) Steps 1, 2, 4 | Lab–deck alignment | No frames for `groups.json` search, the group's variables, or the city without `in` / mistype errors | Add about 9 frames, one per typed cell, plus a mistypes frame for Step 4 ("what status? what text?") |
| 12 "Two cities, ten decades" | ≤8 lines; ≤2 chains; comments | 11 lines: comprehension, `f"{line:03d}"`, `.json()["variables"]`, `.split("!!")[-1]` in a comprehension | Three frames: `pair_params["for"]` + `census_get`; housing request (cut with `...`); the figure on its own frame |
| 13 "Check a number against its margin" | Same as lab; no output | Low/high columns, plus a table of \$87,493 / \$90,671 | Lab Step 7's three cells (difference, margin of difference); ask "Is the difference larger than its margin?" |
| 14 `-666666666` | No printed output; same as lab | `describe()` output as comments, a place table with populations, median income | Frames: Boulder+Branson minimal → `place:*` → `describe()` → `== -666666666` → `mask`; no numbers |
| 16 FRED | ≤8 lines; ≤2 chains; no output | 9 lines (`.json()` chained, `[["date","value"]]`), 2 lines >58 chars, quotes \$103,293 | One frame per cell 81–88, with a minimal one-year frame; `Docs:` link to `series/observations` |
| 17, 18 `units` / `frequency` | No `**` merge; no output; one call a frame | `**years`, three calls in one listing, two output tables | Frames for the minimal `chg` and quarterly calls, then the lab's `start`/`end` calls; questions instead of tables |

**Mechanical counts:**
- Lab: 0 typed cells >4 lines (two at exactly 4); 0 banned constructs in typed cells (1 soft: default-regex `str.contains`); 0 prompts >2 lines; 18 typed cells with a prompt line >90 chars; 2 given cells >15 lines.
- Deck: 2 frames with >1 listing; 3 listings >8 lines (none >12); 13 listing lines >58 chars; 11 frames with code in the left column; 2 listings with output comments, and figures quoted in the narration of 9 frames; 21 of 22 frames over about 60 words.
- Alignment: 3 of 13 lab steps with no frame (1, 2, 4), and 3 more whose frame shows different code (3, 7, 8).

**Effort:** L. The lab is S: 5 small typed additions (about 10 lines; Part 3 goes from 33 to about 39 of its 40), 2 given-cell splits, and prompt trims. The deck is a rebuild to about 50 one-cell frames that follow the rebuilt lab.

## Week 10 — Introduction to APIs: Wikipedia (MediaWiki Action API, Pageviews REST API, mwclient)

**Distance from the rules:** The lab (rebuilt 2026-11-10 as three parts, Mon/Wed/Fri, 17 steps) is close. Typed cells have 1–4 lines, there are no banned constructs, prompts are ≤2 lines, and the budget holds (28/38/14). Rule 0 is met for the first Action API call (Step 1, `prop=info`). It is missing for:
- revisions (Step 4 goes straight to `rvlimit="max"`);
- pageviews (Step 9's first request is 2,099 days);
- agents (Step 13);
- `list=backlinks` (Step 15);
- mwclient (Step 16, all given).

Two typed dictionaries of 5–6 keys break "give the long dictionary". The deck is from a different format and has **diverged structurally from the lab**:
- it has a Monday lecture with a 9-frame interface tour, a Wednesday lab ("Eleven steps, about 75 minutes") and a Friday on the Final Project;
- its code is the chapter's, with `raise_for_status()` (3), `while True` and `**params`, in 13–19-line listings;
- the tour frames put the image on the left.

**Priority:** P1. Next offering's week 10 runs the lab over three days, and no frame matches Steps 3, 4, 11 or 14. The deck must be rebuilt around the lab before that week.

**Minimal first calls to add:**
- **`prop=revisions`**, in Step 4, before `rvlimit="max"`:
  - Typed `rev_params["rvlimit"] = 3`, using `rvprop` `"timestamp|size"` only (no usernames on screen), then print `first_page` whole.
  - Students should see 3 revisions (2026-09-09T12:55:42Z / 95255, 2026-09-04T21:30:31Z / 95179, 2026-09-04T04:47:10Z / 94887) and a `continue` with `rvcontinue: "20260814214343|…"`. That is the next, fourth edit, which they can check on the article's History tab.
  - Checked live 2026-11-16. Then set `"max"`.
- **Pageviews REST API**, in Step 9, before the 2021–2026 URL: `views_path + "/daily/20260901/20260903"`. Students should see 3 items with `"timestamp": "2026090100"` … and views 355, 357 and 429 (from the key's checkpoint). The 10-digit timestamp shows why `format="%Y%m%d%H"` is needed.
- **`agent` / monthly granularity**, in Step 13, before the given loop over three agents: `get_pageviews(ARTICLE, "20260901", "20260930", granularity="monthly")` returns one row, 14,000, which equals the sum of September's daily `user` views in Step 9's saved table. That is a check that monthly equals summed daily. Then `agent="spider"`.
- **`prop=categories`**, in Step 14, before the 6-key `categories|langlinks` request with `max`: `{"action": "query", "titles": ARTICLE, "prop": "categories", "cllimit": 3, "format": "json"}`. Students should see 3 category titles, which they can find at the foot of the article, and a `continue` token. That is the Step 4 idea on a new `prop`.
- **`list=backlinks`**, in Step 15, before the given `query_all` loop (3,314 links): `{"action": "query", "list": "backlinks", "bltitle": ARTICLE, "bllimit": 3, "format": "json"}`. Students should see 3 pages under `data["query"]["backlinks"]`, not under `pages`. That is the shape difference between `list=` and `prop=`.
- **mwclient**, in Step 16, before the given cell: typed `mw_page = site.pages[ARTICLE]`, then `print(mw_page.pageid)`. Students should see 289672, the same ID that Step 1's raw request printed.

**Lab — top revisions**
| Step / cell | Rule | Now | Proposed |
|---|---|---|---|
| Step 4, cells 27–29 | Rule 0 | Page one is 500 revisions, and only `continue` is printed | Typed `rvlimit = 3` with `rvprop "timestamp\|size"` first; print `first_page` whole; then `"max"` |
| Step 9, cells 64–65 | Rule 0 | First pageviews request: 2,099 days, `text[:200]` | Typed 3-day `views_url` first; print the whole text; then the full window (1 changed line) |
| Step 13, cells 91–93 | Rule 0 | New `agent`/`granularity` are first used inside a 3-year monthly call | One-month `user` call (=14,000) checked against Step 9's daily sum (load `daily-views.csv` in Step 12's setup) |
| Step 14, cell 101 (typed) | Give long dicts; Rule 0 | 6-key dict typed over 2 lines with two `max` limits | Minimal `cllimit: 3` call typed; then give the 6-key dict and have students type only `"prop": "categories\|langlinks"` |
| Step 14 microsprint, cell 105 (typed) | Give long dicts | 5-key `redirect_params` typed | Give the dict without the limit; students type `redirect_params["rdlimit"] = "max"` |
| Step 15, cells 109–112 | Rule 0; by hand, then given | `list=backlinks` appears only inside the given `query_all` loop | Typed `bllimit: 3` request + `data["query"]["backlinks"]` (3 lines) before the loop |
| Step 16, cell 116 (given, 10 lines) | By hand, then given; Rule 0 | New library entirely given | Typed `site`, `mw_page`, `print(mw_page.pageid)`; keep the 2023-edit comparison given |
| Step 5, cell 35 (given, 18 lines) | Given ≤15 lines | `get_revisions()` with a 5-key dict inline | Lift `params` out (it is Step 4's `rev_params`) so the function is ≤15 lines and matches what students typed |
| Step 15, cell 112 (given) | Plain given code | Generator `sum("redirect" in b for b in backlinks)` and a nested loop in one cell | Split the save-to-CSV lines off; say what the generator does in the step text (first use) |
| 13 typed prompts | Line ≈90 chars | Prompt lines of 91–95 chars (cells 17, 21, 24, 30, 36, 49, 57, 65, 67, 68, 97, 102, 111) | Trim to ≤90 |

**Deck — top revisions**
| Frame | Rule | Now | Proposed |
|---|---|---|---|
| 1, 20, 31 (glance / day openers) | Same as the lab | Monday lecture, Wednesday "Eleven steps, about 75 minutes", Friday Final Project | Three day sections, each opening with "Part N, start at Step 0/6/12", naming the lab; Friday ends with the 15-minute block |
| 3–18 (Monday concepts) | Lab Part 1 starts Monday; ≤40 words | 16 concept frames (19 of 36 frames >60 words) | Cut to 3–4 short openers before Step 0; keep the tour as reading |
| 10–18 (interface tour) | Never an image on the left | Image at 0.58 left, narration at 0.38 right, in 9 frames, each with a gray `block` | Swap to narration 0.37 / image 0.6; replace the gray blocks (17 in the deck) with a bold lead-in |
| 21 "four parts, then navigate the JSON" | One listing; ≤58 chars; comments | 2 listings (10+3), 8 lines >58, `.json()` chained, side comments | About 7 frames, one per Step 1–2 cell: dict one entry a line, send+print, `.url`, `.keys()` ×3, title/length |
| (none) Steps 3, 4 | Alignment; pagination by hand | No frame for no User-Agent/broken params, or for the two pages by hand | Frames: no-UA request; minimal `rvlimit 3`; page one `continue`; `.copy()` + `.update()`; page two |
| 22 `get_revisions` | ≤8 lines; code right; no error handling | 19-line listing on the left, `raise_for_status()`, `while True` | Two frames (cut with `...`), narration left: "find the two moves you typed"; drop `raise_for_status()` as the lab did |
| 24 "Pageviews: a second API" | One listing; same as lab | Function first (13 lines) + call; lab Step 9 builds the URL by hand | Frames per Step 9 cell: `replace(" ", "_")`, `views_path`, 3-day URL, send/print, `items` DataFrame, `to_datetime` |
| 27 `query_all` | ≤8 lines; no `**` on slides | 17 lines, `**params`, `while True`, `raise_for_status()`, 4 lines >58 | Step 14's minimal `cllimit 3` frame, then the given `query_all` on 2 frames, then the `page_list` call |
| 28 mwclient | One listing; no output comments; code right | 2 listings on the left, `# 0.10.1 from conda-forge`, `# 0.11: api_chunk_size` | One frame: `site`, `site.pages[ARTICLE]`, `.pageid` ("Same as Step 1?"); one frame for the 2023 edit count |
| 23, 25, 29 + Step 11 | No printed output; alignment | Narration quotes 2,988 / 15.9% / ~600 / 5,042 / 16,767; frame 29 is Boulder city; Step 11 (`tz_localize`, `corr`) has no frame | Questions in place of numbers; frames for Step 11's 4 cells; drop or move the city figure |

**Mechanical counts:**
- Lab: 0 typed cells >4 lines; 0 banned constructs in typed cells; 0 prompts >2 lines; 13 typed cells with a prompt line >90 chars; 2 typed dicts of 5–6 keys; 1 given cell >15 lines.
- Deck: 3 frames with >1 listing; 5 of 8 listings >8 lines (3 >12: 17, 19, 13); 13 listing lines >58 chars; 3 code frames with code on the left, plus 9 tour frames with the image on the left; 1 listing with output comments, and figures quoted in 4 frames; 17 gray blocks; 3 `raise_for_status()` not in the lab.
- Alignment: 4 of 14 lab content steps with no frame (3, 4, 11, 14), and 4 with only an image or number frame (7, 8, 10, 13).

**Effort:** L. The lab is S–M: 6 small typed additions (Part 1 goes from 28 to about 31 lines, Part 3 from 14 to about 24) and two dicts converted to given. The deck needs a full restructure from lecture-plus-lab to three lab parts, at about 60 one-cell frames.

## Week 09 — Extracting Data from PDFs (pypdf, pdfplumber, pytesseract)

**Distance from the rules:** This one is the furthest from the rules. It is one 85-minute notebook with no Parts, 40 typed cells against 2 given, a median of 6 typed lines a cell, and 235 typed lines, about 2.8 a minute against a target of about 1.1. Typed cells carry most of what "Little Python assumed" bans: four-pattern `re.sub` repairs, `re.findall`, a compiled `ROW` regex loop, `for number, page in enumerate(...)`, a typed `def get_saved_copy`, and f-string format specs everywhere. No library gets a small predictable call before its pipeline: Step 1's first pdfplumber cell already loops over `page.chars` with five format specs. The deck puts code on the left in 8 of its 11 code frames, prints outputs in comments, and shows functions the key doesn't have (`page_profile`, `clean_page_text`, `roll_call`, `row_words`).

**Priority:** P1. The deck breaks the 2026-11-12 rules worst of the three (code on the left, outputs in comments), and the lab's typed regex is the clearest "Little Python" breach. Fix the deck first, because that is cheaper.

**Minimal first calls to add** (checked locally on the book's `data/ch-09` copies, pypdf 7.0.1 and pdfplumber 0.11.10):
- **pypdf** (new Step 1, before `page.chars`):
  - Typed: `reader = PdfReader(report_2024)`, then `print(len(reader.pages))`, then `print(reader.pages[0].extract_text()[:80])`.
  - Students first open the PDF in a viewer, so they can predict **15** pages and a cover that reads `REVENUE REPORT / December 2024 / Contents`.
  - Point at the run of `\n` and spaces in front of it: the first sign that text comes back the way it was drawn, not the way it reads.
- **pdfplumber** (new step, before `find_tables()`):
  - Typed: `page = pdf.pages[1]`, then `print(page.width, page.height)`. Students predict **612.0 792.0**: US Letter, 8.5 × 11 inches × 72 points.
  - Then `print(page.extract_words()[0]["text"], page.extract_words()[0]["x0"])`. Students predict **`City 54.0`**: the header's first word, ¾ inch from the left edge.
  - Then `found = page.search("Total Sales and Use Tax")` and `print(len(found), found[0]["top"])`. Students predict **1** match, at **≈380** points.
  - This coordinate is the one Step 6's broken table turns on.
- **pytesseract** (new step, before Exhibit 3's whole-page OCR):
  - Given: `exhibit_3` as now, plus `row_2021 = exhibit_3.crop((0, 137, 1000, 165))`, displayed. The box is approximate, so check it in the key.
  - Typed: `print(pytesseract.image_to_string(row_2021))`.
  - Students read `2021 8,059,343 7,608,759 10,351,245` off the image, then see OCR write **`7,608.759`**. That is the deck's period-for-comma misread, on one row they can check by eye.
  - Don't use a scanned council-minutes page: the 2000-12-19 scans list members of the public with home addresses.
- **City records portal** (Step 3, instructor-only): leave it as is, but split the POST from `.json()["data"]`. Print `response.status_code, response.headers["Content-Type"]` first. The portal answers errors as HTML.

**Lab — top revisions**
| Part / cell | Rule | Now | Proposed |
|---|---|---|---|
| Whole lab | Three parts; checkpoints | One notebook, Steps 0–10, 85 min; checkpoints only through `get_saved_copy` | Part 1 (Mon) is Steps 0–2 plus the pypdf and pdfplumber minimal calls. Part 2 (Wed) is text two ways, repair, and tables. Part 3 (Fri, 35 min) is OCR and the seven reports. Each part gets a given setup cell. Add a checkpoint CSV of `summary_df` and `totals` in `labs/week-09/data/`. |
| Step 0, cells 2–3 | Setup is given; students type only their email | 9- and 4-line typed import/version cells, with lines over 90 characters | Make one given setup cell: imports, `HEADERS`, `PDF_DIR`, and `get_saved_copy` (moved here from the typed Step 2 def). |
| Step 1, cell 7 | One minimal call first; 1–4 lines | A 6-line loop over `page.chars[1:8]` with `!r` and `:.1f` | Start with the pypdf and pdfplumber calls above. Make the `chars` peek a given cell, after `page.chars[1]` is typed alone. |
| Step 2, cells 11–12, 15 | No typed `def`; no typed loop that sends requests; no tuple unpacking in a `for` | Typed `def get_saved_copy`; a typed three-file loop that downloads; the microsprint's `for number, page in enumerate(...)` with if/elif | Students type one page by hand: `len(page.extract_text())`, `len(page.images)`. Give the three-file loop. The microsprint changes only the file name in that given cell. |
| Step 5, cells 30–32 | No typed regex | Four typed `re.sub` repairs (with lookaheads) and five typed `re.findall`s | Students type one plain `str.replace` repair, for `"P age 1"`. Give the four-pattern repair. Students type one `re.findall` (dollar amounts) after the given `MONTH` example. Check that it doesn't just answer Recommended Exercise Step 4 ("extract a data element with `re.findall`"). |
| Step 6, cells 37–41 | 1–4 lines; one step per line | 6–7-line cells: bbox tuple unpacking, a set-of-edges loop, a 3-key settings dict, `crop` + `extract_table`, a chained `str.replace(...regex=True)` | Students type `tables = page.find_tables()`, `print(len(tables))` (predict 4), and `tables[0].extract()[-1]` (the missing totals row). Give the edges, settings and crop cells, with the settings dictionary whole. Students type one value: the crop's bottom, `395`. |
| Step 7, cells 46–50 | No typed regex; minimal call first | Typed whole-page OCR, then a typed 9-line `ROW.match` loop with `re.sub` | Start with the one-row OCR call above. Students type `image_to_string(exhibit_3, config="--psm 6")` and print its line count. Give the `ROW` parse and the `ocr_df` build. |
| Step 9, cells 61–65 | A loop is given; a checkpoint after it | A typed nested loop over 7 PDFs × 4 pages, and a typed 10-line crop loop | Students type one report by hand: `search()`, then `crop()`, then `split()`. Give the seven-report loop. Load the checkpoint `totals.csv` from `labs/week-09/data/`. The plot cell is given. |

**Deck — top revisions**
| Frame | Rule | Now | Proposed |
|---|---|---|---|
| 11, 14 (`pdftotext`, OCR at the command line) | Never code on the left | The listing sits in the 0.6/0.64 left column | Swap the columns: narration in 0.37 on the left, code in 0.6 on the right. |
| 17 "Install once" | One listing per frame; no outputs | Two listings, code on the left, `# 6.20.1 0.11.10`, `# 5.5.3` | Split into two frames, install and versions, each at 0.37/0.6, with the output comments cut. Ask: "Which version does yours print?" |
| 18 "Step 3 in code" | Same behavior as the key; no outputs | A `def page_profile()` on the left; output lists in comments | Two frames: one page by hand (`len(page.extract_text())`, `len(page.images)`), then the given loop. Cut `# [1332, …]`. |
| 19 "pypdf: order drawn" | No printed outputs | Six comment lines reprint the extracted text | Put the minimal pypdf frame (15 pages, the cover text) in front of it. Here, keep the code and ask "Where does 'Mayor' break?" Students see the answer when they run the cell. |
| 20 "The one line that flattens" | One listing; code right | Two listings (don't / do), both on the left | Split into two frames, or keep only the right way, and narrate the wrong one in words. Match the key's `[ \t]+` step. |
| 21, 24 (pdfplumber, OCR) | Code right at 0.6; ≤2 chained; no outputs | Code on the left at 0.46/0.5; `PdfReader(...).pages[14].images[0].image.convert("L")`; `# ['Use Tax Audit Revenue', None]` | Put the code on the right. Name the steps (`page = …`, `image = …`, `gray = image.convert("L")`). Add frames for the minimal calls: 612×792, then `City 54.0`, then `search()` at about 380; and the one-row OCR. Move the figures to their own frames. |
| 28, 29 (case-study functions) | ≤8 lines; ≤58 chars; same as the key | 12- and 11-line full-width `def roll_call` / `def row_words`, with 9 lines over 58 characters | These come from the chapter, not the key. Either replace them with the key's typed cells for Step 9 (one report by hand), or cut them to a concept frame with the figure and no code. |
| 13, 32 | No gray blocks | `block` environments | Use a bold lead-in instead, as the 2026-11-12 rules say. |

**Mechanical counts:**
- Lab: 70 cells; 40 typed against 2 given; 235 typed lines plus 13 answer lines (median 6); 30 typed cells over 4 lines and 16 over 6; 110 code lines over 90 characters (max 136); typed regex in 5 cells, typed `def` in 1, tuple unpacking in a `for` in 2 cells.
- Deck: 41 frames, 11 with code (8 with code on the left, 0 at 0.37/0.6, 2 with two listings); about 10 output-comment lines in 6 frames; 11 lines over 58 characters (max 87); 3 `def`s; 2 gray blocks.

**Effort:** L. Rebuilding the lab means moving roughly 60% of the typed code into given cells and writing about 3 new minimal-call steps, 3 parts and 2 checkpoints. The deck alone is M: about 25 frames, one per cell.

## Week 08 — Dynamic Web Pages (Selenium, Playwright, a hidden JSON API)

**Distance from the rules:** This one is the closest of the three. Its sandbox sites are stable and ran live, except Step 10's last cell, and the "requests first, then a browser" arc already resembles a minimal call. It still has 26 typed cells against 2 given, a median of 7 typed lines, a typed `def get_page`, typed comprehensions in 4 cells, a typed `lambda` inside an 11-line `%%writefile` Playwright script, and a typed regex with `re.DOTALL`. Selenium's first use crams the start, the load, the count and the screenshot into one 7-line cell. The deck's Wednesday frames are full-width listings of 8–13 lines, with `# 10` and `# -> …` outputs, and with `try/finally`, `continue` and a `def scrape_infinite_scroll` that the key doesn't use.

**Priority:** P2. Its structure and data are sound. The fixes are smaller cells, given loops, and splitting the deck's frames.

**Minimal first calls to add:**
- **Hidden JSON API** (Step 2): split the current 5-line cell into three.
  - First, `response = requests.get(api_url, params={"page": 1}, headers=HEADERS)` and `print(response.status_code, response.headers["Content-Type"])`. Students predict `200 application/json`.
  - Then `data = response.json()`.
  - Then `print(data.keys())`. Students predict `has_next, page, quotes, tag, top_ten_tags`, then `len(data["quotes"])` is **10**.
- **Selenium** (new step, before `/js/`):
  - Given: Step 0's options cell, with the `LAB_CHROME_FLAGS` key-only loop moved there from the typed cell.
  - Typed: `driver = webdriver.Chrome(options=options)`, then `driver.get("https://quotes.toscrape.com/")`, then `print(driver.title)`. Students predict **`Quotes to Scrape`**, the title `requests` saw in week 6.
  - Then `driver.find_element(By.TAG_NAME, "h1").text` gives the same words.
  - Only then load `/js/` and count `div.quote` (predict **10**, against the 0 `requests` found in Step 1).
- **Playwright** (Step 10):
  - Before the scroll + `expect_response` script, add a given 6-line `%%writefile hello_pw.py` that opens `https://quotes.toscrape.com/` and prints `page.title()`. Students predict `Quotes to Scrape`, the same as Selenium's.
  - Students type one change: the URL `/js/` and `page.locator("div.quote").count()`. Predict 10.
  - The `lambda` and `expect_response` script then becomes a given cell.
  - Run it from a laptop. Step 10's run cell is `not-run-live`.

**Lab — top revisions**
| Part / cell | Rule | Now | Proposed |
|---|---|---|---|
| Whole lab | Three parts; checkpoints | One notebook, 85 minutes, no checkpoints | Part 1 (Mon) is "do you need a browser?" (Steps 1–3). Part 2 (Wed) is Selenium's find, click, type and wait (Steps 4–7). Part 3 (Fri) is scroll + BeautifulSoup, the login, and Playwright (Steps 8–10). Checkpoints: `api_quotes.csv`, plus a saved `scroll-page.html` of `page_source` for a student whose Chrome won't start. |
| Step 1, cell 6 | No typed regex; one step per line | `re.search(r"var data = (\[.*?\]);", …, re.DOTALL)` then `json.loads`, typed | Students type the `requests.get` and `div.quote` count (predict 0). Give the cut of the script's array with the regex. Students type `len(quotes)`. |
| Step 3, cells 13–15 | No typed `def`; by hand, then given; no typed comprehension | A typed `def get_page`, a given `while True` loop, a typed comprehension building `api_quotes` | Drop `get_page`, since Step 2's two pages by hand already teach the move. Keep `get_all_quotes` given. Give the `api_quotes` DataFrame build. Students type `api_quotes.shape`. |
| Step 4, cells 20–21 | 1–4 lines; minimal call first | 10 and 7 typed lines: imports, options, a key-only loop, then start + load + count + screenshot | Give the imports and options. Students type the start, `get`, `title` minimal call (above). The screenshot is its own 2-line cell. |
| Step 5, cell 24 | 1–4 lines; no typed comprehension; ≤90 characters | 6 lines, one 120+ characters, with `[a.text for a in links[:5]]` | One locator a cell: `By.CSS_SELECTOR`, `By.LINK_TEXT`, `By.XPATH`, each printing one thing. Students type the first; the other two are a given comparison. |
| Step 8, cells 41–42 | A loop is given; no typed comprehension | A typed `for … break` scroll loop, 10 lines; a typed comprehension DataFrame | Students type one scroll by hand: `execute_script(scrollTo)`, `sleep(2)`, read the height again. Give the loop to the end. Give the DataFrame build. |
| Step 9, cells 47–48 | 1–4 lines; prompts spell exact names | 5- and 7-line typed cells, including a cookie-name comprehension | Split into: start the browser and count the links logged out (predict 0); log in (3 lines); count again (predict 10). Make the cookie names a given line. |
| Step 10, cell 53 | Typed ≤4–6 lines; no `lambda` | An 11-line typed `%%writefile` with `lambda r: …` | Students type the minimal `hello_pw.py` change. Make the scroll and `expect_response` script given. |

**Deck — top revisions**
| Frame | Rule | Now | Proposed |
|---|---|---|---|
| 10 "Headless mode" | ≤8 lines; code at 0.6; no outputs | 12 lines at 0.46, `# 10`, `# look` | Three frames: the options; start, `get` and `title` (the minimal call); then `/js/` and the count. Each at 0.37/0.6. |
| 13–14 (Playwright) | ≤58 characters; no outputs | Full-width; `# 0 -- does not wait`, `# 10`; 4 lines over 58 characters | Put the `title()` minimal script first, then the locator frame on the right column, with the outputs cut. Ask: "Which line waits?" |
| 15, 16 (codegen, MCP config) | Never code on the left | The listing sits in the left column, with the image on the right | Use no columns: the code or image alone, with narration above it. Or move the code right and put the image on its own frame. |
| 8, 9, 17 (Selenium Manager log, `SessionNotCreated`, aria snapshot) | No printed outputs as listings | Terminal output and a 13-line snapshot set as `lstlisting` | Make each a real screenshot (as an image), or cut it to one quoted line in the narration. |
| 27–29 (locate, read, type) | One cell a frame; same as the key | 8–10 lines full-width, 5 lines over 58 characters each; frame 29 waits on `firstHeading` while the key sleeps 2 s | One frame per key cell, at 0.37/0.6. Match the key, or change the key to `WebDriverWait` on Wikipedia, and say which. |
| 31 "Infinite scroll" | Same as the key; ≤8 lines | A 10-line `def scrape_infinite_scroll`; the key's loop is flat | Two frames: one scroll by hand (typed), then the given loop. |
| 32 "Selenium renders; BeautifulSoup reads" | No error handling the key lacks; ≤12 lines | 13 lines with `try/finally`, `continue`, `if text is None` | Replace it with the key's two cells (`page_source` to `soup`, then `div.quote` count and `quit()`). Move `try/finally` into a Discuss question about what's left running. |
| 1, 11, 20, 23, 34, 40, 42 | No gray blocks | 7 `block`s | Use bold lead-ins instead. |

**Mechanical counts:**
- Lab: 59 cells; 26 typed against 2 given; 157 typed lines plus 11 answer lines (median 7); 21 typed cells over 4 lines and 14 over 6; 69 lines over 90 characters (max 143); 1 typed `def`, 4 typed comprehension cells, 1 `lambda`, 1 typed regex; 1 cell `not-run-live`.
- Deck: 52 frames, 15 with code (11 full-width, 2 with code on the left, 2 on the right at 0.45/0.46, none at 0.6, 2 over 12 lines, 3 that are printed output); about 13 output-comment lines; 39 lines over 58 characters (max 80); 1 `def`, 1 `try`; 7 gray blocks.

**Effort:** M. The parts split naturally, and the sites are stable sandboxes, so a rerun is cheap. Most of the work is splitting cells and writing the 3 minimal calls. The deck's Wednesday section grows from 6 frames to about 20.

## Week 07 — Archived Web Pages (Wayback Machine playback, Availability API, CDX Server, gensim)

**Distance from the rules:** The cell shapes are moderate: 27 typed cells, a median of 5 lines. But the key is the least trustworthy of the three. 21 cells are `not-run-live`, because the Archive refused the cloud machine, and "What did we learn?" still holds placeholder answers. There are no checkpoints, though the Archive is the service most likely to refuse a room on one address. It has 0 given cells, 3 typed functions (`get_snapshot_stats`, `get_wayback_content`, `preprocess_document`), 5 typed loops that send requests, and 4 typed comprehensions. Its first Availability call prints `response.json()` without looking first, so a 429 (an HTML page) surfaces as `JSONDecodeError`. The deck has only 5 code frames, all full-width, two with two listings. One invents an output table (`2000 150 8500 …`), and its code differs from the key (`timeout=60`, `if … is not None`, quarterly dates, `stop`/`dct`).

**Priority:** P1 for the lab, because it has no run key and no checkpoints for the most refusing service in the course. The deck is P2: a small, cheap rewrite.

**Minimal first calls to add** (the Availability calls were checked live on 2026-11-16; CDX reset the cloud machine's connection, so check it from a laptop):
- **Availability API** (Step 3, before CNN):
  - Typed: `params = {"url": "thefacebook.com", "timestamp": "20040212"}`, then `response = requests.get(avail_url, params=params, headers=HEADERS)`, then `print(response.status_code, response.text[:300])`.
  - Students predict the capture they took apart in Step 1. It came back exactly: `"timestamp": "20040212031928"`, `"status": "200"`, `"available": true`.
  - One change, typed: `"url": "this-site-does-not-exist-4617.org"`. It returns `{"archived_snapshots": {}}`. Ask what `["closest"]` would do on that answer.
- **CDX Server** (Step 5, before `facebook.com/terms`):
  - Typed: `params = {"url": "thefacebook.com", "output": "json", "fl": "timestamp,statuscode", "limit": 3}`, then the request, then `print(response.status_code, response.text[:300])`.
  - Students predict 4 rows: the header row `["timestamp", "statuscode"]`, then 3 captures starting in 2004, oldest first. Each is a list, not a dict, which is why Step 5 builds `pd.DataFrame(data[1:], columns=data[0])`.
- **Playback and `id_`** (Step 2): replace the typed comprehension loop with two by-hand cells.
  - `wrapped = requests.get(CAPTURE, headers=HEADERS)` and `print(wrapped.text.count("/web/"))`.
  - Then the same for `RAW`. Students predict that `RAW` has no `/web/` links. Check the count in the key.
- **gensim** (Step 10, before the first and last ToS versions; verified with gensim 4.4.0 and the book's 198-word stopword list):
  - First `simple_preprocess("We may share your data with Facebook's partners.")` gives `['we', 'may', 'share', 'your', 'data', 'with', 'facebook', 'partners']`. Lowercased, the punctuation and the `'s` are gone.
  - Then three sentences: `"We collect your data."`, `"We collect and share your data."`, `"Cats sleep all day."`. Without stopwords these become `['collect','data']`, `['collect','share','data']` and `['cats','sleep','day']`.
  - Their similarities to the first are **1.0, 0.816, 0.0**. Students predict "the first two high, the third zero". This mirrors week 13's three-sentence embedding call.

**Lab — top revisions**
| Part / cell | Rule | Now | Proposed |
|---|---|---|---|
| Key note, Step 12 | The key is run; Discuss uses the key's numbers | 21 cells `not-run-live`; the answers say "TO BE WRITTEN AFTER A LIVE RUN" | Run the rebuilt key from the instructor's laptop. Then write the "What did we learn?" answers and check every Discuss number against the run. |
| Whole lab | Three parts; checkpoints | One 85-minute notebook, no checkpoints | Part 1 (Mon) is addresses, playback, `id_` and Availability. Part 2 (Wed) is CDX: the minimal call, `facebook.com/terms`, the plot, and the 2005 status codes. Part 3 (Fri) is versions and bag of words. Checkpoints in `labs/week-07/data/`: `cdx-facebook-terms.json`, `cdx-facebook-2005.json`, `cnn-three-eras.csv`, and the ten `wayback_cache/*.json` files. |
| Step 3, cell 14 | Look before you read | `print(response.json())` | `print(response.status_code, response.text[:300])` first (the minimal call above). Then `data = response.json()`, and go down one level a cell: `data["archived_snapshots"]`, then `["closest"]`. |
| Step 2, cell 11 | No typed loop that sends requests; no typed comprehension | An 8-line typed loop over `[CAPTURE, RAW]` with two comprehensions | Use the two by-hand `count("/web/")` cells above. Make the link-count comparison a given cell. |
| Step 4, cells 18–19, 21 | No typed `def`; by hand, then given | A typed 8-line `get_snapshot_stats` with a 5-key dict return; a typed loop over 3 dates | Students type CNN 2000 by hand (Step 3 already does most of it) and one count, `len(soup.find_all("a"))`. Give the function and the three-era loop. Load the checkpoint `cnn-three-eras.csv`. The microsprint changes the site name in the given cell. |
| Step 5, cell 24 | A long `params` is given whole | A typed 6-key `params`, with lines over 120 characters | Give the dictionary whole. Students type only `"collapse": "digest"` and `"filter": "statuscode:200"`, the two values that carry the idea. Print the status before `.json()`. |
| Steps 8–9, cells 37, 43 | No typed `def`; a typed loop never sends requests | A typed 9-line `get_wayback_content`; a typed 9-line cache loop with `with open` | Students type one version by hand: an Availability call for 2010, `id_`, then `get_text`. Give the function and the cache loop. The cache doubles as the Part 3 checkpoint. |
| Steps 10–11, cells 48, 51–52 | No typed comprehension or `def` | Typed token comprehensions, `def preprocess_document`, a `change_scores` comprehension | Start with the three-sentence gensim call above (typed, about 3 lines a cell). Give `preprocess_document` and the corpus and index. Students type one score, `1 - index[corpus[0]][1]`. Give the timeline loop and plot. |

**Deck — top revisions**
| Frame | Rule | Now | Proposed |
|---|---|---|---|
| 21 "Availability API" | 0.37/0.6; ≤8 lines; look first; same as the key | 10 full-width lines with `if/else`, `cnn.com`, and no `HEADERS` | Two frames at 0.37/0.6: the `thefacebook.com` minimal call (the status and the text's start), then one level down to `["closest"]`. Ask: "Which timestamp do you expect?" |
| 22 "Retrieve it raw with `id_`" | One listing; no printed outputs | Two listings, the second a made-up output table (`2000 150 8500 …`) | Cut the table. One frame for `RAW = …` and the `/web/` count. Ask: "How many archive links should the raw page have?" |
| 23 "CDX Server" | ≤8 lines; same as the key | 12 lines with `timeout=60` and its own `headers` | Add the `limit=3` minimal frame first. Then the `params` frame, cut with `...` per the rules, and the DataFrame frame. Remove `timeout`. |
| 24 "Tracking a document" | One listing; same as the key | Two listings; a quarterly loop with `if snap is not None`; `# Retrieved 68 snapshots …` | One by-hand frame (one version) and one given-loop frame matching the key's ten `2YS` dates and `wayback_cache/`. Cut the output line. |
| 25 "bag-of-words" | ≤8 lines; ≤58 characters; no nested comprehension | 12 lines, 7 over 58 characters, a nested comprehension | Three frames: `simple_preprocess` on one sentence; three sentences, then `Dictionary`, `doc2bow`, then the index; `1 - similarity`. |
| Wednesday section | One frame per lab cell | 5 code frames for 27 typed cells | Rebuild as about 20–25 frames, one per cell, each Part opening with "Today: Part N" and setup frames as in week 13. |
| 1, 26, 29, 37 | No gray blocks | 4 `block`s | Use bold lead-ins instead. |
| Monday (20 concept frames) | From week 11, Monday is Part 1 of the lab | A screenshot-led concepts day | The instructor should decide whether to keep a concepts Monday (as week 10 did) or fold about 6 frames ("The URL is the query", "Reading the dots", `id_`) into Part 1's steps. |

**Mechanical counts:**
- Lab: 59 cells; 27 typed against 0 given; 145 typed lines plus 12 answer lines (median 5); 18 typed cells over 4 lines and 9 over 6; 63 lines over 90 characters (max 141); 3 typed `def`s, 4 typed comprehension cells, 5 typed loops that send requests; 21 cells `not-run-live`.
- Deck: 38 frames, 5 with code (all full-width, 2 with two listings, 1 invented output table); about 9 output-comment lines; 20 lines over 58 characters (max 88); 1 nested comprehension; 4 gray blocks.

**Effort:** L for the lab. It needs a full live run from a laptop, 4–5 checkpoints and a rewrite of "What did we learn?" on top of the restructure. The deck is S–M: 5 frames become about 20 short ones.

## Week 06 — Parsing Static Web Pages (ch. 6: robots.txt, `read_html`, decoy tables, infoboxes, Drupal cards, custom tags / JS shells)

**Distance from the rules:** Furthest of the three. The lab is a single 85-minute block of 12 steps, with no parts, no checkpoints and only one given cell, holding 167 typed lines (about 2 a minute, double the budget). Students type two functions (`read_infobox`, 8 lines; `parse_oscar_ceremony`, 17 lines, with nested loops and a conditional expression), three loops that send requests, regexes, comprehensions and format specs. Nothing new (`read_html`, CSS selectors, custom tags) gets a minimal call before the real page. The deck predates the lab and contradicts it: its Strategy 1 and 8 code requests Box Office Mojo and IMDb, which the lab's own Step 1 found disallowed. Strategy 7 uses `tile-dynamic` where the lab uses `media-info-tile`, and "Make it reusable" has a `return` outside a function, so it won't run.

**Priority:** P1. The deck shows code that breaks the lab's own `robots.txt` finding and code that doesn't run, so fix it before anything else. The lab rebuild is the largest of the three.

**Minimal first calls to add:**
- **`RobotFileParser`** (Step 1, before the six-site loop): `rp.parse(["User-agent: *", "Disallow: /w/"])`, then `rp.can_fetch(CLIENT, "https://en.wikipedia.org/w/index.php")` should give `False` and `.../wiki/The_Godfather` should give `True`. After that, one real site by hand, then the loop as a given cell.
- **BeautifulSoup on HTML rows, cell by cell** (Step 2, before The Numbers): `row = BeautifulSoup("<tr><td>1</td><td></td><td>Aquaman</td></tr>", "html.parser")`. Students see `[c.get_text(strip=True) for c in row.find_all("td")]` give `['1', '', 'Aquaman']` (the comprehension goes in a given cell, or loop and print), and `row.text` give `1Aquaman`, so the empty cell disappears. This is the deck's "one-line bug" frame, shown on input students can read in full.
- **`pd.read_html`** (Step 3, before the page with 92 tables): `pd.read_html(StringIO("<table><tr><th>Film</th><th>Year</th></tr><tr><td>Titanic</td><td>1997</td></tr></table>"))`. Students should see a list of length 1 holding a 1×2 DataFrame with columns `Film` and `Year`. That they get a list explains `tables[0]` before the real call.
- **Regex cleanup** (Step 4, before the whole column): `pd.Series(["$2,923,706,026", "T$2,264,743,305"]).str.replace(r"[^0-9]", "", regex=True)` should give `2923706026` and `2264743305`. Both are correct, so the microsprint can still discover F8.
- **CSS selector `table:has(caption)`** (Step 7, before French Wikipedia): `BeautifulSoup('<div class="infobox_v3"><table><caption>Le Parrain</caption><tr><th>Réalisation</th><td>Coppola</td></tr></table></div>', "html.parser")`. `select("table.infobox_v3")` should give `[]`, and `select("table:has(caption)")` one match.
- **Custom tags** (Step 10, before Rotten Tomatoes): `BeautifulSoup('<media-info-tile><rt-text slot="criticsScore">93%</rt-text></media-info-tile>', "html.parser").find("rt-text", attrs={"slot": "criticsScore"}).text` should give `'93%'`.
- **JS shell** (Step 10): a single fetch of `https://quotes.toscrape.com/`, counting `div.quote`, should give `10`. Then `/js/` by hand should give `0`, and only then the comparison.

**Lab — top revisions**
| Part / cell | Rule | Now | Proposed |
|---|---|---|---|
| Whole lab | The week, 3 parts, checkpoints | One 85-min block, Steps 0–11; no setup per day; 0 checkpoints | Part 1: robots, decoy table, `read_html`. Part 2: cleanup, infobox in EN/FR/ES. Part 3: Oscars cards, several years, custom tags and JS. Each part has its own setup cell. Checkpoints: The Numbers HTML, Oscars 2024–26 CSV, RT HTML dated snapshot (its grid changes weekly) |
| Step 7 cell 32 / Step 9 cell 45 | By hand, then given; no typed `def` | `read_infobox` (8 lines) and `parse_oscar_ceremony` (17 lines, nested `for`, `if … else`) typed | Both become given cells. Students find in them the lines they typed in Steps 6 and 8 |
| Step 1 cell 6; Step 9 cell 46; Step 10 cell 52 | No typed loop that sends requests | Typed `for page in CHAPTER_PAGES`, `for year in [...]`, and a `for url` loop with `requests.get` | One site, one year and one URL typed by hand, then a given loop |
| Step 2 cell 9 | 1–4 lines; one step a line; look first | 8 lines: two requests, parse, `enumerate` loop with tuple unpacking | Split into: request and `print(status, text[:200])`; parse; `len(tables)`; a given cell listing class and rows |
| Step 8 cells 39–40 | ≤6 lines; no conditional expression | 7 and 13 lines; `film_tag.get_text() if film_tag else None` typed | Type the first card's four fields one per cell (1–2 lines each). The loop with its guard becomes given, and the Step text explains `if … else` |
| Steps 4–5 cells 19, 25 | Little Python: no regex or format spec typed | `str.replace(r"[^0-9]"…)`, `str.extract(r"\$([\d,]+)")`, `f"{…:,.0f}"` typed | Students type `pd.to_numeric(cleaned, errors="coerce")` and the comparison. The regex lines are given, with one sentence explaining the pattern |
| Cells 3, 4, 28, 33, 38 (first fetch of Wikipedia, oscars.org, fr/es WP, RT) | Look before you read | Only The Numbers and quotes print a status; the key note itself says "print `response.status_code` first" | Each service's first request prints `response.status_code, response.text[:200]` |
| Typing budget | ≤55/50 min (Mon/Wed), ≤40 Fri | 167 typed lines; 17 typed lines over 90 chars; median typed cell 6 lines, maximum 17 | About 130 lines across 3 parts, or about 85 if it stays at 85 minutes. Prompts at most 2 lines (5 cells now use 3) |

**Deck — top revisions**
| Frame | Rule | Now | Proposed |
|---|---|---|---|
| Strategy 1 — the one-line win (L339) | Same behavior as the lab | `read_html` on boxofficemojo.com, which the lab's Step 1 found disallowed; inline `# 1 -- no ambiguity` | Show the `read_html(StringIO(...))` minimal call, then the Wikipedia `oldid` fetch with `WIKI_HEADERS`, as in the lab's Step 3. Two frames, with narration at 0.37 and code at 0.6 |
| Strategy 8 — watching requests fail (L493) | Same as the lab; no output | Requests IMDb (disallowed); `# 202 0 -- zero bytes` | Use quotes.toscrape `/` vs `/js/` (lab Step 10). Ask "How many quotes do you expect?" and don't print the answer |
| Strategy 6 — Oscars parser (L454) | ≤8 lines; no line over 58 characters; ≤2 chained methods | 14 lines, 8 over 58 characters, nested loop, `# 24 categories` | 3–4 frames: find the area and its cards; one card's name; one honoree's three fields; then the given loop, with one argument per line and the class names in named variables |
| Make it reusable — and defensive (L508) | One listing a frame; lab style | Two listings; `scrape_oscar_year` vs the lab's `parse_oscar_ceremony`; `try`/`return` outside a function (won't run); `raise_for_status` | One frame with the given multi-year loop (`parse_oscar_ceremony`, `time.sleep(1)`). Move the error-handling talk to narration or a Discuss question. Keep the "Error flavors" alertblock |
| Strategy 3 — cleaning (L399) | One listing; no output; ≤58 characters | Two listings, 7 wide lines, 3 output comments; `read_html(url)` with no headers on the live page (the lab pins `oldid` and passes `StringIO`) | Two frames: the fetch plus `read_html`, then the cleanup with one comment line above each step |
| Strategy 7 — a different card (L474) | Same as the lab; `if … else` | `tile-dynamic` / `span.p--small` / `critics-score`, while the lab uses `media-info-tile` / `rt-text slot="criticsScore"`; 12 lines | Use the lab's tags. Show the minimal custom-tag call first, then a 6-line count |
| The one-line bug (L370) | Never code on the left; one listing | Two listings in the left 0.6 column, narration on the right | Swap the columns (narration 0.37 / code 0.6) and keep one listing. Show the `.text` vs `find_all` contrast on the 3-cell row from the minimal call |
| Strategies 4–5 (L417, L437) | ≤8 lines; ≤58 characters | 12 and 9 lines; `BeautifulSoup(requests.get(...).text, …)` nested; output comments `'Francis Ford Coppola'` and `'The Godfather'` | Split the fetch, parse and loop over 2 frames each. Remove the output comments and ask "Which label holds the director?" |

**Mechanical counts:** Lab: 57 cells, 27 code (1 given, 25 typed), 0 parts, 85 minutes, 167 typed lines, 19 typed cells over 4 lines, 2 typed `def`, 11 typed cells with loops, 0 checkpoints, 9 step texts over 90 words. Deck: 27 frames; 10 code frames with 13 listings; 3 frames with 2 listings; 4 listings over 8 lines; 1 code-left frame; 38 lines over 58 characters; 7 output comments.

**Effort:** L. The lab needs a rebuild into three parts with two functions moved to given cells, about 8 new minimal-call cells and three checkpoints. The deck's 10 code frames become about 22, and 4 of them need new code to match the lab.

## Week 05 — Web Architecture and Protocols (ch. 5: DevTools, TCP/IP, DNS, HTTP status, User-Agent, Session, URLs)

**Distance from the rules:** Medium. The lab has no typed functions, and its first Wikipedia request prints the status before reading anything. But it holds 127 typed lines in 83 minutes, 7 typed loops that send requests (Steps 5, 6, 7 microsprint, 8, 9 twice, 10 microsprint), and 9 prompts of 3 lines. ipify and ip-api are chained straight to `.json()[...]` without looking first. There are no parts and no checkpoints, and the 429-prone pageviews microsprint is `not-run-live`. The deck teaches code the lab deliberately leaves out (`try`/`timeout` in `diagnose_request`, `Retry` mounted on a Session, traceroute, wget). It also uses 3 two-listing frames and has 27 lines over 58 characters.

**Priority:** P2. Fixing the deck is cheap and matters: today it teaches the error handling the lab rejects. The lab needs smaller cells and minimal calls rather than restructuring.

**Minimal first calls to add:**
- **`select_one` / CSS selector** (Step 1, before the 768 KB page): `BeautifulSoup('<h1 id="firstHeading">Hello</h1>', "lxml").select_one("#firstHeading").text` should give `'Hello'`.
- **The `!` shell and `lines = !…`** (Step 3, before `curl -v … 2>&1` and its filter loop): `lines = !echo hello`, then `print(lines)`, should give `['hello']`. Then `!curl -sI -A "<UA>" https://en.wikipedia.org/wiki/Web_scraping`, whose first line should be `HTTP/2 200`.
- **ipify** (Step 3): `ip_response = requests.get("https://api.ipify.org?format=json", headers=HEADERS)` and `print(ip_response.status_code, ip_response.text[:200])` should show `200 {"ip":"…"}`, masked before anyone shares it.
- **dnspython** (Step 4, before `en.wikipedia.org`): `dns.resolver.resolve("one.one.one.one", "A")`. Students should see `1.1.1.1` and `1.0.0.1`, an answer they can predict from the name. Then Wikipedia.
- **ip-api** (Step 4 microsprint, before `WIKI_IP`): `requests.get("http://ip-api.com/json/8.8.8.8", headers=HEADERS)` should print status 200, then `"isp": "Google LLC"` and `"country": "United States"`.
- **Pageviews** (Step 6, before the month): one day, `.../daily/20260101/20260101`. `len(data["items"])` should be `1`, and students read that one dict in full.
- **httpbin** (Step 8, before the three-header loop): one typed call with `HEADERS` should give `{'user-agent': 'WebDataScience/1.0 (<your email>)'}`. The loop over None / honest / spoofed becomes given.
- **`requests.Session`** (Step 9, before the loop): `session.get(PAGE)` once, then `print(session.headers["User-Agent"], r.status_code)` should show your UA and `200`.
- **`urlparse` / `quote`** (Step 10, before the Census URL): `urlparse("https://en.wikipedia.org/wiki/AC/DC")` should give `netloc='en.wikipedia.org'` and `path='/wiki/AC/DC'`, and `quote("AC/DC", safe="")` should give `'AC%2FDC'`.

**Lab — top revisions**
| Part / cell | Rule | Now | Proposed |
|---|---|---|---|
| Whole lab | The week, 3 parts, checkpoints | One block, Steps 0–11, 83 minutes, no checkpoints; Step 7 microsprint `not-run-live` (429s) | Part 1: DevTools, `select_one`, headers. Part 2: socket, curl, DNS, ip-api. Part 3: status codes, pageviews, UA, Session, URLs. Checkpoints: Jan 2026 pageviews JSON for 3 articles; a saved `curl -v` transcript (the key's run went through a proxy) |
| Step 5 cell 23 | No typed loop that sends requests; ≤90 characters | `for url in [PAGE, missing]` with a 138-character f-string, plus an anonymous request: 7 lines | One URL by hand: status, then `headers["Content-Type"]`, one per line. The 404 by hand. The anonymous 403 by hand, with `text[:120]` |
| Steps 7, 8, 9, 10 cells 33, 37, 40, 42, 48 | By hand, then given | 5 more typed loops with `requests.get` / `session.get` | One case typed (one article, one header, one `elapsed`), then a given loop |
| Step 3 cell 13; Step 4 cell 20 | Look before you read; one step a line | `requests.get(...).json()["ip"]`; `requests.get(...).json()` then `location['city']` | `response =` / `print(status, text[:200])` / `data = response.json()` / read one key |
| Step 2 cell 8; Step 7 cell 31 | Little Python: no format spec typed | `f"{len(...):,}"`, `f"{… :.2f}"`, `ax.set(title=f"…")` | Plain `print(len(response.content))`. Number formatting goes in given cells only |
| Step 2 microsprint cell 10 | ≤6 lines; given plot | 11 lines: a dict of dicts plus a plot | Students type their own counts into a 2-line dict. The DataFrame and bar chart are given |
| Step 4 cell 18 | ≤4 lines; minimal first | 8 lines: resolve, loop, `canonical_name`, TTL, socket, `WIKI_IP` | Minimal call `one.one.one.one`; then `answers = …` and `print(answers[0])`; then TTL; then `socket` agrees. Four cells |
| 9 prompts of 3 lines | Prompts: 1–2 lines | Cells 2, 8, 10, 18, 20, 23, 28, 31, 46 | Split each cell where its prompt needs three lines |

**Deck — top revisions**
| Frame | Rule | Now | Proposed |
|---|---|---|---|
| Diagnosing HTTP errors (L342) | Same as the lab; no error handling; ≤8 lines | `def diagnose_request` with `try`/`except`/`timeout=10`, 11 lines | The lab's straight lines: one request, then status, Content-Type, Server, size (2 frames). Move `try` to a Discuss-style question |
| A loop over one host… Session (L406) | Same as the lab; ≤8 lines; ≤58 characters | `Retry` + `HTTPAdapter` mount, 10 lines, 5 wide lines | Session, `headers.update`, one `get` (minimal), then the given loop with `sleep(1)`. Mention `Retry` in narration only |
| Make an API call, get a time series (L360) | Never code left; one listing; OO matplotlib | Two listings in the left 0.6 column, `df.plot(...)`, `ua` vs the lab's `HEADERS` | Three frames: one-day call; month with `PAGEVIEWS` f-string; DataFrame plus `plt.subplots()` plot. Image on its own frame if needed |
| Locating yourself and the server (L274) | No output; look first; same as the lab | ipify with no UA; output `# {'ip': '128.138.xxx.xxx'}`; DNS in the same listing | Split: ipify (status, text, masked) / DNS minimal `one.one.one.one`. Ask "Is that your laptop's address?" |
| Parse — and build — URLs (L471) | One listing; no output | Two listings, 5 wide lines, 3 output comments (`'https', 'api.census.gov'…`, `'AC%2FDC'`) | Two frames: `urlparse` on a Wikipedia URL, then `quote("AC/DC", safe="")`, each with a question in place of its output |
| Traceroute / curl & wget / sleep() / terminal (L307, L426, L441, L454) | Same as the lab; ≤40 words; one listing | 4 frames of terminal tools the lab doesn't use; 38–97 words; `->` output lines; one frame with 2 listings | Keep the one `curl -v` frame that matches lab Step 3. Fold dig/whois/wget into one concept frame, or drop them |
| The terminal, inside the notebook (L290) | ≤40 words; minimal first | 86 words; `platform` `if/else` around `!ping` | `!echo hello` / `lines = !echo hello` as the minimal call; `ping` moves to narration (it is optional in the lab) |
| User-Agent spoofing, mechanically (L389) | ≤58 characters; one call by hand | 4 wide lines; two `requests.get(...).json()` calls nested in `print` | Honest call by hand (frame 1); spoofed dict plus the given loop over three (frame 2), one argument per line |

**Mechanical counts:** Lab: 53 cells, 22 code (1 given, 20 typed), 0 parts, 83 minutes, 127 typed lines, 16 typed cells over 4 lines, 0 typed `def`, 10 typed cells with loops (7 send requests), 11 typed lines over 90 characters, 2 cells `not-run-live`, 0 checkpoints. Deck: 27 frames; 12 code frames with 15 listings; 3 frames with 2 listings; 3 listings over 8 lines; 1 code-left frame; 27 lines over 58 characters; about 8 output lines; 5 code frames over 80 words.

**Effort:** M. The lab needs no new functions removed, but each request loop needs splitting into a by-hand case plus a given loop, and 9 minimal calls added. Most of the deck's terminal frames are cuts; about 6 frames need new code from the lab.

## Week 04 — Data Formats: XML and JSON (ch. 4: House roster XML via BeautifulSoup, `json`, NASA POWER API)

**Distance from the rules:** Medium. The lab's first request is a model of "look before you read": status, Content-Type, encoding and first bytes. Its cells are too big, though: the median typed cell is 7 lines, cell 8 has 8 lines and a 4-line prompt, and 6 prompts are 3 lines or more. Students type a function (`get_daily`, 10 lines) and a request loop with tuple unpacking. Comprehensions and `zip` are typed. No parser or API gets a toy call before the real data, and POWER's first call asks for a full year of three variables. The deck has 3 code-left frames on Wednesday, the instructor's hardest rule. Its live JSON example is Open-Meteo where the lab uses NASA POWER, and it fetches the roster without `HEADERS`.

**Priority:** P2 for the lab. The deck is P1 and cheap, since 3 code-left frames are a "never" and its JSON frame doesn't match the lab.

**Minimal first calls to add:**
- **BeautifulSoup `"xml"`** (Step 2, before the 441-member file): parse a two-member string (the deck's `house_raw`: Neguse D-CO, Hurd R-CO; public officials). `len(soup.find_all("member"))` should give `2`, `soup.find("lastname").text` should give `'Neguse'`, and `soup.find("state")["postal-code"]` should give `'CO'`. Students see text and attribute on input they can read whole.
- **`Counter`** (Step 3): `Counter(["D", "R", "D"])` should give `Counter({'D': 2, 'R': 1})`. Then the roster's parties.
- **`json.loads`** (Step 5, before the `to_dict` round trip): `json.loads('{"state": "Colorado", "seats": 8}')`. `type(...)` should give `dict`, and `["seats"]` should give `8`, an int and not a string, which contrasts with XML.
- **NASA POWER** (Step 6, before the full year): `params` with `"parameters": "T2M_MAX"`, `"start": "20250101"`, `"end": "20250103"`, and Boulder's coordinates. Print `response.status_code, response.text[:200]`, then `data["properties"]["parameter"]["T2M_MAX"]`, which should give three dated keys and three numbers (January highs, near 0–10 °C). Then change one key: three parameters and the whole year.
- **`pd.DataFrame` from a dict of dicts** (Step 7): `pd.DataFrame({"high": {"20250101": 5.1, "20250102": 7.3}, "low": {"20250101": -6.0, "20250102": -4.2}})` should give 2 rows, keyed by date, and 2 columns. This shows the alignment by key before 365 rows.

**Lab — top revisions**
| Part / cell | Rule | Now | Proposed |
|---|---|---|---|
| Whole lab | The week, 3 parts, checkpoints | One block, Steps 0–9, 85 minutes, 0 checkpoints; the roster has no fixed date | Part 1: XML minimal, roster, tree, Counter. Part 2: XML→DataFrame, JSON strings, broken JSON. Part 3: POWER minimal, year, plot, given places loop. Checkpoints: roster XML snapshot (publish-date 2026-10-01) and POWER 2025 CSV |
| Step 8 cells 37–38 | No typed `def`; no typed request loop; no tuple unpacking | `get_daily()` (10 lines) typed; `for place, latitude, longitude in places:` with `requests` and a 2-line dict | Function and loop both given. Students type the one changed value (Leadville's coordinates), then the microsprint's place |
| Step 2 cell 8 | 1–4 lines; prompt 1–2 lines | 8 lines under a 4-line prompt: parse, root attribute, children (comprehension), dot notation, `find`, attribute, `find_all` | 4 cells: parse plus `publish-date`; first member's `lastname`; `state["postal-code"]`; `members = find_all` and `len` |
| Step 3 cell 13 | Little Python | Two list comprehensions, `for … if` and tuple pairs in one 7-line cell | Typed: `parties` via a given comprehension, then `Counter(parties)`. Vacancy loop and party/caucus pairs given |
| Step 4 cell 16 | ≤6 lines; one entry a line | 9 lines; a 5-key dict packed onto 3 lines inside a loop | By hand: `first = members[0]`; a record dict for it, one key a line. The loop over 441 is given |
| Step 2 microsprint cell 10 | No comprehension, `zip` or tuple unpacking typed | Two comprehensions plus `for a, b in zip(...)` | Given: build both lists. Typed: `print(ours[i], theirs[i])` for one index found by the class |
| Step 6 cell 26 | Look before you read; long params given | 7-key `params` packed onto 2 lines; `.json()` with no status print | Minimal 3-day call first. The full `params` is given one key a line, with students typing `start`/`end`. Print the status and `text[:200]` before `.json()` |
| Step 7 cells 30–31; microsprint 34 | ≤4 lines; given plot | 7-line DataFrame cleanup; 7-line and 6-line typed plots; `f"{…:.0f}"` | Students type `pd.DataFrame(...)` and `to_datetime`; the fill-value and rename lines are given. Both plots are given |

**Deck — top revisions**
| Frame | Rule | Now | Proposed |
|---|---|---|---|
| XML → DataFrame: the real House roster (L297) | Never code left; one listing; same as the lab | Code at left 0.55 with a second listing at right; no `HEADERS`; `if st else None` guard (the lab drops it); output comments | 3 frames: fetch with `HEADERS` and print status/Content-Type/first bytes; parse plus `publish-date`; one member to a record. Then the given loop. Narration 0.37 / code 0.6 |
| JSON: peel the onion on a live API (L354) | Never code left; same as the lab; no output | Open-Meteo code in the left 0.6 column; output comments `# latitude, longitude, daily...` | Switch to NASA POWER as in the lab: 3-day minimal call, then `.keys()` one level per frame. The figure goes on its own frame (the lab's 2025 high/low plot) |
| Data exists in two different places (L264) | Never code left; one listing | Two listings in the left 0.6 column; narration at right (80 words) | Split: text vs attribute on the two-member string (one frame); the `None` / `AttributeError` guard as an Error-flavors aside (one frame). Narration left |
| Parsing XML with BeautifulSoup (L246) | Comment above each step; no output | Trailing comments `# 2`, `# Joe Neguse (D) / Jeff Hurd (R)`; 9 lines, 4 wide | This becomes the minimal-call frame: `house_raw`, `find_all`, `len`, one `.text`. Ask "How many members? What's the first last name?" |
| XML: a tree of nested tags (L138) | ≤8 lines; ≤58 characters | 12-line listing at `\large` with inline `# value in TEXT` notes | Cut to one member (8 lines). Put the TEXT / ATTRIBUTE distinction in the narration column |
| JSON: parse a string… (L337) | One step a frame; no output | `json.loads` plus the list-of-dicts DataFrame in one listing; `# Colorado`; "keys -> columns" | Two frames: `json.loads` minimal (`type`, `["seats"]`), then `pd.DataFrame(census)` |
| Missing: Counter and vacancies, encoding | Same as the lab | The deck has no frame for lab Steps 1 and 3 (`response.content` vs `.text`, the 441 vs 439 count) | Add 2 frames: look before you parse (status, Content-Type, `encoding`); `Counter(parties)`, with the question "What is `''`?" |
| JSON vs XML (L171) | No gray blocks | Two gray `block`s side by side | Bold lead-ins, one column each, as plain text |

**Mechanical counts:** Lab: 45 cells, 19 code (0 given, 18 typed), 0 parts, 85 minutes, 118 typed lines, 16 typed cells over 4 lines (9 over 6), 1 typed `def`, 5 typed cells with loops (1 sends requests), 3 with comprehensions, 10 typed lines over 90 characters, 6 prompts of 3+ lines, 0 checkpoints. Deck: 31 frames; 10 code frames with 12 listings (7 on Wednesday); 2 frames with 2 listings; 6 listings over 8 lines; 3 code-left frames (plus 1 on Friday); 14 lines over 58 characters; about 8 output comments; 2 gray blocks.

**Effort:** M. The lab has one function and one loop to move into given cells, about 8 oversized cells to split, and 5 small minimal calls. The deck needs its JSON example switched to POWER and 3 code-left frames rebuilt, about 7 frames growing to about 14.

<!-- Audit of weeks 3, 2, 1 against labs/AUTHORING.md (rev. 2026-11-16) and slides/common/AUTHORING.md (2026-11-12/13). Read-only; origin/main @ 69317d1. -->

Applies to all three weeks:
- **The labs have never been taught.** They were written on 2026-10-21 for the next offering (labs/README.md). Decks 1–3 send students to the chapter's companion notebook (`ch-02-ethics.ipynb` and so on), not to `lab-0N.ipynb`. Nothing in these decks matches a lab cell yet, so the deck work adds frames; it doesn't rework code that's already aligned.
- **The decks' code frames are the instructor's.** `git blame`: every line of the code frames in decks 2 and 3 was last edited by the instructor (Overleaf). AUTHORING says to "never rewrite a frame the instructor authored", and decks 2 and 3 are its named voice references. Every change proposed to an existing frame below needs the instructor's sign-off. New lab frames can be added around those frames without it.
- **The three-part form may not suit these weeks.** All three labs are in the pre-week-10 form: one 85-minute "Wednesday" notebook, no parts, no setup step per day, no checkpoints, and "Run All Above" on Friday. A three-part (135-minute) rebuild only makes sense if the next offering makes weeks 1–3 live-coding weeks. Chapters 2 and 3 have heavy Monday concept material (law and policy), so week 10's form, a Monday lecture plus a two-part Wed/Fri lab (~85 minutes), fits better. The cell-level rules (1–4 typed lines, by hand then given, one minimal call first, look before you read) are worth applying in either form.

## Week 03 — The post-API age (access matrix, dead endpoints, Wayback, Mastodon)

**Distance from the rules:** This lab is furthest from the rules of the three. Of its 15 typed cells, 7 are loops that send requests. Students also type tuple unpacking (`for name, url in X.items()`), format specifications (`{name:<12}`, `!r`), a `try` block, and a 26-line plot. No new service gets a single small call before its loop: Wayback and Mastodon are indexed (`["archived_snapshots"]["closest"]`, `.json()["stats"]["user_count"]`) without printing what came back first. The deck has one Python listing, the chapter's `probe()`. The lab doesn't use it, and it breaks most of the "Code shaped for reading" rules.

**Priority:** P1. This lab is the furthest from the rules, and on 2026-11-16 the Wayback availability API answered `example.com` and `www.colorado.edu` with HTTP 200, `"archived_snapshots": {}` and `"error": {"code": "timeout"}`. Step 5's code, which goes straight to `["closest"]`, would then die on a `KeyError` without showing why. Adding deck frames is cheap; the lab is a rebuild.

**Minimal first calls to add:**
- **Hacker News (Step 1, before the front pages):** `requests.get("https://hacker-news.firebaseio.com/v0/item/1.json", headers=HEADERS)`, then `print(response.status_code, response.text[:200])`. Students predict item 1, a story. They see `200` and `{"by":…,"id":1,…,"title":"Y Combinator","type":"story",…}`. Then `item = response.json()` and `item["title"]` gives `Y Combinator`. Print only the title, not `by`. The list of ~500 ids in `topstories.json` comes after this.
- **Access matrix (Step 2, before the 8-target loop):** send one request by hand to `TARGETS["Wikipedia"]` and print the status, `content-type` and `text[:200]`. Students predict `200 application/json` and see `"sitename":"Wikipedia"`. Then one gated target by hand, `TARGETS["X (Twitter)"]`, where they should see a 401 with `application/problem+json`. Then `VERDICTS.get(response.status_code, "other")` on that one response. Only then the given loop.
- **Retired endpoints (Step 4):** Pushshift alone by hand, printing the status and `text[:60]`. Expect `403 {"detail":"Not authenticated"}`, as in the key's run. CrowdTangle's `ConnectionError` stays in the given `try` cell.
- **Wayback availability (Step 5):** `params = {"url": "www.crowdtangle.com", "timestamp": "20200101"}`, then `print(response.text)`. Students predict a capture near 1 Jan 2020; on 2026-11-16 it was `"timestamp": "20200103071533"`, `"status": "200"`. Then, as a second small call, `"url": "example.com"`, to show the 200 that holds an `"error"` and no snapshot. Add a Discuss question on it: an empty answer is accepted without an error and gives a wrong result.
- **Mastodon (Step 6, before the 6-server loop):** `requests.get("https://mastodon.social/api/v1/instance", headers=HEADERS)` and `print(response.status_code, response.text[:200])`. Students should see `200` and `"uri":"mastodon.social"`. Then one public-timeline request to the same server with `params={"limit": 1}`, which gave `422 {"error":"This method requires an authenticated user"}` on 2026-11-16. Check the provider's docs before relying on this: Mastodon marks `GET /api/v1/instance` deprecated since 4.0 in favour of `/api/v2/instance`, and v2 reports `usage.users.active_month`, not `stats.user_count`.

**Lab — top revisions**
| Part / cell | Rule | Now | Proposed |
|---|---|---|---|
| Whole lab | Parts, setup step per part, checkpoints | One 85-minute session, 7 steps, 118 typed lines (~1.4 a minute), 2 given cells, no checkpoints, "Run All Above" on Friday | Two parts: Wednesday, Steps 1–3 (HN, matrix, refusals); Friday, Steps 4–6 (dead endpoints, Wayback, Mastodon). Each part opens with a given setup cell. Checkpoints `labs/week-03/data/access.csv` and `servers.csv`. Aim for about 55 and 40 typed lines. |
| Step 1, cell 5 | One minimal call; no typed loop that sends requests; no tuple unpacking; no `!r` | 7-line `for name, url in FRONT_PAGES.items()` loop with `!r` | HN item 1 by hand (above), then Reddit by hand: `response`, then `print(status, headers["content-type"], text[:80])`. Drop the dict and the loop. |
| Step 1 µsprint, cell 7 | One step a line | `requests.get(...).json()` chained twice; 107-character line | `response` / `ids = response.json()` / `len(ids)`; the change students type is the id (`ids[0]` instead of `1`). |
| Step 2, cell 11 | By hand, then given; 1–4 lines | 11-line typed loop that builds a 5-key dict with `.get("content-type", "").split(";")[0]` | Typed: the Wikipedia/X calls above. Given: the loop over `TARGETS` that makes `access`. Checkpoint `access.csv`, dated. |
| Step 3 µsprint, cell 18 | No typed request loop; no format spec | 7 lines, 8 requests, `{name:<12}` | Typed: Wikipedia with no headers, then with `HEADERS` (2 lines). Given: the loop over the four sites. |
| Step 4, cells 22, 24 | A `try` only where the failure is the point, in a given cell; a given cell is ≤15 lines | 9-line typed `try`/`except` loop; 26-line typed timeline plot as a microsprint | Typed: Pushshift by hand. Given: the `try` loop, and the step text says why it has one. Timeline: a given cell; the microsprint types one line, `EVENTS.append(...)` with an event of the student's own, and reruns it. |
| Step 5, cells 27, 29 | Look before you read; no typed loop | Two typed loops that index `["closest"]` without printing the answer | The crowdtangle/2020 call by hand, then `example.com`. Given: the loop over the four dates. |
| Step 6, cells 32–33 | By hand, then given; check against the provider's docs | 11-line typed loop of 12 requests with `.json()["stats"]["user_count"]`; 11-line typed plot | The mastodon.social calls by hand. Given: the loop and the plot. Checkpoint `servers.csv`. Recheck `v1/instance` against v2. Split step texts (now 100–146 words) to ≤80. |

**Deck — top revisions**
| Frame | Rule | Now | Proposed |
|---|---|---|---|
| Wednesday section (new frames) | One frame per lab cell; the first day's first frame names the lab and its key | No frame names `lab-03.ipynb`; the section is concept frames plus the Recommended Exercises list | Add "Today: Lab 03, Step 1" (where the lab and key are). Then about 12 code frames in the lab's order: HN item 1 → Reddit → Wikipedia probe → X 401 → `VERDICTS.get` → Pushshift → Wayback 2020 → `example.com` empty → Mastodon instance → timeline 422. Each one 0.37 narration / 0.6 code, ≤8 lines, ending on a "what do you expect?" question. |
| "Claims you can check — the access matrix" | One listing of ≤8 lines; ≤58 characters; ≤2 chains; narration left 0.37 / code right 0.6; same behaviour as the lab | `probe()`: 10 lines, 7 over 58 characters (up to 79), `try`/`except`, `timeout=20`, nested conditional expression; no columns; ~24 words | With sign-off: park it (`%`) and let the lab frames above carry the matrix. Or split it into "one request by hand" and "the notebook loops this over eight". |
| "Popular web data sources", "Three ways web data dies" | No figures from a key's run in narration; ask what to look for | The narration states each result (Reddit 403 `text/html`, X `401 application/problem+json`, Pushshift 403, error 215) | With sign-off: move them after the lab frames as a debrief, or turn each into a question ("What content type did Reddit send?"). |
| "Three ways web data dies", "A guided audit" | No gray blocks | Gray `block` ("HTTP errors", "Submitting") | Bold lead-in plus a line. |
| "Step 5 — review basics" (Friday) | Never code left | A GitHub `suggestion` listing in the left 0.6 column | Low priority (not Python): swap to 0.37 narration left, listing right. |

**Mechanical counts:**
- Deck: 40 frames; 2 listings (1 Python); 0 frames with two listings; 1 code-left frame (the suggestion block); 1 listing over 8 lines (`probe`, 10); 7 lines over 58 characters; 0 output comments; 3 gray blocks.
- Lab: 17 code cells (2 given); 118 typed lines; median typed cell 7 lines; 13 typed cells over 4 lines (8 over 6); 9 cells with lines over 90 characters; 7 typed request loops; 3 tuple-unpacking `for` loops; 5 cells with format specs or `!r`; 1 typed `try`; 6 step texts over 80 words; 0 checkpoints.

**Effort:** L for the lab: almost every typed cell becomes by-hand plus given, it needs 2 checkpoints and a fresh live run, and it needs mistype checks against ~10 hosts. M for the deck: about 12 new frames, plus sign-off on the 3 instructor frames.

## Week 02 — Ethics, law & responsible collection (User-Agent, robots.txt, pacing)

**Distance from the rules:** The lab teaches the right ideas, but students type nearly all of the code: 2 function definitions (one with a dict comprehension), 4 loops that send requests, a conditional expression, a list comprehension, and a 9-line dict of prose. Its first `robots.txt` is the Times's full file, not a small one students can predict. The deck's Wednesday code frames come from the companion notebook. Four put code in the left column. `responsible_get()` is a 15-line `try`/`raise_for_status`/`timeout` function that the lab's style rules forbid.

**Priority:** P1. The deck is the cheap win (4 code-left frames, a 15-line listing, output comments). The lab needs a rebuild, but its steps can be kept as they are.

**Minimal first calls to add:**
- **httpbin (Step 1):** `requests.get("https://httpbin.org/user-agent")` with no headers, then `print(response.text)`. Students see `{"user-agent": "python-requests/2.x"}`. Then the same call with `headers=HEADERS`, which echoes their own string. Each cell is one or two lines. The bare Wikipedia request and its 403 come after.
- **RobotFileParser (new, before Step 2's NYT file):** `rules = ["User-agent: *", "Disallow: /private/", "", "User-agent: GPTBot", "Disallow: /"]`, then `rp = RobotFileParser()` and `rp.parse(rules)`. Then three typed `can_fetch` calls, each predicted before it runs:
  - `can_fetch("*", "https://example.com/private/notes")` gives `False`;
  - `can_fetch("*", "https://example.com/about")` gives `True`;
  - `can_fetch("GPTBot", "https://example.com/about")` gives `False`.

  Verified locally. Optional second call, for Step 3's precedence point: `["User-agent: *", "Disallow: /svc", "Allow: /svc/wordle"]`. It gives `True` for `/svc/wordle` on Python 3.14.5+ and `False` before, the change the key relies on.
- **Pacing (Step 6):** `start = time.time()`, then `time.sleep(2)`, then `print(time.time() - start)`. Students predict about 2.0. Then one timed request to `https://example.com/`, before any loop of five.

**Lab — top revisions**
| Part / cell | Rule | Now | Proposed |
|---|---|---|---|
| Whole lab | Parts, setup steps, checkpoints | One 85-minute session, 10 steps, 115 typed lines, 1 given cell, no checkpoints | Part 1, Wednesday: Steps 0–4 (User-Agent, robots.txt, parser, the `read()` trap). Part 2, Friday: Steps 5–9 (AI crawlers, pacing, polite loop, five questions). Checkpoints: a dated copy of `nytimes_robots.txt` (it also pins the line numbers 70/75 that the Discuss boxes and answers cite) and `allowed.csv`. |
| Step 0, cell 2 | 1–4 typed lines | 9 lines (6 imports) plus a `sys.version.split()[0]` chain | Given: imports and version. Typed: `HEADERS`, email only. |
| Step 1, cell 5 | Minimal call; one step a line | 3 requests in one cell, `.json()` chained, then indexed | The httpbin calls above, one per cell, printing `.text`, then the bare Wikipedia request. |
| Steps 2–3, cells 8, 9, 12 | Minimal call first; no typed loops or comprehensions | Typed `for`/`if` over the NYT lines, `split(":", 1)[1].strip()`, a dict-of-dicts loop over `PAGES` | The hand-typed rules above first. Then typed: `lines = response.text.splitlines()`, `len(lines)`, `lines[:15]`, and one `rp.can_fetch("GPTBot", "https://www.nytimes.com/")`. Given: the agents count and the `PAGES` table. |
| Step 3 µsprint, cell 14 | One or two typed lines | 6-line `range`/`lines.index`/`startswith` loop | Given: the cell that finds the matching rules. Typed change: another path (`"/svc/crosswords"`). |
| Step 5, cells 22, 23, 25 | No typed `def`, comprehension, or request loop | `crawler_check()` with a dict comprehension; a loop over `NEWS`; a list comprehension in the microsprint | One newsroom by hand (fetch, parse, one `can_fetch`; 3 cells). Given: `crawler_check` and the loop, which makes `allowed` (checkpoint). Microsprint: `crawler_check("www.reddit.com")` and print it. |
| Steps 6–7, cells 28, 29, 32, 35 | No conditional expression, typed `def`/loop, or format spec | `wait = delay if delay is not None else 1.0`; two typed 5-request loops; typed `timed_requests()`; `{wait:.0f}` | The `time.sleep(2)` call, then one timed request, by hand. Given: `timed_requests()`, both runs, and the plot. Print `rp.crawl_delay("*")`, and let a Discuss box ask what `None` means. |
| Steps 8–9, cells 38, 43 | No typed request loop; no tuple unpacking | 10-line typed `if`/`else` request loop; 9 typed lines of prose in a dict, printed with `.items()` | One URL by hand (`can_fetch`, then the request). Given: the polite loop. Step 9 becomes a comment-answer cell (`placeholder: ""`), like its microsprint. |

**Deck — top revisions**
| Frame | Rule | Now | Proposed |
|---|---|---|---|
| "Then: launch Jupyter and open the notebook" | One listing per frame; never code left | 2 listings (bash and Python) in the left 0.6 column; bash lines of 73–86 characters with step comments; opens `ch-02-ethics.ipynb` | Two frames, narration 0.37 / code 0.6, one listing each. Open `lab-02.ipynb` (and say where the key is). |
| "robots.txt: read it before you scrape" | ≤8 lines; ≤58 characters; no printed output; minimal call first | 10 lines, 5 over 58 (up to 89); `# True` / `# False` output comments; Wikipedia's whole file first | Three frames: the 5-line hand-typed rules with "What will each print?"; then fetch the Times's file (the lab's case), one argument per line; then `can_fetch`, one call per line, no outputs. |
| "The problem with rp.read()" | Never code left | Standard-library excerpt in the left 0.6 column | Swap: narration 0.37 left, excerpt 0.6 right; the alert text goes into the narration. |
| "What robots.txt reveals across platforms" | ≤2 chained methods; little Python; matches the lab | `.get(...).text.strip().split("\n")` (3 chained); `for name, url in sites.items()`; `sum(... for l in lines)`; 6 lines over 58; code left | Replace with the lab's Step 5: one GPTBot check by hand (3 lines, code right), then "the notebook loops this over six newsrooms". |
| "Identify yourself, then slow down" | Code right; ≤58 characters; runnable | Code left; `urls` undefined; 2 lines of 73–77 characters | Replace with the lab's pacing frames: `time.sleep(2)` timed, then one timed request. The `HEADERS` dict has one entry per line, in the lab's form. |
| "responsible_get(): build it once" | ≤8 lines; the lab's style | 15 lines, 6 over 58, `try`/`raise_for_status`/`timeout=30`, no columns | With sign-off: park it (`%`) or move it to a later chapter's deck. If kept, two frames of ≤8 lines, labelled "what the chapter does", narration left. |
| "Design choices…", "Lab: work these…" and 5 others | No gray blocks | 7 gray blocks | Bold lead-ins. |
| "First: get this week's notebook" | The first day's frame names the lab | Points at the textbook's `ch-02-ethics.ipynb` | Point at `labs/week-02/lab-02.ipynb` and the key. Then one frame per typed lab cell (~10 frames). |

**Mechanical counts:**
- Deck: 39 frames (1 parked); 8 listings (7 live); 1 frame with 2 listings; 4 code-left frames; 2 listings over 8 lines (10, 15); 22 lines over 58 characters; 3 output comments; 7 gray blocks.
- Lab: 22 code cells (1 given); 115 typed lines; median typed cell 6 lines; 14 typed cells over 4 lines (7 over 6); 2 typed `def`s; 4 typed request loops; 2 comprehensions; 1 conditional expression; 1 tuple-unpacking `for`; 4 cells with format specs; 5 step texts over 80 words; 0 checkpoints.

**Effort:** L for the lab: every step after Step 1 is reshaped into by-hand plus given, it needs 2 checkpoints, and its live run needs Python 3.14.5+ (the NYT now answers 403s via DataDome). M for the deck: about 10 new frames, plus sign-off to swap or park 5 instructor frames.

## Week 01 — Introduction & setup (first request, pageviews API)

**Distance from the rules:** This lab is closest of the three. Step 1 is already a single request that students can predict. But the first API call (Step 3) jumps straight to a 31-day window in a 12-line cell. Step 0 is a 12-line cell. Step 7 has students type a function definition, and its microsprint a loop that sends requests. The deck has no code listings; that is fine for a Friday-only orientation. Its setup check lives in `handouts/week-01/setup.md`, whose second cell requests a month and chains `.json()` straight into `["items"]`.

**Priority:** P2. Students meet `requests` here, so the fixes are cheap and visible: a one-day call, cell splits, and the function made given. The calendar question (below) has to be settled first.

**Minimal first calls to add:**
- **Web page (Step 1, keep it, add a look):** after `response = requests.get(url, headers=headers)`, add `print(response.status_code)` and `print(response.text[:200])`. Students predict `200` and see `<!DOCTYPE html>…`, not the article's text yet. `len(response.text)` isn't predictable, so it moves to after this.
- **Pageviews API (Step 3, before the month):** `url = f"{api_url}/en.wikipedia/all-access/all-agents/{article}/daily/20260101/20260101"`, then `print(response.status_code, response.text)`. Students predict exactly one item, timestamp `2026010100`. On 2026-11-16 it was `{"items":[{…,"timestamp":"2026010100",…,"views":657}]}`, a body short enough to read in full. Then `data = response.json()`, `len(data["items"])` (which gives 1), and `data["items"][0]["views"]`. Only then the 31-day window.
- **Setup handout (`handouts/week-01/setup.md`, second check cell):** the same one-day request, with `print(response.text)` before `pd.DataFrame(...)`. Its window is 2024, the lab's is 2026; pick one in `docs/course-facts.md` if it is listed there.

**Lab — top revisions**
| Part / cell | Rule | Now | Proposed |
|---|---|---|---|
| Whole lab | The week's form | An 85-minute Wednesday+Friday lab, but fall 2026's week 1 met **Friday only** (the term started on a Thursday); "Run All Above" on Friday; no checkpoints | The instructor decides the next offering's calendar. Proposal: one ~50-minute part (Steps 0–5: setup, first request, one-day call, month, DataFrame, plot), and Steps 6–9 as Part 2 or as optional reading. If it stays two days, Part 2 opens with a setup cell and loads a checkpoint `jan2026.csv`. |
| Step 0, cell 2 | 1–4 typed lines | 12 lines: print, 4 imports, versions, headers | Typed: `print("Hello, web data science!")`. Given: imports and versions. Typed: `headers`, email only. |
| Step 1, cell 5 | Look before you read | Prints status, `type(response)`, `len(response.text)` | Status, then `text[:200]`, as above. `type()` moves to Step 2. |
| Step 2, cell 10 | One thing per cell; ≤4 lines | 9 lines: a tour of the response plus a second request (`http://` redirect) | Two cells: the tour (3 lines), then the redirect (2 lines). |
| Step 2 µsprint, cell 12 | No comprehension | `[name for name in dir(response) if not name.startswith("_")]` | `print(dir(response))` (1 line). Students skip the `_` names by eye. |
| Step 3, cell 15 | One minimal call; ≤4 lines | 12-line typed cell; the first API call is 31 days; only Content-Type is printed before `.json()` | The one-day call (above) in 3 small cells, then the month in 3 more (`url`, `response`, `data.keys()` / `len`). |
| Step 7, cell 31 | No typed `def`; one step a line | Typed `get_daily_views()` with `response.json()["items"]` chained | Given: the function. Typed: one call for 2025, and `len(year)`. |
| Step 8, cells 34, 36 | ≤2 chains in typed cells; no typed request loop | `year.set_index("date")["views"].resample("W").sum()`; typed 3-university loop with `resample("ME")` and a dict | Typed: `views = year.set_index("date")["views"]`, then `weekly = views.resample("W").sum()`. Given: the loop and the plot. The microsprint's typed change is a fourth university name. |

**Deck — top revisions**
| Frame | Rule | Now | Proposed |
|---|---|---|---|
| "The weekly rhythm"; Key takeaways #2 | Matches the course's form | "Monday concept, Wednesday notebook lab, Friday textbook revisions" | Update to the next offering's rhythm (live-coding parts; what's submitted is the companion notebook's Recommended Exercises). |
| "This week at a glance" | Names the lab | No lab named | If Lab 01 runs in week 1, add a bold lead-in: "Lab 01: your first request". |
| "Before Monday" | Correct path; minimal first call | Says `handouts/setup.md` (the file is `handouts/week-01/setup.md`); describes a "two-cell check" that requests a month | Fix the path. The check's second cell becomes the one-day call (handout edit). |
| (optional new) after "Common sequence across topics" | 0.37 / 0.6 layout, ≤8 lines | No code (setup moved to the handout on purpose) | Only if the lab runs that Friday: two frames, the 3-line first request and the one-day pageviews call, each ending on "What do you expect?". |
| "Our textbook", "No exams", and others | No gray blocks | 14 gray blocks | Bold lead-ins. This is the deck's main mechanical debt. |

**Mechanical counts:**
- Deck: 26 frames; 0 listings; 0 code-left frames; 0 lines over 58 characters; 14 gray blocks.
- Lab: 17 code cells (0 given); 91 typed lines; median typed cell 6 lines; 11 typed cells over 4 lines (6 over 6); 4 cells with lines over 90 characters; 1 typed `def`; 1 typed request loop; 1 comprehension; 6 step texts over 80 words; 0 checkpoints.

**Effort:** M for the lab: mostly cell splits and one `def` made given, and the calendar decision decides whether it is one part or two. S for the deck: the rhythm and path fixes plus removing the gray blocks; two optional code frames.

