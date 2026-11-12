# The three types of ovarioles (schematic, germarium at the top, oldest oocyte at the base). Panoistic:
# no nurse cells; each oocyte makes its own yolk precursors and RNA (Archaeognatha, Zygentoma, Odonata,
# Orthoptera, Blattodea, Phasmatodea, fleas). Polytrophic: each oocyte is accompanied down the ovariole by
# its own cluster of nurse cells, its sister cells joined by ring canals (Dermaptera, Psocodea, most
# Holometabola such as Diptera, Hymenoptera, Lepidoptera). Telotrophic: the nurse cells stay in the
# germarium (tropharium) and feed the oocytes through long nutritive cords (Hemiptera; polyphagan
# Coleoptera). All three: terminal filament, follicle cells around each oocyte, pedicel to the oviduct.
import numpy as np
from matplotlib.patches import Ellipse, Circle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 13)
cols = [(4.0, "Panoistic", "no nurse cells"), (12.0, "Polytrophic", "nurse cells with each oocyte"),
        (20.0, "Telotrophic", "nurse cells in the tropharium")]
for x, t, sub in cols:
    bio.label(ax, (x, 12.6), t, size="normal", bold=True)
    bio.label(ax, (x, 12.05), sub, size="tiny", color=P.muted())
    ax.plot([x, x], [11.6, 10.6], color=P.edge("neutral"), lw=1.2)          # terminal filament
    ax.plot([x - 1.1, x - 1.0, x - 0.4], [10.4, 1.2, 0.4], color=P.edge("neutral"), lw=0.9)
    ax.plot([x + 1.1, x + 1.0, x + 0.4], [10.4, 1.2, 0.4], color=P.edge("neutral"), lw=0.9)
    ax.plot([x - 0.4, x - 0.4], [0.4, -0.2], color=P.edge("neutral"), lw=0.9)
    ax.plot([x + 0.4, x + 0.4], [0.4, -0.2], color=P.edge("neutral"), lw=0.9)
    sizes = [0.25, 0.35, 0.5, 0.65, 0.8]
    ys = [9.4, 8.3, 6.9, 5.1, 2.9]
    if t == "Telotrophic":
        for k in range(14):
            ax.add_patch(Circle((x + 0.45 * np.cos(k * 2.4) * (k % 3) / 2, 10.2 - 0.12 * k), 0.22, facecolor=P.fill("vesicle"),
                                edgecolor=P.edge("vesicle"), lw=0.5, zorder=4))
        ys = [7.9, 6.8, 5.3, 3.4]
        sizes = sizes[1:]
    for k, (y, s) in enumerate(zip(ys, sizes)):
        ax.add_patch(Ellipse((x, y), 2 * s + 0.1, 2.2 * s + 0.15, facecolor="none", edgecolor=P.edge("enzyme"), lw=1.4, zorder=5))
        ax.add_patch(Ellipse((x, y), 2 * s, 2.2 * s, facecolor=P.fill("petal"), edgecolor=P.edge("petal"), lw=0.7, zorder=5))
        ax.add_patch(Circle((x, y), 0.08 + s * 0.1, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.5, zorder=6))
        if t == "Polytrophic":
            for j in range(5):
                ax.add_patch(Circle((x - 0.36 + 0.18 * j, y + 1.1 * s + 0.28 - 0.06 * (j % 2)), 0.17, facecolor=P.fill("vesicle"),
                                    edgecolor=P.edge("vesicle"), lw=0.5, zorder=6))
        if t == "Telotrophic":
            ax.plot([x + 0.1 * (k - 1.5), x + 0.1 * (k - 1.5)], [y + 1.1 * s, 9.4], color=P.edge("vesicle"), lw=0.6, zorder=3)
    bio.callout(ax, (x, 11.2), (x + 1.6, 11.4), "Terminal filament", size="tiny")
    bio.callout(ax, (x - 0.4, 0.0), (x - 2.8, 0.2), "Pedicel", size="tiny")
bio.callout(ax, (4.0, 2.9), (6.2, 2.0), "Oocyte", size="tiny")
bio.callout(ax, (4.0 + 0.85, 5.1), (6.2, 4.6), "Follicle cells", size="tiny")
bio.callout(ax, (12.0 + 0.2, 6.9 + 0.85), (14.6, 8.2), "Nurse cells", size="tiny")
bio.callout(ax, (20.2, 9.7), (22.2, 10.4), "Tropharium", size="tiny")
bio.callout(ax, (20.05, 8.8), (22.2, 8.8), "Nutritive cords", size="tiny")
