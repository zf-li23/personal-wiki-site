"""Endospore formation in Bacillus subtilis (main stages) and the layers of a mature spore."""
import numpy as np
from matplotlib.patches import Ellipse

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(30, 12.5)
bio.panel(ax, "A", (0.2, 12.3))
bio.label(ax, (4.5, 12.0), "Sporulation and germination", size="normal", bold=True)
Y = 9.0
X = [2.0, 6.4, 10.8, 15.2, 19.6, 24.0]
TITLES = ["vegetative cell", "asymmetric\ndivision", "engulfment", "cortex and\ncoat", "maturation:\ndehydration, Ca–DPA,\nSASPs",
          "free spore\n(mother cell lyses)"]
for k, (x, t) in enumerate(zip(X, TITLES)):
    if k < 5:
        M.bacillus(ax, (x, Y), 3.2, 1.3, token="bacterium", zorder=4)
    if k == 0:
        ax.add_patch(Ellipse((x, Y), 1.4, 0.6, facecolor=P.light("dna"), edgecolor=P.edge("dna"), lw=0.7, zorder=6))
    if k == 1:
        ax.plot([x + 0.75, x + 0.75], [Y - 0.62, Y + 0.62], color=P.edge("bacterium"), lw=1.6, zorder=6)
    if k >= 2:
        core = {2: "cytoplasm", 3: "cytoplasm", 4: "neutral", 5: "neutral"}[k]
        cxs = x + (0.95 if k < 5 else 0)
        if k >= 3:
            ax.add_patch(Ellipse((cxs, Y), 1.25, 0.95, facecolor=P.fill("lipid_head"), edgecolor=P.edge("lipid_head"),
                                 lw=1.0, zorder=6))
            ax.add_patch(Ellipse((cxs, Y), 1.0, 0.72, facecolor=P.fill("cell_wall"), edgecolor=P.edge("cell_wall"), lw=0.8,
                                 zorder=7))
        ax.add_patch(Ellipse((cxs, Y), 0.72, 0.5, facecolor=P.fill(core), edgecolor=P.edge(core), lw=0.9, zorder=8))
    bio.label(ax, (x, Y - 1.35), t, size="tiny", va="top")
    if k < 5:
        bio.arrow(ax, (x + 1.75, Y), (X[k + 1] - 1.75, Y), kind="process")
bio.arrow(ax, (24.0, Y + 0.8), (2.0, Y + 0.9), kind="process", bend=-0.12, dashed=True)
bio.label(ax, (13.0, 11.75), "germination and outgrowth (nutrients, minutes)", size="tiny", color=P.muted())
# ---- B: layers
bio.panel(ax, "B", (0.2, 5.6))
bio.label(ax, (7.0, 5.3), "Layers of a mature endospore", size="normal", bold=True)
c = (6.0, 2.4)
LAYERS = [("Exosporium", 9.2, 4.0, "neutral", True), ("Spore coat", 8.2, 3.5, "protein", False),
          ("Outer membrane", 7.3, 3.05, "lipid_head", False), ("Cortex", 7.0, 2.9, "cell_wall", False),
          ("Germ cell wall", 5.0, 2.05, "nag", False), ("Inner membrane", 4.65, 1.9, "lipid_head", False),
          ("Core: DNA, ribosomes, Ca–DPA,\nSASPs; 25–50% water", 4.4, 1.75, "cytoplasm", False)]
for k, (name, w, h, tok, dashed) in enumerate(LAYERS):
    ax.add_patch(Ellipse(c, w, h, facecolor=P.fill(tok) if not dashed else "none", edgecolor=P.edge(tok), lw=1.1,
                         ls="--" if dashed else "-", zorder=4 + k))
ax.add_patch(Ellipse(c, 2.2, 0.8, facecolor="none", edgecolor=P.edge("dna"), lw=0.8, ls=":", zorder=12))
ys = np.linspace(4.6, 0.3, len(LAYERS))
angs = np.deg2rad(np.linspace(62, -62, len(LAYERS)))
for k, ((name, w, h, tok, dashed), yt, a) in enumerate(zip(LAYERS, ys, angs)):
    if k == 0:
        rw, rh = w / 2, h / 2
    elif k < len(LAYERS) - 1:
        rw, rh = (w + LAYERS[k + 1][1]) / 4, (h + LAYERS[k + 1][2]) / 4
    else:
        rw, rh = w / 4, h / 4
    bio.callout(ax, (c[0] + rw * np.cos(a), c[1] + rh * np.sin(a)), (13.0, yt), name)
bio.label(ax, (22.5, 3.6), "outer layers: barriers to enzymes\nand chemicals", size="small", color=P.muted())
bio.label(ax, (22.5, 1.6), "core: dehydrated, mineralized,\nmetabolically inert", size="small", color=P.muted())
