"""Identification of the genera of Pinaceae by the seed cone and the leaves (schematic). Top row:
subfamily Abietoideae; bottom row: Pinoideae. For each genus: cone position (erect or pendent on the
twig), whether the cone scales fall from the axis at maturity, and the leaf arrangement (single and spiral
on long shoots; clustered on short shoots; in fascicles of two to five with a sheath in Pinus)."""
import numpy as np
from matplotlib.patches import Ellipse, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 15)


def cone(cx, cy, w, h, up=True, shatter=False, exserted=False, woody=False):
    """A seed cone as an ellipse of imbricate scales; ``up`` erect, else pendent."""
    rows = 6
    for r in range(rows):
        f = (r + 0.5) / rows
        yy = cy - h / 2 + f * h if up else cy + h / 2 - f * h
        ww = w * np.sqrt(max(0.05, 1 - (2 * f - 1) ** 2)) * 1.05
        for k in range(3):
            xx = cx + (k - 1) * ww / 3
            tok = "bone" if woody else "animal"
            ax.add_patch(Ellipse((xx, yy), ww / 2.6, h / rows * 1.35, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.6,
                                 zorder=6 + r * (1 if up else -1) * 0.01 + 6))
            if woody:
                ax.plot([xx], [yy - 0.03], marker="o", ms=2, color=P.edge(tok), zorder=14)
            if exserted:
                sgn = -1 if up else 1
                ax.plot([xx, xx - 0.06, xx, xx + 0.06], [yy, yy - sgn * 0.32, yy - sgn * 0.42, yy - sgn * 0.32], color=P.edge("bract"),
                        lw=0.9, zorder=15)
    if shatter:
        for dx, dy, a in ((w * 0.75, -h * 0.15, 30), (w * 0.95, -h * 0.45, -20)):
            ax.add_patch(Ellipse((cx + dx, cy + dy), w / 2.6, h / rows * 1.3, angle=a, facecolor=P.light("animal"),
                                 edgecolor=P.edge("animal"), lw=0.6, ls=(0, (2, 1)), zorder=7))
        ax.plot([cx, cx], [cy - h / 2 - 0.1, cy + h / 2 + 0.25], color=P.edge("bone"), lw=1.6, zorder=13)


def twig(x0, y0, x1, y1):
    ax.plot([x0, x1], [y0, y1], color=P.edge("bone"), lw=2.2, solid_capstyle="round", zorder=4)


def leaves(x, y, kind):
    """Leaf glyph below the cone: single, cluster, fascicle-n."""
    if kind == "single":
        twig(x - 1.0, y, x + 1.0, y)
        for k in range(7):
            xx = x - 0.9 + 0.3 * k
            for sgn in (1, -1):
                ax.plot([xx, xx + 0.12], [y, y + sgn * 0.45], color=P.edge("plant"), lw=1.6, solid_capstyle="round", zorder=5)
    elif kind == "cluster":
        twig(x - 1.0, y - 0.1, x + 1.0, y - 0.1)
        for cxx in (x - 0.5, x + 0.5):
            ax.plot([cxx, cxx], [y - 0.1, y + 0.1], color=P.edge("bone"), lw=2.4, zorder=5)
            for a in np.linspace(20, 160, 9):
                r = np.radians(a)
                ax.plot([cxx, cxx + 0.5 * np.cos(r)], [y + 0.1, y + 0.1 + 0.5 * np.sin(r)], color=P.edge("plant"), lw=1.0, zorder=5)
    else:
        n = int(kind)
        twig(x - 1.0, y - 0.2, x + 1.0, y - 0.2)
        for cxx in (x - 0.45, x + 0.45):
            ax.add_patch(Polygon([(cxx - 0.07, y - 0.2), (cxx + 0.07, y - 0.2), (cxx + 0.05, y + 0.12), (cxx - 0.05, y + 0.12)],
                                 closed=True, facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=0.5, zorder=6))
            for a in np.linspace(75, 105, n) if n > 1 else [90]:
                r = np.radians(a)
                ax.plot([cxx, cxx + 0.95 * np.cos(r) * 2.2], [y + 0.1, y + 0.1 + 0.95 * np.sin(r)], color=P.edge("plant"), lw=1.0,
                        zorder=5)


G = [  # genus, up, shatter, leaf kind, lines, special
    ("Cedrus", True, True, "cluster", ["erect barrel cone, 2nd year", "scales fall", "needles on short shoots, evergreen"], {}),
    ("Abies", True, True, "single", ["erect cone, 1st year", "scales and seeds fall", "flat needles, round leaf scars"], {}),
    ("Keteleeria", True, False, "single", ["erect cone, 1st year", "scales persistent", "flat needles, single"], {}),
    ("Pseudolarix", True, True, "cluster", ["erect cone, 1st year", "scales fall", "soft needles in discs; deciduous"], {}),
    ("Tsuga", False, False, "single", ["small pendent cone", "scales persistent", "flat needles, short petiole"], {}),
    ("Pseudotsuga", False, False, "single", ["pendent cone", "3-lobed bracts exserted", "flat needles, single"], dict(exserted=True)),
    ("Larix", True, False, "cluster", ["small erect cone, 1st year", "scales persistent", "needles on short shoots; deciduous"], {}),
    ("Cathaya", False, False, "single", ["axillary cone, erect then pendent", "scales persistent", "flat needles, crowded at tip"], {}),
    ("Picea", False, False, "single", ["pendent cone, 1st year", "scales persistent", "4-angled needles on pegs"], {}),
    ("Pinus", False, False, "3", ["woody cone, 2nd (3rd) year", "apophysis and umbo", "needles in fascicles of 2, 3, 5"],
     dict(woody=True)),
]
for i, (g, up, sh, lk, lines, kw) in enumerate(G):
    col, row = i % 5, i // 5
    x = 3.0 + col * 6.0
    ytop = 14.0 - row * 7.2
    bio.label(ax, (x, ytop), g, size="normal", bold=True, italic=True)
    if up:
        twig(x - 1.6, ytop - 3.55, x + 1.6, ytop - 3.55)
        ax.plot([x, x], [ytop - 3.55, ytop - 3.35], color=P.edge("bone"), lw=1.5, zorder=4)
        cone(x, ytop - 2.35, 1.1, 1.9, up=True, shatter=sh, **kw)
    else:
        twig(x - 1.6, ytop - 1.1, x + 1.6, ytop - 1.1)
        ax.plot([x, x], [ytop - 1.1, ytop - 1.35], color=P.edge("bone"), lw=1.5, zorder=4)
        cone(x, ytop - 2.4, 1.1, 1.9, up=False, shatter=sh, **kw)
    leaves(x, ytop - 4.15, lk)
    for k, ln in enumerate(lines):
        bio.label(ax, (x, ytop - 5.0 - 0.45 * k), ln, size="tiny", color=P.muted())
bio.label(ax, (0.3, 14.6), "Abietoideae", size="small", bold=True, ha="left", color=P.edge("animal"))
bio.label(ax, (0.3, 7.4), "Pinoideae", size="small", bold=True, ha="left", color=P.edge("animal"))
