# Facts that live in more than one place

Some facts about the course are written in several files: the syllabus, the
Canvas tooling, the slides, the handouts, and the textbook. When one of them
changes, change every place listed below in the same pull request, and say in
its description that you did. When you find a new place a fact is written,
add it to this table.

This register comes from the 2026-10-16 AAR
([`aar/2026-10-16-weeks-06-09.md`](aar/2026-10-16-weeks-06-09.md), P0-2): in
the week of 2026-10-12 alone, four facts were correct in one file and wrong in
another, and each was found only when someone asked.

| Fact | Current value | Where it's written |
|---|---|---|
| Grade weights | Notebook Labs 30%, Textbook Revisions 15%, Attendance 15%, Final Project 40% | `syllabus/syllabus.tex` (Evaluation); `canvas/course_spec.py` (`GROUPS`, and the syllabus page's grading table); `canvas/README.md` (the `groups` row); `slides/week-01/week-01.tex` (the grading frames) |
| Final Project parts | Proposal 5% (Friday, Oct 23); presentation 10% (final week, Nov 30–Dec 4); repository and write-up 25% (Monday, Dec 7) | `syllabus/syllabus.tex` (Evaluation, course outline, weeks 10 and 16); `canvas/course_spec.py` (`FINAL_PARTS`, `FINAL_DUE`, and the syllabus page's grading table and schedule note); `slides/week-01/week-01.tex` (course outline); `slides/week-09/week-09.tex` (Friday: grade and dates, what we expect); `slides/week-10/week-10.tex` (at a glance, Monday's proposal frame, Friday's checklist and reminder) |
| What the proposal contains | A research question; data source(s) and method; ethics and feasibility, with one record retrieved | `slides/week-09/week-09.tex` (What we expect); `slides/week-10/week-10.tex` (at a glance, Monday, Friday); `canvas/course_spec.py` (`PROPOSAL_DESCRIPTION`, the assignment page, which also splits the 5 points 1.5 / 1.5 / 2) |
| The `webdata` environment command | `conda create -n webdata --override-channels -c conda-forge python=3.14 notebook requests beautifulsoup4 lxml pandas matplotlib seaborn gensim dnspython selenium playwright-python pypdf pdfplumber pytesseract tesseract praw spotipy atproto mastodon.py openai anthropic` | This repo: `handouts/week-01/setup.md` (the create line and the catch-up `conda install -n webdata` line). The textbook: `ch-01-introduction.qmd`, `README.md`, `AGENTS.md` ("Key Python libraries"), and `docs/decisions.md`. Any deck or chapter that tells students to install one of these packages, such as week 9's install frame |
| Code copied from a chapter onto slides | The chapter's current code | The week's deck. A comment above its Wednesday frames names the chapter and the textbook PR the code came from; when that chapter's code changes, update the frames (or the comment, if the frames still match) |
| Figures copied from the textbook | What `tools/shots` last synced | Each week's `img/shots.json` and the "Copied by tools/shots" table in its `IMAGES.md`. Check them with the textbook's `tools/shots/run synced --course <this repo>` |
