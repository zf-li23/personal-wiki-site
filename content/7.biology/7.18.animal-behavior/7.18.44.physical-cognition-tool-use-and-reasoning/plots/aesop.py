# The Aesop's fable paradigm (Bird and Emery 2009; Jelbert et al. 2014) and the physics a bird would have
# to understand. A: a floating food item lies on water at the bottom of a transparent tube, below the reach
# of the beak; dropping stones raises the water. B: water level against the number of objects dropped, from
# Archimedes' principle. Each fully submerged object of volume v raises the level by v / (pi r^2); a floating
# object of density rho (relative to water) displaces only rho v. Tube radius 1.5 cm (narrow) or 2.5 cm
# (wide), initial level 4 cm, food reachable at 10 cm, object volume 6 cm^3; foam density 0.05.
import numpy as np
from matplotlib.patches import Circle, Rectangle

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22, 10.0)
bio.panel(ax, "A", (0.3, 9.6))

# tube schematic (canvas units: 1 unit = 1.6 cm of tube height)
x0, w, ybot, ytop = 2.2, 2.4, 1.0, 8.4
lvl = ybot + 2.9
ax.add_patch(Rectangle((x0, ybot), w, lvl - ybot, facecolor=P.fill("extracellular"), edgecolor="none", zorder=3))
for x in (x0, x0 + w):
    ax.plot([x, x], [ybot, ytop], color=P.ink(), lw=1.6, zorder=6)
ax.plot([x0, x0 + w], [ybot, ybot], color=P.ink(), lw=1.6, zorder=6)
rng = np.random.default_rng(3)
for k in range(9):
    cx = x0 + 0.35 + (k % 4) * 0.55 + rng.uniform(-0.05, 0.05)
    cy = ybot + 0.32 + (k // 4) * 0.5
    ax.add_patch(Circle((cx, cy), 0.26, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, zorder=5))
bio.box(ax, (x0 + w / 2, lvl + 0.12), 0.9, 0.24, "rna", radius=0.1, zorder=7)
bio.callout(ax, (x0 + w / 2 + 0.45, lvl + 0.12), (x0 + w + 1.9, lvl + 0.1), "floating food")
bio.callout(ax, (x0 + w - 0.4, ybot + 0.35), (x0 + w + 1.9, ybot + 0.6), "stones dropped in")
reach = ybot + 4.6
ax.plot([x0 - 0.3, x0 + w + 0.3], [reach, reach], color=P.edge("negative"), lw=1.0, ls=(0, (3, 2)), zorder=6)
bio.label(ax, (x0 + w + 0.45, reach), "limit of the beak", size="small", ha="left", color=P.edge("negative"))
bio.arrow(ax, (x0 + w / 2, lvl + 0.35), (x0 + w / 2, reach - 0.15), kind="process", color=P.edge("dna"))
bio.label(ax, (x0 - 0.25, lvl), "water", size="small", ha="right")
ax.add_patch(Circle((x0 + 0.8, ytop + 0.45), 0.26, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8))
bio.arrow(ax, (x0 + 0.8, ytop + 0.15), (x0 + 0.8, ytop - 0.6), kind="process", color=P.muted())

# B: model
pb = quant.Plot(ax, (11.6, 1.7, 9.4, 6.9), (0, 14), (0, 16), xlabel="Objects dropped", ylabel="Water level / cm",
                xticks=[0, 2, 4, 6, 8, 10, 12, 14], yticks=[0, 4, 8, 12, 16])
bio.panel(ax, "B", (9.9, 9.6))
n = np.arange(0, 15)
v, h0, hr = 6.0, 4.0, 10.0
cases = [(1.5, 1.0, "dna", False, "stones, narrow tube"), (2.5, 1.0, "rna", False, "stones, wide tube"),
         (1.5, 0.05, "neutral", True, "foam, narrow tube")]
for r, rho, tok, dash, txt in cases:
    h = h0 + n * rho * v / (np.pi * r ** 2)
    pb.line(n, h, tok, lw=2.0, dashed=dash)
    pb.points(n, h, tok, r=0.07)
    k = int(np.argmax(h >= hr)) if np.any(h >= hr) else None
    if k:
        pb.vline(n[k], token=tok, lw=0.7)
pb.hline(hr, token="negative", text="food reachable", side="left")
pb.text(7.4, 14.8, "stones, narrow tube: 8 needed", ha="left", token="dna")
pb.text(8.6, 5.5, "stones, wide tube: 20 needed", ha="left", token="rna")
pb.text(8.6, 3.0, "foam: level barely rises", ha="left", color=P.muted())
