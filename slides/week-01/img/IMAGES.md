# Images for `week-01`

Every image this deck lists in `stubs.tsv` began as a gray placeholder. All
eight were replaced on 2026-08-21 (commit `9007506`), by different methods,
and until 2026-09-24 this file still called them placeholders. One of them,
`anaconda_jupyter.png`, a Jupyter session that no slide showed, was deleted on
2026-09-25, when `handouts/week-01/setup.md` took the textbook's figure 1.1 in
its place (`handouts/week-01/img/`). What each of the other seven is:

**Real captures** (headless Playwright, 2026-08-21):

- `pageviews_plot.png` -- that pipeline's real output: daily pageviews for
  "University of Colorado Boulder," January 2024. Not on a slide; the deck
  uses the instructor's `pageviews.pdf`.

**`book_website.png`** is a live capture (2026-09-25) from the textbook's
`tools/shots` course recipe `week01-book-website`: the book's website loaded
480 pixels wide, with the chapter list that the narrow layout folds away
opened, and cropped to the list. On a 1,920-pixel slide its text is 25.8 px
in the frame's 35% column. `shots.json` records it.

**A render from a local copy** (2026-08-21): `github_repo.png` shows the
textbook's GitHub repository, rendered in the browser from a local copy,
because the session's proxy passed the page but not its CDN-hosted styles
and scripts. It waits for a hand capture: this session can't reach github.com
beyond its own repositories, and the textbook's `week01-github-repo` recipe
gives the steps.

**Look-alikes, to be replaced:** `issue_form.png` and `pr_review.png` are
GitHub's interface rebuilt by hand and filled with the deck's worked example.
The pull request they show (#42, "student-reviewer," "course-instructor")
never existed. Under the rule adopted on 2026-09-24 (`slides/common/AUTHORING.md`,
"What counts as a screenshot"), both are to be replaced with real captures.
Both need a signed-in browser, so they are hand captures: the textbook's
course recipes `week01-issue-form` (the Gap report form filled in with the
revision framework's example, not submitted) and `pr-review` (a review comment
on the instructor's own pull request, one image for weeks 1, 8, and 13) give
the steps, and `tools/shots/run import` takes the screenshot.

**Diagrams:** `book_pipeline.png` (changed by the instructor in Overleaf,
commit `d591a34`) and `weekly_workflow.png` (not on a slide).

Added by the instructor and not listed in `stubs.tsv`: `pageviews.pdf`
(commit `4581430`) and `teambuilding.png` (commit `d591a34`).

## Copied by tools/shots

<!-- shots:begin: copies from the textbook's tools/shots, generated from shots.json; edits between these markers are replaced -->
Copied here by the textbook's `tools/shots/run sync`; `tools/shots/run synced` checks them.

| File | Copy of | Captured | Source | How |
|---|---|---|---|---|
| `book_website.png` | `course/week01-book-website` (tools/shots/out/course/week01-book-website/20260925T185502Z.png, textbook `d4c04a3`) | 2026-09-25 | https://cuinfoscience.github.io/Web-Data-Science-Book/ | tools/shots: Google Chrome for Testing 154.0.8037.57, 480×760 at 2× |
<!-- shots:end -->

## Listed in `stubs.tsv`

`make_stubs.py` keeps this table in step with `stubs.tsv` and draws a gray
placeholder for any listed image that is missing. It rewrites only what is
between the two markers; the notes above are safe.

<!-- stubs:begin: generated from stubs.tsv by slides/common/make_stubs.py; edits between these markers are replaced -->
| File | Size | Should show |
|---|---|---|
| `weekly_workflow.png` | 1300x620 | Diagram: the Monday -> Wednesday -> Friday weekly rhythm (concept+notebook -> hands-on lab -> textbook-revision pull request), drawn as three connected bands |
| `pageviews_plot.png` | 1200x680 | Screenshot: matplotlib line plot of daily Wikipedia pageviews for "University of Colorado Boulder" over January 2024, the output of the chapter's first-request pipeline |
| `github_repo.png` | 1200x780 | Screenshot: the Web Data Science Book GitHub repository page (cuinfoscience/Web-Data-Science-Book) showing the chapter .qmd files and the Fork button |
| `pr_review.png` | 1300x760 | Screenshot: a GitHub pull-request "Files changed" view with an inline peer-review comment on ch-01-introduction.qmd |
| `book_website.png` | 776x1024 | Screenshot: the textbook's website, cuinfoscience.github.io/Web-Data-Science-Book, loaded 480 pixels wide with its chapter list open: Preface, then chapters 1-15 in four parts (tools/shots course recipe week01-book-website) |
| `book_pipeline.png` | 1250x700 | Diagram: ch-NN-topic.qmd (plain text + code) -> `quarto render` -> published website on GitHub Pages; annotate that the repo is the source of truth and the site is a build artifact |
| `issue_form.png` | 1200x780 | Screenshot: the GitHub "New issue" form on the Web-Data-Science-Book repo, with a title following the "<type>: <specific thing> in Ch. N" pattern and the five-field body filled in |
<!-- stubs:end -->
