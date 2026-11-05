# Secondary growth in monocots and cambial variants (transverse sections, schematic; xylem blue, phloem
# orange, cambium yellow). (A) Dracaena: scattered primary collateral bundles in the centre; a cambium in
# the cortex produces inwards a zone of ground tissue with denser amphivasal secondary bundles (xylem
# around phloem), outwards a little parenchyma. (B) Successive cambia: concentric rings of xylem and phloem,
# each from a new cambium outside the last (Amaranthaceae stems, beet root). (C) Included phloem: strands of
# phloem embedded in the secondary xylem (Mirabilis). (D) Furrowed xylem: in four sectors the cambium makes
# little xylem and much phloem, giving a cross-shaped xylem (Bignoniaceae lianas).
import math

import numpy as np
from matplotlib.patches import Circle, Wedge

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(33.0, 10.4)
rng = np.random.default_rng(3)
R = 3.6
cs = [np.array([4.2 + k * 8.2, 4.8]) for k in range(4)]
titles = ["Dracaena", "Successive cambia", "Included phloem", "Furrowed xylem (liana)"]
for k, c in enumerate(cs):
    bio.panel(ax, "ABCD"[k], (c[0] - 4.0, 10.2))
    bio.label(ax, (c[0], 9.8), titles[k], size="normal", bold=True, italic=(k == 0))


def circ(c, r, tok, z=2, fill=True, lw=0.8, ls="-"):
    ax.add_patch(Circle(c, r, facecolor=P.fill(tok) if fill else "none", edgecolor=P.edge(tok), lw=lw, zorder=z, ls=ls))


def bundle(p, r, amphivasal=False, z=5):
    if amphivasal:
        circ(p, r, "xylem", z=z)
        circ(p, r * 0.5, "phloem", z=z + 0.1)
    else:
        circ(p, r, "xylem", z=z)
        ax.add_patch(Wedge(p, r, 20, 160, facecolor=P.fill("phloem"), edgecolor=P.edge("phloem"), lw=0.6, zorder=z + 0.1))


# A
c = cs[0]
circ(c, R, "cytoplasm")
circ(c, R, "cork", fill=False, lw=2.0, z=6)
circ(c, 2.0, "cambium", fill=False, lw=2.4, z=6)
for k in range(26):
    rr, a = 1.75 * math.sqrt(rng.random()), rng.uniform(0, 2 * math.pi)
    bundle(c + rr * np.array([math.cos(a), math.sin(a)]), 0.16)
for k in range(40):
    rr, a = rng.uniform(2.1, 2.9), rng.uniform(0, 2 * math.pi)
    bundle(c + rr * np.array([math.cos(a), math.sin(a)]), 0.12, amphivasal=True)
bio.callout(ax, tuple(c + 2.0 * np.array([0.7, 0.71])), (c[0] + 1.6, 9.0), "Cambium", size="small")
bio.callout(ax, tuple(c + 0.8 * np.array([-0.6, -0.8])), (c[0] - 1.6, 0.4), "Primary bundles", size="small")
bio.callout(ax, tuple(c + 2.5 * np.array([0.7, -0.71])), (c[0] + 1.6, 0.4), "Secondary bundles", size="small")
# B
c = cs[1]
circ(c, R, "cytoplasm")
for r0, r1 in ((0.5, 1.0), (1.3, 1.8), (2.1, 2.6), (2.9, 3.4)):
    for i in range(10):
        a0 = i * 36 + 4
        ax.add_patch(Wedge(c, r1 - 0.18, a0, a0 + 28, width=r1 - 0.18 - r0, facecolor=P.fill("xylem"), edgecolor=P.edge("xylem"),
                           lw=0.5, zorder=4))
        ax.add_patch(Wedge(c, r1, a0, a0 + 28, width=0.17, facecolor=P.fill("phloem"), edgecolor=P.edge("phloem"), lw=0.5, zorder=4))
    circ(c, r1 - 0.18, "cambium", fill=False, lw=1.0, z=5)
bio.callout(ax, tuple(c + 2.4 * np.array([0, 1])), (c[0] + 1.4, 9.0), "One of several cambia", size="small")
bio.callout(ax, tuple(c + 1.9 * np.array([-0.7, -0.7])), (c[0] - 1.4, 0.4), "Parenchyma between rings", size="small")
# C
c = cs[2]
circ(c, R, "phloem")
circ(c, 3.05, "xylem")
circ(c, 3.05, "cambium", fill=False, lw=2.2, z=6)
circ(c, 0.7, "cytoplasm", z=3)
for k in range(28):
    rr, a = rng.uniform(1.0, 2.8), rng.uniform(0, 2 * math.pi)
    p = c + rr * np.array([math.cos(a), math.sin(a)])
    circ(p, 0.15, "phloem", z=5)
bio.callout(ax, tuple(c + 2.0 * np.array([0.6, 0.8])), (c[0] + 1.4, 9.0), "Included phloem", size="small")
bio.callout(ax, tuple(c + 3.05 * np.array([0.7, -0.71])), (c[0] + 1.4, 0.4), "Cambium", size="small")
# D
c = cs[3]
circ(c, R, "phloem")
t = np.linspace(0, 2 * np.pi, 400)
r = 1.6 + 1.4 * np.clip(np.cos(4 * t) * 3, -1, 1) * 0.5 + 0.7
pts = np.c_[c[0] + r * np.cos(t), c[1] + r * np.sin(t)]
from matplotlib.patches import Polygon  # noqa: E402

ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill("xylem"), edgecolor=P.edge("xylem"), lw=0.8, zorder=4))
ax.plot(pts[:, 0], pts[:, 1], color=P.edge("cambium"), lw=2.0, zorder=5)
circ(c, 0.5, "cytoplasm", z=4.5)
bio.callout(ax, tuple(c + 2.4 * np.array([0.71, 0.71])), (c[0] + 1.4, 9.0), "Phloem wedge", size="small")
bio.callout(ax, tuple(c + 2.5 * np.array([1, 0])), (c[0] + 1.4, 0.4), "Xylem arm", size="small")
