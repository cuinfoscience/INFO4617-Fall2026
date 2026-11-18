# Student-persona reviews

Each file here is a review of one week's materials, as five kinds of student would meet them: the lab notebook, the deck, and the chapter's Recommended Exercises. A review says what the week does well and why, then where it falls short and for whom, with a proposed fix for each shortfall and the file to change. It is a list of findings for the instructor to decide on. It changes no lab, deck, chapter or data file itself.

These reviews aren't after-action reports. An AAR (`docs/aar/`) asks how the work on the course was done; a review here asks how a week reads to the students it was written for.

## Method

- **Five personas.** Each is an anonymous composite of a kind of student this course has, not a real student (the table below; approved by the instructor on 2026-11-17). A reviewer plays one persona at a time and keeps to what that student would know.
- **Each does the work.** A persona reads the chapter and the slides, then types its own code for every typed cell of the students' copy of the lab, from the prompt and the slide, and runs it. It makes the mistakes its background makes, and fixes them with what the materials and the error messages say. It opens the key only after an honest try, and records when it had to. Then it attempts the chapter's Recommended Exercises.
- **Steel man.** Each review first makes the strongest case for the materials as designed: what works, and why it was built that way. Only then does it say where they fall short for that student. A shortfall that survives the strongest case is worth more than a list of complaints.
- **One document a week.** The five reviews are put together into `week-NN.md`. Each ranked finding is checked against the repository and the textbook before it is repeated, and marked **verified**, with how, or **reported, not verified**. Claims that turn out wrong are dropped or corrected, in a "Corrections" note.
- **Privacy.** A review describes a finding about contact details; it never reproduces them. It prints no private individual's name.

### What each persona knows, and how it works

- **Knows** only what its background gives it, plus the course's earlier weeks. A minimal persona doesn't know list comprehensions, `**` merges, f-string format specs, regular expressions, or how to read a traceback beyond its last line, until the materials explain them. A moderate persona knows Python basics and some pandas. E knows git and HTTP but not pandas idioms; D thinks in R and statistics.
- **Notices** what matters to its interest. A and B: whether the motivation and the people behind the data are clear, and whether the steps say why. C and D: whether the numbers, checks and validity claims hold. E: whether the code and tools are sound, and whether the given cells hide too much.
- **Reports** the time a real student of that background would need for each part, where it got stuck and how it got unstuck, what it couldn't finish, and what helped.

## The personas

| | Degree and major | Python and data background | Interest | Skill |
|---|---|---|---|---|
| A | BS senior, Information Science | One intro Python course; spreadsheets | Qualitative and design: online communities, UX | Minimal |
| B | BA junior, Journalism and Communication | No Python before this course; strong with public records and Excel | Data journalism, local government | Minimal |
| C | BS senior, Business Analytics | Excel, some SQL, a little pandas | Quantitative analytics: markets, customer data, dashboards | Minimal to moderate |
| D | MS first year, Data Science (BA in Statistics) | Fluent in R, moderate pandas; regression and sampling | Quantitative: measurement and validity | Moderate |
| E | MS first year, Information Science (BS in Computer Science) | Moderate Python, git; little data analysis | Design and tools: automation, APIs, building things | Moderate |

## How to read a review

| Section | What it holds | How to use it |
|---|---|---|
| Header | The week, the commits reviewed, the date | A finding describes that version. Check whether a later pull request already changed the cell. |
| What each completed | Steps finished and blocked, exercises, estimated minutes for each part | Compare the estimates with the lab's own minutes |
| Environment blocks | What the review machine couldn't reach: keys, sites that refused it | Not flaws in the materials. A block that exposed a missing way round it is a ranked finding, and says so. |
| The strongest case | What works and why, by step and frame | What to keep when revising |
| Where it falls short, ranked | Numbered findings, most serious first: who, what happened, why it matters, proposed fix, status | Privacy and wrong-result problems come first; then by how many personas hit a finding, how badly, and whether it stopped A or B |
| Corrections | Reviewers' claims that didn't hold | Don't act on these |
| Disagreements | Where personas differed, and what that suggests | These usually need the instructor's decision |
| Ratings | Five ratings by persona, 1 to 5, with the mean | Compare weeks; one week's numbers mean little alone |
| Small things | Typos, mismatches between files, broken links | Cheap to fix in one pass |
| Suggested next step | The fixes to make first, and the decisions only the instructor can make | Start here |

Two cautions:
- **The times are estimates.** A persona reports what a real student of its background would need, not what its own run took.
- **Run-specific results can't be checked again.** Which free model answered, what it got wrong, and how long it took change from run to run. A review marks these as each persona's own run.

## Reviews

| Week | Topic | Reviewed | File |
|---|---|---|---|
| 13 | AI APIs as Data Tools: Datalab, structured output, embeddings | 2026-11-17, at `efc1e36` (textbook `3f9cf2c`) | [`week-13.md`](week-13.md) |
