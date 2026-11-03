"""Evolution of a Drosophila wing spot (after Futuyma and Kirkpatrick 2017, Fig. 15.17): ancestral (yellow
enhancer does not bind Distal-less, uniform low yellow expression), co-option (enhancer gains Dll binding
sites), diversification (increased Dll expression in one region gives a spot, D. biarmipes)."""
import numpy as np
from matplotlib.patches import Ellipse
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 10)
cols = [(4.0, "Ancestral", False, False), (12.0, "Co-option", True, False), (20.0, "Diversification", True, True)]
for cx, title, binds, spot in cols:
    bio.label(ax, (cx, 9.5), title, size="small", bold=True)
    # wing outline with yellow-expression shading
    ax.add_patch(Ellipse((cx, 7.4), 6.0, 2.2, angle=8, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"), lw=1.0))
    if binds:
        ax.add_patch(Ellipse((cx + 1.6, 7.75), 2.0 if not spot else 1.3, 1.0 if not spot else 0.8, angle=8,
                             facecolor=P.fill("lipid") if not spot else P.edge("lipid"), edgecolor="none",
                             alpha=0.55 if not spot else 0.95))
    # Dll expression dots
    dll = 0.35 if not spot else 0.6
    for dx in (-2.0, -0.5, 1.0, 2.2):
        r = dll * (1.6 if (spot and dx > 0.8) else 1.0) * 0.3
        ax.add_patch(bio.core.Circle((cx + dx, 7.0 + 0.12 * dx), r, facecolor=P.fill("rna"), edgecolor=P.edge("rna"),
                                     lw=0.5, zorder=8))
    # gene diagram
    y = 3.8
    ax.plot([cx - 3.2, cx + 3.2], [y, y], color=P.muted(), lw=1.0)
    bio.box(ax, (cx - 1.6, y), 2.0, 0.55, "dna", radius=0.08, lw=0.8)
    bio.label(ax, (cx - 1.6, y - 0.75), "wing enhancer", size="tiny", color=P.muted())
    if binds:
        for k in range(2):
            bio.box(ax, (cx - 2.15 + 0.6 * k, y), 0.35, 0.55, "rna", radius=0.05, lw=0.6)
        ax.add_patch(bio.core.Circle((cx - 1.85, y + 0.75), 0.28, facecolor=P.fill("rna"), edgecolor=P.edge("rna"),
                                     lw=0.7, zorder=12))
        bio.label(ax, (cx - 1.85, y + 0.75), "Dll", size="tiny", color=P.on_fill())
    bio.box(ax, (cx + 1.6, y), 2.2, 0.6, "lipid", radius=0.08, lw=0.8)
    bio.label(ax, (cx + 1.6, y), "yellow", size="tiny", italic=True, color=P.on_fill())
    note = {"Ancestral": "no Dll sites:\nlow uniform yellow",
            "Co-option": "Dll sites gained (cis):\nyellow follows Dll",
            "Diversification": "Dll up in one region (trans):\ndark spot"}[title]
    bio.label(ax, (cx, 1.9), note, size="tiny", color=P.muted())
for a, b in ((7.3, 8.7), (15.3, 16.7)):
    bio.arrow(ax, (a, 7.4), (b, 7.4), kind="process")
bio.label(ax, (12.0, 0.6), "brown shading: yellow expression (melanin); orange dots and sites: Distal-less and its binding sites", size="tiny",
          color=P.muted())
