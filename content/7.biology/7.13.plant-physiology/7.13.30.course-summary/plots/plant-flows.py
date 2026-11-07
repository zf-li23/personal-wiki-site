# The plant as one system: the main flows of matter (left) and of signals (right) in a schematic plant.
# Left: water and mineral ions move up the xylem along a falling water potential (soil -> root -> leaf ->
# air; values typical of a transpiring leaf on a sunny day, air at 50 % relative humidity and 20 C),
# water vapour leaves and CO2 enters through the stomata, and sucrose moves in the phloem from the
# source leaf to the sinks (shoot apex, fruit, root). Right: long-distance signals: ABA and cytokinin
# from the root in the xylem, florigen (FT protein) from the leaf to the shoot apex in the phloem,
# polar auxin transport from the apex downwards, light perceived by phytochromes, cryptochromes and
# phototropins in the leaf, and strigolactone made in the root that inhibits shoot branching.
import numpy as np
from matplotlib.patches import Circle, Rectangle

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(30.0, 18.0)
SOIL = 4.0
X0 = 15.0  # stem axis

# soil and sky
ax.add_patch(Rectangle((0, 0), 30, SOIL, facecolor=P.mix(P.fill("cell_wall"), P.surface(), 0.8), edgecolor="none",
                       zorder=0))
ax.plot([0, 30], [SOIL, SOIL], color=P.edge("cell_wall"), lw=1.2, zorder=1)
bio.label(ax, (0.4, 0.4), "Soil", size="small", bold=True, ha="left", va="bottom", color=P.muted())
bio.label(ax, (0.4, 17.6), "Atmosphere", size="small", bold=True, ha="left", va="top", color=P.muted())
sun = (3.0, 15.4)
ax.add_patch(Circle(sun, 0.9, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.2, zorder=5))
for a in np.linspace(0, 2 * np.pi, 12, endpoint=False):
    ax.plot([sun[0] + 1.15 * np.cos(a), sun[0] + 1.55 * np.cos(a)],
            [sun[1] + 1.15 * np.sin(a), sun[1] + 1.55 * np.sin(a)], color=P.edge("highlight"), lw=1.2, zorder=5)

# stem, leaves, apex, fruit
ax.plot([X0, X0], [SOIL, 15.2], color=P.edge("plant"), lw=5, solid_capstyle="round", zorder=6)
src = B.leaf(ax, (X0, 11.0), 4.0, angle=150, shape="elliptic", venation="pinnate", petiole=0.4, seed=1)
B.leaf(ax, (X0, 7.2), 3.4, angle=28, shape="elliptic", venation="pinnate", petiole=0.4, seed=2)
B.leaf(ax, (X0, 12.4), 3.0, angle=30, shape="elliptic", venation="pinnate", petiole=0.3, seed=3)
B.leaf(ax, (X0, 5.0), 2.2, angle=18, shape="elliptic", venation="pinnate", petiole=0.3, seed=4, token="bract")
apex = (X0, 15.6)
bio.box(ax, apex, 0.9, 0.7, token="positive", radius=0.3)
fruit = (16.9, 10.6)
ax.plot([X0, fruit[0] - 0.3], [10.2, fruit[1] - 0.3], color=P.edge("plant"), lw=2, zorder=5)
ax.add_patch(Circle(fruit, 0.65, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.2, zorder=7))

# roots
rng = np.random.default_rng(0)
for k, (dx, L) in enumerate(((-3.6, 3.2), (-2.0, 3.6), (0.0, 3.8), (2.1, 3.5), (3.7, 3.0))):
    xs = np.linspace(0, 1, 30)
    x = X0 + dx * xs + 0.15 * np.sin(6 * xs + k)
    y = SOIL - L * xs
    ax.plot(x, y, color=P.edge("cell_wall"), lw=2.2 - 0.3 * abs(dx) / 2, zorder=4)
    for j in range(3):
        f = 0.35 + 0.2 * j
        xa, ya = X0 + dx * f, SOIL - L * f
        s = 1 if dx >= 0 else -1
        ax.plot([xa, xa + s * 0.7], [ya, ya - 0.4], color=P.edge("cell_wall"), lw=0.9, zorder=4)

W, C, S, I, SIG = P.edge("dna"), P.muted(), P.edge("petal"), P.edge("k"), P.edge("rna")

# ---- matter (left half) ----
bio.arrow(ax, (14.55, 1.0), (14.55, 10.4), color=W, lw=2.4)
bio.label(ax, (13.4, 8.6), "xylem:\nwater + ions", size="small", ha="right", color=W)
leaf_mid = src["blade"]
bio.arrow(ax, (leaf_mid[0] - 0.6, leaf_mid[1] + 0.6), (9.6, 15.0), color=W, lw=2.0, dashed=True)
bio.label(ax, (9.4, 15.6), "H₂O vapour\nE = g_tw Δw", size="small", ha="right", color=W)
bio.arrow(ax, (6.6, 10.0), (leaf_mid[0] - 0.9, leaf_mid[1] - 0.2), color=C, lw=2.0)
bio.label(ax, (6.4, 10.0), "CO₂\nA = g_c (c_a − c_i)", size="small", ha="right", color=C)
bio.arrow(ax, (sun[0] + 1.3, sun[1] - 1.2), (leaf_mid[0] - 0.4, leaf_mid[1] + 0.3), color=P.edge("highlight"), lw=1.6)
bio.label(ax, (6.6, 14.0), "light", size="small", color=P.edge("highlight"))
# phloem from source leaf to sinks
bio.arrow(ax, (14.0, 10.6), (14.0, 1.6), color=S, lw=2.4)
bio.arrow(ax, (14.3, 13.4), (14.3, 15.1), color=S, lw=2.0)
bio.label(ax, (13.4, 6.0), "phloem:\nsucrose to sinks", size="small", ha="right", color=S)
bio.label(ax, (14.0, 14.3), "to apex", size="small", ha="right", color=S)
# ions from soil
for xi, kind in ((11.0, "k"), (11.9, "cl")):
    bio.ion(ax, (xi, 1.6), kind, text=False)
bio.arrow(ax, (12.6, 1.6), (14.3, 1.6), color=I, lw=1.4)
bio.label(ax, (11.6, 0.6), "K⁺, NO₃⁻, H₂PO₄⁻", size="small", color=I)

# water-potential ladder
for y, txt in ((2.8, "soil  −0.3 MPa"), (4.6, "root  −0.5 MPa"), (11.0, "leaf  −1.2 MPa")):
    bio.label(ax, (0.6, y), txt, size="small", ha="left", color=W)
bio.label(ax, (0.6, 13.2), "air  −93 MPa\n(50 % RH, 20 °C)", size="small", ha="left", color=W)

# ---- signals (right half) ----
bio.arrow(ax, (15.5, 1.4), (15.5, 11.6), color=SIG, lw=1.6, dashed=True)
bio.label(ax, (21.2, 2.4), "ABA, cytokinin (tZ), ACC:\nroot → shoot in the xylem", size="small", ha="left", color=SIG)
ax.plot([15.6, 21.0], [2.4, 2.4], color=SIG, lw=0.6)
bio.arrow(ax, (18.0, 8.2), (15.6, 15.2), color=SIG, lw=1.6, dashed=True, bend=-0.25)
bio.label(ax, (21.2, 9.2), "FT (florigen):\nleaf → apex in the phloem", size="small", ha="left", color=SIG)
ax.plot([18.2, 21.0], [8.6, 9.2], color=SIG, lw=0.6)
bio.arrow(ax, (16.3, 15.2), (16.3, 4.6), color=P.edge("plant"), lw=1.6, dashed=True)
bio.label(ax, (21.2, 14.6), "auxin: polar transport\napex → base (apical dominance)", size="small", ha="left",
          color=P.edge("plant"))
ax.plot([16.4, 21.0], [14.4, 14.6], color=P.edge("plant"), lw=0.6)
bio.label(ax, (21.2, 12.0), "light signals: phy, cry, phot\n(photoperiod, shade, phototropism)", size="small",
          ha="left", color=P.edge("highlight"))
ax.plot([17.6, 21.0], [12.6, 12.2], color=P.edge("highlight"), lw=0.6)
bio.label(ax, (21.2, 5.8), "strigolactone: root → shoot,\ninhibits bud outgrowth", size="small", ha="left",
          color=SIG)
ax.plot([16.4, 21.0], [5.6, 5.8], color=SIG, lw=0.6)
bio.callout(ax, (apex[0] + 0.45, apex[1]), (18.6, 17.0), "shoot apex (sink, meristem)")
bio.callout(ax, (fruit[0] + 0.6, fruit[1] + 0.2), (19.6, 10.9), "fruit (sink)")
