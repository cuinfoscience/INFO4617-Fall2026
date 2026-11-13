# Images for `week-14`

`make_stubs.py` draws a gray placeholder for every image listed in `stubs.tsv`
that does not exist yet, so the deck compiles. Replace a placeholder with the
real image under the same file name, then write below where it came from, how
it was made, and the date. The script rewrites only the table between the two
markers.

## Listed in `stubs.tsv`

<!-- stubs:begin: generated from stubs.tsv by slides/common/make_stubs.py; edits between these markers are replaced -->
| File | Size | Should show |
|---|---|---|
| `run-workflow.png` | 1600x1000 | Screenshot (a person's, signed in; redact the account name and avatar): a boulder-forecast repository's Actions tab, "Collect Boulder's hourly forecast" selected, the Run workflow menu open with branch main and the green Run workflow button |
| `failed-run.png` | 1600x1000 | Screenshot: a failed run of "Collect Boulder's hourly forecast" (red X), job collect, the step "Collect the forecast" open at requests.exceptions.HTTPError: 404 Client Error, and "Commit the new rows" skipped |
<!-- stubs:end -->

## Notes

The deck rebuilt for chapter 14's rewrite, *Automating Data Collection*
(2026-11-13: the National Weather Service's hourly forecast for Boulder,
collected by a GitHub Actions workflow), replaces the old Selenium and Rotten
Tomatoes deck. That deck's five images (`pipeline_diagram.png`,
`score_timeseries.png`, `actions_run_log.png`, `crontab_guru.png`,
`pr_review.png`) were all gray placeholders, never replaced with real images,
and were deleted with their `stubs.tsv` rows. The week's pipeline on the "This
week at a glance" frame is drawn in TikZ in `week-14.tex`.

**Placeholders** (2026-11-13). Both wait for a real capture:

- `run-workflow.png` (Wednesday, "Step 5: start the first run", at the full
  0.6 column). The **Run workflow** menu shows only to an account that can
  write to the repository, so this is a person's screenshot, taken signed in:
  it goes through the textbook's `tools/shots/run import` (`mode: hand`),
  which blacks out the account's name and avatar, and is then synced here.
- `failed-run.png` (Friday, "Step 11: break your collector", at the full 0.6
  column). A run made to fail as Step 11 says (`hourly` changed to
  `hourlyy`). The log of a public repository's run can be read signed out,
  so the textbook's `tools/shots` can capture it once such a run exists.

**`slides/week-02/img/this-is-fine.jpg`** (Friday, "Quiet failures") is week 2's
image, used by its path from the repository's root, as week 7 does. It is not
copied here or listed in `stubs.tsv`; its source is in week 2's `IMAGES.md`.

## Sources for the hosted-scheduler table

Friday's "Other places to run a schedule" frame. Each free tier was read on its
provider's own page on 2026-11-13:

| Service | Free tier on the slide | Source |
|---|---|---|
| GitHub Actions | Free in public repositories; every 5 minutes at most | <https://docs.github.com/en/billing/concepts/product-billing/github-actions> ("Standard GitHub-hosted runners in public repositories" stay free); <https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule> ("once every 5 minutes"; UTC by default; delays at the start of every hour; disabled in a public repository after 60 days without activity) |
| GitLab scheduled pipelines | 400 compute minutes a month; 24 runs a day per schedule | <https://about.gitlab.com/pricing/> ("400 compute minutes per month"); <https://docs.gitlab.com/user/gitlab_com/> ("Maximum pipelines for each schedule": 24 for the Free tier; cron at most `*/5`) |
| PythonAnywhere scheduled tasks | None on free accounts made since January 2026 | <https://help.pythonanywhere.com/pages/ScheduledTasks/> (scheduled tasks work "in paid accounts or free accounts created before 2026-01-15", 2026-01-08 on the EU system; such a free account gets one daily task); <https://www.pythonanywhere.com/pricing/> (Beginner: no scheduled tasks) |
| Cloudflare Workers Cron Triggers | 5 cron triggers; 10 ms of CPU a run | <https://developers.cloudflare.com/workers/platform/limits/> (Free plan: 5 Cron Triggers per account, 10 ms CPU per Cron Trigger invocation, 100,000 requests a day); <https://developers.cloudflare.com/workers/configuration/cron-triggers/> (a Worker's `scheduled()` handler, examples in JavaScript, TypeScript and Python; UTC) |
| Google Cloud Scheduler | 3 jobs a month per billing account | <https://cloud.google.com/scheduler/pricing> ("Each Google billing account gets 3 jobs per month free"; then $0.10 per job a month) |
| Val Town | Every 15 minutes at most | <https://docs.val.town/vals/cron/> ("Crons can run up to once every 15 minutes on a Free account") |

Vercel Cron Jobs were checked too and left out to keep the table short: on the
Hobby plan they run once a day at most
(<https://vercel.com/docs/cron-jobs/usage-and-pricing>).
