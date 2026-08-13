# Canvas migration

Tooling to migrate the Fall 2024 course (`INFO 4871`, Canvas course **109074**)
into the Fall 2026 course (`INFO 4617`, Canvas course **143304**) and reshape it
to match the current syllabus.

- `course_spec.py` — declarative spec of the target course: teaching calendar,
  assignment groups and weights, weekly assignments, module layout, and the
  syllabus page. Derived from `syllabus/syllabus.tex` and `slides/`.
- `migrate.py` — the tool that makes Canvas match the spec.

## Get a token

Canvas → **Account → Settings → Approved Integrations → + New Access Token**.
Give it an expiry you're comfortable with and copy the value (Canvas shows it
once).

```bash
export CANVAS_TOKEN='<paste your token>'
# or: python migrate.py inspect --token-file /path/to/canvas_key.json
```

## Run it

Every command is a **dry run by default** — it makes only `GET` requests and
prints the writes it would perform. Add `--apply` to actually write.

```bash
cd canvas

python migrate.py inspect              # read-only survey of both courses
python migrate.py copy                 # preview the content migration
python migrate.py copy --apply         # copy files + pages from the old course
python migrate.py build                # preview groups/assignments/modules/syllabus
python migrate.py build --apply        # build the new structure
```

Recommended order: `inspect` first (see what's actually in both courses), then
`copy --apply`, then `build --apply`.

### Options

| Flag | Effect |
|---|---|
| `--apply` | Actually write to Canvas (default: dry run) |
| `--only groups,assignments,modules,syllabus,settings` | Limit what `build` touches |
| `--include-slides` | Upload each `slides/week-NN/slides.pdf` and link it in that week's module |
| `--everything` | `copy`: bring over the **entire** old course, not just files/pages |
| `--host` | Canvas host (default `canvas.colorado.edu`) |
| `--snapshot PATH` | Where `inspect` writes its JSON dump |

## What `copy` does

Runs a Canvas `course_copy_importer` content migration from 109074 → 143304.

By default it is **selective: files and pages only**. The old course's
assignments, modules, and groups follow the 2024 design (Attendance 15% /
Module Assignments 60% / Final 25%) and would collide with the new 30/30/40
structure, so they are deliberately left behind and rebuilt fresh by `build`.
Use `--everything` if you'd rather bring it all over and prune by hand.

## What `build` does

| Step | Result |
|---|---|
| `settings` | Course name/code, term dates (Aug 20 – Dec 4, 2026), weighted grading on, home page = Modules |
| `groups` | Notebook Labs **30%** (drops 2 lowest), Textbook Revisions **30%**, Final Project **40%** |
| `assignments` | 13 labs (due Wednesdays), 13 revisions (due Fridays), 3 final-project items — 29 total, all with due dates in `America/Denver` |
| `modules` | One module per week (1–16, no 15) laid out Monday → Wednesday → Friday, with the chapter reading, slides, companion notebook, and that week's two assignments |
| `syllabus` | Canvas syllabus page styled to match the PDF syllabus, including the 16-week schedule table |

The calendar honors the CU Boulder Fall 2026 academic calendar: Week 1 meets
Friday only, no class Labor Day (Sep 7) or Fall Break (Nov 23–27), and Dec 4 is
the last day of class.

## Safety notes

- **Idempotent by name.** Re-running updates existing groups/assignments rather
  than creating duplicates. Existing modules are left alone rather than having
  items appended twice.
- **Nothing is deleted.** Leftover assignment groups from the old design are
  reported so you can remove them in Canvas yourself.
- Assignments are created **published**. If you'd rather stage them, change
  `"published": True` in `build_assignments`.
