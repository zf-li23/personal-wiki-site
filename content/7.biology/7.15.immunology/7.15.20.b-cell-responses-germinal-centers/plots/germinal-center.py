# Structure of a germinal center in a secondary follicle and the cyclic re-entry between its zones.
# Dark zone (nearer the T-cell zone): centroblasts proliferate and hypermutate (AID, CXCR4 / CXCL12).
# Light zone: centrocytes test their mutated BCR on antigen held by follicular dendritic cells and compete
# for help from Tfh cells (CD40L, IL-21); selected cells return to the dark zone, the rest die or exit as
# plasmablasts or memory B cells. Naive IgD+ B cells are pushed aside to form the mantle zone.
import math

import numpy as np
from matplotlib.patches import Ellipse

import wikibio as bio
from wikibio import immuno

P = bio.P
rng = np.random.default_rng(3)
fig, ax = bio.canvas(29, 13)

# T-cell zone below, follicle above
bio.box(ax, (11.5, 0.9), 13.5, 1.2, "extracellular")
bio.label(ax, (11.5, 0.9), "T-cell zone (paracortex): Tfh precursors primed by DCs", size="small")
cx, cy = 11.5, 7.0
ax.add_patch(Ellipse((cx, cy), 15.0, 10.6, facecolor=P.fill("extracellular"), edgecolor=P.edge("neutral"), lw=1.0, zorder=1))
# mantle zone of small naive B cells
for k in range(70):
    th = 2 * math.pi * k / 70
    for rr in (0.9, 0.96):
        x = cx + 7.0 * rr * math.cos(th)
        y = cy + 4.95 * rr * math.sin(th)
        immuno.immune_cell(ax, (x, y), r=0.16, token="neutral", seed=k)
bio.label(ax, (cx, cy + 5.75), "Mantle zone: naive IgM⁺IgD⁺ B cells", size="small")

# germinal center
ax.add_patch(Ellipse((cx, cy), 11.0, 7.6, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("antibody"), lw=1.0, zorder=2))
# dark zone: lower half (towards T zone)
ax.add_patch(Ellipse((cx, cy - 1.7), 10.0, 3.9, facecolor=P.fill("antibody"), edgecolor="none", alpha=0.55, zorder=3))
for k in range(55):
    x = cx + rng.uniform(-4.3, 4.3)
    y = cy - 1.7 + rng.uniform(-1.4, 1.4)
    if ((x - cx) / 4.8) ** 2 + ((y - cy + 1.7) / 1.8) ** 2 < 1:
        immuno.immune_cell(ax, (x, y), r=0.24, token="antibody", seed=k)
bio.label(ax, (cx - 7.7, cy - 2.2), "Dark zone\ncentroblasts:\nproliferation,\nsomatic hypermutation\n(AID; CXCR4–CXCL12)",
          size="tiny", ha="right")

# light zone: FDC network with antigen, Tfh, centrocytes
for k, (fx, fy) in enumerate(((cx - 2.4, cy + 1.8), (cx + 0.3, cy + 2.4), (cx + 2.8, cy + 1.5))):
    immuno.immune_cell(ax, (fx, fy), r=0.5, kind="dendritic", token="receptor", seed=k)
    for j in range(6):
        a = 2 * math.pi * j / 6 + 0.4
        bio.protein(ax, (fx + 0.85 * math.cos(a), fy + 0.85 * math.sin(a)), 0.18, 0.15, "carbohydrate")
for k, (tx, ty) in enumerate(((cx - 0.9, cy + 0.9), (cx + 1.7, cy + 0.55))):
    immuno.immune_cell(ax, (tx, ty), r=0.32, token="cd4", seed=20 + k)
for k in range(9):
    x = cx + rng.uniform(-3.6, 3.6)
    y = cy + rng.uniform(0.5, 2.9)
    immuno.immune_cell(ax, (x, y), r=0.22, token="antibody", seed=40 + k, receptor_token="antibody", receptors=4)
bio.label(ax, (cx - 7.7, cy + 2.6), "Light zone\nFDCs hold antigen;\ncentrocytes compete\nfor antigen and\nTfh help (CD40L, IL-21)",
          size="tiny", ha="right")
bio.label(ax, (cx + 2.8, cy + 0.75), "FDC", size="tiny")
bio.label(ax, (cx + 1.7, cy + 0.0), "Tfh", size="tiny")

# the cycle
bio.arrow(ax, (cx - 3.0, cy - 0.6), (cx - 3.0, cy + 0.9), kind="process", bend=0.3, lw=2.0)
bio.label(ax, (cx - 3.4, cy + 0.15), "~15 % per hour", size="tiny", ha="right")
bio.arrow(ax, (cx + 3.4, cy + 0.6), (cx + 3.4, cy - 0.9), kind="process", bend=0.3, lw=2.0, color=P.edge("positive"))
bio.label(ax, (cx + 3.75, cy - 0.25), "selected (~10–30 %):\nre-enter dark zone", size="tiny", ha="left",
          color=P.edge("positive"))

# outcomes on the right
ox = cx + 9.2
immuno.immune_cell(ax, (ox, 10.4), r=0.55, kind="plasma", token="neutral", seed=5)
bio.label(ax, (ox + 0.9, 10.4), "Plasmablast → long-lived\nplasma cell (bone marrow)", size="tiny", ha="left")
immuno.immune_cell(ax, (ox, 7.9), r=0.45, kind="memory", token="neutral", receptor_token="antibody", receptors=6, seed=6)
bio.label(ax, (ox + 0.9, 7.9), "Memory B cell", size="tiny", ha="left")
immuno.immune_cell(ax, (ox, 5.5), r=0.4, token="negative", seed=7)
bio.label(ax, (ox + 0.9, 5.5), "Apoptosis (most cells);\ncleared by tingible-body\nmacrophages", size="tiny", ha="left")
for y in (10.4, 7.9, 5.5):
    bio.arrow(ax, (cx + 5.4, cy + 0.2), (ox - 0.7, y), kind="process", head=0.16)
