# Domestication traits of rice and some of the genes responsible (schematic, not to scale).
# Left: common wild rice (Oryza rufipogon): prostrate, spreading tillers (PROG1), open panicle with
# few grains, long awns, dark hulls, grains shed at maturity (SH4, qSH1), red pericarp (Rc).
# Right: cultivated rice (O. sativa): erect tillers (prog1), compact panicle with many grains
# (grain number and size: Gn1a, GS3, GW2, GW5), awnless (An-1), straw-white hulls (Bh4),
# grains retained (sh4, qSH1), white pericarp (rc), endosperm amylose set by Waxy alleles.
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse

fig, ax = bio.canvas(26, 13)
STEM = bio.P.edge("plant")


def grain(x, y, ang, token, awn=0.0, size=0.32):
    ax.add_patch(Ellipse((x, y), size, size * 0.42, angle=ang, facecolor=bio.P.fill(token),
                         edgecolor=bio.P.edge(token), lw=0.7, zorder=8))
    if awn > 0:
        r = math.radians(ang)
        x1, y1 = x + 0.5 * size * math.cos(r), y + 0.5 * size * math.sin(r)
        ax.plot([x1, x1 + awn * math.cos(r)], [y1, y1 + awn * math.sin(r)], color=bio.P.muted(), lw=0.6, zorder=7)


def tiller(base, angle, length, droop, panicle):
    """A culm from base at angle (deg from vertical, + right), curving by droop; returns the top and direction."""
    t = np.linspace(0, 1, 40)
    a0 = math.radians(angle)
    ang = a0 + math.radians(droop) * t ** 2
    xs = base[0] + np.cumsum(np.sin(ang)) * length / 40
    ys = base[1] + np.cumsum(np.cos(ang)) * length / 40
    ax.plot(xs, ys, color=STEM, lw=1.6, zorder=5, solid_capstyle="round")
    for k in (12, 22):  # two leaves
        side = 1 if k == 12 else -1
        lx, ly = xs[k], ys[k]
        la = ang[k] + side * 0.7
        tt = np.linspace(0, 1, 20)
        ax.plot(lx + np.sin(la + side * 0.6 * tt) * 1.6 * tt, ly + np.cos(la + side * 0.6 * tt) * 1.6 * tt,
                color=STEM, lw=1.0, zorder=4)
    top = (xs[-1], ys[-1])
    direction = ang[-1]
    panicle(top, direction)
    return top


def wild_panicle(top, d):
    # open, drooping panicle: few long primary branches with few awned dark grains
    for b, off in enumerate((-0.5, -0.15, 0.25)):
        a = d + 0.9 + off
        pts = [(top[0] + math.sin(a) * s, top[1] + math.cos(a) * s - 0.08 * s * s) for s in np.linspace(0, 1.9, 6)]
        ax.plot(*zip(*pts), color=STEM, lw=0.8, zorder=6)
        for (x, y) in pts[2::2]:
            grain(x, y, math.degrees(math.atan2(math.cos(a), math.sin(a))) - 40, "mitochondrion", awn=0.7)


def crop_panicle(top, d):
    # compact panicle bending outwards under the weight of many awnless straw-coloured grains
    sign = 1 if d >= 0 else -1
    for off in (-0.2, 0.0, 0.2):
        a = d + sign * 1.9 + off
        pts = [(top[0] + math.sin(a) * s, top[1] + math.cos(a) * s) for s in np.linspace(0, 1.6, 7)]
        ax.plot(*zip(*pts), color=STEM, lw=0.8, zorder=6)
        for (x, y) in pts[1:]:
            grain(x, y, math.degrees(math.atan2(math.cos(a), math.sin(a))), "highlight", size=0.36)


# Wild rice
bio.label(ax, (6.5, 12.4), "Common wild rice", size="title")
bio.label(ax, (6.5, 11.75), "Oryza rufipogon", italic=True)
base_w = (6.5, 1.0)
tops = [tiller(base_w, a, 5.2, d, wild_panicle) for a, d in ((-62, 25), (-38, 30), (40, -30), (64, -25))]
ax.plot([1.0, 12.0], [1.0, 1.0], color=bio.P.muted(), lw=1.0)
for i, (x, y) in enumerate(((10.3, 3.4), (10.7, 2.2), (11.2, 1.3))):  # shed grains
    grain(x, y, 30 + 40 * i, "mitochondrion", awn=0.5)
bio.arrow(ax, (10.0, 4.2), (10.6, 1.8), kind="process", dashed=True, head=0.15)
bio.callout(ax, (3.9, 3.4), (1.0, 6.2), "prostrate tillers (PROG1)")
bio.callout(ax, (10.7, 2.2), (9.6, 0.45), "grains shed (SH4, qSH1)")
bio.callout(ax, tops[2], (12.3, 8.6), "open panicle, few grains")
bio.callout(ax, (tops[1][0] - 1.4, tops[1][1] + 0.4), (1.0, 9.6), "long awns, dark hulls")

# Cultivated rice
bio.label(ax, (19.5, 12.4), "Cultivated rice", size="title")
bio.label(ax, (19.5, 11.75), "Oryza sativa", italic=True)
base_c = (19.5, 1.0)
tops_c = [tiller(base_c, a, 6.4, d, crop_panicle) for a, d in ((-16, -14), (-6, -10), (6, 10), (16, 14))]
ax.plot([14.0, 25.0], [1.0, 1.0], color=bio.P.muted(), lw=1.0)
bio.callout(ax, (19.3, 3.0), (15.0, 3.6), "erect tillers (prog1)")
bio.callout(ax, (tops_c[3][0] + 0.5, tops_c[3][1] - 0.3), (24.6, 10.0), "compact panicle, many grains")
bio.callout(ax, (tops_c[3][0] + 0.8, tops_c[3][1] - 0.9), (24.6, 4.8), "grains retained (sh4, qSH1)")
bio.label(ax, (24.6, 9.35), "Gn1a, GS3, GW2, GW5", size="small", italic=True, ha="right")
bio.label(ax, (24.6, 8.75), "awnless (An-1), straw hulls (Bh4)", size="small", ha="right")

# Dehulled grains: pericarp colour
for (x, token, txt) in ((2.0, "mitochondrion", "red pericarp (Rc)"), (21.6, "highlight", "white pericarp (rc)")):
    ax.add_patch(Ellipse((x, 0.45), 0.9, 0.42, facecolor=bio.P.fill(token), edgecolor=bio.P.edge(token), lw=0.8))
    bio.label(ax, (x + 0.65, 0.45), txt, size="small", ha="left")
bio.arrow(ax, (13.0, 6.5), (14.8, 6.5), kind="process")
bio.label(ax, (13.9, 7.0), "domestication", size="small", color=bio.P.muted())
