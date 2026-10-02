# Week 7 handouts: images

The three Friday handouts (`../triage-an-issue.md`,
`../review-a-pull-request.md`, `../issue-to-pull-request.md`) use the
figures below.

## Annotated, from week 4's captures

The instructor captured these four screenshots of GitHub's web editor for
week 4 (`slides/week-04/img/handout_*.png`, September 2026). Each
`*_annotated.tex` file here draws numbered markers on one of them. `make
figures` in `handouts/` builds the `*_annotated.pdf` and `*_annotated.png`
files, and the handouts show the PNG.

| File | Source capture | Markers |
|---|---|---|
| `edit-this-page_annotated.png` | `handout_edit_this_page.png` | (1) Edit this page |
| `editor-search_annotated.png` | `handout_editor_search.png` | (1) the editor's search bar, (2) the line it found |
| `preview-diff_annotated.png` | `handout_preview_diff.png` | (1) Preview, (2) the old line, (3) the new line, (4) Commit changes… |
| `commit-dialog_annotated.png` | `handout_commit_branch_choice.png` | (1) Commit message, (2) Create a new branch…, (3) the button that then says Propose changes |

## To capture by hand

These screens appear only when someone is signed in to GitHub, so they are
hand captures. Each handout marks the place for one with an HTML comment,
`<!-- Screenshot to add: img/NAME.png -->`.

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
4. Save the PNG here with its file name. In the handout, replace the
   comment with an image line and a caption that names what it shows, as in
   `../issue-to-pull-request.md`.
