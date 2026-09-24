# Finding an RSS feed

*Starter feeds and a directory to browse more — Chapter 4's take-home exercise*

The Chapter 4 lab and take-home both start the same way: find an RSS feed
from a news outlet or podcast, check its `robots.txt`, and parse it with
BeautifulSoup's `"xml"` parser. This page is the practical reference for
that step — a verified starting list, the technique for finding one
yourself, and a directory to browse if none of these fit what you're
interested in.

---

## Starter feeds

The same ten feeds from [the chapter's Recommended
Exercises](https://cuinfoscience.github.io/Web-Data-Science-Book/ch-04-data-formats.html#recommended-exercises),
researched as of September 2026 — treat these as a starting point, not a
guarantee. If one has moved, the status-code check in the exercise's Step 2
is exactly how you'd notice.

**News**

| Outlet | Feed |
|---|---|
| The New York Times | `https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml` |
| BBC News | `https://feeds.bbci.co.uk/news/rss.xml` |
| The Guardian | `https://www.theguardian.com/world/rss` |
| PBS NewsHour | `https://www.pbs.org/newshour/feeds/rss/headlines` |
| Al Jazeera | `https://www.aljazeera.com/xml/rss/all.xml` |

**Podcasts (data, tech, and data journalism)**

| Podcast | Feed |
|---|---|
| Data Skeptic | `https://dataskeptic.libsyn.com/rss` |
| Planet Money (NPR) | `https://feeds.npr.org/510289/podcast.xml` |
| The Changelog | `https://changelog.com/podcast/feed` |
| Data Engineering Podcast | no single published URL — find it on [dataengineeringpodcast.com](https://www.dataengineeringpodcast.com/) using the technique below |
| The PolicyViz Podcast | no single published URL — find it on [policyviz.com/podcast](https://policyviz.com/podcast/) using the technique below |

---

## What a feed looks like

Open a feed's address in Chrome before you write any code. If the feed is
served as XML (`text/xml` or `application/xml`), Chrome draws it as a tree
you can fold: `<rss>`, then one `<channel>`, then one `<item>` per story.
The `<item>` is the element that repeats, and the one your code will loop
over. A feed served as `application/rss+xml`, such as PBS NewsHour's, shows
as plain text instead, with the same structure.

![Screenshot of Chrome's tree view of the feed. Marker 1: the rss root tag and its namespaces. Marker 2: channel, with title BBC News, description BBC News - Science & Environment, a link, and folded image and copyright. Marker 3: the first item, titled Elephants use medicinal plants to treat themselves, researchers find, with description, link, guid, pubDate of 24 September 2026, and thumbnail. Marker 3 again: the second item.](img/rss-feed-xml_annotated.png)

*BBC News's science and environment feed in Chrome, September 2026, one of
the feeds the BBC publishes for each section. `<rss>` ① holds one
`<channel>` ②: the feed's title, description, and link, then one `<item>` ③
per story. Each `CDATA` wrapper marks text the parser takes as it is, and
BeautifulSoup's `.text` returns what is inside. Chrome's triangles fold the
channel's `<image>` and `<copyright>`. (The textbook's Figure 4.3.)*

---

## Finding a feed this list doesn't cover

Most sites don't advertise their feed on the homepage:

- Try appending `/rss`, `/feed`, or `/rss.xml` to the site's root URL — the
  most common convention.
- View the page source, not the rendered page (right-click the page and
  choose **View Page Source**, or press Ctrl + U; ⌘ + ⌥ + U on a Mac), and
  search it for `application/rss+xml`. The `<link>` tag with that `type`
  names the feed's address in its `href`, even when nothing on the page
  itself links to the feed (see the figure below).
- For a podcast specifically, check its listing on a podcast directory
  (Apple Podcasts, Podchaser, Listen Notes) — most display or link to the
  canonical feed even when the show's own site doesn't.
- Look for a small RSS icon or a "Subscribe" link, often in a page footer
  or sidebar.

![Screenshot of Chrome's toolbar over a View Source page. The address bar reads view-source:https://www.pbs.org/newshour/, and the find bar holds application/rss+xml, match 1 of 1. Under the end of a script, line 32 is a canonical link, and line 33 is a link with rel alternate, href https://www.pbs.org/newshour/feeds/rss/headlines, and type application/rss+xml, highlighted. Marker 1 is beside the href.](img/view-source-rss-link_annotated.png)

*PBS NewsHour's home page in View Source, searched with Chrome's find bar
(Ctrl + F, or ⌘ + F on a Mac) for `application/rss+xml`, September 2026.
The one match is on line 33, in a `<link rel="alternate">` whose `href` ① is
the feed's address. (The textbook's Figure 4.2.)*

---

## Browse further

Ten examples won't cover everyone's interests. A few larger, actively
maintained resources for finding more:

- [awesome-rsshub-routes](https://github.com/JackyST0/awesome-rsshub-routes)
  — a searchable, health-checked directory of both official RSS feeds and
  [RSSHub](https://docs.rsshub.app/)-generated ones, for sites that don't
  publish a native feed at all.
- [awesome-rss-feeds](https://github.com/plenaryapp/awesome-rss-feeds) — a
  curated list of RSS feeds (and OPML files) across news and other
  categories.
- [Most Popular RSS Feeds](https://rss.com/blog/popular-rss-feeds/#the-most-popular-podcast-rss-feeds)
  — a roundup of widely-followed podcast feeds specifically (the link jumps
  straight to that section).

Pick something you'd actually want to read or listen to. The exercise works
the same regardless of topic, and you'll enjoy the debugging more if the
data is something you care about.

> **Note:** a feed that looked fine in a directory can still turn out to be
> stale, region-locked, or subtly malformed. That's not a reason to avoid
> the directory — it's the same live-web unpredictability the rest of this
> course runs on. Verify what you pick the same way you'd verify anything
> else: fetch it, check the status code, and look at what actually comes
> back.

---

*See also: [`revision-framework.md`](../common/revision-framework.md) for
turning what you find here into a textbook revision, and
[`pull-request-walkthrough.md`](../common/pull-request-walkthrough.md) for
the click-by-click mechanics of opening that PR.*
