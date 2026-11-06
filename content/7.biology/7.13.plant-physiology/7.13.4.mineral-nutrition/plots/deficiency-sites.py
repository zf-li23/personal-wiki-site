# Where deficiency symptoms appear first (schematic). A: a phloem-mobile nutrient (N, P, K, Mg, Cl) is
# withdrawn from the older, lower leaves and moved to the growing shoot tip, so chlorosis and later necrosis
# begin on the old leaves while the young leaves stay green. B: a nutrient that is hardly remobilized
# (Ca, B, Fe, S, Cu, often Mn) stays where it was deposited, so the old leaves stay green and the young leaves and
# the shoot apex show the symptoms (chlorosis for Fe and S, necrosis of the apex for Ca and B).
import numpy as np

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(19.0, 12.0)


def plant(x0, sick_old, title, sub, letter):
    bio.panel(ax, letter, (x0 - 4.0, 11.7))
    bio.label(ax, (x0 - 3.3, 11.65), title, size="title", ha="left", va="top")
    bio.label(ax, (x0 - 3.3, 11.0), sub, size="small", ha="left", va="top", color=P.muted())
    # soil
    ax.plot([x0 - 3.5, x0 + 3.5], [1.0, 1.0], color=P.edge("cell_wall"), lw=1.5)
    ax.plot([x0, x0], [1.0, 9.6], color=P.edge("plant"), lw=3.0, solid_capstyle="round", zorder=5)
    n = 6
    leaves = []
    for k in range(n):
        y = 1.8 + 1.25 * k
        side = 1 if k % 2 == 0 else -1
        L = 2.6 - 0.28 * k
        old = k <= 1
        young = k >= 4
        if sick_old:
            tok = "highlight" if old else ("bract" if k == 2 else "leaf")
        else:
            tok = "highlight" if young else "leaf"
        a = B.leaf(ax, (x0, y), L, angle=90 - side * 62, shape="elliptic", venation="pinnate", token=tok,
                   petiole=0.25, seed=k)
        leaves.append(a)
    # apex
    tip = (x0, 9.75)
    if sick_old:
        bio.box(ax, tip, 0.35, 0.35, token="positive")
    else:
        bio.box(ax, tip, 0.38, 0.38, token="negative")
        bio.callout(ax, tip, (x0 + 2.3, 10.4), "necrotic apex (Ca, B)")
    return leaves


L1 = plant(4.8, True, "Mobile nutrient", "N, P, K, Mg, Cl", "A")
for k in (0, 1):
    a = L1[k]
    bio.arrow(ax, a["blade"], (4.95, 9.3), kind="process", bend=0.25 if k == 0 else -0.25, color=P.edge("rna"), dashed=True)
bio.callout(ax, L1[0]["apex"], (8.8, 2.0), "old leaves yellow first")
bio.label(ax, (8.6, 6.2), "remobilized\nin the phloem", size="small", color=P.edge("rna"))

L2 = plant(14.3, False, "Immobile nutrient", "Ca, B, Fe, S, Cu", "B")
bio.callout(ax, L2[5]["apex"], (17.8, 8.4), "young leaves\nchlorotic (Fe, S)")
bio.callout(ax, L2[0]["apex"], (18.3, 2.2), "old leaves green")
