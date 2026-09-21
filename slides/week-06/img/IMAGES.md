# Images for `week-06`

All images are **real, live-sourced or content-accurate assets** as of the
Ch.~6 restructure around the "common static website data formats" strategy
framework. None are gray placeholders.

## Live screenshots (Playwright, real sites, movies theme)

- `bom_weekly_chart.png` -- Box Office Mojo's weekly chart for 2018W52
  (`boxofficemojo.com/weekend/2018W52/`), one clean `<table>`. Strategy 1.
- `the_numbers_table.png` -- The Numbers' weekly chart for 2018-12-28
  (`the-numbers.com/box-office-chart/weekly/2018/12/28`); the page ships
  two `<table>` elements (`chart-desktop` + `chart-mobile`), so the real
  task is picking the right one. Strategy 2.
- `wiki_highest_grossing_table.png` -- the `wikitable` on English
  Wikipedia's "List of highest-grossing films," footnote markers and
  merged studio cells and all. Strategy 3.
- `wiki_infobox_en.png` -- the infobox on English Wikipedia's
  *The Godfather* article (`table.infobox`). Strategy 4.
- `wiki_infobox_fr.png` -- the infobox on French Wikipedia's
  *Le Parrain (film)* article. Same content pattern as `wiki_infobox_en.png`,
  ported to a different site/language edition -- note the table itself
  carries no reusable class name here (Wikipedia's infobox template markup
  is not standardized across language editions the way `infobox`/`infobox_v3`
  might suggest), so the anchor that transfers is the `<caption>` text, not
  a class. Strategy 5.
- `oscar-nominees.png` -- a real screenshot of the Actor in a Leading Role
  category from oscars.org/oscars/ceremonies/2026 (replaces an earlier
  `oscars_cards.png` mockup built before a live screenshot was possible).
  A live headless-browser session (Playwright/Chromium, needed to screenshot
  the rendered page) still times out against oscars.org regardless of
  User-Agent -- confirmed, the site's own bot protection, not a network
  issue on our end. A plain HTTP fetch is different: `requests.get()` with
  no headers or a browser-spoofed one gets HTTP 403, but one with an honest,
  identifying `User-Agent` gets a clean 200 -- see Strategy 6 in the
  notebook and the textbook chapter, both of which fetch the live page this
  way. The class names in the Wednesday code
  (`field--name-field-award-categories`, `paragraph--type--award-category`,
  `field--name-field-honoree-type`, etc.) are the real ones, verified
  against the live page. Strategy 6, and the chapter's running non-tabular
  example.
- `rt_movie_tiles.png` -- Rotten Tomatoes' "Movies in Theaters" tile grid
  (`rottentomatoes.com/browse/movies_in_theaters/`), repeating card elements
  with a visibly different template than the Oscars cards above. Strategy 7.
- `imdb_rendered.png` -- IMDb's *The Godfather* page as a real browser
  renders it after JavaScript runs (cast, ratings, etc. all visible). Paired
  in the deck with the plain-`requests` failure mode: `requests.get()`
  against the same URL returns HTTP 202 with a literally empty body (`len(r.text)
  == 0`). Strategy 8 / the dynamic-content boundary case.

## Recreated-UI mockups (real content, no live screenshot possible)

- `dev_tools_inspect.png` -- a Chrome DevTools-style split view (rendered
  page + Elements panel) built as a static HTML/CSS page rather than
  captured from a live DevTools session (headless Chromium can't screenshot
  its own DevTools panel). The markup shown in the Elements pane is real,
  copied from Box Office Mojo's actual page source (`mojo-body-table`,
  `mojo-field-type-rank`, etc.), not invented.
- `pr_review.png` -- a GitHub pull-request "Files changed" mockup, built
  the same way, showing a real illustrative diff against
  `ch-06-static-pages.qmd` (adding a `colspan`/`rowspan` debugging note)
  with an inline review comment. No such PR needed to be opened against the
  book repo to produce this image.
