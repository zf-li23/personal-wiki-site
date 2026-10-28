"""Three experiments showing that differentiated cells keep a complete genome (schematic).

A: nuclear transfer in Xenopus (Gurdon 1962): the nucleus of an intestinal epithelial cell of a tadpole is
injected into an egg whose own nucleus has been destroyed by ultraviolet light; a fraction of the eggs
develop into swimming tadpoles, and some into fertile adult frogs. B: somatic cell nuclear transfer in a
mammal (Wilmut and colleagues 1997): a mammary epithelial cell of a Finn Dorset ewe, made quiescent by
serum starvation, is fused by an electric pulse with an enucleated oocyte of a Scottish Blackface ewe; the
embryo grows to a blastocyst in culture and is transferred to a surrogate mother, which gives birth to a lamb
genetically identical to the donor of the nucleus (Dolly, born 1996; 1 lamb from 277 fused eggs).
C: reprogramming without an egg (Takahashi and Yamanaka 2006): retroviral expression of four transcription
factors (Oct4, Sox2, Klf4, c-Myc) turns a small fraction of fibroblasts into induced pluripotent stem cells,
which form colonies like embryonic stem cells and can contribute to every tissue of a chimeric mouse.
"""

import wikibio as bio
from wikibio import development as dev

P = bio.P
fig, ax = bio.canvas(30.0, 10.6)


def egg(xy, r=0.75, nucleus=True, token="animal"):
    ax.add_patch(__import__("matplotlib").patches.Circle(xy, r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=1.4, zorder=6))
    if nucleus:
        ax.add_patch(__import__("matplotlib").patches.Circle((xy[0] + 0.15, xy[1] + 0.25), 0.18, facecolor=P.fill("nucleus"),
                     edgecolor=P.edge("nucleus"), lw=1.0, zorder=7))


def tadpole(xy, size=1.0, token="animal"):
    import numpy as np
    from matplotlib.patches import Ellipse, Polygon
    x, y = xy
    t = np.linspace(0, 1, 30)
    top = np.c_[x + 0.25 * size + t * 1.0 * size, y + 0.18 * size * (1 - t) + 0.08 * size * np.sin(t * 6)]
    bot = np.c_[x + 0.25 * size + t * 1.0 * size, y - 0.12 * size * (1 - t) + 0.08 * size * np.sin(t * 6)]
    ax.add_patch(Polygon(np.vstack([top, bot[::-1]]), closed=True, facecolor=P.light(token), edgecolor=P.edge(token), lw=1.0, zorder=5))
    ax.add_patch(Ellipse((x, y), 0.7 * size, 0.5 * size, facecolor=P.fill(token), edgecolor=P.edge(token), lw=1.2, zorder=6))
    ax.add_patch(Ellipse((x - 0.18 * size, y + 0.08 * size), 0.08 * size, 0.08 * size, color=P.edge(token), zorder=7))


# A: Xenopus
bio.panel(ax, "A", (0.1, 10.5))
bio.label(ax, (5.0, 10.2), r"Nuclear transfer in $\it{Xenopus}$", size="small", bold=True)
tadpole((1.0, 8.0), 1.1)
bio.label(ax, (1.4, 7.0), "donor tadpole", size="tiny")
for k in range(3):
    ax.add_patch(__import__("matplotlib").patches.FancyBboxPatch((2.7 + k * 0.42, 7.4), 0.38, 1.1,
                 boxstyle="round,pad=0,rounding_size=0.08", facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=1.0, zorder=5))
    ax.add_patch(__import__("matplotlib").patches.Circle((2.89 + k * 0.42, 7.75), 0.1, facecolor=P.fill("nucleus"),
                 edgecolor=P.edge("nucleus"), lw=0.8, zorder=6))
bio.label(ax, (3.3, 7.0), "intestinal\ncells", size="tiny")
bio.arrow(ax, (4.2, 7.95), (5.0, 7.95), kind="process")
egg((6.3, 7.95), nucleus=False)
bio.icon(ax, "servier/micropipette", at=(5.3, 8.9), height=1.7, rotate=-50)
ax.add_patch(__import__("matplotlib").patches.Circle((6.25, 7.95), 0.15, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"),
             lw=0.9, zorder=8))
bio.label(ax, (6.3, 6.85), "UV-irradiated egg\n+ donor nucleus", size="tiny")
bio.arrow(ax, (7.3, 7.95), (8.1, 7.95), kind="process")
dev.embryo(ax, (8.9, 7.95), r=0.6, stage="morula")
bio.label(ax, (8.9, 6.95), "blastula", size="tiny")
bio.arrow(ax, (9.6, 7.95), (10.4, 7.95), kind="process")
bio.icon(ax, "phylopic/xenopus", at=(11.2, 7.95), height=1.1, color="positive")
bio.label(ax, (11.2, 6.95), "tadpole, frog", size="tiny")

# B: Dolly
bio.panel(ax, "B", (0.1, 5.6))
bio.label(ax, (5.0, 5.3), "Somatic cell nuclear transfer (Dolly)", size="small", bold=True)
bio.icon(ax, "servier/sheep", at=(1.2, 3.4), height=1.3)
bio.label(ax, (1.2, 2.3), "Finn Dorset:\nmammary cell", size="tiny")
bio.icon(ax, "servier/sheep", at=(1.2, 0.9), height=1.0)
bio.label(ax, (2.4, 0.5), "Blackface: oocyte", size="tiny", ha="left")
ax.add_patch(__import__("matplotlib").patches.Circle((3.3, 3.4), 0.35, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=1.0, zorder=6))
ax.add_patch(__import__("matplotlib").patches.Circle((3.3, 3.4), 0.15, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.8, zorder=7))
egg((4.3, 1.9), nucleus=False, r=0.6)
bio.arrow(ax, (2.3, 3.3), (2.9, 3.4), kind="process")
bio.arrow(ax, (2.3, 1.1), (3.6, 1.7), kind="process")
bio.label(ax, (4.3, 1.0), "enucleated", size="tiny")
bio.arrow(ax, (3.7, 3.1), (4.1, 2.5), kind="process")
bio.label(ax, (5.6, 3.3), "electric\npulse: fusion", size="tiny")
bio.arrow(ax, (5.0, 1.9), (5.9, 1.9), kind="process")
dev.embryo(ax, (6.7, 1.9), r=0.6, stage="blastocyst")
bio.label(ax, (6.7, 0.95), "blastocyst", size="tiny")
bio.arrow(ax, (7.4, 1.9), (8.2, 1.9), kind="process")
bio.icon(ax, "servier/sheep", at=(9.1, 1.9), height=1.0)
bio.label(ax, (9.1, 0.9), "surrogate", size="tiny")
bio.arrow(ax, (9.9, 1.9), (10.5, 1.9), kind="process")
bio.icon(ax, "servier/sheep", at=(11.3, 1.9), height=0.9)
bio.label(ax, (11.3, 0.9), "Dolly (1996)", size="tiny")

# C: iPS cells
bio.panel(ax, "C", (14.0, 10.5))
bio.label(ax, (21.5, 10.2), "Induced pluripotent stem cells", size="small", bold=True)
bio.icon(ax, "servier/fibroblast", at=(16.4, 6.6), width=2.6)
bio.label(ax, (16.4, 5.4), "skin fibroblast", size="tiny")
bio.arrow(ax, (18.0, 6.6), (21.0, 6.6), kind="process")
for k, name in enumerate(("Oct4", "Sox2", "Klf4", "c-Myc")):
    bio.box(ax, (19.5, 9.5 - 0.45 * k), 1.5, 0.38, "dna", text=name, size="tiny", italic=False)
bio.label(ax, (19.5, 7.3), "transcription factors\n(retroviral vectors)", size="tiny")
bio.label(ax, (19.5, 6.15), "2–3 weeks; < 0.1 % of cells", size="tiny", color=P.muted())
bio.icon(ax, "bioicons/stem-cell-colony", at=(22.6, 6.6), height=2.0)
bio.label(ax, (22.6, 5.2), "iPS colony", size="tiny")
bio.arrow(ax, (24.0, 7.2), (25.6, 8.6), kind="process")
bio.arrow(ax, (24.0, 6.0), (25.6, 4.6), kind="process")
bio.icon(ax, "servier/mouse", at=(27.4, 8.6), height=1.3)
bio.label(ax, (27.4, 7.5), "chimeric mouse", size="tiny")
for k, (ic, name, sz) in enumerate((("servier/smooth-muscle-cell", "muscle", dict(width=1.2)),
                                     ("servier/columnar-cell", "epithelium", dict(height=1.1)),
                                     ("servier/red-blood-cell", "blood", dict(height=0.8)))):
    bio.icon(ax, ic, at=(25.8 + 1.4 * k, 4.2), **sz)
    bio.label(ax, (25.8 + 1.4 * k, 3.3), name, size="tiny")
bio.label(ax, (27.2, 2.6), "cells of all three germ layers", size="tiny", color=P.muted())
bio.label(ax, (21.5, 1.2), "Conclusion: differentiation changes which genes are expressed,\nnot which genes the nucleus contains",
          size="small")
