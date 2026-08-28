#!/usr/bin/env python3
"""Create the weekly attendance assignments from course_spec.py.

One 1-point, no-submission entry per week the class meets — 15 in all
(weeks 1–14 and 16; week 15 is Fall Break and drops out on its own).
Existing assignments with the same name in the Attendance group are left
alone, so re-running is safe. Creation only: this never updates or
deletes, and it refuses to run if the Attendance group is missing.

migrate.py is not used for this because its name matching would also
try to update every other assignment, and the live course has drifted
from the spec (week 2's titles differ) — a full build would duplicate
week 2's revision.

Dry run unless you pass --apply.

    export CANVAS_TOKEN=...
    python create_attendance.py            # show what would be created
    python create_attendance.py --apply    # create it
"""
import json
import os
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
    print(f"=== {mode} — attendance assignments, course {CID} ===\n")

    groups = {g["name"]: g for g in get_all(f"/courses/{CID}/assignment_groups")}
    if "Attendance" not in groups:
        sys.exit("No 'Attendance' assignment group on the live course — "
                 "create it first (retime.py does).")
    att_gid = groups["Attendance"]["id"]

    existing = {a["name"] for a in get_all(f"/courses/{CID}/assignments")
                if a["assignment_group_id"] == att_gid}

    created = present = 0
    for a in spec.attendance_assignments():
        if a["name"] in existing:
            print(f"  =  {a['name']} already exists")
            present += 1
            continue
        print(f"  +  {a['name']}  ({a['points_possible']} pt, no submission)")
        created += 1
        if APPLY:
            call("POST", f"/courses/{CID}/assignments", {
                "assignment[name]": a["name"],
                "assignment[assignment_group_id]": att_gid,
                "assignment[points_possible]": a["points_possible"],
                "assignment[submission_types][]": a["submission_types"],
                "assignment[description]": a["description"],
                "assignment[published]": True,
            })
    print(f"\n  {created} to create, {present} already present")
    if not APPLY:
        print("\nDry run. Re-run with --apply to make these changes.")


if __name__ == "__main__":
    main()
