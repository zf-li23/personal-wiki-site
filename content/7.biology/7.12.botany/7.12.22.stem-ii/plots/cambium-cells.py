# Cells and divisions of the vascular cambium. (A) Tangential view of the cambium: long, pointed fusiform
# initials (staggered) and small clusters of near-isodiametric ray initials. (B) One radial file in
# transverse section: the initial (dark yellow) divides periclinally again and again; inner derivatives
# (xylem mother cells) differentiate into secondary xylem, outer ones into secondary phloem; far more cells
# are produced inwards. (C) Multiplicative divisions of fusiform initials: radial anticlinal, lateral
# anticlinal, and pseudotransverse division followed by intrusive growth of the tips. (D) Origin of ray
# initials from a fusiform initial (cut off at the end or from the side).
import numpy as np
from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon, Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(33.0, 13.0)
rng = np.random.default_rng(4)


def fusiform(x, y, L, w, tok="cambium", z=5, lw=0.8):
    pts = [(x, y - L / 2), (x + w / 2, y - L / 4), (x + w / 2, y + L / 4), (x, y + L / 2), (x - w / 2, y + L / 4), (x - w / 2, y - L / 4)]
    return ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=lw, zorder=z, joinstyle="round"))


# ---- A
bio.panel(ax, "A", (0.2, 12.8))
bio.label(ax, (0.85, 12.77), "Cambium, tangential view", size="title", ha="left", va="top")
W = 0.55
frame = Rectangle((0.6, 0.6), 6.8, 11.4, transform=ax.transData)
for col in range(12):
    x = 0.9 + col * W
    off = (col % 2) * 1.6
    y = 0.6 - off
    while y < 12.0:
        L = rng.uniform(2.6, 3.6)
        if -1.0 < y + L / 2 < 13.0:
            fusiform(x, y + L / 2, L, W * 0.95).set_clip_path(frame)
        y += L * 0.98
for (cx, cy, n) in ((2.3, 7.5, 3), (4.5, 4.0, 4), (5.6, 9.0, 2), (3.4, 2.4, 3)):
    for k in range(n):
        ax.add_patch(Rectangle((cx - 0.22, cy + k * 0.36 - n * 0.18), 0.44, 0.34, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"),
                               lw=0.6, zorder=6))
ax.add_patch(Rectangle((0.6, 0.6), 6.8, 11.4, facecolor="none", edgecolor=P.muted(), lw=0.6, zorder=7))
bio.callout(ax, (1.45, 6.0), (0.8, 0.2), "Fusiform initial", size="small")
bio.callout(ax, (4.5, 4.2), (5.2, 0.2), "Ray initials", size="small")

# ---- B: radial file
bio.panel(ax, "B", (8.2, 12.8))
bio.label(ax, (8.85, 12.77), "Periclinal divisions", size="title", ha="left", va="top")
y = 6.4
cells = ([("xylem", 0.7)] * 3 + [("channel", 0.5)] * 3 + [("cambium", 0.32)] + [("phloem", 0.42)] * 2 + [("lipid_head", 0.6)] * 2)
x = 8.8
for tok, wdt in cells:
    big = tok == "xylem"
    h = 1.4 if big else 1.0
    ax.add_patch(FancyBboxPatch((x, y - h / 2), wdt - 0.05, h, boxstyle="round,pad=0,rounding_size=0.08",
                                facecolor=P.fill(tok) if tok != "cambium" else P.edge("cambium"), edgecolor=P.edge(tok if tok != "cambium" else "highlight"),
                                lw=0.8, zorder=5))
    x += wdt
xs = np.cumsum([0] + [w for _, w in cells]) + 8.8
bio.label(ax, ((xs[0] + xs[3]) / 2, 8.0), "secondary xylem", size="small")
bio.label(ax, ((xs[3] + xs[6]) / 2 - 0.4, 4.9), "xylem mother cells", size="tiny", color=P.muted())
bio.label(ax, ((xs[6] + xs[7]) / 2, 8.0), "initial", size="small")
bio.label(ax, ((xs[7] + xs[9]) / 2 + 0.6, 4.3), "phloem mother cells", size="tiny", color=P.muted())
bio.label(ax, ((xs[9] + xs[11]) / 2, 8.0), "secondary phloem", size="small")
bio.arrow(ax, (xs[6] - 0.1, 9.0), (xs[0] + 0.3, 9.0), kind="process", color=P.edge("xylem"))
bio.arrow(ax, (xs[7] + 0.1, 9.0), (xs[11] - 0.1, 9.0), kind="process", color=P.edge("phloem"))
bio.label(ax, ((xs[0] + xs[6]) / 2, 9.5), "inwards (towards pith)", size="tiny", color=P.muted())
bio.label(ax, ((xs[7] + xs[11]) / 2, 9.5), "outwards", size="tiny", color=P.muted())

# ---- C: multiplicative divisions
bio.panel(ax, "C", (8.2, 3.9))
bio.label(ax, (8.85, 3.87), "Multiplicative divisions", size="title", ha="left", va="top")
L, w0 = 2.6, 0.7
x = 9.4
for name in ("radial", "lateral", "pseudotransverse"):
    fusiform(x, 1.6, L, w0)
    if name == "radial":
        ax.plot([x, x], [0.3, 2.9], color=P.edge("negative"), lw=1.2, zorder=6)
    elif name == "lateral":
        ax.plot([x + 0.1, x + 0.12, x + 0.35], [0.9, 2.1, 2.3], color=P.edge("negative"), lw=1.2, zorder=6)
    else:
        ax.plot([x - 0.35, x + 0.35], [1.35, 1.85], color=P.edge("negative"), lw=1.2, zorder=6)
        bio.arrow(ax, (x + 0.6, 1.6), (x + 1.2, 1.6), kind="process", color=P.muted())
        fusiform(x + 1.85, 1.95, L * 0.95, w0 * 0.6)
        fusiform(x + 2.25, 1.25, L * 0.95, w0 * 0.6)
    bio.label(ax, (x, 0.0) if name != "pseudotransverse" else (x + 1.0, 0.0), name, size="tiny", color=P.muted())
    x += 2.0

# ---- D: origin of ray initials
bio.panel(ax, "D", (24.2, 12.8))
bio.label(ax, (24.85, 12.77), "Origin of ray initials", size="title", ha="left", va="top")
for k, (x, mode) in enumerate(((26.2, "end"), (29.4, "side"))):
    fusiform(x, 6.6, 7.0, 1.2)
    if mode == "end":
        ax.plot([x - 0.45, x + 0.45], [9.0, 9.0], color=P.edge("negative"), lw=1.2, zorder=6)
        ax.add_patch(Rectangle((x - 0.3, 9.1), 0.6, 0.5, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=0.8, zorder=6))
        bio.label(ax, (x, 2.3), "cut off at one end", size="tiny", color=P.muted())
    else:
        ax.add_patch(Rectangle((x - 0.3, 6.0), 0.6, 1.2, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=0.8, zorder=6))
        bio.label(ax, (x, 2.3), "cut off from the side", size="tiny", color=P.muted())
bio.callout(ax, (29.6, 6.6), (31.4, 10.6), "Ray initial", size="small")
