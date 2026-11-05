# Lauraceae. A: floral diagram of Cinnamomum: tepals 3 + 3, stamens in four whorls of three (the third
# whorl extrorse, the fourth reduced to staminodes), a single carpel. B-E: stamens seen from the inner
# side. B: stamen of whorls 1 and 2, anther with four locules opening by upward-lifting valves (flaps),
# introrse. C: stamen of whorl 3, extrorse, with a pair of glands at the base of the filament. D: a
# staminode of whorl 4. E: two-locular anther of Lindera. F-H: fruits. F: drupe of camphor tree seated in
# a shallow cup (the persistent floral tube); G: Phoebe, persistent tepals erect and clasping the fruit
# base; H: Machilus, persistent tepals reflexed.
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon, Wedge
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(34, 13)

bio.panel(ax, "A", (0.3, 12.7))
bio.label(ax, (4.2, 12.3), r"$\it{Cinnamomum}$", size="title")
plant.floral_diagram(ax, (4.2, 6.6), 3.0, [
    dict(organ="tepal", n=3, phase=0, r=0.98, width=32),
    dict(organ="tepal", n=3, phase=60, r=0.84, width=30),
    dict(organ="stamen", n=3, phase=0, r=0.68),
    dict(organ="stamen", n=3, phase=60, r=0.56),
    dict(organ="stamen", n=3, phase=0, r=0.44),
    dict(organ="staminode", n=3, phase=60, r=0.33),
    dict(organ="gynoecium", n=1, placentation="basal", ovules=1, size=0.2),
], symmetry="radial")
bio.label(ax, (4.2, 1.3), "P3+3, A3+3+3+3 (4th whorl staminodes), G1", size="small")


def anther(x, y, locules=4, extrorse=False, glands=False, label=None):
    ax.add_patch(Polygon([(x - 0.13, y - 3.0), (x + 0.13, y - 3.0), (x + 0.11, y), (x - 0.11, y)], closed=True,
                         facecolor=P.fill("petal"), edgecolor=P.edge("petal"), lw=0.9, zorder=4))
    ax.add_patch(FancyBboxPatch((x - 0.65, y), 1.3, 2.0, boxstyle="round,pad=0.02,rounding_size=0.3",
                                facecolor=P.fill("anther") if not extrorse else P.light("anther"),
                                edgecolor=P.edge("anther"), lw=1.1, zorder=5))
    rows = [(y + 0.55, y + 1.45)] if locules == 4 else [(y + 1.0,)]
    pos = [(-0.3, y + 0.55), (0.3, y + 0.55), (-0.3, y + 1.45), (0.3, y + 1.45)] if locules == 4 else \
        [(-0.3, y + 1.0), (0.3, y + 1.0)]
    for dx, yy in pos:
        ax.add_patch(Ellipse((x + dx, yy), 0.42, 0.55, facecolor=P.fill("ovule"), edgecolor=P.edge("anther"), lw=0.8,
                             zorder=6))
        ax.add_patch(Polygon([(x + dx - 0.2, yy + 0.25), (x + dx + 0.2, yy + 0.25), (x + dx + 0.28, yy + 0.75),
                              (x + dx - 0.12, yy + 0.8)], closed=True, facecolor=P.fill("anther"),
                             edgecolor=P.edge("anther"), lw=0.8, zorder=7))
    if glands:
        for s in (-1, 1):
            ax.add_patch(Ellipse((x + s * 0.42, y - 2.3), 0.55, 0.75, facecolor=P.fill("highlight"),
                                 edgecolor=P.edge("highlight"), lw=0.9, zorder=6))
    if label:
        bio.label(ax, (x, y - 3.7), label, size="small")


bio.panel(ax, "B", (9.0, 12.7))
anther(10.4, 6.4, label="Whorls 1-2")
bio.callout(ax, (10.85, 8.25), (11.9, 10.4), "Valve (flap)", size="small")
bio.panel(ax, "C", (12.6, 12.7))
anther(14.0, 6.4, extrorse=True, glands=True, label="Whorl 3")
bio.callout(ax, (14.42, 4.1), (15.6, 2.4), "Glands", size="small")
bio.panel(ax, "D", (16.2, 12.7))
ax.add_patch(Polygon([(17.47, 3.4), (17.73, 3.4), (17.7, 6.3), (18.2, 6.6), (17.6, 7.7), (17.0, 6.6), (17.5, 6.3)],
                     closed=True, facecolor=P.fill("atp"), edgecolor=P.edge("atp"), lw=1.0, zorder=5))
bio.label(ax, (17.6, 2.7), "Whorl 4: staminode", size="small")
bio.panel(ax, "E", (19.6, 12.7))
anther(21.0, 6.4, locules=2, label=r"$\it{Lindera}$: 2 locules")

# fruits
def berry(c, r=0.95):
    ax.add_patch(Ellipse(c, 2 * r, 2.2 * r, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=1.1,
                         zorder=5))


bio.panel(ax, "F", (23.8, 12.7))
berry((25.4, 7.6))
ax.add_patch(Wedge((25.4, 6.4), 0.95, 200, 340, width=0.45, facecolor=P.fill("plant"), edgecolor=P.edge("plant"),
                   lw=1.1, zorder=6))
ax.plot([25.4, 25.4], [3.4, 6.0], color=P.edge("plant"), lw=2.2, zorder=4)
bio.label(ax, (25.4, 2.7), "Cupule", size="small")
bio.label(ax, (25.4, 11.0), "Camphor tree", size="small")
bio.panel(ax, "G", (27.2, 12.7))
berry((28.8, 7.8))
for s in (-1, 0, 1):
    ax.add_patch(Polygon([(28.8 + s * 0.45 - 0.22, 6.2), (28.8 + s * 0.45 + 0.22, 6.2), (28.8 + s * 0.6, 7.2)],
                         closed=True, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=7))
ax.plot([28.8, 28.8], [3.4, 6.2], color=P.edge("plant"), lw=2.2, zorder=4)
bio.label(ax, (28.8, 2.7), "Erect tepals", size="small")
bio.label(ax, (28.8, 11.0), r"$\it{Phoebe}$", size="small")
bio.panel(ax, "H", (30.6, 12.7))
berry((32.2, 7.8))
for s in (-1, 1):
    ax.add_patch(Polygon([(32.2 + s * 0.1, 6.25), (32.2 + s * 0.35, 6.15), (32.2 + s * 1.15, 5.4)], closed=True,
                         facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=7))
ax.plot([32.2, 32.2], [3.4, 6.2], color=P.edge("plant"), lw=2.2, zorder=4)
bio.label(ax, (32.2, 2.7), "Reflexed tepals", size="small")
bio.label(ax, (32.2, 11.0), r"$\it{Machilus}$", size="small")
