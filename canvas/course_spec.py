"""Declarative spec for the Fall 2026 INFO 4617 Canvas course.

This is the single source of truth for what the migrated course should look
like: the teaching calendar, assignment groups and weights, the weekly
assignments, the module layout, and the syllabus page. `migrate.py` reads this
and makes Canvas match it.

Everything here is derived from `syllabus/syllabus.tex` and the weekly decks in
`slides/`. If the syllabus changes, change it here too.
"""

from datetime import date, datetime, time
from pathlib import Path
from zoneinfo import ZoneInfo

# --------------------------------------------------------------------------
# Course identity
# --------------------------------------------------------------------------

OLD_COURSE_ID = 109074          # INFO 4871, Fall 2024 (source)
NEW_COURSE_ID = 143304          # INFO 4617, Fall 2026 (target)

COURSE_NAME = "Web Data Science"
COURSE_CODE = "INFO 4617"
TERM = "Fall 2026"
MEETING = "Mondays, Wednesdays & Fridays, 12:20–1:10 pm"
ROOM = "CASE W262"

INSTRUCTOR = "Brian C. Keegan, Ph.D."
INSTRUCTOR_TITLE = "Associate Professor, Department of Information Science"
INSTRUCTOR_EMAIL = "brian.keegan@colorado.edu"
INSTRUCTOR_OFFICE = "INFO 129"
OFFICE_HOURS = "TBD — posted on Canvas"     # placeholder, mirrors the syllabus

BOOK_URL = "https://github.com/cuinfoscience/Web-Data-Science-Book"
# Rendered Quarto site. Students read here; the repo above is for editing.
BOOK_SITE_URL = "https://cuinfoscience.github.io/Web-Data-Science-Book"
REPO_URL = "https://github.com/cuinfoscience/INFO4617-Fall2026"

TZ = ZoneInfo("America/Denver")

# Semester bounds and non-meeting days (CU Boulder Fall 2026 academic calendar)
FIRST_DAY = date(2026, 8, 20)   # Thursday — so week 1 meets Friday only
LAST_DAY = date(2026, 12, 4)    # Friday — follows a Monday schedule
LABOR_DAY = date(2026, 9, 7)
FALL_BREAK = (date(2026, 11, 23), date(2026, 11, 27))
FINAL_DUE = date(2026, 12, 7)   # project repo + write-up, Monday of finals week (syllabus)

CU_GOLD = "#CFB87C"
CU_DARK = "#565A5C"

# --------------------------------------------------------------------------
# Weekly plan: (week, module, chapter, topic, notebook slug, chapter file, note)
# --------------------------------------------------------------------------

WEEKS = [
    (1,  "Foundations", 1,  "Introduction & setup",
     "ch-01-introduction", "ch-01-introduction.qmd",
     "Semester starts Thursday — we meet Friday only this week."),
    (2,  "Foundations", 2,  "Ethics, law & responsible collection",
     "ch-02-ethics", "ch-02-ethics.qmd", None),
    (3,  "Foundations", 3,  "The post-API age",
     "ch-03-post-api", "ch-03-post-api.qmd", None),
    (4,  "Foundations", 4,  "Data formats: XML & JSON",
     "ch-04-data-formats", "ch-04-data-formats.qmd",
     "No class Monday, September 7 (Labor Day). Concepts move to Wednesday."),
    (5,  "Foundations", 5,  "Web architecture & protocols",
     "ch-05-protocols", "ch-05-protocols.qmd", None),
    (6,  "Documents", 6,  "Parsing static web pages",
     "ch-06-static-pages", "ch-06-static-pages.qmd", None),
    (7,  "Documents", 7,  "Archived web pages & the Wayback Machine",
     "ch-07-archives", "ch-07-archives.qmd", None),
    (8,  "Documents", 8,  "Dynamic web pages with Selenium",
     "ch-08-dynamic-pages", "ch-08-dynamic-pages.qmd", None),
    (9,  "Documents", 9,  "Extracting data from PDFs",
     "ch-09-pdfs", "ch-09-pdfs.qmd", None),
    (10, "APIs", 10, "Wikipedia APIs",
     "ch-10-wikipedia", "ch-10-wikipedia.qmd",
     "Final Project proposal due Sunday, October 25."),
    (11, "APIs", 11, "Government data APIs",
     "ch-11-government", "ch-11-government.qmd", None),
    (12, "APIs", 12, "Social & media platform APIs",
     "ch-12-social", "ch-12-social.qmd", None),
    (13, "APIs", 13, "AI & language-model APIs",
     "ch-13-ai-apis", "ch-13-ai-apis.qmd", None),
    (14, "Practice", 14, "Automating data collection",
     "ch-14-automation", "ch-14-automation.qmd", None),
    (15, None, None, "Fall Break — no class", None, None,
     "Fall Break, November 23–27. University closed November 26 & 27."),
    (16, "Practice", 15, "Research design & final presentations",
     "ch-15-research-design", "ch-15-research-design.qmd",
     "December 4 is the last day of class and follows a Monday schedule."),
]

# Weeks that run a Wednesday notebook lab and a Friday textbook-revision workshop.
# Week 1 is orientation (Friday only), week 15 is Fall Break, and week 16 runs a
# project workshop and final presentations instead.
TEACHING_WEEKS = [w for w in range(2, 15)]
# Week 10 (the proposal week) has no lab or revision assignment in Canvas, by
# the instructor's decision on 2026-10-23.
NO_ASSIGNMENT_WEEKS = {10}

# --------------------------------------------------------------------------
# Assignment groups (weights come straight from the syllabus: 30/15/15/40)
# --------------------------------------------------------------------------

GROUPS = [
    {
        "name": "Notebook Labs",
        "group_weight": 30,
        "position": 1,
        # The syllabus drops the two lowest lab scores.
        "rules": "drop_lowest:2\n",
        "blurb": "Wednesday labs, due the following Sunday. Graded on "
                 "participation and completion; your two lowest scores are dropped.",
    },
    {
        "name": "Textbook Revisions",
        "group_weight": 15,
        "position": 2,
        "rules": "",
        "blurb": "Friday workshops, due the following Sunday. Pull requests to "
                 "the Web Data Science book plus the peer reviews you provide.",
    },
    {
        # One 1-point entry per meeting week (see attendance_assignments).
        # Canvas ignores ungraded assignments in the running total, so the
        # weight takes effect as attendance is actually recorded.
        "name": "Attendance",
        "group_weight": 15,
        "position": 3,
        "rules": "",
        "blurb": "Attendance is required. The methods are cumulative, so missed "
                 "sessions are hard to recover from.",
    },
    {
        "name": "Final Project",
        "group_weight": 40,
        "position": 4,
        "rules": "",
        "blurb": "Proposal, in-class presentation, and the project repository "
                 "and write-up.",
    },
]

LAB_POINTS = 10
# Textbook Revisions are credit/no credit: 1 point for any issue, pull request,
# or comment that lands on GitHub in a class repository (the book, this repo,
# or the Missing Manual). Set in Canvas on 2026-10-23; docs/course-facts.md.
REVISION_POINTS = 1
# Canvas weights the assignments inside a group by their points, so these must
# stay in the ratio 5 : 10 : 25 to give the syllabus's split of the Final
# Project's 40%. The proposal's rubric (PROPOSAL_RUBRIC) is 10 criteria x 3
# points = 30, so the other two parts are 60 and 150. Change all three together.
FINAL_PARTS = [
    ("Final Project — Proposal", 30, date(2026, 10, 25),
     "A research question; your data source(s) and method; and an ethics and "
     "feasibility check, with one record you retrieved. The assignment page is "
     "PROPOSAL_DESCRIPTION, below."),
    ("Final Project — Presentation", 60, LAST_DAY,
     "Present your project to the class during the final week. Bring your data, "
     "one or two visualizations that carry an argument, and what surprised you."),
    ("Final Project — Repository & Write-up", 150, FINAL_DUE,
     "Your project repository (code, data or collection scripts, and a README "
     "someone else could follow) plus the written analysis. Due during finals "
     "week; there is no final exam."),
]


# --------------------------------------------------------------------------
# Calendar helpers
# --------------------------------------------------------------------------

def week_monday(week_number: int) -> date:
    """Monday of the given teaching week (week 1's Monday is Aug 17, 2026)."""
    from datetime import timedelta
    return date(2026, 8, 17) + timedelta(weeks=week_number - 1)


def meeting_days(week_number: int):
    """Actual Mon/Wed/Fri meeting dates for a week, minus holidays."""
    from datetime import timedelta
    monday = week_monday(week_number)
    days = [monday + timedelta(days=d) for d in (0, 2, 4)]
    brk_start, brk_end = FALL_BREAK
    return [
        d for d in days
        if FIRST_DAY <= d <= LAST_DAY
        and d != LABOR_DAY
        and not (brk_start <= d <= brk_end)
    ]


def due_at(day: date, hour: int = 23, minute: int = 59) -> str:
    """ISO8601 timestamp in Mountain time, which Canvas stores correctly."""
    return datetime.combine(day, time(hour, minute), tzinfo=TZ).isoformat()


def lab_day(week_number: int):
    """The Wednesday of a week (the notebook lab meets in class)."""
    return next((d for d in meeting_days(week_number) if d.weekday() == 2), None)


def revision_day(week_number: int):
    """The Friday of a week (the textbook-revision workshop meets in class)."""
    return next((d for d in meeting_days(week_number) if d.weekday() == 4), None)


def sunday_of(week_number: int):
    """The Sunday that closes a teaching week — when its work is due.

    Labs and revisions meet on Wednesday and Friday but are both due the
    following Sunday night, so students have the weekend. lab_day() and
    revision_day() still decide *whether* a week runs each session; this
    only sets the deadline.
    """
    from datetime import timedelta
    return week_monday(week_number) + timedelta(days=6)


def week_info(week_number: int):
    """Look up the WEEKS row for a week number."""
    for row in WEEKS:
        if row[0] == week_number:
            return row
    raise KeyError(f"no such week: {week_number}")


def chapter_url(chapter_file: str) -> str:
    """Link the rendered chapter, not the .qmd source: students read the site.
    Takes the source filename (ch-02-ethics.qmd) so the week table stays the
    single place a chapter is named."""
    slug = chapter_file.removesuffix(".qmd")
    return f"{BOOK_SITE_URL}/{slug}.html"


def notebook_url(slug: str) -> str:
    return f"{BOOK_URL}/blob/main/notebooks/{slug}.ipynb"


def slides_url(week_number: int) -> str:
    return f"{REPO_URL}/blob/main/slides/week-{week_number:02d}/week-{week_number:02d}.pdf"


def lab_items(week_number: int) -> list:
    """Links to the week's lab notebook and its key, placed in Wednesday's lab
    after the companion notebook (after the slides in week 1, which has no
    Wednesday).
    Empty for a week with no lab on disk (labs/week-NN/lab-NN.ipynb), so a
    held lab stays out of Canvas until it's merged."""
    nn = f"{week_number:02d}"
    if not (Path(__file__).resolve().parent.parent / "labs" / f"week-{nn}" / f"lab-{nn}.ipynb").exists():
        return []
    base = f"{REPO_URL}/blob/main/labs/week-{nn}"
    return [
        {"type": "ExternalUrl", "title": f"Lab: lab-{nn}.ipynb",
         "external_url": f"{base}/lab-{nn}.ipynb", "new_tab": True},
        {"type": "ExternalUrl", "title": f"Lab key: lab-{nn}-key.ipynb",
         "external_url": f"{base}/lab-{nn}-key.ipynb", "new_tab": True},
    ]


# --------------------------------------------------------------------------
# Assignment construction
# --------------------------------------------------------------------------

def lab_assignments():
    """One notebook lab per teaching week, met Wednesday and due that Sunday."""
    out = []
    for wk in TEACHING_WEEKS:
        _, _, ch, topic, slug, chfile, _ = week_info(wk)
        if lab_day(wk) is None or wk in NO_ASSIGNMENT_WEEKS:
            continue
        out.append({
            "group": "Notebook Labs",
            "name": f"Week {wk} Lab — {topic}",
            "points_possible": LAB_POINTS,
            "due_at": due_at(sunday_of(wk)),
            # HTML export only: the file shows code and output together,
            # and the upload widget refuses anything but .html
            "submission_types": ["online_upload"],
            "allowed_extensions": ["html", "htm"],
            "description": (
                f"<p>Read <a href=\"{chapter_url(chfile)}\">Chapter {ch}: "
                f"{topic}</a> and work through its code in the companion "
                f"notebook — we do this together in Wednesday's lab.</p>"
                f"<p>The take-home is the chapter's <strong>Recommended "
                f"Exercises</strong>: a guided, step-by-step build at the end "
                f"of the notebook. Fill in each empty code cell and answer the "
                f"final interpretation step in your own words.</p>"
                f'<p><strong>Notebook:</strong> <a href="{notebook_url(slug)}">'
                f"{slug}.ipynb</a></p>"
                "<p><strong>Submit your completed notebook as HTML</strong>, "
                "with all cells run so your code and its output are both "
                "visible. In JupyterLab: <em>File &rarr; Save and Export "
                "Notebook As&hellip; &rarr; HTML</em> (see the "
                '<a href="https://jupyterlab.readthedocs.io/en/stable/user/'
                'export.html">JupyterLab export guide</a>), then upload the '
                "<code>.html</code> file here.</p>"
                "<p>The <em>Additional Exercises</em> are optional "
                "extensions — worth your time, not required. Labs are graded "
                "on participation and completion rather than perfection — "
                "come with questions, work with a partner, and bring something to "
                "show-and-tell: a challenging bug, interesting data, or a provocation "
                "for a research design.</p>"
            ),
        })
    return out


# Week 3 is the browser-only on-ramp: students read and comment on the open
# issues and see a web-editor pull request demonstrated. The deliverable is an
# issue or a substantive comment; the pull-request deliverable starts later.
COMMENT_WEEKS = {3}

ISSUE_QUEUES = (
    ("Web Data Science book", "https://github.com/cuinfoscience/Web-Data-Science-Book/issues"),
    ("course repository", "https://github.com/cuinfoscience/INFO4617-Fall2026/issues"),
    ("Missing Manual", "https://github.com/cuinfoscience/INFO-Missing-Manual/issues"),
)


def _comment_week_description(ch, topic, chfile):
    queues = ", ".join(f'<a href="{url}">{name}</a>' for name, url in ISSUE_QUEUES)
    return (
        f"<p>Keep improving "
        f'<a href="{chapter_url(chfile)}">Chapter {ch}: {topic}</a>. This week the '
        f"work happens in the browser: read the open issues, then either "
        f"<strong>file a new issue</strong> or <strong>add a substantive comment</strong> "
        f"to an existing one — a reproduction, a missing location or piece of "
        f"evidence, a scoping proposal, or a claim that you will tackle it.</p>"
        f"<p><strong>Submit:</strong> the URL of your issue or your comment. "
        f"Issues in the {queues} all count. Pull requests are demonstrated in "
        f"class and welcome, not required this week.</p>"
        "<p>A strong issue or comment is <em>located</em> (chapter, section, and "
        "file), <em>evidenced</em> (the passage, command, or output), and "
        "<em>actionable</em> (a concrete change someone else could make). "
        "&ldquo;I agree&rdquo; earns nothing; a thumbs-up reaction says that for free.</p>"
    )


def _pull_request_description(ch, topic, chfile):
    return (
        f"<p>Propose a revision to "
        f'<a href="{chapter_url(chfile)}">Chapter {ch}: {topic}</a> as a '
        f"<strong>pull request</strong> to the "
        f'<a href="{BOOK_URL}">Web Data Science book</a>, and review two '
        f"classmates' pull requests.</p>"
        "<p><strong>Submit:</strong> the URL of your pull request. Leave "
        "your two reviews on classmates' pull requests on GitHub — they "
        "are visible from your account, so no separate links are needed.</p>"
        "<p>A strong PR makes one focused change, explains the problem it fixes, "
        "builds without errors, matches the book's voice, and discloses any AI "
        "assistance. A strong review runs or reads the change, names specifics, "
        "separates &ldquo;must fix&rdquo; from &ldquo;nice to have,&rdquo; and ends "
        "with a clear verdict.</p>"
    )


# Canvas titles that differ from the "Chapter N" pattern. build matches
# assignments by name, so a title here must match Canvas exactly.
REVISION_TITLES = {2: "First issue on Chapter 2"}


# Weeks 11-14 of Textbook Revisions are project-portfolio checkpoints instead
# of textbook pull requests: each student builds their Final Project repo on
# their own GitHub account, one stage a week, ending close to the final
# submission. Each is 2 points (two 1-point criteria, PORTFOLIO_RUBRICS).
# Week 14's is due after Fall Break.
PORTFOLIO_POINTS = 2
_PORTFOLIO_INTRO = (
    "<p>From week 11, the Friday revision block builds your Final Project as a "
    "public portfolio: one GitHub repository on your own account that you "
    "update each week. <strong>Submit the URL of your repository.</strong> It "
    "is graded on what has been pushed by the deadline.</p>")
_PORTFOLIO_DATA_NOTE = (
    "<p>Commit your code and a small sample of your data. Leave the full raw "
    "data out where its terms of service, its size, or personal information "
    "make sharing it unwise, and say in the README what you left out and "
    "why.</p>")
PORTFOLIO_WEEKS = {
    11: {"title": "Set up your project repo", "due": None, "html": (
        "<h4>This week: set up the repository</h4><ul>"
        "<li>A <strong>public repository</strong> on your own GitHub account, "
        "with a descriptive name.</li>"
        "<li><code>README.md</code> with a title, your name, a one-paragraph "
        "summary of your research question, and placeholder sections: Data, "
        "Methods, Findings, How to reproduce.</li>"
        "<li><code>proposal.md</code>: your proposal, revised if you have had "
        "feedback.</li>"
        "<li>Placeholders for the rest: a notebook (<code>.ipynb</code>), a "
        "<code>report.md</code> (or a note that your report will be a PDF), "
        "and a <code>data/</code> folder.</li></ul>")},
    12: {"title": "Collect and clean your data", "due": None, "html": (
        "<h4>This week: collect and clean</h4><ul>"
        "<li>Collection code that runs, makes polite requests (a User-Agent "
        "that identifies you, pauses between requests), and saves the raw "
        "data.</li>"
        "<li>A cleaning step, with its code and output, that produces a tidy "
        "dataset.</li>"
        "<li>A small sample of the cleaned data in the repo, with a data "
        "dictionary: each field and what it means.</li>"
        "<li>The README's Data section: the source, when you collected it, how "
        "many records, and what you kept out of the repo and why.</li></ul>")
        + _PORTFOLIO_DATA_NOTE},
    13: {"title": "Analyze your data", "due": None, "html": (
        "<h4>This week: analyze</h4><ul>"
        "<li>An analysis notebook that runs top to bottom, with its output "
        "visible.</li>"
        "<li>Results that answer at least part of your question: the counts or "
        "comparisons your proposal named.</li>"
        "<li>At least one figure saved in the repo, with a title, labeled axes, "
        "and a one-sentence caption.</li>"
        "<li>The README's Methods section and your preliminary Findings.</li>"
        "</ul>")},
    14: {"title": "Draft your write-up", "due": date(2026, 11, 29), "html": (
        "<h4>This week: a draft close to final</h4><ul>"
        "<li>A full draft of your written document (<code>report.md</code> or "
        "<code>report.pdf</code>), with every section present, using your own "
        "results and figures and citing your sources.</li>"
        "<li>All four required files present and current: "
        "<code>README.md</code>, <code>proposal.md</code>, your notebook, and "
        "your report.</li>"
        "<li>A README complete enough that someone else could reproduce the "
        "project: setup, how to run it, and where the data came from.</li>"
        "</ul><p>Due after Fall Break, on Sunday, November 29. Your final "
        "presentation is in the following week, and the final repository and "
        "write-up are due Monday, December 7.</p>")},
}


def revision_name(wk):
    """The Canvas title of a week's Textbook Revisions assignment."""
    _, _, ch, _, _, _, _ = week_info(wk)
    if wk in PORTFOLIO_WEEKS:
        return f"Week {wk} Portfolio — {PORTFOLIO_WEEKS[wk]['title']}"
    return f"Week {wk} Revision — {REVISION_TITLES.get(wk, f'Chapter {ch}')}"


def revision_assignments():
    """One textbook-revision workshop per teaching week, met Friday and due
    that Sunday; weeks 11-14 are portfolio checkpoints (PORTFOLIO_WEEKS)."""
    out = []
    for wk in TEACHING_WEEKS:
        _, _, ch, topic, _, chfile, _ = week_info(wk)
        if revision_day(wk) is None or wk in NO_ASSIGNMENT_WEEKS:
            continue
        if wk in PORTFOLIO_WEEKS:
            pw = PORTFOLIO_WEEKS[wk]
            out.append({
                "group": "Textbook Revisions",
                "name": revision_name(wk),
                "points_possible": PORTFOLIO_POINTS,
                "due_at": due_at(pw["due"] or sunday_of(wk)),
                "submission_types": ["online_url"],
                "description": _PORTFOLIO_INTRO + pw["html"],
            })
            continue
        describe = _comment_week_description if wk in COMMENT_WEEKS else _pull_request_description
        out.append({
            "group": "Textbook Revisions",
            "name": revision_name(wk),
            "points_possible": REVISION_POINTS,
            "due_at": due_at(sunday_of(wk)),
            # URL only: the deliverable is the issue, comment, or pull request itself
            "submission_types": ["online_url"],
            "description": describe(ch, topic, chfile),
        })
    return out


ATTENDANCE_POINTS = 1

def attendance_assignments():
    """One attendance entry per week the class actually meets.

    meeting_days() already knows the calendar: week 15 falls entirely
    inside Fall Break and drops out on its own, week 1 keeps its single
    Friday, and week 16 runs through the December 4 last day. That
    yields 15 entries. Graded by the instructor -- there is nothing to
    submit -- so no due date and a "none" submission type.
    """
    out = []
    for row in WEEKS:
        wk = row[0]
        if not meeting_days(wk):
            continue
        days = ", ".join(d.strftime("%b %-d") for d in meeting_days(wk))
        out.append({
            "group": "Attendance",
            "name": f"Week {wk:02d} Attendance",
            "points_possible": ATTENDANCE_POINTS,
            "due_at": None,
            "submission_types": ["none"],
            "description": (
                f"<p>Attendance for week {wk} ({days}). Recorded by the "
                "instructor — nothing to submit. If circumstances prevent "
                "your attendance, email me so we can work out an "
                "accommodation plan.</p>"
            ),
        })
    return out


# The proposal's full assignment page, as the instructor last edited it in
# Canvas (copied 2026-10-23, with the part headings at 9 / 9 / 12 points to match
# PROPOSAL_RUBRIC). Its three parts are the ones the week 9 ("What we expect")
# and week 10 slides name; keep them in step (docs/course-facts.md, "What the
# proposal contains").
PROPOSAL_DESCRIPTION = """\
<p>The Final Project is a portfolio piece that matches a web data source with a research design. The proposal is is short, it can change, and it has two jobs: to show that your question is worth answering and to show that you can get the data to answer it.</p>
<h4>What to submit</h4>
<p>One document of about 1&ndash;2 pages (500&ndash;1,000 words, not counting the record you paste in part 3). Submit it as a PDF file or as a link to a README in your project&rsquo;s GitHub repository to Canvas by Sunday, October 25. Put your name at the top, and your partner&rsquo;s if you are working in a pair.</p>
<h4>1. A research question (9 points)</h4>
<ul>
<li><strong>A question, not a topic.</strong> Not &ldquo;Wikipedia&rdquo;, but &ldquo;Which events send readers to articles about wildfires?&rdquo; Not &ldquo;housing&rdquo;, but &ldquo;How often did Boulder&rsquo;s city council discuss housing from 2020 to 2025?&rdquo; Questions should be <em>empirical</em> (uses web data) and <em>falsifiable</em> (the answer could have many values).</li>
<li><strong>Who would care about the answer</strong>: a newsroom, a city agency, a local politician, a lawyer, a community group, researchers, or the platform&rsquo;s own users.</li>
<li><strong>What you expect to find</strong>, in a sentence or two, and what would surprise you.</li>
</ul>
<h4>2. Data source(s) and method (9 points)</h4>
<ul>
<li><strong>The exact source</strong>, with links: the URL for a website, the API endpoint, or a set of documents.</li>
<li><strong>How you will get it</strong>: an API, scraping static or dynamic pages, PDFs, web archives, or a mix. Name the chapter(s) whose methods you will use.</li>
<li><strong>The scope</strong>: which records, what time window, and roughly how many. If you will collect over time, say how often and for how long.</li>
<li><strong>The analysis</strong>: the counts, comparisons, or charts that would answer your question.</li>
</ul>
<h4>3. Ethics and feasibility (12 points)</h4>
<ul>
<li><strong>Terms of service and <code>robots.txt</code></strong>: what rules govern the data you will collect? Is your collection is allowed? Does it fall under a fair use or research exception? How you will stay within the limits (a User-Agent that identifies you, pauses between requests, rate limits)?</li>
<li><strong>Personal information</strong>: does the data include people&rsquo;s names, usernames, photos, or other personal details? Say how you will handle them: leave them out, aggregate, or anonymize.</li>
<li><strong>One record, retrieved</strong>: paste a request you actually ran (the code or the URL) and what came back (the status code and the record, or a screenshot of it). Name the fields you will use.</li>
<li><strong>The biggest risk</strong> to finishing, and your fallback: a smaller scope, a second source, or a different time window.</li>
</ul>
<h4>Working in a pair</h4>
<p>Pairs need the instructor&rsquo;s permission before the proposal is due; email to ask. Submit proposals and final submissions individually, not as a team, and say who will do what.</p>
<h4>AI tools</h4>
<p>As the syllabus says, you may use AI tools if you say where and how they shaped your proposal, and you must be able to explain your question, your source, and your method yourself.</p>
<h4>Late work</h4>
<p>Late work loses 1% of its maximum value for each day after the deadline, unless you have an approved excuse.</p>
<h4>Where to start</h4>
<ul>
<li>Every chapter&rsquo;s <em>Additional Exercises</em> are potential project questions.</li>
<li>Chapter 15&rsquo;s <em>Research proposal</em> exercise lists the six parts a full research proposal has.</li>
<li><strong>Office hours</strong>, for a question or source you are unsure of.</li>
</ul>
<h4>What comes next</h4>
<p>A presentation of about five minutes plus questions in the final week, November 30&ndash;December 4 (10%), and a write-up of about 2,000&ndash;3,000 words, due Monday, December 7 (25%).</p>
"""

WRITEUP_DESCRIPTION = (
    "<p>Your project repository (code, data or collection scripts, and a README "
    "someone else could follow) plus the written analysis. Due during finals "
    "week; there is no final exam.</p>"
    "<h4>What the repository must contain</h4><ul>"
    "<li><code>README.md</code>: what the project is, how to set it up and run "
    "it, and where the data came from.</li>"
    "<li><code>proposal.md</code>: your proposal.</li>"
    "<li>At least one Jupyter notebook (<code>.ipynb</code>) that runs top to "
    "bottom with its output visible.</li>"
    "<li>Your written document, <code>report.md</code> or "
    "<code>report.pdf</code>, of about 2,000&ndash;3,000 words.</li></ul>"
    "<p>Submit the URL of your repository. It is graded with the rubric below on "
    "what has been pushed by the deadline.</p>")

DESCRIPTIONS = {"Final Project — Proposal": PROPOSAL_DESCRIPTION,
                "Final Project — Repository & Write-up": WRITEUP_DESCRIPTION}
# The proposal takes a PDF or a link to the project's README; Canvas has no
# text-entry box for it.
SUBMISSION_TYPES = {"Final Project — Proposal": ["online_upload", "online_url"]}

# Rubrics attached in Canvas and used for grading. Each criterion is
# (title, long description, [(level, points, description), ...]); a criterion
# is worth its top level. migrate.py's `rubrics` step attaches a rubric to each
# assignment listed that has none, and leaves the others alone. Grading rules a
# rubric can't hold (a blank scaffold, late work) are in docs/grading.md.

# The proposal: one criterion per bullet of PROPOSAL_DESCRIPTION, each 3 / 2 /
# 1 / 0 with no half points, so parts 1-3 are worth 9 / 9 / 12. Attached
# 2026-10-23.
_PROPOSAL_LEVELS = (("Full", 3), ("Mostly", 2), ("Attempted", 1), ("Missing", 0))


def _levels(levels, descriptions):
    return [(name, pts, text) for (name, pts), text in zip(levels, descriptions)]


PROPOSAL_RUBRIC = {
    "assignments": ["Final Project — Proposal"],
    "title": "Final Project Proposal (30 points)",
    "criteria": [
        ("1a. A question, not a topic", "Part 1: research question", _levels(_PROPOSAL_LEVELS, [
            "A specific, empirical question web data can answer, whose answer could take many values.",
            "A question, but one element is weak: too broad, yes/no only, or loosely tied to web data.",
            "Vague or mostly a topic phrased as a question.",
            "Only a topic, or no question."])),
        ("1b. Who would care", "Part 1: research question", _levels(_PROPOSAL_LEVELS, [
            "Names a specific audience (newsroom, agency, community group, researchers, users) and why the answer matters to them.",
            "Names an audience but not why it matters, or the audience is general.",
            "Gestures at an audience vaguely.",
            "No audience."])),
        ("1c. Expected finding", "Part 1: research question", _levels(_PROPOSAL_LEVELS, [
            "States what they expect to find and what would surprise them.",
            "Gives an expectation or a surprise, not both.",
            "Expectation is vague or not tied to the question.",
            "Neither."])),
        ("2a. Source and how to get it", "Part 2: data and method", _levels(_PROPOSAL_LEVELS, [
            "Exact source with links (URL, API endpoint, or document set) and the collection method (API, static or dynamic scraping, PDFs, web archives), naming the chapter(s).",
            "Source and method given, but missing links or the chapter.",
            "Source or method vague, or only one of the two given.",
            "Neither given."])),
        ("2b. Scope", "Part 2: data and method", _levels(_PROPOSAL_LEVELS, [
            "Which records, what time window, and roughly how many; how often and for how long if collecting over time.",
            "One of these elements is missing.",
            "Scope only gestured at.",
            "No scope."])),
        ("2c. Analysis plan", "Part 2: data and method", _levels(_PROPOSAL_LEVELS, [
            "The counts, comparisons, or charts that would answer the question.",
            "Analysis named but loosely tied to the question.",
            "Generic (e.g. 'analyze the data').",
            "No analysis plan."])),
        ("3a. Terms of service and robots.txt", "Part 3: ethics and feasibility", _levels(_PROPOSAL_LEVELS, [
            "Names the governing rules (terms of service, robots.txt), whether collection is allowed or falls under a research/fair-use exception, and how they will stay within limits (identifying User-Agent, pauses, rate limits).",
            "Covers the rules or the limits well, the other thinly.",
            "Mentions rules or politeness only in passing.",
            "Not discussed."])),
        ("3b. Personal information", "Part 3: ethics and feasibility", _levels(_PROPOSAL_LEVELS, [
            "Says whether the data includes names, usernames, photos, or other personal details and how they will handle them (leave out, aggregate, anonymize), or states there are none.",
            "Identifies personal data but the handling plan is thin.",
            "Raises the issue without a plan.",
            "Not addressed."])),
        ("3c. One record, retrieved", "Part 3: ethics and feasibility", _levels(_PROPOSAL_LEVELS, [
            "A request actually run (code or URL), what came back (status code and the record, or a screenshot), and the fields they will use.",
            "Request and result shown, but no fields named.",
            "Request without a result, or a result without the request.",
            "No retrieved record."])),
        ("3d. Biggest risk and fallback", "Part 3: ethics and feasibility", _levels(_PROPOSAL_LEVELS, [
            "Names the biggest risk to finishing and a concrete fallback (smaller scope, second source, different time window).",
            "Risk and fallback given, but the fallback is vague.",
            "Risk without a fallback, or a fallback without a risk.",
            "Neither."])),
    ],
}

# Notebook Labs: five elements, each 2 / 1 / 0, for 10 points. Attached
# 2026-10-23 to weeks 11-14; weeks 2-9 were graded before it existed and have
# no rubric in Canvas. Week 10's lab isn't in Canvas yet.
LAB_RUBRIC = {
    "assignments": [f"Week {wk} Lab — {week_info(wk)[3]}" for wk in (11, 12, 13, 14)],
    "title": "Notebook Lab (10 points)",
    "criteria": [
        ("1. Valid notebook HTML", "Your completed companion notebook, exported to HTML.", [
            ("Met", 2, "An HTML file of your notebook, in any layout."),
            ("Not met", 0, "Missing or unreadable.")]),
        ("2. Every required step attempted", "Recommended Exercises, Steps 1 to N-1.", [
            ("Met", 2, "Every Recommended Exercises code step has your own code. Steps announced as optional count as done."),
            ("Partly met", 1, "At least half of the required steps."),
            ("Not met", 0, "Fewer than half, or the blank scaffold.")]),
        ("3. Run, with output visible", "Run every cell before exporting.", [
            ("Met", 2, "Your code cells are run and their output shows. Errors left visible still count."),
            ("Partly met", 1, "Some cells with your code are unrun."),
            ("Not met", 0, "No cell with your code was run.")]),
        ("4. Interpretation in your own words", "The final step of the Recommended Exercises.", [
            ("Met", 2, "The final step answered at about the requested length and about your own results, in the prompt cell, comments, a Markdown cell, or a print()."),
            ("Partly met", 1, "Present but thin (one to three sentences), or generic."),
            ("Not met", 0, "Missing, or the placeholder left as is.")]),
        ("5. Each step does its task", "Judged on the steps you attempted.", [
            ("Met", 2, "Each attempted step does what it asks, using your own choices where the step says to choose."),
            ("Partly met", 1, "Some steps substitute something else, such as the chapter's own example."),
            ("Not met", 0, "The code is unrelated to the steps.")]),
    ],
}

# Portfolio checkpoints (weeks 11-14): two criteria a week, 1 point each,
# met or not. Attached 2026-10-23.
def _met(text):
    return [("Met", 1, text), ("Not met", 0, "Missing, or only a placeholder.")]


_PORTFOLIO_CRITERIA = {
    11: [("1. Repository and README", "Set up the repository.", _met(
            "A public repository on your own GitHub account, its URL submitted, "
            "with a README.md giving a title, your name, a one-paragraph summary "
            "of your question, and placeholder sections (Data, Methods, Findings, "
            "How to reproduce).")),
         ("2. Proposal and placeholders", "Set up the repository.", _met(
            "proposal.md with your proposal, plus a notebook (.ipynb), a report "
            "placeholder (report.md, or a note that it will be a PDF), and a data/ "
            "folder."))],
    12: [("1. Collection and cleaning code", "Collect and clean.", _met(
            "Collection code that runs, makes polite requests (an identifying "
            "User-Agent, pauses), and saves the raw data; a cleaning step, with "
            "code and output, that produces a tidy dataset.")),
         ("2. Data documented", "Collect and clean.", _met(
            "A small sample of the cleaned data with a data dictionary, and the "
            "README's Data section: source, when collected, how many records, and "
            "what was kept out of the repo and why."))],
    13: [("1. Analysis notebook", "Analyze.", _met(
            "An analysis notebook that runs top to bottom with output visible, "
            "with results that answer at least part of your question.")),
         ("2. Figure and README", "Analyze.", _met(
            "At least one figure saved in the repo with a title, labeled axes, "
            "and a one-sentence caption, and the README's Methods section and "
            "preliminary Findings."))],
    14: [("1. Full draft report", "Draft your write-up.", _met(
            "A full draft of report.md or report.pdf with every section present, "
            "using your own results and figures and citing your sources.")),
         ("2. Complete, reproducible repository", "Draft your write-up.", _met(
            "README.md, proposal.md, your notebook, and your report all present "
            "and current, with a README that lets someone else reproduce the "
            "project: setup, how to run it, and where the data came from."))],
}
PORTFOLIO_RUBRICS = [
    {"assignments": [revision_name(wk)],
     "title": f"Week {wk} Portfolio ({PORTFOLIO_POINTS} points)",
     "criteria": crit}
    for wk, crit in _PORTFOLIO_CRITERIA.items()
]


# The final presentation (60 points) and repository and write-up (150 points):
# each criterion is Full / Mostly / Attempted / Missing at about 100 / 67 / 33 /
# 0 percent of its points, in whole points. Attached 2026-10-23.
def _scaled(points, full):
    return [("Full", points, full),
            ("Mostly", round(points * 2 / 3), "Mostly there: one part is thin or missing."),
            ("Attempted", round(points / 3), "Present, but thin or largely incomplete."),
            ("Missing", 0, "Not addressed.")]


PRESENTATION_RUBRIC = {
    "assignments": ["Final Project — Presentation"],
    "title": "Final Project Presentation (60 points)",
    "criteria": [
        ("1. Question and who cares", "About five minutes plus questions.", _scaled(10,
            "A clear research question and why it matters to a named audience.")),
        ("2. Data and method", "About five minutes plus questions.", _scaled(10,
            "The source, how it was collected and cleaned, its scope, and the "
            "ethics checks, in brief.")),
        ("3. Findings that carry an argument", "About five minutes plus questions.", _scaled(15,
            "One or two readable visualizations, each making a point that answers "
            "the question.")),
        ("4. Surprises and limitations", "About five minutes plus questions.", _scaled(10,
            "What surprised you and what the data can't tell you.")),
        ("5. Delivery", "About five minutes plus questions.", _scaled(10,
            "About five minutes, a clear structure, and slides or a notebook "
            "legible from the room.")),
        ("6. Questions", "About five minutes plus questions.", _scaled(5,
            "Answers questions about the data and method directly.")),
    ],
}

WRITEUP_RUBRIC = {
    "assignments": ["Final Project — Repository & Write-up"],
    "title": "Final Project Repository & Write-up (150 points)",
    "criteria": [
        ("1. Required files", "The repository.", _scaled(10,
            "README.md, proposal.md, at least one .ipynb notebook, and the report "
            "(report.md or report.pdf), all present and current.")),
        ("2. Reproducibility", "The repository.", _scaled(20,
            "The README covers setup, how to run, and where the data came from; "
            "the notebook runs top to bottom with output visible.")),
        ("3. Collection and cleaning", "The repository.", _scaled(20,
            "Polite collection code, a documented cleaning step, a data sample and "
            "dictionary, and what was withheld from the repo and why.")),
        ("4. Analysis", "The repository.", _scaled(25,
            "Counts or comparisons that answer the question, and figures with "
            "titles, labeled axes, and captions.")),
        ("5. The written report", "The write-up.", _scaled(30,
            "About 2,000-3,000 words covering the question and its audience, data "
            "and methods, findings, limitations, and a conclusion.")),
        ("6. Claims match the evidence", "The write-up.", _scaled(20,
            "Every claim is backed by your own results, and the limits of the data "
            "are stated.")),
        ("7. Ethics", "The repository and write-up.", _scaled(15,
            "Terms of service and robots.txt respected, personal information left "
            "out, aggregated, or anonymized, and an identifying User-Agent.")),
        ("8. Portfolio practice", "The repository.", _scaled(10,
            "A clear layout, a commit history showing work through weeks 11-14, "
            "and AI use disclosed.")),
    ],
}

RUBRICS = ([PROPOSAL_RUBRIC, LAB_RUBRIC] + PORTFOLIO_RUBRICS
           + [PRESENTATION_RUBRIC, WRITEUP_RUBRIC])


def final_assignments():
    out = []
    for name, points, day, blurb in FINAL_PARTS:
        out.append({
            "group": "Final Project",
            "name": name,
            "points_possible": points,
            "due_at": due_at(day),
            "submission_types": SUBMISSION_TYPES.get(
                name, ["online_upload", "online_text_entry", "online_url"]),
            "description": DESCRIPTIONS.get(name, f"<p>{blurb}</p>"),
        })
    return out


def all_assignments():
    return (lab_assignments() + revision_assignments()
            + attendance_assignments() + final_assignments())


# --------------------------------------------------------------------------
# Modules
# --------------------------------------------------------------------------

def modules():
    """One module per week, laid out on the Monday/Wednesday/Friday rhythm."""
    out = []
    for wk, module_name, ch, topic, slug, chfile, note in WEEKS:
        if wk == 15:
            out.append({
                "week": wk,
                "name": f"Week {wk} — Fall Break",
                "items": [{"type": "SubHeader", "title": note}],
            })
            continue

        items = [{"type": "SubHeader", "title": f"Monday · Concepts — {topic}"}]
        if note:
            items.append({"type": "SubHeader", "title": note})
        items.append({
            "type": "ExternalUrl",
            "title": f"Read: Chapter {ch} — {topic}",
            "external_url": chapter_url(chfile),
            "new_tab": True,
        })
        items.append({
            "type": "ExternalUrl",
            "title": f"Slides: Week {wk}",
            "external_url": slides_url(wk),
            "new_tab": True,
        })
        if wk not in TEACHING_WEEKS:
            items.extend(lab_items(wk))

        if wk in TEACHING_WEEKS:
            items.append({"type": "SubHeader", "title": "Wednesday · Notebook Lab"})
            items.append({
                "type": "ExternalUrl",
                "title": f"Companion notebook: {slug}.ipynb",
                "external_url": notebook_url(slug),
                "new_tab": True,
            })
            items.extend(lab_items(wk))
            if wk not in NO_ASSIGNMENT_WEEKS:
                items.append({"type": "Assignment", "title": f"Week {wk} Lab — {topic}"})
            items.append({"type": "SubHeader", "title": "Friday · Textbook Revisions"
                          if wk not in PORTFOLIO_WEEKS else "Friday · Project portfolio"})
            if wk not in NO_ASSIGNMENT_WEEKS:
                items.append({"type": "Assignment", "title": revision_name(wk)})
        elif wk == 1:
            items.append({"type": "SubHeader", "title": "Friday · Welcome, setup & how this class works"})
            items.append({
                "type": "ExternalUrl",
                "title": "Course repository (slides & syllabus)",
                "external_url": REPO_URL,
                "new_tab": True,
            })
        elif wk == 16:
            items.append({"type": "SubHeader", "title": "Wednesday · Project workshop"})
            items.append({"type": "Assignment", "title": "Final Project — Presentation"})
            items.append({"type": "SubHeader", "title": "Friday · Final presentations (last day of class)"})
            items.append({"type": "Assignment", "title": "Final Project — Repository & Write-up"})

        out.append({"week": wk, "name": f"Week {wk} — {topic}", "items": items})
    return out


# --------------------------------------------------------------------------
# Syllabus page
# --------------------------------------------------------------------------

def _schedule_rows():
    rows = []
    for wk, module_name, ch, topic, _, chfile, note in WEEKS:
        days = meeting_days(wk)
        if wk == 15:
            dates = "Nov 23–27"
        elif days:
            first, last = days[0], days[-1]
            dates = (f"{first.strftime('%b %-d')}–{last.strftime('%-d')}"
                     if first.month == last.month
                     else f"{first.strftime('%b %-d')}–{last.strftime('%b %-d')}")
            if len(days) == 1:
                dates = first.strftime("%b %-d")
        else:
            dates = ""
        rows.append((wk, module_name or "—", dates, topic,
                     f"Ch. {ch}" if ch else "—", note))
    return rows


def syllabus_html() -> str:
    """The Canvas syllabus page, styled to match the PDF syllabus."""
    sched = []
    for wk, module_name, dates, topic, chap, note in _schedule_rows():
        bg = "#FAF8F2" if wk % 2 else "#FFFFFF"
        topic_cell = topic
        if note:
            topic_cell += f'<br><span style="color:{CU_DARK};font-size:0.9em;">{note}</span>'
        sched.append(
            f'<tr style="background:{bg};">'
            f'<td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;text-align:center;">{wk}</td>'
            f'<td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;"><em>{module_name}</em></td>'
            f'<td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;white-space:nowrap;">{dates}</td>'
            f'<td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;">{topic_cell}</td>'
            f'<td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;text-align:center;white-space:nowrap;">{chap}</td>'
            f"</tr>"
        )
    schedule_body = "\n".join(sched)

    return f"""
<div style="max-width:60em;">

  <div style="border-left:6px solid {CU_GOLD};padding:0.6em 1em;margin-bottom:1.2em;background:#FAF8F2;">
    <h2 style="margin:0 0 0.2em 0;">{COURSE_NAME}</h2>
    <p style="margin:0;"><strong>{COURSE_CODE}</strong> &middot; {TERM}<br>
    {MEETING} &middot; {ROOM}</p>
    <p style="margin:0.6em 0 0 0;">
      <strong>{INSTRUCTOR}</strong><br>
      {INSTRUCTOR_TITLE}<br>
      Email: <a href="mailto:{INSTRUCTOR_EMAIL}">{INSTRUCTOR_EMAIL}</a> &middot;
      Office: {INSTRUCTOR_OFFICE} &middot; Office hours: {OFFICE_HOURS}
    </p>
  </div>

  <h3>Course description</h3>
  <p>The internet makes many kinds of information easy to access. The ability to
  retrieve, parse, and analyze this information is a valuable skill for data
  scientists. This course provides an overview of computational tools and
  practices for transforming web documents and APIs into data for common research
  designs.</p>
  <p>The course is organized around an open-source textbook, the
  <a href="{BOOK_URL}">Web Data Science</a> book, which we read chapter-by-chapter
  and&mdash;crucially&mdash;improve together. Each week you implement the concepts
  in companion Jupyter notebooks and then propose and evaluate revisions to the
  textbook itself through GitHub.</p>

  <h3>Learning objectives</h3>
  <ul>
    <li>Understand the legal and ethical contours of web data access</li>
    <li>Navigate and parse common web data formats like XML and JSON</li>
    <li>Retrieve and automate data extraction from HTML and PDF documents</li>
    <li>Access popular APIs to collect data for common research designs</li>
    <li>Use version control and collaborative open-source workflows (Git and
        GitHub pull requests) to contribute to a shared codebase</li>
    <li>Document, communicate, and critically evaluate data-collection code and
        technical writing</li>
  </ul>

  <h3>How the week works</h3>
  <table style="border-collapse:collapse;width:100%;margin-bottom:1em;">
    <tr style="background:{CU_GOLD};">
      <th style="padding:8px 10px;text-align:left;width:8em;">Day</th>
      <th style="padding:8px 10px;text-align:left;">Focus</th>
    </tr>
    <tr style="background:#FAF8F2;">
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;"><strong>Monday</strong></td>
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;">
        Introduce a new concept and its companion notebook</td>
    </tr>
    <tr>
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;"><strong>Wednesday</strong></td>
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;">
        <strong>Notebook Lab</strong> &mdash; work through and share the notebook exercises</td>
    </tr>
    <tr style="background:#FAF8F2;">
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;"><strong>Friday</strong></td>
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;">
        <strong>Textbook Revisions</strong> &mdash; propose and peer-review pull
        requests to the book</td>
    </tr>
  </table>

  <h3>Evaluation</h3>
  <p>There is no midterm and no final exam.</p>
  <table style="border-collapse:collapse;width:100%;margin-bottom:1em;">
    <tr style="background:{CU_GOLD};">
      <th style="padding:8px 10px;text-align:left;">Component</th>
      <th style="padding:8px 10px;text-align:center;width:6em;">Weight</th>
      <th style="padding:8px 10px;text-align:left;">Notes</th>
    </tr>
    <tr style="background:#FAF8F2;">
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;"><strong>Notebook Labs</strong></td>
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;text-align:center;">30%</td>
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;">
        Wednesday labs, due the following Sunday at 11:59pm. Graded on
        participation and completion; the two lowest scores are dropped.</td>
    </tr>
    <tr>
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;"><strong>Textbook Revisions</strong></td>
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;text-align:center;">15%</td>
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;">
        Friday workshops, due the following Sunday at 11:59pm. Both the revisions
        you propose and the peer reviews you provide.</td>
    </tr>
    <tr style="background:#FAF8F2;">
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;"><strong>Attendance</strong></td>
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;text-align:center;">15%</td>
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;">
        Attendance is required. The methods are cumulative and build on each
        other, so missed sessions are hard to recover from.</td>
    </tr>
    <tr>
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;"><strong>Final Project</strong></td>
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;text-align:center;">40%</td>
      <td style="padding:6px 10px;border-bottom:1px solid #E8E4D9;">
        Proposal (Oct 25, 5%), in-class presentation (final week, 10%), and the
        repository and write-up (Dec 7, 25%).</td>
    </tr>
  </table>
  <p>Attendance is required and carries its own weight. We cover technical
  methods that are cumulative and that require sustained effort, so a missed
  session is hard to recover from, and there is no way to make up missed
  attendance. If personal, professional, medical, or other circumstances will
  prevent your attendance, please email me so we can develop an accommodation
  plan together. If you need to miss several classes, come to office hours so we
  can check in on the material and your progress.</p>

  <h3>Computing</h3>
  <p>We use <a href="https://jupyter.org/">Jupyter notebooks</a> in Python 3; the
  <a href="https://www.anaconda.com/">Anaconda distribution</a> of Python 3.12 or
  above is strongly recommended. Over the semester we use <code>requests</code>,
  <code>BeautifulSoup</code>, <code>selenium</code>, <code>pypdf</code>, and
  <code>pandas</code>. Because we contribute to the textbook through GitHub, you
  also need <a href="https://git-scm.com/">Git</a> and a free
  <a href="https://github.com/">GitHub</a> account; we set these up together in
  the first week. Bring a laptop to class.</p>

  <h3>Generative AI and coauthorship</h3>
  <p>Generative AI tools are part of contemporary data-science practice, and you
  are welcome to use them in this course as collaborators&mdash;much as the course
  textbook itself was drafted with AI assistance and documents that process in its
  AI-disclosure appendix. Three expectations apply. <strong>Disclosure:</strong>
  when AI tools materially shape a notebook, a pull request, or your Final
  Project, note where and how you used them. <strong>Understanding:</strong> you
  are responsible for every line you submit and must be able to explain how your
  code works and why it is correct. <strong>Integrity:</strong> presenting
  AI-generated work as another person's, or using it to misrepresent data,
  sources, or effort, violates the Honor Code. When in doubt, disclose and ask.</p>

  <h3>A note on public contributions</h3>
  <p>Pull requests to the Web Data Science book are made to a <em>public</em>
  open-source repository under an open license, and your accepted contributions
  will be visible to anyone. If you prefer to contribute under a pseudonym or have
  concerns about public attribution, email me and we will work out an
  alternative.</p>

  <h3>Course schedule</h3>
  <table style="border-collapse:collapse;width:100%;">
    <tr style="background:{CU_GOLD};">
      <th style="padding:8px 10px;text-align:center;width:4em;">Week</th>
      <th style="padding:8px 10px;text-align:left;width:9em;">Module</th>
      <th style="padding:8px 10px;text-align:left;width:9em;">Dates</th>
      <th style="padding:8px 10px;text-align:left;">Topic</th>
      <th style="padding:8px 10px;text-align:center;width:5em;">Reading</th>
    </tr>
{schedule_body}
  </table>
  <p style="color:{CU_DARK};font-size:0.9em;">No class Labor Day (Sep 7) or Fall
  Break (Nov 23&ndash;27). December 4 is the last day of class and follows a Monday
  schedule. The Final Project repository and write-up are due Monday, December 7;
  there is no final exam.</p>

  <h3>University policies</h3>
  <p>This course follows CU Boulder's policies on
  <a href="https://www.colorado.edu/policies/student-classroom-course-related-behavior">classroom
  behavior</a>, <a href="https://www.colorado.edu/disabilityservices/students">accommodations
  for disabilities</a>, <a href="https://www.colorado.edu/policies/academic-integrity-policy">academic
  integrity and the Honor Code</a>,
  <a href="https://www.colorado.edu/oiec/">discrimination and harassment</a>, and
  <a href="https://www.colorado.edu/policies/observance-religious-holidays-and-absences-classes-andor-exams">religious
  observance</a>. Full text of each policy, along with the complete course
  description and readings, is in the
  <strong>syllabus PDF</strong> posted to this course and in the
  <a href="{REPO_URL}">course repository</a>.</p>

</div>
""".strip()
