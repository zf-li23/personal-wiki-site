# Nodal anatomy. (A) Median longitudinal section through a node: a vascular bundle of the stem bends out
# through the cortex into the petiole (leaf trace); above its departure the vascular cylinder has a
# parenchymatous leaf gap; branch traces from either side of the leaf trace supply the axillary bud.
# (B-D) The vascular cylinder slit along one side and unrolled (vertical lines = bundles; green = the
# traces to one leaf; pale = gaps): unilacunar (one trace, one gap), trilacunar (median and two lateral
# traces, three gaps) and multilacunar nodes (many traces and gaps, as in sheathing leaves).
import numpy as np
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(32.0, 13.0)

# ---- A
bio.panel(ax, "A", (0.2, 12.8))
bio.label(ax, (0.85, 12.77), "Node, longitudinal section", size="title", ha="left", va="top")
cx = 4.2
ax.add_patch(Rectangle((cx - 2.4, 0.6), 4.8, 11.4, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cell_wall"), lw=1.2, zorder=2))
ax.add_patch(Rectangle((cx - 1.0, 0.6), 2.0, 11.4, facecolor=P.mix(P.fill("cytoplasm"), P.surface(), 0.4), edgecolor="none",
                       zorder=2.2))  # pith
for sx in (-1, 1):
    x = cx + sx * 1.25
    if sx == 1:
        ax.add_patch(Rectangle((x - 0.25, 0.6), 0.5, 5.4, facecolor=P.fill("xylem"), edgecolor=P.edge("xylem"), lw=0.8, zorder=3))
        ax.add_patch(Rectangle((x - 0.25, 8.0), 0.5, 4.0, facecolor=P.fill("xylem"), edgecolor=P.edge("xylem"), lw=0.8, zorder=3))
        ax.add_patch(Rectangle((x - 0.25, 6.0), 0.5, 2.0, facecolor=P.light("cytoplasm"), edgecolor=P.edge("cell_wall"), lw=0.6,
                               ls=(0, (2, 2)), zorder=3))
    else:
        ax.add_patch(Rectangle((x - 0.25, 0.6), 0.5, 11.4, facecolor=P.fill("xylem"), edgecolor=P.edge("xylem"), lw=0.8, zorder=3))
# petiole leaving to the right
pet = Polygon([(cx + 2.4, 5.6), (cx + 6.2, 7.6), (cx + 6.4, 8.4), (cx + 2.4, 7.0)], closed=True, facecolor=P.fill("plant"),
              edgecolor=P.edge("plant"), lw=1.0, zorder=2.5)
ax.add_patch(pet)
t = np.linspace(0, 1, 40)[:, None]
p0, p1, p2 = np.array([cx + 1.25, 5.6]), np.array([cx + 1.6, 6.2]), np.array([cx + 6.2, 7.95])
trace = (1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t ** 2 * p2
ax.plot(trace[:, 0], trace[:, 1], color=P.edge("positive"), lw=6, solid_capstyle="round", zorder=4)
# axillary bud in the axil with branch trace
bud = bio.smooth_closed([(cx + 2.4, 7.2), (cx + 2.9, 7.8), (cx + 3.1, 8.6), (cx + 2.7, 8.9), (cx + 2.4, 8.4)], n=60)
ax.add_patch(Polygon(bud, closed=True, facecolor=P.fill("sepal"), edgecolor=P.edge("sepal"), lw=0.9, zorder=3))
bt = np.array([(cx + 1.4, 6.4), (cx + 2.0, 7.4), (cx + 2.7, 8.2)])
ax.plot(bt[:, 0], bt[:, 1], color=P.edge("highlight"), lw=2.5, zorder=4.5, ls=(0, (3, 1.5)))
bio.callout(ax, (cx + 3.4, 6.85), (10.4, 5.0), "Leaf trace")
bio.callout(ax, (cx + 1.25, 7.0), (10.4, 9.8), "Leaf gap")
bio.callout(ax, (cx + 2.1, 7.6), (10.4, 8.6), "Branch trace")
bio.callout(ax, (cx + 2.8, 8.4), (10.4, 11.0), "Axillary bud")
bio.callout(ax, (cx + 5.0, 7.75), (10.4, 6.6), "Petiole")
bio.callout(ax, (cx - 1.25, 3.0), (0.9, 0.3), "Vascular bundle", size="small")
bio.callout(ax, (cx, 2.0), (3.6, 0.3), "Pith", size="small")
bio.callout(ax, (cx - 1.9, 4.0), (6.6, 0.3), "Cortex", size="small")

# ---- B-D: unrolled steles
types = [("B", "Unilacunar", [0]), ("C", "Trilacunar", [-1, 0, 1]), ("D", "Multilacunar", [-3, -2, -1, 0, 1, 2, 3])]
for k, (L, name, traces) in enumerate(types):
    x0 = 13.6 + k * 6.2
    bio.panel(ax, L, (x0 - 0.4, 12.8))
    bio.label(ax, (x0 + 2.6, 12.3), name, size="normal", bold=True)
    n = 9
    xs = np.linspace(x0 + 0.3, x0 + 4.9, n)
    mid = n // 2
    node_y = 6.0
    gap_cols = {mid + d for d in traces}
    for i, x in enumerate(xs):
        if i in gap_cols:
            ax.plot([x, x], [1.0, node_y], color=P.edge("xylem"), lw=2.0, zorder=3)
            ax.plot([x, x], [node_y + 1.8, 11.6], color=P.edge("xylem"), lw=2.0, zorder=3)
            ax.add_patch(Rectangle((x - 0.22, node_y), 0.44, 1.8, facecolor=P.light("highlight"), edgecolor=P.edge("highlight"),
                                   lw=0.6, ls=(0, (2, 2)), zorder=2))
            # the leaf trace leaves the cylinder at the base of its gap (seen end-on where it turns outwards)
            ax.plot([x, x], [node_y - 0.05, node_y + 1.1], color=P.edge("positive"), lw=3.4, zorder=4, solid_capstyle="round")
            ax.add_patch(__import__("matplotlib.patches", fromlist=["Circle"]).Circle((x, node_y + 1.15), 0.16,
                         facecolor=P.fill("positive"), edgecolor=P.edge("positive"), lw=1.0, zorder=4.5))
        else:
            ax.plot([x, x], [1.0, 11.6], color=P.edge("xylem"), lw=2.0, zorder=3)
    bio.label(ax, (x0 + 2.6, 0.5), f"{len(traces)} trace{'s' if len(traces) > 1 else ''}, {len(traces)} gap{'s' if len(traces) > 1 else ''}",
              size="small", color=P.muted())
bio.label(ax, (13.2, 6.9), "node", size="tiny", color=P.muted(), ha="right")
