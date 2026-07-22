# Lecture slides

Weekly lecture decks for INFO 4617 Web Data Science, one folder per teaching
week. Each deck covers the full week on the course's Monday/Wednesday/Friday
rhythm:

- **Monday** — introduce the week's concept and its companion notebook
- **Wednesday** — a hands-on notebook lab working the chapter's code and exercises
- **Friday** — propose and peer-review revisions to the [Web Data Science textbook](https://github.com/cuinfoscience/Web-Data-Science-Book)

Decks are grounded chapter-by-chapter in the textbook (and draw on the prior
offering's slides). Week 15 has no deck (Fall Break); Week 1 is a shorter
Friday-only intro, and Week 16 covers research design plus final presentations.

| Week | Topic | Chapter |
|---|---|---|
| 01 | Introduction & setup | 1 |
| 02 | Ethics, law & responsible collection | 2 |
| 03 | The post-API age | 3 |
| 04 | Data formats: XML & JSON | 4 |
| 05 | Web architecture & protocols | 5 |
| 06 | Parsing static web pages | 6 |
| 07 | Archived web pages & the Wayback Machine | 7 |
| 08 | Dynamic web pages with Selenium | 8 |
| 09 | Extracting data from PDFs | 9 |
| 10 | Wikipedia APIs (project proposal due) | 10 |
| 11 | Government data APIs | 11 |
| 12 | Social & media platform APIs | 12 |
| 13 | AI & language-model APIs | 13 |
| 14 | Automating data collection | 14 |
| 16 | Research design & final presentations | 15 |

## Layout

```
slides/
  common/     shared Gotham theme (vendored), preamble.tex, bibliography.bib,
              make_stubs.py, AUTHORING.md
  week-NN/    slides.tex, slides.pdf, img/ (stub PNGs + IMAGES.md)
  Makefile
```

## Building

Requires a TeX Live install with `beamer`, `fbb`, `expl3`, `biber`, and
`latexmk` (the Gotham theme is vendored in `common/`, so no separate theme
install is needed).

**Each deck compiles standalone.** Open `week-NN/slides.tex` in your editor and
build it, or from inside the folder run:

```bash
cd week-06 && latexmk -pdf slides.tex
```

No `TEXINPUTS` or other environment setup is needed: each `slides.tex` adds
`../common/` to LaTeX's input path itself (the line right after
`\documentclass`), so the shared theme, preamble, and bibliography resolve
automatically. This assumes you compile from within the week's own folder,
which is what editors do by default.

The `Makefile` is a convenience for building everything at once:

```bash
make            # build every deck
make week-06    # build one week
make stubs      # regenerate placeholder images
make clean      # remove build artifacts (keeps slides.pdf)
```

## Images

The `img/*.png` files are **placeholders** — gray boxes labeled with what each
one should show. Replace them with real screenshots/figures (keeping the same
filename) and rebuild. Every folder's `img/IMAGES.md` lists what belongs where.
The manifest `img/stubs.tsv` regenerates the placeholders via
`common/make_stubs.py`.
