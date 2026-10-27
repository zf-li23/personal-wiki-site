"""Topologies of proteins made at the ER, and the signals that produce them (ER lumen up, cytosol down).

1 Soluble secretory protein: cleaved N-terminal signal sequence; the whole chain enters the lumen.
2 Type I single-pass: cleaved signal sequence (start transfer) + internal stop-transfer sequence;
  N-terminus in the lumen.
3 Type II: internal uncleaved signal-anchor sequence with positive charges on its N-terminal side;
  N-terminus in the cytosol.
4 Type III: signal-anchor in the opposite orientation (positive charges on its C-terminal side);
  N-terminus in the lumen.
5 Tail-anchored: a single C-terminal transmembrane segment, inserted after translation (GET pathway).
6 Multipass: alternating start- and stop-transfer sequences (here four transmembrane helices).
7 GPI-anchored: the C-terminal transmembrane segment is cleaved and replaced by a GPI anchor in the
  lumenal leaflet.
Red segments: cleaved signal sequences; blue: transmembrane segments; + marks basic residues.
"""

import numpy as np
import wikibio as bio
from wikibio import cellbio as CB
from matplotlib.patches import FancyBboxPatch

P = bio.P
fig, ax = bio.canvas(26.0, 8.6)
y = 4.2
MH = CB.MH
CB.sides(ax, (0.2, 25.8), y, height=(3.6, 3.4), top=None, bottom=None)
bio.bilayer(ax, [(0.2, y), (25.8, y)])
bio.label(ax, (0.4, 7.5), "ER lumen (≡ exterior)", size="small", bold=True, ha="left", color=P.muted())
bio.label(ax, (0.4, 1.05), "Cytosol", size="small", bold=True, ha="left", color=P.muted())
LW = 2.0
ink = P.edge("protein")


def chain(pts):
    pts = np.asarray(pts, float)
    t = np.linspace(0, 1, len(pts))
    tt = np.linspace(0, 1, 200)
    from scipy.interpolate import make_interp_spline
    k = min(3, len(pts) - 1)
    sp = make_interp_spline(t, pts, k=k)
    q = sp(tt)
    ax.plot(q[:, 0], q[:, 1], color=ink, lw=LW, solid_capstyle="round", zorder=12)


def tm(x, tok="channel"):
    ax.add_patch(FancyBboxPatch((x - 0.14, y - MH - 0.12), 0.28, 2 * MH + 0.24, boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=13))


def end(xy, text):
    bio.label(ax, xy, text, size="tiny", bold=True)


def plus(xy):
    bio.label(ax, xy, "+", size="small", bold=True, color=P.edge("negative"))


def title(x, t1, t2):
    bio.label(ax, (x, 0.55), t1, size="small", bold=True)
    bio.label(ax, (x, 0.12), t2, size="tiny", color=P.muted())


top, bot = y + MH + 0.12, y - MH - 0.12
# 1 soluble
x = 1.9
chain([(x - 0.6, 6.0), (x - 0.1, 6.7), (x + 0.5, 6.1), (x + 0.1, 5.4), (x + 0.6, 5.0)])
bio.protein(ax, (x + 0.6, 6.3), 0.9, 0.8, "protein", wobble=0.06)
bio.label(ax, (x - 0.6, 5.6), "signal\ncleaved", size="tiny", color=P.edge("negative"))
title(x, "secretory", "soluble")
# 2 type I
x = 5.3
tm(x)
chain([(x, top), (x - 0.4, 5.4), (x - 0.9, 6.2)])
end((x - 1.15, 6.35), "N")
chain([(x, bot), (x + 0.3, 2.9), (x + 0.8, 2.5)])
end((x + 1.0, 2.35), "C")
plus((x + 0.35, bot - 0.25))
title(x, "type I", "stop-transfer")
# 3 type II
x = 8.7
tm(x, "receptor")
chain([(x, bot), (x - 0.4, 2.9), (x - 0.9, 2.5)])
end((x - 1.1, 2.35), "N")
plus((x - 0.35, bot - 0.25))
chain([(x, top), (x + 0.4, 5.4), (x + 0.9, 6.2)])
end((x + 1.1, 6.35), "C")
title(x, "type II", "signal anchor, N in")
# 4 type III
x = 12.1
tm(x, "receptor")
chain([(x, top), (x - 0.4, 5.4), (x - 0.9, 6.2)])
end((x - 1.1, 6.35), "N")
chain([(x, bot), (x + 0.4, 2.9), (x + 0.9, 2.5)])
end((x + 1.1, 2.35), "C")
plus((x + 0.35, bot - 0.25))
title(x, "type III", "signal anchor, N out")
# 5 tail-anchored
x = 15.3
tm(x, "enzyme")
chain([(x, bot), (x - 0.6, 3.0), (x - 0.4, 2.2), (x - 1.0, 1.8)])
bio.protein(ax, (x - 0.6, 2.5), 0.9, 0.7, "protein", wobble=0.06)
end((x - 1.25, 1.6), "N")
end((x, top + 0.25), "C")
title(x, "tail-anchored", "C-terminal TM (GET)")
# 6 multipass
x = 18.8
xs = [x - 0.9, x - 0.3, x + 0.3, x + 0.9]
for xi in xs:
    tm(xi)
chain([(xs[0], bot), (xs[0] - 0.4, 3.0), (xs[0] - 0.7, 2.6)])
end((xs[0] - 0.85, 2.45), "N")
chain([(xs[0], top), ((xs[0] + xs[1]) / 2, top + 0.45), (xs[1], top)])
chain([(xs[1], bot), ((xs[1] + xs[2]) / 2, bot - 0.45), (xs[2], bot)])
chain([(xs[2], top), ((xs[2] + xs[3]) / 2, top + 0.45), (xs[3], top)])
chain([(xs[3], bot), (xs[3] + 0.4, 3.0), (xs[3] + 0.7, 2.6)])
end((xs[3] + 0.85, 2.45), "C")
for xi in (xs[0], xs[2]):
    plus((xi - 0.12, bot - 0.3))
title(x, "multipass", "start / stop alternate")
# 7 GPI
x = 23.3
ax.plot([x, x], [y + 0.05, top + 0.25], color=P.edge("lipid"), lw=1.6, zorder=13)
for k in range(3):
    bio.molecule(ax, (x + 0.12 * (k % 2), top + 0.32 + 0.22 * k), token="carbohydrate", r=0.09, zorder=14)
chain([(x, top + 0.95), (x - 0.3, 5.6), (x + 0.2, 6.3)])
bio.protein(ax, (x + 0.3, 6.5), 0.95, 0.75, "protein", wobble=0.06)
end((x - 0.5, 5.5), "C")
bio.callout(ax, (x, y + 0.1), (x + 1.2, y - 1.2), "GPI anchor", size="tiny")
title(x, "GPI-anchored", "TM replaced by lipid")
