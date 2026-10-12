# Images for `week-09`

All nine of the deck's images are real as of 2026-10-12. Six are copies made by
the textbook's `tools/shots` (listed under "Copied by tools/shots" below); the
other three are recorded here. Text in each reaches 16 pixels on a slide shown
1,920 pixels wide (`slides/common/AUTHORING.md`), at the width its frame shows
it.

## How the images were made

- `council_minutes_pdf.png` -- page 1 of the City Council's signed minutes
  for Thursday, December 5, 2024: the masthead, "MINUTES", the roll call
  ("Council Members present:" and "Virtually present:"), and the first
  motion's row. (The web's filing cabinets)
  - A render of the textbook's saved copy,
    `data/ch-09/council-minutes-2024-12-05.pdf` (hash in its
    `manifest.csv`), made 2026-10-12 with Poppler's `pdftoppm` 24.02.0:
    `pdftoppm -f 1 -l 1 -r 200 -x 153 -y 389 -W 1306 -H 861 -png
    -singlefile`, which is PDF points 55--525 across and 140--450 down.
  - The page names only council members, who are public officials; nothing
    on it names a member of the public.
  - Its text is 12 points. The frame's 40% column shows the 470-point crop
    672 pixels wide, so the text comes to 17 pixels. A 35% column would show
    it at 15.
  - It is the same page as the chapter's precision-and-recall example: the
    list of names wraps, and a member is listed as present virtually.
- `attendance_chart.png` -- members present at the roll call of each of the
  13 saved minutes (December 2000, 2018--2024), counted by hand (dark bars),
  beside what the slide's `extract_attendance()` returns (light bars).
  (Case study 1: the obvious regex)
  - Drawn 2026-10-12 by `attendance_chart.py` (in this folder) with
    matplotlib 3.11.2 and pypdf 6.20.1:
    `python -I attendance_chart.py PATH/TO/data/ch-09 attendance_chart.png`,
    with `data/ch-09` from the textbook.
  - By hand: the members listed at roll call on page 1, in the room or
    online, with the presiding mayor; a member who arrived later is not
    counted. 2000-12-05: 8; 2000-12-19: 7; 2018-12-04: 8; 2019-12-03: 9;
    2020-12-01 and 2020-12-15: 8; 2021-12-14: 8; the six meetings from
    2022-12-01 to 2024-12-19: 9. Votes recorded right after roll call (8:0,
    9:0) agree.
  - The slide's regex finds no "Present:" line in the seven meetings before
    2022, whose minutes say "were present" or "Those present were", and only
    5 of 9 names in the six after, because the list wraps onto a second line.
- `pr_suggestion.png` -- a review suggestion on textbook PR #228, the
  instructor's demonstration pull request, with **Apply suggestion**.
  (Improving Chapter 9 together)
  - A byte-for-byte copy of `slides/week-08/img/pr_suggestion.png`, itself a
    copy of `handouts/week-08/img/pr-suggestion.png`, which the instructor
    captured on 2026-10-06, signed in; its `IMAGES.md` records the capture.
  - Its code is 12 pixels, so the frame shows it in a 62% column, where the
    code comes to 16.4 pixels.

## Removed

`pr_review.png`, a gray placeholder for a GitHub "Files changed" view, was
deleted with its `stubs.tsv` row on 2026-10-12. Weeks 7 and 8 dropped theirs
the same way; the Friday frame uses `pr_suggestion.png`.

`extraction_pipeline.png` and its source, `extraction_pipeline.dot`, were
deleted with their `stubs.tsv` row on 2026-10-12, when the "Scale it" frame was
cut. Chapter 9 no longer builds a corpus pipeline; Wednesday's case studies use
`open_comment.png` and `sales_use_tax.png` instead.

## Copied by tools/shots

Widths of the copies, on a 1,920-pixel slide: `missing_totals_row.png`
and `sales_use_tax.png` sit in 50% columns, 840 pixels, so their 16-pixel text
(in an 800-pixel frame) comes to 16.8; `open_comment.png` in a 48% column, 16.1;
`ocr_confidence.png` in a 46% column, where its 20-pixel figures come to 19.3.

<!-- shots:begin: copies from the textbook's tools/shots, generated from shots.json; edits between these markers are replaced -->
Copied here by the textbook's `tools/shots/run sync`; `tools/shots/run synced` checks them.

| File | Copy of | Captured | Source | How |
|---|---|---|---|---|
| `documentcloud.png` | `course/week09-documentcloud` (tools/shots/out/course/week09-documentcloud/20261012T180809Z.png, textbook `f5042a5`) | 2026-10-12 | https://www.documentcloud.org/home/ | tools/shots: Google Chrome for Testing 154.0.8037.92, 480×600 at 2× |
| `missing_totals_row.png` | `ch-09/missing-totals-row` (images/ch-09/missing-totals-row.png, textbook `5b3caf2`) | 2026-10-06 | https://documents.bouldercolorado.gov/WebLink/ElectronicFile.aspx?docid=194397&dbid=0&repo=LF8PROD2 | Claude Code: rendered with pdfplumber 0.11.10; imported by tools/shots |
| `ocr_confidence.png` | `ch-09/ocr-confidence` (images/ch-09/ocr-confidence.png, textbook `5b3caf2`) | 2026-10-06 | https://documents.bouldercolorado.gov/WebLink/ElectronicFile.aspx?docid=194397&dbid=0&repo=LF8PROD2 | Claude Code: rendered with pytesseract 0.3.13 with Tesseract 5.5.3; imported by tools/shots |
| `open_comment.png` | `ch-09/open-comment` (images/ch-09/open-comment.png, textbook `1743581`) | 2026-10-12 | https://documents.bouldercolorado.gov/WebLink/Browse.aspx?id=194345&dbid=0&repo=LF8PROD2 | Claude Code: rendered with matplotlib 3.11.2 with pypdf 6.20.1; imported by tools/shots |
| `pdf_drawing_instructions.png` | `ch-09/pdf-objects` (images/ch-09/pdf-objects.png, textbook `74a950a`) | 2026-10-06 | https://documents.bouldercolorado.gov/WebLink/ElectronicFile.aspx?docid=194397&dbid=0&repo=LF8PROD2 | Claude Code: rendered with pdfplumber 0.11.10; imported by tools/shots |
| `sales_use_tax.png` | `ch-09/sales-use-tax` (images/ch-09/sales-use-tax.png, textbook `1743581`) | 2026-10-12 | https://documents.bouldercolorado.gov/WebLink/Browse.aspx?id=194345&dbid=0&repo=LF8PROD2 | Claude Code: rendered with matplotlib 3.11.2 with pdfplumber 0.11.10; imported by tools/shots |
<!-- shots:end -->
