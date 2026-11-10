# Week 10's saved copies (checkpoints)

Made by `lab-10-key.ipynb`'s own code on the run its key note describes, and read by the lab from this folder's raw address on `main`. Each lets a student go on when a request was refused, or start a day without the earlier days' kernel.

| File | Made by | What it holds |
|---|---|---|
| `revisions.csv` | Step 5 | Every edit to *University of Colorado Boulder* up to 2026-09-30T23:59:59Z, oldest first: `timestamp`, `size`, `anon` and `temp` (True when the edit came from an IP address or a temporary account), and `editor`, a number for each editor in the order of their first edit (1 is the article's first editor; 0 is an edit whose username Wikipedia has hidden). |
| `daily-views.csv` | Step 9 | Daily views by people (`agent` `user`), 2021-01-01 to 2026-09-30, as the pageviews API returned them. |
| `by-agent.csv` | Step 13 | Monthly views for each agent (`user`, `spider`, `automated`), January 2024 to September 2026. |
| `links.csv` | Step 15 | The article's wikilinks (`prop=links`): namespace and title. |
| `backlinks.csv` | Step 15 | The pages in namespace 0 that link to the article (`list=backlinks`), redirects included (`redirect` is set for those). |

**Privacy.** The revisions table holds no usernames, IP addresses, edit summaries or revision IDs: Step 5's given cell drops them before saving, because a published file shouldn't carry a private person's name or address (`AGENTS.md`, "Images and privacy"), and edit summaries often name other editors or IP addresses. The editor numbers let a student count editors and the top ten's share without naming anyone. The other files hold article titles and counts only.
