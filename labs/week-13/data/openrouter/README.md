# Step 10's two tables, 2026-11-18

The week 13 lab's two seven-report tables, saved so that a student whose loop stops (a 429 from every free model, an answer with no content, or the day's limit) can go on from the key's. Each was made by the given loop of Step 10 in `labs/week-13/lab-13-key.ipynb`, on 2026-11-18, through OpenRouter, from the book's saved Markdown of the seven year-end reports (`data/ch-13/` in the textbook).

| File | What it holds |
|---|---|
| `seven-reports-instruction.csv` | The first loop: `extract_totals()` with `INSTRUCTION`, the schema in `response_format` only. Right in all four fields for 4 of 7 reports (2020 to 2023). |
| `seven-reports-with-schema.csv` | The second loop: the same, with `with_schema`, the schema added to the instruction as text. Right in all four fields for 7 of 7. |

One row per report. `month`, `year`, `total_prior` and `total_current` are the model's answer; `model` is the model that gave it (`nvidia/nemotron-3.5-super-vl:free` for every row); `prior_ok`, `current_ok`, `year_ok` and `month_ok` compare the answer with week 9's figures (`TRUTH`), the year in the report's name, and December.

A rerun won't necessarily match: which free model answers, and what it gets wrong, change from run to run.
