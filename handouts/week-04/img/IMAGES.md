# Images for the week-04 RSS handout

The two figures in `rss-feeds.md` are copies of figures from the textbook's
chapter 4, captured on 2026-09-24 by `tools/shots` in the textbook repo
(recipes in `tools/shots/recipes/ch-04.yml`, provenance in
`images/ch-04/provenance.json` there, and notes on retaking them in
`images/ch-04/IMAGES.md`). To refresh one, retake and promote it in the
textbook, then copy its `_annotated.png` here. The numbered markers are drawn
by the toolkit, not painted into the screenshots.

| File | Shows | Book figure |
|---|---|---|
| `rss-feed-xml_annotated.png` | BBC News's science and environment feed in Chrome's XML tree: `<rss>` (1), `<channel>` (2), and the first and second `<item>` (3), with the channel's `<image>` and `<copyright>` folded | Figure 4.3 |
| `view-source-rss-link_annotated.png` | View Source of PBS NewsHour's home page, searched with Chrome's find bar for `application/rss+xml`; line 33's `<link rel="alternate">` and its `href` (1) | Figure 4.2 |

Both show things that change: the feed's headlines change through the day,
and PBS's page source changes with each release of its site.

## Copied by tools/shots

<!-- shots:begin: copies from the textbook's tools/shots, generated from shots.json; edits between these markers are replaced -->
Copied here by the textbook's `tools/shots/run sync`; `tools/shots/run synced` checks them.

| File | Copy of | Captured | Source | How |
|---|---|---|---|---|
| `rss-feed-xml_annotated.png` | `ch-04/rss-feed-xml` (images/ch-04/rss-feed-xml_annotated.png, textbook `5e89cea`) | 2026-09-24 | https://feeds.bbci.co.uk/news/science_and_environment/rss.xml | tools/shots: Google Chrome for Testing 154.0.8037.57, 800×700 at 2× |
| `view-source-rss-link_annotated.png` | `ch-04/view-source-rss-link` (images/ch-04/view-source-rss-link_annotated.png, textbook `5e89cea`) | 2026-09-24 | view-source:https://www.pbs.org/newshour/ | tools/shots: Google Chrome for Testing 154.0.8037.57, 816×600 at 2× |
<!-- shots:end -->
