"""Grading helpers for INFO 4617: attendance, Textbook Revisions, portfolio
checkpoints, and Notebook Labs, read from and posted to Canvas.

`grading.ipynb` walks through these one step at a time. The rules are the
ones in `docs/grading.md`; change them there first. Nothing here writes to
Canvas unless a `Canvas` client was made with `apply=True`, and even then
`post()` asks for a typed confirmation.

Student data (downloads, proposed scores) goes to GRADING_DIR, outside the
repository (default ~/info4617-grading). Never commit it.
"""
from __future__ import annotations

import json
import math
import os
import re
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import requests

import course_spec as spec

HOST = "canvas.colorado.edu"
COURSE = spec.NEW_COURSE_ID
GRADING_DIR = Path(os.environ.get("GRADING_DIR", Path.home() / "info4617-grading"))
BOOK = ("cuinfoscience", "Web-Data-Science-Book")
CLASS_REPOS = {("cuinfoscience", "web-data-science-book"),
               ("cuinfoscience", "info4617-fall2026"),
               ("cuinfoscience", "info-missing-manual")}

# docs/grading.md, "Notebook Labs": steps the instructor told students to skip
OPTIONAL_STEPS = {5: {2}, 7: {4, 5}}
LATE_GRACE_HOURS = 24
LATE_CAP = 5

COMMENTS = {
    "own_comment": ("Full credit this week, but next time please submit the link to "
                    "your own comment (click its timestamp to copy a URL ending in "
                    "#issuecomment-…) rather than the link to the whole issue."),
    "blank": ("This upload was the blank exercise scaffold, so please save your "
              "notebook after completing the exercises, export it to HTML, and "
              "upload that completed file."),
    "unrun": ("Please run every cell before exporting so that both your code and "
              "its output appear in the HTML you submit."),
    "traceback": ("When you hit a traceback, check that the libraries you need are "
                  "imported and that the cells defining your variables have been "
                  "run first, in order."),
    "unseen": ("Your interpretation reports results that don't appear in your "
               "notebook's output, so please run every cell before exporting so "
               "the evidence for your claims is visible."),
}


def late_comment(days, deducted):
    s = "s" if days > 1 else ""
    text = (f"This lab was submitted {days} day{s} late, past the 24-hour grace "
            f"period, so {deducted} point{'s' if deducted > 1 else ''} "
            f"{'were' if deducted > 1 else 'was'} deducted")
    return text + (" (the late penalty is capped at 5 points)." if days > LATE_CAP else ".")


def late_days(submitted_at, due_at):
    """Started days late after the grace period counts from the due date:
    36 hours late is 2 days. Within the grace period it is 0."""
    if not submitted_at or not due_at:
        return 0
    hours = (_ts(submitted_at) - _ts(due_at)).total_seconds() / 3600
    return math.ceil(hours / 24) if hours > LATE_GRACE_HOURS else 0


def _ts(s):
    return datetime.fromisoformat(str(s).replace("Z", "+00:00"))


# ------------------------------------------------------------------ Canvas

class Canvas:
    """A small Canvas client. Writes are refused unless apply=True."""

    def __init__(self, token=None, apply=False):
        self.token = token or os.environ.get("CANVAS_TOKEN", "").strip()
        if not self.token:
            raise RuntimeError("Set CANVAS_TOKEN (Canvas → Account → Settings → New Access Token).")
        self.apply = apply
        self.base = f"https://{HOST}/api/v1/courses/{COURSE}"
        self.s = requests.Session()
        self.s.headers["Authorization"] = f"Bearer {self.token}"

    def get(self, path, **params):
        r = self.s.get(self.base + path, params=params)
        r.raise_for_status()
        return r.json()

    def get_all(self, path, **params):
        url, out, params = self.base + path, [], {**params, "per_page": 100}
        while url:
            r = self.s.get(url, params=params)
            r.raise_for_status()
            out.extend(r.json())
            url, params = r.links.get("next", {}).get("url"), None
        return out

    def write(self, method, path, data):
        if not self.apply:
            raise RuntimeError("This client is read-only. Make it with apply=True to post.")
        r = self.s.request(method, self.base + path, data=data)
        r.raise_for_status()
        return r.json()

    def roster(self):
        """Students (no test student), one row each."""
        rows = self.get_all("/users", **{"enrollment_type[]": "student"})
        return pd.DataFrame([{"user_id": u["id"], "name": u["name"],
                              "sortable_name": u.get("sortable_name"),
                              "identikey": (u.get("login_id") or "").lower()} for u in rows])

    def group_assignments(self, group):
        for g in self.get_all("/assignment_groups", **{"include[]": "assignments"}):
            if g["name"] == group:
                return sorted(g["assignments"], key=lambda a: a.get("due_at") or "")
        raise KeyError(group)

    def assignment(self, name_or_id):
        if isinstance(name_or_id, int):
            return self.get(f"/assignments/{name_or_id}")
        for a in self.get_all("/assignments", search_term=name_or_id):
            if a["name"] == name_or_id:
                return a
        raise KeyError(name_or_id)

    def submissions(self, assignment_id):
        return self.get_all(f"/assignments/{assignment_id}/submissions",
                            **{"include[]": ["submission_comments", "submission_history"]})


def week_of(name):
    m = re.match(r"Week (\d+)", name or "")
    return int(m.group(1)) if m else None


# ------------------------------------------------------------- proposals
# One row per student per assignment. `action` is grade, comment_only, hold,
# or skip. `rubric` is a JSON list of points, one per criterion, in the
# rubric's order, or empty. `review` marks rows the instructor must look at.

COLUMNS = ["kind", "week", "assignment_id", "user_id", "name", "action", "score",
           "rubric", "comment", "review", "notes", "url"]


def proposal(**kw):
    row = {c: "" for c in COLUMNS}
    row.update(review=False, action="grade")
    row.update(kw)
    if isinstance(row["rubric"], (list, tuple)):
        row["rubric"] = json.dumps(list(row["rubric"]))
        if row["score"] == "":
            row["score"] = sum(json.loads(row["rubric"]))
    return row


def save(df, name):
    GRADING_DIR.mkdir(parents=True, exist_ok=True)
    path = GRADING_DIR / f"{name}.csv"
    df.to_csv(path, index=False)
    return path


def load(name):
    df = pd.read_csv(GRADING_DIR / f"{name}.csv", dtype=str, keep_default_na=False)
    df["review"] = df["review"].str.lower().isin(["true", "1", "yes"])
    return df


def post(canvas, df, confirm=None):
    """Post every row whose action is grade or comment_only. Rows still marked
    review=True are refused: resolve them first. Pass confirm="post N" where N
    is the number of rows being posted."""
    rows = df[df["action"].isin(["grade", "comment_only"])]
    if rows["review"].any():
        raise ValueError(f"{int(rows['review'].sum())} rows still need review.")
    if confirm != f"post {len(rows)}":
        raise ValueError(f'Re-run with confirm="post {len(rows)}" to post {len(rows)} rows.')
    rubrics = {}
    for _, r in rows.iterrows():
        data = {}
        if r["comment"]:
            data["comment[text_comment]"] = r["comment"]
        if r["action"] == "grade":
            pts = json.loads(r["rubric"]) if r["rubric"] else None
            aid = int(r["assignment_id"])
            if pts is not None:
                if aid not in rubrics:
                    rubrics[aid] = [c["id"] for c in canvas.get(f"/assignments/{aid}").get("rubric") or []]
                ids = rubrics[aid]
                if len(ids) != len(pts):
                    raise ValueError(f"{r['name']} week {r['week']}: rubric has {len(ids)} criteria, row has {len(pts)}")
                for cid, p in zip(ids, pts):
                    data[f"rubric_assessment[{cid}][points]"] = p
            else:
                data["submission[posted_grade]"] = r["score"]
        path = f"/assignments/{int(r['assignment_id'])}/submissions/{int(r['user_id'])}"
        canvas.write("PUT", path, data)
        # An override (a late penalty, a blank scaffold) is posted after the
        # rubric, which would otherwise set the score to the rubric's total.
        if r["action"] == "grade" and r["rubric"] and float(r["score"]) != sum(json.loads(r["rubric"])):
            canvas.write("PUT", path, {"submission[posted_grade]": r["score"]})
    return verify(canvas, df)


def verify(canvas, df):
    """Read every posted row back. Returns the rows that don't match."""
    bad, cache = [], {}
    for _, r in df[df["action"].isin(["grade", "comment_only", "hold"])].iterrows():
        aid = int(r["assignment_id"])
        if aid not in cache:
            cache[aid] = {s["user_id"]: s for s in canvas.submissions(aid)}
        s = cache[aid].get(int(r["user_id"]), {})
        comments = [c["comment"] for c in s.get("submission_comments") or []]
        ok = (not r["comment"] or r["comment"] in comments)
        if r["action"] == "grade":
            ok = ok and s.get("score") is not None and float(s["score"]) == float(r["score"])
        elif r["action"] == "hold":
            ok = s.get("score") is None
        if not ok:
            bad.append({"name": r["name"], "week": r["week"], "action": r["action"],
                        "wanted": r["score"], "canvas": s.get("score")})
    return pd.DataFrame(bad)


# -------------------------------------------------------------- attendance

def load_signins(path, id_col="identikey", time_col="timestamp"):
    """A sign-in CSV: one row per sign-in, with the student's identikey and a
    timestamp. Times without a zone are read as Mountain time."""
    df = pd.read_csv(path, dtype=str)
    t = pd.to_datetime(df[time_col], errors="coerce")
    if t.dt.tz is None:
        t = t.dt.tz_localize(spec.TZ, ambiguous="NaT", nonexistent="NaT")
    out = pd.DataFrame({"identikey": df[id_col].str.strip().str.lower(),
                        "date": t.dt.tz_convert(spec.TZ).dt.date})
    out["week"] = [None if pd.isna(d) else _week_number(d) for d in out["date"]]
    return out.dropna(subset=["date"])


def _week_number(d):
    return (d - spec.week_monday(1)).days // 7 + 1


def propose_attendance(canvas, signins, week, extra_dates=()):
    """One point per session held. A session is a scheduled meeting day
    (spec.meeting_days) that appears in the sheet; a class that didn't meet
    has no sign-ins and drops out. Sign-ins on other days are listed and
    ignored unless the date is passed in extra_dates (a make-up session)."""
    a = canvas.assignment(f"Week {week:02d} Attendance")
    roster = canvas.roster()
    wk = signins[signins["week"] == week]
    scheduled = set(spec.meeting_days(week)) | set(extra_dates)
    notes = [f"{d}: {int((wk['date'] == d).sum())} sign-ins on a day the class "
             f"doesn't meet, ignored" for d in sorted(set(wk["date"]) - scheduled)]
    wk = wk[wk["date"].isin(scheduled)]
    held = sorted(set(wk["date"]))
    attended = wk.drop_duplicates(["identikey", "date"]).groupby("identikey")["date"].nunique()
    unknown = sorted(set(attended.index) - set(roster["identikey"]))
    rows = []
    for _, st in roster.iterrows():
        n = int(attended.get(st["identikey"], 0))
        rows.append(proposal(kind="attendance", week=week, assignment_id=a["id"],
                             user_id=st["user_id"], name=st["name"], score=n,
                             notes=f"{n} of {len(held)} sessions"))
    info = {"assignment": a["name"], "points_now": a["points_possible"],
            "sessions_held": len(held), "dates": held, "graded": a.get("has_submitted_submissions"),
            "sheet_ids_not_on_roster": unknown, "date_notes": notes}
    return pd.DataFrame(rows), info


def set_attendance_points(canvas, week, sessions):
    """Set a week's attendance to one point per session, but only while it has
    no grades: changing points after grading changes students' percentages."""
    a = canvas.assignment(f"Week {week:02d} Attendance")
    if any(s.get("score") is not None for s in canvas.submissions(a["id"])):
        raise RuntimeError(f"{a['name']} already has grades; leave its points at {a['points_possible']}.")
    return canvas.write("PUT", f"/assignments/{a['id']}", {"assignment[points_possible]": sessions})


# ------------------------------------------------------------------ GitHub

class GitHub:
    """Read-only GitHub REST client. Set GITHUB_TOKEN for 5,000 requests an
    hour instead of 60."""

    def __init__(self, token=None):
        self.s = requests.Session()
        self.s.headers["Accept"] = "application/vnd.github+json"
        token = token or os.environ.get("GITHUB_TOKEN", "").strip()
        if token:
            self.s.headers["Authorization"] = f"Bearer {token}"
        self.cache = {}

    def get(self, path):
        if path not in self.cache:
            r = self.s.get("https://api.github.com" + path)
            self.cache[path] = r.json() if r.ok else {"_status": r.status_code}
        return self.cache[path]

    def get_all(self, path):
        out, page = [], 1
        while True:
            chunk = self.get(f"{path}{'&' if '?' in path else '?'}per_page=100&page={page}")
            if not isinstance(chunk, list) or not chunk:
                return out
            out += chunk
            page += 1


GH = re.compile(r"https?://github\.com/([^/]+)/([^/#?]+)(?:/(issues|pull|commit|compare|blob|tree)/([^#?]+))?(?:\?[^#]*)?(?:#(.*))?")


def parse_github_url(url):
    """What a submitted link points at: issue, pr, issuecomment, review,
    commit, compare, file, repo, or not github."""
    m = GH.match((url or "").strip())
    if not m:
        return {"type": "not github", "url": url}
    owner, repo, kind, rest, anchor = m.groups()
    d = {"owner": owner, "repo": repo, "url": url,
         "class_repo": (owner.lower(), repo.lower()) in CLASS_REPOS}
    if kind in ("issues", "pull"):
        d["number"] = int(rest.split("/")[0])
        d["type"] = "pr" if kind == "pull" else "issue"
        if anchor and anchor.startswith("issuecomment-"):
            d["type"], d["comment_id"] = "issuecomment", int(anchor.split("-")[1])
        elif anchor and anchor.startswith("pullrequestreview-"):
            d["type"], d["review_id"] = "review", int(anchor.split("-")[1])
        sub = rest.split("/")
        if kind == "pull" and len(sub) > 2 and sub[1] == "changes" and re.fullmatch(r"[0-9a-f]{7,40}", sub[2]):
            d["type"], d["sha"] = "commit", sub[2]
    elif kind == "commit":
        d["type"], d["sha"] = "commit", rest.split("/")[0]
    elif kind == "compare":
        d["type"], d["spec"] = "compare", rest
    elif kind in ("blob", "tree"):
        d["type"] = "file"
    else:
        d["type"] = "repo"
    return d


def resolve(gh, url):
    """Who made the linked item, when, how big it is, and who else took part."""
    d = parse_github_url(url)
    o, r = d.get("owner"), d.get("repo")
    base = f"/repos/{o}/{r}"
    item, author, created, size = {}, None, None, None
    if d["type"] in ("issue", "pr", "issuecomment", "review"):
        item = gh.get(f"{base}/issues/{d['number']}")
        d["title"] = item.get("title")
        author, created = (item.get("user") or {}).get("login"), item.get("created_at")
        size = len(item.get("body") or "")
        if d["type"] == "issuecomment":
            c = gh.get(f"{base}/issues/comments/{d['comment_id']}")
            author, created, size = (c.get("user") or {}).get("login"), c.get("created_at"), len(c.get("body") or "")
        if d["type"] == "review":
            c = gh.get(f"{base}/pulls/{d['number']}/reviews/{d['review_id']}")
            author, created, size = (c.get("user") or {}).get("login"), c.get("submitted_at"), len(c.get("body") or "")
        if d["type"] == "pr":
            pr = gh.get(f"{base}/pulls/{d['number']}")
            d["changed_lines"] = (pr.get("additions") or 0) + (pr.get("deletions") or 0)
        people = [(c.get("user") or {}).get("login") for c in gh.get_all(f"{base}/issues/{d['number']}/comments")]
        if item.get("pull_request"):
            people += [(c.get("user") or {}).get("login") for c in gh.get_all(f"{base}/pulls/{d['number']}/reviews")]
        d["participants"] = sorted({p for p in people if p})
    elif d["type"] == "commit":
        c = gh.get(f"{base}/commits/{d['sha']}")
        author = (c.get("author") or {}).get("login")
        created = ((c.get("commit") or {}).get("author") or {}).get("date")
        size = (c.get("stats") or {}).get("total")
    elif d["type"] == "compare":
        c = gh.get(f"{base}/compare/{d['spec']}")
        commits = c.get("commits") or []
        author = ((commits[-1] if commits else {}).get("author") or {}).get("login")
        created = (((commits[-1] if commits else {}).get("commit") or {}).get("author") or {}).get("date")
        size = sum(f.get("changes", 0) for f in c.get("files") or [])
    elif d["type"] in ("file", "repo"):
        author = o
    d.update(author=author, created_at=created, size=size)
    return d


def propose_revisions(canvas, gh, weeks=range(2, 10), logins=None):
    """Weeks 2-9: 1 point for any issue, PR, or comment the student made on
    GitHub (a commit, compare page, or fork PR counts too). Returns the
    proposals and the GitHub-to-Canvas mapping. `logins` maps a Canvas
    user_id to the GitHub login (or list of logins) you have confirmed."""
    roster = canvas.roster().set_index("user_id")
    subs = []
    for a in canvas.group_assignments("Textbook Revisions"):
        wk = week_of(a["name"])
        if wk not in weeks:
            continue
        for s in canvas.submissions(a["id"]):
            if s["user_id"] in roster.index:
                subs.append((wk, a, s))
    resolved = {}
    for wk, a, s in subs:
        if s.get("url"):
            resolved[(wk, s["user_id"])] = resolve(gh, s["url"])
    # each student's GitHub login: confirmed, else the most common author of their links
    votes = defaultdict(Counter)
    for (wk, uid), d in resolved.items():
        if d.get("author"):
            votes[uid][d["author"]] += 1
    login = {uid: c.most_common(1)[0][0] for uid, c in votes.items()}
    mine = {uid: {l} for uid, l in login.items()}
    for uid, l in (logins or {}).items():
        mine[uid] = {l} if isinstance(l, str) else set(l)
        login[uid] = sorted(mine[uid])[0]
    mapping = pd.DataFrame([{"user_id": uid, "name": roster.loc[uid, "name"],
                             "identikey": roster.loc[uid, "identikey"],
                             "github": ", ".join(sorted(mine.get(uid, set()))),
                             "other_logins": ", ".join(k for k in votes[uid] if k not in mine.get(uid, set()))}
                            for uid in roster.index])
    seen = defaultdict(list)
    rows = []
    for wk, a, s in sorted(subs, key=lambda x: x[0]):
        uid, name = s["user_id"], roster.loc[s["user_id"], "name"]
        base = dict(kind="revision", week=wk, assignment_id=a["id"], user_id=uid, name=name,
                    url=s.get("url") or "")
        if s["workflow_state"] == "unsubmitted" or not s.get("url"):
            rows.append(proposal(**base, score=0, notes="no submission"))
            continue
        d, me = resolved[(wk, uid)], mine.get(uid, set())
        notes, review, score, comment = [d["type"]], False, 1, ""
        # what counts as "the same item": a comment, a review, a commit, an
        # issue or PR, or (for files and compare pages) the link itself
        key = (d.get("owner", "").lower(), d.get("repo", "").lower(),
               d.get("comment_id") or d.get("review_id") or d.get("sha") or d.get("number")
               or re.sub(r"[#?].*$", "", d["url"]).lower())
        if d["type"] == "not github":
            score, review = 0, True
            notes.append("not a GitHub link")
        elif d.get("author") not in me:
            if me & set(d.get("participants", [])):
                comment = COMMENTS["own_comment"]
                notes.append(f"linked {d.get('author')}'s item; the student commented on it")
            else:
                score, review = 0, True
                notes.append(f"item is by {d.get('author')}, not {', '.join(sorted(me)) or 'a known login'}")
        if d["type"] in ("commit", "compare", "file", "repo"):
            notes.append("not an issue, PR, or comment (counts if it's the student's)")
        if not d.get("class_repo") and d["type"] != "not github":
            notes.append(f"in {d.get('owner')}/{d.get('repo')}")
        if d.get("size") is not None and d["type"] in ("issuecomment", "review") and d["size"] < 80:
            notes.append(f"short ({d['size']} characters)")
            review = True
        seen[(uid, key)].append(len(rows))
        rows.append(proposal(**base, score=score, comment=comment, review=review,
                             notes="; ".join(notes), created=d.get("created_at") or ""))
    # The same item submitted for more than one week earns credit once, in the
    # week it was made (by its creation date); the other weeks earn 0.
    for (uid, key), idx in seen.items():
        if len(idx) < 2:
            continue
        created = rows[idx[0]]["created"]
        made = _week_number(_ts(created).astimezone(spec.TZ).date()) if created else None
        keep = min(idx, key=lambda i: abs(rows[i]["week"] - made)) if made else idx[0]
        for i in idx:
            if i != keep:
                rows[i].update(score=0, review=True, comment="",
                               notes=rows[i]["notes"] + f"; same item as week {rows[keep]['week']}, "
                                     f"where it was made: credit once")
    return pd.DataFrame(rows).drop(columns=["created"]), mapping


# -------------------------------------------------------------- portfolios

def repo_at(url, due_at, workdir=None):
    """Clone a student's public portfolio repo and check out its state at the
    deadline. Returns the checkout's path, or None if nothing was pushed by then."""
    d = parse_github_url(url)
    if d["type"] == "not github":
        return None
    workdir = Path(workdir or GRADING_DIR / "repos")
    path = workdir / f"{d['owner']}__{d['repo']}".lower()
    remote = f"https://github.com/{d['owner']}/{d['repo']}"
    if path.exists():
        subprocess.run(["git", "-C", str(path), "fetch", "-q", "origin"], check=True)
    else:
        workdir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", "-q", "--filter=blob:none", remote, str(path)], check=True)
    sha = subprocess.run(["git", "-C", str(path), "rev-list", "-1", f"--before={due_at}", "origin/HEAD"],
                         capture_output=True, text=True).stdout.strip()
    if not sha:
        return None
    subprocess.run(["git", "-C", str(path), "checkout", "-q", "--detach", sha], check=True)
    return path


def _readme_sections(path):
    readme = next((p for p in path.glob("*") if p.name.lower() == "readme.md"), None)
    text = readme.read_text(errors="replace") if readme else ""
    heads = [h.strip().lower() for h in re.findall(r"^#+\s*(.+)$", text, re.M)]
    return text, heads


def _section_words(text, name):
    """Words under the fullest README heading that starts with `name`."""
    found = re.findall(rf"^#+\s*{name}[^\n]*\n(.*?)(?=^#|\Z)", text, re.M | re.S | re.I)
    return max((len(f.split()) for f in found), default=0)


def _notebook_outputs(path):
    n_out = n_code = 0
    for nb in path.rglob("*.ipynb"):
        try:
            cells = json.loads(nb.read_text(errors="replace")).get("cells", [])
        except ValueError:
            continue
        for c in cells:
            if c.get("cell_type") == "code" and "".join(c.get("source", [])).strip():
                n_code += 1
                n_out += bool(c.get("outputs"))
    return n_code, n_out


def portfolio_checks(path, week):
    """The two criteria of a week's checkpoint, met (1) or not (0), with the
    evidence. These are checks for presence; read anything borderline."""
    if path is None:
        return [0, 0], "nothing pushed by the deadline"
    files = [p for p in path.rglob("*") if p.is_file() and ".git" not in p.parts]
    names = {p.name.lower() for p in files}
    text, heads = _readme_sections(path)
    nbs = [p for p in files if p.suffix == ".ipynb"]
    code = [p for p in files if p.suffix in (".py", ".ipynb")]
    data = [p for p in files if "data" in [x.lower() for x in p.relative_to(path).parts[:-1]]]
    figs = [p for p in files if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".svg", ".pdf") and p.name.lower() != "report.pdf"]
    report = next((p for p in files if p.name.lower() in ("report.md", "report.pdf")), None)
    n_code, n_out = _notebook_outputs(path)
    ev = [f"files: {len(files)}", f"README headings: {', '.join(heads[:8]) or 'none'}"]
    if week == 11:
        c1 = int(bool(text) and len(text.split()) >= 40 and sum(h in " ".join(heads) for h in ("data", "method", "finding", "reproduc")) >= 3)
        c2 = int("proposal.md" in names and bool(nbs) and (report is not None or "report" in text.lower()) and any((path / d).is_dir() for d in ("data", "Data")))
    elif week == 12:
        c1 = int(bool(code) and any(re.search(r"user-agent|headers\s*=", p.read_text(errors="replace"), re.I) for p in code if p.stat().st_size < 5_000_000))
        c2 = int(bool(data) and _section_words(text, "data") >= 40)
        ev.append(f"data files: {len(data)}; Data section: {_section_words(text, 'data')} words")
    elif week == 13:
        c1 = int(n_code > 0 and n_out >= max(1, n_code // 2))
        c2 = int(bool(figs) and _section_words(text, "method") >= 20 and _section_words(text, "finding") >= 20)
        ev.append(f"code cells with output: {n_out} of {n_code}; figures: {len(figs)}")
    elif week == 14:
        words = len(report.read_text(errors="replace").split()) if report and report.suffix == ".md" else None
        c1 = int(report is not None and (words is None or words >= 1000))
        c2 = int({"readme.md", "proposal.md"} <= names and bool(nbs) and report is not None
                 and _section_words(text, "reproduc") + _section_words(text, "how to") >= 20)
        ev.append(f"report: {report.name if report else 'none'}" + (f", {words} words" if words else ""))
    else:
        raise ValueError(f"week {week} has no portfolio checkpoint")
    return [c1, c2], "; ".join(ev)


def propose_portfolio(canvas, week):
    a = canvas.assignment(spec.revision_name(week))
    roster = canvas.roster().set_index("user_id")
    rows = []
    for s in canvas.submissions(a["id"]):
        if s["user_id"] not in roster.index:
            continue
        base = dict(kind="portfolio", week=week, assignment_id=a["id"], user_id=s["user_id"],
                    name=roster.loc[s["user_id"], "name"], url=s.get("url") or "")
        if not s.get("url"):
            rows.append(proposal(**base, rubric=[0, 0], notes="no submission"))
            continue
        try:
            path = repo_at(s["url"], a["due_at"])
            pts, ev = portfolio_checks(path, week)
        except subprocess.CalledProcessError as e:
            pts, ev = [0, 0], f"could not clone: {e}"
        rows.append(proposal(**base, rubric=pts, review=(sum(pts) < 2), notes=ev))
    return pd.DataFrame(rows)


# -------------------------------------------------------------------- labs

def download_labs(canvas, week):
    """Each student's HTML upload for a week's lab, saved under GRADING_DIR."""
    a = canvas.assignment(next(x["name"] for x in spec.lab_assignments() if week_of(x["name"]) == week))
    out = GRADING_DIR / "labs" / f"week-{week:02d}"
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for s in canvas.submissions(a["id"]):
        files = []
        for i, att in enumerate(s.get("attachments") or []):
            p = out / f"{s['user_id']}_{i}.html.txt"   # .txt: never opened as a web page by accident
            p.write_bytes(canvas.s.get(att["url"]).content)
            files.append(str(p))
        rows.append({"user_id": s["user_id"], "state": s["workflow_state"], "late": s.get("late"),
                     "submitted_at": s.get("submitted_at"), "files": files})
    return a, rows


def _cells(soup):
    out = []
    for c in soup.select("div.jp-Cell") or soup.select("div.cell"):
        cls = c.get("class", [])
        if "jp-MarkdownCell" in cls or "text_cell" in cls:
            out.append({"t": "md", "text": c.get_text("\n", strip=True)})
        elif "jp-CodeCell" in cls or "code_cell" in cls:
            ed = c.select_one(".jp-InputArea-editor, .input_area")
            outs = c.select(".jp-OutputArea-output, .output_area")
            otext = "\n".join(o.get_text("\n", strip=True) for o in outs)
            prompt = c.select_one(".jp-InputPrompt, .input_prompt")
            out.append({"t": "code", "code": ed.get_text() if ed else "", "nout": len(outs),
                        "exc": bool(re.search(r"Traceback \(most recent call last\)|^\w+(Error|Exception):", otext, re.M)),
                        "ran": bool(prompt and re.search(r"\d", prompt.get_text())), "otext": otext})
    return out


STEP = re.compile(r"(?:^|\n)\s*(?:#+\s*)?(?:\*\*)?Step\s*(\d+)\s*(?:—|–|-|:|\.|\*\*|¶|$)", re.I | re.M)
END = re.compile(r"^\s*#*\s*(Additional Exercises|Social History|Public Interest|Common Issues|Key Takeaways|Further Reading|Missing Manual Reference)", re.I)
AGENT_SIGNS = re.compile(r"revise it to reflect your own|no measurements have been invented|example interpretation|as an ai\b", re.I)


def _section(cells):
    start = next((i for i, c in enumerate(cells) if c["t"] == "md" and re.search(r"^\s*#*\s*Recommended Exercises", c["text"], re.M)), None)
    if start is None:
        start = next((i for i, c in enumerate(cells) if re.search(r"Step\s*1\b", c.get("text") or c.get("code") or "")), None)
    if start is None:
        return None
    sec = []
    for c in cells[start:]:
        if sec and c["t"] == "md" and END.search(c["text"]):
            break
        sec.append(c)
    return sec


def _by_step(sec):
    cur, out = 0, defaultdict(list)
    for c in sec:
        found = [int(x) for x in STEP.findall(c.get("text") if c["t"] == "md" else c["code"]) if 0 < int(x) < 12]
        if found:
            cur = max(found)
        out[cur].append(c)
    return out


def _code_lines(cells):
    return Counter(l.strip() for c in cells if c["t"] == "code" for l in c["code"].splitlines()
                   if l.strip() and not l.strip().startswith("#"))


def _words(cells):
    """Words in an interpretation, wherever it was written: Markdown, comments,
    or a string or print() in a code cell."""
    w = Counter()
    for c in cells:
        t = c["text"] if c["t"] == "md" else c["code"]
        w.update(x.lower() for x in re.findall(r"[A-Za-z']{2,}", t))
    return w


def scaffold(week, gh=None):
    """The companion notebook as students got it: the book's version just
    before the lab's due date. Returns its cells in the same shape as _cells."""
    gh = gh or GitHub()
    slug = spec.week_info(week)[4]
    due = next(a["due_at"] for a in spec.lab_assignments() if week_of(a["name"]) == week)
    commits = gh.get(f"/repos/{BOOK[0]}/{BOOK[1]}/commits?path=notebooks/{slug}.ipynb&until={due}&per_page=10")
    shas = [c["sha"] for c in commits] if isinstance(commits, list) else []
    raw = None
    # Some versions of a notebook were broken JSON (an edit in the browser);
    # step back to the most recent version that parses.
    for sha in shas or ["main"]:
        try:
            raw = requests.get(f"https://raw.githubusercontent.com/{BOOK[0]}/{BOOK[1]}/{sha}/notebooks/{slug}.ipynb").json()
            break
        except ValueError:
            continue
    if raw is None:
        raise RuntimeError(f"no readable version of notebooks/{slug}.ipynb before {due}")
    cells = []
    for c in raw["cells"]:
        src = "".join(c["source"])
        if c["cell_type"] == "markdown":
            cells.append({"t": "md", "text": re.sub(r"[*`_#>]", "", src)})
        elif c["cell_type"] == "code":
            cells.append({"t": "code", "code": src, "nout": 0, "exc": False, "ran": False, "otext": ""})
    return cells


def analyze_lab(paths, week, scaffold_cells):
    """Automated checks on one student's HTML upload(s). With more than one
    file, the one with the most work is used."""
    if len(paths) > 1:
        results = [analyze_lab([p], week, scaffold_cells) for p in paths]
        best = max(results, key=lambda r: (len(r["attempted"]), r["interp_words"]))
        best["irregular"] = best["irregular"] + [f"{len(paths)} files; checked the fullest"]
        return best
    from bs4 import BeautifulSoup
    irregular = []
    cells = _cells(BeautifulSoup(Path(paths[0]).read_text(errors="replace"), "lxml"))
    if not cells:
        irregular.append("not a Jupyter HTML export: score by hand")
    sec = _section(cells)
    found = sec is not None
    if not found:
        irregular.append("no Recommended Exercises section or step labels: score by hand")
        sec = cells
    steps, sc = _by_step(sec), _by_step(_section(scaffold_cells) or [])
    n = max([k for k in sc] + [0])
    if n == 0:
        irregular.append("the scaffold has no numbered steps (weeks 2 and earlier)")
    required = [k for k in range(1, n) if k not in OPTIONAL_STEPS.get(week, set())]
    attempted = [k for k in required if sum((_code_lines(steps.get(k, [])) - _code_lines(sc.get(k, []))).values()) > 0]
    student = [c for c in sec if c["t"] == "code" and any(l.strip() and not l.strip().startswith("#") for l in c["code"].splitlines())]
    interp = sum((_words(steps.get(n, [])) - _words(sc.get(n, []))).values()) if n else 0
    if interp < 3:
        # an answer under its own heading ("Final interpretation") rather than the last step
        extra = [c for c in sec if c["t"] == "md" and re.match(r"\s*(final\s+)?interpret", c["text"], re.I)]
        interp = max(interp, sum((_words(extra) - _words(sc.get(n, []))).values()))
    text = " ".join((c.get("text") or c.get("code") or "") for c in sec)
    return {"required": required, "attempted": attempted, "found": found and bool(cells),
            "code_cells": len(student), "unrun": sum(not c["ran"] for c in student),
            "traceback": any(c["exc"] for c in student), "interp_words": interp,
            "has_numbers_no_output": bool(re.search(r"\d{2,}", " ".join(c.get("text", "") for c in steps.get(n, [])))) and not any(c["nout"] for c in student),
            "agent_signs": bool(AGENT_SIGNS.search(text)), "irregular": irregular}


def propose_labs(canvas, week, unrun_full_credit=None, gh=None):
    """Proposals for one week's lab. Criteria 1-4 come from the checks;
    criterion 5 ("each step does its task") is set to 2 and marked for review
    wherever anything looks off, since only a reader can judge it.
    unrun_full_credit: weeks 4-9 gave unrun code full credit; the rubric from
    week 11 doesn't. Defaults by week."""
    if unrun_full_credit is None:
        unrun_full_credit = week < 11
    a, subs = download_labs(canvas, week)
    sc = scaffold(week, gh)
    roster = canvas.roster().set_index("user_id")
    rows = []
    for s in subs:
        if s["user_id"] not in roster.index:
            continue
        base = dict(kind="lab", week=week, assignment_id=a["id"], user_id=s["user_id"],
                    name=roster.loc[s["user_id"], "name"])
        if not s["files"]:
            rows.append(proposal(**base, score=0, notes="no submission"))
            continue
        r = analyze_lab(s["files"], week, sc)
        req, att = r["required"], r["attempted"]
        e2 = 2 if len(att) == len(req) else 1 if len(att) >= len(req) / 2 else 0
        if unrun_full_credit or r["unrun"] == 0:
            e3 = 2 if r["code_cells"] else 0
        else:
            e3 = 1 if r["unrun"] < r["code_cells"] else 0
        e4 = 2 if r["interp_words"] >= 50 else 1 if r["interp_words"] >= 3 else 0
        pts = [2, e2, e3, e4, 2]
        comments, notes, review = [], [], False
        blank = r["found"] and not att and r["interp_words"] < 10
        if not r["found"]:
            rows.append(proposal(**base, score="", review=True, notes="; ".join(r["irregular"])))
            continue
        if blank:
            score, comments = 0, [COMMENTS["blank"]]
        else:
            score = sum(pts)
            if r["has_numbers_no_output"]:
                comments.append(COMMENTS["unseen"]); review = True
                notes.append("interpretation cites numbers but nothing ran")
            elif r["unrun"]:
                comments.append(COMMENTS["unrun"])
            if r["traceback"]:
                comments.append(COMMENTS["traceback"])
            days = late_days(s["submitted_at"], a["due_at"])
            if days:
                ded = min(days, LATE_CAP)
                score = max(0, score - ded)
                comments.append(late_comment(days, ded))
        missing = [k for k in req if k not in att]
        notes += [f"steps missing: {missing}" if missing else "all required steps",
                  f"{r['unrun']} of {r['code_cells']} code cells unrun",
                  f"interpretation ~{r['interp_words']} new words"] + r["irregular"]
        if r["agent_signs"]:
            notes.append("phrases that look AI-generated: hold for the instructor?")
        review = review or blank or bool(missing) or e4 == 1 or r["agent_signs"] or bool(r["irregular"])
        rows.append(proposal(**base, rubric=pts if week >= 11 else "", score=score,
                             comment=" ".join(comments), review=review, notes="; ".join(notes)))
    return pd.DataFrame(rows)


# ------------------------------------------------------------------ status

def summary(df):
    """Counts by action and score, and the rows that still need review."""
    counts = df.groupby(["action", "score"], dropna=False).size().rename("rows").reset_index()
    return counts, df[df["review"]][["week", "name", "score", "notes", "url"]]


def needs_grading(canvas, groups=("Notebook Labs", "Textbook Revisions", "Final Project")):
    """Submissions with no score, or resubmitted after grading, in published
    assignments: what is left to grade or to look at."""
    roster = canvas.roster().set_index("user_id")
    out = []
    for g in groups:
        for a in canvas.group_assignments(g):
            if not a.get("published"):
                continue
            for s in canvas.submissions(a["id"]):
                if s["user_id"] not in roster.index or not s.get("submitted_at"):
                    continue
                regraded = s.get("graded_at") and s["submitted_at"] > s["graded_at"]
                if s.get("score") is None or regraded:
                    last = (s.get("submission_comments") or [{}])[-1].get("comment", "")
                    out.append({"assignment": a["name"], "name": roster.loc[s["user_id"], "name"],
                                "score": s.get("score"), "submitted_at": s["submitted_at"][:16],
                                "resubmitted_after_grading": bool(regraded), "last_comment": last[:90]})
    return pd.DataFrame(out)
