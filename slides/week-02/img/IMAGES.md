# Image placeholders for `week-02`

These are auto-generated gray **placeholders** so the deck compiles. Replace each with the real asset described below (keep the same filename), then rebuild.

| File | Size | Should show |
|---|---|---|
| `legal_timeline.png` | 1240x560 | Diagram: timeline of CFAA scraping cases -- Van Buren v. United States (2021, gates-up-or-down), hiQ Labs v. LinkedIn (2019/2022, public data but breach of contract), Sandvig v. Barr (2020, ToS violation is not a crime) |
| `ethics_framework.png` | 900x900 | Diagram: the five-question ethical decision framework as a top-to-bottom funnel/checklist -- legality, consent, proportionality, privacy, server impact |
| `robots_txt_browser.png` | 1200x615 | REAL ASSET -- rendered from the live file by common/make_figures.py. Wikipedia's robots.txt: header comment plus the generic User-agent block, with Disallow: /trap/ highlighted. |
| `user_agent_devtools.png` | 1200x414 | REAL ASSET -- rendered from a live response by common/make_figures.py. The course User-Agent echoed back by httpbin.org/headers, i.e. what the server actually receives. |
| `pr_review.png` | 1300x760 | Screenshot: a GitHub pull-request Files-changed view with an inline review comment on ch-02-ethics.qmd |
| `github_issue.png` | 1300x820 | STILL A PLACEHOLDER -- needs a manual screenshot: the GitHub 'New issue' form on Web-Data-Science-Book, filled in with the Title/Location/Problem/Why/Proposal skeleton. Requires a signed-in browser. |

## From the textbook's screenshot toolkit (chapter 2)

Two figures from the textbook's chapter 2, captured on 2026-09-24 by
`tools/shots` in the textbook repo (recipes in `tools/shots/recipes/ch-02.yml`,
provenance in `images/ch-02/provenance.json` there). They are copies, offered
beside the deck's two renders, `robots_txt_browser.png` and
`user_agent_devtools.png`, which stay: those are renders of live text, and
these are the same sources in a real browser. Placing either is the
instructor's call. To refresh one, retake and promote it in the textbook, then
copy it here. The `_annotated.pdf` carries the numbered markers as vector
graphics.

| File | Shows | For | Narrowest legible width |
|---|---|---|---|
| `robots-txt-wikipedia_annotated.pdf` | Wikipedia's robots.txt in Chrome: the comment welcoming "friendly, low-speed bots" on article pages (1), `User-agent: *` (2), its four `Allow` exceptions (3), and `Disallow` for `/w/`, `/api/`, `/trap/`, and `/wiki/Special:` (4) | the robots.txt frame, beside or instead of `robots_txt_browser.png` | `0.44\textwidth` |
| `wikimedia-ua-policy_annotated.pdf` | Wikimedia's User-Agent policy: identify your bot and give a way to contact you (1), the policy's example (2), and the format `<client name>/<version> (<contact information>)` (3) | the User-Agent frame | `0.27\textwidth` |

The narrowest legible width is where the figure's text reaches 16 pixels on a
slide shown 1920 pixels wide (`slides/common/AUTHORING.md`, "How much a
screenshot shows"). Both frames give their image `0.35\textwidth`: the policy
fits it, and the robots.txt figure needs a wider column.

