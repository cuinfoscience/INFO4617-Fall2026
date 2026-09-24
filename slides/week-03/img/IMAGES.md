# Image placeholders for `week-03`

These are auto-generated gray **placeholders** so the deck compiles. Replace each with the real asset described below (keep the same filename), then rebuild.

<!-- stubs:begin: generated from stubs.tsv by slides/common/make_stubs.py; edits between these markers are replaced -->
| File | Size | Should show |
|---|---|---|
| `three_pressures.png` | 1200x760 | Diagram: enclosure, exemption, and erosion shown as three forces compressing open access to web data, each annotated with its mechanisms (API shutdowns & repricing; legal / ToS barriers & privacy claims; link rot & platform churn) |
| `ad_observatory.png` | 1200x800 | Screenshot: 2021 news coverage or the Meta notice disabling NYU Ad Observatory researcher accounts, justified on privacy grounds -- the exemption case |
| `link_rot.png` | 1200x760 | Figure: link rot over time -- the share of web pages that existed in 2013 but were inaccessible a decade later (Pew, ~1/3), with a 404 / Wayback Machine callout |
| `api_timeline.png` | 1300x600 | Figure: timeline of major API-access changes 2008-2026 across Twitter/X, Facebook/Meta, and Reddit, color-coded by enclosure / exemption / erosion |
| `pr_review.png` | 1300x760 | Screenshot: a GitHub pull-request "Files changed" view with an inline review comment on ch-03-post-api.qmd |
<!-- stubs:end -->

`make_stubs.py` keeps the table above in step with `stubs.tsv`. It rewrites
only what is between the two markers; the notes below are safe.

## From the textbook's screenshot toolkit (chapter 3)

Two figures from the textbook's chapter 3, captured on 2026-09-24 by
`tools/shots` in the textbook repo (recipes in `tools/shots/recipes/ch-03.yml`,
provenance in `images/ch-03/provenance.json` there). They are copies, offered
for frames that describe what they show; no frame changed, and placing either
is the instructor's call. To refresh one, retake and promote it in the
textbook, then copy it here. The `_annotated.pdf` carries its marker as
vector graphics.

| File | Shows | For | Narrowest legible width |
|---|---|---|---|
| `dead-endpoints.png` | The three retired endpoints in Chrome, one above another: Pushshift's 403, one line of JSON (`{"detail":"Not authenticated"}`); Chrome's own error page for api.crowdtangle.com, which doesn't answer, captured through a proxy, so it names a failed tunnel (`ERR_TUNNEL_CONNECTION_FAILED`); and Twitter v1.1's 400, error 215, "Bad Authentication data." Twitter's part is captured as an API client (the textbook's `docs/decisions.md`, 2026-09-24) | "Three ways web data dies", which describes all three | `0.43\textwidth` |
| `dsa-article-40_annotated.pdf` | Article 40 of the Digital Services Act, "Data access and scrutiny", on EUR-Lex, from its heading through paragraph 4, boxed (1): very large platforms and search engines must give vetted researchers access to data | "Counter-value 2 --- Oversight against exemption", or "Pushback 3 --- Turn access into a policy problem" | `0.48\textwidth` |

The narrowest legible width is where the figure's text reaches 16 pixels on a
slide shown 1920 pixels wide (`slides/common/AUTHORING.md`, "How much a
screenshot shows"). These frames' right-hand columns are `0.35\textwidth`, so
either figure needs the wider column or a frame of its own. Two more of the
back-fill plan's candidates, CrowdTangle's last capture in the Wayback Machine
and Reddit's 2023 pricing post, wait for web.archive.org; the textbook's
`docs/handoff.md` says why.
