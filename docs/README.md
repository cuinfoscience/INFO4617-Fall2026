# Project documentation

Process artifacts for this repo that aren't course content: after-action
reports, and the plans that come out of them.

- `aar/` — after-action reports, one file per review, named
  `YYYY-MM-DD-<scope>.md`. Each report compares what the written rules (such as
  `slides/common/AUTHORING.md`) and the shipped work say should happen against
  what actually happened. It root-causes any gap and turns findings into
  concrete revisions with a tracking table. When a finding gets
  resolved, update that report's tracking table and add a dated resolution
  note rather than deleting or rewriting the original findings — the report
  is a record of what was decided and why, and a later AAR checks it to see
  whether a revision actually stopped the pattern from recurring.
- `plans/` — plans for larger pieces of work that an AAR recommends, named
  `YYYY-MM-DD-<topic>.md`. Each plan names the AAR revision it implements. A
  plan records a proposal and the decisions behind it; once work starts,
  progress goes in the AAR's tracking table, not in the plan.

Current contents:

| File | What it is |
|---|---|
| `aar/2026-09-21-week-06-slides.md` | Slide-authoring contract vs. weeks 04–05; week-06 expansion |
| `aar/2026-09-24-screenshots.md` | Screenshots, editing, and annotation in ch-07–08, weeks 07–08, and the week-06 handout |
| `plans/2026-09-24-screenshot-toolkit.md` | A screenshot toolkit for the textbook repo (`tools/shots/`) |
| `plans/2026-09-24-screenshot-backfill-ch01-05.md` | Using the toolkit to back-fill chapters 1–5, their slides, and handouts |
