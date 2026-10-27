"""The erythrocyte membrane skeleton (schematic).

A: the network seen from the cytoplasm: junctional complexes (short actin filaments with protein 4.1)
at the nodes of a roughly triangular lattice, spectrin tetramers between neighboring nodes (alpha-beta
heterodimers joined head to head at the small dot in the middle), and ankyrin-band 3 complexes bound
near the middle of each tetramer.
B: side view of the vertical linkages: band 3 dimers in the bilayer bind ankyrin, which binds
beta-spectrin; glycophorin C binds protein 4.1 at a junctional complex.
"""

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch
import wikibio as bio
from wikibio.structures import actin

P = bio.P
fig, ax = bio.canvas(25.0, 9.4)
rng = np.random.default_rng(3)

# ---- A: top view
bio.panel(ax, "A", (0.1, 9.2))
bio.label(ax, (6.0, 9.0), "Network seen from the cytoplasm", size="normal", bold=True)
s = 2.6
nodes = {}
for i in range(-1, 5):
    for j in range(-1, 4):
        x = 1.2 + i * s + (j % 2) * s / 2 + rng.normal(0, 0.12)
        y = 1.3 + j * s * 0.866 + rng.normal(0, 0.12)
        nodes[(i, j)] = np.array([x, y])
inside = lambda p: 0.4 < p[0] < 11.6 and 0.5 < p[1] < 8.4


def wavy(a, b, amp=0.12, waves=3.5, tok="protein", lw=2.2):
    t = np.linspace(0, 1, 80)
    d = b - a
    nrm = np.array([-d[1], d[0]]) / np.linalg.norm(d)
    pts = a + np.outer(t, d) + np.outer(amp * np.sin(2 * np.pi * waves * t), nrm)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok), lw=lw, solid_capstyle="round", zorder=6)
    ax.plot(pts[:, 0], pts[:, 1], color=P.fill(tok), lw=lw * 0.45, solid_capstyle="round", zorder=6.1)


edges = []
for (i, j), p in nodes.items():
    nb = [(i + 1, j), (i + (j % 2), j + 1), (i + (j % 2) - 1, j + 1)]
    for q in nb:
        if q in nodes:
            edges.append((p, nodes[q]))
for a, b in edges:
    if inside(a) and inside(b):
        wavy(a, b)
        m = (a + b) / 2
        ax.add_patch(Circle(m, 0.07, color=P.edge("protein"), zorder=7))
        k = a + (b - a) * 0.38
        bio.protein(ax, k + np.array([0.0, 0.18]), 0.34, 0.26, "enzyme", wobble=0.05, text=None)
for p in nodes.values():
    if inside(p):
        actin(ax, p - np.array([0.33, 0.0]), p + np.array([0.33, 0.0]), r=0.07)
        bio.protein(ax, p + np.array([0.0, -0.26]), 0.3, 0.22, "antibody", wobble=0.05)

# legend
lx, ly = 13.0, 8.3
def key(y, draw, text):
    draw(np.array([lx, y]))
    bio.label(ax, (lx + 0.6, y), text, size="small", ha="left")
key(ly, lambda p: wavy(p - [0.35, 0], p + [0.35, 0], waves=1.5), "spectrin tetramer (αβ)₂")
key(ly - 0.65, lambda p: actin(ax, p - [0.3, 0], p + [0.3, 0], r=0.07), "actin (junctional complex)")
key(ly - 1.3, lambda p: bio.protein(ax, p, 0.3, 0.22, "antibody", wobble=0.05), "protein 4.1")
key(ly - 1.95, lambda p: bio.protein(ax, p, 0.34, 0.26, "enzyme", wobble=0.05), "ankyrin–band 3")

# ---- B: side view
bio.panel(ax, "B", (12.6, 5.6))
y = 3.2
x0, x1 = 12.9, 24.8
from wikibio import cellbio as CB
CB.sides(ax, (x0, x1), y, height=(1.5, 2.3), top="Outside", bottom="Cytoplasm")
bio.bilayer(ax, [(x0, y), (x1, y)])
MH = CB.MH
# band 3 dimer
for dx in (-0.32, 0.32):
    bio.protein(ax, (15.6 + dx, y), 0.6, 1.25, "channel", wobble=0.05, text=None)
bio.label(ax, (15.6, y + 1.1), "band 3 dimer", size="small")
bio.protein(ax, (15.9, y - 1.05), 1.3, 0.7, "enzyme", wobble=0.07, text="ankyrin")
bio.protein(ax, (17.0, y - 1.4), 0.5, 0.4, "lipid", wobble=0.07)
bio.callout(ax, (17.1, y - 1.55), (17.6, y - 2.1), "4.2")
wavy(np.array([13.3, y - 1.75]), np.array([16.6, y - 1.45]), waves=2.5)
wavy(np.array([16.6, y - 1.45]), np.array([21.0, y - 1.7]), waves=3.0)
bio.label(ax, (19.2, y - 2.05), "β-spectrin", size="small")
# glycophorin C + 4.1 + actin
ax.add_patch(FancyBboxPatch((22.0 - 0.12, y - MH - 0.15), 0.24, 2 * MH + 0.3,
                                     boxstyle="round,pad=0,rounding_size=0.1", facecolor=P.fill("receptor"),
                                     edgecolor=P.edge("receptor"), lw=0.9, zorder=12))
for k in range(3):
    bio.molecule(ax, (22.0 + 0.05 * k, y + MH + 0.25 + 0.22 * k), token="carbohydrate", r=0.09)
bio.label(ax, (22.7, y + 1.15), "glycophorin C", size="small", ha="left")
bio.protein(ax, (21.7, y - 0.95), 0.6, 0.45, "antibody", wobble=0.07, text="4.1")
actin(ax, np.array([20.6, y - 1.75]), np.array([23.4, y - 1.75]), r=0.09)
bio.label(ax, (23.0, y - 2.25), "actin", size="small")
bio.label(ax, (18.9, 0.35), "vertical linkages: defects → spherocytosis", size="small", italic=True, color=P.muted())
