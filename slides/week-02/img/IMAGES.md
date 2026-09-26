# Images for `week-02`

The two images `stubs.tsv` lists are real: renders of live text by
`common/make_figures.py`. Four gray placeholders that no frame used,
`legal_timeline.png`, `ethics_framework.png`, `pr_review.png`, and
`github_issue.png`, were deleted with their rows on 2026-09-25; the rows'
descriptions are in the file's history. The deck's other images were added by
the instructor and aren't listed in `stubs.tsv`.

<!-- stubs:begin: generated from stubs.tsv by slides/common/make_stubs.py; edits between these markers are replaced -->
| File | Size | Should show |
|---|---|---|
| `robots_txt_browser.png` | 1200x615 | REAL ASSET -- rendered from the live file by common/make_figures.py. Wikipedia's robots.txt: header comment plus the generic User-agent block, with Disallow: /trap/ highlighted. |
| `user_agent_devtools.png` | 1200x414 | REAL ASSET -- rendered from a live response by common/make_figures.py. The course User-Agent echoed back by httpbin.org/headers, i.e. what the server actually receives. |
<!-- stubs:end -->

`make_stubs.py` keeps the table above in step with `stubs.tsv`. It rewrites
only what is between the two markers; the notes below are safe.

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

