# Week 8 handouts: images

`../revise-a-pull-request.tex` (`make` in `handouts/`) shows how to revise a
pull request in the browser. Every screen it shows is GitHub's, seen signed
in, so every figure is a hand capture.

## Captured

The instructor captured these on 2026-10-06, signed in, in GitHub's dark
theme, and saved them here without their metadata.

| File | Handout | Shows |
|---|---|---|
| `pr-suggestion.png` | Step 2 | The suggestion on the "Netwrok" line, with **Apply suggestion** and **Add suggestion to batch** (763 px wide). |
| `pr-comment.png` | Step 3 | The comment on the `curl` line in **Files changed**: "Please give the flag's long form too…". |
| `pr-conflict-editor.png` | Step 4 | The conflict editor: **1 conflict**, the gray **Mark as resolved**, the three **Accept** links, and lines 709–713. |

The captures corrected the handout's labels. GitHub's button is now
**Apply suggestion**, which opens a commit box; it was **Commit
suggestion**. The conflict editor adds **Accept current change**,
**Accept incoming change**, and **Accept both changes** above each conflict,
and keeps **Mark as resolved** gray until no marker line is left.

## To capture by hand

Each figure shows textbook #228, the instructor's demonstration pull request
([cuinfoscience/Web-Data-Science-Book#228](https://github.com/cuinfoscience/Web-Data-Science-Book/pull/228)).
#228 is set up for these screens:

- Its base is `demo/week08-base`, a copy of `main`, so it can never change `main`.
- Its review has a suggestion (the typo "Netwrok") and a comment on the `curl` line.
- `demo/week08-base` changed the same `curl` line after #228 opened, so #228 has a conflict.

No student's name, picture, or work shows in it. Close it after the
captures, and delete both `demo/week08-*` branches.

The handout calls `\handcapture{NAME.png}{...}{...}` where each figure
belongs. The figure prints once `img/NAME.png` exists, with its caption and
number, and is left out until then.

| File | Handout | Screen and state |
|---|---|---|
| `pr-edit-commit.png` | Step 3 | After **Files changed** → **⋯** → **Edit file** on `ch-05-protocols.qmd`, and an edit to the `curl` line: the **Commit changes** dialog, with a message typed and **Commit directly to the `demo/week08-revise` branch** selected. Cancel; commit nothing. |
| `pr-rerequest.png` | Step 5 | The right-hand sidebar's **Reviewers** section, with the pointer on the circular arrows, **Re-request review**. On #228, the author is also the reviewer, so the arrows may not show. If they don't, capture this one from another pull request of your own after someone else has reviewed it. |

For each capture:

1. Make the browser window about 1000 pixels wide (the slides' rule in
   `slides/common/AUTHORING.md`: 800×600 by default, up to 1024×768).
2. Capture each screen before you click its button. Then the next screen
   still has its problem to show. Take step 4's capture before you commit
   either fix, or after: the conflict stays until it is resolved.
3. Save the PNG here under its file name, and run `make` in `handouts/`.
   For numbered markers, add a `NAME_annotated.tex` like week 7's, run
   `make figures`, and point the handout's `\handcapture` line at the
   annotated PDF.
4. Check the button labels in the handout's steps against the capture:
   GitHub renames buttons now and then.
