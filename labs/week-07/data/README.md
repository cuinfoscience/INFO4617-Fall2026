# Week 7's saved copies (checkpoints)

Read by `lab-07.ipynb` from this folder's raw address on `main`. Each lets a student go on when the Internet Archive refuses a request: thirty people behind one campus address share its allowance.

**Not made yet.** All four hold answers from `web.archive.org`, which refused the course's cloud machine on 2026-10-21 and again on 2026-11-17, when the lab was rebuilt (issue #197 collects the laptop runs). Until the files are here, the four loading cells in the lab would stop with a 404; they are commented out, and no setup step needs them.

To make them, run the key from a laptop with `labs/tools/run_key.py`, then run the key once more in JupyterLab with one line added at the end of each cell below, and commit the four files here. Write the date of that run in this file, in place of this paragraph.

| File | Made by | The line to add | What it holds |
|---|---|---|---|
| `cnn-three-eras.csv` | Step 5, the given loop that builds `comparison` | `comparison.to_csv("cnn-three-eras.csv", index=False)` | CNN's home page in August 2000, 2012 and 2024: the year asked for, the capture's own timestamp, and four counts. |
| `cdx-facebook-terms.json` | Step 7, the cell that makes `terms_rows` | `json.dump(terms_rows, open("cdx-facebook-terms.json", "w"))` (after `import json`) | The CDX Server's answer for `facebook.com/terms` up to 2026-09-30, status 200, collapsed on digest: a header row, then one row per capture. |
| `cdx-facebook-2005.json` | Step 9, the cell that makes `fb2005_rows` | `json.dump(fb2005_rows, open("cdx-facebook-2005.json", "w"))` | The CDX Server's answer for `facebook.com` in 2005, unfiltered: a header row, then each capture's timestamp and status code. |
| `facebook-terms-versions.json` | Step 11, the given cell that reads `wayback_cache/` back into `results` | `json.dump(results, open("facebook-terms-versions.json", "w"))` | Ten versions of Facebook's Terms of Service, one for the start of every other year from 2006 to 2024: each capture's timestamp, its `id_` address, its number of words, and its text. |

**Privacy.** The files hold public pages and capture metadata: no usernames, handles or addresses of private people. Check the ten versions' text once, when the file is made, for a name that isn't a company's or an officer's.
