"""Regenerate the week-02 figures from live HTTP responses.

Not mock screenshots: the body text is the verbatim response fetched from the
live URL named in each figure's header strip, so the figure shows the same
information a browser would for a text/plain document.

These files WILL go out of date -- Wikipedia edits its robots.txt, and that
drift is exactly what the Chapter 2 revision exercise asks students to find.
Refetch and re-render with:

    cd slides && python3 common/make_figures.py

Requires network access. Writes into week-02/img/.
"""
import subprocess, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WEEK02 = os.path.join(HERE, "..", "week-02")

def fetch(url, headers=None):
    cmd = ["curl", "-sS", "--fail", url]
    for k, v in (headers or {}).items():
        cmd += ["-H", f"{k}: {v}"]
    try:
        return subprocess.run(cmd, capture_output=True, text=True,
                              check=True, timeout=60).stdout
    except Exception as e:
        sys.exit(f"fetch failed for {url}: {e}")

from PIL import Image, ImageDraw, ImageFont

MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONOB = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

INK, MUTED, RULE, CHROME = (26, 26, 28), (110, 110, 116), (205, 205, 210), (242, 242, 244)


def bar_h(fs):
    return int(fs * 2.6)


def render(path, url, lines, w, h=None, fs=17, highlight=()):
    lh0 = int(fs * 1.52)
    if h is None:
        h = bar_h(fs) + 14 + lh0 * len(lines) + 16
    img = Image.new("RGB", (w, h), (255, 255, 255))
    d = ImageDraw.Draw(img)
    mono, monob = ImageFont.truetype(MONO, fs), ImageFont.truetype(MONOB, fs)
    sans = ImageFont.truetype(SANS, max(11, int(fs * 0.92)))

    # header strip carrying the real URL
    bar = int(fs * 2.6)
    d.rectangle([0, 0, w, bar], fill=CHROME)
    d.line([0, bar, w, bar], fill=RULE, width=2)
    d.rounded_rectangle([12, 8, w - 12, bar - 8], radius=6,
                        fill=(255, 255, 255), outline=RULE, width=1)
    d.text((24, int(bar*0.3)), url, font=sans, fill=INK)

    y, lh = bar + 14, lh0
    for ln in lines:
        if y + lh > h - 14:
            break
        if ln in highlight:
            d.rectangle([8, y - 2, w - 8, y + lh - 4], fill=(238, 238, 240))
            d.text((20, y), ln, font=monob, fill=INK)
        else:
            f = mono
            c = MUTED if ln.strip().startswith("#") else INK
            d.text((26, y), ln, font=f, fill=c)
        y += lh
    d.rectangle([0, 0, w - 1, h - 1], outline=RULE, width=2)
    img.save(path)
    print("wrote", path)


OUT = os.path.join(WEEK02, "img")
UA = "WebDataScience/1.0 (INFO 4617; brian.keegan@colorado.edu)"

# --- 1. Wikipedia robots.txt: the header comment + the generic User-agent block
raw = fetch("https://en.wikipedia.org/robots.txt").lstrip("\ufeff").splitlines()
start = next(i for i, l in enumerate(raw) if l.strip() == "User-agent: *")
block = raw[start:start + 14]
lines = raw[0:6] + [""] + block
hl = [l for l in block if l.startswith(("User-agent:", "Disallow: /trap/"))]
render(f"{OUT}/robots_txt_browser.png",
       "https://en.wikipedia.org/robots.txt", lines, 640, None, 15, hl)

# --- 2. What the server sees: our own User-Agent, echoed back
hdr = fetch("https://httpbin.org/headers", {"User-Agent": UA}).rstrip().splitlines()
lines = ["$ curl -H 'User-Agent: WebDataScience/1.0 (INFO 4617;",
         "        brian.keegan@colorado.edu)' \\",
         "       https://httpbin.org/headers",
         ""] + hdr
hl = [l for l in hdr if "User-Agent" in l]
render(f"{OUT}/user_agent_devtools.png",
       "https://httpbin.org/headers", lines, 800, None, 14, hl)
