# Images for the week-06 Oscars handout

Both figures in `oscars-cards-to-rows.pdf` and its notebook are **real
screenshots** of <https://www.oscars.org/oscars/ceremonies/2026>, captured
2026-09-24.

## How they were made

Chrome for Testing 154 driven by Selenium 4.49 on a virtual display (Xvfb),
captured with ImageMagick. The page was loaded with an identifying
`User-Agent` (`INFO4617-course-materials/1.0 (contact: accounts@brianckeegan.com)`),
and only necessary cookies were accepted. The DevTools panel was operated
with real clicks (xdotool), not mocked up.

- `oscars_card.png` (1120x1190) -- the Actor in a Leading Role card and the
  top of the next card, rendered at device scale factor 2 for print. Figure 1.
- `oscars_devtools.png` (1040x824) -- Chrome DevTools, Elements panel,
  docked at the bottom and zoomed to 175%, after right-click > Inspect on
  MICHAEL B. JORDAN. The film's `<div class="field">` was opened with one
  click, and then Inspect was repeated so that the name stays selected.
  Figure 2.

## The annotated versions

The numbered markers and braces are drawn with TikZ, not painted into the
screenshots: `oscars_card_annotated.tex` and `oscars_devtools_annotated.tex`
place them in pixel coordinates of the screenshot, with the marker styles
from `../../common/handoutmarkers.sty`. `make figures` in `handouts/` builds
each one twice: `*_annotated.pdf` (vector, for the PDF handout) and
`*_annotated.png` (250 dpi, embedded in the notebook). If you retake a
screenshot, move the coordinates too.

## What the live page does that the HTML does not

In the browser, a script hides every "Nominees" label after the first one
(`style="display: none;"` on nominees 2 to 4). The HTML that `requests`
receives has the label on every nominee, which is why each row in the
handout's DataFrame gets `Nominees`. Step 9 of the handout says this.
