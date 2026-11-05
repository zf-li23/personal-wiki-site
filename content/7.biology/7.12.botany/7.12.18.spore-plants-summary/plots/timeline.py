"""A time line of plant evolution on the ICS time scale. Top: the Precambrian (4000-541 Ma, eons) with the
first cyanobacterial microfossils, the Great Oxidation Event, the first eukaryotes and the first
multicellular red and green algae. Bottom: the Phanerozoic (541-0 Ma, eras and periods) with the first
appearances of land plant groups and bars for the times of dominance. Ages are approximate."""
import numpy as np
from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(32, 17)
X0, X1 = 1.0, 31.0

# ---- Precambrian strip
bio.label(ax, (X0, 16.4), "Precambrian (4000-541 Ma)", size="normal", bold=True, ha="left")
yb = phylo.geo_scale(ax, (X0, X1), (4000, 541), 15.6, ranks=("eon", "era"), height=0.55, size="small")


def px(a, a0=4000, a1=541):
    return X0 + (a0 - a) / (a0 - a1) * (X1 - X0)


pre = [(3480, "stromatolites (oldest life?)"), (2400, "Great Oxidation Event"), (1880, "cyanobacterial microfossils"),
       (1650, "first eukaryotes"), (1047, "Bangiomorpha (red alga)"), (1000, "Proterocladus (green alga)"),
       (680, "Snowball Earth")]
for k, (a, t) in enumerate(pre):
    x = px(a)
    y = yb - 0.6 - [0, 1, 0, 1, 0, 2, 0][k] * 0.9
    ax.plot([x, x], [yb, y + 0.25], color=P.muted(), lw=0.8)
    ax.plot([x], [yb - 0.05], marker="v", color=P.edge("plant"), ms=6)
    bio.label(ax, (x, y), t, size="small", ha="center")

# ---- Phanerozoic
Y = 10.6
bio.label(ax, (X0, Y + 0.8), "Phanerozoic (541-0 Ma)", size="normal", bold=True, ha="left")
yb2 = phylo.geo_scale(ax, (X0, X1), (541, 0), Y, ranks=("era", "period"), height=0.55, size="small")


def qx(a):
    return X0 + (541 - a) / 541 * (X1 - X0)


events = [(470, "cryptospores:\nland plants"), (432, "Cooksonia"), (420, "Baragwanathia\n(lycophytes)"),
          (407, "Rhynie chert"), (385, "first forests,\nferns"), (365, "first seeds"), (305, "coal swamps\ncollapse"),
          (252, "end-Permian\nextinction"), (133, "angiosperm\npollen"), (100, "polypod fern\nradiation"), (7, "C4\ngrasslands")]
for k, (a, t) in enumerate(events):
    x = qx(a)
    y = yb2 - 0.7 - [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1][k] * 1.15
    ax.plot([x, x], [yb2, y + 0.35], color=P.muted(), lw=0.8)
    ax.plot([x], [yb2 - 0.05], marker="v", color=P.edge("plant"), ms=6)
    bio.label(ax, (x, y), t, size="small", ha="center")

# dominance bars
bars = [("Algae (marine primary producers)", 541, 0, "dna"), ("Bryophytes", 470, 0, "plant"),
        ("Early vascular plants", 432, 380, "bract"), ("Lycophyte trees, calamites, tree ferns", 380, 290, "animal"),
        ("Gymnosperms dominant", 290, 100, "ovule"), ("Angiosperms dominant", 100, 0, "petal")]
for k, (t, a0, a1, tok) in enumerate(bars):
    y = 3.9 - k * 0.62
    x0, x1 = qx(a0), qx(a1)
    ax.add_patch(FancyBboxPatch((x0, y - 0.22), x1 - x0, 0.44, boxstyle="round,pad=0,rounding_size=0.15",
                                facecolor=P.mix(P.surface(), P.fill(tok), 0.55), edgecolor=P.edge(tok), lw=0.8))
    bio.label(ax, (x0 + 0.15, y), t, size="small", ha="left")
