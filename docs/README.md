# Project documentation

Process artifacts for this repo that aren't course content — currently just
after-action reports.

- `aar/` — after-action reports on the slide decks, one file per review,
  named `YYYY-MM-DD-<scope>.md`. Each report compares what
  `slides/common/AUTHORING.md` (and the shipped decks) says should happen
  against what actually happened, root-causes any gap, and turns findings
  into concrete revisions with a tracking table. When a finding gets
  resolved, update that report's tracking table and add a dated resolution
  note rather than deleting or rewriting the original findings — the report
  is a record of what was decided and why, and a later AAR checks it to see
  whether a revision actually stopped the pattern from recurring.
