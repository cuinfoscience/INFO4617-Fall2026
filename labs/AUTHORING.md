# Writing a lab notebook

How to turn a chapter of [*Web Data Science*](https://github.com/cuinfoscience/Web-Data-Science-Book) into the week's live-coding lab. [`README.md`](README.md) is for students; this file is for whoever writes a lab, person or agent. It came from the instructor's answers on 2026-10-21, after week 10 piloted the format at students' request: they wanted to code with the instructor rather than work through the chapter's notebook alone. Its code style was rewritten after the instructor taught week 10 live; [`docs/aar/2026-10-21-live-coding-labs.md`](../docs/aar/2026-10-21-live-coding-labs.md) says why. It was revised again on 2026-11-10, after an audit of weeks 10–13 (issues #165 and #167–#169) and the instructor's decision to rebuild those labs for students with little Python: smaller cells, one case typed by hand before a given loop, saved checkpoints, and a check of every request against its provider's documentation. A lab written or rebuilt from that date follows this file as it stands; the labs for weeks 1–9, and weeks 10–13 until each is rebuilt, were written to the earlier rules.

## What a lab is for

Students asked to code *with* the instructor rather than work through a chapter's notebook alone. A lab is the script for that session, so it serves the person typing at the front of the room and the 30 people typing along, in that order:

- **Teach the chapter's core idea in about 135 minutes of typing, over the week's three days,** on the chapter's own case, so the Recommended Exercises are within reach. Coverage is the chapter's job.
- **Keep everyone typing.** A typed cell is one to four lines that do one visible thing, so a student who falls behind can catch up from the key in seconds, and one who is new to Python can say what each line does.
- **Make room to think.** Microsprints and Discuss boxes are where students do and say something themselves. The code is short so that they have time.
- **Cover the chapter by reading as well as typing.** Students type the one case that carries a step's idea. The loop, function or plot that repeats or dresses it is a given cell the class reads and runs together. That is how a lab keeps the chapter's coverage without more typing.
- **Run honestly.** Every request is sent live first, and a failure is something to read and discuss, not to hide behind a wrapper. A saved copy is there for the student the site refuses, not in place of the request.

When a rule here conflicts with getting the key to run from a cloud machine, the classroom wins: flag the cell `not-run-live`, and leave the code plain. The first version of these conventions put the key's run first, with a retrying `get()` helper, `raise_for_status()` everywhere, and the chapter's helper functions copied whole. That code ran well from the cloud, but week 10's pagination step took more than 25 minutes to type in class, and every lab was rewritten the next day.

## The week

- **Monday, Wednesday and Friday** are one lab in three parts, one a day: about 135 minutes in all, Monday's 50, Wednesday's 50, and Friday's first 35. The instructor writes the code on screen and students write it in their copy. If a day ends mid-part, the next day finishes it first.
- **Before week 11** the week was different. In week 10, Monday was a lecture, and the lab ran over Wednesday and Friday, about 85 minutes in all. The labs for weeks 1–10 are written to that two-day form.
- **Friday's last 15 minutes** were the textbook-revision block in weeks 2–10. In weeks 11–14 they are work on that week's project-portfolio checkpoint (`docs/course-facts.md`, "Weeks 10–14 of Textbook Revisions", says what each is and when it's due; decided 2026-11-02). The lab's last cell says which.
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

A lab is one notebook in three parts, one for each day, of numbered steps, in this order:

1. **The opening cell.** The title, `# Lab NN: <the chapter's title>`; a line linking the chapter; two or three sentences on what we'll build and on which case; a sentence saying what the 💬 Discuss boxes are; a **Before class** line (environment, keys, accounts); and one line for later days: "On Wednesday and Friday, start at that day's setup step." Don't send students to **Run All Above**: it repeats every request of the earlier days, which costs time, rate limit, and in some labs money No outline table: each step's heading gives its time. In the key only, this cell ends with the key note (see "The key").
2. **Three parts**, each headed `# Part N — <day>: <what we build>`, with steps numbered across the lab, `## Step 0` to about `## Step 15`. Each part opens with a short setup step, so a student who missed a day can start there: a given cell that imports, defines the User-Agent and checks the keys, in which students type only their email, and a given cell that loads the earlier days' checkpoints (see "Checkpoints"). No variable crosses a day except through a checkpoint. Step 0 is the first.
3. **What did we learn?** The last numbered step: three or four reflection questions, answered as comments, plus the **Recommended Exercises ahead** list.
4. **Friday's revision block**, a last Markdown cell.

### A step

Each step is, in order:

1. **A Markdown cell**, headed `## Step N — <what we build> (M minutes)`. At most about 80 words say what the step does and why, in plain sentences, and point to the chapter's section for more. Define each term where it first appears, in the same sentence. Name the function, parameter, or idea the step turns on, and link its documentation the first time it appears. If a step needs more than 80 words, it is two steps, or the rest belongs in the chapter.
2. **Code cells**, each holding a comment prompt and then the code. A typed cell's prompt is one line, or two at most, in plain words: what this cell does, and any name or key the student must spell exactly. See "Code style" and "Prompts" below. A step usually has several cells: the typed cells that work one case by hand, then the given cell that repeats it.
3. **A microsprint**, after most steps (see below): a Markdown cell and a code cell.
4. **A 💬 Discuss box** (see below). It goes last in the step, after the microsprint if there is one, so the class can discuss what the microsprint found.

Minutes include the microsprint and the discussion. A lab's minutes add up to about 135: about 50 in Monday's part, 50 in Wednesday's, and 35 in Friday's.

Every code cell carries metadata saying what students see, which `tools/make_student_copy.py` reads:

| Metadata | Students see |
|---|---|
| `{"lab": {"prompt_lines": 3}}` | the first 3 lines (the prompt), then `# Your code here` |
| `{"lab": {"prompt_lines": 1, "placeholder": ""}}` | the first line, then an empty line (for answers written as comments) |
| `{"lab": {"given": true}}` | the whole cell: code the class reads and runs but doesn't type. Its first line is a comment starting `# Given:` that says what the cell does. See "By hand, then given". |

### Code style

The code is typed live, in front of the class, by students some of whom are unsure of loops, dictionaries and f-strings. Week 10's pilot showed the cost of long cells: its revisions step, a `continue` loop inside a function that called a helper function, took more than 25 minutes and had to be rewritten on the fly. The audit of weeks 10–13 showed the cost of dense ones: a 12-line cell that chained a request to `.json()["feed"]`, looped, and built a five-key dictionary from three levels of nesting, under a prompt that only a student who didn't need the lab could turn into code.

- **One to four lines a typed cell, six at most,** doing one thing a student can see: build the parameters; send the request; look at what came back; read one value. A line is at most about 90 characters, so it fits a projector and can be typed without a slip.
- **One step at a line.** Don't chain a request to `.json()` to a lookup. Write `response = requests.get(...)`, then `data = response.json()`, then `data["query"]`, each where a student can print it. Go down nested JSON one level a cell the first time a shape appears (`data.keys()`, then `data["query"].keys()`).
- **Look before you read.** The first request to each API prints what came back before anything indexes into it: `print(response.status_code, response.text[:200])` for a service that answers errors in plain text or HTML (Wikimedia, the Census Bureau), or `print(data.get("error"))` for one that answers them as JSON (OpenRouter, FRED, YouTube). This isn't error handling; it's the habit that makes the next rule livable. Without it, every refusal, bad key and misspelled parameter in weeks 10–13 reached the student as the same `JSONDecodeError` or `KeyError`, with the service's own message unread.
- **No error handling.** No `raise_for_status()`, `try`/`except`, retry loops, back-off, `timeout=` arguments, or status checks that branch, unless the step is about them (chapter 3's refusals, chapter 5's status codes). Acknowledge the limitation in a Discuss box: at least one per lab asks what would break here (a 429, a 403, a missing key, a changed page) and how the chapter guards against it.
- **Little Python assumed.** In typed cells, don't use comprehensions, tuple unpacking in a `for`, `**` to merge or pass dictionaries, conditional expressions, `while True` with `break`, regular expressions, or format specifications inside f-strings. Where the chapter's code needs one, it goes in a given cell. The first time any construct appears in the lab, typed or given, the step's text explains it in a sentence.
- **By hand, then given.** See the next section. Students never type a function definition or a loop that sends requests.
- **One name for one thing.** Don't reuse `params`, `data`, `response` or `page` for a different request later in the lab, and don't have a microsprint replace a name a later cell reads: name them for what they hold (`profile_params`, `first_page`, `census_rows`). A cell run twice, or out of order, should give the same result. Week 13's Step 14 checked one tool call and ran another because a microsprint replaced `call` but not `args`.
- **Pause in a loop.** A loop that sends requests sleeps a second between them (`time.sleep(1)`). That's politeness, not error handling, and it's one line.
- **One way to do each thing:** f-strings to print, pandas to tabulate, `plt.subplots()` to plot, and nothing the chapter doesn't use.
- **A `try` only where the failure is the point:** a step about errors (week 4's broken JSON), or a step whose subject is a request that never completes (week 3's dead endpoint). Say why in the step's text.

`tools/run_key.py` decides whether to retry a cell from the error the cell raises, and that depends on this style: with no `raise_for_status()`, a 429 usually surfaces at `.json()`, as a `JSONDecodeError`. A change to these rules that changes how a refused request fails needs the same change to its `TRANSIENT` pattern, in the same pull request.

### By hand, then given

Every idea a lab teaches is typed once, on one case, in small cells. What repeats it is given.

1. **One case by hand.** One profile, one county, one page of results, one row's sum: built, sent, looked at and read in typed cells.
2. **The repetition, given.** The loop over five accounts, the function that follows a cursor to the end, the table and its plot are already in the notebook (`{"lab": {"given": true}}`). The class reads the cell together, finds in it the lines they just typed, and runs it.
3. **One change, typed.** Where it helps, students then change one value and run the given cell again: another handle, another year, `units` set to `"chg"`.

A given cell follows the same plain style where it can, and may use what "Little Python assumed" keeps out of typed cells where the chapter's code does. Keep it under about 15 lines. A given function is flat: never one function inside another, and never one helper calling another, unless the chapter's Recommended Exercises name both (chapter 10's `page_list()` and `query_all()`), in which case the lab gives both and calls each once.

When a step's first `params` or request body is long (five keys, or nested), give the dictionary whole and have students type the one or two values that carry the idea. Reading a nested body is the lesson; typing its brackets isn't.

### Prompts

A prompt is what a student who has fallen behind, or who is reading alone, works from.

- **One plain line a typed cell,** two at most, saying what the cell does: `# Send the request, and print its status and the first 200 characters`.
- **Spell out what must be exact.** A key, parameter or field name the service requires is written as it is typed, in quotes: `# params: change "for" to "place:07850"`, not `for=place:07850`. Week 13's prompt gave `file_url (book + ...)`; typed as `"file"`, it got a 422. Week 11's gave `for="county:013", in="state:08"`, which isn't Python. Giving away a key's name gives away nothing a student should have to guess.
- **Don't write a specification.** If a prompt needs four lines and a list of five fields, the cell is too big: split it, or give it.

### The typing budget

Count typed lines: the lines of code cells that aren't `given`, without prompt lines, blank lines, or the answers in "What did we learn?". A part has at most about **55 typed lines** for Monday's and Wednesday's 50 minutes and **40** for Friday's 35, a little over one line a minute, with microsprints inside the count. Parts 1 and 2 of week 13 ran at that rate and fit their days; its Part 3, at more than two lines a minute, didn't. Count the waiting too: a loop of model requests or paced API calls that takes three minutes is three of the step's minutes.

What the labs written before 2026-11-10 measured, for comparison: 17–28 code cells in 85 minutes, a median cell of 5–7 lines, zero to three typed functions, and zero to two given cells. A rebuilt lab has more cells, each smaller, and more of them given.

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

When a chapter's API pages its results (a `continue` token, a cursor, a page number), teach it by hand, then given:

1. **Two pages by hand.** Request page one and print its token; then request page two with the token added. Keep the whole answer in a name (`first_page`), so the token is there to print. Small typed cells.
2. **The whole loop, given.** The function or loop that follows the token to the end is already in the notebook. The class reads it together, finds the two typed moves in it, and uses it; nobody types it. Save its result as a checkpoint: it is the request a rate limit is most likely to stop.

There is no typed one-batch function between the two, as the earlier rules had.

### Microsprints

A microsprint is a 3–8 minute task students do alone or in pairs, right after the step that taught what it needs. It ends in a **result the class can share and discuss**: a number, a plot, a short list, a one-sentence finding. Most steps after a setup step have one; a lab has about eight, two or three a part.

```markdown
### ⏱ Microsprint (5 minutes, alone or in pairs)

**Do:** run `get_revisions()` on an article about your hometown, and count its editors.
**Share:** the article, its number of revisions, and its number of editors.
```

The code cell under it starts with `# Microsprint:` and a prompt, like any other. Good microsprints change one thing about the step: another case, another parameter, another time window, or a check of the step's result. The chapter's **Additional Exercises** are the first place to look for one: cut an exercise down to five minutes, and name it ("a short version of Additional Exercise 3"). The change should be one or two typed lines: a new value in a name the given cell reads, then that cell run again. A microsprint never asks students to retype a step's cells. And it leaves the lab's names as it found them, or works on names of its own, so the cells after it give the same results whether or not it was run.

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

Each question is one sentence, or two short ones, and answerable in a minute of talk. A question states only what the class has seen: a number or finding it cites is printed by a cell above it, and one that comes from a model or from live data that changes is worded "in the key's run". Check each against the key's outputs after the run.

### What did we learn?

The last numbered step has three or four reflection questions about the whole lab, with a code cell for answers as comments (`placeholder: ""`). The key answers them from its own outputs, with the numbers. Below the questions comes **Recommended Exercises ahead**: one line per step of the chapter's Recommended Exercises, saying which lab step prepared it, without solving it.

```markdown
**Recommended Exercises ahead** (in the chapter's companion notebook, due Sunday):

- Step 1, choose an article and get its pageviews: Steps 5–6 built `get_pageviews()`.
- Step 3, get the revision history: Step 3's pagination loop.
```

### Friday's revision block

In weeks 11–14 the last cell is instead `## Friday: your portfolio checkpoint (15 minutes)`, saying what that week's checkpoint asks and when it's due, from `docs/course-facts.md`. Before week 11, the last cell, Markdown, is headed `## Friday: from the lab to the textbook (15 minutes)`. Point at what the lab might have turned up: a cell that broke, a sentence in the chapter that confused, an output that has changed since the chapter was written, a microsprint that would make a good exercise. Link [`handouts/common/revision-framework.md`](../handouts/common/revision-framework.md) for how to propose one.

## Following the chapter

- **The chapter's case, the chapter's code, flattened.** Use the chapter's running example and its code, but where the chapter wraps a step in a function, write the step's lines straight, and keep a function only as "Code style" allows. Keep the chapter's names for what you keep, so a student who reads the chapter later recognizes them. Where the lab must differ (the chapter has no case that fits the lab's minutes, or its code would fail live), say why in the pull request. If the chapter's code is wrong, file it in the textbook repository too.
- **After the chapter, when it changes.** When the chapter is revised in the sprint before its week, write or revise the lab after the chapter's pull request merges, so that the lab's code, names and section links match what students read. A part taught before the revision can merge follows the current chapter, and is revised once the revision merges. Week 11's Part 1 was that case (textbook plan `docs/plans/2026-10-25-ch11-four-apis.md`, §6).
- **Cover the Learning Objectives** at the top of the chapter. If one doesn't fit, say which in the pull request.
- **Say where it comes from.** The key note names the textbook commit the lab follows (`git -C <book> rev-parse --short HEAD`), so a later chapter change can be checked against the lab.
- **Earlier weeks, by number.** When a step or a question uses an earlier week's idea, name the week and the idea, and check it against that chapter. Don't reach forward to a chapter students haven't met, except in week 1.
- **Only the `webdata` environment.** Use libraries in the environment command in [`docs/course-facts.md`](../docs/course-facts.md). If the chapter installs one more (as chapter 10 installs mwclient), the step says how, as the chapter does.

## Live data

- **Every request is live first.** The User-Agent and pacing are part of the lesson, so each kind of request is sent live by every student at least once. Fix the end of every time window at a past date, so a rerun gives the key's answer. Saved copies come second, as checkpoints (below).
- **The User-Agent:** the book's form, `WebDataScience/1.0 (your-email@colorado.edu)`, defined once in Step 0 and sent with every request. For Wikimedia, use chapter 10's full form, with the library and its version.
- **Be polite:** pause a second between requests in a loop. Don't code around rate limits; a 429 is something to read and discuss (see "Code style"). Thirty students behind one campus address share its allowance, so a step that has everyone run a paging loop at once is a step some of them will fail: that is what its checkpoint is for. Don't promise a rate in the lab's text ("200 a minute"); say what the service's policy says and that the network is shared.
- **API keys** come from environment variables, never from the notebook. Step 0 reads them with `os.environ["NAME"]`; a missing key raises a `KeyError` that names it, which is message enough. If a service will answer a request that has no key, or the wrong parameter, from a default that costs money (OpenRouter's default model), a typed line checks what answered.
- **Privacy:** follow [`AGENTS.md`](../AGENTS.md), "Images and privacy". Don't print a private person's name in an output, and don't build a ranking of people the chapter doesn't build.

### Checkpoints

A checkpoint is a saved copy of a step's result that lets a student go on when they fell behind, missed a day, have no working key, or were refused by the site.

- **Where.** After each given loop that sends several requests, and at the end of each part. A lab has about three to five.
- **What.** A CSV for a table; JSON for a raw response. Files live in `labs/week-NN/data/` (or the textbook's `data/ch-NN/` when the chapter already saves them), and the lab reads them from the repository's raw address on `main`. Make them with the key's own code, on the run the key note describes, and say so there.
- **How it's used.** The live cell comes first. Under it, a given cell loads the checkpoint, with its two lines commented out and a first line that says when to use it: `# Given, only if the cell above stopped: remove the "#" from the next two lines`. Each part's setup step loads the earlier parts' checkpoints the same way, uncommented, so a part never depends on another day's kernel.
- **Privacy.** A published checkpoint holds no private person's name, username, handle or IP address, and no contact details ([`AGENTS.md`](../AGENTS.md), "Images and privacy"). Drop those columns, or keep that step live and have each student save their own copy locally. Institutions' and public officials' accounts are fine.
- **Honesty.** A checkpoint is dated in its loading cell's comment, and a Discuss question somewhere in the lab asks what a saved copy can't tell you that the live request can.

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

### Check it against the provider, not only the run

A cell that runs isn't yet a cell that's right, or one a student can get right. Before the pull request, for each service the lab calls:

- **Read its current documentation** for every endpoint, parameter name and value, limit, and deprecation the lab uses, and for what a failure looks like: the status, and whether the body is JSON, plain text or HTML. Link the page you read in the step. Libraries too: check the version the `webdata` command installs against the version `pip` gives (mwclient 0.10's `limit` became 0.11's `api_chunk_size`, and the old spelling was silently ignored).
- **Try the likely mistypes live,** one request each: the wrong spelling of each typed key, a value in the wrong form (`county:13`), the key in the wrong place, a required parameter left out. Note what comes back and which line the student would see fail. Fix the prompt for any that is easy to make, and write a Discuss question for any that is **accepted without an error** and gives a wrong result (a misspelled `filter` that Bluesky ignores; `model` for `models`, which OpenRouter answers from a default model).
- **Check every statement** in the step texts, Discuss boxes and "What did we learn?" against the key's outputs and the page it cites.
- **Know what `run_key.py` skipped.** Cells tagged `skip-execution`, which every `not-run-live` cell is, aren't run and raise nothing. A key with such cells has not been run top to bottom, whatever the report says; a later cell that depends on one ran on whatever state was there, or failed for that reason alone.

Put what you found in the pull request: the mistypes tried and their results, as a short table.

## How the pieces fit

- **One source.** The key (`lab-NN-key.ipynb`) is the only file anyone edits. `tools/make_student_copy.py` makes the students' copy from each code cell's `lab` metadata, `tools/run_key.py` fills its outputs from the live sites, and `tools/make_key_pdf.py` makes its PDF. Change the key, then run all three.
- **Where students find it.**
  - `labs/README.md`'s table has a row per lab: the students' copy, the key, and the key's PDF.
  - Canvas links the lab and its key in the week's Wednesday section (from week 11 the lab starts on Monday, and `migrate.py` doesn't know that yet; see `docs/course-facts.md`): `python canvas/migrate.py labs` adds them to modules that already exist; see [`canvas/README.md`](../canvas/README.md).
  - The week's slides name the lab in the at-a-glance frame and in each day's first frame.
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
- The minutes in the step headings add up to about 135, by part as "A step" says, and the typed lines are within "The typing budget".
- No typed cell has more than six lines, a line over about 90 characters, a function definition, a loop that sends requests, or anything "Little Python assumed" rules out.
- The first request to each service prints what came back before it's indexed.
- Every step has a Discuss box, and most have a microsprint; no microsprint retypes a step or replaces a name a later cell reads.
- No cell has error handling, and no given function sits inside another.
- No microsprint answers a Recommended Exercise step, and "Recommended Exercises ahead" matches the chapter's steps as merged.
- Every part starts from its own setup step and its checkpoints, and no checkpoint holds a private person's name, handle or address.
- Every step's text is within about 80 words and defines its terms.
- Every "week N" in a question matches what that chapter teaches, and every number in a question is one the class has seen.
- Every figure in the key's outputs reads at a glance, with a title and labeled axes.

The pull request:
- lists the cells not run live;
- gives the typed lines and minutes for each part, and the mistypes tried against each service;
- says where the lab departs from the chapter;
- names the textbook commit;
- adds the lab's row to [`README.md`](README.md)'s table.

When a week's slides exist, their at-a-glance frame and each day's first frame name the lab. The instructor edits slides in Overleaf, so say in the pull request what the slides should say rather than editing them, unless asked.
