# Apiaceae. A: compound umbel in side view: rays from the top of the peduncle with an involucre at their
# base; each ray ends in an umbellet with an involucel; marginal flowers with enlarged outer petals.
# B: flower: five free petals with inflexed tips, five stamens, inferior ovary topped by the swollen
# stylopodium and two styles. C: mature cremocarp splitting into two mericarps suspended from the forked
# carpophore. D: cross-section of a dorsally compressed cremocarp (schematic): each mericarp with five
# primary ribs, the lateral ribs winged, one oil duct (vitta) under each furrow and two on the commissure.
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, Polygon
from wikibio import botany

P = bio.P
fig, ax = bio.canvas(36, 12.5)
bio.panel(ax, "A", (0.3, 12.2))
bio.label(ax, (5.2, 11.8), "Compound umbel", size="title")
botany.inflorescence(ax, (5.2, 0.6), 10.0, kind="compound umbel")

bio.panel(ax, "B", (11.0, 12.2))
bio.label(ax, (14.0, 11.8), "Flower", size="title")
c = np.array([14.0, 5.0])
ax.add_patch(Ellipse(c - [0, 1.4], 1.4, 1.8, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=4))
ax.add_patch(Ellipse(c - [0, 0.35], 1.3, 0.55, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=6))
for s in (-1, 1):
    ax.plot([c[0] + s * 0.15, c[0] + s * 0.7], [c[1] - 0.2, c[1] + 1.4], color=P.edge("ovary"), lw=1.4, zorder=7)
    for k, dx in enumerate((1.2, 2.3)):
        x0 = c[0] + s * dx
        ax.add_patch(Ellipse((x0, c[1] + 0.6 + 0.3 * k), 1.0, 1.7, angle=-s * (25 + 15 * k), facecolor=P.fill("petal"),
                             edgecolor=P.edge("petal"), lw=0.9, zorder=5))
        ax.plot([c[0] + s * 0.4, c[0] + s * (dx - 0.4)], [c[1] - 0.4, c[1] + 2.2 + 0.2 * k], color=P.edge("anther"), lw=1.0, zorder=6)
        ax.add_patch(Ellipse((c[0] + s * (dx - 0.4), c[1] + 2.3 + 0.2 * k), 0.4, 0.3, facecolor=P.fill("anther"),
                             edgecolor=P.edge("anther"), zorder=7))
bio.callout(ax, c + [0.5, -0.3], (16.8, 2.4), "Stylopodium (disc)", size="small")
bio.callout(ax, c + [0, -1.8], (11.6, 1.4), "Inferior ovary", size="small")
bio.callout(ax, c + [0.65, 1.3], (16.6, 9.6), "Styles (2)", size="small")

bio.panel(ax, "C", (19.0, 12.2))
bio.label(ax, (21.6, 11.8), "Cremocarp", size="title")
b = np.array([21.6, 1.6])
ax.plot([b[0], b[0]], [b[1], b[1] + 6.4], color=P.edge("plant"), lw=1.6, zorder=4)
for s in (-1, 1):
    ax.plot([b[0], b[0] + s * 0.4], [b[1] + 6.4, b[1] + 7.2], color=P.edge("plant"), lw=1.4, zorder=4)
    ax.add_patch(Ellipse((b[0] + s * 1.0, b[1] + 4.3), 1.3, 5.6, angle=s * 6, facecolor=P.fill("ovary"),
                         edgecolor=P.edge("ovary"), lw=1.1, zorder=5))
    for k in (-0.3, 0.0, 0.3):
        ax.plot([b[0] + s * (1.0 + k), b[0] + s * (1.0 + k) + s * 0.25], [b[1] + 1.7, b[1] + 6.9], color=P.edge("ovary"),
                lw=0.7, zorder=6)
bio.callout(ax, (b[0], b[1] + 6.8), (24.2, 10.6), "Carpophore", size="small")
bio.callout(ax, (b[0] + 1.5, b[1] + 3.0), (24.2, 2.0), "Mericarp", size="small")

bio.panel(ax, "D", (26.0, 12.2))
bio.label(ax, (31.0, 11.8), "Cross-section", size="title")
c = np.array([31.0, 6.0])
for s in (1, -1):
    pts = []
    for t in np.linspace(0, np.pi, 60):
        r = 1.9
        x = 3.6 * np.cos(t)
        y = s * (0.15 + r * np.sin(t))
        pts.append(c + [x, y])
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.1, zorder=4))
    ax.add_patch(Ellipse(c + [0, s * 0.9], 3.4, 1.1, facecolor=P.light("ovary"), edgecolor=P.edge("ovary"), lw=0.8, zorder=5))
    for k, x in enumerate((-3.6, -1.6, 0.0, 1.6, 3.6)):
        y = s * (0.15 + 1.9 * np.sqrt(max(0.0, 1 - (x / 3.6) ** 2)))
        if abs(x) == 3.6:
            ax.add_patch(Polygon([c + [x, s * 0.15], c + [x + np.sign(x) * 1.2, s * 0.3], c + [x, s * 0.6]],
                                 closed=True, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=4))
        else:
            ax.add_patch(Circle(c + [x, y], 0.22, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=6))
    for x in (-2.6, -0.8, 0.8, 2.6):
        y = s * (0.15 + 1.9 * np.sqrt(max(0.0, 1 - (x / 3.6) ** 2)) - 0.35)
        ax.add_patch(Circle(c + [x, y], 0.16, facecolor=P.fill("atp"), edgecolor=P.edge("atp"), lw=0.8, zorder=7))
for x in (-0.7, 0.7):
    ax.add_patch(Circle(c + [x, 0.0], 0.15, facecolor=P.fill("atp"), edgecolor=P.edge("atp"), lw=0.8, zorder=7))
ax.plot([c[0] - 3.6, c[0] + 3.6], [c[1], c[1]], color=P.edge("ovary"), lw=0.9, ls="--", zorder=6)
bio.callout(ax, c + [-4.6, 0.3], (26.2, 9.0), "Lateral rib (wing)", size="small")
bio.callout(ax, c + [0, 2.05], (30.2, 10.4), "Dorsal rib", size="small")
bio.callout(ax, c + [-2.6, 1.45], (26.4, 2.6), "Vitta (oil duct)", size="small")
bio.callout(ax, c + [0.7, 0.0], (34.0, 2.2), "Commissure", size="small")
bio.callout(ax, c + [1.5, 0.9], (34.6, 9.4), "Seed", size="small")
