# Images for `week-01`

Every image this deck lists in `stubs.tsv` began as a gray placeholder. All
eight were replaced on 2026-08-21 (commit `9007506`), by different methods,
and until 2026-09-24 this file still called them placeholders. What each one
is:

**Real captures** (headless Playwright, 2026-08-21):

- `anaconda_jupyter.png` -- a real Jupyter Notebook session running the
  `webdata` kernel on Chapter 1's first-request pipeline. Used by
  `handouts/week-01/setup.md`; not on a slide.
- `pageviews_plot.png` -- that pipeline's real output: daily pageviews for
  "University of Colorado Boulder," January 2024. Not on a slide; the deck
  uses the instructor's `pageviews.pdf`.

**Renders from a local copy** (2026-08-21): `book_website.png` and
`github_repo.png` show real content from the textbook's published site and
its GitHub repository. They were rendered in the browser from a local copy,
because the session's proxy passed the pages but not their CDN-hosted styles
and scripts. Both are to be re-captured live in the chapter 1 back-fill
(the textbook repo's `docs/plans/2026-09-24-screenshot-backfill-ch01-05.md`).

**Look-alikes, to be replaced:** `issue_form.png` and `pr_review.png` are
GitHub's interface rebuilt by hand and filled with the deck's worked example.
The pull request they show (#42, "student-reviewer," "course-instructor")
never existed. Under the rule adopted on 2026-09-24 (`slides/common/AUTHORING.md`,
"What counts as a screenshot"), both are to be replaced with real captures in
the chapter 1 back-fill: a real filed issue on the textbook repo, and a
public pull request's "Files changed" view.

**Diagrams:** `book_pipeline.png` (changed by the instructor in Overleaf,
commit `d591a34`) and `weekly_workflow.png` (not on a slide).

Added by the instructor and not listed in `stubs.tsv`: `pageviews.pdf`
(commit `4581430`) and `teambuilding.png` (commit `d591a34`).

## Listed in `stubs.tsv`

`make_stubs.py` keeps this table in step with `stubs.tsv` and draws a gray
placeholder for any listed image that is missing. It rewrites only what is
between the two markers; the notes above are safe.

<!-- stubs:begin: generated from stubs.tsv by slides/common/make_stubs.py; edits between these markers are replaced -->
| File | Size | Should show |
|---|---|---|
| `weekly_workflow.png` | 1300x620 | Diagram: the Monday -> Wednesday -> Friday weekly rhythm (concept+notebook -> hands-on lab -> textbook-revision pull request), drawn as three connected bands |
| `anaconda_jupyter.png` | 1200x820 | Screenshot: Anaconda Navigator (or a terminal running `jupyter notebook`) launching a Jupyter Notebook with the webdata environment active |
| `pageviews_plot.png` | 1200x680 | Screenshot: matplotlib line plot of daily Wikipedia pageviews for "University of Colorado Boulder" over January 2024, the output of the chapter's first-request pipeline |
| `github_repo.png` | 1200x780 | Screenshot: the Web Data Science Book GitHub repository page (cuinfoscience/Web-Data-Science-Book) showing the chapter .qmd files and the Fork button |
| `pr_review.png` | 1300x760 | Screenshot: a GitHub pull-request "Files changed" view with an inline peer-review comment on ch-01-introduction.qmd |
| `book_website.png` | 1200x800 | Screenshot: the published Quarto book at cuinfoscience.github.io/Web-Data-Science-Book showing the sidebar table of contents (four modules, 15 chapters) and a chapter open |
| `book_pipeline.png` | 1250x700 | Diagram: ch-NN-topic.qmd (plain text + code) -> `quarto render` -> published website on GitHub Pages; annotate that the repo is the source of truth and the site is a build artifact |
| `issue_form.png` | 1200x780 | Screenshot: the GitHub "New issue" form on the Web-Data-Science-Book repo, with a title following the "<type>: <specific thing> in Ch. N" pattern and the five-field body filled in |
<!-- stubs:end -->
