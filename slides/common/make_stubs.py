#!/usr/bin/env python3
"""Generate placeholder ("stub") images for a week's slide deck.

Each week directory contains ``img/stubs.tsv`` describing the images the deck
references. This script renders a labeled gray placeholder PNG for each entry so
the deck compiles, and writes ``img/IMAGES.md`` noting what each stub should be
replaced with.

Usage:
    python make_stubs.py <week_dir> [<week_dir> ...]

stubs.tsv format (tab-separated, '#' comments and blank lines ignored):
    filename <TAB> WIDTHxHEIGHT <TAB> caption/description
e.g.
    dev_tools_network.png    1200x800    Screenshot: browser Network tab on a live page load
"""
import sys
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont


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


def make_stub(path, w, h, caption):
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


def process(week_dir):
    # Resolve before naming: the Makefile invokes this as `make_stubs.py .`
    # from inside the week folder, so basename() on the raw argument would
    # label everything "." instead of "week-NN".
    week_name = os.path.basename(os.path.abspath(week_dir))
    img_dir = os.path.join(week_dir, "img")
    manifest = os.path.join(img_dir, "stubs.tsv")
    if not os.path.exists(manifest):
        print(f"  (no {manifest}; skipping)")
        return
    os.makedirs(img_dir, exist_ok=True)
    rows = []
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
            make_stub(os.path.join(img_dir, fname), w, h, caption)
            rows.append((fname, f"{w}x{h}", caption))
    # write IMAGES.md
    with open(os.path.join(img_dir, "IMAGES.md"), "w") as md:
        md.write(f"# Image placeholders for `{week_name}`\n\n")
        md.write("These are auto-generated gray **placeholders** so the deck "
                 "compiles. Replace each with the real asset described below "
                 "(keep the same filename), then rebuild.\n\n")
        md.write("| File | Size | Should show |\n|---|---|---|\n")
        for fname, size, caption in rows:
            md.write(f"| `{fname}` | {size} | {caption} |\n")
    print(f"  {week_name}: generated {len(rows)} stub(s)")


if __name__ == "__main__":
    targets = sys.argv[1:] or ["."]
    for t in targets:
        process(t)
