# Friday code review: the review table

This is the review table from §3 of the
[Friday code-review plan](2026-09-24-friday-code-review.md), for the first
standup on week 7's Friday, October 2. It lists the 39 pull requests open on
the [textbook](https://github.com/cuinfoscience/Web-Data-Science-Book) on
2026-09-24, by chapter, with the textbook's `main` at 892833c. None had changed
by 2026-09-25. Pull requests keep opening and changing, so the table is rebuilt
the day before class, and week 7's Friday slides are built from that version
(plan §4).

Every `#` number here is a textbook pull request or issue, not one in this
repository.

## For the standup

- **Authors:** be ready to say, in a sentence or two, what your pull request
  fixes and where.
- **Reviewers:** read the pull requests you're assigned before class. Give a
  verdict (approve, request changes, or close) with at most two points: what
  must change, and what would be nice.

## What the columns mean

- **Checks.** The book's two checks, run on `main` with the pull request merged
  in:
  - *Render* builds the whole book.
  - *Notebook sync* regenerates the companion notebooks. It fails whenever a
    chapter changes without its notebook, which a pull request made in the
    browser can't avoid. The maintainer regenerates the notebooks after
    merging.
- **Conflicts with `main`.** "Yes" means `main` has moved under the branch.
  Catch up by merging `main` into your branch, and don't force-push.
- **Overlaps.** Another pull request, or existing text, that covers the same
  place.

## The table, by chapter

### Chapter 1 — Introduction

| PR | Author | Chapter and section | Issue it fixes | Checks (Render, Notebook sync) | Conflicts with `main`? | Overlaps with |
|---|---|---|---|---|---|---|
| [#52] | Simon0Spillane | What is Pandas? (new section) | — | not run: conflicts | **Yes**: `ch-01-introduction.qmd` | Pandas is already introduced in setup and Further Reading |

### Chapter 2 — Ethics

| PR | Author | Chapter and section | Issue it fixes | Checks (Render, Notebook sync) | Conflicts with `main`? | Overlaps with |
|---|---|---|---|---|---|---|
| [#50] | brianckeegan (maintainer) | Comparing robots.txt Across Platforms (Reddit) | mentions [#43] | Render ✓ · Sync ✗ (notebook not regenerated) | No; with [#79] once either merges | [#79]: same sentence; they conflict |
| [#54] | michaelchow38 | The Computer Fraud and Abuse Act; Additional Exercises | [#18] | Render ✓ · Sync ✗ (notebook not regenerated) | No | — |
| [#56] | saintxromain | Missing Manual Reference | [#17] | Render ✓ · Sync ✗ (notebook not regenerated) | No | [#104] adds the same link in ch-05 |
| [#59] | Jonah-Schwartz521 | Responsible Request Headers; Rate Limiting | [#15] (Closes [#15]) | Render ✓ · Sync ✗ (notebook not regenerated) | No | — |
| [#63] | Puzz27 | Comparing robots.txt Across Platforms | [#28] ("Fixing Issue [#28]") | Render ✓ · Sync ✗ (notebook not regenerated) | No | Same section as [#50] and [#79]; no conflict |
| [#79] | mhostetter235 | Comparing robots.txt Across Platforms (Reddit) | [#43] | Render ✓ · Sync ✗ (notebook not regenerated) | No; with [#50] once either merges | [#50]: same sentence; they conflict |

### Chapter 3 — The Post-API Age

| PR | Author | Chapter and section | Issue it fixes | Checks (Render, Notebook sync) | Conflicts with `main`? | Overlaps with |
|---|---|---|---|---|---|---|
| [#62] | seanpotts-gif | The generated notebook's title | — | Render ✓ · Sync ✗ (regeneration reverts the edit) | No | The notebook generator |
| [#80] | daphnnec | An Access Matrix (`probe()`) | [#60] | Render ✓ · Sync ✗ (notebook not regenerated) | No | — |
| [#95] | asheninu | Exemption (the A/B-testing sentence) | [#68] | Render ✓ · Sync ✗ (notebook not regenerated) | No | — |

### Chapter 4 — Data Formats

| PR | Author | Chapter and section | Issue it fixes | Checks (Render, Notebook sync) | Conflicts with `main`? | Overlaps with |
|---|---|---|---|---|---|---|
| [#81] | Michael-Benner | Why Data Formats Matter (adds an "XML vs. JSON" subsection) | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | "When to Use Which" already compares the formats |
| [#82] | michaelchow38 | Social History and Public Interest | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | — |
| [#86] | Puzz27 | Recommended Exercises, Step 5 | — ([#84], the blank-page report, was fixed by [#149]) | Render ✓ · Sync ✗ (notebook not regenerated) | No | — |
| [#88] | Jonah-Schwartz521 | Working with Real XML; Parsing JSON Strings; Handling Deeply Nested JSON (+ notebook) | — | not run: conflicts | **Yes**: `ch-04-data-formats.qmd`, `ch-04-data-formats.ipynb` | [#93] makes the same change |
| [#89] | fionackim | Recommended Exercises, Step 2 | — | not run: conflicts | **Yes**: `ch-04-data-formats.qmd` | — |
| [#92] | hamzaabulaila007 | Starter feeds (The Changelog row) | [#90] (Closes [#90]) | Render ✓ · Sync ✗ (notebook not regenerated) | No; with [#99] once either merges | [#99]: adjacent row; they conflict |
| [#93] | maddiedeutsch | Same three requests as [#88] | — | not run: conflicts | **Yes**: `ch-04-data-formats.qmd` | [#88] makes the same change |
| [#98] | meezie7 | Lists and Dictionaries | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | [#100]: same section; no conflict |
| [#99] | saintxromain | Starter feeds (Data Engineering Podcast row) | [#94] (closed by its author when the PR opened) | Render ✓ · Sync ✗ (notebook not regenerated) | No; with [#92] once either merges | [#92]: adjacent row; they conflict |
| [#100] | lukecarrano-eng | Lists and Dictionaries (adds a JSON-to-Python type table) | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | [#98]: same section; no conflict |
| [#101] | brmy2261 | Where you'll actually find each format | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | — |
| [#102] | Jobo2621 | Handling Deeply Nested JSON | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | — |

### Chapter 5 — Protocols

| PR | Author | Chapter and section | Issue it fixes | Checks (Render, Notebook sync) | Conflicts with `main`? | Overlaps with |
|---|---|---|---|---|---|---|
| [#104] | AnnieSchneeberger | Missing Manual Reference | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | [#56] adds the same link in ch-02 |
| [#106] | mhostetter235 | Installing and Running `scapy` (step 3) | [#105] | Render ✓ · Sync ✗ (notebook not regenerated) | No | [#112]: same list; no conflict |
| [#107] | daphnnec | Common Issues to Debug (DNS REFUSED) | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | — |
| [#108] | Michael-Benner | The generated notebook only (adds "Understanding Query Parameters") | — | Render ✓ · Sync ✗ (regeneration reverts the edit) | No | The notebook generator; related to issue [#114] |
| [#109] | haal5146-oss | User-Agent Spoofing | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | — |
| [#111] | Puzz27 | Recommended Exercises, Step 2 | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | [#112] mentions it |
| [#112] | hamzaabulaila007 | Installing and Running `scapy`; Common Issues to Debug | — (mentions [#110], [#111]) | Render ✓ · Sync ✗ (notebook not regenerated) | No | [#106]: same list; no conflict |
| [#113] | brmy2261 | Recommended Exercises, Steps 5–6 (+ notebook) | — | Render ✓ · Sync ✓ | No; with [#127] once either merges | [#127]: same Step 5 paragraph; they conflict |
| [#116] | Jonah-Schwartz521 | Diagnosing HTTP Errors (`get_with_backoff()`) | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | [#122]: same section; no conflict |
| [#118] | meezie7 | `curl` and `wget` (the `time.sleep()` paragraph) | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | — |
| [#121] | diba8530 | DNS: The Address Book; also ch-04 XML and BeautifulSoup | [#120] (closed by its author, citing [#117]) | Render ✓ · Sync ✗ (notebook not regenerated) | No | — |
| [#122] | saintxromain | Diagnosing HTTP Errors (`diagnose_request()`) | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | [#116]: same section; no conflict |
| [#126] | lukecarrano-eng | Recommended Exercises, Step 4 | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | — |
| [#127] | Jobo2621 | Recommended Exercises, Step 5 | — | Render ✓ · Sync ✗ (notebook not regenerated) | No; with [#113] once either merges | [#113]: same Step 5 paragraph; they conflict |

### Chapter 6 — Static Pages

| PR | Author | Chapter and section | Issue it fixes | Checks (Render, Notebook sync) | Conflicts with `main`? | Overlaps with |
|---|---|---|---|---|---|---|
| [#130] | daphnnec | Strategy 3: The Table That Needs Cleanup (`read_html`) | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | [#131]: same author and chapter |
| [#131] | daphnnec | Abstracting into Functions | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | [#130]; copies ch-02's `responsible_get()` |

### Chapter 11 — Government Data

| PR | Author | Chapter and section | Issue it fixes | Checks (Render, Notebook sync) | Conflicts with `main`? | Overlaps with |
|---|---|---|---|---|---|---|
| [#78] | haal5146-oss | U.S. Census Bureau API | — | Render ✓ · Sync ✗ (notebook not regenerated) | No | — |

## How it was built

- **Fetching and merging.** Each pull request's head was fetched read-only
  from `refs/pull/N/head`. It was merged with `--no-ff` onto `main` in a
  scratch worktree, as GitHub's merge ref does. No branch was changed, and
  nothing was posted to GitHub.
- **Render.** A `quarto render` of the whole book (Quarto 1.10.18, Python
  3.14). It fails on a non-zero exit or any `WARN:` line, like the textbook's
  `render.yml`. `main` alone renders cleanly.
- **Notebook sync.** `python tools/make_notebooks.py` fails if `notebooks/`
  changes, like `notebook-sync.yml`. On `main` alone, the notebooks are in
  sync.
- **Why locally.** GitHub hadn't run the checks on 23 of these pull requests.
  On pull requests from forks, it waits for a maintainer to approve each run.
- **No code ran.** Rendering runs no code: the book sets
  `execute: eval: false`, and no pull request changes that.
- **Conflicts.** Each pull request was test-merged onto `main`, and so was
  each pair that changes the same file.

[#15]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/15
[#17]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/17
[#18]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/18
[#28]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/28
[#43]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/43
[#50]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/50
[#52]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/52
[#54]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/54
[#56]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/56
[#59]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/59
[#60]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/60
[#62]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/62
[#63]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/63
[#68]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/68
[#78]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/78
[#79]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/79
[#80]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/80
[#81]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/81
[#82]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/82
[#84]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/84
[#86]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/86
[#88]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/88
[#89]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/89
[#90]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/90
[#92]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/92
[#93]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/93
[#94]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/94
[#95]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/95
[#98]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/98
[#99]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/99
[#100]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/100
[#101]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/101
[#102]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/102
[#104]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/104
[#105]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/105
[#106]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/106
[#107]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/107
[#108]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/108
[#109]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/109
[#110]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/110
[#111]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/111
[#112]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/112
[#113]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/113
[#114]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/114
[#116]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/116
[#117]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/117
[#118]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/118
[#120]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/120
[#121]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/121
[#122]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/122
[#126]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/126
[#127]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/127
[#130]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/130
[#131]: https://github.com/cuinfoscience/Web-Data-Science-Book/pull/131
[#149]: https://github.com/cuinfoscience/Web-Data-Science-Book/issues/149
