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

python migrate.py plan                 # print the whole target design (no token, no network)
python migrate.py inspect              # read-only survey of both courses
python migrate.py copy                 # preview the content migration
python migrate.py copy --apply         # copy files + pages from the old course
python migrate.py build                # preview groups/assignments/modules/syllabus
python migrate.py build --apply        # build the new structure
python migrate.py labs                 # preview: each week's lab and lab-key links, in its Wednesday lab
python migrate.py labs --apply         # add them to the modules that already exist
```

Recommended order: `plan` to review the design, `inspect` to see what is actually
in both courses, then `copy --apply`, then `build --apply`.

### Options

| Flag | Effect |
|---|---|
| `--apply` | Actually write to Canvas (default: dry run) |
| `--only groups,assignments,rubrics,modules,syllabus,settings` | Limit what `build` touches |
| `--overwrite` | `build`: also update assignments that already exist (by default they are reported, not changed) |
| `--include-slides` | Upload each `slides/week-NN/week-NN.pdf` and link it in that week's module |
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
| `groups` | Notebook Labs **30%** (drops 2 lowest), Textbook Revisions **15%**, Attendance **15%**, Final Project **40%** (proposal 30, presentation 60, repository and write-up 150 points), as in the syllabus. Canvas weights the assignments inside a group by their points, so the three parts keep the syllabus's 5 / 10 / 25 split only while their points stay in that ratio |
| `assignments` | 12 labs (10 points each), 12 Textbook Revisions (weeks 2–9 at 1 point each, credit or no credit; weeks 11–14 are 2-point project-portfolio checkpoints; week 10 has neither a lab nor a revision), 3 final-project items, and 15 attendance entries; labs and revisions are due Sundays, in `America/Denver`. Creates the ones that are missing; an assignment that already exists is left as it is, and the dry run lists how it differs from the spec (points, due date, submission types), unless you pass `--overwrite` |
| `rubrics` | Attaches each rubric in `RUBRICS` to the assignments it lists, for grading: the proposal's 10 criteria at 3 / 2 / 1 / 0 points (30 total), and the Notebook Lab rubric's 5 criteria at 2 / 1 / 0 (10 total) on weeks 11–14, a 2-point rubric on each week 11–14 portfolio checkpoint, and the presentation (60) and repository and write-up (150) rubrics. A rubric is created once and shared by its assignments. An assignment that already has a rubric is left alone |
| `modules` | One module per week (1–16, no 15) laid out Monday → Wednesday → Friday, with the chapter reading, slides, companion notebook (followed by the week's lab and lab key, when `labs/week-NN/` has one), and that week's two assignments |
| `syllabus` | Canvas syllabus page styled to match the PDF syllabus, including the 16-week schedule table |

The calendar honors the CU Boulder Fall 2026 academic calendar: Week 1 meets
Friday only, no class Labor Day (Sep 7) or Fall Break (Nov 23–27), and Dec 4 is
the last day of class.

## What `labs` does

`build` leaves an existing module's items alone, so a lab added after its
module was built needs `labs`. For every week with a lab on `main`
(`labs/week-NN/lab-NN.ipynb`), it finds the week's module by name and adds two
links right after the `Companion notebook:` item in its Wednesday section
(after the `Slides:` item in week 1, which meets Friday only): **Lab:
lab-NN.ipynb** and **Lab key: lab-NN-key.ipynb**, both to the files on GitHub,
and publishes them (Canvas
creates a module item unpublished whatever the request says). A link already in
the module, by title or by URL, isn't added again, and a held lab that isn't on
disk gets no link. The URL check is what keeps week 10, which already links the
lab as "Live coding notebook", from getting a second pair.

## Grading: `grading.ipynb`

`grading.ipynb` grades the recurring work from Canvas. It is one notebook,
run top to bottom, with all of its code in its cells:
- attendance, from the daily note's responses (the Google Form's CSV), at one
  point per class held;
- Textbook Revisions in weeks 2–9, by resolving each submitted GitHub link to
  its author;
- the portfolio checkpoints in weeks 11–14, by checking each student's repo
  as it stood at the deadline;
- Notebook Labs, by checking each HTML upload against the companion notebook.

The rules are the ones in `docs/grading.md`.

Each section works in small steps, and each cell prints a summary of what it
found. A section scores only the plain case, where there's nothing to decide,
and saves those rows as a CSV. Every other case gets a cell of its own that
prints it for you to decide and enter in Canvas: a late or incomplete lab, a
link to someone else's issue, a note from a personal email, a class day with
no notes. The last section posts one table, with no comments, only with
`APPLY = True` and a typed confirmation of how many rows, then reads every
score back. The notebook needs `CANVAS_TOKEN`;
`GITHUB_TOKEN` is optional but raises GitHub's limit from 60 to 5,000
requests an hour.

Student data goes to `GRADING_DIR` (default `~/info4617-grading`), outside the
repository. Clear the notebook's outputs before you commit it.

## Safety notes

- **Idempotent by name.** Re-running updates existing groups rather than
  creating duplicates. Existing assignments, rubrics, and modules are left
  alone: the instructor edits Canvas directly and grades are posted against
  it, so changing an assignment's points after grading would change students'
  percentages. The dry run lists each assignment that has drifted from the
  spec; `--overwrite` makes them match the spec again.
- **Nothing is deleted.** Leftover assignment groups from the old design are
  reported so you can remove them in Canvas yourself.
- Assignments are created **published**. If you'd rather stage them, change
  `"published": True` in `build_assignments`.
