"""Declarative spec for the Fall 2026 INFO 4617 Canvas course.

This is the single source of truth for what the migrated course should look
like: the teaching calendar, assignment groups and weights, the weekly
assignments, the module layout, and the syllabus page. `migrate.py` reads this
and makes Canvas match it.

Everything here is derived from `syllabus/syllabus.tex` and the weekly decks in
`slides/`. If the syllabus changes, change it here too.
"""

from datetime import date, datetime, time
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
FINAL_DUE = date(2026, 12, 11)  # project repo + write-up, finals week

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
     "Final Project proposal due Friday, October 23."),
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
REVISION_POINTS = 10
FINAL_PARTS = [
    ("Final Project — Proposal", 20, date(2026, 10, 23),
     "A short proposal naming your web data source, your research question, and "
     "the design that connects them. See the Week 10 and Week 16 materials."),
    ("Final Project — Presentation", 30, LAST_DAY,
     "Present your project to the class during the final week. Bring your data, "
     "one or two visualizations that carry an argument, and what surprised you."),
    ("Final Project — Repository & Write-up", 50, FINAL_DUE,
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


# --------------------------------------------------------------------------
# Assignment construction
# --------------------------------------------------------------------------

def lab_assignments():
    """One notebook lab per teaching week, met Wednesday and due that Sunday."""
    out = []
    for wk in TEACHING_WEEKS:
        _, _, ch, topic, slug, chfile, _ = week_info(wk)
        if lab_day(wk) is None:
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


def revision_assignments():
    """One textbook-revision workshop per teaching week, met Friday and due that Sunday."""
    out = []
    for wk in TEACHING_WEEKS:
        _, _, ch, topic, _, chfile, _ = week_info(wk)
        if revision_day(wk) is None:
            continue
        out.append({
            "group": "Textbook Revisions",
            "name": f"Week {wk} Revision — Chapter {ch}",
            "points_possible": REVISION_POINTS,
            "due_at": due_at(sunday_of(wk)),
            # URL only: the deliverable is the pull request itself
            "submission_types": ["online_url"],
            "description": (
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
            ),
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


def final_assignments():
    out = []
    for name, points, day, blurb in FINAL_PARTS:
        out.append({
            "group": "Final Project",
            "name": name,
            "points_possible": points,
            "due_at": due_at(day),
            "submission_types": ["online_upload", "online_text_entry", "online_url"],
            "description": f"<p>{blurb}</p>",
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

        if wk in TEACHING_WEEKS:
            items.append({"type": "SubHeader", "title": "Wednesday · Notebook Lab"})
            items.append({
                "type": "ExternalUrl",
                "title": f"Companion notebook: {slug}.ipynb",
                "external_url": notebook_url(slug),
                "new_tab": True,
            })
            items.append({"type": "Assignment", "title": f"Week {wk} Lab — {topic}"})
            items.append({"type": "SubHeader", "title": "Friday · Textbook Revisions"})
            items.append({"type": "Assignment", "title": f"Week {wk} Revision — Chapter {ch}"})
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
        Proposal (Oct 23), in-class presentation (final week), and the repository
        and write-up (Dec 11).</td>
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
  schedule. The Final Project repository and write-up are due Friday, December 11;
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
