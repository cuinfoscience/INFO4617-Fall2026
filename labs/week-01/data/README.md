# Lab 01's saved copies

| File | What it is | Made |
|---|---|---|
| `jan2026.json` | The pageviews API's whole answer for the chapter's article, University_of_Colorado_Boulder, daily from 20260101 to 20260131 (`all-access`, `all-agents`): 31 items | 2026-11-18, by the key's own Step 3 request (`month_response.text`; Step 2 since the fix pass of 2026-11-18), saved unchanged |
| `universities-2025.csv` | Daily pageviews in 2025 for the four universities of Step 8's loop, as `get_daily_views()` returns them, one row per day per article: `date`, `article` (University_of_Colorado_Boulder, Colorado_State_University, University_of_Denver, Colorado_School_of_Mines) and `views` (`all-access`, `all-agents`): 1,460 rows | 2026-11-18, by the key's own `get_daily_views()`, on the run its key note describes, right after Step 8's loop |

Step 2's given cell loads `jan2026.json` only when the live request stopped, such as on a 429 from Wikimedia. The given cells under Step 7's year and Step 8's loop load `universities-2025.csv` the same way. They hold counts for articles, and no person's name, username or address.
