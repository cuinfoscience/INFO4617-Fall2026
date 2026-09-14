"""Regenerate the real (non-placeholder) images for slides/week-05.

Run from this directory:  python3 generate_images.py

Produces: protocol_stack.png, url_anatomy.png, request_lifecycle.png,
tcp_handshake.png (all script-drawn diagrams) and pageviews_timeseries.png
(a live chart from the Wikimedia pageviews API, matching the exact call
and date range shown in the Wednesday "Make an API call" slide).

dev_tools_network.png and pr_review.png stay hand-made placeholders --
one is a live browser DevTools panel, the other a real GitHub PR review
comment, and neither is honestly reproducible by a script.
"""
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import requests

# CU Boulder gold + the deck's own tab10-derived accent palette (preamble.tex)
GOLD = "#CFB87C"
BLUE = "#4E79A7"
RED = "#E15759"
GREEN = "#59A14F"
ORANGE = "#F28E2B"
INK = "#1A1A1A"
DPI = 150


def _box(ax, xy, w, h, text, color, fontsize=15, textcolor="black"):
    box = FancyBboxPatch(
        xy, w, h,
        boxstyle="round,pad=0.02,rounding_size=0.02",
        linewidth=1.5, edgecolor=INK, facecolor=color,
    )
    ax.add_patch(box)
    ax.text(xy[0] + w / 2, xy[1] + h / 2, text, ha="center", va="center",
             fontsize=fontsize, color=textcolor, wrap=True)


# ---------------------------------------------------------------- protocol_stack
def protocol_stack():
    fig, ax = plt.subplots(figsize=(1000 / DPI, 900 / DPI), dpi=DPI)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    layers = [
        ("URL", "https://en.wikipedia.org/wiki/Python", GOLD),
        ("HTTP", "GET /wiki/Python HTTP/1.1", BLUE),
        ("DNS", "en.wikipedia.org  →  151.101.130.133", GREEN),
        ("TCP/IP", "151.101.130.133 : 443  (packets)", RED),
    ]
    band_h = 1.9
    gap = 0.35
    top = 9.3
    for i, (name, example, color) in enumerate(layers):
        y = top - i * (band_h + gap) - band_h
        _box(ax, (0.4, y), 9.2, band_h, "", color)
        ax.text(0.9, y + band_h * 0.68, name, fontsize=22, fontweight="bold",
                color="black", va="center")
        ax.text(0.9, y + band_h * 0.28, example, fontsize=13, family="monospace",
                color="black", va="center")
        if i < len(layers) - 1:
            ax.annotate("", xy=(5, y - gap * 0.15), xytext=(5, y + gap * 1.15),
                        arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.5))

    ax.text(5, 9.75, "Four protocols, one layered conversation", ha="center",
            fontsize=15, style="italic")
    fig.tight_layout(pad=0.6)
    fig.savefig("protocol_stack.png", dpi=DPI)
    plt.close(fig)


# ----------------------------------------------------------------- url_anatomy
def url_anatomy():
    fig, ax = plt.subplots(figsize=(1300 / DPI, 480 / DPI), dpi=DPI)
    ax.axis("off")
    fig.canvas.draw()  # need a renderer to measure text extents
    renderer = fig.canvas.get_renderer()

    parts = [
        ("https", "scheme", BLUE),
        ("://", None, None),
        ("api.census.gov", "host", GREEN),
        (":443", "port", ORANGE),
        ("/data/2022/acs/acs5", "path", GOLD),
        ("?get=NAME&for=place:07850", "query", RED),
        ("#results", "fragment", "#9C755F"),
    ]

    y_str = 0.62
    pad_frac = 0.22  # extra horizontal padding inside each colored box, as a fraction of text width
    gap = 0.006  # gap between segments, in axes fraction
    margin = 0.03  # left/right margin to leave inside the axes, as a fraction
    target_w = 1 - 2 * margin

    def measure(fontsize):
        widths = []
        for text, label, color in parts:
            t = ax.text(0, y_str, text, fontsize=fontsize, family="monospace", fontweight="bold")
            bbox = t.get_window_extent(renderer=renderer).transformed(ax.transAxes.inverted())
            widths.append(bbox.width)
            t.remove()
        total = sum(w * (1 + pad_frac if parts[i][2] else 1) for i, w in enumerate(widths)) + gap * (len(parts) - 1)
        return widths, total

    # Measure once, then scale the font to make the whole URL fit the target width exactly.
    fontsize = 20
    widths, total_w = measure(fontsize)
    fontsize *= target_w / total_w
    widths, total_w = measure(fontsize)

    x = (1 - total_w) / 2  # center the whole URL horizontally
    label_targets = []
    for (text, label, color), w in zip(parts, widths):
        seg_w = w * (1 + pad_frac) if color else w
        if color:
            box = FancyBboxPatch((x, y_str - 0.16), seg_w, 0.32,
                                  boxstyle="round,pad=0.006,rounding_size=0.01",
                                  linewidth=1.2, edgecolor=INK, facecolor=color,
                                  alpha=0.85, transform=ax.transAxes, clip_on=False)
            ax.add_patch(box)
            label_targets.append((x + seg_w / 2, label))
        ax.text(x + seg_w / 2, y_str, text, ha="center", va="center",
                fontsize=fontsize, family="monospace", fontweight="bold" if color else "normal",
                transform=ax.transAxes)
        x += seg_w + gap

    for cx, label in label_targets:
        ax.annotate(label, xy=(cx, y_str - 0.17), xytext=(cx, 0.12),
                    xycoords="axes fraction", textcoords="axes fraction",
                    ha="center", fontsize=13,
                    arrowprops=dict(arrowstyle="-", color=INK, lw=1.1, linestyle="dotted"))

    ax.text(0.5, 0.92, "scheme://host:port/path?query#fragment", ha="center",
            fontsize=14, style="italic", color="#555555", transform=ax.transAxes)
    fig.savefig("url_anatomy.png", dpi=DPI)
    plt.close(fig)


# ------------------------------------------------------------ request_lifecycle
def request_lifecycle():
    fig, ax = plt.subplots(figsize=(1000 / DPI, 900 / DPI), dpi=DPI)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    steps = [
        ("DNS resolves the\ndomain to an IP", GREEN),
        ("TCP/IP opens a\nconnection to the server", RED),
        ("HTTP sends a\nrequest to spec", BLUE),
        ("The server returns\na response", ORANGE),
        ("The browser renders\nHTML, CSS \\& JS", GOLD),
    ]
    box_h = 1.35
    gap = 0.42
    top = 9.2
    for i, (text, color) in enumerate(steps):
        y = top - i * (box_h + gap) - box_h
        _box(ax, (1.5, y), 7, box_h, "", color, fontsize=14)
        ax.text(5, y + box_h / 2, text, ha="center", va="center", fontsize=14)
        ax.text(0.9, y + box_h / 2, str(i + 1), ha="center", va="center",
                fontsize=20, fontweight="bold", color=INK)
        if i < len(steps) - 1:
            ax.annotate("", xy=(5, y - gap * 0.1), xytext=(5, y + gap * 1.05),
                        arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.8))

    ax.text(5, 9.75, "URL to rendered page", ha="center", fontsize=15, style="italic")
    fig.tight_layout(pad=0.6)
    fig.savefig("request_lifecycle.png", dpi=DPI)
    plt.close(fig)


# -------------------------------------------------------------- tcp_handshake
def tcp_handshake():
    fig, ax = plt.subplots(figsize=(1100 / DPI, 520 / DPI), dpi=DPI)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 5.2)
    ax.axis("off")

    client_x, server_x = 1.6, 9.4
    top_y, bottom_y = 4.6, 0.7

    _box(ax, (client_x - 0.9, top_y - 0.35), 1.8, 0.7, "Client", BLUE, fontsize=15)
    _box(ax, (server_x - 0.9, top_y - 0.35), 1.8, 0.7, "Server", RED, fontsize=15)
    ax.plot([client_x, client_x], [top_y - 0.35, bottom_y], color="#999999", lw=1, zorder=0)
    ax.plot([server_x, server_x], [top_y - 0.35, bottom_y], color="#999999", lw=1, zorder=0)

    arrows = [
        ("SYN", client_x, server_x, 3.55, GREEN),
        ("SYN-ACK", server_x, client_x, 2.55, ORANGE),
        ("ACK", client_x, server_x, 1.55, GREEN),
    ]
    for label, x0, x1, y, color in arrows:
        ax.annotate("", xy=(x1, y), xytext=(x0, y),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=2.2))
        ax.text((x0 + x1) / 2, y + 0.18, label, ha="center", fontsize=13,
                fontweight="bold", color=color)

    ax.text(5.5, 0.15, "Three packets, zero bytes of your actual request, yet",
            ha="center", fontsize=11, style="italic", color="#555555")
    fig.tight_layout(pad=0.5)
    fig.savefig("tcp_handshake.png", dpi=DPI)
    plt.close(fig)


# --------------------------------------------------------- pageviews_timeseries
def pageviews_timeseries():
    url = (
        "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article"
        "/en.wikipedia/all-access/all-agents/"
        "University_of_Colorado_Boulder/daily/20260101/20260131"
    )
    headers = {"User-Agent": "INFO4617-course-deck/1.0 (contact: accounts@brianckeegan.com)"}
    for attempt in range(4):
        response = requests.get(url, headers=headers, timeout=20)
        if response.status_code == 200 and response.content:
            try:
                data = response.json()
                break
            except ValueError:
                pass
        time.sleep(2 * (attempt + 1))
    else:
        raise RuntimeError(f"Wikimedia pageviews API did not return usable JSON after retries (last status {response.status_code})")

    dates = [item["timestamp"][:8] for item in data["items"]]
    views = [item["views"] for item in data["items"]]
    labels = [f"{d[4:6]}/{d[6:8]}" for d in dates]

    fig, ax = plt.subplots(figsize=(1100 / DPI, 560 / DPI), dpi=DPI)
    ax.plot(range(len(dates)), views, marker="o", color=BLUE, linewidth=2)
    ax.fill_between(range(len(dates)), views, alpha=0.12, color=BLUE)
    ax.set_title("Daily Pageviews: University_of_Colorado_Boulder (Jan 2026)")
    ax.set_ylabel("Views")
    ax.set_xticks(range(0, len(dates), 4))
    ax.set_xticklabels([labels[i] for i in range(0, len(dates), 4)], rotation=0)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig("pageviews_timeseries.png", dpi=DPI)
    plt.close(fig)


if __name__ == "__main__":
    protocol_stack()
    url_anatomy()
    request_lifecycle()
    tcp_handshake()
    pageviews_timeseries()
    print("Generated: protocol_stack.png, url_anatomy.png, request_lifecycle.png, "
          "tcp_handshake.png, pageviews_timeseries.png")
