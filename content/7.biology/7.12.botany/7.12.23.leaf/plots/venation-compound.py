"""Venation and compound leaves, generated from rules (wikibio.botany). A: pinnate venation with
secondaries ending at the margin (craspedodromous), pinnate with secondaries looping inside the margin
(brochidodromous), palmate, arcuate, parallel (with transverse veinlets) and dichotomous (Ginkgo-like).
B: odd-pinnate, even-pinnate, bipinnate, palmately compound, pinnately trifoliolate, and a unifoliate
compound leaf (Citrus type: one leaflet jointed to a winged petiole).
"""

import numpy as np
from matplotlib.patches import Polygon

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(27.0, 15.4)

bio.panel(ax, "A", (0.2, 15.2))
bio.label(ax, (0.85, 15.17), "Venation", size="title", ha="left", va="top")
VEN = [("Pinnate\n(craspedodromous)", dict(shape="elliptic", margin="serrate", venation="pinnate", secondaries=7)),
       ("Pinnate\n(brochidodromous)", dict(shape="elliptic", venation="brochidodromous", secondaries=6, tertiary="reticulate")),
       ("Palmate", dict(shape="palmately lobed", venation="palmate", length=3.0, width=3.2)),
       ("Arcuate", dict(shape="elliptic", venation="arcuate", secondaries=4, width=2.1)),
       ("Parallel", dict(shape="linear", width=0.8, venation="parallel", secondaries=4, tertiary=True, length=4.6)),
       ("Dichotomous", dict(shape="flabellate", venation="dichotomous", length=2.6, width=3.9))]
for i, (name, kw) in enumerate(VEN):
    x = 2.2 + i * 4.45
    ln = kw.pop("length", 4.0)
    B.leaf(ax, (x, 9.4 if name != "Palmate" else 10.0), ln, 90, petiole=0.45 if name != "Palmate" else 0.2, **kw)
    bio.label(ax, (x, 8.85), name, size="small", va="center")

bio.panel(ax, "B", (0.2, 7.6))
bio.label(ax, (0.85, 7.57), "Compound leaves", size="title", ha="left", va="top")
items = [("Odd-pinnate", dict(kind="imparipinnate", leaflets=3)), ("Even-pinnate", dict(kind="paripinnate", leaflets=4)),
         ("Bipinnate", dict(kind="bipinnate", leaflets=4, pinnae=2)), ("Palmate", dict(kind="palmate", leaflets=5)),
         ("Pinnately\ntrifoliolate", dict(kind="trifoliate"))]
for i, (name, kw) in enumerate(items):
    x = 2.3 + i * 4.45
    B.compound_leaf(ax, (x, 1.3), 4.6, 90, **kw)
    bio.label(ax, (x, 0.75), name, size="small", va="center")

# unifoliate compound leaf: winged petiole, joint, single leaflet
x = 24.6
ec, fc = P.edge("plant"), P.fill("plant")
wing = [(x, 1.3), (x - 0.35, 1.9), (x - 0.42, 2.45), (x, 2.75), (x + 0.42, 2.45), (x + 0.35, 1.9)]
ax.add_patch(Polygon(wing, closed=True, facecolor=fc, edgecolor=ec, lw=0.9, zorder=6))
ax.plot([x, x], [1.3, 2.8], color=ec, lw=1.4, zorder=6.5)
ax.plot([x - 0.18, x + 0.18], [2.82, 2.82], color=ec, lw=2.2, zorder=7)
B.leaf(ax, (x, 2.86), 3.3, 90, shape="ovate", petiole=0.0, venation="pinnate", secondaries=6)
bio.callout(ax, (x + 0.18, 2.82), (26.4, 3.7), "Joint", size="tiny")
bio.callout(ax, (x + 0.3, 2.1), (26.4, 1.9), "Wing", size="tiny")
bio.label(ax, (x, 0.75), "Unifoliate", size="small", va="center")
