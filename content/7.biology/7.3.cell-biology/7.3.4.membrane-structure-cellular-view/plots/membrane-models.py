"""Four historical models of the plasma membrane, each with the evidence that motivated it.

A: Gorter and Grendel (1925): a lipid bilayer, from the 2:1 ratio of monolayer area to cell area.
B: Davson and Danielli (1935): a bilayer sandwiched between two layers of protein (low surface tension).
C: Robertson (1959): the unit membrane, as seen in osmium-stained thin sections (two dark lines
   about 2 nm thick separated by a light band about 3.5 nm wide, 7.5 nm in all).
D: Singer and Nicolson (1972): the fluid mosaic model, globular integral proteins embedded in a fluid
   bilayer, peripheral proteins on its surfaces, glycans outside.
"""

import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(26.0, 7.2)
MH = 0.37
y = 3.4
W = 5.6
xs = [0.4, 6.9, 13.4, 19.9]
titles = ["Lipid bilayer", "Protein–lipid sandwich", "Unit membrane", "Fluid mosaic"]
years = ["Gorter & Grendel 1925", "Davson & Danielli 1935", "Robertson 1959", "Singer & Nicolson 1972"]
evidence = ["monolayer area = 2 × cell area", "low surface tension of cells", "trilaminar image in EM", "freeze-fracture, cell fusion"]

for k, (x0, t, yr, ev) in enumerate(zip(xs, titles, years, evidence)):
    bio.panel(ax, "ABCD"[k], (x0, 7.0))
    bio.label(ax, (x0 + W / 2, 6.55), t, size="normal", bold=True)
    bio.label(ax, (x0 + W / 2, 6.05), yr, size="small", color=P.muted())
    bio.label(ax, (x0 + W / 2, 0.45), ev, size="small", italic=True, color=P.muted())

# A: plain bilayer
x0 = xs[0]
bio.bilayer(ax, [(x0, y), (x0 + W, y)])
bio.label(ax, (x0 + W + 0.05, y + 1.0), "outside", size="tiny", ha="right", color=P.muted())
bio.label(ax, (x0 + W + 0.05, y - 1.0), "inside", size="tiny", ha="right", color=P.muted())


def sheet(x0, x1, yc, h, tok="protein"):
    ax.add_patch(FancyBboxPatch((x0, yc - h / 2), x1 - x0, h, boxstyle="round,pad=0,rounding_size=0.14",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=bio.core.LINE * 0.8, zorder=9))


# B: sandwich with protein layers (and a protein-lined pore)
x0 = xs[1]
bio.bilayer(ax, [(x0, y), (x0 + 2.4, y)])
bio.bilayer(ax, [(x0 + 3.2, y), (x0 + W, y)])
sheet(x0, x0 + W, y + MH + 0.38, 0.42)
sheet(x0, x0 + W, y - MH - 0.38, 0.42)
for side in (-1, 1):
    ax.add_patch(Rectangle((x0 + 2.8 + side * 0.33 - 0.09, y - MH - 0.2), 0.18, 2 * MH + 0.4,
                           facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.8, zorder=9))
bio.callout(ax, (x0 + 1.2, y + MH + 0.55), (x0 + 1.2, y + 2.0), "protein layer")
bio.callout(ax, (x0 + 2.8, y - MH - 0.15), (x0 + 3.9, y - 2.0), "protein-lined pore")

# C: the trilaminar EM image, with dimensions
x0 = xs[2]
ink = P.ink()
for yy, h, alpha in ((y + 0.55, 0.42, 0.85), (y - 0.55, 0.42, 0.85)):
    ax.add_patch(Rectangle((x0 + 0.2, yy - h / 2), W - 1.4, h, facecolor=ink, edgecolor="none", alpha=alpha, zorder=8))
quant.bracket(ax, (x0 + W - 1.05, y + 0.76), (x0 + W - 1.05, y + 0.34), "2 nm", side=-1, size="tiny")
quant.bracket(ax, (x0 + W - 1.05, y + 0.34), (x0 + W - 1.05, y - 0.34), "3.5 nm", side=-1, size="tiny")
quant.bracket(ax, (x0 + W - 1.05, y - 0.34), (x0 + W - 1.05, y - 0.76), "2 nm", side=-1, size="tiny")
bio.label(ax, (x0 + 2.4, y + 1.55), "stained head groups", size="tiny", color=P.muted())
bio.label(ax, (x0 + 2.4, y), "unstained chains", size="tiny", color=P.muted())
bio.label(ax, (x0 + 2.4, y - 1.55), "(proposed: extended protein sheets)", size="tiny", color=P.muted())

# D: fluid mosaic
x0 = xs[3]
bio.bilayer(ax, [(x0, y), (x0 + W, y)])
bio.protein(ax, (x0 + 1.1, y + 0.1), 0.9, 1.75, "channel", wobble=0.06)
bio.protein(ax, (x0 + 2.9, y + 0.25), 1.2, 1.5, "receptor", wobble=0.06)
bio.protein(ax, (x0 + 4.3, y - 0.35), 0.8, 0.8, "enzyme", wobble=0.06)        # monotopic, inner leaflet
bio.protein(ax, (x0 + 4.9, y - 1.15), 0.75, 0.55, "protein", wobble=0.08)     # peripheral
for gx in (x0 + 2.6, x0 + 3.2, x0 + 0.9):
    gy = y + 1.0 if gx > x0 + 2 else y + 1.0
    pts = [(gx, gy + 0.22 * i) for i in range(1, 4)]
    ax.plot([gx] + [p[0] for p in pts], [gy] + [p[1] for p in pts], color=P.edge("carbohydrate"), lw=0.8, zorder=13)
    for p in pts:
        bio.molecule(ax, p, token="carbohydrate", r=0.09, zorder=14)
bio.callout(ax, (x0 + 4.9, y - 1.35), (x0 + 4.4, y - 2.1), "peripheral")
bio.callout(ax, (x0 + 2.9, y - 0.5), (x0 + 2.1, y - 2.1), "integral")
