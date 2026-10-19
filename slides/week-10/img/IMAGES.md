# Images for `week-10`

Every image is real, and every one is a copy from chapter 10 of the textbook,
made with its `tools/shots` (the table at the end). Text in a real image should reach 16 pixels on a slide shown
1,920 pixels wide (`slides/common/AUTHORING.md`), at the width its frame shows
it: the screenshots are shown 58% of the text width or wider (50% for the
`jsonfm` page, whose JSON is 20 pixels), and the charts at 56% or wider.

<!-- stubs:begin: generated from stubs.tsv by slides/common/make_stubs.py; edits between these markers are replaced -->
| File | Size | Should show |
|---|---|---|
<!-- stubs:end -->

## Removed

Five gray placeholders were deleted with their `stubs.tsv` rows on
2026-10-16, when the deck moved to chapter 10's new case study (University of
Colorado Boulder, in place of Elizabeth II): `api_vs_scraping.png` and
`api_call_anatomy.png` (diagrams; the frames now show real pages),
`elizabeth_edits_spike.png` and `edits_vs_views.png` (charts of the old case;
the chapter's own charts replace them), and `mediawiki_api_sandbox.png` (the
sandbox's forms load through the API, which rate-limited every take; the frame
shows the API's `jsonfm` page instead).

`pr_suggestion.png`, a copy of week 8's review-suggestion screenshot, was
deleted on 2026-10-19 with the Friday revision-workshop frame that showed it:
Friday is now a notebook lab and Final Project Q&A, with no GitHub
submissions this week.

`pr_review.png`, a gray placeholder for a GitHub "Files changed" view, was
deleted with its `stubs.tsv` row on 2026-10-16. Weeks 7, 8, and 9 dropped
theirs the same way, for `pr_suggestion.png`.

## Copied by tools/shots

<!-- shots:begin: copies from the textbook's tools/shots, generated from shots.json; edits between these markers are replaced -->
Copied here by the textbook's `tools/shots/run sync`; `tools/shots/run synced` checks them.

| File | Copy of | Captured | Source | How |
|---|---|---|---|---|
| `api-response.png` and `api-response_annotated.png` and `api-response_annotated.pdf` | `ch-10/api-response` (images/ch-10/api-response.png, textbook `9a22395`) | 2026-10-16 | https://en.wikipedia.org/w/api.php?action=query&titles=University_of_Colorado_Boulder&prop=info&format=jsonfm | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×600 at 2× |
| `article-categories.png` and `article-categories_annotated.png` and `article-categories_annotated.pdf` | `ch-10/article-categories` (images/ch-10/article-categories.png, textbook `9a22395`) | 2026-10-16 | https://en.wikipedia.org/wiki/University_of_Colorado_Boulder | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×700 at 2× |
| `article-references.png` and `article-references_annotated.png` and `article-references_annotated.pdf` | `ch-10/article-references` (images/ch-10/article-references.png, textbook `9a22395`) | 2026-10-16 | https://en.wikipedia.org/wiki/University_of_Colorado_Boulder | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×700 at 2× |
| `article-tabs.png` and `article-tabs_annotated.png` and `article-tabs_annotated.pdf` | `ch-10/article-tabs` (images/ch-10/article-tabs.png, textbook `9a22395`) | 2026-10-19 | https://en.wikipedia.org/wiki/University_of_Colorado_Boulder | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×860 at 2× |
| `cu-boulder-combined.png` | `ch-10/cu-boulder-combined` (images/ch-10/cu-boulder-combined.png, textbook `9a22395`) | 2026-10-16 | https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Boulder%2C_Colorado/daily/20210101/20260930 | Claude Code: rendered with matplotlib 3.11.2 with requests 2.34.2; imported by tools/shots |
| `cu-daily-views.png` | `ch-10/cu-daily-views` (images/ch-10/cu-daily-views.png, textbook `9a22395`) | 2026-10-16 | https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/University_of_Colorado_Boulder/daily/20210101/20260930 | Claude Code: rendered with matplotlib 3.11.2 with requests 2.34.2; imported by tools/shots |
| `cu-monthly-edits.png` | `ch-10/cu-monthly-edits` (images/ch-10/cu-monthly-edits.png, textbook `9a22395`) | 2026-10-16 | https://en.wikipedia.org/w/api.php?action=query&titles=University_of_Colorado_Boulder&prop=revisions&rvlimit=max&rvstart=2026-09-30T23:59:59Z | Claude Code: rendered with matplotlib 3.11.2 with requests 2.34.2; imported by tools/shots |
| `cu-views-by-agent.png` | `ch-10/cu-views-by-agent` (images/ch-10/cu-views-by-agent.png, textbook `9a22395`) | 2026-10-16 | https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/University_of_Colorado_Boulder/monthly/20240101/20260930 | Claude Code: rendered with matplotlib 3.11.2 with requests 2.34.2; imported by tools/shots |
| `languages-menu.png` and `languages-menu_annotated.png` and `languages-menu_annotated.pdf` | `ch-10/languages-menu` (images/ch-10/languages-menu.png, textbook `9a22395`) | 2026-10-16 | https://en.wikipedia.org/wiki/University_of_Colorado_Boulder | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×860 at 2× |
| `pageviews-tool.png` and `pageviews-tool_annotated.png` and `pageviews-tool_annotated.pdf` | `ch-10/pageviews-tool` (images/ch-10/pageviews-tool.png, textbook `9a22395`) | 2026-10-16 | https://pageviews.wmcloud.org/pageviews/?project=en.wikipedia.org&platform=all-access&agent=user&redirects=0&start=2026-07-01&end=2026-09-30&pages=University_of_Colorado_Boulder | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×700 at 2× |
| `revision-history.png` and `revision-history_annotated.png` and `revision-history_annotated.pdf` | `ch-10/revision-history` (images/ch-10/revision-history.png, textbook `9a22395`) | 2026-10-16 | https://en.wikipedia.org/w/index.php?title=University_of_Colorado_Boulder&action=history | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×760 at 2× |
| `talk-page.png` and `talk-page_annotated.png` and `talk-page_annotated.pdf` | `ch-10/talk-page` (images/ch-10/talk-page.png, textbook `9a22395`) | 2026-10-16 | https://en.wikipedia.org/wiki/Talk:University_of_Colorado_Boulder | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×1100 at 2× |
| `user-contributions.png` and `user-contributions_annotated.png` and `user-contributions_annotated.pdf` | `ch-10/user-contributions` (images/ch-10/user-contributions.png, textbook `9a22395`) | 2026-10-16 | https://en.wikipedia.org/wiki/Special:Contributions/Jimbo_Wales | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×760 at 2× |
| `what-links-here.png` and `what-links-here_annotated.png` and `what-links-here_annotated.pdf` | `ch-10/what-links-here` (images/ch-10/what-links-here.png, textbook `9a22395`) | 2026-10-16 | https://en.wikipedia.org/wiki/Special:WhatLinksHere/University_of_Colorado_Boulder | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×1000 at 2× |
<!-- shots:end -->
