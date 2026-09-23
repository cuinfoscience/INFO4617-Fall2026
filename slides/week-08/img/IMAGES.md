# Images for `week-08`

As of the October rebuild (check by hand first, Selenium Manager, Playwright
as a scripting and agent option), 10 of this deck's 14 images are **real
screenshots or a real diagram**, captured 2026-09-22/23. Four are **meme
placeholders** left for the instructor to pick. All six of the deck's older
gray placeholders were replaced.

## How the images were made

Selenium 4.49.0 and Playwright 1.63.0 in a fresh virtual environment. The
Chrome windows are Chrome for Testing 154, downloaded by Selenium Manager
itself (the machine had no Chrome), driven headed on a virtual display (Xvfb)
and captured with ImageMagick; DevTools was operated with real clicks
(xdotool), not mocked up. Playwright's own screenshots used its bundled
Chrome for Testing 153. Pages were loaded with an identifying `User-Agent`
(`INFO4617-course-materials ... (contact: accounts@brianckeegan.com)`).
The practice pages are the Quotes to Scrape sandbox (toscrape.com), which is
built for scraping practice and has no `robots.txt`.

Live details in these images (xkcd's current comic, version numbers, the PR's
file count) drift; they are correct as of the capture dates.

## Real images

- `requests_vs_browser.png` -- `quotes.toscrape.com/js/` rendered with
  JavaScript disabled (title, Login, Next, footer) and enabled (quotes), side
  by side, labeled. (Zero bytes)
- `decision_tree.png` -- Graphviz diagram: API? -> in View Source (even in a
  `<script>`)? -> JSON in the Network tab? -> drive a browser (Selenium in the
  notebook, Playwright as a script). Source: `decision_tree.dot`, next to
  the image; regenerate with `dot -Tpng decision_tree.dot -o decision_tree.png`. (Check by hand first)
- `view_source_js.png` -- View Source of `quotes.toscrape.com/js/`, lines
  27-43: the quotes sit in a `<script>` as `var data = [ ... ]`. (Check 1)
- `js_off.png` -- the same page with JavaScript disabled. (Check 2)
- `network_json.png` -- Chrome DevTools Network tab on
  `quotes.toscrape.com/scroll`, filtered to Fetch/XHR after scrolling:
  `quotes?page=1` through `page=4`, with Preview showing page 2's JSON
  (`has_next`, `page`, `quotes[0].author/tags/text`). (Check 3)
- `selenium_browser.png` -- Chrome for Testing 154, downloaded by Selenium
  Manager and driven by Selenium, on xkcd.com. It shows CfT's own "only for
  automated testing" bar (not the classic "controlled by automated test
  software" banner, which regular Chrome shows). The mouse happened to rest on
  the comic, so xkcd's hover text is visible -- the `title` attribute the lab
  extracts. (Selenium: a browser you drive with code)
- `playwright_home.png` -- playwright.dev/python, 2026-09-23: "Playwright
  enables reliable web automation for testing, scripting, and AI agents."
  (Playwright)
- `codegen.png` -- `playwright codegen --target python` on
  quotes.toscrape.com after two recorded clicks (the tag *change*, then an
  *(about)* link); the browser shows codegen's locator tooltip,
  `get_by_role("heading", name="Albert Einstein")`, and the Inspector shows
  the generated script. (Record, then read)
- `xkcd_inspect.png` -- DevTools Elements panel after right-click > Inspect on
  xkcd's comic: the selected `<img>` with its `title` (hover joke) and `alt`
  attributes. (Read attributes, then act like a user)
- `pr_review.png` -- the public "Files changed" view of textbook PR #129
  (the Chapter 8 expansion this deck was built with). It shows the PR header,
  Checks and Files-changed tabs, the file tree, and an image diff; GitHub
  collapses the large `.qmd` diff for anonymous viewers. No student work is
  shown. (Improving Chapter 8 together)

To retake any of these, open the page in Chrome and screenshot it; the
DevTools shots need the panel docked right at about 1680x1000.

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

Note: `make_stubs.py` regenerates this file from `stubs.tsv` whenever `make`
runs. If that happens, restore these notes from git history.
