"""Myogenesis: lineage from dermomyotome to myofibre (with a satellite cell), and the MRF regulatory hierarchy."""
import numpy as np
from matplotlib.patches import Ellipse, FancyBboxPatch, Circle
import wikibio as bio

fig, ax = bio.canvas(26, 11.5)
P = bio.P


def cell(xy, rx, ry, tok, angle=0, nuc=True):
    ax.add_patch(Ellipse(xy, 2 * rx, 2 * ry, angle=angle, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=5))
    if nuc:
        ax.add_patch(Ellipse(xy, rx * 0.8, ry * 0.8, angle=angle, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"),
                             lw=0.7, zorder=6))


bio.panel(ax, "A", (0.2, 11.2))
y = 8.4
# dermomyotome epithelium
for k in range(5):
    ax.add_patch(FancyBboxPatch((0.6 + k * 0.42, y - 0.6), 0.38, 1.2, boxstyle="round,pad=0,rounding_size=0.08",
                                facecolor=P.fill("rrna"), edgecolor=P.edge("rrna"), lw=0.8, zorder=5))
    ax.add_patch(Circle((0.79 + k * 0.42, y), 0.11, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.6, zorder=6))
bio.label(ax, (1.6, y + 1.2), "Dermomyotome", size="small")
bio.label(ax, (1.6, y - 1.1), "Pax3, Pax7", size="tiny", italic=True)
bio.arrow(ax, (2.9, y), (4.0, y), kind="process")
bio.label(ax, (3.45, y + 0.45), "Wnt, Shh;", size="tiny")
bio.label(ax, (3.45, y - 0.45), "BMP blocked", size="tiny")
# myoblasts dividing
for k, (dx, dy) in enumerate(((4.7, 0.5), (4.7, -0.5), (5.7, 0.0))):
    cell((dx, y + dy), 0.42, 0.3, "muscle")
bio.label(ax, (5.2, y + 1.2), "Myoblasts", size="small")
bio.label(ax, (5.2, y - 1.1), "Myf5, MyoD", size="tiny", italic=True)
bio.label(ax, (5.2, y - 1.45), "divide while FGF high", size="tiny", color=P.muted())
bio.arrow(ax, (6.4, y), (7.5, y), kind="process")
bio.label(ax, (6.95, y + 0.45), "exit cycle", size="tiny")
# aligned
for k in range(4):
    cell((8.4 + k * 0.95, y), 0.5, 0.26, "muscle")
bio.label(ax, (9.8, y + 1.2), "Alignment", size="small")
bio.label(ax, (9.8, y - 1.1), "myogenin, MEF2", size="tiny", italic=True)
bio.arrow(ax, (11.6, y), (12.5, y), kind="process")
bio.label(ax, (11.9, y + 0.45), "fusion", size="tiny")
bio.label(ax, (11.9, y - 0.45), "Myomaker", size="tiny")
bio.label(ax, (11.9, y - 0.8), "Myomixer", size="tiny")
# myotube
ax.add_patch(FancyBboxPatch((12.7, y - 0.32), 4.0, 0.64, boxstyle="round,pad=0,rounding_size=0.3",
                            facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=1.0, zorder=5))
for k in range(5):
    ax.add_patch(Ellipse((13.2 + k * 0.75, y), 0.4, 0.26, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.6, zorder=6))
bio.label(ax, (14.7, y + 1.2), "Myotube", size="small")
bio.label(ax, (14.7, y - 1.1), "central nuclei", size="tiny", color=P.muted())
bio.arrow(ax, (17.0, y), (18.0, y), kind="process")
bio.label(ax, (17.5, y + 0.45), "mature", size="tiny")
# myofibre with striations and peripheral nuclei, basal lamina and satellite cell
x0, x1 = 18.3, 25.4
ax.add_patch(FancyBboxPatch((x0, y - 0.55), x1 - x0, 1.1, boxstyle="round,pad=0,rounding_size=0.25",
                            facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=1.0, zorder=5))
for xs in np.arange(x0 + 0.25, x1 - 0.1, 0.22):
    ax.plot([xs, xs], [y - 0.45, y + 0.45], color=P.edge("muscle"), lw=0.6, zorder=6)
for k in range(5):
    ax.add_patch(Ellipse((x0 + 0.7 + k * 1.45, y - 0.48), 0.5, 0.16, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"),
                         lw=0.6, zorder=7))
ax.plot([x0 - 0.05, x1 + 0.05], [y + 0.78, y + 0.78], color=P.edge("enzyme"), lw=1.4, zorder=6)
cell((21.6, y + 0.66), 0.38, 0.12, "positive", nuc=False)
bio.label(ax, (21.85, y + 1.2), "Myofibre", size="small")
bio.callout(ax, (21.6, y + 0.66), (23.6, y + 1.55), "Satellite cell (Pax7)")
bio.callout(ax, (24.6, y + 0.78), (25.0, y + 2.2), "Basal lamina")

bio.panel(ax, "B", (0.2, 5.0))
yb = 2.6
nodes = {"pax": (2.4, yb, "Pax3 / Pax7", "rrna"), "myf5": (6.5, yb + 1.2, "Myf5", "muscle"),
         "myod": (6.5, yb - 1.2, "MyoD", "muscle"), "myog": (11.0, yb + 1.2, "myogenin", "drug"),
         "mrf4": (11.0, yb - 1.2, "MRF4", "drug"), "mef2": (14.6, yb + 2.1, "MEF2", "enzyme"),
         "genes": (16.6, yb, "muscle genes", "protein"), "myostatin": (20.6, yb + 1.3, "myostatin", "negative"),
         "fgf": (20.6, yb - 1.3, "FGF (mitogens)", "neutral")}
for k, (x, y_, t, tok) in nodes.items():
    bio.box(ax, (x, y_), 2.9 if k == "genes" or k == "fgf" else 2.3, 0.85, token=tok, text=t, size="small",
            italic=k in ("pax",) and False)
bio.arrow(ax, (3.55, yb + 0.25), (5.35, yb + 1.1), kind="activation")
bio.arrow(ax, (3.55, yb - 0.25), (5.35, yb - 1.1), kind="activation")
bio.arrow(ax, (6.3, yb + 0.78), (6.3, yb - 0.78), kind="activation")
bio.arrow(ax, (6.7, yb - 0.78), (6.7, yb + 0.78), kind="activation")
bio.arrow(ax, (7.65, yb + 1.2), (9.85, yb + 1.2), kind="activation")
bio.arrow(ax, (7.65, yb - 1.2), (9.85, yb - 1.2), kind="activation")
bio.arrow(ax, (12.15, yb + 1.0), (15.1, yb + 0.3), kind="activation")
bio.arrow(ax, (12.15, yb - 1.0), (15.1, yb - 0.3), kind="activation")
bio.arrow(ax, (14.9, yb + 1.68), (16.2, yb + 0.43), kind="activation")
bio.arrow(ax, (19.45, yb + 1.1), (18.1, yb + 0.3), kind="inhibition")
bio.arrow(ax, (19.15, yb - 1.1), (18.1, yb - 0.3), kind="inhibition")
bio.label(ax, (6.5, yb + 2.0), "determination", size="tiny", color=P.muted())
bio.label(ax, (11.0, yb + 2.0), "differentiation", size="tiny", color=P.muted())
bio.label(ax, (7.25, yb), "cross-activation", size="tiny", ha="left", color=P.muted())
