# Images for `week-03`

`stubs.tsv` lists no images now. The five it listed, `three_pressures.png`,
`ad_observatory.png`, `link_rot.png`, `api_timeline.png`, and `pr_review.png`,
were gray placeholders that no frame used after the deck's edits of late
August. They were deleted with their rows on 2026-09-25; the rows'
descriptions are in the file's history. The deck's images were added by the
instructor (2026-08-30 to 09-01) and aren't listed in `stubs.tsv`.

<!-- stubs:begin: generated from stubs.tsv by slides/common/make_stubs.py; edits between these markers are replaced -->
| File | Size | Should show |
|---|---|---|
<!-- stubs:end -->

`make_stubs.py` keeps the table above in step with `stubs.tsv`. It rewrites
only what is between the two markers; the notes below are safe.

## From the textbook's screenshot toolkit (chapter 3)

Four figures from the textbook's chapter 3, captured on 2026-09-24 and 25 by
`tools/shots` in the textbook repo (recipes in `tools/shots/recipes/ch-03.yml`,
provenance in `images/ch-03/provenance.json` there). They are copies, offered
for frames that describe what they show; no frame changed, and placing any
is the instructor's call. To refresh one, retake and promote it in the
textbook, then copy it here. The `_annotated.pdf` carries its marker as
vector graphics.

| File | Shows | For | Narrowest legible width |
|---|---|---|---|
| `dead-endpoints.png` | The three retired endpoints in Chrome, one above another: Pushshift's 403, one line of JSON (`{"detail":"Not authenticated"}`); Chrome's own error page for api.crowdtangle.com, which doesn't answer, captured through a proxy, so it names a failed tunnel (`ERR_TUNNEL_CONNECTION_FAILED`); and Twitter v1.1's 400, error 215, "Bad Authentication data." Twitter's part is captured as an API client (the textbook's `docs/decisions.md`, 2026-09-24) | "Three ways web data dies", which describes all three | `0.43\textwidth` |
| `dsa-article-40_annotated.pdf` | Article 40 of the Digital Services Act, "Data access and scrutiny", on EUR-Lex, from its heading through paragraph 4, boxed (1): very large platforms and search engines must give vetted researchers access to data | "Counter-value 2 --- Oversight against exemption", or "Pushback 3 --- Turn access into a policy problem" | `0.48\textwidth` |
| `reddit-api-pricing.png` | u/spez's post in r/reddit, 9 June 2023, from old.reddit.com's copy in the Wayback Machine: its title and byline above its item "Premium Enterprise API / Third-party apps", $0.24 per 1K API calls from 1 July 2023, and Apollo, Reddit is Fun, and Sync closing. reddit.com's robots.txt disallows every path, so it is the archive's copy | "Pressure 1 --- Enclosure", beside the Reddit item | `0.34\textwidth` |
| `crowdtangle-last-capture.png` | CrowdTangle's last capture in the Wayback Machine, 14 August 2024, twice: under the archive's toolbar (the date, and the address's captures, 2012 to December 2024), and without it, where the page's banner reads "CrowdTangle will no longer be available after August 14, 2024" | "Three ways web data dies", beside CrowdTangle | `0.55\textwidth` |

The narrowest legible width is where the figure's text reaches 16 pixels on a
slide shown 1920 pixels wide (`slides/common/AUTHORING.md`, "How much a
screenshot shows"). These frames' right-hand columns are `0.35\textwidth`, so
Reddit's post fits one; the other three need the wider column or a frame of
their own.

## Copied by tools/shots

<!-- shots:begin: copies from the textbook's tools/shots, generated from shots.json; edits between these markers are replaced -->
Copied here by the textbook's `tools/shots/run sync`; `tools/shots/run synced` checks them.

| File | Copy of | Captured | Source | How |
|---|---|---|---|---|
| `crowdtangle-last-capture.png` | `ch-03/crowdtangle-last-capture` (images/ch-03/crowdtangle-last-capture.png, textbook `57dda60`) | 2026-09-25 |  | tools/shots: Google Chrome for Testing 154.0.8037.57, 776×600 at 2× |
| `dead-endpoints.png` | `ch-03/dead-endpoints` (images/ch-03/dead-endpoints.png, textbook `dd0ff37`) | 2026-09-24 |  | tools/shots: Google Chrome for Testing 154.0.8037.57, 560×400 at 2× |
| `reddit-api-pricing.png` | `ch-03/reddit-api-pricing` (images/ch-03/reddit-api-pricing.png, textbook `57dda60`) | 2026-09-25 |  | tools/shots: Google Chrome for Testing 154.0.8037.57, 776×600 at 2× |
<!-- shots:end -->
