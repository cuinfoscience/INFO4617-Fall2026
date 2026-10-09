# Run-of-show: the backlog sprint, Friday, October 9

Week 8's Friday follows the week 7 standup
([run-of-show](2026-10-02-standup-run-of-show.md)). The slides are week 8's
Friday section, from "Since last Friday" to "A good revision, and a good
review". The instructor decided on October 7:

- The class splits into three groups, and each student picks one:
  - **issue → pull request**, with week 7's `issue-to-pull-request.pdf`;
  - **pull request → merged**:
    - students with an open pull request answer its review with
      week 8's `revise-a-pull-request.pdf`;
    - the others review a classmate's with week 7's
      `review-a-pull-request.pdf`;
  - **a new Chapter 8 pull request**, from the revision menu.
- The slides open with a summary of the cleanup sprint. They name Claude Code,
  say why 11 pull requests closed, and say that a closed pull request still
  counts.
- Submissions stay individual. Pull requests, reviews, comments, and issues
  all count.
- The class tries GitHub's project tools: assignees, chapter and status
  labels, and a project board. Issue types are not used yet.

## Before class

1. **Give the class Triage on the textbook repository.** Triage lets a
   student apply labels, assign people, and request reviews. It also lets
   them close and reopen issues and pull requests, which is why "Claim it on
   GitHub" asks them not to. It doesn't let them merge. Their approvals don't
   count toward a required review either.
   ([GitHub's role table](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization))
2. **Make the "Textbook backlog" project**. "Labels say what's next" names
   it, so make it before class (steps below).
3. **Close #27** as a duplicate of #15. Its triage comment says so, and it
   has the `duplicate` label.
4. **Recount** if pull requests merge or close before Friday. The queries
   are below. Change the counts on "Since last Friday" and the chapter
   boards, and move the labels to match.
5. **Fill in "Daily note questions"** if the daily note brought any.
   `check_daily_questions.py` flags week 8 because the deck has no such
   frame yet.

## The labels (made October 7)

Claude Code made 23 labels on the textbook repository and applied them to
all 45 open issues and to the 37 open pull requests from students. On
October 8 it labeled two Chapter 8 pull requests opened the evening before,
#238 and #239. The instructor's demonstration pull request, #228, has none. Each item has one
chapter label and one status label, except #27, which has `duplicate`.

| Label | Color | Applied to |
|---|---|---|
| `ch-01` to `ch-15`, `whole book` | `c5def5` | the chapter an item is about; for a pull request, the chapter its `.qmd` change is in |
| `status: needs triage` | `ededed` | 5 issues with no triage comment: #19, #22, #29, #49, #64 |
| `status: needs info` | `d4c5f9` | 6 issues whose triage comment asks the author a question: #24, #70, #85, #177, #185, #207 |
| `status: needs PR` | `fbca04` | 26 issues whose triage comment says "Still a problem", gives a size, and says how to turn it into a pull request |
| `status: has PR` | `bfdadc` | 7 issues that an open pull request works on: #15, #28, #43, #133, #175, #189, #206 |
| `status: needs review` | `1d76db` | 4 pull requests with no review: #78, #237, and the new #238 and #239 |
| `status: changes requested` | `e99695` | the other 35 pull requests, each reviewed on October 5 |
| `status: approved` | `0e8a16` | none yet |

The plan asked for five status labels. Two more were needed, because 11
issues aren't ready for a pull request: `needs triage` and `needs info`.

Students change a status label as their work moves on ("Labels say what's
next"):

- open a pull request: `needs review` on it, and `has PR` on its issue;
- push a revision: `needs review`;
- request changes: `changes requested`;
- approve: `approved`.

## Making the board

A GitHub project can't group its board by labels, but it can filter by them
with **Slice by**
([table layout](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-table-layout),
[board layout](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-board-layout)).
So the labels stay the record of each item's status, and the project is a
view of them. These steps make the view the slide describes, where you click
a label on the left.

1. On the cuinfoscience organization's **Projects** tab, click **New
   project**. Choose **Table**, and name it `Textbook backlog`. A project
   must belong to the organization that owns the repository to show on the
   repository's tab.
2. In the project's **Settings**, set **Visibility** to **Public**. Students
   who aren't organization members can then see it. Everything on it comes
   from the public textbook repository.
3. Add the open items. On the textbook's **Issues** tab, select all the open
   issues. Click **Projects** above the list, and choose `Textbook backlog`.
   Do the same on the **Pull requests** tab. Then remove #228.
   ([adding items](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project))
4. Add new items automatically. Open the project's menu (**…**), then
   **Workflows**, then **Auto-add to project**. Choose the textbook
   repository, keep the filter `is:issue,pr is:open`, and click **Save and
   turn on workflow**. It adds items only when they are created or updated,
   which is why step 3 comes first. GitHub Free allows one auto-add
   workflow per project.
   ([auto-add](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically))
5. In the table view, show the **Labels**, **Assignees**, **Reviewers**, and
   **Linked pull requests** fields, and choose **Slice by: Labels**. The left
   panel then lists every label with its count.
6. Link the project to the repository. On the textbook's **Projects** tab,
   click **Link a project**, and choose `Textbook backlog`.
   ([linking](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/adding-your-project-to-a-repository))

**Optional: a board view.** A board's columns come from a single-select
field, such as the project's own **Status** field, not from labels. Give
Status the seven status values and turn on the built-in workflows that set
it: **Code changes requested**, **Code review approved**, **Pull request
merged**, and **Item closed**. The board then follows reviews and merges on
its own. It doesn't follow a label that a student changes by hand, so the
two can disagree. If they do, trust the label.

## The counts and how they were made

Every count on "Since last Friday", "Why 11 closed", and the chapter boards
comes from the textbook's REST API. They were read on October 7, 2026 with
`per_page=100`, and every list was paged to its end:

- `repos/cuinfoscience/web-data-science-book/pulls?state=all` (164 pull
  requests) and `…/issues?state=all` (236 issues and pull requests);
- for each open pull request: `…/pulls/N` (for its merge state, read twice,
  because GitHub works out mergeability on the first request),
  `…/pulls/N/files`, `…/pulls/N/reviews`, and `…/issues/N/timeline`;
- for each open issue, and each pull request closed since October 2:
  `…/issues/N/timeline`.

The boards read these as follows:

- "Last Friday" is October 2, 10 a.m. Mountain. Then, 50 pull requests from
  students and 53 issues were open. On October 8, 39 and 45 were: the 37
  read on October 7, plus #238 and #239.
- Since then, 19 pull requests from students merged, 18 of them on Monday
  night, October 5. 11 closed without merging, and 13 issues closed.
- The maintainer's account posted 35 reviews on October 5, each asking for
  changes, and 48 issue comments on October 7. They end with "Generated by
  Claude Code".
- A pull request's chapter is the `.qmd` file it changes. #102 also changes
  chapters 6 and 7, through commits made after its review, and #180 and
  #201 change notebooks of other chapters. The boards list each under its
  title's chapter.
- "(conflict)" marks a pull request whose `mergeable_state` was `dirty`:
  #52, #79, #89, #93, #99, #102, #122, #180, #191.
- A size, "(small)", "(medium)", or "(large)", is the one in the issue's
  triage comment.

The 11 closed pull requests, and the reason each closing review gives:

| Reason | Pull requests |
|---|---|
| A classmate's pull request made the same fix | #88 (#93 continues), #101 (#212 merged), #127 (#113 merged), #130 (#188 merged) |
| Chapter 5 dropped Scapy on October 2 | #106, #111, #112 |
| Nothing left to merge | #62 (edited a generated notebook, for Python 3.11.9), #171 (head `main`, base the issue branch) |
| The cause was something else | #203 (the Availability API sometimes answers empty) |
| Closed on October 2, before the cleanup | #121 |

## After class

1. Merge the approved pull requests with merge commits. Merging closes the
   issues they name.
2. Regenerate the notebooks once, so that Notebook sync goes green again.
3. Check the status labels against the pull requests' reviews, and fix any
   that disagree.
