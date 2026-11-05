"""Characteristic structures of cycads, Ginkgo and gnetophytes (schematic). A: megasporophyll of Cycas, a
leaf-like organ with a pinnately divided tip and two to several ovules along the stalk (no seed cone).
B: coralloid roots of a cycad, upward-growing, repeatedly forked, with a ring of cyanobacteria in the cortex
(inset, cross section). C: an ovulate short shoot of Ginkgo: a long stalk ending in two ovules, each on a
collar; usually only one matures. D: the Ginkgo seed in section: fleshy outer layer (sarcotesta), stony
middle layer with two or three ridges (sclerotesta), thin inner layer, female gametophyte and embryo; there
is no fruit wall. E: seed cone of Ephedra: decussate bracts, the uppermost enclosing an ovule whose
integument extends into a long micropylar tube bearing a pollination drop. F: Welwitschia mirabilis, whose
two strap-shaped leaves grow from a basal meristem throughout the life of the plant."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 11)


def poly(pts, tok, lw=0.9, z=6, light=False):
    ax.add_patch(Polygon(np.asarray(pts), closed=True, facecolor=P.light(tok) if light else P.fill(tok), edgecolor=P.edge(tok),
                         lw=lw, joinstyle="round", zorder=z))


def ell(xy, w, h, tok, z=6, light=False, lw=0.9, angle=0):
    ax.add_patch(Ellipse(xy, w, h, angle=angle, facecolor=P.light(tok) if light else P.fill(tok), edgecolor=P.edge(tok), lw=lw,
                         zorder=z))


# A: Cycas megasporophyll
x = 2.5
poly([(x - 0.18, 1.3), (x - 0.22, 5.2), (x + 0.22, 5.2), (x + 0.18, 1.3)], "bract", z=5)
poly([(x - 0.9, 5.0), (x - 1.2, 7.8), (x, 9.0), (x + 1.2, 7.8), (x + 0.9, 5.0)], "bract", z=5)
for k in range(5):
    y = 5.5 + 0.65 * k
    for sgn in (-1, 1):
        ax.plot([x + sgn * 0.8, x + sgn * 1.6], [y, y + 0.35], color=P.edge("bract"), lw=2.0, solid_capstyle="round", zorder=4)
for k, y in enumerate((2.0, 3.0, 4.0)):
    for sgn in (-1, 1):
        ell((x + sgn * 0.55, y), 0.62, 0.75, "animal", z=7)
bio.callout(ax, (x + 0.85, 3.0), (x + 1.9, 2.2), "ovule")

# B: coralloid roots
x = 7.3
ax.plot([x, x], [1.2, 3.2], color=P.edge("bone"), lw=3.0, zorder=4)


def fork(p, a, L, d):
    if d == 0:
        return
    q = (p[0] + L * np.cos(np.radians(a)), p[1] + L * np.sin(np.radians(a)))
    ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge("ovule"), lw=3.2 - 0.5 * (3 - d), solid_capstyle="round", zorder=5)
    if d == 1:
        ax.add_patch(Circle(q, 0.14, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=0.6, zorder=6))
    fork(q, a + 32, L * 0.75, d - 1)
    fork(q, a - 32, L * 0.75, d - 1)


fork((x, 3.2), 90, 1.1, 4)
c = (x, 8.6)
ell(c, 2.0, 2.0, "ovule", z=6)
ax.add_patch(Circle(c, 0.66, facecolor="none", edgecolor=P.edge("chloroplast"), lw=4.0, zorder=7))
ell(c, 0.6, 0.6, "channel", z=8)
bio.callout(ax, (c[0] + 0.62, c[1] + 0.25), (c[0] + 1.7, c[1] + 1.5), "cyanobacteria")

# C: Ginkgo ovulate short shoot
x = 12.2
ax.plot([x, x], [1.2, 2.4], color=P.edge("bone"), lw=4.0, zorder=4)
for a in np.linspace(50, 130, 5):
    r = np.radians(a)
    poly([(x, 2.4), (x + 1.3 * np.cos(r - 0.25), 2.4 + 1.3 * np.sin(r - 0.25)), (x + 1.4 * np.cos(r + 0.2), 2.4 + 1.4 * np.sin(r + 0.2))],
         "plant", z=3, light=True)
ax.plot([x, x], [2.4, 6.4], color=P.edge("plant"), lw=1.6, zorder=5)
for sgn in (-1, 1):
    ax.plot([x, x + sgn * 0.55], [6.4, 7.0], color=P.edge("plant"), lw=1.4, zorder=5)
    ell((x + sgn * 0.55, 7.05), 0.75, 0.22, "plant", z=6)
    ell((x + sgn * 0.6, 7.6 - 0.25 * (sgn > 0)), 0.65 if sgn < 0 else 0.42, 0.85 if sgn < 0 else 0.5, "animal", z=7)
bio.callout(ax, (x - 0.9, 7.05), (x - 1.7, 6.0), "collar")

# D: Ginkgo seed section
c = (17.2, 5.2)
ell(c, 3.4, 3.9, "petal", z=5, light=True)
ell(c, 2.4, 2.9, "bone", z=6)
ell(c, 2.05, 2.55, "tepal", z=7, light=True)
ell(c, 1.85, 2.35, "lipid", z=8)
ell((c[0], c[1] + 0.25), 0.3, 1.2, "plant", z=9)
for sgn in (-1, 1):
    ax.plot([c[0] + sgn * 1.2, c[0] + sgn * 1.38], [c[1], c[1]], color=P.edge("bone"), lw=1.5, zorder=7)
bio.callout(ax, (c[0] + 1.5, c[1] + 1.0), (c[0] + 2.3, c[1] + 2.8), "sarcotesta")
bio.callout(ax, (c[0] + 1.15, c[1] - 0.6), (c[0] + 2.3, c[1] - 2.8), "sclerotesta")
bio.callout(ax, (c[0] - 0.6, c[1] - 0.7), (c[0] - 2.2, c[1] - 2.9), "female gametophyte")
bio.callout(ax, (c[0], c[1] + 0.7), (c[0] - 1.6, c[1] + 3.0), "embryo")

# E: Ephedra seed cone
x = 22.6
ax.plot([x, x], [1.2, 3.0], color=P.edge("plant"), lw=2.4, zorder=4)
for k in range(3):
    y = 3.0 + 0.9 * k
    w = 1.3 - 0.2 * k
    for sgn in (-1, 1):
        poly([(x, y), (x + sgn * w, y + 0.5), (x + sgn * w * 0.6, y + 1.05), (x, y + 0.35)], "plant", z=5 + k)
ell((x, 6.2), 0.95, 1.45, "animal", z=9)
poly([(x - 0.08, 6.85), (x - 0.06, 8.5), (x + 0.06, 8.5), (x + 0.08, 6.85)], "bract", z=10)
ax.add_patch(Circle((x, 8.7), 0.22, facecolor=P.light("vacuole"), edgecolor=P.edge("vacuole"), lw=0.8, zorder=11))
bio.callout(ax, (x + 0.07, 7.8), (x + 1.5, 8.6), "micropylar tube")
bio.callout(ax, (x + 0.45, 6.0), (x + 1.6, 6.9), "envelope")
bio.callout(ax, (x + 1.0, 3.6), (x + 1.9, 2.4), "bracts")

# F: Welwitschia
x = 27.6
bio.icon(ax, "phylopic/welwitschia", at=(x, 3.6), height=3.2, color="plant")

for x, h in ((2.5, r"A  $\it{Cycas}$ megasporophyll"), (7.3, "B  Coralloid roots"), (12.2, r"C  $\it{Ginkgo}$ ovules"), (17.2, r"D  $\it{Ginkgo}$ seed"),
             (22.6, r"E  $\it{Ephedra}$ seed cone"), (27.6, r"F  $\it{Welwitschia}$")):
    bio.label(ax, (x, 10.6), h, size="normal", bold=True)
