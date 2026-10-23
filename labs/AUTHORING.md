# Writing a lab notebook

How to turn a chapter of [*Web Data Science*](https://github.com/cuinfoscience/Web-Data-Science-Book) into the week's live-coding lab. [`README.md`](README.md) is for students; this file is for whoever writes a lab, person or agent. It came from the instructor's answers on 2026-10-21, after week 10 piloted the format at students' request: they wanted to code with the instructor rather than work through the chapter's notebook alone. Its code style was rewritten after the instructor taught week 10 live; [`docs/aar/2026-10-21-live-coding-labs.md`](../docs/aar/2026-10-21-live-coding-labs.md) says why.

## What a lab is for

Students asked to code *with* the instructor rather than work through a chapter's notebook alone. A lab is the script for that session, so it serves the person typing at the front of the room and the 30 people typing along, in that order:

- **Teach the chapter's core idea in about 85 minutes of typing,** on the chapter's own case, so the Recommended Exercises are within reach. Coverage is the chapter's job.
- **Keep everyone typing.** Short, plain cells mean a student who falls behind can catch up from the key in seconds.
- **Make room to think.** Microsprints and Discuss boxes are where students do and say something themselves. The code is short so that they have time.
- **Run honestly.** Every request is live, and a failure is something to discuss, not to hide behind a wrapper.

When a rule here conflicts with getting the key to run from a cloud machine, the classroom wins: flag the cell `not-run-live`, and leave the code plain. The first version of these conventions put the key's run first, with a retrying `get()` helper, `raise_for_status()` everywhere, and the chapter's helper functions copied whole. That code ran well from the cloud, but week 10's pagination step took more than 25 minutes to type in class, and every lab was rewritten the next day.

## The week

- **Monday** is a lecture: the week's concepts and its chapter, on the week's slides.
- **Wednesday and Friday** are one lab across both days, about 85 minutes in all: Wednesday's 50, and Friday's first 35. The instructor writes the code on screen and students write it in their copy. Wherever Wednesday stops, Friday picks up.
- **Friday's last 15 minutes** are the textbook-revision block (graded under Textbook Revisions, 15%).
- **What students submit** is the chapter's **Recommended Exercises**, in the chapter's companion notebook, due the Sunday after the lab (graded under Notebook Labs, 30%). The lab itself isn't turned in.

So a lab teaches what the Recommended Exercises need, and stops short of doing them.

## Files

Each lab lives in `labs/week-NN/`, where `NN` is the week, as in `slides/` and `handouts/`. Week *N* teaches chapter *N* for weeks 1–11.

| File | What it is |
|---|---|
| `lab-NN-key.ipynb` | The source. Every cell filled in, and run against the live sites. The only file you edit. |
| `lab-NN.ipynb` | The students' copy, made from the key by `tools/make_student_copy.py`. Never edit it by hand. |
| `lab-NN-key.pdf` | The key as a PDF, made from it by `tools/make_key_pdf.py` (pandoc and LuaLaTeX). Never edit it by hand. There's no PDF of the students' copy. |

The labs are written as notebooks, not built from a `.qmd`, so `handouts/`'s `make` and workflow leave them alone. Write the key however you like (by hand in JupyterLab, or with a script that calls `nbformat`), as long as the result follows this file.

## What a lab is made of

A lab is one notebook of numbered steps, in this order:

1. **The opening cell.** The title, `# Lab NN: <the chapter's title>`; a line linking the chapter; two or three sentences on what we'll build and on which case; a sentence saying what the 💬 Discuss boxes are; a **Before class** line (environment, keys, accounts); and one line for Friday: "On Friday, run every cell above where we stopped (**Run → Run All Above Selected Cell**)." No outline table: each step's heading gives its time. In the key only, this cell ends with the key note (see "The key").
2. **Steps**, `## Step 0` to about `## Step 10`. Step 0 is setup.
3. **What did we learn?** The last numbered step: three or four reflection questions, answered as comments, plus the **Recommended Exercises ahead** list.
4. **Friday's revision block**, a last Markdown cell.

### A step

Each step is, in order:

1. **A Markdown cell**, headed `## Step N — <what we build> (M minutes)`. One short paragraph says what the step does and why, in the chapter's terms, and points to the chapter's section for more. Name the function, parameter, or idea the step turns on, and link its documentation the first time it appears.
2. **A code cell** that holds the comment prompt and then the code. The prompt is one to four comment lines that say what to write, closely enough that a student can follow it without the instructor, but without giving the code away: `# Request page two: add data["continue"] to params, then request again`, not the code itself. See "Code style" below.
3. **A microsprint**, after most steps (see below): a Markdown cell and a code cell.
4. **A 💬 Discuss box** (see below). It goes last in the step, after the microsprint if there is one, so the class can discuss what the microsprint found.

Minutes include the microsprint and the discussion. A lab's minutes add up to about 85.

Every code cell carries metadata saying what students see, which `tools/make_student_copy.py` reads:

| Metadata | Students see |
|---|---|
| `{"lab": {"prompt_lines": 3}}` | the first 3 lines (the prompt), then `# Your code here` |
| `{"lab": {"prompt_lines": 1, "placeholder": ""}}` | the first line, then an empty line (for answers written as comments) |
| `{"lab": {"given": true}}` | the whole cell: code students don't need to write, such as a long URL or a plotting style. Use it rarely. |

### Code style

The code is typed live, in front of the class, so it has to be short and plain. Week 10's pilot showed the cost of the opposite: its revisions step, a `continue` loop inside a function that called a helper function, took more than 25 minutes and had to be rewritten on the fly.

- **Short, imperative cells.** A cell does one thing, in about 3–8 lines, in the order you'd say it aloud: build the parameters, send the request, read the JSON, print. Prompts are commands: `# Request page one with params and HEADERS; print its "continue"`.
- **Straight-line first.** Write a step's code at the top level of its cell, with no function around it.
- **A function only when it's reused,** and only in a step after the one that showed its parts as plain code, so the function gathers lines the class has already written. Never define a function inside another, and never have one helper call another: one function, flat.
- **No error handling.** No `raise_for_status()`, `try`/`except`, retry loops, back-off, `timeout=` arguments, or status checks, unless the step is about them (chapter 3's refusals, chapter 5's status codes). The code assumes every request works. Acknowledge that as a limitation in a Discuss box instead: at least one per lab asks what would break here (a 429, a 403, a missing key, a changed page) and how the chapter guards against it.
- **Pause in a loop.** A loop that sends requests sleeps a second between them (`time.sleep(1)`). That's politeness, not error handling, and it's one line.
- **One way to do each thing:** f-strings to print, pandas to tabulate, `plt.subplots()` to plot, and nothing the chapter doesn't use.
- **A `try` only where the failure is the point:** a step about errors (week 4's broken JSON), or a step whose subject is a request that never completes, where letting it stop the cell would also stop Friday's **Run All Above** (week 3's dead endpoint). Say why in the step's text.

`tools/run_key.py` decides whether to retry a cell from the error the cell raises, and that depends on this style: with no `raise_for_status()`, a 429 usually surfaces at `.json()`, as a `JSONDecodeError`. A change to these rules that changes how a refused request fails needs the same change to its `TRANSIENT` pattern, in the same pull request.

What the eleven restyled labs (measured on 2026-10-22) have in common, as a yardstick rather than a rule:
- 8–13 steps, 5–6 microsprints, and 83–85 minutes. 17–28 code cells, or more when they're short (week 9 has 42). The median code cell has 5–7 lines of code. Few have more than 10, and those few are a function gathering an earlier step's lines (week 6), a given cell (week 10's `get_revisions()`), or a key's long answer to an open-ended microsprint (week 3's, whose prompt asks for five or more events and whose key lists 13).
- Zero to three functions, each written in the step after its lines were typed plainly: `get_daily_views()`, `read_infobox()`, `get_saved_copy()`. Most are called three or more times; week 7's `preprocess_document()` is called from one loop, and kept because the chapter's Recommended Exercise names it.
- `time.sleep(1)` in every loop that sends requests.
- Zero to two `given` cells, for a whole pagination loop or a long list of URLs.
- Three to six Discuss boxes that ask what would break here: a 429, a 403, a missing key, a page that changed.

### Links

A step's text links the two or three pages a student would open while typing its code. A microsprint links the one page its change needs, if any. Links already there count, so a step that has three has its share.
- **Specific:** the exact page or anchor for what the step turns on:
  - the function's reference page (`pandas.DataFrame.resample`);
  - the endpoint's or parameter's page in the service's own docs (MediaWiki's `API:Revisions`);
  - the chapter's subsection (`ch-10-wikipedia.html#getting-revisions`);
  - an MDN or RFC page for an HTTP idea (status 429, `Retry-After`, RFC 9309 for `robots.txt`).

  A library's front page or a whole manual isn't specific: point it at the section it means.
- **Inline:** on the name, where the text first mentions it ("ask for [`prop=info`](…)"), never as a list of links. Step text and microsprints get them. Discuss boxes, "What did we learn?" and Friday's block keep only the links they need to make sense.
- **Stable:** link a library's stable docs, not its development version or one the course doesn't install. On Read the Docs that's `/en/stable/`, where the site has one (requests and mwclient do; BeautifulSoup's mirror there doesn't).
- **Checked:** every link opens, and every `#anchor` exists on its page, the textbook's included. Renaming a heading in the chapter breaks its anchor without a warning, so when a chapter's headings change, check the labs that link them.

### Pagination

When a chapter's API pages its results (a `continue` token, a cursor, a page number), teach it in three moves:

1. **Two pages by hand.** Request page one and print its token; then request page two with the token added. Straight-line code, in one or two cells.
2. **One batch, as a function, written live.** A short function that takes the title or query and returns one batch, up to the API's limit (500 revisions for the MediaWiki API): the lines from move 1, gathered.
3. **The whole loop, given.** The function that follows the token to the end is already in the notebook (`{"lab": {"given": true}}`). The class reads it together, compares it with move 2, and uses it; nobody types it.

### Microsprints

A microsprint is a 3–8 minute task students do alone or in pairs, right after the step that taught what it needs. It ends in a **result the class can share and discuss**: a number, a plot, a short list, a one-sentence finding. Most steps after Step 0 have one; a lab has about five.

```markdown
### ⏱ Microsprint (5 minutes, alone or in pairs)

**Do:** run `get_revisions()` on an article about your hometown, and count its editors.
**Share:** the article, its number of revisions, and its number of editors.
```

The code cell under it starts with `# Microsprint:` and a prompt, like any other. Good microsprints change one thing about the step: another case, another parameter, another time window, or a check of the step's result. The chapter's **Additional Exercises** are the first place to look for one: cut an exercise down to five minutes, and name it ("a short version of Additional Exercise 3").

**Never a Recommended Exercise.** A microsprint can practise a technique the Recommended Exercises use, but never produce what one of their steps asks for. The test: if a student could paste the microsprint's code into the companion notebook, change a name, and have answered a Recommended Exercise step, the microsprint is too close. Change what it produces.

### 💬 Discuss boxes

After each step, a collapsed box holds two or three questions for the instructor to pose and the class to answer out loud. It is unobtrusive on purpose: closed, the box is one line. Students don't write answers, and the key doesn't hold them.

```html
<details>
<summary>💬 Discuss</summary>

- First question?
- Second question?

</details>
```

Keep the blank lines around the list, or the questions won't render as Markdown. Mix three kinds:

- **Understanding:** what the step showed, or what would have happened otherwise. "Without the `continue` loop, how many revisions would we have, and would anything warn us?"
- **Implications:** what it means for research, ethics, or the data's validity. "A spike measures attention, not approval. Which claims can it support?"
- **Connections:** a concept from an earlier week, named by week and checked against that chapter's text. "In week 6 we scraped Wikipedia infoboxes. Which approach breaks first when Wikipedia redesigns its pages?" Most boxes have one, but don't force one. Week 1's lab can only look ahead, or connect to students' own experience.

Each question is one sentence, or two short ones, and answerable in a minute of talk.

### What did we learn?

The last numbered step has three or four reflection questions about the whole lab, with a code cell for answers as comments (`placeholder: ""`). The key answers them from its own outputs, with the numbers. Below the questions comes **Recommended Exercises ahead**: one line per step of the chapter's Recommended Exercises, saying which lab step prepared it, without solving it.

```markdown
**Recommended Exercises ahead** (in the chapter's companion notebook, due Sunday):

- Step 1, choose an article and get its pageviews: Steps 5–6 built `get_pageviews()`.
- Step 3, get the revision history: Step 3's pagination loop.
```

### Friday's revision block

The last cell, Markdown, headed `## Friday: from the lab to the textbook (15 minutes)`. Point at what the lab might have turned up: a cell that broke, a sentence in the chapter that confused, an output that has changed since the chapter was written, a microsprint that would make a good exercise. Link [`handouts/common/revision-framework.md`](../handouts/common/revision-framework.md) for how to propose one.

## Following the chapter

- **The chapter's case, the chapter's code, flattened.** Use the chapter's running example and its code, but where the chapter wraps a step in a function, write the step's lines straight, and keep a function only as "Code style" allows. Keep the chapter's names for what you keep, so a student who reads the chapter later recognizes them. Where the lab must differ (the chapter has no case that fits 85 minutes, or its code would fail live), say why in the pull request. If the chapter's code is wrong, file it in the textbook repository too.
- **Cover the Learning Objectives** at the top of the chapter. If one doesn't fit, say which in the pull request.
- **Say where it comes from.** The key note names the textbook commit the lab follows (`git -C <book> rev-parse --short HEAD`), so a later chapter change can be checked against the lab.
- **Earlier weeks, by number.** When a step or a question uses an earlier week's idea, name the week and the idea, and check it against that chapter. Don't reach forward to a chapter students haven't met, except in week 1.
- **Only the `webdata` environment.** Use libraries in the environment command in [`docs/course-facts.md`](../docs/course-facts.md). If the chapter installs one more (as chapter 10 installs mwclient), the step says how, as the chapter does.

## Live data

- **Every request is live,** with no saved copies: the User-Agent and pacing are part of the lesson. Fix the end of every time window at a past date, so a rerun gives the key's answer.
- **The User-Agent:** the book's form, `WebDataScience/1.0 (your-email@colorado.edu)`, defined once in Step 0 and sent with every request. For Wikimedia, use chapter 10's full form, with the library and its version.
- **Be polite:** pause a second between requests in a loop. Don't code around rate limits; a 429 is something to discuss (see "Code style").
- **API keys** come from environment variables, never from the notebook. Step 0 reads them with `os.environ["NAME"]`; a missing key raises a `KeyError` that names it, which is message enough.
- **Privacy:** follow [`AGENTS.md`](../AGENTS.md), "Images and privacy". Don't print a private person's name in an output, and don't build a ranking of people the chapter doesn't build.

## The key

The key's opening cell ends with the key note, one paragraph that starts `> **Instructor key.**`. It says:
- when the key was run, and what will and won't match a rerun;
- the textbook commit it follows;
- any step that wasn't run, and why.

`tools/make_student_copy.py` removes this paragraph from the students' copy. Write it last, after `tools/run_key.py` finishes, from its report of which cells ran. Until then, leave the word `PLACEHOLDER` in its place, so that a note describing a run that hasn't happened can't slip through.

Commit the key before you run it: a live run can take an hour, and a restarted machine takes uncommitted work with it. Then run it with `tools/run_key.py`, which:
- runs it cell by cell from a scratch folder;
- reruns a cell that hits a rate limit, including a 429 that surfaces as a `JSONDecodeError` when the cell reads the refusal page with `.json()`;
- puts the placeholder email back afterwards;
- refuses to write the notebook if an output holds an API key.

A cell a site keeps refusing keeps its code, loses its outputs, and is tagged `not-run-live`; list those cells in the pull request so the instructor can run them before class. Give a refusing site about 30 minutes for the whole run, not for each cell: `run_key.py --retries 2 --wait 60` spends two minutes on a cell, so a site that refuses fifteen cells has had its half hour. Then accept the flags and move on. Sites rate-limit the course's cloud machine far more than a laptop on campus: on 2026-10-21 Wikimedia answered it with 429s for hours, the Wayback Machine refused it, and FRED was down for maintenance. The instructor's laptop is the better place to run flagged cells. Microsprints are filled in and run like any other cell, on the case the key's microsprint names.

A rerun isn't better because it's newer. `run_key.py` writes over the key in place, so a rerun on a bad day looks like an ordinary update. Before committing one, compare its `not-run-live` cells with the committed key's (`git show HEAD:<key>`). If it flags a cell the key had filled, keep the key, and run the flagged cells from a laptop.

## How the pieces fit

- **One source.** The key (`lab-NN-key.ipynb`) is the only file anyone edits. `tools/make_student_copy.py` makes the students' copy from each code cell's `lab` metadata, `tools/run_key.py` fills its outputs from the live sites, and `tools/make_key_pdf.py` makes its PDF. Change the key, then run all three.
- **Where students find it.**
  - `labs/README.md`'s table has a row per lab: the students' copy, the key, and the key's PDF.
  - Canvas links the lab and its key in the week's Wednesday section: `python canvas/migrate.py labs` adds them to modules that already exist; see [`canvas/README.md`](../canvas/README.md).
  - The week's slides name the lab in the at-a-glance frame and in Wednesday's first frame.
- **One folder per week.** Labs never share files, so several can be written at once, each on its own branch and pull request, without conflicts. That's how eleven were written in a day.
- **The machine.** The tools run in the `webdata` environment.
  - `make_key_pdf.py` also needs pandoc and LuaLaTeX with its font loader: TeX Live's `texlive-luatex`, which the course's cloud machine had to install.
  - Selenium and Playwright need a browser that matches the library's version.
  - Week 2's key runs on Python 3.14, because `robots.txt` parsing changed in 3.14.5.

## Before the pull request

From the repository's top folder, in the `webdata` environment:

```bash
LAB_EMAIL=you@colorado.edu python labs/tools/run_key.py labs/week-NN/lab-NN-key.ipynb
python labs/tools/make_student_copy.py labs/week-NN/lab-NN-key.ipynb
python labs/tools/make_student_copy.py --check labs/week-NN/lab-NN-key.ipynb
python labs/tools/make_key_pdf.py labs/week-NN/lab-NN-key.ipynb
```

`make_key_pdf.py` needs pandoc, LuaLaTeX (TeX Live's `texlive-luatex`), and the DejaVu and Noto fonts. Rerun it whenever the key changes, so the PDF never shows an older key.

Then check by reading:
- The minutes in the step headings add up to about 85.
- Every step has a Discuss box, and most have a microsprint.
- No cell has error handling, no function sits inside another, and every function is used more than once.
- No microsprint answers a Recommended Exercise step.
- Every "week N" in a question matches what that chapter teaches.
- Every figure in the key's outputs reads at a glance, with a title and labeled axes.

The pull request:
- lists the cells not run live;
- says where the lab departs from the chapter;
- names the textbook commit;
- adds the lab's row to [`README.md`](README.md)'s table.

When a week's slides exist, their at-a-glance frame and Wednesday's first frame name the lab, as week 10's do. The instructor edits slides in Overleaf, so say in the pull request what the slides should say rather than editing them, unless asked.
