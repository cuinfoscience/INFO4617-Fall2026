# Images for `week-07`

As of the Monday rebuild (web archiving, the Wayback Machine by hand, failure
modes, research designs), 15 of this deck's 21 images are **real screenshots
of the live Wayback Machine**, captured 2026-09-22. Four are **meme
placeholders** left for the instructor to pick, and two (Wednesday's
`cdx_response.png`, Friday's `pr_review.png`) are older gray placeholders
this pass did not touch.

## How the screenshots were made

Headless Chromium (Playwright), routed through this environment's HTTPS
proxy, with an identifying `User-Agent`
(`INFO4617-course-slides ... (contact: accounts@brianckeegan.com)`) and
8--30 second pauses between page loads. The Archive answered `502 Bad
Gateway` or dropped the connection on roughly half of the first attempts, so
every capture was retried with backoff -- the same polite-client pattern the
chapter and the "Why is it so slow?" frame teach. `devtools_archived.png` is
a real Chrome DevTools window, captured from a virtual display (Xvfb), not a
mockup. Crops were done with Pillow from full 1280x800 screenshots.

Live numbers visible in these images (capture counts, "Saved N times")
drift daily; they are correct as of 2026-09-22 and the frames say so.

## Real screenshots

- `wayback_trillion.png` -- the Wayback search header: "Explore more than 1
  trillion web pages saved over time." (Web archiving)
- `wayback_calendar.png`, `calendar_dots_2005.png` -- the calendar view for
  `facebook.com` in 2005 (`web.archive.org/web/2005*/facebook.com`). The
  dots go blue (AboutFace's page) through March, orange (HTTP 403) from
  April, and blue again from 2005-08-06, when the domain starts serving
  Thefacebook's homepage -- verified against the CDX API and the raw
  2005-08-13 capture, whose `<title>` is "Thefacebook | Welcome to
  Thefacebook!". (Finding a capture; Reading the dots)
- `toolbar.png` -- the toolbar on facebook.com, 2004-01-21. (Moving through
  time)
- `address_bar.png` -- the browser address bar on
  `web.archive.org/web/20040212031928/http://www.thefacebook.com/`.
  (The URL is the query)
- `about_capture.png` -- About this capture on the 2004-02-12
  thefacebook.com capture, both sections open. Collected by: organization
  Alexa Crawls, collection `alexa_dv` (the panel loads this section from
  `/__wb/provenance` on hover, so it can lag a few seconds behind the
  Timestamps list). Timestamps: `images/logo-right.jpg` "+1 year 3
  months", `images/logo-left.jpg` "+3 months 20 days". Retaken 2026-09-22
  to show Collected by, which the first take missed. (About this capture)
- `x_com_1999.png` -- x.com, 1999-11-14, X.com Corporation's pre-launch
  page with every visible image broken. The CDX API shows why: of the
  seven images the page references, six have never been captured
  successfully -- their first captures, from August and September 2000,
  are all 404s -- and the seventh, a transparent `spacer.gif`, was saved
  only in April 2000. (Broken captures; x.com before X)
- `toolbar_counts.png` -- three toolbars stacked: google.com 19,954,262
  captures, facebook.com 8,461,424, x.com 83,190. (Why some sites are
  archived better)
- `wayback_down.png` -- web.archive.org itself answering "upstream request
  failed" during capture. (Why is it so slow?)
- `devtools_archived.png` -- Chrome DevTools, Elements panel, on the
  archived thefacebook.com page: `<div id="wm-ipp-base">`,
  `<!-- END WAYBACK TOOLBAR INSERT -->`, then the original `<center>`.
  (The Inspector still works)
- `wrapped_vs_raw.png` -- view-source of the same capture, wrapped (the
  injected `athena.js`, `wombat.js`, `ruffle.js`, `__wm.init`) above the
  `id_` raw bytes (starts at the page's own `<style>`). (Raw or wrapped?)
- `facebook_2004.png`, `thefacebook_2004.png` -- facebook.com on 2004-01-21
  (AboutFace, "The first name in directories") and thefacebook.com on
  2004-02-12. (Facebook before Facebook)
- `x_com_1997.png` -- x.com on 1997-04-11, "not nearly the worst place on
  the web!!!" (x.com before X)
- `google_1998.png` -- google.com on 1998-11-11, the earliest capture.
  (google.com, November 1998)

To retake any of these, open the URL above in a browser and screenshot it;
expect to retry when the Archive returns 502.

## Meme placeholders -- instructor's pick

Gray placeholders so the deck compiles. Each description in `stubs.tsv`
suggests a meme; swap in whatever lands better, keeping the filename.

- `meme_link_rot.png` -- Link rot (suggested: the Thanos snap).
- `meme_archives_incomplete.png` -- Missing captures (suggested: Obi-Wan,
  "Perhaps the archives are incomplete").
- `meme_internet_jones.png` -- Internet Jones and the Raiders of the Lost
  Trackers (suggested: Indiana Jones, "It belongs in a museum!").
- `meme_i_was_there.png` -- Closing activity (suggested: Elrond, "I was
  there 3000 years ago").

## Older placeholders, not touched in this pass

- `cdx_response.png` (Wednesday) and `pr_review.png` (Friday).

`change_timeline.png` was removed: the Monday frame that used it ("From
snapshots to a longitudinal source") was replaced by "Research designs with
the archived web," and the one Wednesday sentence that pointed back at it
no longer does.

Note: `make_stubs.py` regenerates this file from `stubs.tsv` whenever `make`
runs. If that happens, restore these notes from git history.
