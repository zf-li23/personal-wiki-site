"""The developmental cycle of Chlamydia trachomatis in an epithelial cell (schematic; approximate times
after infection). 1: the small, infectious, metabolically inactive elementary body (EB, about 0.3 um)
attaches and is taken up into a membrane-bound vacuole. 2: within a few hours the EB converts into a
larger reticulate body (RB, about 1 um), which is metabolically active but not infectious. 3: RBs divide
by binary fission inside the growing vacuole, the inclusion, which avoids fusion with lysosomes and
takes up host nutrients and ATP. 4: from about 24 h, RBs asynchronously convert back into EBs.
5: at 48-72 h the EBs are released by lysis of the host cell or by extrusion of the whole inclusion."""
import numpy as np
from matplotlib.patches import Circle, Ellipse

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26, 8)
EB, RB = "negative", "receptor"


def host(cx):
    ax.add_patch(Ellipse((cx, 4.2), 4.2, 4.6, facecolor=P.light("cytoplasm"), edgecolor=P.edge("cytoplasm"), lw=1.2,
                         zorder=3))
    ax.add_patch(Ellipse((cx - 1.0, 3.0), 1.3, 1.0, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=1.0,
                         zorder=4))


def eb(c):
    ax.add_patch(Circle(c, 0.13, facecolor=P.fill(EB), edgecolor=P.edge(EB), lw=0.9, zorder=9))


def rb(c, r=0.32):
    ax.add_patch(Circle(c, r, facecolor=P.light(RB), edgecolor=P.edge(RB), lw=0.9, zorder=8))


def inclusion(c, rx, ry):
    ax.add_patch(Ellipse(c, 2 * rx, 2 * ry, facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=1.0, zorder=6))


xs = [2.6, 7.7, 12.8, 17.9, 23.0]
for x in xs[:4]:
    host(x)
# 1 entry
eb((xs[0] + 0.4, 6.65))
inclusion((xs[0] + 0.5, 5.4), 0.3, 0.3)
eb((xs[0] + 0.5, 5.4))
bio.arrow(ax, (xs[0] + 0.45, 6.45), (xs[0] + 0.5, 5.8), kind="process", color=P.muted())
# 2 EB -> RB
inclusion((xs[1] + 0.5, 5.0), 0.6, 0.55)
rb((xs[1] + 0.5, 5.0))
# 3 RB division
inclusion((xs[2] + 0.5, 4.8), 1.2, 1.05)
rng = np.random.default_rng(2)
for k in range(9):
    a, r = 2 * np.pi * k / 9, 0.62
    rb((xs[2] + 0.5 + r * np.cos(a), 4.8 + 0.82 * r * np.sin(a)), 0.26)
rb((xs[2] + 0.5, 4.8), 0.26)
# 4 conversion
inclusion((xs[3] + 0.5, 4.7), 1.5, 1.35)
for k in range(10):
    a = 2 * np.pi * k / 10
    rb((xs[3] + 0.5 + 0.95 * np.cos(a), 4.7 + 0.8 * np.sin(a)), 0.24)
for k in range(18):
    r, a = 0.6 * np.sqrt(rng.uniform()), rng.uniform(0, 2 * np.pi)
    eb((xs[3] + 0.5 + r * np.cos(a), 4.7 + r * np.sin(a)))
# 5 release
for k in range(22):
    r, a = rng.uniform(1.2, 2.6), rng.uniform(0, 2 * np.pi)
    eb((xs[4] + r * np.cos(a), 4.2 + r * np.sin(a) * 1.05))
ax.add_patch(Ellipse((xs[4], 4.2), 4.2, 4.6, fill=False, edgecolor=P.muted(), lw=1.0, ls="--", zorder=5))
for i in range(4):
    bio.arrow(ax, (xs[i] + 2.15, 4.2), (xs[i + 1] - 2.15, 4.2), kind="process", color=P.muted())
labels = [("attachment, entry", "0-2 h"), ("EB to RB", "2-8 h"), ("RB division", "8-24 h"),
          ("RB to EB", "24-48 h"), ("release", "48-72 h")]
for x, (a, b) in zip(xs, labels):
    bio.label(ax, (x, 1.25), a, size="small")
    bio.label(ax, (x, 0.75), b, size="tiny", color=P.muted())
ax.add_patch(Circle((1.0, 7.6), 0.13, facecolor=P.fill(EB), edgecolor=P.edge(EB), lw=0.9))
bio.label(ax, (1.3, 7.6), "elementary body (infectious)", size="tiny", ha="left")
ax.add_patch(Circle((7.0, 7.6), 0.22, facecolor=P.light(RB), edgecolor=P.edge(RB), lw=0.9))
bio.label(ax, (7.35, 7.6), "reticulate body (dividing)", size="tiny", ha="left")
ax.add_patch(Ellipse((12.6, 7.6), 0.6, 0.4, facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=0.9))
bio.label(ax, (13.05, 7.6), "inclusion", size="tiny", ha="left")
