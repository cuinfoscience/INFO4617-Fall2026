#!/usr/bin/env python3
"""Update the live lab assignments' descriptions to match course_spec.py.

The book's chapters now split their exercises into a guided "Recommended
Exercises" build (the take-home, submitted as a completed notebook) and
open-ended "Additional Exercises". The lab descriptions on Canvas still
described a single undifferentiated exercises section; this pushes the
new wording from spec.lab_assignments() to the live course.

Assignments are matched by Canvas id via the "Week N Lab" prefix, not by
full name, because the live course has drifted from the spec (week 2's
lab carries a different title than the spec generates). Only the
description field is written -- names, points, and due dates are left
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
        body = urllib.parse.urlencode(data).encode()
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
    print(f"=== {mode} — lab descriptions, course {CID} ===\n")

    # The spec's new description for each teaching week, keyed by week.
    want = {}
    for a in spec.lab_assignments():
        wk = int(re.match(r"Week (\d+) Lab", a["name"]).group(1))
        want[wk] = a["description"]

    groups = {g["name"]: g for g in get_all(f"/courses/{CID}/assignment_groups")}
    lab_gid = groups["Notebook Labs"]["id"]

    changed = skipped = same = 0
    for a in get_all(f"/courses/{CID}/assignments"):
        if a["assignment_group_id"] != lab_gid:
            continue
        m = re.match(r"^Week (\d+) Lab\b", a["name"])
        if not m:
            print(f"  !! unparsed name, left alone: {a['name']}")
            skipped += 1
            continue
        wk = int(m.group(1))
        new = want.get(wk)
        if new is None:
            print(f"  !! no spec description for week {wk}: {a['name']}")
            skipped += 1
            continue
        # Canvas rewrites stored HTML (link attributes, entity encoding),
        # so compare the visible text, entities decoded, not the raw markup.
        def visible(html):
            text = re.sub(r"<[^>]+>", " ", html or "")
            return " ".join(unescape(text).split())
        if visible(a.get("description")) == visible(new):
            same += 1
            continue
        print(f"  -> {a['name']}")
        old_text = re.sub(r"<[^>]+>", "", a.get("description") or "")
        print(f"       was: {old_text[:90]}...")
        changed += 1
        if APPLY:
            call("PUT", f"/courses/{CID}/assignments/{a['id']}",
                 {"assignment[description]": new})
    print(f"\n  {changed} to change, {same} already current, {skipped} skipped")
    if not APPLY:
        print("\nDry run. Re-run with --apply to make these changes.")


if __name__ == "__main__":
    main()
