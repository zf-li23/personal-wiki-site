"""Nitrogen inversion of N-methylethylamine. The pyramidal amine (lone pair up, sp3) passes through a
planar transition state in which nitrogen is sp2 and the lone pair occupies a p orbital, and comes
out as its mirror image (lone pair down). The barrier is only about 25-35 kJ/mol, so the two
enantiomeric pyramids interconvert about 10^7 times a second at room temperature and cannot be
resolved. Wedge: bond toward the viewer; hashes: bond away from the viewer."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgb
from matplotlib.patches import Ellipse, Polygon

from wikichem import Scheme

GAP = 0.3  # bonds stop short of an atom label
INK = plt.rcParams["text.color"]  # the renderer sets it per theme


def trim(a, b, ga, gb):
    a, b = np.asarray(a, float), np.asarray(b, float)
    u = (b - a) / np.linalg.norm(b - a)
    return a + ga * u, b - gb * u


def plain(ax, a, b, ga=0.0, gb=0.0):
    a, b = trim(a, b, ga, gb)
    ax.plot(*zip(a, b), color=INK, lw=1.4, solid_capstyle="round")


def wedge(ax, a, b, ga=0.0, gb=0.0):
    a, b = trim(a, b, ga, gb)
    n = np.array([-(b - a)[1], (b - a)[0]])
    n = n / np.linalg.norm(n)
    ax.add_patch(Polygon([a, b + 0.09 * n, b - 0.09 * n], closed=True, color=INK, lw=0))


def hashed(ax, a, b, ga=0.0, gb=0.0):
    a, b = trim(a, b, ga, gb)
    n = np.array([-(b - a)[1], (b - a)[0]])
    n = n / np.linalg.norm(n)
    for t in np.linspace(0.1, 1.0, 7):
        p = a + t * (b - a)
        ax.plot(*zip(p - 0.09 * t * n, p + 0.09 * t * n), color=INK, lw=1.0)


def label(ax, p, s):
    ax.text(*p, s, ha="center", va="center", fontsize=12, color=INK)


def pair(ax, p, d):
    """Two dots for a lone pair at distance 0.42 from p in direction d."""
    d = np.asarray(d, float) / np.linalg.norm(d)
    c = np.asarray(p, float) + 0.42 * d
    n = np.array([-d[1], d[0]])
    for q in (c + 0.07 * n, c - 0.07 * n):
        ax.plot(*q, "o", color=INK, ms=2.6)


def amine(ax, o, up):
    """Pyramidal N-methylethylamine at o; up=+1 puts the lone pair on top, -1 at the bottom (mirror image)."""
    o = np.asarray(o, float)
    s = up
    n = o
    me, et1, h = o + (-0.95, -0.45 * s), o + (0.55, -0.85 * s), o + (0.95, 0.15 * s)
    et2 = et1 + (0.95, 0.3 * s)
    label(ax, n, "N")
    label(ax, h + (0.2, 0.05 * s), "H")
    plain(ax, n, me, GAP, 0)
    wedge(ax, n, et1, GAP, 0)
    plain(ax, et1, et2)
    hashed(ax, n, h, GAP, 0.05)
    pair(ax, n, (0, s))


s = Scheme()
# bounds and the parts wikichem draws itself: arrows, the p orbital and the captions
for p in [(-1.3, -1.6), (2.2, 1.6), (4.0, -1.6), (12.6, 1.6), (6.0, 1.5), (6.0, -1.5)]:
    s.text(p, "")
s.arrow((2.6, 0), (4.0, 0), kind="equilibrium")
ts = np.array((6.0, 0.0))
s.arrow((8.4, 0), (9.8, 0), kind="equilibrium")
s.text((0.3, -2.0), "pyramidal (sp$^3$)")
s.text(ts + (0.3, -2.0), "planar TS (sp$^2$)")
s.text((11.4, -2.0), "mirror image")
fig, ax = s.draw()
amine(ax, (0, 0), +1)
amine(ax, (11.1, 0), -1)
# planar transition state seen edge-on: the three bonds lie in the horizontal plane
label(ax, ts, "N")
for dy, shaded in ((0.78, True), (-0.78, False)):
    ax.add_patch(Ellipse(ts + (0, dy), 0.5, 1.05, facecolor=(*to_rgb(INK), 0.3) if shaded else "none", edgecolor=INK, lw=1.0, zorder=0))
plain(ax, ts, ts + (-1.0, 0), GAP, 0)
wedge(ax, ts, ts + (0.85, -0.45), GAP, 0)
plain(ax, ts + (0.85, -0.45), ts + (1.8, -0.15))
hashed(ax, ts, ts + (0.75, 0.3), GAP, 0.05)
label(ax, ts + (0.98, 0.38), "H")
