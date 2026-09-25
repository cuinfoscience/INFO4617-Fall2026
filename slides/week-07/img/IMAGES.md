# Images for `week-07`

15 of this deck's 21 images are **real screenshots of the live Wayback
Machine**. Twelve were remade on 2026-09-25 so that their text reaches 16
pixels on a slide shown 1,920 pixels wide (`slides/common/AUTHORING.md`); the
2026-09-22 crops they replace showed it at 6 to 15. Three small crops from
2026-09-22 already reached it and were kept. Four are **memes the instructor
picked**, and two (Wednesday's `cdx_response.png`, Friday's `pr_review.png`)
are older gray placeholders.

## How the screenshots were made

**Remade 2026-09-25.** Eleven come from the recipes named `week07-*` in the
textbook's `tools/shots/recipes/course.yml`, captured with its `tools/shots`.
Each recipe crops to what its frame discusses and names the width the frame
shows it at, and the capture reports the text's size on the slide.
`about_capture.png` is a copy of the textbook's chapter 7 figure
`images/ch-07/about-this-capture.png`. Every request sent the User-Agent
`Web Data Science/v1 brian.keegan@colorado.edu`, page loads were 8--30
seconds apart, and the Archive's 502s were retried 30, 60, and 120 seconds
apart. `devtools_archived.png` and `wrapped_vs_raw.png` are real Chrome
windows (DevTools, View Source) on a virtual display. To retake one, run
`tools/shots/run capture course --only week07-...` in the textbook repo and
copy the take here under the deck's file name; the recipe's comments say why
it is cropped as it is.

**Kept from 2026-09-22.** `wayback_trillion.png`, `address_bar.png`, and
`wayback_down.png` were cut with Pillow from 1,280-pixel screenshots taken by
a hand-run Playwright script, with an identifying User-Agent and 8--30
second pauses. Their few words already reach 19 to 28 pixels on the slide.
`wayback_down.png` is the Archive's own error page and can't be retaken on
demand.

Live numbers in these images (capture counts, the calendar's dots) drift
daily. The remade ones are correct as of 2026-09-25, and the frames quote
them.

## Real screenshots

Sizes on the slide are the text's, where the frame shows the image.

- `wayback_trillion.png` (kept) -- the Wayback search header: "Explore more
  than 1 trillion web pages saved over time." (Web archiving)
- `wayback_calendar.png` -- the Calendar tab for `facebook.com`
  (`web.archive.org/web/2005*/facebook.com`): the bars of captures per year,
  2005 selected, and January to March 2005, where dots of different sizes
  mark the days with captures. At 0.72 of the text width, 17.2 pixels.
  (Finding a capture)
- `calendar_dots_2005.png` -- April and August 2005 from the same calendar,
  stacked and labeled: blue on April 6 and 8, orange (HTTP 403) from April
  10 to August 4, and blue from August 6, when the domain starts serving
  Thefacebook's homepage. The CDX API gives the same boundaries: 200 until
  2005-04-08 (still AboutFace's page, by the raw capture's `<title>`), 403
  from 2005-04-10, 200 from 2005-08-06; the raw 2005-08-13 capture's
  `<title>` is "Thefacebook | Welcome to Thefacebook!". 24.1 pixels. (Reading
  the dots)
- `toolbar.png` -- the Wayback toolbar on facebook.com's 2004-01-21 capture,
  from the address box to the date: 8,516,746 captures, the strip of bars
  across the years, and the big yellow date between its arrows. The strip of
  bars appears only in a window at least 1,100 pixels wide, so this is a
  1,040-pixel strip at the slide's full width. The count and the date read
  at 19 pixels and more; the date range under the count, 9 pixels in the
  toolbar at any width, comes to 14.5. (Moving through time)
- `address_bar.png` (kept) -- the browser address bar on
  `web.archive.org/web/20040212031928/http://www.thefacebook.com/`. (The URL
  is the query)
- `about_capture.png` -- the toolbar and About this capture on the
  2004-02-12 thefacebook.com capture, both sections open. Collected by:
  organization Alexa Crawls, collection `alexa_dv` (the panel loads this
  section on hover, a few seconds after Timestamps). Timestamps:
  `images/logo-right.jpg` "+1 year 3 months", `images/logo-left.jpg` "+3
  months 20 days". At 0.96 of the text width, 24 pixels. (About this capture)
- `x_com_1999.png` -- the top of x.com's 1999-11-14 page, below the toolbar,
  with every visible image broken: the big image, the four navigation images
  shown as their alt text (About X.com, Managment Team, Employment
  Opportunities, Contact Us), and the logo's. The CDX API shows why: of the
  seven images the page references, six have never been captured
  successfully -- their first captures, from August and September 2000, are
  all 404s, and later ones redirects -- and the seventh, a transparent
  `spacer.gif`, was saved on April 29 and May 5, 2000. The full query is the
  textbook's evidence `x-com-images` (`images/ch-07/IMAGES.md`). The alt text
  reaches 16.8 pixels in the 0.35 column. (Broken captures; x.com before X)
- `toolbar_counts.png` -- three toolbars' counts and strips of bars, labeled:
  google.com 20,394,311 captures, facebook.com 8,516,746, x.com 94,893
  (2026-09-25). The counts read at 19 pixels; the date ranges under them
  come to 14.4. (Why some sites are archived better)
- `wayback_down.png` (kept) -- web.archive.org itself answering "upstream
  request failed" while this deck was being made, 2026-09-22. (Why is it so
  slow?)
- `devtools_archived.png` -- Chrome DevTools' Elements tree on the archived
  thefacebook.com page, zoomed to 175%: `<div id="wm-ipp-base">`, the
  second div and the script, `<!-- END WAYBACK TOOLBAR INSERT -->`, then the
  original `<center>`, selected. 18.2 pixels. (The Inspector still works)
- `wrapped_vs_raw.png` -- View Source of the same capture, lines wrapped,
  labeled: wrapped (the injected `athena.js`, analytics, `bundle-playback.js`,
  `wombat.js`, Ruffle) above the `id_` raw bytes, which start at the page's
  own `<style>`. 16.5 pixels. (Raw or wrapped?)
- `facebook_2004.png` -- two crops of facebook.com on 2004-01-21, labeled:
  AboutFace's banner, "The first name in directories", and its pitch to
  colleges, "Eliminate the need for printed facebooks." 30 pixels. (Facebook
  before Facebook)
- `thefacebook_2004.png` -- thefacebook.com on 2004-02-12: the
  "[ thefacebook ]" banner and the welcome box, through "Harvard
  University". 17.7 pixels. (Facebook before Facebook)
- `x_com_1997.png` -- x.com on 1997-04-11: its logo, "not nearly the worst
  place on the web!!!", and Dave's World and Rob's House of Weather. The
  page's background image resolves to a 2013 capture the Archive answered
  with 500 on every load, so the page's own beige background color shows.
  17.7 pixels. (x.com before X)
- `google_1998.png` -- google.com on 1998-11-11, the earliest capture, under
  the toolbar with 20,394,311 captures: "Welcome to Google" and its two
  links. 21.4 pixels. (google.com, November 1998)

## Memes -- the instructor's picks

The instructor replaced the four gray meme placeholders in Overleaf (commit
`adb1ce4`, 2026-09-22) with these, under new file names. The old
`meme_*.png` rows were then removed from `stubs.tsv`, so a build does not
draw them again.

- `i-dont-feel-so-good.jpg` -- Link rot.
- `archives-are-incomplete.jpg` -- Missing captures.
- `train-bus.jpg` -- Internet Jones and the Echoes of the Lost Trackers.
- `elrond-i-was-there.jpg` -- Closing activity: time travel with the
  Wayback Machine.

## Older placeholders, not touched in this pass

- `cdx_response.png` (Wednesday) and `pr_review.png` (Friday).

`change_timeline.png` was removed: the Monday frame that used it ("From
snapshots to a longitudinal source") was replaced by "Research designs with
the archived web," and the one Wednesday sentence that pointed back at it
no longer does.

## Listed in `stubs.tsv`

`make_stubs.py` keeps this table in step with `stubs.tsv` and draws a gray
placeholder for any listed image that is missing. It rewrites only what is
between the two markers; the notes above are safe.

<!-- stubs:begin: generated from stubs.tsv by slides/common/make_stubs.py; edits between these markers are replaced -->
| File | Size | Should show |
|---|---|---|
| `wayback_trillion.png` | 810x105 | Screenshot: Wayback Machine search header, "Explore more than 1 trillion web pages saved over time" (web.archive.org, 2026-09-22) |
| `wayback_calendar.png` | 1480x724 | Screenshot: facebook.com's Calendar tab, 2005 selected -- bars of captures per year and January to March 2005's dots (web.archive.org, 2026-09-25) |
| `toolbar.png` | 2080x136 | Screenshot: the Wayback toolbar on facebook.com, January 21, 2004 -- address, 8,516,746 captures, the strip of bars across the years, the date and its arrows (2026-09-25) |
| `address_bar.png` | 1004x42 | Screenshot: browser address bar showing web.archive.org/web/20040212031928/http://www.thefacebook.com/ |
| `about_capture.png` | 1600x478 | Screenshot (copy of textbook figure 7.3): About this capture on thefacebook.com, 2004-02-12 -- Collected by Alexa Crawls (alexa_dv); Timestamps: logo-right.jpg +1 year 3 months, logo-left.jpg +3 months 20 days |
| `calendar_dots_2005.png` | 512x560 | Screenshot composite: facebook.com's 2005 calendar, April (blue on the 6th and 8th, orange from the 10th) and August (orange to the 4th, blue from the 6th) |
| `x_com_1999.png` | 1120x814 | Screenshot: x.com, 1999-11-14 (X.com's pre-launch page), below the toolbar -- every visible image broken, its alt text showing |
| `toolbar_counts.png` | 1892x382 | Screenshot composite: Wayback toolbar counts and strips for google.com (20,394,311 captures), facebook.com (8,516,746), x.com (94,893), 2026-09-25 |
| `wayback_down.png` | 254x42 | Screenshot: web.archive.org answering "upstream request failed" (HTTP 502) while this deck was being made, 2026-09-22 |
| `devtools_archived.png` | 1600x736 | Screenshot: Chrome DevTools Elements tree at 175% on the archived thefacebook.com page (2004-02-12) -- wm-ipp-base toolbar div, END WAYBACK TOOLBAR INSERT, center selected |
| `wrapped_vs_raw.png` | 1272x1010 | Screenshot composite: View Source of the same capture, wrapped (injected Wayback scripts) above id_ raw (the page's own style) |
| `facebook_2004.png` | 542x440 | Screenshot composite: facebook.com, 2004-01-21 -- AboutFace's banner, "The first name in directories", and its pitch, "Eliminate the need for printed facebooks" |
| `thefacebook_2004.png` | 1092x444 | Screenshot: thefacebook.com, 2004-02-12 -- "[ thefacebook ]" banner and the welcome box, through Harvard University |
| `x_com_1997.png` | 1460x840 | Screenshot: x.com, 1997-04-11 -- "not nearly the worst place on the web!!!", Dave's World, Rob's House of Weather |
| `google_1998.png` | 1600x400 | Screenshot: google.com, 1998-11-11, under the toolbar (20,394,311 captures) -- "Welcome to Google", "Google Search Engine Prototype" |
| `cdx_response.png` | 1200x720 | Screenshot: a CDX Server API JSON response, showing the header row then rows of timestamp / original / statuscode / length for successive captures |
| `pr_review.png` | 1300x760 | Screenshot: a GitHub pull-request "Files changed" view with an inline review comment on ch-07-archives.qmd |
<!-- stubs:end -->
