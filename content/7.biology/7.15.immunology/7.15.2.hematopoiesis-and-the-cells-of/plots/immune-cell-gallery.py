# A gallery of the main immune cells drawn natively (approximate relative sizes): granulocytes with their
# nuclear shapes and granules, mast cell, monocyte, macrophage, dendritic cell; small lymphocyte,
# plasma cell, memory cell and large granular lymphocyte (NK cell).
import math

import numpy as np
from matplotlib.patches import Circle, Ellipse

import wikibio as bio
from wikibio import immuno

P = bio.P
fig, ax = bio.canvas(24.0, 8.4)
rng = np.random.default_rng(0)


def body(c, rx, ry, tok="neutral", seed=0, wobble=0.05):
    bio.shape(ax, bio.blob(c, rx, ry, wobble=wobble, seed=seed, k=9), token=tok, zorder=5)


def granules(c, r, n, tok, size=0.06, zorder=8):
    k = 0
    while k < n:
        x, y = rng.uniform(-r, r, 2)
        if x * x + y * y < (r * 0.9) ** 2:
            ax.add_patch(Circle((c[0] + x, c[1] + y), size, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.3,
                                zorder=zorder))
            k += 1


def lobes(c, centres, r):
    pts = [(c[0] + dx, c[1] + dy) for dx, dy in centres]
    for a, b in zip(pts[:-1], pts[1:]):
        ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge("nucleus"), lw=2.2, zorder=9, solid_capstyle="round")
    for p in pts:
        ax.add_patch(Circle(p, r, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.9, zorder=10))


y1, y2 = 5.9, 1.9
cells = []
# neutrophil
c = (1.6, y1); body(c, 0.95, 0.92, seed=1); granules(c, 0.85, 40, "neutral", 0.035)
lobes(c, [(-0.42, 0.1), (-0.1, 0.32), (0.25, 0.15), (0.38, -0.25)], 0.22); cells.append((c, "neutrophil"))
# eosinophil
c = (4.4, y1); body(c, 1.0, 0.97, seed=2); granules(c, 0.9, 38, "drug", 0.085)
lobes(c, [(-0.35, 0.05), (0.35, 0.05)], 0.3); cells.append((c, "eosinophil"))
# basophil
c = (7.2, y1); body(c, 0.9, 0.88, seed=3); lobes(c, [(-0.2, 0.0), (0.22, 0.12)], 0.3)
granules(c, 0.8, 34, "protein", 0.1, zorder=11); cells.append((c, "basophil"))
# mast cell (tissue)
c = (10.2, y1); body(c, 1.25, 1.0, seed=4, wobble=0.09)
ax.add_patch(Circle((c[0] + 0.1, c[1]), 0.35, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.9, zorder=10))
granules(c, 1.0, 70, "protein", 0.075, zorder=11); cells.append((c, "mast cell (tissue)"))
# monocyte
c = (13.5, y1); body(c, 1.15, 1.1, seed=5)
ax.add_patch(Ellipse((c[0] + 0.15, c[1] + 0.05), 1.15, 0.8, angle=20, facecolor=P.fill("nucleus"),
                     edgecolor=P.edge("nucleus"), lw=0.9, zorder=10))
ax.add_patch(Circle((c[0] - 0.33, c[1] + 0.18), 0.27, facecolor=P.fill("neutral"), edgecolor="none", zorder=11))
cells.append((c, "monocyte"))
# macrophage (tissue)
c = (17.2, y1); body(c, 1.65, 1.25, seed=6, wobble=0.16)
ax.add_patch(Circle((c[0] + 0.45, c[1] + 0.25), 0.42, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.9, zorder=10))
for dx, dy, r in ((-0.7, -0.3, 0.32), (-0.2, 0.45, 0.22), (0.3, -0.55, 0.25), (-0.95, 0.35, 0.18)):
    bio.vesicle(ax, (c[0] + dx, c[1] + dy), r, token="lysosome", zorder=10)
cells.append((c, "macrophage (tissue)"))
# dendritic cell
c = (21.4, y1); immuno.immune_cell(ax, c, r=0.85, kind="dendritic", token="antibody", seed=7)
cells.append((c, "dendritic cell"))

# lymphoid row
c = (3.0, y2); immuno.immune_cell(ax, c, r=0.62, token="channel", seed=8); cells.append((c, "small lymphocyte\n(T, B or NK: same look)"))
c = (8.0, y2); immuno.immune_cell(ax, c, r=0.85, kind="plasma", token="channel", seed=9); cells.append((c, "plasma cell"))
c = (13.0, y2); immuno.immune_cell(ax, c, r=0.62, kind="memory", token="channel", seed=10); cells.append((c, "memory lymphocyte"))
c = (18.0, y2); body(c, 0.9, 0.88, tok="channel", seed=11)
ax.add_patch(Circle((c[0] + 0.18, c[1] + 0.05), 0.5, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.9, zorder=10))
for k in range(7):
    a = 2.4 + k * 0.33
    ax.add_patch(Circle((c[0] + 0.62 * math.cos(a), c[1] + 0.62 * math.sin(a)), 0.07,
                        facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.3, zorder=11))
cells.append((c, "NK cell (large\ngranular lymphocyte)"))

for (x, y), name in cells:
    bio.label(ax, (x, y - (1.45 if y > 4 else 1.1)), name, size="tiny", va="top")
bio.label(ax, (0.2, 7.95), "Myeloid", size="title", bold=True, ha="left", color=P.edge("drug"))
bio.label(ax, (0.2, 3.55), "Lymphoid", size="title", bold=True, ha="left", color=P.edge("dna"))
