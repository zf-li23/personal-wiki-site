# Long-, intermediate- and short-germ development (schematic, not to scale). Top row: the germ anlage on the
# ventral side of the blastoderm egg, coloured by the body regions it already contains (head, thorax, abdomen)
# and the posterior growth zone. Bottom row: the segmented germ band; in short- and intermediate-germ embryos
# the segments posterior to the anlage are added one by one from the growth zone (arrows).
import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, Polygon

P = bio.P
fig, ax = bio.canvas(27, 12.5)
REG = {"head": "enzyme", "thorax": "positive", "abdomen": "channel", "growth": "highlight"}


def egg(cx, cy, w=7.0, h=2.6):
    ax.add_patch(Ellipse((cx, cy), w, h, facecolor=P.light("ovule"), edgecolor=P.edge("ovule"), lw=1.0, zorder=3))


def band(cx, cy, parts, w=7.0, h=2.6, start=-0.45, thick=0.5):
    """parts: list of (fraction of egg length, region); drawn along the ventral (lower) side, anterior left."""
    a = -w / 2 * 0.88
    x = cx + a + (start + 0.5) * w * 0.0
    pos = cx - w / 2 * 0.86
    for frac, reg, nseg in parts:
        L = frac * w * 0.86
        for k in range(nseg):
            x0 = pos + k * L / nseg
            x1 = pos + (k + 1) * L / nseg - 0.04
            xs = np.linspace(x0, x1, 8)
            yb = cy - (h / 2) * np.sqrt(np.clip(1 - ((xs - cx) / (w / 2)) ** 2, 0, 1)) * 0.92
            pts = list(zip(xs, yb)) + list(zip(xs[::-1], yb[::-1] + thick))
            ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(REG[reg]), edgecolor=P.edge(REG[reg]), lw=0.7,
                                 zorder=5))
        pos += L
    return pos


cols = [(4.6, "A  Long germ (fruit fly)"), (13.5, "B  Intermediate germ (flour beetle)"), (22.4, "C  Short germ (grasshopper)")]
anl = [
    [(0.18, "head", 3), (0.14, "thorax", 3), (0.62, "abdomen", 8)],
    [(0.18, "head", 3), (0.14, "thorax", 3), (0.08, "growth", 1)],
    [(0.16, "head", 2), (0.08, "growth", 1)],
]
full = [
    [(0.18, "head", 3), (0.14, "thorax", 3), (0.62, "abdomen", 8)],
    [(0.18, "head", 3), (0.14, "thorax", 3), (0.5, "abdomen", 8), (0.06, "growth", 1)],
    [(0.18, "head", 3), (0.14, "thorax", 3), (0.5, "abdomen", 8), (0.06, "growth", 1)],
]
for (cx, title), a, f in zip(cols, anl, full):
    bio.label(ax, (cx, 11.6), title, size="small", bold=True)
    egg(cx, 8.9)
    band(cx, 8.9, a)
    egg(cx, 3.9)
    end = band(cx, 3.9, f)
    if "Long" not in title:
        bio.arrow(ax, (end - 2.2, 2.25), (end - 0.2, 2.25), kind="process", color=P.edge("highlight"))
        bio.label(ax, (end - 1.2, 1.85), "segments added", size="tiny", color=P.edge("highlight"))
    else:
        bio.label(ax, (cx, 1.85), "all segments specified together", size="tiny", color=P.muted())
bio.label(ax, (0.3, 10.4), "blastoderm:", size="tiny", ha="left", color=P.muted())
bio.label(ax, (0.3, 5.4), "germ band:", size="tiny", ha="left", color=P.muted())
x = 6.0
for name, reg in (("head", "head"), ("thorax", "thorax"), ("abdomen", "abdomen"), ("growth zone", "growth")):
    ax.add_patch(Ellipse((x, 0.6), 0.5, 0.32, facecolor=P.fill(REG[reg]), edgecolor=P.edge(REG[reg]), lw=0.7))
    bio.label(ax, (x + 0.4, 0.6), name, size="tiny", ha="left")
    x += 3.6
bio.label(ax, (22.0, 0.6), "anterior left, ventral down", size="tiny", color=P.muted())
