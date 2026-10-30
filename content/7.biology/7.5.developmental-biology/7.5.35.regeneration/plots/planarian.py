"""Planarian regeneration: polarity, its molecular control, and the axes.

Worms are drawn schematically in dorsal view, anterior to the left (head with two eyes and auricles, pharynx in
the middle). New tissue (blastema) is pale. A: a worm cut in three: each piece regenerates the missing structures,
with a head at the end that faced anterior and a tail at the end that faced posterior. B: RNA interference before
amputation of the head and tail: control trunk pieces regenerate normally; with beta-catenin-1 knocked down the
posterior blastema forms a head (two-headed worm); with notum knocked down the anterior blastema forms a tail.
C: the axes and their signals in muscle cells: Wnt/beta-catenin high posteriorly (wnt1 and wntP-2), Notum at
the anterior tip; BMP4 on the dorsal midline (dorsal fate, opposite to vertebrates where BMP is ventral); Slit
at the midline and Wnt5 laterally (mediolateral axis).
"""

import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon
import wikibio as bio

P = bio.P
LW = bio.core.LINE
fig, ax = bio.canvas(32.0, 15.0)


def outline(x0, x1, y, w, head_l=True, head_r=False):
    """Points of a flatworm outline from x0 (left end) to x1; head ends are triangular with auricles."""
    t = np.linspace(0, 1, 60)
    xs = x0 + (x1 - x0) * t
    prof = np.ones_like(t)
    L = x1 - x0
    for end, is_head in ((0, head_l), (1, head_r)):
        s = t if end == 0 else 1 - t
        if is_head:
            prof = np.minimum(prof, np.clip(0.45 + 2.6 * s, 0, 1))
        else:
            prof = np.minimum(prof, np.sqrt(np.clip(s / 0.18, 0, 1)) * 0.95 + 0.05 * (s > 0))
    top = np.column_stack([xs, y + 0.5 * w * prof])
    bot = np.column_stack([xs[::-1], y - 0.5 * w * prof[::-1]])
    pts = np.vstack([top, bot])
    return pts, L


def worm(x0, x1, y, w=1.3, left="head", right="tail", new_left=0.0, new_right=0.0, tok="animal"):
    pts, L = outline(x0, x1, y, w, left == "head", right == "head")
    ax.add_patch(Polygon(pts, closed=True, fc=P.fill(tok), ec=P.edge(tok), lw=LW, zorder=5))
    # blastemas
    for frac, side in ((new_left, 0), (new_right, 1)):
        if frac > 0:
            xa, xb = (x0, x0 + frac * L) if side == 0 else (x1 - frac * L, x1)
            m = (pts[:, 0] >= xa - 1e-9) & (pts[:, 0] <= xb + 1e-9)
            sub = pts[m]
            ax.add_patch(Polygon(sub, closed=True, fc=P.light(tok), ec="none", zorder=6))
            ax.plot([xb if side == 0 else xa] * 2, [y - 0.45 * w, y + 0.45 * w], color=P.muted(), lw=0.7,
                    ls=(0, (2, 2)), zorder=7)
    for end, kind in ((x0, left), (x1, right)):
        if kind == "head":
            sgn = 1 if end == x0 else -1
            for dy in (-0.18, 0.18):
                ax.add_patch(Circle((end + sgn * 0.55, y + dy * w), 0.09, color=P.ink(), zorder=8))
            for dy in (-1, 1):
                ax.add_patch(Polygon([(end + sgn * 0.35, y + dy * 0.36 * w), (end + sgn * 0.15, y + dy * 0.62 * w),
                                      (end + sgn * 0.7, y + dy * 0.42 * w)], closed=True, fc=P.fill(tok),
                                     ec=P.edge(tok), lw=LW * 0.8, zorder=4))


# A: cutting in three
bio.panel(ax, "A", (0.2, 14.8))
bio.label(ax, (1.4, 14.5), "Polarity of regeneration", size="small", bold=True, ha="left")
worm(1.0, 9.0, 12.6)
ax.add_patch(Ellipse((5.0, 12.6), 0.9, 0.35, fc=P.light("animal"), ec=P.edge("animal"), lw=LW * 0.7, zorder=7))
for xc in (3.6, 6.6):
    ax.plot([xc, xc], [11.6, 13.6], color=P.edge("negative"), lw=1.2, ls=(0, (3, 2)), zorder=9)
bio.label(ax, (2.3, 13.9), "head", size="tiny", color=P.muted())
bio.label(ax, (5.1, 13.9), "trunk", size="tiny", color=P.muted())
bio.label(ax, (7.8, 13.9), "tail", size="tiny", color=P.muted())
bio.arrow(ax, (5.0, 11.4), (5.0, 10.3), kind="process")
worm(0.6, 4.4, 9.2, w=1.2, new_right=0.35)
worm(5.0, 8.4, 9.2, w=1.2, new_left=0.28, new_right=0.28)
worm(9.0, 12.4, 9.2, w=1.2, new_left=0.35)
bio.label(ax, (6.5, 8.0), "pale: blastema; a head forms at the end that faced anterior", size="tiny", color=P.muted())

# B: RNAi
bio.panel(ax, "B", (14.0, 14.8))
bio.label(ax, (15.2, 14.5), "RNAi, then remove head and tail", size="small", bold=True, ha="left")
rows = (("control", "head", "tail"), (r"$\it{\beta}$-$\it{catenin}$-$\it{1}$ RNAi", "head", "head"), (r"$\it{notum}$ RNAi", "tail", "tail"))
for i, (name, l, r) in enumerate(rows):
    y = 12.8 - 2.2 * i
    bio.label(ax, (15.0, y), name, size="small", ha="left")
    bio.arrow(ax, (19.3, y), (20.4, y), kind="process")
    worm(20.8, 26.8, y, w=1.2, left=l, right=r, new_left=0.22, new_right=0.22,
         tok="animal" if i == 0 else "negative")
    res = ("normal worm" if i == 0 else "two heads" if i == 1 else "two tails")
    bio.label(ax, (27.4, y), res, size="small", ha="left", bold=True,
              color=P.edge("positive" if i == 0 else "negative"))

# C: axes and signals
bio.panel(ax, "C", (0.2, 6.4))
bio.label(ax, (1.4, 6.1), "Body axes and position control genes in muscle", size="small", bold=True, ha="left")
x0, x1, y = 2.0, 16.0, 3.0
pts, L = outline(x0, x1, y, 2.6, True, False)
ax.add_patch(Polygon(pts, closed=True, fc=P.fill("animal"), ec=P.edge("animal"), lw=LW, zorder=5))
for k in range(10):
    xa = x0 + L * (0.5 + 0.05 * k)
    m = pts[:, 0] >= xa
    ax.add_patch(Polygon(pts[m], closed=True, fc=P.fill("receptor"), ec="none", alpha=0.12, zorder=6))
ax.add_patch(Circle((x0 + 0.35, y), 0.28, fc=P.fill("enzyme"), ec=P.edge("enzyme"), lw=LW * 0.8, zorder=8))
ax.plot([x0 + 0.9, x1 - 0.4], [y, y], color=P.edge("highlight"), lw=2.2, zorder=7)
for dy in (-1, 1):
    ax.plot([x0 + 2.0, x1 - 2.0], [y + dy * 1.0, y + dy * 1.0], color=P.edge("channel"), lw=1.8,
            ls=(0, (4, 2)), zorder=7)
for dy in (-0.25, 0.25):
    ax.add_patch(Circle((x0 + 0.9, y + dy * 2.6), 0.1, color=P.ink(), zorder=9))
bio.callout(ax, (x0 + 0.35, y + 0.2), (x0 + 0.2, 5.3), r"$\it{notum}$ (anterior pole)", size="tiny")
bio.callout(ax, (x1 - 2.5, y + 0.5), (x1 - 2.5, 5.3), r"$\it{wnt1}$, $\it{wntP}$-$\it{2}$: posterior", size="tiny")
bio.callout(ax, (x0 + 6.0, y), (x0 + 6.0, 5.3), r"$\it{slit}$ (midline)", size="tiny")
bio.callout(ax, (x0 + 9.0, y - 1.0), (x0 + 9.0, 0.7), r"$\it{wnt5}$ (lateral)", size="tiny")
# DV section
cx, cy = 20.0, 3.0
ax.add_patch(Ellipse((cx, cy), 3.6, 1.6, fc=P.fill("animal"), ec=P.edge("animal"), lw=LW, zorder=5))
ax.add_patch(Ellipse((cx, cy + 0.62), 0.9, 0.3, fc=P.fill("protein"), ec=P.edge("protein"), lw=LW * 0.8, zorder=6))
bio.label(ax, (cx, cy + 1.15), r"dorsal: $\it{bmp4}$", size="tiny")
bio.label(ax, (cx, cy - 1.2), "ventral (mouth, nerve cords)", size="tiny")
bio.label(ax, (cx, 4.6), "cross-section", size="tiny", color=P.muted())
txt = ("Wnt/β-catenin: posterior identity\n(as in vertebrates)\n"
       "BMP: dorsal identity\n(opposite to vertebrates)\n"
       "Notum inhibits Wnt at the anterior pole")
bio.label(ax, (23.5, 3.2), txt, size="tiny", ha="left")
