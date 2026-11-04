# The three structural classes of exotoxin: AB toxin, pore-forming toxin, superantigen.
import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(19.0, 7.4)


def panel_frame(x0, w, letter, title, subtitle):
    bio.panel(ax, letter, (x0, 7.15))
    bio.label(ax, (x0 + w / 2, 7.15), title, size="title", bold=True)
    bio.label(ax, (x0 + w / 2, 6.72), subtitle, size="tiny", color=P.muted())
    ax.add_patch(Rectangle((x0, 0.5), w, 3.3, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=1))
    bio.bilayer(ax, [(x0, 3.8), (x0 + w, 3.8)], zorder=4)
    bio.label(ax, (x0 + 0.15, 0.72), "cytoplasm", size="tiny", color=P.muted(), ha="left")


# ================================================================ A: AB toxin
X, W = 0.4, 5.6
panel_frame(X, W, "A", "AB toxin", "an enzyme delivered into the cytosol")

cx = X + 1.1
bio.protein(ax, (cx, 6.0), 0.8, 0.5, "drug", text="A", size="small")
for k in range(5):
    ax.add_patch(Circle((cx - 0.8 + k * 0.4, 5.45), 0.19, facecolor=P.fill("enzyme"),
                        edgecolor=P.edge("enzyme"), lw=1.0, zorder=10))
bio.label(ax, (cx + 1.1, 5.45), "B: binds the receptor", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (cx + 0.6, 6.05), "A: the enzyme", size="tiny", color=P.muted(), ha="left")

bio.receptor(ax, cx + 1.4, 3.8, kind="channel", token="receptor", text=None)
bio.arrow(ax, (cx + 0.3, 5.1), (cx + 1.25, 4.25), kind="process")
bio.label(ax, (X + 0.15, 4.45), "1. binding", size="tiny", ha="left", color=P.muted())

bio.vesicle(ax, (cx + 1.5, 2.8), 0.62)
ax.add_patch(Circle((cx + 1.5, 2.8), 0.22, facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=1.0, zorder=12))
bio.arrow(ax, (cx + 1.45, 3.5), (cx + 1.5, 3.15), kind="process")
bio.label(ax, (cx + 2.3, 3.0), "2. endocytosis;\nlow pH or the ER route", size="tiny", ha="left", color=P.muted())
bio.arrow(ax, (cx + 1.3, 2.3), (cx + 1.1, 1.75), kind="process")
bio.protein(ax, (cx + 1.0, 1.45), 0.65, 0.45, "drug", text="A", size="tiny")
bio.arrow(ax, (cx + 1.4, 1.45), (cx + 2.1, 1.45), kind="catalysis")
bio.box(ax, (X + 4.2, 1.45), 1.7, 0.8, token="protein", radius=0.15)
bio.label(ax, (X + 4.2, 1.45), "target modified", size="tiny", color=P.on_fill())
bio.label(ax, (X + W / 2, 0.22), "catalytic: a few molecules kill the cell", size="tiny", color=P.muted())

# ================================================================ B: pore-forming toxin
X, W = 6.7, 5.6
panel_frame(X, W, "B", "Pore-forming toxin", "a hole punched in the membrane")

for k, x in enumerate((X + 1.2, X + 2.0, X + 2.8)):
    bio.protein(ax, (x, 6.05 - 0.14 * k), 0.55, 0.42, "negative", text=None)
bio.label(ax, (X + 0.15, 6.35), "soluble monomers", size="tiny", ha="left", color=P.muted())
bio.arrow(ax, (X + 2.4, 5.4), (X + 2.8, 4.6), kind="process")
bio.label(ax, (X + 0.15, 4.45), "1. bind a lipid:\ncholesterol, sphingomyelin", size="tiny", ha="left", color=P.muted())

bx = X + 3.0
for k in range(7):
    xx = bx - 0.72 + k * 0.24
    ax.add_patch(Rectangle((xx - 0.08, 3.42), 0.16, 0.78, facecolor=P.fill("negative"),
                           edgecolor=P.edge("negative"), lw=0.8, zorder=12))
ax.add_patch(Rectangle((bx - 0.14, 3.42), 0.28, 0.78, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=13))
bio.label(ax, (X + 4.3, 4.6), "2. oligomerize\n3. insert a β-barrel", size="tiny", color=P.muted())

for k, tok in enumerate(("k", "na", "ca")):
    bio.ion(ax, (bx - 0.05, 3.0 - k * 0.6), tok)
bio.arrow(ax, (bx + 1.0, 3.3), (bx + 1.0, 1.3), kind="process")
bio.label(ax, (X + 2.9, 1.25), "ions and water flow; the cell swells and lyses", size="tiny", color=P.muted())
bio.label(ax, (X + W / 2, 0.22), "the target is the membrane, not a cytosolic protein",
          size="tiny", color=P.muted())

# ================================================================ C: superantigen
X, W = 13.0, 5.6
bio.panel(ax, "C", (X, 7.15))
bio.label(ax, (X + W / 2, 7.15), "Superantigen", size="title", bold=True)
bio.label(ax, (X + W / 2, 6.72), "the immune synapse crosslinked from outside", size="tiny", color=P.muted())

ax.add_patch(Rectangle((X, 4.9), W, 1.4, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=1))
bio.bilayer(ax, [(X, 4.9), (X + W, 4.9)], zorder=4)
bio.label(ax, (X + 0.15, 6.05), "antigen-presenting cell", size="tiny", ha="left", color=P.muted())
ax.add_patch(Rectangle((X, 0.5), W, 1.8, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=1))
bio.bilayer(ax, [(X, 2.3), (X + W, 2.3)], zorder=4)
bio.label(ax, (X + 0.15, 0.68), "T cell", size="tiny", ha="left", color=P.muted())

for mx in (X + 1.5, X + 3.9):
    ax.add_patch(Polygon([[mx - 0.42, 4.9], [mx + 0.42, 4.9], [mx + 0.26, 4.1], [mx - 0.26, 4.1]],
                         closed=True, facecolor=P.fill("antibody"), edgecolor=P.edge("antibody"), lw=1.0, zorder=10))
    ax.add_patch(Polygon([[mx - 0.42, 2.3], [mx + 0.42, 2.3], [mx + 0.26, 3.1], [mx - 0.26, 3.1]],
                         closed=True, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=1.0, zorder=10))
bio.label(ax, (X + 0.1, 4.2), "MHC II", size="tiny", ha="left")
bio.label(ax, (X + 0.1, 2.95), "TCR", size="tiny", ha="left")

ax.add_patch(Circle((X + 1.5, 3.6), 0.17, facecolor=P.fill("metabolite"), edgecolor=P.edge("metabolite"),
                    lw=0.9, zorder=12))
bio.label(ax, (X + 1.4, 1.5), "peptide in the groove:\n0.01–0.1 % of T cells", size="tiny", color=P.muted())

ax.add_patch(Polygon([[X + 4.32, 4.15], [X + 4.95, 3.92], [X + 4.95, 3.12], [X + 4.32, 3.0]], closed=True,
                     facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=1.1, zorder=12))
bio.label(ax, (X + 5.05, 3.55), "super-\nantigen", size="tiny", color=P.edge("drug"), ha="left")
bio.label(ax, (X + 4.2, 1.5), "outside the groove:\n5–30 % of T cells", size="tiny", color=P.muted())
bio.label(ax, (X + W / 2, 0.22), "massive cytokine release: fever, capillary leak, shock",
          size="tiny", color=P.muted())
