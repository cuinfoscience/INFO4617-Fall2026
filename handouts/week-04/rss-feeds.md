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

## Finding a feed this list doesn't cover

Most sites don't advertise their feed on the homepage:

- Try appending `/rss`, `/feed`, or `/rss.xml` to the site's root URL — the
  most common convention.
- View the page source (not the rendered page) and search for
  `type="application/rss+xml"` — it names the feed URL directly in a
  `<link>` tag, even when nothing is visible on the page itself.
- For a podcast specifically, check its listing on a podcast directory
  (Apple Podcasts, Podchaser, Listen Notes) — most display or link to the
  canonical feed even when the show's own site doesn't.
- Look for a small RSS icon or a "Subscribe" link, often in a page footer
  or sidebar.

---

## Browse further

Ten examples won't cover everyone's interests. [Feedspot](https://www.feedspot.com/)
maintains a much larger, actively updated directory, organized by category:

- [Best News RSS Feeds by Category](https://rss.feedspot.com/news_rss_feeds/)
  — national, business, politics, regional, and more
- [Best Podcast RSS Feeds by Category](https://rss.feedspot.com/bestpodcasts_rss_feeds/)
  — organized by topic; each entry links to its actual feed

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
