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

## Three forms

The book's issue tracker gives you three forms. Which one you pick is the first
decision you make, and it is not a filing detail — each form asks for the
evidence that its kind of problem actually needs.

| Form | Use it when | It asks you to show |
|---|---|---|
| **Something is wrong** | It is wrong, or no longer works | What you ran, and what happened instead |
| **Gap report** | You needed something and it was missing or unclear, and it *stopped you* | Where you got stuck, and who else would hit it |
| **Suggestion** | It would be better, but nothing blocked you | What you would change, and who benefits |

Two things follow from this.

**The dividing line between a gap and a suggestion is whether you got stuck.**
Not how big the change is. A single missing sentence that cost you forty minutes
is a gap report. A whole section you would reorganize, having understood it fine,
is a suggestion. Gap reports and broken reports get priority, so put it there if
it fits.

**You do not need to know the fix.** Every form makes the proposed fix optional
and the evidence required. Reporting where you got stuck is the whole
contribution — you are reading this material for the first time, which is
exactly what makes you able to see the hole.

Go to
[the book's issue tracker](https://github.com/cuinfoscience/Web-Data-Science-Book/issues/new/choose)
and pick one. Blank issues are turned off, so there is always a form. If you
genuinely cannot tell which fits, pick the closest — a report in the wrong form
is still a useful report and can be relabelled.

---

## Seven types of revision

These cover nearly everything you'll propose all semester. The **Form** column
tells you where each one goes.

| # | Type | Form | You noticed… | Your contribution includes | Size |
|---|---|---|---|---|---|
| 1 | **Code drift** | Something is wrong | An example errors, returns nothing, or returns the wrong shape | The error text, the corrected code, and one line on what changed upstream | M |
| 2 | **Stale figure** | Something is wrong | A screenshot no longer matches today's interface | A fresh screenshot — same filename, same crop, same thing highlighted | S |
| 3 | **Common issue** | Gap report | You hit an error that isn't in the chapter's "Common Issues to Debug" | Symptom → cause → fix, written in the list's existing format | S |
| 4 | **Missing figure** | Gap report | You had to sketch it yourself before it made sense | The figure, a caption, and alt text | M |
| 5 | **Reading** | Suggestion | You found a source that grounds or complicates a claim | The citation added to `references.bib`, plus one line on why it belongs | S |
| 6 | **Exercise** | Suggestion | An exercise is ambiguous, unverifiable, or too thin | Expected output, a rubric, a starter cell — or a new exercise with all three | M |
| 7 | **Explanation** | Gap report | You reread a passage three times | The rewrite, plus a sentence on what confused you the first time | M |

Two of these move depending on how they hit you. A **missing figure** you drew
yourself before the section made sense is a gap; one you think would be a nice
addition is a suggestion. An **exercise** so vague you could not tell whether you
had finished it is a gap; one you completed and think could be stronger is a
suggestion.

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

## Filling in a form well

The forms ask short questions. Short questions invite short answers, and short
answers are where most of the credit is lost. Here is the same real problem
filed twice, field by field.

A student runs the `robots.txt` example in Chapter 2 and cannot work out where
to find a site's `robots.txt` in the first place. Nothing errored. The book just
never said. That is a **gap report**.

**Where were you?** — a dropdown, so this one is free. Pick `Ch. 2 — Ethics,
Law, and Responsible Data Collection`.

**Which section or heading?** Copy the nearest heading exactly.

> ✗ "the robots part"
> ✓ "Technical Norms: robots.txt"

The first makes someone search the chapter. The second is a jump target. This
field costs you five seconds and is worth 2 of 10 points.

**What kind of gap?** — `Something was missing`, `Something was unclear`, or
`Not sure / both`. If you hesitate, `Not sure / both` is a real answer, not a
cop-out. Nobody is grading your taxonomy.

**Where did you get stuck?** This is the field that decides your score.

> ✗ "This section is confusing and needs more detail."
>
> ✓ "I was trying to run the first `robots.txt` example. The text says to check
> whether a page is allowed, but I did not know where to find a site's
> `robots.txt` to begin with, and I could not tell whether I was supposed to
> open it in a browser or fetch it in Python. I spent about fifteen minutes
> guessing URLs before I searched outside the book."

The second is longer, but length is not why it is better. It names what you were
trying to do, the exact sentence you got stuck on, what you tried, and how long
you lost. Someone can now reproduce your confusion without asking you anything.

**Who else would hit this?** One sentence. Resist the urge to say "everyone."

> ✗ "Everyone."
> ✓ "Anyone running this chapter's first code block without having seen a
> `robots.txt` before."

This field is how the editor decides priority. A gap that stops every reader at
the first code block outranks one that only affects someone attempting an
optional exercise.

**What would have helped?** Optional — and leaving it blank costs you nothing if
you genuinely do not know. But a guess is usually worth writing:

> ✓ "One sentence saying `robots.txt` always lives at the site root, with an
> example URL like `https://example.com/robots.txt`."

You are not committing to write the fix. You are showing you understood your own
problem well enough to imagine its shape.

**Before you submit** — a required checkbox confirming you searched the open
issues. Actually search. Duplicates earn no credit, and if someone already filed
yours, reviewing theirs does.

### What carries over to pull requests

Titles are handled for you: each form prefixes `Broken:`, `Gap:`, or
`Suggestion:`, and you complete the sentence. Make what you add specific —
`Gap: no explanation of where to find robots.txt` beats `Gap: confusing section`.

Pull requests have no form. From week 3 on, write the PR description with the
same fields the forms would have asked, in this order:

```
Location: Chapter and section, and the source file —
          e.g. ch-06-static-pages.qmd, "Strategy 1: Manual Table Parsing"

Problem:  What you did, what you expected, what happened.
          Paste the code and the output.

Why:      Who this affects and how much. One sentence.

Change:   What this PR does, and anything you chose not to do.
```

If you can't fill in **Location** and **Problem** with specifics, you don't have
a revision yet — you have a hunch. Go back to the chapter and reproduce it.

---

## How issues and pull requests are graded

Textbook Revisions are **15% of the course grade**, scored weekly out of **10
points**. The rubric follows the same fields the forms ask for, so a proposal
that answers every question properly scores well by construction.

| | Criterion | What earns full marks | Pts |
|---|---|---|---|
| **Located** | You can find it | Chapter and section named precisely — plus the source file, for a pull request | 2 |
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

- **Weeks 1–2** — you find, describe, and file your first *issue*. No git
  required: browse the book, find one real problem, and fill in the form that
  fits it. Week 1 is a single short session, so **Week 2's Friday** is where
  everyone gets GitHub working and files that first issue for credit.
- **Weeks 3–14** — you open *pull requests* and review two classmates'.
- Each week's lecture deck ends with a **revision menu**: the same seven types,
  aimed at that specific chapter's known thin spots.

Deadlines are **Sunday at 11:59pm**, covering both that week's notebook lab and
that week's revision.

Contributions and reviews together are **15%** of your grade. The target for the
semester is posted on Canvas.
