"""The life cycle of a frog as the generic animal life cycle.

Stages around the cycle: gametes, zygote, 8-cell embryo (cleavage), blastula (section: blastocoel in the
animal half), gastrula (section: the three germ layers, ectoderm blue, mesoderm red, endoderm yellow,
around the archenteron, with the blastopore), neurula (cross-section: neural tube, notochord, somites,
gut), tadpole (larva), and adult. The arrows name the processes between stages. Germ cells are set aside
early and complete gametogenesis in the adult.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch, Wedge
from matplotlib.path import Path

import wikibio as bio
from wikibio import gametes as gam

P = bio.P
fig, ax = bio.canvas(24, 16)
C = (12.0, 8.2)
RX, RY = 8.6, 5.6
GERM = {"ecto": "ectoderm", "meso": "mesoderm", "endo": "endoderm"}


def pos(angle):
    a = math.radians(angle)
    return (C[0] + RX * math.cos(a), C[1] + RY * math.sin(a))


def yolky_egg(c, r, cells=None):
    """An amphibian egg/embryo: pigmented animal half, pale yolky vegetal half."""
    ax.add_patch(Wedge(c, r, 0, 180, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1.0, zorder=5))
    ax.add_patch(Wedge(c, r, 180, 360, facecolor=P.light("lipid"), edgecolor=P.edge("animal"), lw=1.0, zorder=5))


ANG = {"gametes": 90, "zygote": 47, "cleavage": 12, "blastula": -25, "gastrula": -62, "neurula": -118,
       "tadpole": 180 + 22, "adult": 180 - 35}

# gametes
gx, gy = pos(ANG["gametes"])
gam.egg(ax, (gx - 0.4, gy), 0.62, kind="urchin", granules=False, nucleus=False, polar_bodies=0)
ax.add_patch(Wedge((gx - 0.4, gy), 0.62, 0, 180, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1.0, zorder=8))
gam.sperm(ax, (gx + 0.45, gy + 0.1), angle=180, length=1.9, kind="mammal", wave=0.05)
bio.label(ax, (gx, gy - 1.05), "Gametes", size="small", bold=True)

# zygote
zx, zy = pos(ANG["zygote"])
yolky_egg((zx, zy), 0.75)
ax.add_patch(Circle((zx - 0.05, zy + 0.38), 0.12, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.8, zorder=7))
bio.label(ax, (zx, zy - 1.1), "Zygote", size="small", bold=True)

# 8-cell (cleavage): unequal third cleavage, small animal cells
cx, cy = pos(ANG["cleavage"])
r = 0.78
yolky_egg((cx, cy), r)
ax.plot([cx - r, cx + r], [cy + 0.18, cy + 0.18], color=P.edge("animal"), lw=0.9, zorder=6)
ax.plot([cx, cx], [cy - r, cy + r], color=P.edge("animal"), lw=0.9, zorder=6)
ax.plot([cx - 0.42, cx + 0.42], [cy + 0.62, cy - 0.62], color=P.edge("animal"), lw=0.6, zorder=6, alpha=0.6)
bio.label(ax, (cx, cy - 1.15), "8-cell embryo", size="small", bold=True)

# blastula (section)
bx, by = pos(ANG["blastula"])
r = 0.85
yolky_egg((bx, by), r)
ax.add_patch(Ellipse((bx, by + 0.28), 0.95, 0.55, facecolor=P.fill("vacuole"), edgecolor=P.edge("animal"), lw=0.8, zorder=6))
bio.label(ax, (bx, by - 1.2), "Blastula", size="small", bold=True)
bio.callout(ax, (bx + 0.3, by + 0.3), (bx + 1.5, by + 1.25), "blastocoel", size="tiny")

# gastrula (section): ectoderm outside, mesoderm in the middle, endoderm lining the archenteron
gx2, gy2 = pos(ANG["gastrula"])
r = 0.9
ax.add_patch(Circle((gx2, gy2), r, facecolor=P.fill(GERM["ecto"]), edgecolor=P.edge(GERM["ecto"]), lw=1.0, zorder=5))
ax.add_patch(Circle((gx2, gy2), r * 0.82, facecolor=P.fill(GERM["meso"]), edgecolor=P.edge(GERM["meso"]), lw=0.8, zorder=5.1))
ax.add_patch(Circle((gx2 - 0.06, gy2 - 0.05), r * 0.62, facecolor=P.fill(GERM["endo"]), edgecolor=P.edge(GERM["endo"]), lw=0.8, zorder=5.2))
ax.add_patch(Ellipse((gx2 + 0.12, gy2 + 0.05), 0.95, 0.32, angle=15, facecolor=P.fill("vacuole"), edgecolor=P.edge(GERM["endo"]),
                     lw=0.7, zorder=5.3))
ax.add_patch(Circle((gx2 + 0.62, gy2 - 0.08), 0.1, facecolor=P.surface(), edgecolor=P.edge(GERM["ecto"]), lw=0.8, zorder=5.4))
bio.label(ax, (gx2, gy2 - 1.25), "Gastrula", size="small", bold=True)
bio.callout(ax, (gx2 + 0.66, gy2 - 0.08), (gx2 + 1.75, gy2 - 0.7), "blastopore", size="tiny")

# neurula cross-section
nx, ny = pos(ANG["neurula"])
ax.add_patch(Ellipse((nx, ny), 2.1, 1.6, facecolor=P.fill(GERM["ecto"]), edgecolor=P.edge(GERM["ecto"]), lw=1.0, zorder=5))
ax.add_patch(Ellipse((nx, ny - 0.05), 1.85, 1.35, facecolor=P.fill(GERM["meso"]), edgecolor=P.edge(GERM["meso"]), lw=0.8, zorder=5.1))
ax.add_patch(Ellipse((nx, ny - 0.3), 1.2, 0.7, facecolor=P.fill(GERM["endo"]), edgecolor=P.edge(GERM["endo"]), lw=0.8, zorder=5.2))
ax.add_patch(Ellipse((nx, ny - 0.3), 0.6, 0.26, facecolor=P.fill("vacuole"), edgecolor=P.edge(GERM["endo"]), lw=0.6, zorder=5.3))
ax.add_patch(Circle((nx, ny + 0.5), 0.28, facecolor=P.fill(GERM["ecto"]), edgecolor=P.edge(GERM["ecto"]), lw=0.9, zorder=5.4))
ax.add_patch(Circle((nx, ny + 0.5), 0.08, facecolor=P.fill("vacuole"), edgecolor=P.edge(GERM["ecto"]), lw=0.6, zorder=5.5))
ax.add_patch(Circle((nx, ny + 0.1), 0.13, facecolor=P.edge(GERM["meso"]), edgecolor=P.edge(GERM["meso"]), lw=0.6, zorder=5.4))
for s in (-1, 1):
    ax.add_patch(Ellipse((nx + s * 0.5, ny + 0.3), 0.34, 0.45, facecolor=P.edge(GERM["meso"]), edgecolor=P.edge(GERM["meso"]),
                         lw=0.6, zorder=5.4))
bio.label(ax, (nx, ny - 1.15), "Neurula (cross-section)", size="small", bold=True)
bio.callout(ax, (nx + 0.2, ny + 0.62), (nx + 1.7, ny + 1.3), "neural tube", size="tiny")
bio.callout(ax, (nx + 0.1, ny + 0.1), (nx + 1.85, ny + 0.5), "notochord", size="tiny")
bio.callout(ax, (nx - 0.55, ny + 0.32), (nx - 1.9, ny + 1.0), "somite", size="tiny")

# tadpole (native outline): oval body and tapering tail fin
tx, ty = pos(ANG["tadpole"])
body = bio.blob((tx - 0.55, ty), 0.62, 0.44, wobble=0.02, seed=3, k=10)
ax.add_patch(PathPatch(Path(body, closed=True), facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1.0, zorder=6))
t = np.linspace(0, 1, 50)
top = np.c_[tx - 0.1 + 1.8 * t, ty + 0.05 + 0.32 * (1 - t) * np.sin(np.pi * (0.25 + 0.75 * t)) + 0.05 * np.sin(5 * t)]
bot = np.c_[tx - 0.1 + 1.8 * t, ty - 0.05 - 0.26 * (1 - t) * np.sin(np.pi * (0.25 + 0.75 * t)) + 0.05 * np.sin(5 * t)]
fin = np.vstack([top, bot[::-1]])
ax.add_patch(PathPatch(Path(fin, closed=True), facecolor=P.light("animal"), edgecolor=P.edge("animal"), lw=0.9, zorder=5.8))
ax.add_patch(Circle((tx - 0.85, ty + 0.12), 0.07, facecolor=P.ink(), edgecolor="none", zorder=7))
bio.label(ax, (tx + 0.2, ty - 0.9), "Tadpole (larva)", size="small", bold=True)

# adult
ax_, ay_ = pos(ANG["adult"])
bio.icon(ax, "phylopic/xenopus", at=(ax_, ay_), height=1.9, color="animal")
bio.label(ax, (ax_, ay_ - 1.35), "Adult", size="small", bold=True)

# arrows along the ellipse between stages with process names
order = ["gametes", "zygote", "cleavage", "blastula", "gastrula", "neurula", "tadpole", "adult"]
procs = ["Fertilization", "Cleavage", "Blastulation", "Gastrulation", "Neurulation,\norganogenesis", "Hatching,\nlarval growth",
         "Metamorphosis", "Gametogenesis"]
for k, (a, b) in enumerate(zip(order, order[1:] + order[:1])):
    a0, a1 = ANG[a], ANG[b]
    if a1 > a0:
        a1 -= 360
    da = a0 - a1
    s0, s1 = a0 - da * 0.24, a1 + da * 0.24
    th = np.radians(np.linspace(s0, s1, 40))
    pts = np.c_[C[0] + (RX - 0.2) * np.cos(th), C[1] + (RY - 0.2) * np.sin(th)]
    ax.plot(pts[:-2, 0], pts[:-2, 1], color=P.muted(), lw=1.3, zorder=3)
    bio.arrow(ax, pts[-4], pts[-1], kind="process", color=P.muted(), head=0.24)
    mid = np.radians((s0 + s1) / 2)
    lx, ly = C[0] + (RX - 1.65) * math.cos(mid), C[1] + (RY - 1.25) * math.sin(mid)
    bio.label(ax, (lx, ly), procs[k], size="small", color=P.ink())

bio.label(ax, C, "Embryogenesis:\nfertilization to hatching", size="small", color=P.muted())
bio.label(ax, (C[0], C[1] - 0.95), "Germ cells set aside early,\ngametes mature in the adult", size="tiny", color=P.muted())
