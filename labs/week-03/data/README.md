# Week 3's saved copies (checkpoints)

Read by `lab-03.ipynb` from this folder's raw address on `main`. Each lets a student go on when a site refuses a request, or start Friday without Wednesday's kernel.

| File | Made from | What it holds |
|---|---|---|
| `access.csv` | Step 4's given loop, as `lab-03-key.ipynb` ran it on 2026-10-21 at 21:56 UTC, from a cloud machine | The access matrix: one row for each of the chapter's eight endpoints, with its status code, verdict, content type, and `x-ratelimit-limit` header, and the time of the audit. Step 4's fallback cell and Friday's setup step (Step 6) load it; Step 6 says how to load a student's own copy from Wednesday instead. |
| `servers.csv` | The given loop of the after-class Mastodon step (Step 9 until 2026-11-18), in the same run | Six Mastodon servers: the number of accounts each reported, the status code of its public timeline for an anonymous request, and the time of the audit. That step's fallback cell loads it. |

**How they were made.** Each file is the table its loop printed in full in the key's run of 2026-10-21, copied to CSV on 2026-11-17 from the key's saved output, with the `audit_date` column that the lab's saving cells add. No value was typed by hand. The loops weren't run again on 2026-11-17: several of their hosts' `robots.txt` files disallow the lab's paths to automated clients, and that run was automated. When the instructor runs the key from a laptop, the saving cells under each loop write new copies; replace these files with them, and change the dates in the lab's loading cells and in this table.

**What a saved copy changes.** In a table read from `access.csv`, `rate_limit` is a number (`300.0`) or empty (`NaN`); in a table the loop makes, it is the header's text (`"300"`) or `None`. The statuses are the cloud machine's on one afternoon: a laptop on campus, on another day, may get different ones, which is the lab's point.

**Privacy.** Both files hold services' and servers' names, status codes, content types and counts. Neither holds a person's name, username or address.
