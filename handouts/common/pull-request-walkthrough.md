# From bug to pull request

*The GitHub web-editor mechanics — INFO 4617 Web Data Science*

[`revision-framework.md`](revision-framework.md) covers *what* is worth
proposing and *why*. This page is the *how*: the click-by-click path from
"I found something" to a merged pull request, using GitHub's own web editor —
no terminal, no local clone.

This is the **weeks 3–4 method**. From week 5 on you'll do the same five
stages from your own clone with GitHub Desktop or `gh` (see
[`../week-01/setup.md`](../week-01/setup.md)) — the file you edit, the
description you write, and what happens after you merge are identical either
way. Only the editor changes.

**Running example.** Wednesday's slides walked through one real fix: Chapter
4's "Missing Manual Reference" callout named Chapter 20 but never linked to
it. That gap is already fixed on `main` — what follows is a worked example
of exactly how, not a live task. Your bug will be a different one; the
mechanics below are identical either way.

---

## 1 · Match your bug to a file

Every chapter is one file, named `ch-NN-slug.qmd` — `ch-01-introduction.qmd`
up through `ch-15-research-design.qmd`, plus three appendices
(`appendix-notebooks.qmd`, `appendix-ai-disclosure.qmd`,
`appendix-further.qmd`). You rarely need to know the exact filename before
you start, because GitHub finds it for you:

1. **You're reading the live book.** Every page has an **Edit this page**
   link in the sidebar. Click it — GitHub takes you straight to the matching
   `.qmd` source. This is the fast path, and the one you'll use most.
2. **You're not on the page** — a classmate mentioned a bug, or you're
   browsing the repository directly. Press <kbd>t</kbd> on any page in
   [`cuinfoscience/Web-Data-Science-Book`](https://github.com/cuinfoscience/Web-Data-Science-Book)
   to open GitHub's file finder, then type a fragment of the filename
   (`data-formats`, `static-pages`) to jump to it.

> **Note:** the `.qmd` file is always the one true source. Never edit the
> rendered HTML page — there is no save button on a website. And never edit
> a file under `notebooks/`: every notebook there is generated from its
> matching `.qmd` by a script, so a direct edit gets silently overwritten the
> next time someone regenerates them.

**Worked example.** Chapter 4's "Missing Manual Reference" callout used to
name a chapter without linking to it. Starting from the live page, the fix
began with **Edit this page** — GitHub opens `ch-04-data-formats.qmd`, the
same source Wednesday's slides used.

---

## 2 · Edit the file in GitHub's web editor

You land on the raw `.qmd` source in GitHub's file viewer. From here:

1. Click the **pencil icon** (top right) — **Edit this file**. You have
   write access now: no fork, no separate copy. You're editing the real
   repository directly.
2. The chapter runs past 500 lines — don't scroll hunting for one sentence.
   Click inside the editor and press <kbd>Ctrl+F</kbd> (<kbd>Cmd+F</kbd> on a
   Mac) to open **the editor's own search bar**, not your browser's. Your
   browser only searches what's currently rendered; the editor holds the
   whole file. Search for a distinctive phrase from your bug — for the
   worked example, `Missing Manual Reference` — so you land in the same spot
   every time.
3. Make the edit. Shape depends on what you found — a broken link, a stale
   code block, a missing citation — but a Markdown link fix is the most
   common first PR, and it's small enough to see the whole pattern at once:

   ```
   Before:
   ...see *Missing Manual* Chapter 20: Data File Formats.

   After:
   ...see [*Missing Manual* Chapter 20: Data File Formats]
   (https://cuinfoscience.github.io/INFO-Missing-Manual/
   chapters/data-file-formats.html).
   ```

   A Markdown link is `[text](url)`. Wrap the existing phrase — don't retype
   it — and any formatting inside the brackets (here, the italics) survives.

4. Click the **Preview** tab above the editor and check three things: the
   change reads correctly (a link is blue and underlined), any formatting
   around it survived, and nothing else on the page moved.

> **Note:** one change per pull request. Add the fix you came for, not every
> other thing you happen to notice along the way — save those for their own
> PRs.

---

## 3 · Turn it into a pull request

1. Scroll down. Below the editor, GitHub asks how to save your change. Write
   a short, specific commit title — *"Link the Missing Manual chapter
   reference in Ch. 4"*, not *"fix typo"*.
2. Select **Create a new branch for this commit and start a pull request**
   — not *Commit directly to the main branch*. You *can* push straight to
   `main`; that doesn't mean you should. A branch gives a reviewer something
   to read before your change ships, and it's what triggers the checks
   described in §5 below.
3. Click **Propose changes**. GitHub moves you to the **Comparing changes**
   screen — your branch on the left, `main` on the right, the diff between
   them. Check it: one line removed, one added, nothing else. That's what
   "one change per PR" looks like on screen, not just in principle.
4. Click **Create pull request** to open the title and description form.

---

## 4 · Write the PR description

Pull requests use the same four fields the issue forms do — see
[`revision-framework.md`](revision-framework.md#what-carries-over-to-pull-requests)
for the template and why each field earns its place. Filled in for the
worked example:

```
Location: ch-04-data-formats.qmd, "Missing Manual Reference"

Problem:  The callout names Chapter 20 but gives no way to
          click through to it.

Why:      A reader has to leave the page and search the
          Missing Manual site by hand to find the chapter.

Change:   Wrapped the existing text in a Markdown link to
          the chapter's page.
```

Unlike issues, PR titles aren't prefixed for you — write one that names the
change, not the fact that you made one:

> ✗ "Update ch-04-data-formats.qmd"
> ✓ "Link the Missing Manual chapter reference in Ch. 4"

If you used a tool to help draft or diagnose the fix, disclose it in the
description — same standard the book holds itself to.

Click **Create pull request**. It's open.

---

## 5 · What happens after you click "Create pull request"

Two separate automated jobs touch your change — one before it merges, one
after.

**Before merge — the render check.** Opening (or updating) a PR that touches
a `.qmd` file automatically runs a full `quarto render` of the whole book,
not just your chapter — this catches anything your edit might have broken
elsewhere, like a cross-reference that no longer resolves. A green check
means the book still builds with your change in it. A red check means
something broke; open the check's log; the failing file and line are
usually named directly in the output.

**The review.** A classmate reads your diff and leaves comments — that's the
other half of Friday. Push a follow-up commit to the *same* branch if a
change is needed (the same **Edit this file** pencil-icon flow, but now
you're committing to your existing PR branch instead of creating a new one),
or reply to explain your reasoning if you disagree.

**After merge — publishing.** Merging your PR pushes your change to `main`,
which triggers a second, separate job: the book is rendered again in full
and the result is published to the live site. This takes a few minutes.
Reload the chapter afterward — your fix is live.

> **Note:** if the render check goes red, the fix is almost always in your
> edit, not the workflow. Common causes: a stray Quarto cross-reference
> (`@sec-...`, `@fig-...`) copied from somewhere it doesn't apply, or a
> broken code fence. Fix it in the same editor, on the same branch — the
> check reruns automatically on the new commit.

That loop — reader finds a gap, edits, opens a PR, gets reviewed, merges,
republishes — is the whole workflow. Every step happened in a browser tab.
