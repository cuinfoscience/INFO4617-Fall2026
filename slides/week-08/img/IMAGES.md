# Images for `week-08`

As of the October rebuild (check by hand first, Selenium Manager, Playwright
as a scripting and agent option), 10 of this deck's 14 images are **real
screenshots or a real diagram**, first captured 2026-09-22/23. Four are
**meme placeholders** left for the instructor to pick. All six of the deck's
older gray placeholders were replaced.

On a slide shown 1,920 pixels wide, text should reach 16 pixels
(`slides/common/AUTHORING.md`). Three screenshots were remade on 2026-09-25
to reach it: `requests_vs_browser.png`, `js_off.png`, and
`playwright_home.png`, whose text had come to about 7 to 11 pixels.
`network_json.png`, retaken on 2026-09-24, reaches 23. Three still fall short
and wait: `selenium_browser.png` and `codegen.png`, whose subject is the tool
itself, for the toolkit's Selenium and codegen engines (milestone M4), and
`pr_review.png`, for a session that can read github.com's `robots.txt`.

## How the images were made

**Remade 2026-09-25.** `requests_vs_browser.png`, `js_off.png`, and
`playwright_home.png` come from the recipes named `week08-*` in the
textbook's `tools/shots/recipes/course.yml`, captured with its `tools/shots`
(Chrome for Testing 154, headless, through Playwright 1.63.0) in windows 480
CSS pixels wide, at 2 image pixels per CSS pixel. Each recipe names the width
its frame shows it at, and the capture reports the text's size on the slide.
Every request sent the User-Agent `Web Data Science/v1
brian.keegan@colorado.edu`, and page loads on one host were 8--30 seconds
apart; playwright.dev's `robots.txt` allows `/python/`. To retake one, run
`tools/shots/run capture course --only week08-...` in the textbook repo and
copy the take here under the deck's file name.

**Captured 2026-09-22/23.** Selenium 4.49.0 and Playwright 1.63.0 in a fresh
virtual environment. The Chrome windows are Chrome for Testing 154,
downloaded by Selenium Manager itself (the machine had no Chrome), driven
headed on a virtual display (Xvfb) and captured with ImageMagick; DevTools
was operated with real clicks
(xdotool), not mocked up. Playwright's own screenshots used its bundled
Chrome for Testing 153. Pages were loaded with an identifying `User-Agent`
(`INFO4617-course-materials ... (contact: accounts@brianckeegan.com)`).
The practice pages are the Quotes to Scrape sandbox (toscrape.com), which is
built for scraping practice and has no `robots.txt`.

Live details in these images (xkcd's current comic, version numbers, the PR's
file count, Playwright's star count) drift; they are correct as of the
capture dates.

## Real images

- `requests_vs_browser.png` -- `quotes.toscrape.com/js/` rendered with
  JavaScript disabled (title, Login, Next, footer) and enabled (quotes), side
  by side, labeled. (Zero bytes)
  - Remade 2026-09-25 (`week08-requests-vs-browser`): two 480-pixel pages,
    410 CSS pixels tall with their labels. At `0.78\textwidth` its text comes
    to 18 pixels on a 1920-pixel slide; the 2026-09-23 version, two
    900-pixel pages, showed it at about 10. The frame needed no change,
    because the new image has the old one's shape.
- `decision_tree.png` -- Graphviz diagram: API? -> in View Source (even in a
  `<script>`)? -> JSON in the Network tab? -> drive a browser (Selenium in the
  notebook, Playwright as a script). Source: `decision_tree.dot`, next to
  the image; regenerate with `dot -Tpng decision_tree.dot -o decision_tree.png`. (Check by hand first)
- `view_source_js.png` -- View Source of `quotes.toscrape.com/js/`, lines
  27-43: the quotes sit in a `<script>` as `var data = [ ... ]`. (Check 1)
- `js_off.png` -- the same page with JavaScript disabled. (Check 2)
  - Remade 2026-09-25 (`week08-js-off`): 480×400 CSS pixels, with the
    footer's two lines. In its 35% column its text comes to 19.6 pixels; the
    900-pixel version showed it at about 10.5.
- `network_json.png` -- Chrome DevTools Network tab on
  `quotes.toscrape.com/scroll`, filtered to Fetch/XHR after scrolling:
  `quotes?page=1` through `page=4`, with Preview showing page 2's JSON
  (`has_next`, `page`, `quotes[0].author/tags/text`). (Check 3)
  - Retaken 2026-09-24. The first version showed the whole 1680-pixel window,
    with Chrome for Testing's "only for automated testing" notice under the
    address bar. It is now the top 800×335 CSS pixels of the textbook's
    `images/ch-08/network-tab-json.png`, cropped to end after
    `quotes[0].text`. That figure was captured by `tools/shots`: DevTools
    alone, zoomed to 125%, with no notice.
  - At `0.8\textwidth` its text comes to about 23 pixels on a 1920-pixel
    slide, above the 16-pixel floor. The frame needed no change, because the
    crop is close to the old image's shape.
- `selenium_browser.png` -- Chrome for Testing 154, downloaded by Selenium
  Manager and driven by Selenium, on xkcd.com. It shows CfT's own "only for
  automated testing" bar (not the classic "controlled by automated test
  software" banner, which regular Chrome shows). It is the one screenshot
  that keeps that bar, because the bar is the point of the slide; every
  other screenshot is taken without it (`AUTHORING.md`). The mouse happened to rest on
  the comic, so xkcd's hover text is visible -- the `title` attribute the lab
  extracts. (Selenium: a browser you drive with code)
  - Too small on its slide: 1,280 pixels across in a 35% column shows it at
    46% of its size on screen. The window Selenium opens is the subject, so
    the retake waits for the toolkit's Selenium engine (M4).
- `playwright_home.png` -- playwright.dev/python, 2026-09-25: its menu bar
  and headline, "Playwright enables reliable web automation for testing,
  scripting, and AI agents." (Playwright)
  - Remade 2026-09-25 (`week08-playwright-home`): 480 pixels wide, where the
    site shows its phone layout, cropped at the foot of the headline block
    (480×528 CSS pixels). In its 35% column its text comes to 19.6 pixels;
    the 1,280-pixel version of 2026-09-23 showed its menu at about 7.
- `codegen.png` -- `playwright codegen --target python` on
  quotes.toscrape.com after two recorded clicks (the tag *change*, then an
  *(about)* link); the browser shows codegen's locator tooltip,
  `get_by_role("heading", name="Albert Einstein")`, and the Inspector shows
  the generated script. (Record, then read)
  - Too small on its slide: 1,630 pixels across in a 55% column shows it at
    57% of its size on screen. The retake waits for the toolkit's codegen
    engine (M4).
- `xkcd_inspect.png` -- DevTools Elements panel after right-click > Inspect on
  xkcd's comic: the selected `<img>` with its `title` (hover joke) and `alt`
  attributes. (Read attributes, then act like a user)
- `pr_review.png` -- the public "Files changed" view of textbook PR #129
  (the Chapter 8 expansion this deck was built with). It shows the PR header,
  Checks and Files-changed tabs, the file tree, and an image diff; GitHub
  collapses the large `.qmd` diff for anonymous viewers. No student work is
  shown. (Improving Chapter 8 together)
  - Too small on its slide: 1,300 pixels across in a 35% column shows it at
    45% of its size on screen. The retake waits for a session that can read
    github.com's `robots.txt`: a cloud session reaches github.com only for
    its own repositories.

To retake one of the 2026-09-22/23 images by hand, open the page in Chrome
and screenshot it; the DevTools shots need the panel docked right at about
1680x1000.

## Meme placeholders -- instructor's pick

Gray placeholders so the deck compiles. Each description in `stubs.tsv`
suggests a meme; swap in whatever lands better, keeping the filename.

- `meme_it_just_works.png` -- Selenium Manager (suggested: Todd Howard, "It
  just works"; the next frame is titled "When it doesn't").
- `meme_its_a_trap.png` -- Why not in the notebook? (suggested: Admiral
  Ackbar, "It's a trap!").
- `meme_captain_now.png` -- An assistant at the wheel (suggested: Captain
  Phillips, "Look at me. I am the captain now.").
- `meme_is_this_dynamic.png` -- Closing activity (suggested: "Is this a
  pigeon?" relabeled "Is this a dynamic page?").

## Removed

`infinite_scroll.png` (a gray placeholder diagram) was dropped: the
infinite-scroll lab frame now points back to Monday's Network-tab check,
which shows the same scroll page's JSON at a legible size.

## Listed in `stubs.tsv`

`make_stubs.py` keeps this table in step with `stubs.tsv` and draws a gray
placeholder for any listed image that is missing. It rewrites only what is
between the two markers; the notes above are safe.

<!-- stubs:begin: generated from stubs.tsv by slides/common/make_stubs.py; edits between these markers are replaced -->
| File | Size | Should show |
|---|---|---|
| `requests_vs_browser.png` | 2020x820 | Screenshot composite: quotes.toscrape.com/js/ at 480 pixels wide, JavaScript off (no quotes) and on (quotes rendered), 2026-09-25 |
| `decision_tree.png` | 1619x1002 | Diagram (Graphviz): API? -> in View Source (even in a script)? -> JSON in the Network tab? -> drive a browser (Selenium in the notebook, Playwright as a script) |
| `view_source_js.png` | 1100x290 | Screenshot: View Source of quotes.toscrape.com/js/, lines 27-43 -- the quotes sit in a script as var data = [ ... ] |
| `js_off.png` | 960x800 | Screenshot: quotes.toscrape.com/js/ at 480 pixels wide with JavaScript disabled -- title, Login, Next, footer, no quotes (2026-09-25) |
| `network_json.png` | 1600x670 | Screenshot: Chrome DevTools Network tab on quotes.toscrape.com/scroll, Fetch/XHR filter, quotes?page=1..4, Preview of page 2's JSON (a crop of the textbook's ch-08 network-tab-json, 2026-09-24) |
| `selenium_browser.png` | 1280x860 | Screenshot: Chrome for Testing 154 (downloaded by Selenium Manager) driven by Selenium on xkcd.com, with its "only for automated testing" bar |
| `meme_it_just_works.png` | 1000x750 | Meme: Todd Howard, "It just works" -- Selenium Manager fetching the driver and browser for you |
| `playwright_home.png` | 960x1056 | Screenshot: playwright.dev/python at 480 pixels wide, its menu bar and headline -- "Playwright enables reliable web automation for testing, scripting, and AI agents." (2026-09-25) |
| `meme_its_a_trap.png` | 1000x750 | Meme: Admiral Ackbar, "It's a trap!" -- Playwright's sync API inside a Jupyter notebook |
| `codegen.png` | 1630x860 | Screenshot: playwright codegen recording on quotes.toscrape.com -- browser with locator tooltip, Inspector with the generated Python |
| `meme_captain_now.png` | 1000x750 | Meme: Captain Phillips, "Look at me. I am the captain now." -- an AI agent taking the wheel of your browser |
| `meme_is_this_dynamic.png` | 1000x750 | Meme: "Is this a pigeon?" relabeled "Is this a dynamic page?" -- closing activity, Do you need a browser? |
| `xkcd_inspect.png` | 555x300 | Screenshot: Chrome DevTools Elements panel on xkcd.com with the comic img selected -- title (hover joke) and alt attributes |
| `pr_review.png` | 1300x820 | Screenshot: GitHub "Files changed" view of a textbook pull request (Web-Data-Science-Book #129) |
<!-- stubs:end -->
