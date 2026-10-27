"""Cohesin and the life cycle of sister-chromatid cohesion in mitosis (schematic).

(A) Cohesin is a ring of about 50 nm made of two SMC proteins (Smc1 and Smc3), each a long antiparallel coiled
coil with a hinge at one end and an ATPase head at the other, closed by the kleisin Scc1 (Rad21) that bridges
the two heads and binds SA1/SA2 (Scc3). Cohesive cohesin entraps the two sister DNAs; separase cuts Scc1.
Condensin has the same architecture (Smc2, Smc4 and the kleisin CAP-H or CAP-H2) and compacts chromatids by
loop extrusion.
(B) The cycle of cohesion. G1: cohesin is loaded by the Scc2-Scc4 loader and released again by Wapl (dynamic).
S: as the replication fork passes, cohesin comes to embrace both sisters and Eco1/Esco acetylates Smc3;
sororin counteracts Wapl, so cohesion is stable. Prophase: Plk1 and Aurora B phosphorylate SA2 and sororin
and Wapl opens the Smc3-Scc1 gate, removing cohesin from the arms (the prophase pathway); at centromeres
shugoshin (Sgo1) with PP2A-B56 keeps cohesin dephosphorylated and protected. Metaphase: sisters are joined
mainly at their centromeres. Anaphase: separase, released when APC/C-Cdc20 destroys securin, cleaves Scc1 of
the remaining cohesin, and the sisters separate.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, PathPatch
from matplotlib.path import Path

import wikibio as bio

P = bio.P
FT = bio.core.FONT

fig, ax = bio.canvas(27.0, 11.5)

# ----- A: the cohesin ring
bio.panel(ax, "A", (0.2, 11.3))
cx, cy = 3.6, 6.2
hinge = np.array([cx, cy + 3.3])
heads = [np.array([cx - 1.2, cy - 1.0]), np.array([cx + 1.2, cy - 1.0])]
for hd, tok, name in ((heads[0], "channel", "Smc1"), (heads[1], "enzyme", "Smc3")):
    mid = (hinge + hd) / 2 + np.array([1.0 if hd[0] < cx else -1.0, 0]) * -0.35
    t = np.linspace(0, 1, 40)[:, None]
    curve = (1 - t) ** 2 * hinge + 2 * (1 - t) * t * mid + t ** 2 * hd
    ax.plot(curve[:, 0], curve[:, 1], color=P.edge(tok), lw=6.0, solid_capstyle="round", zorder=5)
    ax.plot(curve[:, 0], curve[:, 1], color=P.fill(tok), lw=4.2, solid_capstyle="round", zorder=5.1)
    ax.add_patch(Ellipse(hd, 1.0, 0.75, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.1, zorder=6))
    bio.label(ax, hd + np.array([0, 0.0]), name, size="tiny", bold=True, color=P.on_fill(), zorder=7)
ax.add_patch(Circle(hinge, 0.35, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=1.0, zorder=6))
bio.callout(ax, hinge + np.array([0.3, 0.15]), (cx + 1.6, cy + 3.9), "hinge", size="tiny")
# kleisin bridging the heads
k = np.array([[heads[0][0] + 0.3, heads[0][1] - 0.3], [cx, cy - 2.1], [heads[1][0] - 0.3, heads[1][1] - 0.3]])
t = np.linspace(0, 1, 40)[:, None]
kc = (1 - t) ** 2 * k[0] + 2 * (1 - t) * t * k[1] + t ** 2 * k[2]
ax.plot(kc[:, 0], kc[:, 1], color=P.edge("negative"), lw=4.0, solid_capstyle="round", zorder=5)
bio.label(ax, (cx, cy - 2.05), "Scc1 (Rad21)", size="tiny", color=P.edge("negative"), bold=True)
bio.protein(ax, (cx + 1.95, cy - 2.15), 1.4, 0.7, token="positive", text="SA1/2", size="tiny", zorder=6)
# scissors mark of separase
bio.callout(ax, (cx - 0.55, cy - 1.75), (cx - 2.6, cy - 2.9), "separase cuts here", size="tiny")
# sister DNAs (cross-sections of chromatin fibers)
for dx in (-0.4, 0.4):
    ax.add_patch(Circle((cx + dx, cy + 0.6), 0.36, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=1.0, zorder=4))
bio.label(ax, (cx, cy + 0.6 - 0.65), "sister chromatids", size="tiny", color=P.muted())
bio.label(ax, (cx, 1.1), "cohesin entraps two sister DNAs\n(about 50 nm ring)", size="tiny")

# ----- B: cohesion through the cycle
bio.panel(ax, "B", (8.6, 11.3))
stages = ["G1", "S → G2", "prophase", "metaphase", "anaphase"]
xs = np.linspace(10.6, 25.0, 5)
yb = 6.0
L = 3.4


def chromatid(x, y, dx=0.0, bend=0.0, tok="dna", lw=7.0, half=None):
    t = np.linspace(-1, 1, 40)
    xx = x + dx + bend * t ** 2
    yy = y + t * L / 2
    if half == "top":
        mask = t <= 0.05
    elif half == "bottom":
        mask = t >= -0.05
    else:
        mask = np.ones_like(t, bool)
    ax.plot(xx, yy, color=P.edge(tok), lw=lw, solid_capstyle="round", zorder=5)
    ax.plot(xx, yy, color=P.fill(tok), lw=lw - 2.0, solid_capstyle="round", zorder=5.1)


def ring(x, y, tok="enzyme", protected=False):
    ax.add_patch(Ellipse((x, y), 0.95, 0.28, facecolor="none", edgecolor=P.edge(tok), lw=1.8, zorder=7))
    if protected:
        ax.add_patch(Circle((x + 0.6, y), 0.13, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=8))


for i, (x, name) in enumerate(zip(xs, stages)):
    bio.label(ax, (x, 10.4), name, size="small", bold=True)
    if i == 0:
        chromatid(x, yb, lw=8)
        for y in np.linspace(yb - 1.4, yb + 1.4, 5):
            ring(x, y, tok="neutral")
        note = "loaded by Scc2–Scc4,\nreleased by Wapl"
    elif i == 1:
        chromatid(x, yb, dx=-0.18)
        chromatid(x, yb, dx=0.18, tok="dna2")
        for y in np.linspace(yb - 1.4, yb + 1.4, 5):
            ring(x, y)
        note = "cohesion established;\nSmc3 acetylated, sororin"
    elif i == 2:
        chromatid(x, yb, dx=-0.32, bend=-0.35)
        chromatid(x, yb, dx=0.32, bend=0.35, tok="dna2")
        ring(x, yb, protected=True)
        ring(x, yb - 1.1)
        for y in (yb + 1.3, yb - 1.9):
            ax.add_patch(Ellipse((x + (0.95 if y > yb else -0.95), y), 0.6, 0.18, facecolor="none",
                                 edgecolor=P.edge("enzyme"), lw=1.4, ls=(0, (2, 1.5)), zorder=7))
        note = "prophase pathway (Plk1,\nWapl) clears the arms;\nSgo1–PP2A protects\nthe centromere"
    elif i == 3:
        chromatid(x, yb, dx=-0.42, bend=-0.5)
        chromatid(x, yb, dx=0.42, bend=0.5, tok="dna2")
        ring(x, yb, protected=True)
        for s in (-1, 1):
            ax.plot([x + s * 0.5, x + s * 1.2], [yb, yb], color=P.edge("channel"), lw=1.3, zorder=4)
        note = "joined at the\ncentromere; tension"
    else:
        chromatid(x - 0.75, yb, bend=0.35)
        chromatid(x + 0.75, yb, bend=-0.35, tok="dna2")
        for s in (-1, 1):
            bio.arrow(ax, (x + s * 1.0, yb - 2.1), (x + s * 1.8, yb - 2.1), kind="process")
        # cleaved kleisin fragments
        for dy in (-0.15, 0.15):
            ax.plot([x - 0.15, x + 0.15], [yb + dy, yb - dy], color=P.edge("negative"), lw=1.2, zorder=6)
        note = "separase cleaves\nScc1; sisters part"
    bio.label(ax, (x, 2.9), note, size="tiny", color=P.muted(), va="top")
    if i < 4:
        bio.arrow(ax, (x + 1.2, 8.3), (xs[i + 1] - 1.2, 8.3), kind="process", color=P.muted())

# legend
lx = 10.0
ax.add_patch(Ellipse((lx, 0.75), 0.7, 0.22, facecolor="none", edgecolor=P.edge("enzyme"), lw=1.8, zorder=7))
bio.label(ax, (lx + 0.55, 0.75), "cohesive cohesin", size="tiny", ha="left")
ax.add_patch(Ellipse((lx + 4.6, 0.75), 0.7, 0.22, facecolor="none", edgecolor=P.edge("neutral"), lw=1.8, zorder=7))
bio.label(ax, (lx + 5.15, 0.75), "dynamic (G1) cohesin", size="tiny", ha="left")
ax.add_patch(Circle((lx + 10.0, 0.75), 0.13, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8))
bio.label(ax, (lx + 10.3, 0.75), "shugoshin–PP2A", size="tiny", ha="left")
