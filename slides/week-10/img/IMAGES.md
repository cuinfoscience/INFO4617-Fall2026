# Images for `week-10`

One image is real; the others are still gray placeholders, generated so the
deck compiles. Replace each placeholder with the real asset its row describes
(keep the filename), then rebuild. Text in a real image should reach 16 pixels
on a slide shown 1,920 pixels wide (`slides/common/AUTHORING.md`), at the width
its frame shows it.

<!-- stubs:begin: generated from stubs.tsv by slides/common/make_stubs.py; edits between these markers are replaced -->
| File | Size | Should show |
|---|---|---|
| `api_vs_scraping.png` | 1200x820 | Diagram: scraping (reverse-engineer messy HTML with fragile CSS selectors) beside an API (documented request -> server -> clean JSON response) |
| `api_call_anatomy.png` | 1300x520 | Diagram: an annotated MediaWiki API URL broken into base URL, action=query, the narrowing parameters, and format=json |
| `elizabeth_edits_spike.png` | 1300x620 | Chart: monthly edits to the "Elizabeth II" article over time, with a dramatic spike in September 2022 |
| `edits_vs_views.png` | 1300x640 | Dual-axis chart: monthly revisions (bars) vs monthly pageviews (line) for Elizabeth II in 2022, both spiking in September |
| `mediawiki_api_sandbox.png` | 1250x820 | Screenshot: the MediaWiki API:Main_page documentation / API sandbox showing action=query parameters and a sample JSON response |
| `pr_suggestion.png` | 763x255 | Screenshot: a review suggestion on textbook PR #228 (the instructor's demonstration), with Apply suggestion, signed in, dark theme (2026-10-06); a copy of week 8's |
<!-- stubs:end -->

## How the images were made

- `pr_suggestion.png` -- a review suggestion on textbook PR #228, the
  instructor's demonstration pull request, with **Apply suggestion**.
  (Improving Chapter 10 together)
  - A byte-for-byte copy of `slides/week-08/img/pr_suggestion.png`, itself a
    copy of `handouts/week-08/img/pr-suggestion.png`, which the instructor
    captured on 2026-10-06, signed in; its `IMAGES.md` records the capture.
    It shows the instructor's account and no student's.
  - Its code is 12 pixels, so the frame shows it in a 62% column, where the
    code comes to 16.4 pixels.

## Removed

`pr_review.png`, a gray placeholder for a GitHub "Files changed" view, was
deleted with its `stubs.tsv` row on 2026-10-16. Weeks 7, 8, and 9 dropped
theirs the same way, for `pr_suggestion.png`.
