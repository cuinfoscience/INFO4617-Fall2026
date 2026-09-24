#!/usr/bin/env python3
"""Generate placeholder ("stub") images for a week's slide deck.

Each week directory contains ``img/stubs.tsv`` describing the images the deck
references. This script renders a labeled gray placeholder PNG for each entry
that does not exist yet, so the deck compiles, and keeps a table of the entries
in ``img/IMAGES.md``.

IMAGES.md is also where people record where each real image came from, so the
script rewrites only the table between these two lines:

    <!-- stubs:begin ... -->
    <!-- stubs:end -->

It never touches anything outside them. A file with no markers is left alone,
unless every line in it is one this script used to write (the old format, a
file with no notes in it), which is regenerated as before. A missing file is
created with the markers.

Usage:
    python make_stubs.py [--force] [--check] <week_dir> [<week_dir> ...]

    --force   redraw placeholders even where an image already exists
    --check   change nothing; report what would change and exit 1 if anything would

stubs.tsv format (tab-separated, '#' comments and blank lines ignored):
    filename <TAB> WIDTHxHEIGHT <TAB> caption/description
e.g.
    dev_tools_network.png    1200x800    Screenshot: browser Network tab on a live page load
"""
import sys
import os
import re
import textwrap
from PIL import Image, ImageDraw, ImageFont

BEGIN = ("<!-- stubs:begin: generated from stubs.tsv by slides/common/make_stubs.py;"
         " edits between these markers are replaced -->")
END = "<!-- stubs:end -->"

# What this script wrote before it kept notes. A file made only of these lines
# holds nothing a person wrote, so regenerating it loses nothing.
LEGACY_HEAD = "# Image placeholders for `"
LEGACY_INTRO = ("These are auto-generated gray **placeholders** so the deck "
                "compiles. Replace each with the real asset described below "
                "(keep the same filename), then rebuild.")
TABLE_HEAD = ("| File | Size | Should show |", "|---|---|---|")
TABLE_ROW = re.compile(r"^\| `[^`]+` \| \d+x\d+ \| .* \|$")

NEW_FILE_INTRO = """\
`make_stubs.py` draws a gray placeholder for every image listed in `stubs.tsv`
that does not exist yet, so the deck compiles. Replace a placeholder with the
real image under the same file name, then write below where it came from, how
it was made, and the date. The script rewrites only the table between the two
markers.
"""


def _font(size):
    for path in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()


def make_stub(path, w, h, caption, force=False, check=False):
    # Never clobber a real asset. Once a placeholder has been replaced with an
    # actual screenshot or figure, a later `make` would otherwise silently
    # overwrite it with a gray box again -- and the loss is invisible until
    # someone opens the PDF. Pass --force to regenerate deliberately.
    if os.path.exists(path) and not force:
        return False
    if check:
        return True
    img = Image.new("RGB", (w, h), (228, 228, 230))
    d = ImageDraw.Draw(img)
    # border
    d.rectangle([2, 2, w - 3, h - 3], outline=(150, 150, 155), width=3)
    # diagonal guides
    d.line([0, 0, w, h], fill=(205, 205, 210), width=2)
    d.line([0, h, w, 0], fill=(205, 205, 210), width=2)
    # label plate
    tag = "PLACEHOLDER"
    tf = _font(max(16, h // 14))
    cf = _font(max(13, h // 22))
    tb = d.textbbox((0, 0), tag, font=tf)
    d.text(((w - (tb[2] - tb[0])) / 2, h * 0.30), tag, fill=(120, 90, 20), font=tf)
    # wrapped caption
    avg = max(1, cf.getbbox("n")[2] - cf.getbbox("n")[0])
    wrap_at = max(12, int((w * 0.85) / avg))
    lines = textwrap.wrap(caption, width=wrap_at) or [""]
    y = h * 0.46
    for line in lines[:6]:
        lb = d.textbbox((0, 0), line, font=cf)
        d.text(((w - (lb[2] - lb[0])) / 2, y), line, fill=(70, 70, 75), font=cf)
        y += (cf.getbbox("Ag")[3] - cf.getbbox("Ag")[1]) + 6
    # filename footer
    ff = _font(max(11, h // 30))
    fn = os.path.basename(path)
    fb = d.textbbox((0, 0), fn, font=ff)
    d.text(((w - (fb[2] - fb[0])) / 2, h * 0.9), fn, fill=(140, 140, 145), font=ff)
    img.save(path)
    return True


def table(rows):
    lines = list(TABLE_HEAD) + [f"| `{f}` | {s} | {c} |" for f, s, c in rows]
    return "\n".join(lines) + "\n"


def is_legacy(text):
    """True if every line of text is one the old version of this script wrote."""
    if not text.startswith(LEGACY_HEAD):
        return False
    return all(not line or line.startswith(LEGACY_HEAD) or line == LEGACY_INTRO
               or line in TABLE_HEAD or TABLE_ROW.match(line)
               for line in text.splitlines())


def images_md(path, week_name, rows):
    """Return (new text, what happened) for IMAGES.md; new text is None to leave it."""
    block = f"{BEGIN}\n{table(rows)}{END}\n"
    if not os.path.exists(path):
        text = (f"# Images for `{week_name}`\n\n{NEW_FILE_INTRO}\n"
                f"## Listed in `stubs.tsv`\n\n{block}")
        return text, "created IMAGES.md"
    with open(path) as f:
        old = f.read()
    lines = old.splitlines(keepends=True)
    starts = [i for i, l in enumerate(lines) if l.startswith("<!-- stubs:begin")]
    ends = [i for i, l in enumerate(lines) if l.startswith(END)]
    if len(starts) == 1 and len(ends) == 1 and starts[0] < ends[0]:
        new = "".join(lines[:starts[0]]) + block + "".join(lines[ends[0] + 1:])
        return (None, "IMAGES.md table unchanged") if new == old else (new, "updated the IMAGES.md table")
    if starts or ends:
        return None, "IMAGES.md has unmatched stubs markers; not touching it"
    if is_legacy(old):
        new = (f"# Image placeholders for `{week_name}`\n\n{LEGACY_INTRO}\n\n"
               + table(rows))
        return (None, "IMAGES.md unchanged") if new == old else (new, "regenerated IMAGES.md")
    return None, ("IMAGES.md has hand-written notes and no stubs markers; not touching it. "
                  "To keep its table current, put these two lines where the table belongs:\n"
                  f"      {BEGIN}\n      {END}")


def process(week_dir, force=False, check=False):
    """Returns True if anything changed (or, with check, would change)."""
    # Resolve before naming: the Makefile invokes this as `make_stubs.py .`
    # from inside the week folder, so basename() on the raw argument would
    # label everything "." instead of "week-NN".
    week_name = os.path.basename(os.path.abspath(week_dir))
    img_dir = os.path.join(week_dir, "img")
    manifest = os.path.join(img_dir, "stubs.tsv")
    if not os.path.exists(manifest):
        print(f"  (no {manifest}; skipping)")
        return False
    if not check:
        os.makedirs(img_dir, exist_ok=True)
    rows = []
    made = []
    with open(manifest) as f:
        for raw in f:
            line = raw.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 3:
                print(f"  skip malformed line: {line!r}")
                continue
            fname, size, caption = parts[0].strip(), parts[1].strip(), parts[2].strip()
            try:
                w, h = (int(x) for x in size.lower().split("x"))
            except ValueError:
                print(f"  skip bad size {size!r} for {fname}")
                continue
            if make_stub(os.path.join(img_dir, fname), w, h, caption, force, check):
                made.append(fname)
            rows.append((fname, f"{w}x{h}", caption))
    md_path = os.path.join(img_dir, "IMAGES.md")
    new_md, md_note = images_md(md_path, week_name, rows)
    if new_md is not None and not check:
        with open(md_path, "w") as md:
            md.write(new_md)
    verb = "would draw" if check else "drew"
    stubs = f"{verb} {len(made)} placeholder(s)" + (f" ({', '.join(made)})" if made else "")
    if check and new_md is not None:
        md_note = "would have " + md_note
    print(f"  {week_name}: {stubs}; {md_note}")
    return bool(made) or new_md is not None


if __name__ == "__main__":
    args = sys.argv[1:]
    force = "--force" in args
    check = "--check" in args
    targets = [a for a in args if a not in ("--force", "--check")] or ["."]
    changed = [process(t, force, check) for t in targets]
    if check and any(changed):
        sys.exit(1)
