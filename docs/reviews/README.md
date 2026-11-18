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
| 1 | Introduction to Web Data Science | 2026-11-18, #217 at `a91f57f` (textbook `3f9cf2c`) | [`week-01.md`](week-01.md) |
| 2 | Ethics, Law, and Responsible Data Collection | 2026-11-18, #214 at `1c59716` (textbook `3f9cf2c`) | [`week-02.md`](week-02.md) |
| 3 | The Post-API Age | 2026-11-18, #212 at `e136c69` (textbook `3f9cf2c`) | [`week-03.md`](week-03.md) |
| 4 | Data Formats: XML and JSON | 2026-11-18, #208 at `7d62e42` (textbook `3f9cf2c`) | [`week-04.md`](week-04.md) |
| 5 | Web Architecture and Protocols | 2026-11-17 and 18, #211 at `8ee384e` (textbook `3f9cf2c`) | [`week-05.md`](week-05.md) |
| 6 | Parsing Static Web Pages | 2026-11-18, #206 at `21b478e` (textbook `3f9cf2c`) | [`week-06.md`](week-06.md) |
| 7 | Archived Web Pages and the Wayback Machine | two of five reviews done (#207); the other three wait for the laptop run that makes the checkpoints (#197) | not yet |
| 8 | Dynamic Web Pages with Selenium | 2026-11-17 and 18, #203 at `2cbbad7` (textbook `3f9cf2c`) | [`week-08.md`](week-08.md) |
| 9 | Extracting Data from PDFs | 2026-11-17 and 18, #204 at `50192aa` (textbook `3f9cf2c`) | [`week-09.md`](week-09.md) |
| 10 | Introduction to APIs: Wikipedia | 2026-11-18, #205 at `ea4a699` (textbook `3f9cf2c`) | [`week-10.md`](week-10.md) |
| 11 | Government Data APIs | 2026-11-18, #201 at `1d3f270` (textbook `3f9cf2c`) | [`week-11.md`](week-11.md) |
| 12 | Social and Media Platform APIs | 2026-11-17, at `efc1e36` (textbook `3f9cf2c`) | [`week-12.md`](week-12.md) |
| 13 | AI APIs as Data Tools: Datalab, structured output, embeddings | 2026-11-17, at `efc1e36` (textbook `3f9cf2c`) | [`week-13.md`](week-13.md) |
| 14 | Automating Data Collection | 2026-11-17 and 18, #213 at `576551b` (persona A at `efc1e36`; textbook `90fd7ef`) | [`week-14.md`](week-14.md) |
