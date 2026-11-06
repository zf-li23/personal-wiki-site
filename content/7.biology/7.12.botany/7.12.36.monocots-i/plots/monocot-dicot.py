# Monocots versus eudicots (schematic). Top row: monocot; bottom row: eudicot. A: primary stem with
# scattered closed bundles (Zea type) versus a ring of open bundles (Helianthus type). B: young root,
# polyarch with a pith versus tetrarch without pith. C: parallel versus pinnate-reticulate venation.
# D: floral diagram of a trimerous five-whorled flower (Lilium) versus a pentamerous flower.
# E: pollen grain, monosulcate versus tricolpate.
import numpy as np
from matplotlib.patches import Ellipse, Circle
import wikibio as bio
from wikibio import botany, plant

P = bio.P
fig, ax = bio.canvas(34, 16)
XS = [3.6, 10.4, 17.0, 23.6, 30.4]
YM, YD = 11.0, 4.0
heads = ["Stem", "Root", "Venation", "Floral diagram", "Pollen"]
for i, h in enumerate(heads):
    bio.panel(ax, "ABCDE"[i], (XS[i] - 3.0, 15.6))
    bio.label(ax, (XS[i], 15.5), h, size="title")
bio.label(ax, (0.3, YM), "Monocot", size="title", rotation=90)
bio.label(ax, (0.3, YD), "Eudicot", size="title", rotation=90)

botany.stem_section(ax, (XS[0], YM), 2.6, kind="monocot", seed=1)
botany.stem_section(ax, (XS[0], YD), 2.6, kind="eudicot", seed=2)
botany.root_section(ax, (XS[1], YM), 2.6, kind="monocot", hairs=0, seed=3)
botany.root_section(ax, (XS[1], YD), 2.6, kind="eudicot", hairs=0, seed=4)

botany.leaf(ax, (XS[2], YM - 3.0), 5.6, angle=90, shape="linear", width=1.3, venation="parallel", petiole=0,
            tertiary="percurrent")
botany.leaf(ax, (XS[2], YD - 3.0), 4.6, angle=90, shape="ovate", venation="pinnate", tertiary="reticulate",
            petiole=0.8)

plant.floral_diagram(ax, (XS[3], YM), 2.2, [
    dict(organ="tepal", n=3, phase=180, keel=0.35, width=52), dict(organ="tepal", n=3, width=48),
    dict(organ="stamen", n=3), dict(organ="stamen", n=3),
    dict(organ="gynoecium", n=3, placentation="axile", ovules=2, size=0.3)], symmetry="radial")
plant.floral_diagram_from_formula(ax, (XS[3], YD), 2.2, "* K5 C5 A5+5 G_(5:5:2)")


def pollen(c, r, kind):
    if kind == "mono":
        ax.add_patch(Ellipse(c, 2 * r * 1.35, 2 * r * 0.85, facecolor=P.fill("anther"), edgecolor=P.edge("anther"),
                             lw=1.4, zorder=6))
        ax.add_patch(Ellipse(c, 2 * r * 1.1, 0.22 * r, facecolor=P.light("anther"), edgecolor=P.edge("anther"),
                             lw=1.0, zorder=7))
        bio.callout(ax, (c[0] + 0.6 * r, c[1]), (c[0] + 0.6, c[1] - 2.0), "One furrow (sulcus)")
    else:
        ax.add_patch(Circle(c, r, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=1.4, zorder=6))
        for a in (90, 210, 330):
            t = np.radians(a)
            p = (c[0] + 0.62 * r * np.cos(t), c[1] + 0.62 * r * np.sin(t))
            ax.add_patch(Ellipse(p, 0.75 * r, 0.16 * r, angle=a, facecolor=P.light("anther"),
                                 edgecolor=P.edge("anther"), lw=1.0, zorder=7))
        bio.callout(ax, (c[0], c[1] + 0.62 * r), (c[0] + 0.6, c[1] - 2.0 - 0.0), "Three furrows (colpi)")


pollen((XS[4], YM + 0.4), 1.5, "mono")
pollen((XS[4], YD + 0.4), 1.5, "tri")
