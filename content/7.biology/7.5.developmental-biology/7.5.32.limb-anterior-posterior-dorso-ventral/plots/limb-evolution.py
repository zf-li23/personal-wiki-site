"""Regulatory evolution of the limb (schematic).

A: the HoxD cluster between two regulatory landscapes (topologically associating domains). Early in the limb bud,
enhancers in the telomeric landscape (T-DOM) activate Hoxd9-11 in the presumptive zeugopod; later, enhancers in the
centromeric landscape (C-DOM) activate Hoxd13 and its neighbours in the autopod; the boundary between the domains
lies within the cluster, and cells switch from one landscape to the other.
B: enhancer-swap experiment of Kvon et al. (2016): the mouse ZRS, the limb enhancer of Shh about 1 Mb away inside
Lmbr1, was replaced by its orthologues. Human and coelacanth ZRS give normal limbs; the python ZRS, which has lost
part of a binding site cluster (a 17 bp deletion), gives severely truncated limbs; restoring the missing sequence in
the python ZRS rescues them.
"""

import numpy as np
import wikibio as bio
from wikibio import limbdev as LD
from matplotlib.patches import FancyBboxPatch

P = bio.P
fig, ax = bio.canvas(30.0, 10.0)

bio.panel(ax, "A", (0.2, 9.8))
y = 6.4
ax.plot([0.8, 14.2], [y, y], color=P.muted(), lw=1.2)
for name, x0, x1, tk in (("C-DOM (centromeric)", 0.9, 5.6, "phalanges"), ("T-DOM (telomeric)", 9.4, 14.1, "radius")):
    ax.add_patch(FancyBboxPatch((x0, y - 0.55), x1 - x0, 1.1, boxstyle="round,pad=0,rounding_size=0.5",
                                facecolor=P.mix(P.fill(tk), P.surface(), 0.55), edgecolor=P.edge(tk), lw=0.8, zorder=3))
    bio.label(ax, ((x0 + x1) / 2, y + 0.95), name, size="small")
    for xe in np.linspace(x0 + 0.6, x1 - 0.6, 4):
        ax.add_patch(FancyBboxPatch((xe - 0.12, y - 0.18), 0.24, 0.36, boxstyle="round,pad=0,rounding_size=0.05",
                                    facecolor=P.fill(tk), edgecolor=P.edge(tk), lw=0.6, zorder=4))
genes = ["13", "12", "11", "10", "9", "8"]
for i, g in enumerate(genes):
    x = 6.0 + 0.55 * i
    tk = "phalanges" if g in ("13", "12") else "radius" if g in ("11", "10", "9") else "neutral"
    ax.add_patch(FancyBboxPatch((x, y - 0.3), 0.42, 0.6, boxstyle="round,pad=0,rounding_size=0.06",
                                facecolor=P.fill(tk), edgecolor=P.edge(tk), lw=0.7, zorder=5))
    bio.label(ax, (x + 0.21, y - 0.62), g, size="tiny", va="top")
bio.label(ax, (7.65, y - 1.25), "Hoxd", size="small", italic=True)
bio.arrow(ax, (3.2, y - 0.7), (6.5, y - 0.4), kind="activation", bend=0.35, lw=1.0)
bio.arrow(ax, (11.8, y - 0.7), (7.8, y - 0.4), kind="activation", bend=-0.35, lw=1.0)
bio.label(ax, (3.2, 3.4), "late phase: autopod (digits)", size="small", color=P.edge("phalanges") if not P.is_dark() else P.fill("phalanges"))
bio.label(ax, (11.8, 3.4), "early phase: zeugopod", size="small", color=P.edge("radius") if not P.is_dark() else P.fill("radius"))
bio.label(ax, (7.5, 1.6), "domain boundary inside the cluster; cells switch landscapes", size="tiny", color=P.muted())

bio.panel(ax, "B", (15.4, 9.8))
rows = [("mouse ZRS (control)", {}), ("human ZRS", {}), ("coelacanth ZRS", {}),
        ("python ZRS", dict(upto="zeugopod", proportions=(0.34, 0.1, 0.38))), ("python ZRS + restored site", {})]
for k, (name, kw) in enumerate(rows):
    yy = 8.6 - 1.75 * k
    bio.label(ax, (16.0, yy), name, size="small", ha="left")
    LD.limb_skeleton(ax, (21.6, yy), 5.6, width=0.22, digits=(1, 2, 3, 4, 5), **kw)
