# Week 4's saved copies (checkpoints)

Saved by `lab-04-key.ipynb`'s run of 2026-11-17, and read by the lab from this folder's raw address on `main`. Each lets a student go on when a site refuses a request, or start a day without the earlier days' kernel.

| File | Made by | What it holds |
|---|---|---|
| `MemberData-2026-11-03.xml` | Step 2, `roster.content`, byte for byte | The roster of the U.S. House of Representatives as the Office of the Clerk published it at `https://clerk.house.gov/xml/lists/MemberData.xml` with `publish-date="November 3, 2026"`: 441 `<member>` blocks, 2 of them vacant seats. Part 2's setup step loads it, so Wednesday's counts don't change when the Clerk updates the live file. |
| `power-boulder-2025.json` | Step 12, `year_response.text` | NASA POWER's answer for the daily high, low and precipitation at 40.01, -105.27 for the whole of 2025. A past year, so a new request gives the same values. |

**What a saved copy changes.** GitHub serves both files as `text/plain; charset=utf-8`. So a student who loads the roster from here in Step 2 sees `utf-8` where the Clerk's server makes `requests` guess `ISO-8859-1`, and Step 3's microsprint finds no garbled names. The loading cell says so.

**Privacy.** The roster is a public record of public officials: members' names, parties, districts, committee assignments, and their offices' rooms and telephone numbers in the House office buildings, as the Clerk publishes them. It holds no private person's name or contact details. The weather file holds no names at all.
