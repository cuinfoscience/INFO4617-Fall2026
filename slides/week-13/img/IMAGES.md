# Images for `week-13`

`make_stubs.py` draws a gray placeholder for every image listed in `stubs.tsv`
that does not exist yet, so the deck compiles. Replace a placeholder with the
real image under the same file name, then write below where it came from, how
it was made, and the date. The script rewrites only the table between the two
markers.

## Listed in `stubs.tsv`

<!-- stubs:begin: generated from stubs.tsv by slides/common/make_stubs.py; edits between these markers are replaced -->
| File | Size | Should show |
|---|---|---|
| `lead-similarity.png` | 1680x1110 | Chart: cosine similarity of each January 1 Wikipedia lead (Obama, Clinton, Trump, Biden, Harris), 2004-2026, to the article's current lead, drawn from labs/week-13/data/wikipedia/ as the lab key's Step 12 computes it |
<!-- stubs:end -->

## Notes

The deck rebuilt for chapter 13's rewrite, *AI APIs as Data Tools*
(2026-11-07), used no image files: the week's pipeline on the "This week at a
glance" frame is drawn in TikZ in `week-13.tex`. The old deck's five
placeholders (`chat_api_request.png`, `model_comparison.png`,
`embeddings_heatmap.png`, `token_pricing.png`, `pr_review.png`) were never
replaced with real images, and were deleted with their `stubs.tsv` rows.

**`lead-similarity.png`** (2026-11-09) is a render of the lab's own data, not a
screenshot. `make_lead_similarity.py`, beside it, loads
`labs/week-13/data/wikipedia/lead-vectors.npy` and `lead-vectors-rows.csv`
(the vectors the lab key's Step 12 embeds, from
`nvidia/nemotron-3-embed-1b:free` on 2026-11-09, saved for its fallback
cell), checks that their rows line up with `leads.csv`, and computes each
lead's cosine similarity to its article's current lead and the year × article
table exactly as Step 12 of `labs/week-13/lab-13-key.ipynb` (commit d679ddb)
does. Its table matches the key's printed table to three places. The plot is
the key's line chart restyled for a slide: larger type, ticks every four
years, no title (the frame has one), and a different marker for each article,
because the default colors for Trump and Clinton are hard to tell apart for
readers with red-green color blindness. Chapter 13's `@fig-lead-similarity`
("Similarity Over Time") draws the same data. Rebuild it from the repository
root with:

```bash
python3 -I slides/week-13/img/make_lead_similarity.py labs/week-13/data/wikipedia/ slides/week-13/img/lead-similarity.png
```

**Used on** (Friday): "Step 12: twenty-three years of leads", at 0.6 of the
text width.
