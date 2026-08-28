#!/usr/bin/env python3
"""Sync live lab and revision assignments with course_spec.py.

The book's chapters now split their exercises into a guided "Recommended
Exercises" build (the take-home, submitted as a completed notebook) and
open-ended "Additional Exercises". The lab descriptions on Canvas still
described a single undifferentiated exercises section; this pushes the
new wording from spec.lab_assignments() to the live course.

Labs get their description, submission_types (upload only), and
allowed_extensions (html only). Revisions get their description and
submission_types (URL only). Assignments are matched by Canvas id via
the "Week N Lab" / "Week N Revision" prefix, not by full name, because
the live course has drifted from the spec (week 2 carries different
titles than the spec generates). Names, points, and due dates are left
alone.

Dry run unless you pass --apply.

    export CANVAS_TOKEN=...
    python relabel_labs.py            # show what would change
    python relabel_labs.py --apply    # change it
"""
import json
from html import unescape
import os
import re
import sys
import urllib.parse
import urllib.request

import course_spec as spec

HOST = "canvas.colorado.edu"
CID = spec.NEW_COURSE_ID

APPLY = "--apply" in sys.argv
TOKEN = os.environ.get("CANVAS_TOKEN", "").strip()
if not TOKEN:
    sys.exit("No token. Set CANVAS_TOKEN.")


def call(method, path, data=None):
    url = f"https://{HOST}/api/v1{path}"
    body = None
    headers = {"Authorization": f"Bearer {TOKEN}"}
    if data is not None:
        body = urllib.parse.urlencode(data, doseq=True).encode()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=30) as f:
        return json.load(f)


def get_all(path, **params):
    params.setdefault("per_page", 100)
    out, url = [], f"{path}?{urllib.parse.urlencode(params)}"
    while url:
        req = urllib.request.Request(
            f"https://{HOST}/api/v1{url}" if url.startswith("/") else url,
            headers={"Authorization": f"Bearer {TOKEN}"})
        with urllib.request.urlopen(req, timeout=30) as f:
            out.extend(json.load(f))
            link = f.headers.get("Link", "")
        url = ""
        for part in link.split(","):
            if 'rel="next"' in part:
                url = part.split(";")[0].strip().strip("<>")
    return out


def main():
    mode = "APPLY" if APPLY else "DRY RUN"
    print(f"=== {mode} — lab + revision sync, course {CID} ===\n")

    # What the spec wants for each assignment kind, keyed by week.
    want = {}
    for a in spec.lab_assignments():
        wk = int(re.match(r"Week (\d+) Lab", a["name"]).group(1))
        want[("Lab", wk)] = a
    for a in spec.revision_assignments():
        wk = int(re.match(r"Week (\d+) Revision", a["name"]).group(1))
        want[("Revision", wk)] = a

    groups = {g["name"]: g for g in get_all(f"/courses/{CID}/assignment_groups")}
    kind_of_gid = {groups["Notebook Labs"]["id"]: "Lab",
                   groups["Textbook Revisions"]["id"]: "Revision"}

    def visible(html):
        text = re.sub(r"<[^>]+>", " ", html or "")
        return " ".join(unescape(text).split())

    changed = skipped = same = 0
    for a in get_all(f"/courses/{CID}/assignments"):
        kind = kind_of_gid.get(a["assignment_group_id"])
        if kind is None:
            continue
        m = re.match(rf"^Week (\d+) {kind}\b", a["name"])
        if not m:
            print(f"  !! unparsed name, left alone: {a['name']}")
            skipped += 1
            continue
        spec_a = want.get((kind, int(m.group(1))))
        if spec_a is None:
            print(f"  !! no spec entry: {a['name']}")
            skipped += 1
            continue

        diffs = []
        # Week 2's revision is the customized "first issue" assignment --
        # its live description is intentionally different from the generic
        # PR text the spec generates, so never overwrite it.
        keep_description = (kind, int(m.group(1))) == ("Revision", 2)
        if not keep_description and \
                visible(a.get("description")) != visible(spec_a["description"]):
            diffs.append("description")
        if sorted(a.get("submission_types") or []) != sorted(spec_a["submission_types"]):
            diffs.append(f"types {a.get('submission_types')} -> {spec_a['submission_types']}")
        want_ext = spec_a.get("allowed_extensions") or []
        if want_ext and sorted(a.get("allowed_extensions") or []) != sorted(want_ext):
            diffs.append(f"extensions {a.get('allowed_extensions')} -> {want_ext}")

        if not diffs:
            same += 1
            continue
        print(f"  -> {a['name']}")
        for d in diffs:
            print(f"       {d}")
        changed += 1
        if APPLY:
            data = {"assignment[submission_types][]": spec_a["submission_types"]}
            if not keep_description:
                data["assignment[description]"] = spec_a["description"]
            if want_ext:
                data["assignment[allowed_extensions][]"] = want_ext
            call("PUT", f"/courses/{CID}/assignments/{a['id']}", data)
    print(f"\n  {changed} to change, {same} already current, {skipped} skipped")
    if not APPLY:
        print("\nDry run. Re-run with --apply to make these changes.")


if __name__ == "__main__":
    main()
