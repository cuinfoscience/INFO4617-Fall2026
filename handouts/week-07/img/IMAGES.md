# Week 7 handouts: images

The three Friday handouts are LaTeX files built to PDF
(`../triage-an-issue.tex`, `../review-a-pull-request.tex`,
`../issue-to-pull-request.tex`; `make` in `handouts/`). They use the figures
below.

## Annotated, from week 4's captures

The instructor captured four screenshots of the book and of GitHub's web
editor for week 4 (`slides/week-04/img/handout_*.png`, September 2026). Each
`*_annotated.tex` file here draws numbered markers on one of them. `make
figures` in `handouts/` builds the `*_annotated.pdf` that the handouts print,
and a `*_annotated.png` copy.

| File | Source capture | Markers | Handout |
|---|---|---|---|
| `book-page_annotated` | `handout_edit_this_page.png` | (1) Table of contents, (2) Report an issue | Triage, step 2 |
| `diff-markdown_annotated` | `handout_preview_diff.png` | (1) the removed line, (2) the added line, (3) a link, (4) the empty line above a callout | Review, step 3 |
| `edit-this-page_annotated` | `handout_edit_this_page.png` | (1) Edit this page | Issue to pull request, step 2 |
| `editor-search_annotated` | `handout_editor_search.png` | (1) the editor's search bar, (2) the line it found | Issue to pull request, step 3 |
| `preview-diff_annotated` | `handout_preview_diff.png` | (1) Preview, (2) the old line, (3) the new line, (4) Commit changes… | Issue to pull request, step 3 |
| `commit-dialog_annotated` | `handout_commit_branch_choice.png` | (1) Commit message, (2) Create a new branch…, (3) the button that then says Propose changes | Issue to pull request, step 4 |

GitHub's own pages were not captured automatically: this environment
can't read github.com's robots.txt, and every issue on the textbook is a
student's.

## To capture by hand

These screens appear only when someone is signed in to GitHub, so they are
hand captures. Each handout calls `\handcapture{NAME.png}{...}{...}` where
one belongs: the figure prints once `img/NAME.png` exists, with its caption
and number, and is left out until then.

| File | Handout | Screen and state |
|---|---|---|
| `issue-page.png` | Triage, step 1 | An open issue filed with the Gap or Broken form: the form's answers and the right-hand sidebar, with **Development** in view. |
| `issue-comment.png` | Triage, step 4 | The bottom of the same issue: a triage comment typed in the box and not posted, with **Comment** and **Close issue** in view. |
| `pr-checks.png` | Review, step 2 | The bottom of a pull request's **Conversation** tab: its checks (**Render**, **Notebook sync**, **Trope lint**) and the merge box. |
| `pr-line-comment.png` | Review, step 4 | **Files changed**, with the comment box open on one line after clicking **+**: a comment typed, and **Add a suggestion**, **Start a review**, and **Add single comment** in view. Nothing submitted. |
| `pr-review-changes.png` | Review, step 5 | The **Review changes** panel open: the summary box and the three options. Nothing submitted. |
| `pr-template.png` | Issue to pull request, step 5 | The *Open a pull request* form with the template in the description box, before **Create pull request**. |
| `pr-edit-file.png` | Issue to pull request, step 6 | **Files changed** on your own pull request, with the file's **⋯** menu open on **Edit file**. |

For each capture:

1. Use a pull request or an issue of your own, such as textbook #50 or
   #194, so that no student's name, picture, or work shows. If a student's
   name shows anyway, cover it with a redact box.
2. Make the browser window about 1000 pixels wide (the slides' rule in
   `slides/common/AUTHORING.md`: 800×600 by default, up to 1024×768).
3. Type text, capture, then cancel. Submit nothing.
4. Save the PNG here under its file name, and run `make` in `handouts/`.
   For numbered markers, add a `NAME_annotated.tex` like the ones above, run
   `make figures`, and point the handout's `\handcapture` line at the
   annotated PDF.
5. Check the labels in the handout's steps against the capture: GitHub
   renames buttons now and then.
