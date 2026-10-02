# Triage an issue

*Week 7 Friday activity · easy · about 10 minutes an issue — INFO 4617 Web Data Science*

To triage an issue, you check it against the book as it is today. Then you
leave one comment that says what should happen next. You change nothing in
the book.

Triage makes the other two activities faster. A pull request needs an issue
that is still a problem, and a reviewer needs to know what the issue asks for.

Your chapter's board in week 7's slides lists the issues to triage. A line
like `#15 → #59?` asks one question: does pull request #59 fix issue #15?

| Activity | Difficulty | Handout |
|---|---|---|
| **Triage an issue** | easy | this page |
| Review a pull request | medium | [`review-a-pull-request.md`](review-a-pull-request.md) |
| Issue to pull request | hard | [`issue-to-pull-request.md`](issue-to-pull-request.md) |

Work in pairs. One partner works in the browser, and the other reads this
page aloud.

---

## 1 · Open the issue

1. Sign in to GitHub.
2. Open the issue. Its address is
   `https://github.com/cuinfoscience/Web-Data-Science-Book/issues/` followed
   by its number, for example `.../issues/110`.
3. Read the answers on the form:
   - **Where were you?** gives the chapter;
   - **Which section or heading?** gives the place in the chapter;
   - the long answers say what went wrong, or what is missing.
4. Read the comments under the issue. If someone has already triaged it, go
   to the next issue on your board.

<!-- Screenshot to add: img/issue-page.png (see img/IMAGES.md) -->

## 2 · Check it against the book

1. Open the book: <https://cuinfoscience.github.io/Web-Data-Science-Book/>
2. Go to the chapter and the section that the issue names.
3. Look for the problem. The book changes every week, so the problem may
   already be fixed.

## 3 · Look for a pull request, and for a twin

1. **A pull request.** On the issue page, look at **Development** in the
   right-hand sidebar. Then look down the issue's timeline: a pull request
   that names the issue shows as *mentioned this*, with its number. Open the
   pull request, and read what it changes.
2. **A twin.** Click the **Issues** tab. Search for a word from the title,
   such as `traceroute`. Is another open issue about the same problem?

## 4 · Leave one comment

Find the row that matches what you found. Copy its comment, and change the
numbers and the words.

| You found | Comment |
|---|---|
| A pull request fixes it | `#59 fixes this when it merges: it adds the output that this issue asks for.` |
| A pull request fixes part of it | `#59 adds the output. The second half, a note about rate limits, is still open.` |
| Another issue reports the same problem | `Duplicate of #13` |
| The book already fixed it | `Fixed in the book: "Technical Norms: robots.txt" now shows the output (checked October 2).` |
| It is still a problem, with no pull request | `Still a problem in "Traceroute" (checked October 2). Size: small.` |
| You can't tell what it asks for | `Suggested title: "Gap: Ch. 5 doesn't say what a hop is". Is that what you meant?` |

Use one of three sizes:

- **small**: a sentence or a link;
- **medium**: a paragraph or one code cell;
- **large**: a section, or more than one file.

End the comment with your partner's GitHub name: `Triaged with @partner`.
Then click **Comment**.

<!-- Screenshot to add: img/issue-comment.png (see img/IMAGES.md) -->

---

## Do not

- **Do not click Close issue.** I close issues after class.
- **Do not change the labels or the assignees.**
- **Do not fix the problem in this activity.** An issue that is still a
  problem is ready for the hard activity:
  [Issue to pull request](issue-to-pull-request.md).

## Next

Triage the next issue on your board. When your chapter's triage is done,
[review a pull request](review-a-pull-request.md).
