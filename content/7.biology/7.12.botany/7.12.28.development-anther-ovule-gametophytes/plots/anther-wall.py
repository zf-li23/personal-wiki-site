# Development of the anther wall, shown as a radial strip from the anther surface (top) to the locule
# (bottom). A: (1) an archesporial cell differentiates below the epidermis; (2) it divides periclinally
# into a primary parietal cell and a primary sporogenous cell; (3) parietal derivatives form the
# endothecium, the middle layer and the tapetum around the pollen mother cells; (4) in the mature anther
# the middle layer and the tapetum have disappeared, the endothecium has band-like wall thickenings
# (fibrous layer) and the locule holds pollen grains. B: the four types of anther wall formation (Davis
# 1966), according to which of the two secondary parietal layers divides again.
from matplotlib.patches import FancyBboxPatch, Circle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22.6, 12.6)
LAY = {"Epidermis": "plant", "Archesporial cell": "nucleus", "Primary parietal": "atp",
       "Primary sporogenous": "nucleus", "Endothecium": "atp", "Middle layer": "lipid", "Tapetum": "mitochondrion",
       "Pollen mother cells": "nucleus", "Fibrous layer": "atp", "Pollen": "anther"}


def row(x0, y, n, w, h, tok, squash=1.0, nuclei=True, cells=None):
    cw = w / n
    for i in range(n):
        cx = x0 + cw * (i + 0.5)
        ax.add_patch(FancyBboxPatch((cx - cw * 0.46, y - h * squash / 2), cw * 0.92, h * squash,
                                    boxstyle="round,pad=0,rounding_size=0.08", facecolor=P.fill(tok),
                                    edgecolor=P.edge(tok), lw=0.8, zorder=6))
        if nuclei and squash > 0.5:
            ax.add_patch(Circle((cx, y), min(cw, h * squash) * 0.16, facecolor=P.edge(tok), edgecolor="none", zorder=7))


bio.panel(ax, "A", (0.2, 12.4))
bio.label(ax, (11.0, 12.2), "Anther wall development (radial strip)", size="normal", bold=True)
W, X = 3.0, [0.8, 6.2, 11.6, 17.0]
stages = [
    [("Epidermis", 6, 0.55), ("Archesporial cell", 1, 1.1), ("", 0, 0)],
    [("Epidermis", 6, 0.55), ("Primary parietal", 3, 0.6), ("Primary sporogenous", 3, 0.9)],
    [("Epidermis", 6, 0.5), ("Endothecium", 5, 0.6), ("Middle layer", 6, 0.35), ("Tapetum", 4, 0.75),
     ("Pollen mother cells", 3, 1.0)],
    [("Epidermis", 7, 0.25), ("Fibrous layer", 5, 0.9)],
]
for k, layers in enumerate(stages):
    x0 = X[k]
    y = 10.8
    for name, n, h in layers:
        if not name:
            continue
        row(x0, y - h / 2, n, W, h, LAY[name])
        if name == "Fibrous layer":
            cw = W / n
            for i in range(n):
                for t in (-0.25, 0.0, 0.25):
                    cx = x0 + cw * (i + 0.5) + t * cw
                    ax.plot([cx, cx], [y - h + 0.08, y - 0.08], color=P.edge("bone"), lw=1.4, zorder=8)
        bio.label(ax, (x0 + W + 0.15, y - h / 2), name, size="tiny", ha="left")
        y -= h + 0.08
    if k == 3:
        for i, (px, py) in enumerate(((0.6, 8.6), (1.5, 8.2), (2.4, 8.7), (1.0, 7.4), (2.0, 7.3))):
            ax.add_patch(Circle((x0 + px, py), 0.32, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.9,
                                zorder=6))
        bio.label(ax, (x0 + W + 0.15, 8.0), "Pollen grains", size="tiny", ha="left")
        bio.label(ax, (x0 + W + 0.15, 7.4), "(locule)", size="tiny", ha="left", color=P.muted())
    bio.label(ax, (x0 + W / 2, 11.5), f"({k + 1})", size="small", bold=True)
    if k < 3:
        bio.arrow(ax, (x0 + W + 1.65, 6.4), (X[k + 1] - 0.2, 6.4), kind="process")
bio.label(ax, (0.8, 5.7), "Top of each strip: anther surface; bottom: locule", size="tiny", ha="left", color=P.muted())

bio.panel(ax, "B", (0.2, 4.9))
bio.label(ax, (11.0, 4.7), "Types of anther wall formation", size="normal", bold=True)
TY = [("Basic", ["En", "M"], ["M", "T"]), ("Dicotyledonous", ["En", "M"], ["T"]), ("Monocotyledonous", ["En"], ["M", "T"]),
      ("Reduced", ["En"], ["T"])]
TT = {"En": ("Endothecium", "atp"), "M": ("Middle layer", "lipid"), "T": ("Tapetum", "mitochondrion")}
for k, (name, outer, inner) in enumerate(TY):
    x = 2.6 + 5.6 * k
    bio.label(ax, (x, 4.05), name, size="small", bold=True)
    bio.box(ax, (x, 3.35), 2.6, 0.5, token="atp", text="Primary parietal", size="tiny")
    for j, (lst, dx, lab) in enumerate(((outer, -1.3, "outer"), (inner, 1.3, "inner"))):
        bio.arrow(ax, (x, 3.08), (x + dx * 0.8, 2.6), kind="process", head=0.15)
        bio.label(ax, (x + dx * 0.95, 2.4), lab + " SPL", size="tiny", color=P.muted())
        for i, t in enumerate(lst):
            txt, tok = TT[t]
            yy = 1.7 - 0.62 * i
            bio.box(ax, (x + dx, yy), 2.4, 0.5, token=tok, text=txt, size="tiny")
bio.label(ax, (11.0, 0.2), "SPL = secondary parietal layer; a layer that divides again gives two wall layers",
          size="tiny", color=P.muted())
