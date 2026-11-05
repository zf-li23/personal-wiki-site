"""Parts of a leaf. A: a simple eudicot leaf at a node: blade with apex, margin, midrib and veins,
petiole, a pair of stipules, axillary bud. B: the blade-sheath junction of a grass leaf: the sheath wraps
the culm, a membranous ligule stands on the adaxial side at the junction, a pair of auricles clasps the
culm at the blade base, and the collar is the pale band on the abaxial side.
"""

import numpy as np
from matplotlib.patches import Polygon

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(26.0, 13.0)


def poly(pts, tk, light=False, z=5, lw=1.1):
    fc = P.light(tk) if light else P.fill(tk)
    ax.add_patch(Polygon(np.asarray(pts), closed=True, facecolor=fc, edgecolor=P.edge(tk), lw=lw, zorder=z,
                         joinstyle="round"))


# ---- A: simple leaf -------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 12.8))
bio.label(ax, (0.85, 12.77), "Simple leaf (eudicot)", size="title", ha="left", va="top")
sx, sy = 2.6, 1.0
ax.plot([sx, sx], [sy, sy + 10.0], color=P.edge("plant"), lw=7.0, solid_capstyle="round", zorder=4)
ax.plot([sx, sx], [sy, sy + 10.0], color=P.fill("plant"), lw=4.6, solid_capstyle="round", zorder=4.1)
node = (sx, sy + 3.2)
a = B.leaf(ax, node, 6.0, 40, shape="ovate", margin="serrate", venation="pinnate", secondaries=6, petiole=1.8,
           stipules=True, tertiary="percurrent")
bud = B.bud(ax, (sx + 0.22, node[1] + 0.5), 0.55, angle=70)
right = [("Apex", a["apex"]), ("Blade (lamina)", B.leaf_point(a, 0.7, -0.35)),
         ("Margin (serrate)", B.leaf_point(a, 0.45, -1.0)), ("Secondary vein", B.vein_point(a, 2, 0.5, -0.55)),
         ("Midrib", B.leaf_point(a, 0.85, 0))]
right.sort(key=lambda t: -t[1][1])
for k, (name, p) in enumerate(right):
    bio.callout(ax, p, (11.4, 11.6 - k * 1.05), name)
bio.callout(ax, a["petiole"], (6.4, 2.7), "Petiole")
bio.callout(ax, a["stipules"][1], (5.8, 1.5), "Stipule")
bio.callout(ax, a["attachment"], (1.3, 9.0), "Leaf base")
bio.callout(ax, bud, (1.3, 6.8), "Axillary bud")
bio.callout(ax, node, (1.3, 2.6), "Node")

# ---- B: grass leaf junction ------------------------------------------------------------------------
X0 = 17.0
bio.panel(ax, "B", (14.2, 12.8))
bio.label(ax, (14.85, 12.77), "Grass leaf: blade-sheath junction", size="title", ha="left", va="top")
cw = 0.9  # culm width
# culm (behind)
poly([(X0 - cw / 2, 0.6), (X0 + cw / 2, 0.6), (X0 + cw / 2, 12.0), (X0 - cw / 2, 12.0)], "plant", light=True, z=3)
# sheath wrapping the culm: slightly wider, from 0.6 to 7.0
yt = 7.0
sw = 1.5
poly([(X0 - sw / 2, 0.6), (X0 + sw / 2, 0.6), (X0 + sw / 2 + 0.05, yt), (X0 - sw / 2, yt - 0.25)], "plant", z=5)
for x in np.linspace(X0 - sw / 2 + 0.25, X0 + sw / 2 - 0.25, 5):
    ax.plot([x, x + 0.02], [0.8, yt - 0.35], color=P.edge("plant"), lw=0.5, zorder=5.2)
# overlapping margin line of the sheath
ax.plot([X0 + 0.15, X0 + 0.35], [0.6, yt - 0.1], color=P.edge("plant"), lw=0.9, zorder=5.3)
# collar (pale band, abaxial side = right)
poly([(X0 + sw / 2 - 0.05, yt - 0.35), (X0 + sw / 2 + 0.45, yt + 0.05), (X0 + sw / 2 + 0.75, yt + 0.55),
      (X0 + sw / 2 + 0.15, yt + 0.25)], "bract", z=6.5)
# blade: bends outward to the right
t = np.linspace(0, 1, 60)
cx = X0 + sw / 2 + 0.2 + 7.6 * t ** 1.1
cy = yt + 0.25 + 4.3 * np.sin(t * 1.25) - 1.2 * t ** 3
half = 0.55 * (1 - t ** 1.6) + 0.02
nrm = np.c_[-(np.gradient(cy)), np.gradient(cx)]
nrm /= np.hypot(*nrm.T)[:, None]
up = np.c_[cx, cy] + nrm * half[:, None]
dn = np.c_[cx, cy] - nrm * half[:, None]
poly(np.vstack([up, dn[::-1]]), "plant", z=6)
for f in (-0.5, 0.0, 0.5):
    pts = np.c_[cx, cy] + nrm * (half * f)[:, None]
    ax.plot(pts[3:-4, 0], pts[3:-4, 1], color=P.edge("plant"), lw=0.6 if f else 0.9, zorder=6.2)
# ligule: membranous, adaxial side, between culm and blade base
poly([(X0 - 0.35, yt - 0.1), (X0 + 0.55, yt - 0.05), (X0 + 0.6, yt + 0.75), (X0 + 0.15, yt + 0.95),
      (X0 - 0.3, yt + 0.7)], "bract", light=True, z=6.8, lw=0.9)
# auricles: two claw-like lobes clasping the culm
poly([(X0 + sw / 2 - 0.1, yt + 0.15), (X0 - 0.1, yt + 0.55), (X0 - 0.75, yt + 0.4), (X0 - 0.55, yt + 0.2),
      (X0 - 0.05, yt + 0.25)], "plant", z=7.0, lw=0.9)
# leader labels
bio.callout(ax, (cx[30], cy[30]), (21.5, 12.0), "Blade (lamina)")
bio.callout(ax, (X0 + 0.15, yt + 0.8), (14.9, 10.2), "Ligule")
bio.callout(ax, (X0 - 0.6, yt + 0.35), (14.9, 8.6), "Auricle")
bio.callout(ax, (X0 + sw / 2 + 0.45, yt + 0.25), (21.0, 5.6), "Collar")
bio.callout(ax, (X0 + sw / 2 - 0.1, 3.5), (21.0, 3.6), "Leaf sheath")
bio.callout(ax, (X0, 10.8), (14.9, 11.4), "Culm")
