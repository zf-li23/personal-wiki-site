"""Five widespread types of marine invertebrate larva (schematic, not to scale; ciliary bands in green,
gut in yellow, apical organ or eye in dark).

Planula (cnidarians): a ciliated, solid or hollow two-layered larva without a mouth in most species, swimming
with its aboral pole forward. Trochophore (annelids, many molluscs): a top-shaped larva with an apical
organ and ciliary tuft, a preoral girdle of compound cilia (the prototroch) above the mouth, often a
metatroch below it, a complete gut ending in the anus, and a pair of protonephridia. Veliger (gastropods
and bivalves): a later molluscan larva with a shell, a foot and a velum, two ciliated lobes derived from the
prototroch. Nauplius (crustaceans): an unsegmented larva with three pairs of appendages (first antennae,
second antennae, mandibles) and a median naupliar eye, swimming with its limbs. Dipleurula (the generalized
deuterostome larva of echinoderms and hemichordates): bilateral, with a single looped ciliary band around
the mouth field, a through gut with the anus near the posterior end and an apical plate.
"""

import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, Polygon, Circle

P = bio.P
fig, ax = bio.canvas(29.0, 9.0)
BODY, CIL, GUT = "cytoplasm", "positive", "endoderm"


def oval(c, rx, ry, tok=BODY, z=5, angle=0):
    ax.add_patch(Ellipse(c, 2 * rx, 2 * ry, angle=angle, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.2, zorder=z))


def cilia(c, rx, ry, n=40, length=0.2, a0=0, a1=360):
    for t in np.radians(np.linspace(a0, a1, n)):
        x, y = c[0] + rx * np.cos(t), c[1] + ry * np.sin(t)
        nx, ny = np.cos(t) / rx, np.sin(t) / ry
        L = np.hypot(nx, ny)
        ax.plot([x, x + length * nx / L], [y, y + length * ny / L], color=P.edge(CIL), lw=0.8, zorder=6)


def band(x0, x1, y, lw=5):
    ax.plot([x0, x1], [y, y], color=P.fill(CIL), lw=lw, solid_capstyle="round", zorder=9)
    for x in np.linspace(x0, x1, 12):
        ax.plot([x, x - 0.05], [y, y + 0.35], color=P.edge(CIL), lw=0.8, zorder=9)
        ax.plot([x, x - 0.05], [y, y - 0.35], color=P.edge(CIL), lw=0.8, zorder=9)


X = [2.8, 8.4, 14.4, 20.4, 26.0]
Y = 4.6
# planula
oval((X[0], Y), 1.0, 1.7, "ectoderm")
oval((X[0], Y), 0.55, 1.2, "endoderm", z=6)
cilia((X[0], Y), 1.0, 1.7)
bio.label(ax, (X[0], 8.3), "Planula", size="small", bold=True)
bio.label(ax, (X[0], 0.6), "Cnidaria", size="tiny", color=P.muted())
bio.callout(ax, (X[0] + 0.3, Y - 0.6), (X[0] - 1.6, Y - 2.8), "Endoderm", size="tiny")

# trochophore
oval((X[1], Y), 1.8, 1.9)
ax.plot([X[1], X[1]], [Y + 1.9, Y + 2.6], color=P.ink(), lw=1.0, zorder=8)
for dx in (-0.12, 0, 0.12):
    ax.plot([X[1], X[1] + dx * 3], [Y + 1.9, Y + 2.6], color=P.ink(), lw=0.8, zorder=8)
ax.add_patch(Circle((X[1], Y + 1.75), 0.16, facecolor=P.ink(), zorder=9))
band(X[1] - 1.8, X[1] + 1.8, Y + 0.3)
band(X[1] - 1.5, X[1] + 1.5, Y - 0.8, lw=3)
gut = [(X[1] - 1.75, Y - 0.25), (X[1] - 0.6, Y - 0.2), (X[1] - 0.2, Y - 0.5), (X[1] + 0.1, Y - 1.2), (X[1] + 0.05, Y - 1.9)]
ax.plot(*zip(*gut), color=P.edge(GUT), lw=7, solid_capstyle="round", zorder=7)
ax.plot(*zip(*gut), color=P.fill(GUT), lw=5, solid_capstyle="round", zorder=7.5)
bio.label(ax, (X[1], 8.3), "Trochophore", size="small", bold=True)
bio.label(ax, (X[1], 0.6), "Annelida, Mollusca", size="tiny", color=P.muted())
bio.callout(ax, (X[1], Y + 2.4), (X[1] + 2.0, Y + 3.1), "Apical tuft", size="tiny")
bio.callout(ax, (X[1] + 1.6, Y + 0.3), (X[1] + 2.4, Y + 1.6), "Prototroch", size="tiny")
bio.callout(ax, (X[1] - 1.75, Y - 0.25), (X[1] - 2.2, Y + 1.9), "Mouth", size="tiny")
bio.callout(ax, (X[1] + 0.05, Y - 1.85), (X[1] + 1.6, Y - 3.0), "Anus", size="tiny")

# veliger
ax.add_patch(Polygon([(X[2] - 1.2, Y - 1.8), (X[2] + 1.2, Y - 1.8), (X[2] + 1.0, Y - 0.2), (X[2] - 1.0, Y - 0.2)],
                     closed=True, facecolor=P.fill("lipid_tail"), edgecolor=P.edge("lipid_tail"), lw=1.2, zorder=5))
for s in (-1, 1):
    oval((X[2] + s * 1.1, Y + 0.9), 1.15, 0.65, BODY, z=6, angle=s * 15)
    cilia((X[2] + s * 1.1, Y + 0.9), 1.15, 0.65, n=24, a0=0 if s > 0 else 90, a1=180 if s > 0 else 270)
oval((X[2], Y - 2.2), 0.5, 0.35, BODY, z=6)
bio.label(ax, (X[2], 8.3), "Veliger", size="small", bold=True)
bio.label(ax, (X[2], 0.6), "Gastropoda, Bivalvia", size="tiny", color=P.muted())
bio.callout(ax, (X[2] + 1.9, Y + 1.0), (X[2] + 2.6, Y + 2.6), "Velum", size="tiny")
bio.callout(ax, (X[2] - 0.8, Y - 1.2), (X[2] - 2.6, Y - 2.6), "Shell", size="tiny")
bio.callout(ax, (X[2], Y - 2.4), (X[2] + 1.6, Y - 3.2), "Foot", size="tiny")

# nauplius
oval((X[3], Y), 1.3, 1.6, "atp")
ax.add_patch(Circle((X[3], Y + 1.1), 0.18, facecolor=P.ink(), zorder=9))
for k, (y0, L, ang) in enumerate(((Y + 0.8, 2.2, 25), (Y + 0.1, 2.6, 0), (Y - 0.6, 1.8, -25))):
    for s in (-1, 1):
        a = np.radians(ang)
        x1, y1 = X[3] + s * (1.1 + L * np.cos(a)), y0 + L * np.sin(a)
        ax.plot([X[3] + s * 1.1, x1], [y0, y1], color=P.edge("atp"), lw=3.0 if k else 2.0, solid_capstyle="round", zorder=6)
        if k:
            for j in range(4):
                xb = X[3] + s * (1.4 + 0.3 * j) ; yb = y0 + (xb - X[3] - s * 1.1) * np.tan(a) * s
                ax.plot([xb, xb + s * 0.2], [yb, yb - 0.35], color=P.edge("atp"), lw=0.8, zorder=6)
bio.label(ax, (X[3], 8.3), "Nauplius", size="small", bold=True)
bio.label(ax, (X[3], 0.6), "Crustacea", size="tiny", color=P.muted())
bio.callout(ax, (X[3], Y + 1.1), (X[3] + 0.4, Y + 3.1), "Naupliar eye", size="tiny")
bio.label(ax, (X[3], Y - 2.2), "3 pairs of limbs", size="tiny")

# dipleurula
oval((X[4], Y), 1.5, 2.0)
loop = [(X[4] - 1.2, Y + 1.2), (X[4] - 0.5, Y + 1.5), (X[4] + 0.6, Y + 1.4), (X[4] + 1.2, Y + 0.6), (X[4] + 1.15, Y - 0.8),
        (X[4] + 0.4, Y - 1.2), (X[4] - 0.3, Y - 0.5), (X[4] - 1.1, Y - 0.9), (X[4] - 1.3, Y + 0.2), (X[4] - 1.2, Y + 1.2)]
ax.plot(*zip(*loop), color=P.fill(CIL), lw=5, solid_capstyle="round", zorder=8)
ax.plot(*zip(*loop), color=P.edge(CIL), lw=1.0, ls=(0, (1, 1.5)), zorder=8.5)
gut2 = [(X[4] - 0.3, Y + 0.4), (X[4] + 0.1, Y - 0.2), (X[4] + 0.2, Y - 1.0), (X[4] + 0.1, Y - 1.95)]
ax.plot(*zip(*gut2), color=P.edge(GUT), lw=7, solid_capstyle="round", zorder=7)
ax.plot(*zip(*gut2), color=P.fill(GUT), lw=5, solid_capstyle="round", zorder=7.5)
bio.label(ax, (X[4], 8.3), "Dipleurula", size="small", bold=True)
bio.label(ax, (X[4], 0.6), "Echinodermata, Hemichordata", size="tiny", color=P.muted())
bio.callout(ax, (X[4] + 1.2, Y + 0.6), (X[4] + 2.2, Y + 2.6), "Ciliary band", size="tiny")
bio.callout(ax, (X[4] - 0.3, Y + 0.4), (X[4] - 2.4, Y + 2.6), "Mouth", size="tiny")
bio.callout(ax, (X[4] + 0.1, Y - 1.95), (X[4] + 1.8, Y - 3.0), "Anus", size="tiny")
