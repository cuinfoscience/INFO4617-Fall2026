#!/usr/bin/env python3
"""Migrate INFO 4871 (Fall 2024) to INFO 4617 (Fall 2026) on Canvas.

Reads the target design from `course_spec.py` and makes the new Canvas course
match it: copies reusable content from the old course, then builds the
assignment groups, weekly assignments, modules, and syllabus page described by
the Fall 2026 syllabus.

SAFETY: every command is a dry run unless you pass --apply. A dry run makes only
GET requests and prints the writes it would perform.

Usage
-----
    export CANVAS_TOKEN=...                 # or use --token-file

    python migrate.py inspect               # read-only survey of both courses
    python migrate.py copy                  # dry run: content migration
    python migrate.py copy --apply          # actually copy files/pages
    python migrate.py build                 # dry run: groups/assignments/modules/syllabus
    python migrate.py build --apply         # actually build
    python migrate.py all --apply           # copy, then build

Useful flags
------------
    --only groups,assignments,modules,syllabus,settings   limit what `build` touches
    --include-slides       upload slides/week-NN/week-NN.pdf and link it in each module
    --host HOST            default canvas.colorado.edu
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import course_spec as spec  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------- API client

class CanvasError(RuntimeError):
    pass


class Canvas:
    def __init__(self, host: str, token: str, dry_run: bool = True):
        self.base = f"https://{host}/api/v1"
        self.token = token
        self.dry_run = dry_run
        self.writes = []          # recorded (method, path, payload) in dry-run

    # -- plumbing ----------------------------------------------------------
    def _request(self, method: str, url: str, data=None, raw_body=None,
                 content_type=None, _retry=0):
        if not url.startswith("http"):
            url = self.base + url
        body = None
        headers = {"Authorization": f"Bearer {self.token}"}
        if raw_body is not None:
            body = raw_body
            if content_type:
                headers["Content-Type"] = content_type
        elif data is not None:
            body = urllib.parse.urlencode(_flatten(data), doseq=True).encode()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

        req = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                payload = r.read().decode()
                link = r.headers.get("Link", "")
                return (json.loads(payload) if payload.strip() else None), link
        except urllib.error.HTTPError as e:
            detail = e.read().decode()[:600]
            # Canvas throttles with 403 + "Rate Limit Exceeded"
            if (e.code in (403, 502, 503) and "Rate Limit" in detail or e.code in (502, 503)) and _retry < 4:
                wait = 2 ** (_retry + 1)
                print(f"    [throttled/{e.code}] retrying in {wait}s", file=sys.stderr)
                time.sleep(wait)
                return self._request(method, url, data, raw_body, content_type, _retry + 1)
            if e.code == 401:
                raise CanvasError(
                    f"401 Unauthorized — {detail}\n"
                    "The API token is missing, expired, or lacks permission on this course."
                ) from e
            raise CanvasError(f"{method} {url} -> HTTP {e.code}: {detail}") from e
        except urllib.error.URLError as e:
            if _retry < 3:
                time.sleep(2 ** (_retry + 1))
                return self._request(method, url, data, raw_body, content_type, _retry + 1)
            raise CanvasError(f"{method} {url} -> {e}") from e

    def get(self, path, **params):
        if params:
            path += ("&" if "?" in path else "?") + urllib.parse.urlencode(params, doseq=True)
        return self._request("GET", path)[0]

    def get_all(self, path, **params):
        """GET with Link-header pagination."""
        params.setdefault("per_page", 100)
        path += ("&" if "?" in path else "?") + urllib.parse.urlencode(params, doseq=True)
        out, url = [], path
        while url:
            page, link = self._request("GET", url)
            if isinstance(page, list):
                out.extend(page)
            else:
                return page
            url = _next_link(link)
        return out

    def write(self, method, path, data=None, label=None):
        """POST/PUT/DELETE — suppressed (and recorded) during a dry run."""
        self.writes.append((method, path, data))
        if self.dry_run:
            print(f"    DRY-RUN {method} {path}" + (f"  # {label}" if label else ""))
            return {"id": f"<dry-run-{len(self.writes)}>", "_dry_run": True}
        result = self._request(method, path, data=data)[0]
        print(f"    {method} {path}" + (f"  # {label}" if label else ""))
        return result


def _next_link(link_header: str):
    for part in (link_header or "").split(","):
        seg = part.split(";")
        if len(seg) >= 2 and 'rel="next"' in seg[1]:
            return seg[0].strip().strip("<>")
    return None


def _flatten(data, parent=""):
    """Turn nested dicts/lists into Canvas's bracketed form-encoding."""
    items = []
    if isinstance(data, dict):
        for k, v in data.items():
            key = f"{parent}[{k}]" if parent else str(k)
            items.extend(_flatten(v, key))
    elif isinstance(data, (list, tuple)):
        for v in data:
            items.extend(_flatten(v, f"{parent}[]"))
    elif isinstance(data, bool):
        items.append((parent, "true" if data else "false"))
    elif data is None:
        items.append((parent, ""))
    else:
        items.append((parent, str(data)))
    return items


# ---------------------------------------------------------------- inspect

def cmd_inspect(api: Canvas, args):
    snapshot = {}
    for label, cid in (("old", spec.OLD_COURSE_ID), ("new", spec.NEW_COURSE_ID)):
        print(f"\n=== {label} course {cid} ===")
        course = api.get(f"/courses/{cid}", include=["term", "syllabus_body"])
        print(f"  name:        {course.get('name')}")
        print(f"  code:        {course.get('course_code')}")
        print(f"  workflow:    {course.get('workflow_state')}")
        print(f"  term:        {(course.get('term') or {}).get('name')}")
        print(f"  dates:       {course.get('start_at')} -> {course.get('conclude_at')}")
        print(f"  weighted:    {course.get('apply_assignment_group_weights')}")
        body = course.get("syllabus_body") or ""
        print(f"  syllabus:    {len(body)} chars")

        inv = {"course": course}
        for name, path in (
            ("assignment_groups", f"/courses/{cid}/assignment_groups"),
            ("assignments", f"/courses/{cid}/assignments"),
            ("modules", f"/courses/{cid}/modules"),
            ("pages", f"/courses/{cid}/pages"),
            ("files", f"/courses/{cid}/files"),
            ("quizzes", f"/courses/{cid}/quizzes"),
            ("announcements", f"/courses/{cid}/discussion_topics?only_announcements=true"),
            ("discussions", f"/courses/{cid}/discussion_topics"),
        ):
            try:
                got = api.get_all(path)
                inv[name] = got
                print(f"  {name:<18} {len(got) if isinstance(got, list) else 'n/a'}")
                if isinstance(got, list) and got and name in ("assignment_groups", "modules"):
                    for g in got[:20]:
                        extra = (f" ({g.get('group_weight')}%)"
                                 if name == "assignment_groups" else "")
                        print(f"      - {g.get('name')}{extra}")
            except CanvasError as e:
                inv[name] = {"error": str(e)}
                print(f"  {name:<18} ERROR: {str(e)[:120]}")
        snapshot[label] = inv

    out = Path(args.snapshot)
    out.write_text(json.dumps(snapshot, indent=2, default=str))
    print(f"\nWrote full snapshot -> {out}")
    return snapshot


# ---------------------------------------------------------------- copy

def cmd_copy(api: Canvas, args):
    """Copy reusable content (files, pages) from the old course.

    Canvas's selective-import course copy is a two-phase API flow, not a
    single POST: creating the migration with selective_import=true only
    gets it to workflow_state "waiting_for_select" -- passing a `select`
    payload in that same initial POST is silently ignored. The actual
    selection has to be submitted as a separate PUT to the migration
    resource, using property names Canvas hands back from its own
    /selective_data tree (e.g. "copy[all_attachments]" for files -- not
    "files"), which also tells us what content types the source course
    actually has, so we don't hardcode types a given course might lack.
    """
    print(f"\n=== content migration: {spec.OLD_COURSE_ID} -> {spec.NEW_COURSE_ID} ===")
    payload = {
        "migration_type": "course_copy_importer",
        "settings": {"source_course_id": spec.OLD_COURSE_ID},
    }
    selective = not args.everything
    if selective:
        # Only bring across durable assets. The old course's assignments and
        # modules follow the 2024 design (Attendance/Module Assignments/Final)
        # and would fight the new 30/30/40 structure, so they stay behind.
        payload["selective_import"] = True
        print("  scope: files + pages only (old assignments/modules intentionally skipped)")
        print("         pass --everything to copy the entire old course instead")
    else:
        print("  scope: ENTIRE old course (assignments, modules, quizzes, everything)")

    res = api.write("POST", f"/courses/{spec.NEW_COURSE_ID}/content_migrations",
                    payload, label="start course copy")
    if api.dry_run:
        return
    mig_id = res.get("id")
    print(f"  migration id {mig_id}")

    if selective:
        # Wait for Canvas to finish indexing the source course before the
        # selective_data tree is queryable.
        for _ in range(60):
            st = api.get(f"/courses/{spec.NEW_COURSE_ID}/content_migrations/{mig_id}")
            if st.get("workflow_state") == "waiting_for_select":
                break
            if st.get("workflow_state") == "failed":
                raise CanvasError(f"migration failed before selection: {json.dumps(st)[:500]}")
            time.sleep(3)
        else:
            raise CanvasError("migration never reached waiting_for_select; "
                              "check Canvas manually before re-running")

        tree = api.get(f"/courses/{spec.NEW_COURSE_ID}/content_migrations/{mig_id}/selective_data")
        wanted_types = {"attachments", "pages"}
        selection = {}
        for node in tree:
            if node.get("type") in wanted_types:
                selection[node["property"]] = "1"
                print(f"    selecting: {node['title']} ({node.get('count', 0)} items)")
        if not selection:
            print("    nothing to select (source has no files or pages) -- skipping copy")
            return
        api.write("PUT", f"/courses/{spec.NEW_COURSE_ID}/content_migrations/{mig_id}",
                  selection, label="submit selective-import choices")

    print("  waiting for completion...")
    for _ in range(120):
        time.sleep(5)
        st = api.get(f"/courses/{spec.NEW_COURSE_ID}/content_migrations/{mig_id}")
        state = st.get("workflow_state")
        prog = (st.get("migration_issues_count") or 0)
        print(f"    state={state} issues={prog}")
        if state in ("completed", "failed"):
            if state == "failed":
                raise CanvasError(f"content migration failed: {json.dumps(st)[:500]}")
            print("  copy complete.")
            return
    print("  still running — check Canvas; the build step does not depend on it.")


# ---------------------------------------------------------------- build

def _index_by_name(items):
    return {i.get("name"): i for i in (items or []) if isinstance(i, dict)}


def build_settings(api, args):
    print("\n--- course settings ---")
    data = {"course": {
        "name": f"{spec.COURSE_NAME} ({spec.COURSE_CODE}, {spec.TERM})",
        "course_code": spec.COURSE_CODE,
        "start_at": spec.due_at(spec.FIRST_DAY, 8, 0),
        "conclude_at": spec.due_at(spec.LAST_DAY, 23, 59),
        "apply_assignment_group_weights": True,
        "default_view": "modules",
    }}
    api.write("PUT", f"/courses/{spec.NEW_COURSE_ID}", data,
              label="name/dates/weighted grading/home=modules")


def build_groups(api, args):
    print("\n--- assignment groups (30 / 30 / 40) ---")
    existing = _index_by_name(api.get_all(f"/courses/{spec.NEW_COURSE_ID}/assignment_groups"))
    ids = {}
    for g in spec.GROUPS:
        # Drop rules (e.g. drop_lowest:2) are deliberately NOT sent here.
        # Canvas rejects a drop rule that exceeds the group's current
        # assignment count, and on a fresh course that count is 0 at this
        # point in the build -- see apply_group_rules(), which sets them
        # after build_assignments() has populated each group.
        payload = {"name": g["name"], "group_weight": g["group_weight"],
                   "position": g["position"]}
        if g["name"] in existing:
            gid = existing[g["name"]]["id"]
            api.write("PUT", f"/courses/{spec.NEW_COURSE_ID}/assignment_groups/{gid}",
                      payload, label=f"update {g['name']} ({g['group_weight']}%)")
            ids[g["name"]] = gid
        else:
            res = api.write("POST", f"/courses/{spec.NEW_COURSE_ID}/assignment_groups",
                            payload, label=f"create {g['name']} ({g['group_weight']}%)")
            ids[g["name"]] = res.get("id")

    # Flag any leftover groups from the old design rather than deleting silently.
    known = {g["name"] for g in spec.GROUPS}
    for name, g in existing.items():
        if name not in known:
            weight = g.get("group_weight")
            count = len(g.get("assignments") or [])
            print(f"    NOTE leftover group '{name}' ({weight}%, {count} assignments) "
                  f"— left in place; delete it in Canvas if unwanted")
    return ids


def apply_group_rules(api, args, group_ids):
    """Set drop rules (e.g. drop_lowest:2) now that build_assignments() has
    populated each group -- Canvas rejects a drop rule against a group with
    fewer assignments than the rule drops."""
    for g in spec.GROUPS:
        if not g["rules"]:
            continue
        gid = group_ids.get(g["name"])
        if gid is None or str(gid).startswith("<dry-run"):
            if not api.dry_run:
                continue
        api.write("PUT", f"/courses/{spec.NEW_COURSE_ID}/assignment_groups/{gid}",
                  {"rules": g["rules"]},
                  label=f"apply rule to {g['name']}: {g['rules'].strip()}")


def build_assignments(api, args, group_ids):
    print("\n--- assignments ---")
    existing = _index_by_name(api.get_all(f"/courses/{spec.NEW_COURSE_ID}/assignments"))
    made = {}
    for a in spec.all_assignments():
        gid = group_ids.get(a["group"])
        payload = {"assignment": {
            "name": a["name"],
            "description": a["description"],
            "points_possible": a["points_possible"],
            "due_at": a["due_at"],
            "submission_types": a["submission_types"],
            "published": True,
        }}
        if gid and not str(gid).startswith("<dry-run"):
            payload["assignment"]["assignment_group_id"] = gid
        if a["name"] in existing:
            aid = existing[a["name"]]["id"]
            api.write("PUT", f"/courses/{spec.NEW_COURSE_ID}/assignments/{aid}",
                      payload, label=f"update · due {a['due_at'][:10]}")
            made[a["name"]] = aid
        else:
            res = api.write("POST", f"/courses/{spec.NEW_COURSE_ID}/assignments",
                            payload, label=f"{a['name']} · due {a['due_at'][:10]}")
            made[a["name"]] = res.get("id")
    print(f"  {len(spec.lab_assignments())} labs, "
          f"{len(spec.revision_assignments())} revisions, "
          f"{len(spec.final_assignments())} final-project items")
    return made


def _upload_file(api, course_id, local: Path, folder="course files/slides"):
    """Canvas's 3-step file upload. Returns the new file id (or None in dry run)."""
    if api.dry_run:
        print(f"    DRY-RUN upload {local.relative_to(REPO_ROOT)} -> {folder}")
        return None
    step1 = api._request("POST", f"/courses/{course_id}/files", data={
        "name": local.name, "size": local.stat().st_size,
        "content_type": "application/pdf", "parent_folder_path": folder,
        "on_duplicate": "overwrite",
    })[0]
    upload_url, params = step1["upload_url"], step1["upload_params"]
    boundary = "----canvasmigrate7f3a"
    body = bytearray()
    for k, v in params.items():
        body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n").encode()
    body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; "
             f"filename=\"{local.name}\"\r\nContent-Type: application/pdf\r\n\r\n").encode()
    body += local.read_bytes() + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(upload_url, data=bytes(body), method="POST",
                                 headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(req, timeout=300) as r:
        loc = r.headers.get("Location")
        payload = r.read().decode()
    if loc:
        return api._request("GET", loc)[0].get("id")
    return json.loads(payload).get("id") if payload.strip() else None


def build_modules(api, args, assignment_ids):
    print("\n--- modules ---")
    existing = _index_by_name(api.get_all(f"/courses/{spec.NEW_COURSE_ID}/modules"))
    for m in spec.modules():
        wk = m["week"]
        if m["name"] in existing:
            mid = existing[m["name"]]["id"]
            print(f"  module '{m['name']}' exists (id {mid}) — leaving items alone")
            continue
        res = api.write("POST", f"/courses/{spec.NEW_COURSE_ID}/modules",
                        {"module": {"name": m["name"], "position": wk}},
                        label=f"create module")
        mid = res.get("id")

        slides_file_id = None
        if args.include_slides:
            local = REPO_ROOT / "slides" / f"week-{wk:02d}" / f"week-{wk:02d}.pdf"
            if local.exists():
                slides_file_id = _upload_file(api, spec.NEW_COURSE_ID, local)

        pos = 0
        for item in m["items"]:
            pos += 1
            it = {"title": item["title"], "type": item["type"], "position": pos}
            if item["type"] == "ExternalUrl":
                # Prefer the uploaded PDF over the GitHub link when we have one.
                if slides_file_id and item["title"].startswith("Slides:"):
                    it = {"title": item["title"], "type": "File",
                          "content_id": slides_file_id, "position": pos}
                else:
                    it["external_url"] = item["external_url"]
                    it["new_tab"] = item.get("new_tab", True)
            elif item["type"] == "Assignment":
                aid = assignment_ids.get(item["title"])
                if aid is None or str(aid).startswith("<dry-run"):
                    if not api.dry_run:
                        print(f"      skip item (no assignment id): {item['title']}")
                        continue
                else:
                    it["content_id"] = aid
            if str(mid).startswith("<dry-run"):
                print(f"    DRY-RUN   item {pos:>2}. [{item['type']}] {item['title']}")
                continue
            api.write("POST", f"/courses/{spec.NEW_COURSE_ID}/modules/{mid}/items",
                      {"module_item": it}, label=f"item {pos}: {item['title'][:48]}")
        if not str(mid).startswith("<dry-run"):
            api.write("PUT", f"/courses/{spec.NEW_COURSE_ID}/modules/{mid}",
                      {"module": {"published": True}}, label="publish module")


def build_syllabus(api, args):
    print("\n--- syllabus page ---")
    html = spec.syllabus_html()
    print(f"  {len(html)} chars of HTML "
          f"({len(spec.WEEKS)}-week schedule table, 30/30/40 grading table)")
    api.write("PUT", f"/courses/{spec.NEW_COURSE_ID}",
              {"course": {"syllabus_body": html}}, label="update syllabus body")


def cmd_build(api: Canvas, args):
    only = {s.strip() for s in args.only.split(",")} if args.only else None

    def want(step):
        return only is None or step in only

    group_ids, assignment_ids = {}, {}
    if want("settings"):
        build_settings(api, args)
    if want("groups") or want("assignments") or want("modules"):
        group_ids = build_groups(api, args) if want("groups") else \
            {g["name"]: v["id"] for g, v in
             ((g, _index_by_name(api.get_all(
                 f"/courses/{spec.NEW_COURSE_ID}/assignment_groups")).get(g["name"], {}))
              for g in spec.GROUPS) if v}
    if want("assignments") or want("modules"):
        if want("assignments"):
            assignment_ids = build_assignments(api, args, group_ids)
            if want("groups"):
                apply_group_rules(api, args, group_ids)
        else:
            assignment_ids = {k: v["id"] for k, v in _index_by_name(
                api.get_all(f"/courses/{spec.NEW_COURSE_ID}/assignments")).items()}
    if want("modules"):
        build_modules(api, args, assignment_ids)
    if want("syllabus"):
        build_syllabus(api, args)


# ---------------------------------------------------------------- entry

def cmd_plan(args):
    """Print the full target design. Makes no API calls and needs no token."""
    print(f"\n{'='*72}\nPLAN — what `build --apply` will create in course {spec.NEW_COURSE_ID}"
          f"\n{'='*72}")

    print(f"\nCourse settings")
    print(f"  name            {spec.COURSE_NAME} ({spec.COURSE_CODE}, {spec.TERM})")
    print(f"  meets           {spec.MEETING} · {spec.ROOM}")
    print(f"  term dates      {spec.FIRST_DAY} → {spec.LAST_DAY}")
    print(f"  weighted grades on · home page = Modules")

    print(f"\nAssignment groups")
    total = 0
    for g in spec.GROUPS:
        total += g["group_weight"]
        rule = f"   [{g['rules'].strip()}]" if g["rules"] else ""
        print(f"  {g['name']:<20} {g['group_weight']:>3}%{rule}")
    print(f"  {'TOTAL':<20} {total:>3}%")

    labs, revs, fin = (spec.lab_assignments(), spec.revision_assignments(),
                       spec.final_assignments())
    print(f"\nAssignments ({len(labs)+len(revs)+len(fin)} total)")
    for group, items in (("Notebook Labs", labs), ("Textbook Revisions", revs),
                         ("Final Project", fin)):
        print(f"  {group}:")
        for a in items:
            when = a["due_at"][:16].replace("T", " ")
            print(f"    {when}  {a['points_possible']:>3}pt  {a['name']}")

    print(f"\nModules ({len(spec.modules())})")
    for m in spec.modules():
        print(f"  {m['name']}")
        for i, item in enumerate(m["items"], 1):
            kind = item["type"]
            marker = {"SubHeader": "  ·", "Assignment": "  →"}.get(kind, "  -")
            print(f"  {marker} [{kind}] {item['title']}")

    html = spec.syllabus_html()
    print(f"\nSyllabus page: {len(html)} chars of HTML "
          f"({html.count('<tr')} table rows: weekly rhythm, 30/30/40 grading, "
          f"{len(spec.WEEKS)}-week schedule)")
    if args.write_html:
        Path(args.write_html).write_text(html)
        print(f"  wrote preview -> {args.write_html}")

    print(f"\nContent migration: course {spec.OLD_COURSE_ID} → {spec.NEW_COURSE_ID}, "
          f"{'ENTIRE course' if args.everything else 'files + pages only'}")
    print("\nNothing above has happened yet. Run `build --apply` (with a token) to execute.")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("command", choices=["plan", "inspect", "copy", "build", "all"])
    p.add_argument("--apply", action="store_true",
                   help="actually write to Canvas (default is a dry run)")
    p.add_argument("--host", default="canvas.colorado.edu")
    p.add_argument("--token-file", default=None,
                   help="file containing the API token (else $CANVAS_TOKEN)")
    p.add_argument("--only", default=None,
                   help="build steps to run: settings,groups,assignments,modules,syllabus")
    p.add_argument("--include-slides", action="store_true",
                   help="upload each week's deck PDF and link it in the module")
    p.add_argument("--everything", action="store_true",
                   help="copy: bring over the ENTIRE old course, not just files/pages")
    p.add_argument("--snapshot", default="canvas_snapshot.json",
                   help="where inspect writes its JSON dump")
    p.add_argument("--write-html", default=None,
                   help="plan: also write the generated syllabus HTML to this path")
    args = p.parse_args()

    # `plan` is pure computation — no token, no network.
    if args.command == "plan":
        cmd_plan(args)
        return

    token = None
    if args.token_file:
        token = Path(args.token_file).read_text().strip()
        if token.startswith("{"):
            token = json.loads(token)["key"]
    token = token or os.environ.get("CANVAS_TOKEN", "").strip()
    if not token:
        sys.exit("No token. Set CANVAS_TOKEN or pass --token-file.\n"
                 "Canvas → Account → Settings → + New Access Token.")

    api = Canvas(args.host, token, dry_run=not args.apply)
    mode = "APPLY (writing to Canvas)" if args.apply else "DRY RUN (no writes)"
    print(f"Canvas {args.host} · {mode}")
    print(f"source course {spec.OLD_COURSE_ID} → target course {spec.NEW_COURSE_ID}")

    try:
        if args.command == "inspect":
            cmd_inspect(api, args)
        elif args.command == "copy":
            cmd_copy(api, args)
        elif args.command == "build":
            cmd_build(api, args)
        elif args.command == "all":
            cmd_copy(api, args)
            cmd_build(api, args)
    except CanvasError as e:
        sys.exit(f"\nERROR: {e}")

    if api.dry_run:
        print(f"\nDry run complete — {len(api.writes)} write(s) withheld. "
              f"Re-run with --apply to execute.")
    else:
        print(f"\nDone — {len(api.writes)} write(s) sent.")


if __name__ == "__main__":
    main()
