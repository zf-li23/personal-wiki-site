"""How embryonic cells exchange signals.

A, paracrine: a secreted factor diffuses through the extracellular space to receptors on nearby cells.
B, autocrine: the secreting cell responds to its own factor. C, juxtacrine: a membrane-bound ligand binds a
receptor on an adjacent cell (Delta-Notch, ephrin-Eph). D, gap junctions: small molecules and ions pass
directly between the cytoplasms of neighbours. E, extracellular vesicles (exosomes): vesicles released by one
cell carry proteins and RNAs and are taken up by another. F, cytonemes: thin actin-based filopodia carry
ligand (or receptor) to distant cells and transmit the signal at a contact.
"""

import numpy as np
from matplotlib.patches import Circle, Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 7.4)


def cell(c, rx=1.0, ry=0.8, tok="cytoplasm", seed=0):
    o = bio.blob(c, rx, ry, wobble=0.04, seed=seed, k=9)
    bio.shape(ax, o[:-1], tok, lw=1.2, zorder=4)
    ax.plot(o[:, 0], o[:, 1], color=P.edge("membrane"), lw=1.3, zorder=4.5)
    ax.add_patch(Circle(c, 0.25, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.8, zorder=5))


def receptor(p, angle=90):
    a = np.radians(angle)
    q = (p[0] + 0.22 * np.cos(a), p[1] + 0.22 * np.sin(a))
    ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge("receptor"), lw=2.4, solid_capstyle="round", zorder=6)


def ligand(p, tok="highlight", r=0.08):
    ax.add_patch(Circle(p, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.6, zorder=7))


titles = ["Paracrine", "Autocrine", "Juxtacrine", "Gap junction", "Extracellular vesicles", "Cytoneme"]
for k, t in enumerate(titles):
    bio.panel(ax, "ABCDEF"[k], (0.2 + k * 5.0, 7.2))
    bio.label(ax, (2.6 + k * 5.0, 6.75), t, size="small", bold=True)

# A paracrine
cell((1.4, 3.6), seed=1)
cell((3.9, 2.4), seed=2)
cell((3.9, 4.9), seed=3)
rng = np.random.default_rng(3)
for _ in range(14):
    ligand((2.4 + rng.uniform(0, 1.0), 3.6 + rng.uniform(-1.0, 1.0)))
receptor((3.15, 2.6), 160)
receptor((3.15, 4.7), 200)

# B autocrine
cell((7.6, 3.6), 1.2, 1.0, seed=4)
for a in (30, 90, 150, 210, 270, 330):
    r = np.radians(a)
    receptor((7.6 + 1.18 * np.cos(r), 3.6 + 0.98 * np.sin(r)), a)
    ligand((7.6 + 1.6 * np.cos(r + 0.25), 3.6 + 1.35 * np.sin(r + 0.25)))
bio.arrow(ax, (8.9, 4.6), (8.75, 4.25), kind="process", bend=0.6, head=0.14)

# C juxtacrine
cell((11.6, 3.6), 1.05, 1.0, seed=5)
cell((13.7, 3.6), 1.05, 1.0, tok="cytoplasm", seed=6)
for y in (3.1, 3.6, 4.1):
    ax.plot([12.55, 12.75], [y, y], color=P.edge("highlight"), lw=3, zorder=6)
    ax.plot([12.75, 12.95], [y, y], color=P.edge("receptor"), lw=3, zorder=6)
bio.label(ax, (12.7, 2.0), "ligand | receptor", size="tiny", color=P.muted())

# D gap junction
cell((16.6, 3.6), 1.05, 1.0, seed=7)
cell((18.7, 3.6), 1.05, 1.0, seed=8)
for y in (3.2, 3.6, 4.0):
    ax.add_patch(Rectangle((17.55, y - 0.1), 0.4, 0.2,
                 facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=0.6, zorder=6))
for x in (17.25, 17.75, 18.2):
    ax.add_patch(Circle((x, 3.6), 0.05, facecolor=P.fill("ca"), edgecolor=P.edge("ca"), lw=0.4, zorder=7))
bio.label(ax, (17.7, 2.0), "ions, small molecules", size="tiny", color=P.muted())

# E vesicles
cell((21.5, 3.6), seed=9)
cell((24.0, 3.6), seed=10)
for x, y in ((22.6, 3.9), (22.95, 3.3), (23.2, 4.05)):
    ax.add_patch(Circle((x, y), 0.17, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.7, zorder=7))
    ligand((x, y), "rna", 0.05)
bio.label(ax, (22.8, 2.0), "proteins, RNAs", size="tiny", color=P.muted())

# F cytoneme
cell((26.3, 4.6), 0.9, 0.7, seed=11)
cell((29.0, 2.3), 0.8, 0.65, seed=12)
t = np.linspace(0, 1, 40)
pts = np.c_[26.9 + 1.55 * t, 4.1 - 1.4 * t + 0.15 * np.sin(4 * t)]
ax.plot(pts[:, 0], pts[:, 1], color=P.edge("actin"), lw=1.4, zorder=6)
ligand(tuple(pts[-1]), "highlight", 0.1)
receptor((28.45, 2.75), 140)
bio.label(ax, (27.3, 1.3), "filopodium carries ligand", size="tiny", color=P.muted())
