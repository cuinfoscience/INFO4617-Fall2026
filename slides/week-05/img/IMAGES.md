# Images for `week-05`

Five of the six images are **real, script-generated assets** as of the Ch.~5
slide restructure: `protocol_stack.png`, `url_anatomy.png`,
`request_lifecycle.png`, and `tcp_handshake.png` are diagrams drawn by
`generate_images.py`; `pageviews_timeseries.png` is a live chart pulled from
the Wikimedia pageviews API, using the exact same call and date range
(`University_of_Colorado_Boulder`, `20260101`-`20260131`) shown in the
Wednesday "Make an API call, get a time series" slide, so the chart matches
what students actually see if they run that cell themselves.

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

## Handout screenshots (`handout_*.png`)

Four real GitHub screenshots for `handouts/common/pull-request-walkthrough.md`,
captured by the instructor from an actual write-access session -- not scripted
or regenerable, so recapture manually if GitHub's UI changes enough to make
these stale:

- `handout_edit_this_page.png` -- the live chapter page's sidebar, showing
  **Edit this page** / **Report an issue**.
- `handout_editor_search.png` -- GitHub's in-editor search bar, open and
  searching for the target line.
- `handout_preview_diff.png` -- the diff view after the edit, old line in red
  and new line in green.
- `handout_commit_branch_choice.png` -- the commit panel, showing both save
  options.

`handout_commit_branch_choice.png` had one field redacted before use: the
"Commit Email" dropdown showed the instructor's real address, which has no
pedagogical value in the handout and shouldn't be published to a public repo.
Redacted with:

```python
from PIL import Image, ImageDraw
im = Image.open("4.png").convert("RGB")
draw = ImageDraw.Draw(im)
draw.rectangle([20, 968, 520, 1058], fill=(30, 33, 40))
draw.rectangle([20, 968, 520, 1058], outline=(70, 74, 84), width=2)
```

All four were then downscaled to 700px wide (LANCZOS), preserving each
image's own aspect ratio rather than force-cropping to a fixed size -- these
are dense UI screenshots and a hard crop would either cut content or blur
small text.

Note: this file documents `week-05`'s own images only. The
`handout_*.png` assets above actually live under
`handouts/common/img/` and are cross-referenced here because they were
captured in the same instructor session as the rest of this directory's
history; see that directory directly for the authoritative copies.
