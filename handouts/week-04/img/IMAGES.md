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
