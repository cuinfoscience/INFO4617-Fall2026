# Proposing revisions to the textbook

*A framework for the Friday workshops — INFO 4617 Web Data Science*

Every Friday you propose a change to the [Web Data Science
book](https://github.com/cuinfoscience/Web-Data-Science-Book) and review a
classmate's. This page is the reusable part: **what kinds of changes are worth
proposing, and what each kind needs to be accepted.** Use it every week.

---

## Why your revisions matter

The book was drafted with the help of large language models and then reviewed
and edited by the instructor. That process is fast and fluent, and it is exactly
the process that produces three predictable weaknesses:

- **Confident text that is subtly wrong** — a selector that never matched, an
  API parameter that doesn't exist, a claim no source supports.
- **Explanations written from the far side of understanding** — technically
  correct, but skipping the step where a first-time reader actually gets stuck.
- **Examples that decay** — the web changes underneath the book. Code that ran
  when it was written may not run today.

You are meeting this material for the first time. That makes you the book's best
reviewer for exactly the failures a fluent draft hides. The question that starts
every revision is:

> **Where did this chapter fail me?**

Not "what could be added in principle" — what actually tripped *you*.

---

## Three families

Sort what you noticed into one of three families. This tells you what kind of
evidence your proposal needs.

| Family | Means | Your proposal must show |
|---|---|---|
| **Broken** | It is wrong, or no longer works | What you ran, and what happened instead |
| **Unclear** | It is right, but you couldn't follow it | Where you got stuck, and why |
| **Missing** | You needed something that wasn't there | That the gap is real, not just possible |

---

## Seven types of revision

These cover nearly everything you'll propose all semester.

| # | Type | Family | You noticed… | Your contribution includes | Size |
|---|---|---|---|---|---|
| 1 | **Code drift** | Broken | An example errors, returns nothing, or returns the wrong shape | The error text, the corrected code, and one line on what changed upstream | M |
| 2 | **Stale figure** | Broken | A screenshot no longer matches today's interface | A fresh screenshot — same filename, same crop, same thing highlighted | S |
| 3 | **Common issue** | Missing | You hit an error that isn't in the chapter's "Common Issues to Debug" | Symptom → cause → fix, written in the list's existing format | S |
| 4 | **Missing figure** | Missing | You had to sketch it yourself before it made sense | The figure, a caption, and alt text | M |
| 5 | **Reading** | Missing | You found a source that grounds or complicates a claim | The citation added to `references.bib`, plus one line on why it belongs | S |
| 6 | **Exercise** | Unclear / Missing | An exercise is ambiguous, unverifiable, or too thin | Expected output, a rubric, a starter cell — or a new exercise with all three | M |
| 7 | **Explanation** | Unclear | You reread a passage three times | The rewrite, plus a sentence on what confused you the first time | M |

**Size** is a rough guide to review effort: **S** is a few lines, **M** is a
paragraph or a code block. Anything bigger than M should start as an issue or a
discussion before you write it.

---

## What each type looks like in practice

**1 · Code drift.** You run the chapter's scraper and get an empty list. The
site renamed a CSS class. Propose the corrected selector — and say how you
found it (dev tools, "Copy selector") so the fix teaches the method, not just
the answer.

**2 · Stale figure.** The chapter shows the Network tab from an older browser
version. Retake it at the same zoom, highlighting the same request, and keep
the filename so nothing else has to change.

**3 · Common issue.** You spent twenty minutes on a `ModuleNotFoundError`
because your notebook kernel pointed at the wrong environment. That is a real
symptom with a real cause and a two-line fix. Add it. This is the single easiest
high-value contribution in the book — it converts your lost time into somebody
else's saved time.

**4 · Missing figure.** You couldn't hold the DOM tree in your head until you
drew it. Contribute the drawing. Diagrams that helped *you* are far more likely
to help the next reader than diagrams invented for completeness.

**5 · Reading.** The chapter asserts something about platform data access and
cites nothing. You find the study, the court filing, or the news report that
actually establishes it. One citation with one sentence of justification.

**6 · Exercise.** "Scrape a table of your choice and visualize it" — with no
expected output, you can't tell whether you did it right. Propose a concrete
target, a sample of the expected DataFrame, or a short rubric.

**7 · Explanation.** The paragraph explaining why `find_all(["td","th"])` beats
splitting on newlines assumed you already knew the failure mode. Rewrite it so
the failure comes first, then the fix. Say what confused you — that sentence is
often more useful to the editor than the rewrite itself.

---

## Rules that apply to every type

**One change per pull request.** A PR that fixes a selector *and* adds a reading
*and* rewrites a paragraph is three reviews wearing one coat. Small, single-purpose
PRs get merged; sprawling ones stall.

**Show, don't assert.** "This is confusing" is a reaction. "I expected X here
because of the previous section, but the code returns Y" is evidence. Paste the
command, the output, the error.

**Match the book's voice.** The repository's `claude.md` documents editorial
voice, formatting conventions, and chapter structure. Read it once; skim it
before each PR. A change in the wrong register costs a review round.

**Check it builds.** The book is Quarto. If you can, run `quarto render` (or at
minimum `quarto preview` on the chapter) before opening the PR. Note in the PR
whether you did.

**Disclose AI assistance.** If a tool helped you draft or diagnose, say so in
the PR description — same standard the book holds itself to, and the same
standard in the course syllabus.

---

## Anatomy of a good issue or pull request

Both use the same skeleton:

```
Title:    <type>: <specific thing> in Ch. N
          e.g. "Common issue: kernel/environment mismatch in Ch. 1"

Location: Chapter and section — and the file, e.g. ch-06-static-pages.qmd,
          "Strategy 1: Manual Table Parsing"

Problem:  What you did, what you expected, what happened.
          Paste the code and the output.

Why:      Who this affects and how much. One sentence.

Proposal: The concrete change. For an issue: what you'd write.
          For a PR: the diff itself.
```

If you can't fill in **Location** and **Problem** with specifics, you don't have
a revision yet — you have a hunch. Go back to the chapter and reproduce it.

---

## How issues and pull requests are graded

Textbook Revisions are **30% of the course grade**, scored weekly out of **10
points**. The rubric follows the skeleton above, so a proposal that fills in
every field scores well by construction.

| | Criterion | What earns full marks | Pts |
|---|---|---|---|
| **Located** | You can find it | Chapter, section, and source file named precisely | 2 |
| **Evidenced** | I can reproduce it | The command, output, error, or quoted passage — enough that I hit the same wall | 3 |
| **Actionable** | I can act on it | A concrete proposed change, correctly scoped to one thing | 3 |
| **Reviews** | You reviewed two peers | Specific, kind, separates must-fix from nice-to-have, ends with a clear verdict | 2 |
| | | **Total** | **10** |

### Merged is not the bar

**You are graded on the proposal and the review, not on whether I merge it.** A
well-evidenced, correctly scoped PR that I decline for editorial reasons earns
full credit. A merged one-character typo fix does not. The skill being assessed
is diagnosis and communication, not acceptance rate.

### What earns little or no credit

- **Bulk typo PRs.** Twenty whitespace changes in one PR is not twenty
  contributions; it is one low-value contribution and a slow review.
- **Reactions without evidence.** "This section is confusing" with no location,
  no quote, and no proposal.
- **Duplicates.** Check open issues and PRs first. If someone already raised it,
  *review theirs* — that counts.
- **Undisclosed AI text.** Using a tool is fine and expected; passing off
  unverified generated text as your own diagnosis is an Honor Code matter. If
  you didn't run it, don't claim it.
- **Scope sprawl.** A PR that changes five unrelated things gets sent back to be
  split before it can be reviewed.

### Partial credit is normal

Most weeks, most people land at 7–9. A 10 means someone else could act on your
proposal without asking you a single follow-up question.

---

## How this maps onto the semester

- **Week 1** — you file your first *issue*. No git required: browse the book,
  find one real problem, describe it with this skeleton.
- **Weeks 2–14** — you open *pull requests* and review two classmates'.
- Each week's lecture deck ends with a **revision menu**: the same seven types,
  aimed at that specific chapter's known thin spots.

Contributions and reviews together are **30%** of your grade. The target for the
semester is posted on Canvas.
