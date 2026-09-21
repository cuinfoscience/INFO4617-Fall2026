#!/usr/bin/env python3
"""Flag missing, blank, or duplicated "Daily note questions" frames.

Run this before each class to catch the one piece of course-operations
furniture that can't be written ahead of time (it depends on the real
questions students submitted) -- see slides/common/AUTHORING.md.

Usage:
    python3 check_daily_questions.py                 # check every week-NN/ folder
    python3 check_daily_questions.py week-06 week-07  # check specific weeks
    python3 check_daily_questions.py 6 7              # short form also works

Exit status is 0 if nothing needs attention, 1 if any week is flagged.
"""
import re
import sys
from pathlib import Path

COMMON_DIR = Path(__file__).resolve().parent
SLIDES_DIR = COMMON_DIR.parent

FRAME_RE = re.compile(
    r"\\begin\{frame\}(?:\[[^\]]*\])?\{([^}]*)\}(.*?)\\end\{frame\}",
    re.DOTALL,
)
TITLE_RE = re.compile(r"daily\s+note\s+questions", re.IGNORECASE)
ITEM_RE = re.compile(r"\\item\s+((?:\\textbf\{[^}]*\}\s*)+)-{2,3}\s*(.+)")
TEXTBF_RE = re.compile(r"\\textbf\{([^}]*)\}")

# A week whose question set overlaps an earlier week's by at least this much
# (by normalized question text) is flagged as likely copy-pasted rather than
# freshly answered.
DUPLICATE_OVERLAP_THRESHOLD = 0.6


def normalize_week_arg(arg):
    """Accept "6", "06", or "week-06" and return the folder name "week-06"."""
    if re.fullmatch(r"week-\d+", arg):
        return arg
    if re.fullmatch(r"\d+", arg):
        return f"week-{int(arg):02d}"
    return arg


def find_week_dirs(args):
    if args:
        return [SLIDES_DIR / normalize_week_arg(a) for a in args]
    return sorted(p for p in SLIDES_DIR.glob("week-*") if p.is_dir())


def extract_daily_frames(tex_text):
    """Return [(title, body), ...] for frames titled "Daily note questions"
    (optionally with a ", part N" suffix, as week-02 uses for two frames)."""
    frames = []
    for m in FRAME_RE.finditer(tex_text):
        title, body = m.group(1), m.group(2)
        if TITLE_RE.search(title):
            frames.append((title.strip(), body))
    return frames


def extract_qa_pairs(body):
    pairs = []
    for line in body.splitlines():
        m = ITEM_RE.search(line)
        if m:
            question = " ".join(TEXTBF_RE.findall(m.group(1))).strip()
            pairs.append((question, m.group(2).strip()))
    return pairs


def normalize(text):
    return re.sub(r"\s+", " ", text).strip().lower()


def check_week(week_dir):
    """Return (findings, qa_pairs) for one week folder."""
    tex_files = sorted(week_dir.glob("week-*.tex"))
    if not tex_files:
        return [f"no week-NN.tex file found in {week_dir}"], []

    tex_text = tex_files[0].read_text(encoding="utf-8")
    frames = extract_daily_frames(tex_text)

    if not frames:
        return ['MISSING: no "Daily note questions" frame found'], []

    findings = []
    all_pairs = []
    for title, body in frames:
        pairs = extract_qa_pairs(body)
        all_pairs.extend(pairs)
        if not pairs:
            findings.append(f'BLANK: frame "{title}" has no Question/Answer lines')

        seen = {}
        for q, a in pairs:
            key = normalize(q)
            if key in seen:
                findings.append(
                    f'DUPLICATE (within frame): "{q}" appears more than once in "{title}"'
                )
            seen[key] = True

    return findings, all_pairs


def check_cross_week_duplicates(per_week_pairs, per_week_findings):
    """Flag a week whose question set looks copy-pasted from an earlier week."""
    weeks_seen_so_far = []
    for week_name in sorted(per_week_pairs):
        pairs = per_week_pairs[week_name]
        if pairs:
            this_set = frozenset(normalize(q) for q, _ in pairs)
            for other_name, other_set in weeks_seen_so_far:
                if not other_set:
                    continue
                overlap = this_set & other_set
                if overlap and len(overlap) / len(this_set) >= DUPLICATE_OVERLAP_THRESHOLD:
                    per_week_findings[week_name].append(
                        f"DUPLICATE (cross-week): {len(overlap)}/{len(this_set)} "
                        f"questions match {other_name} verbatim -- looks copy-pasted "
                        f"rather than answered fresh"
                    )
        else:
            this_set = frozenset()
        weeks_seen_so_far.append((week_name, this_set))


def main():
    args = sys.argv[1:]
    week_dirs = find_week_dirs(args)

    per_week_findings = {}
    per_week_pairs = {}
    for week_dir in week_dirs:
        if not week_dir.exists():
            per_week_findings[week_dir.name] = [f"no such folder: {week_dir}"]
            per_week_pairs[week_dir.name] = []
            continue
        findings, pairs = check_week(week_dir)
        per_week_findings[week_dir.name] = findings
        per_week_pairs[week_dir.name] = pairs

    check_cross_week_duplicates(per_week_pairs, per_week_findings)

    any_flagged = False
    for week_name in sorted(per_week_findings):
        findings = per_week_findings[week_name]
        if findings:
            any_flagged = True
            print(f"{week_name}:")
            for finding in findings:
                print(f"  - {finding}")
        else:
            n = len(per_week_pairs.get(week_name, []))
            print(f"{week_name}: OK ({n} question{'s' if n != 1 else ''})")

    sys.exit(1 if any_flagged else 0)


if __name__ == "__main__":
    main()
