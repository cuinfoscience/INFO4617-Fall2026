# Images for `week-05`

Four images are **real, script-generated assets** as of the Ch.~5 slide
restructure: `protocol_stack.png`, `url_anatomy.png`, `request_lifecycle.png`,
and `tcp_handshake.png` are diagrams drawn by `generate_images.py`;
`pageviews_timeseries.png` is a live chart pulled from the Wikimedia
pageviews API, using the exact same call and date range
(`University_of_Colorado_Boulder`, `20260101`-`20260131`) shown in the
Wednesday "Make an API call, get a time series" slide, so the chart matches
what students actually see if they run that cell themselves.

## Real, hand-sourced images

- `arpanet_map_1977.png` -- "ARPANET Logical Map, March 1977," downloaded
  from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Arpanet_logical_map,_march_1977.png)
  (public domain, US no-notice; Computer History Museum collection). Used
  on the "A brief history: ARPANET and a persistent myth" frame.
- `network-requests-inspector.png` -- a real DevTools Network-tab
  screenshot, captured and dropped in directly (via Overleaf), replacing
  the `dev_tools_network.png` placeholder this file previously described.
  `dev_tools_network.png` itself is no longer referenced by any frame but
  is left in place rather than deleted.
- `how-do-you-do.jpeg` -- a still from the "How do you do, fellow kids"
  meme, added to the User-Agent-spoofing frame. Not regenerable/scripted;
  replace by hand if it ever needs to change.

Regenerate all five with:

```bash
cd slides/week-05/img
python3 generate_images.py
```

The script lives in this directory rather than inline here (unlike
`week-04`'s single-image script) because it draws four separate diagrams
plus the live chart -- worth keeping as one reusable, re-runnable file
instead of a markdown code block. Dependencies: `matplotlib` and `requests`
(`pip install matplotlib requests` if not already present).

Re-run `pageviews_timeseries.png` before class if you want the data current
for that day; the chapter's own framing ("yours will differ, and that's
fine -- record the date") applies here too.

## From the textbook's screenshot toolkit (chapter 5)

Four figures from the textbook's chapter 5, captured on 2026-09-24 by
`tools/shots` in the textbook repo (recipes in `tools/shots/recipes/ch-05.yml`,
provenance in `images/ch-05/provenance.json` there). These are copies: to
refresh one, retake and promote it in the textbook, then copy it here. The
`_annotated.pdf` files carry the numbered markers as vector graphics.

| File | Shows | Used on | Narrowest legible width |
|---|---|---|---|
| `inspector-heading_annotated.pdf` | The article's title shaded on the page (1), its `<h1>` node selected in the Elements tree (2) | "Inspecting a page: what the Inspector shows" | `0.56\textwidth` |
| `element-picker_annotated.pdf` | The element picker switched on (1) over the infobox, and the infobox's node in the tree (2) | not yet | `0.56\textwidth` |
| `network-requests.png` | The Network tab after a first-visit reload: filter buttons, Name/Status/Type/Size/Time/Waterfall | not yet (the Network frame keeps the instructor's own capture) | `0.56\textwidth` |
| `network-headers_annotated.pdf` | The article request's headers: Client Hints (1), this course's User-Agent (2) | not yet | `0.58\textwidth` |

The narrowest legible width is where the figure's text reaches 16 pixels on a
slide shown 1920 pixels wide (`slides/common/AUTHORING.md`, "How much a
screenshot shows"). The Inspector frame shows its figure at `0.75\textwidth`.

## Still placeholders (`dev_tools_network.png`, `pr_review.png`)

Two images remain auto-generated gray **placeholders** so the deck compiles.
Both show something a script cannot honestly fabricate -- replace by hand
(keep the same filename), then rebuild:

| File | Size | Should show |
|---|---|---|
| `dev_tools_network.png` | 1300x850 | Screenshot: browser Network tab on a live Wikipedia page load, showing dozens of requests with Name/Status/Type columns and the selected request's User-Agent and Cookie response headers |
| `pr_review.png` | 1300x820 | Screenshot: a GitHub pull-request "Files changed" view with an inline review comment left on ch-05-protocols.qmd |

`dev_tools_network.png` needs an actual interactive browser session --
capturing a real DevTools panel isn't something a headless script can do
cleanly. `pr_review.png` needs a real inline review comment on a real PR;
rather than post a comment solely to manufacture a screenshot, this is left
for the instructor to capture from an actual Friday peer-review session (or
any real PR against this chapter with a genuine review comment on it).

## Handout screenshots

The four `handout_*.png` screenshots used by
`handouts/common/pull-request-walkthrough.md` live in `slides/week-04/img/`,
not here. Their notes, including the email redaction, are in that folder's
`IMAGES.md`.

## Listed in `stubs.tsv`

`make_stubs.py` keeps this table in step with `stubs.tsv` and draws a gray
placeholder for any listed image that is missing. It rewrites only what is
between the two markers; the notes above are safe.

<!-- stubs:begin: generated from stubs.tsv by slides/common/make_stubs.py; edits between these markers are replaced -->
| File | Size | Should show |
|---|---|---|
| `request_lifecycle.png` | 1000x900 | Diagram: the URL-to-rendered-page sequence -- DNS resolve, TCP connect, HTTP request, server response, browser render -- shown as a vertical waterfall across the protocol layers |
| `protocol_stack.png` | 1000x900 | Diagram: the four-layer web stack (TCP/IP transport, DNS naming, HTTP application, URL identifier) drawn as stacked bands with example values at each layer |
| `dev_tools_network.png` | 1300x850 | Screenshot: browser Network tab on a live Wikipedia page load, showing dozens of requests with Name/Status/Type columns and the selected request's User-Agent and Cookie response headers |
| `url_anatomy.png` | 1300x480 | Diagram: a Census API URL broken into labeled parts -- scheme, host, port, path, query, fragment -- with each component called out beneath the string |
| `pageviews_timeseries.png` | 1100x560 | Figure: matplotlib line chart of daily Wikipedia pageviews for University of Colorado Boulder over January 2026, with visible spikes |
| `pr_review.png` | 1300x820 | Screenshot: a GitHub pull-request "Files changed" view with an inline review comment left on ch-05-protocols.qmd |
| `tcp_handshake.png` | 1100x520 | Diagram: a client/server sequence showing TCP's three-way handshake -- SYN, SYN-ACK, ACK -- as labeled arrows before any HTTP request data is sent |
<!-- stubs:end -->
