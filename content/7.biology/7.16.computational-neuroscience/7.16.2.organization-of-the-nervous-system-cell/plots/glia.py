"""The four main classes of glial cells (schematic, not to scale). A: an astrocyte whose
processes end on a capillary (endfeet) and ensheath a synapse (tripartite synapse). B: an
oligodendrocyte in the CNS myelinating segments of several axons, with nodes of Ranvier between
sheaths. C: a myelinating Schwann cell in a peripheral nerve wraps one segment of one axon.
D: a microglial cell with fine ramified processes that survey the neuropil."""

import numpy as np
import wikibio as bio

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(20, 8.4)
rng = np.random.default_rng(3)


def process(a, b, tok, lw=2.2, bend=0.15):
    a, b = np.asarray(a, float), np.asarray(b, float)
    m = (a + b) / 2 + bend * np.array([-(b - a)[1], (b - a)[0]])
    s = np.linspace(0, 1, 40)[:, None]
    pts = (1 - s) ** 2 * a + 2 * (1 - s) * s * m + s ** 2 * b
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok), lw=lw, solid_capstyle="round", zorder=6)
    return pts


# A astrocyte
cap_y = 1.4
from matplotlib.patches import FancyBboxPatch, Circle, Ellipse
ax.add_patch(FancyBboxPatch((0.4, cap_y - 0.45), 4.6, 0.9, boxstyle="round,pad=0,rounding_size=0.4",
             facecolor=P.fill("blood"), edgecolor=P.edge("blood"), lw=1.0, zorder=3))
astro = (2.7, 4.4)
for k in range(9):
    ang = 2 * np.pi * k / 9 + 0.3
    end = astro + np.array([np.cos(ang), np.sin(ang)]) * rng.uniform(1.3, 1.9)
    process(astro, end, "vesicle", lw=2.0, bend=rng.uniform(-0.2, 0.2))
for x in (1.6, 2.7, 3.8):  # endfeet on the capillary
    process(astro, (x, cap_y + 0.5), "vesicle", lw=2.6, bend=0.05)
    ax.add_patch(Ellipse((x, cap_y + 0.5), 0.7, 0.22, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.9, zorder=7))
bio.shape(ax, bio.blob(astro, 0.55, 0.5, seed=2), token="vesicle", zorder=8)
syn = np.array([4.2, 6.4])
process(astro, syn - (0.2, 0.25), "vesicle", lw=2.6)
ax.add_patch(Circle(syn + (0, 0.25), 0.28, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.9, zorder=9))
ax.add_patch(Ellipse(syn - (0, 0.22), 0.6, 0.3, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.9, zorder=9))
bio.callout(ax, syn + (0.3, 0.2), (5.3, 7.4), "synapse", size="tiny")
bio.callout(ax, (4.6, cap_y), (5.0, 0.4), "capillary", size="tiny")
bio.callout(ax, (3.8, cap_y + 0.55), (4.7, 2.6), "endfoot", size="tiny")
bio.label(ax, (2.7, 7.9), "A  Astrocyte", size="small", bold=True)

# B oligodendrocyte
ol = np.array([9.0, 4.4])
axon_y = [6.6, 4.4, 2.2]
for y in axon_y:
    ax.plot([6.3, 11.8], [y - 0.9 if y != 4.4 else y - 1.4, y - 0.9 if y != 4.4 else y - 1.4], color=P.edge("neuron"), lw=2.2, zorder=4)
targets = [(7.2, 5.7), (10.6, 5.7), (8.0, 3.0), (10.4, 3.0), (7.6, 1.3), (10.2, 1.3)]
for tx, ty in targets:
    process(ol, (tx, ty + 0.18), "lipid", lw=1.6, bend=0.1)
    ax.add_patch(FancyBboxPatch((tx - 0.75, ty - 0.2), 1.5, 0.4, boxstyle="round,pad=0,rounding_size=0.18",
                 facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.9, zorder=7))
bio.shape(ax, bio.blob(ol, 0.5, 0.45, seed=5), token="lipid", zorder=8)
bio.callout(ax, (9.2, 3.0), (9.2, 0.35), "node of Ranvier", size="tiny")
bio.callout(ax, (10.6, 5.9), (11.4, 7.3), "myelin sheath", size="tiny")
bio.label(ax, (9.0, 7.9), "B  Oligodendrocyte (CNS)", size="small", bold=True)

# C Schwann cell
y = 4.2
ax.plot([12.6, 16.6], [y, y], color=P.edge("neuron"), lw=2.2, zorder=4)
for x0 in (12.75, 14.75):
    ax.add_patch(FancyBboxPatch((x0, y - 0.32), 1.7, 0.64, boxstyle="round,pad=0,rounding_size=0.3",
                 facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.9, zorder=6))
    ax.add_patch(Ellipse((x0 + 0.85, y + 0.42), 0.7, 0.32, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.8, zorder=7))
# cross-section: concentric wraps
c = np.array([14.6, 1.8])
for r in np.linspace(0.9, 0.45, 6):
    ax.add_patch(Circle(c, r, facecolor="none", edgecolor=P.edge("lipid"), lw=0.9, zorder=6))
ax.add_patch(Circle(c, 0.38, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.9, zorder=7))
bio.callout(ax, (c[0] + 0.9, c[1]), (16.6, 1.0), "cross section:\ncompact wraps", size="tiny")
bio.callout(ax, (14.6, y), (14.6, 6.3), "node", size="tiny")
bio.label(ax, (14.6, 7.9), "C  Schwann cells (PNS)", size="small", bold=True)

# D microglia
mg = np.array([18.4, 4.4])
def ramify(p, ang, L, depth):
    if depth == 0:
        return
    q = p + L * np.array([np.cos(ang), np.sin(ang)])
    ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge("bacterium"), lw=0.6 + 0.5 * depth, zorder=6, solid_capstyle="round")
    for d in (-0.5, 0.5):
        ramify(q, ang + d + rng.uniform(-0.2, 0.2), L * 0.62, depth - 1)
for k in range(5):
    ramify(mg, 2 * np.pi * k / 5 + 0.4, 0.8, 3)
bio.shape(ax, bio.blob(mg, 0.4, 0.3, seed=8), token="bacterium", zorder=8)
bio.label(ax, (18.4, 7.9), "D  Microglia", size="small", bold=True)
