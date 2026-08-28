#!/usr/bin/env python3
"""Move notebook labs and textbook revisions to Sunday 11:59pm, fix the
assignment-group weights, and drop the dead Week 16 slides link.

Matches assignments by Canvas id rather than by name. course_spec.py has
drifted from the live course (week 2's revision is titled "First issue on
Chapter 2" there, and its lab was moved to Friday when week 1's content
shifted forward), so migrate.py's name matching would create duplicates
instead of updating what is already there.

Dry run unless you pass --apply.

    export CANVAS_TOKEN=...
    python retime.py            # show what would change
    python retime.py --apply    # change it
"""
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime

import course_spec as spec

HOST = "canvas.colorado.edu"
CID = spec.NEW_COURSE_ID
DEAD_SLIDES_ITEM = (995499, 7729231)   # (module id, item id) — "Slides: Week 16"

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
        return json.load(f) if f.status != 204 else {}


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


def fmt(iso):
    if not iso:
        return "(none)"
    return (datetime.fromisoformat(iso.replace("Z", "+00:00"))
            .astimezone(spec.TZ).strftime("%a %b %d %H:%M"))


def main():
    mode = "APPLY" if APPLY else "DRY RUN"
    print(f"=== {mode} — course {CID} ===\n")

    # ---- 1. due dates ----------------------------------------------------
    groups = {g["name"]: g for g in get_all(f"/courses/{CID}/assignment_groups")}
    target_gids = {groups[n]["id"]: n for n in ("Notebook Labs", "Textbook Revisions")
                   if n in groups}

    print("--- due dates -> Sunday 11:59pm ---")
    changed = skipped = 0
    for a in get_all(f"/courses/{CID}/assignments"):
        if a["assignment_group_id"] not in target_gids:
            continue
        m = re.match(r"^Week (\d+) (Lab|Revision)\b", a["name"])
        if not m:
            print(f"  !! unparsed name, left alone: {a['name']}")
            skipped += 1
            continue
        wk = int(m.group(1))
        want = spec.due_at(spec.sunday_of(wk))
        if a.get("due_at") and fmt(a["due_at"]) == fmt(want):
            print(f"  =  {a['name'][:46]:<48} already {fmt(want)}")
            continue
        print(f"  -> {a['name'][:46]:<48} {fmt(a.get('due_at')):>16}  =>  {fmt(want)}")
        changed += 1
        if APPLY:
            call("PUT", f"/courses/{CID}/assignments/{a['id']}",
                 {"assignment[due_at]": want})
    print(f"  {changed} to change, {skipped} unparsed\n")

    # ---- 2. group weights ------------------------------------------------
    print("--- assignment group weights -> 30 / 15 / 15 / 40 ---")
    for g in spec.GROUPS:
        live = groups.get(g["name"])
        if live is None:
            print(f"  +  create '{g['name']}' weight={g['group_weight']} "
                  f"position={g['position']}")
            if APPLY:
                call("POST", f"/courses/{CID}/assignment_groups",
                     {"name": g["name"], "group_weight": g["group_weight"],
                      "position": g["position"]})
            continue
        if (live.get("group_weight") != g["group_weight"]
                or live.get("position") != g["position"]):
            print(f"  -> {g['name']:<20} weight {live.get('group_weight')} "
                  f"=> {g['group_weight']}, position {live.get('position')} "
                  f"=> {g['position']}")
            if APPLY:
                call("PUT", f"/courses/{CID}/assignment_groups/{live['id']}",
                     {"group_weight": g["group_weight"], "position": g["position"]})
        else:
            print(f"  =  {g['name']:<20} weight {g['group_weight']} already correct")
    print()

    # ---- 3. dead Week 16 slides link -------------------------------------
    print("--- dead module item ---")
    mid, iid = DEAD_SLIDES_ITEM
    try:
        item = call("GET", f"/courses/{CID}/modules/{mid}/items/{iid}")
    except urllib.error.HTTPError as e:
        print(f"  item {iid} not found ({e.code}) — already gone")
    else:
        print(f"  -  delete [{iid}] {item['title']}")
        print(f"        -> {item.get('external_url')}")
        if APPLY:
            call("DELETE", f"/courses/{CID}/modules/{mid}/items/{iid}")
            print("     deleted")

    if not APPLY:
        print("\nDry run. Re-run with --apply to make these changes.")


if __name__ == "__main__":
    main()
