#!/usr/bin/env python3
"""Before class: flag what a week's deck still lacks.

Two checks, both warnings (see docs/aar/2026-10-16-weeks-06-09.md, P1-1 and P1-2):

- Placeholders. Any image the deck includes that is still the gray box that
  make_stubs.py draws. Placeholders are allowed while a deck is in progress
  (slides/common/AUTHORING.md, Images), but shouldn't reach the projector.
- Standing course-operations items. "Effort over perfection" (a good-faith
  attempt sentence) and "Error flavors" (code designed to break vs. code that
  is broken), which AUTHORING.md calls standing rules. A week with no lab
  submission can skip them; that is why these are warnings.

The third standing item, the Daily-note-questions frame, has its own check:
check_daily_questions.py.

Usage:
    python3 check_deck_readiness.py                  # every week-NN/ folder
    python3 check_deck_readiness.py week-10 11       # specific weeks

Needs Pillow for the placeholder check. Exit status is 0 if nothing is
flagged, 1 otherwise; CI runs it as information only.
"""
import re
import sys
from pathlib import Path

COMMON_DIR = Path(__file__).resolve().parent
SLIDES_DIR = COMMON_DIR.parent

# make_stubs.py fills a placeholder with this gray.
PLACEHOLDER_FILL = (228, 228, 230)
PLACEHOLDER_SHARE = 0.5  # at least half the pixels that exact gray

INCLUDE_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}")
EFFORT_RE = re.compile(r"good[- ]faith", re.IGNORECASE)
FLAVORS_RE = re.compile(r"error flavou?rs?|designed to break", re.IGNORECASE)


def normalize_week_arg(arg):
    """Accept "6", "06", or "week-06" and return the folder name "week-06"."""
    if re.fullmatch(r"\d+", arg):
        return f"week-{int(arg):02d}"
    return arg


def find_week_dirs(args):
    if args:
        return [SLIDES_DIR / normalize_week_arg(a) for a in args]
    return sorted(p for p in SLIDES_DIR.glob("week-*") if p.is_dir())


def deck_text(week_dir):
    """The deck's source, with commented-out lines removed."""
    tex = week_dir / f"{week_dir.name}.tex"
    if not tex.exists():
        return None
    lines = []
    for line in tex.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("%"):
            lines.append(line)
    return "\n".join(lines)


def included_images(week_dir, text):
    """The image files the deck includes, as paths in its img/ folder."""
    found = []
    for name in INCLUDE_RE.findall(text):
        name = name.strip()
        # Instructor frames say slides/week-NN/img/x.png; local ones say img/x.png
        path = week_dir / "img" / Path(name).name
        if path.suffix == "":
            path = path.with_suffix(".png")
        # Only raster images can be placeholders; make_stubs.py draws PNGs
        if path.suffix.lower() not in (".png", ".jpg", ".jpeg"):
            continue
        if path.exists() and path not in found:
            found.append(path)
    return found


def is_placeholder(path):
    try:
        from PIL import Image
    except ImportError:
        sys.exit("check_deck_readiness.py needs Pillow: pip install pillow")
    with Image.open(path) as image:
        small = image.convert("RGB").resize((64, 48))
        if hasattr(small, "get_flattened_data"):
            pixels = small.get_flattened_data()
        else:
            pixels = small.getdata()
        gray = 0
        total = 0
        for pixel in pixels:
            total += 1
            if tuple(pixel) == PLACEHOLDER_FILL:
                gray += 1
    return gray / total >= PLACEHOLDER_SHARE


def check_week(week_dir):
    """Return a list of warnings for one week's deck."""
    text = deck_text(week_dir)
    if text is None:
        return [f"no {week_dir.name}.tex"]
    warnings = []
    for path in included_images(week_dir, text):
        if is_placeholder(path):
            warnings.append(f"PLACEHOLDER: img/{path.name} is still make_stubs.py's gray box")
    if not EFFORT_RE.search(text):
        warnings.append('MISSING: no "good-faith attempt" sentence (Effort over perfection)')
    if not FLAVORS_RE.search(text):
        warnings.append("MISSING: no Error flavors block (designed to break vs. broken)")
    return warnings


def main(args):
    flagged = False
    for week_dir in find_week_dirs(args):
        warnings = check_week(week_dir)
        if warnings:
            flagged = True
            print(f"{week_dir.name}:")
            for warning in warnings:
                print(f"  - {warning}")
        else:
            print(f"{week_dir.name}: OK")
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
