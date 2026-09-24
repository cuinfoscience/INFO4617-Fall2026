# Authoring a weekly lecture deck — contract

Every weekly deck in `slides/week-NN/` is built to this spec so the set is
consistent. Three reference decks, for different things: **`week-06/week-06.tex`**
for build mechanics and preamble usage, and **`week-02/week-02.tex`** and
**`week-03/week-03.tex`, both as they stand on main** — the instructor
hand-rewrote both, extensively — for voice, frame patterns, and density.
week-02 set the original voice; week-03 is that voice three weeks into a live
classroom, and is where the course-operations patterns below (grading
philosophy, error triage, the Daily-note-questions frame) repeated often
enough to codify as rules rather than one-off choices. When decks disagree
about how a frame should read, prefer whichever was hand-edited more
recently — voice evolves forward, not backward.

## Files a week folder must contain
- `week-NN.tex` — the deck source, named for its folder (this spec)
- `week-NN.pdf` — compiled output (must build clean)
- `img/stubs.tsv` — manifest of placeholder images
- `img/*.png` — real images, or placeholders drawn by `make_stubs.py`
- `img/IMAGES.md` — where each image came from; `make_stubs.py` maintains only
  the table between its `<!-- stubs:… -->` markers

## Deck structure (target 25–40 frames; density from one-topic-per-frame, not from packing)
1. `\documentclass[9pt,aspectratio=169]{beamer}`, then the input-path line
   `\makeatletter\def\input@path{{../common/}}\makeatother`, then
   `\input{preamble}` (identical to week-06 — do **not** re-declare
   packages/theme/colors). The input-path line lets the deck find the shared
   theme and preamble in `../common/` when compiled directly from its folder.
2. `\title[Week N · short]{{\Huge Full Title}}`, `\subtitle{Week N · <module> module · Textbook Chapter C}`,
   `\author[Keegan]{\textbf{Brian C. Keegan, Ph.D.} \\ Associate Professor, Department of Information Science \\ University of Colorado Boulder}`,
   `\date{<dates>}`, then `\maketitle`.
3. **"This week at a glance"** frame — the Monday/Wednesday/Friday roadmap using `\dayband{Day}{Topic}`, plus a companion-notebook block (`ch-NN-slug.ipynb`).
4. `\section{Monday · Concepts}` — motivation + the chapter's core concepts,
   grounded in its conceptual prose, one topic per frame. Shipped decks range
   from 9 to 22 frames here (week-02: 17, week-03: 22, week-05: 9, week-06: 13)
   depending on how many distinct concepts/strategies/cases the chapter's
   material actually supports — let the chapter's own density decide the
   count rather than aiming for a fixed number. Note cross-references the
   chapter makes to other chapters, and back-reference (don't re-teach in
   depth) any skill an earlier week already covered in full.
5. `\section{Wednesday · Notebook Lab}` — condensed **real code** from the
   chapter as `[fragile]` frames with `lstlisting` (trim each snippet to
   ≤ ~12 lines; keep it runnable-looking and faithful), plus:
   - a frame listing the chapter's **Exercises** to work in pairs (mark any "graduate / INFO 5617" exercise with a bold `\textbf{5617}` label);
   - a **Show-and-Tell** prompt (bring a bug / interesting data / a research provocation — the instructor's recurring habit);
   - one `[standout]` frame with a memorable takeaway from the chapter.

   Shipped decks range from 6 to 15 frames here (week-02: 12, week-03: 6,
   week-05: 14, week-06: 12) — a chapter with more distinct strategies or
   code patterns earns more frames; a chapter that's mostly one worked
   example doesn't need padding to hit a number. If a chapter's Monday and
   Wednesday material is thin enough that splitting them reads as padding,
   merging into one `\section{Wednesday · Concepts \& Notebook}` is an
   established alternative (week-04) — the three-section Monday/Wednesday/
   Friday split is the default, not a hard requirement.
6. `\section{Friday · Textbook Revisions}` — 3 frames: the PR + peer-review workflow (reuse week-06's), a **chapter-specific "revision menu"** (concrete targets pulled from *this* chapter's callouts / "Common Issues" / "Further Reading" / thin exercises), and "what makes a good PR / good review" (reuse week-06's). End the last frame with a one-line teaser of next week.
7. **"Key takeaways"** — 5 numbered points from the chapter, trimmed to short
   plain statements. No trailing reading-list line (see Citations, below).

## Images
List every image you reference in `img/stubs.tsv` — tab-separated:
`filename<TAB>WIDTHxHEIGHT<TAB>one-line description of the real asset`.
Aim for ~3–6 images that mirror useful figures/screenshots the chapter or the
prior deck implies (dev-tools screenshots, diagrams, network/graph figures, a
GitHub PR screenshot for the Friday section, etc.). Then, **from the week
folder**, run:

```bash
python3 ../common/make_stubs.py .
```

This renders a labeled gray placeholder for each listed image that doesn't
exist yet, and keeps a table of them in `IMAGES.md` between two
`<!-- stubs:… -->` markers. Everything else in `IMAGES.md` is yours, and the
script never rewrites it: when you replace a placeholder, record there where
the real image came from, how it was made, and the date. When a listed image
is no longer wanted, or you replace it under a new file name, delete its row
from `stubs.tsv`, or the next build draws the placeholder again. Reference
images as `img/name.png`.

**What counts as a screenshot** (decided 2026-09-24; see P0-3 of the
screenshot AAR, now in the textbook repo at
[`docs/aar/2026-09-24-screenshots.md`](https://github.com/cuinfoscience/Web-Data-Science-Book/blob/main/docs/aar/2026-09-24-screenshots.md)):

- A screenshot is a real capture of a real page, by a person or a tool.
  `IMAGES.md` records its URL, its date, and how it was made.
- Diagrams, charts, and renders drawn from live data (week-02's `robots.txt`
  figure, for example) are welcome. `IMAGES.md` says what each one is, and a
  render drawn to look like a browser window says so in its slide caption.
- Never rebuild a real site's interface by hand and fill it with invented
  content. If a page can't be captured (it needs a login, say), keep the
  placeholder until someone captures the real page, or show a real page that
  makes the same point.
- A count, date, or total printed in a caption or on a slide comes from a
  query whose limit and paging are recorded next to the figure. If the query
  hit its limit, page until it doesn't, or don't print the number.
- No browser banners (decided 2026-09-24). A screenshot never shows Chrome
  for Testing's "only for automated testing" notice, or any other infobar. It
  takes space and says nothing about the page. Run Chrome with
  `--disable-infobars`: the textbook's `tools/shots` does, and fails a
  capture with an infobar. The one exception is a screenshot whose subject is
  the bar itself, week 08's `selenium_browser.png`.

**How much a screenshot shows** (decided 2026-09-24, P1-5; restated the same
day as P0-1 of the
[textbook AAR](https://github.com/cuinfoscience/Web-Data-Science-Book/blob/main/docs/aar/AAR_Web-Data-Science-Book_2026-09-24.md)):
text in a screenshot must be readable where it is shown, at both ends. A
student can't use text that is too small, and can't use a screenshot too
crammed to follow. So scope each screenshot to what the slide discusses,
then make it large.

- Crop to what the slide discusses, and hide the panels, columns, and
  sidebars it doesn't mention. As a soft limit, a screenshot shows 800×600
  CSS pixels of the screen by default.
- It may relax to 1024×768 (decided 2026-09-24) when two things are true:
  the extra room removes clutter (rows that wrap, columns cut short with "…",
  panels squeezed together), and its text still reaches 16 pixels on the
  slide. Say what the room removes in `IMAGES.md`, or in the recipe's
  `oversize:` when the textbook's `tools/shots` makes it.
- For DevTools, zoom DevTools to 125–175% rather than widening the window. A
  row that wraps, or a column cut short with "…", means the capture shows
  too much for its size: crop it, or relax to 1024×768 if the text still
  reaches 16 pixels.
- Capture at 2× (a 1600×1200 image), so text stays sharp on a projector.
- On a slide, the smallest text has to reach 16 pixels on a slide shown
  1920 pixels wide. The textbook's `tools/shots/run check` is the one place
  that judges this. Give the recipe the width you plan to use
  (`targets: {slides: {width: …}}`), and `check` fails the figure if its
  text comes out smaller.
- As a starting point for a page's own text, a capture W CSS pixels wide
  needs at least W/1680 of the text width. For an 800-pixel capture that is
  `width=0.48\textwidth`, and for a 1024-pixel capture `width=0.61\textwidth`.
  DevTools' text is smaller, so DevTools needs more: week 05's Inspector
  figure needs 0.56, and a 1024-pixel DevTools capture zoomed to 150% about
  0.6. Chrome's XML viewer and View Source draw 13-pixel text, so an
  800-pixel capture of either needs about 0.59: week 04's House roster does.
- Going beyond 1024×768 is allowed with a reason in `IMAGES.md`. For
  example, a thin strip like the Wayback toolbar can be 1280 wide, because it
  is shown at full width.

**Copies from the textbook.** A figure the textbook's `tools/shots` made is
copied here, not retaken: to refresh it, retake and promote it in the
textbook, then copy it again. Slides take the `_annotated.pdf`, whose markers
are vector graphics. A Markdown handout, read on GitHub, takes the
`_annotated.png`, because GitHub doesn't show a PDF inline. A copy the deck
doesn't use yet gets a row in the week's `IMAGES.md` ("Used on: not yet") and
none in `stubs.tsv`, which lists what the deck includes.

**Field notes.** What earlier captures taught is in the textbook's
[`tools/shots/README.md`](https://github.com/cuinfoscience/Web-Data-Science-Book/blob/main/tools/shots/README.md#field-notes),
"Field notes": robots.txt rules per host and for AI agents, content types,
Chrome's XML viewer and View Source, crops, and markers. Read it before a
capture, and add a note when a capture teaches you something the next person
would otherwise find out again.

## Voice and frame patterns (learned from the instructor's week-02 and week-03 rewrites)

The instructor hand-rewrote the week-02 deck in August 2026 (commits `9362b5b`,
`d07486a`, `8c4aa64`, `6f8641b`, `9e511ef`, `1e76b18`) and the week-03 deck across
late August and early September (commits `f23c248`, `ae10824`, `310d5d1`,
`99e0292`, `d0ccebe`). Those edits are the best available record of how these
slides should sound. The patterns below were each applied repeatedly across
frames — treat them as the house voice, and treat the current
`week-02/week-02.tex` and `week-03/week-03.tex` as the exemplars to imitate.

**The concept-frame formula.** A frame that presents one case, event, or idea:
a bare, factual title (*"Aaron Swartz"*, *"Bright Data (2024)"* — not *"2024:
Bright Data and the limits of contract"*); a 0.6 column of two to four short
plain paragraphs separated by `\medskip`; a 0.35 column with an image
(`\centering`, width `.65`–`1.0\textwidth`); and, where the frame has a
so-what, a full-width `\begin{alertblock}{Consequences}` at the bottom of the
frame carrying it. No labeled sub-structure ("The facts. / The holding. / Why
it matters.") — the paragraphs just say the thing.

**One topic per frame.** Split combined frames (the instructor split
Swartz/Cambridge Analytica into two). Cover a topic fully on its frame and move
on. No minute-by-minute agenda frames — the "This week at a glance" frame is
the only roadmap — and no end-of-section summary tables; the Consequences
blocks carry the through-line.

**Cut the meta-commentary — start with the question.** The instructor
repeatedly deleted sentences that announce what a section is about to do,
leaving only the thing itself. Week-03's access-matrix frame opened with
"Enclosure, exemption, and erosion are claims about the world. Claims about
the world can be checked. The chapter's audit asks eight endpoints one
question:" — he cut all three sentences to one: "What happens if you show up
to a website with no credentials and ask for data?" A frame's opening line
should be the question, the claim, or the case — never a sentence describing
that a question, claim, or case is coming.

**A live frame can end on a question a book chapter would answer.**
Declarative verdicts work in prose meant to be read alone; a frame meant to
be *taught* can leave the verdict open for the room. The instructor changed
"CrowdTangle does not resolve at all. No HTTP conversation happens. Enclosure
completed; nothing left to ask." to "CrowdTangle does not resolve at all. No
HTTP conversation happens. Enclosed, or destroyed?" — same evidence, but the
frame now invites the class to argue the label instead of receiving it. Use
this only where the room genuinely has something to discuss; a frame stating
a fact with no live debate in it should still end on the fact.

**Vertical rhythm beats run-in prose.** Body paragraphs are one or two
sentences, stacked with `\medskip`. A sequence of questions gets one bold
question per line with space between, not a sentence that lists them. When a
right-column block reads as a paragraph, consider whether it wants to be three
stacked one-liners instead.

**Images almost everywhere, memes welcome.** Nearly every concept frame carries
a right-column visual. Pop-culture stills and image-macro memes are in-voice
(*WarGames*, Ben Parker, "this is fine" — the instructor's own revision menu
asks for "image macro memes that connect with the kids"), alongside real
artifacts: court-filing headers, logos, screenshots. Enrichment links to
documentaries and films are welcome (*The Internet's Own Boy*, *The Great
Hack*). Keep placeholder stubs for anything you cannot source; never ship a
diagram where a meme lands better. The instructor demonstrated the trade
directly in week-03: he deleted a full `alertblock` carrying a paragraph of
attribution reasoning (the GitHub-403-in-the-drafting-sandbox anecdote) and
replaced it with a meme image and a five-word caption — the meme carried the
point the paragraph was working to make.

**The register is direct, personal, and occasionally funny.** "Talk to a lawyer
before web scraping a private website that might make rich people mad." "If you
want to be hardcore and use the terminal…" Dry asides, first person, and
plain-spoken verdicts ("Probably!") are the instructor's voice. What is *not*
in-voice: lawyerly hedging, formal transitions, and meta-commentary that
narrates the course to itself. Legal-topic frames get a standing not-legal-advice
disclaimer once per deck.

**Slides carry course operations.** Recurring furniture the spec's chapter-only
structure misses: the daily-note URL and a read-the-chapter reminder on the
Monday→Wednesday transition frame; a "What to submit" frame stating the week's
deliverables and the Sunday-11:59pm / HTML-export mechanics; links to the
handouts and the Missing Manual where students will actually need them. Four
specific pieces of course-operations furniture were introduced across
week-02 and week-03 and are **standing rules going forward, not per-week
choices** — week-05 shipped with none of the four present, and that was a
gap the deck should have caught, not a deliberate simplification. Include
each one where it applies:

- **"Daily note questions" frames on Friday.** When the daily note produced
  questions, answer them in one or two frames of stacked
  `\textbf{Question?} --- answer` one-liners — bold question, dash, short
  plain answer, `\medskip` between. No elaboration beyond the one line; if an
  answer needs more, it belongs in the chapter, not the FAQ frame. Unlike the
  other three items below, this one genuinely can't be written ahead of the
  real questions students submit — a deck authored before class legitimately
  has nothing to put here yet. That is exactly the gap
  `slides/common/check_daily_questions.py` exists to catch: run it against
  the coming week's deck before class and fill the frame in from that week's
  actual daily-note responses, rather than shipping the deck with the frame
  missing, blank, or (from copy-pasting a previous week) duplicated.
- **"Effort over perfection" on the lab-submission frame.** State explicitly
  that the lab is graded on a good-faith attempt to complete, not on getting
  every cell working — week-03's exact phrasing was "Graded on good-faith
  attempt to complete rather than getting everything working." This is a
  grading fact, not a mood; state it as a fact.
- **"Error flavors" on a debugging or lab frame.** Distinguish code that is
  *designed* to break (a guard demonstrating a crash, an intentionally-missing
  field) from code that is *genuinely* broken. Only the second needs a GitHub
  issue. Give students this triage before sending them to file issues, or
  every deliberate crash becomes a duplicate report.
- **A "claim / link / sharpen" taxonomy for comments**, not just claim and
  sharpen. Claim an issue with a sentence on your approach (the comment is the
  claim; the instructor sets the assignee, since students lack write access).
  Sharpen an issue by adding a missing location, reproduction, or scope.
  *Link* two similar issues to each other by commenting with a cross-reference
  — this keeps parallel conversations about the same problem from forking.
  This taxonomy is taught **in full once**, the week it's first needed for a
  real PR/issue workflow (week-03) — later weeks that reuse the same GitHub
  workflow give it a one-line back-reference ("comments still follow Week 3's
  claim / link / sharpen taxonomy") rather than re-teaching the three terms
  from scratch. Re-explaining it every week it's used is not the standing
  rule; citing it briefly is.

**Don't script the instructor's patter.** Cut sentences that perform the
instructor's role — "tell me if a step fails," "you will use this for the rest
of the semester," timing promises. Slides state content; the person at the
front of the room supplies the rest.

**Trim hardest at the very end of the deck.** Both rewrites cut the "Key
takeaways" frame further than any other: week-03 dropped its closing
`\bottomcite` reading list entirely and shortened multi-clause bullets to
short plain statements ("The open-API era ($\sim$2008--2018) was a
**strategic bargain**, not a natural state — and computational social science
was built on the trade" became "a **temporary bargain** around open access to
platform data"). A deck's last frame is not the place to reach for a citation
or a literary flourish it skipped everywhere else — if anything, cut more
there than you did in the body. Frame titles get the same treatment: drop
throat-clearing prefixes ("The take-home — a guided audit in seven steps" →
"A guided audit in seven steps"; "The road from browser to clone" → "Next
week," which also promoted next week's topic from a footnote to the frame's
main content).

## Working alongside the instructor (process)

- **Overleaf is the instructor's editor and it pushes to `main` without
  warning.** Always start from fresh `origin/main`; if a deck was touched in
  the last few days, assume more edits may land mid-branch and rebase rather
  than fight.
- **Never rewrite a frame the instructor authored or reworked** — extend around
  it. If a shipped frame came back rewritten, that rewrite *is* the review
  comment: imitate it in the next deck instead of restoring the old shape.
  Fix outright typos quietly in passing; do not restructure while doing so.
- **A commented-out frame is parked, not rejected.** The instructor cut week-02's
  "Anatomy of a good issue" frame by wrapping every line in `%` rather than
  deleting it — content he may want back, not content he's decided against.
  Leave `%`-commented blocks alone when touching a file; don't delete them to
  "clean up," and don't silently un-comment them either without a signal that
  he wants it back.
- **Image paths come in two dialects.** Overleaf compiles from the repo root,
  so instructor-authored frames say `slides/week-NN/img/foo.png`; local builds
  compile from the week folder and want `img/foo.png`. The preamble's
  `\graphicspath` makes both resolve — do not "fix" one style to the other in
  instructor-authored frames, and never let a deck ship that only builds from
  one directory.

## Citations
**`\bottomcite` is retired — do not use it.** It started as a per-frame
attribution footer, the instructor spent two decks trimming it down (week-02
kept a quarter of its instances, week-03 kept none), and it was removed
outright from all fourteen decks in one pass rather than continuing to argue
over which quarter earns its place. If Overleaf syncs one back in on a frame
you're touching, delete it in passing — that is now a bug, not a style
choice. Anything the line was carrying that is actually worth keeping (a
citable study, a dataset, a ruling) goes as plain text in the frame body, in
the voice of the surrounding prose, not as a separate footer.

`\textcite`, `\cite`, and `\parencite` are still in normal use inline and are
unaffected by this — only cite keys that exist in `slides/common/bibliography.bib`.
The chapter's own `@key` references are safe (they are in that bib) — reuse
those. `grep` to confirm any key before using it; undefined citations are a
build failure.

## Build & verify (must pass before you finish)
From the week folder, run this **twice** (the second pass resolves citations) —
no environment variables needed, since the deck puts `../common/` on the input
path itself:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error week-NN.tex
```

Then confirm all of:
- `week-NN.pdf` exists;
- `grep -ci undefined week-NN.log` returns `0`;
- page count ≥ 15 (`python3 -c "from pypdf import PdfReader; print(len(PdfReader('week-NN.pdf').pages))"`).

If the build fails or any citation is undefined, **fix it and rebuild** until
clean. Never leave a broken deck.

## Code style notes
- Frames containing `lstlisting` **must** use `\begin{frame}[fragile]`.
- `lstlisting` blocks start at column 0 — never indent them to match the
  surrounding LaTeX, because the indentation prints inside the listing. (The
  instructor hit this once restructuring a frame in Overleaf and had to fix it
  in a follow-up commit; save him the round trip.)
- Keep two-column `\begin{columns}[T]` layouts like week-06 for text+image or text+code.
  Default the split to `\begin{column}{0.6\textwidth}` / `\begin{column}{0.35\textwidth}`
  (left/right) unless a frame genuinely needs a different ratio — e.g. a three-column
  comparison, or two columns that must stay visually symmetric.
- Use `\texttt{}` for inline code, package, and file names.
- **Write procedures in Simplified Technical English (ASD-STE100).** Anything a
  student *executes* — lab exercises, in-class activities, setup steps, the
  Friday workflow — follows STE: start each step with an imperative verb, one
  instruction per sentence, 20 words or fewer, active voice, no `-ing` forms,
  no idioms, and no dashes or colons standing in for omitted words. Write
  "Get a Wikipedia table with `read_html`. Then make a visualization." — not
  "Wikipedia table via `read_html` + a visualization."
- **Explanatory prose stays plain, not STE.** Concept frames keep the teaching
  voice: rhetorical questions, deliberate metaphor, and the course's real
  vocabulary (*enclosure*, *proportionality*, *authentication*) are all fine —
  STE's controlled dictionary has no words for this subject. Apply only its
  clarity rules there: keep sentences under 25 words, prefer active voice, and
  cut idioms a non-native reader would miss.
- **Body text is black and white.** Never colorize prose — no
  `\textcolor{tab-blue}{\textbf{...}}` labels, no color-coded key terms, no
  colored block titles. Use `\textbf{}` and `\textit{}` for emphasis and let
  the layout carry the rest. (The `tab-*` colors remain in the palette for
  the theme's own chrome and for `lstlisting` syntax highlighting — not for
  prose.)
- Escape `_`, `#`, `%`, `&`, `$` in prose; inside `lstlisting` they are literal.
- **Matplotlib: object-oriented interface only.** Any plotting code shown in a
  deck uses `fig, ax = plt.subplots()` and calls methods on `ax`
  (`ax.plot(...)`, `ax.set_xlabel(...)`, `ax.set_title(...)`) — never the
  implicit pyplot state-machine (`plt.plot(...)`, `plt.xlabel(...)`,
  `plt.title(...)`). The OO interface is explicit about which figure/axes
  it's drawing to, which is what a slide's necessarily-short snippet should
  model, and it's the interface [Matplotlib's own docs recommend for
  anything beyond a one-off interactive
  plot](https://matplotlib.org/stable/tutorials/lifecycle.html) (see also
  [pyplot vs. object-oriented
  interface](https://matplotlib.org/matplotblog/posts/pyplot-vs-object-oriented-interface/)).
  `plt.subplots()` itself is the one acceptable `plt.` call — it's how you
  obtain the `fig`/`ax` objects in the first place.
