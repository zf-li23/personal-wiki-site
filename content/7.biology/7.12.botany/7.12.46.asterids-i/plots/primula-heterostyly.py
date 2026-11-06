# Distyly in Primula. A: pin (long-styled) flower, stigma at the mouth of the corolla tube, anthers
# half-way down. B: thrum (short-styled) flower, anthers at the mouth, stigma half-way down. Arrows:
# pollen carried at a given height on an insect's proboscis reaches the stigma of the other morph.
# Below: pollen size, stigma papillae and compatibility; thrum plants are hemizygous for the S-locus.
import numpy as np
from matplotlib.patches import Circle, Ellipse

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26, 15)


def flower(cx, pin):
    y0, y1 = 3.6, 10.0
    bio.shape(ax, [(cx - 0.9, y0), (cx + 0.9, y0), (cx + 0.95, y0 + 1.6), (cx + 0.7, y0 + 2.6), (cx - 0.7, y0 + 2.6),
                   (cx - 0.95, y0 + 1.6)], token="sepal", lw=0.9, zorder=3)                     # calyx
    for s in (-1, 1):                                                                         # corolla tube and limb
        bio.shape(ax, [(cx + s * 0.35, y0 + 0.5), (cx + s * 0.6, y0 + 0.5), (cx + s * 0.62, y1), (cx + s * 3.0, y1 + 1.2),
                       (cx + s * 3.0, y1 + 1.6), (cx + s * 0.38, y1 + 0.35)], token="petal", lw=0.9, zorder=4)
    bio.shape(ax, [(cx - 0.32, y0 + 0.3), (cx + 0.32, y0 + 0.3), (cx + 0.3, y0 + 1.2), (cx - 0.3, y0 + 1.2)], token="ovary", lw=0.9, zorder=5)
    style_top = y1 + 0.1 if pin else y0 + 3.6
    anther_y = y0 + 3.6 if pin else y1 - 0.3
    ax.plot([cx, cx], [y0 + 1.2, style_top], color=P.edge("ovary"), lw=1.4, zorder=5)
    ax.add_patch(Circle((cx, style_top + 0.15), 0.28 if pin else 0.2, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=0.8, zorder=6))
    for s in (-1, 1):
        ax.add_patch(Ellipse((cx + s * 0.38, anther_y), 0.24, 0.62, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.7, zorder=6))
    return style_top + 0.15, anther_y


bio.panel(ax, "A", (0.4, 14.8))
bio.label(ax, (6.0, 14.2), "Pin (long-styled)", size="title")
pin_st, pin_an = flower(6.0, True)
bio.panel(ax, "B", (13.4, 14.8))
bio.label(ax, (19.0, 14.2), "Thrum (short-styled)", size="title")
th_st, th_an = flower(19.0, False)
bio.arrow(ax, (19.4, th_an + 0.3), (6.3, pin_st + 0.2), kind="process", bend=-0.25, color=P.muted(), lw=1.0, shrink=0.3)
bio.arrow(ax, (6.4, pin_an), (18.7, th_st), kind="process", bend=0.15, color=P.muted(), lw=1.0, shrink=0.3)
bio.callout(ax, (6.0, pin_st), (2.0, 12.6), "Stigma")
bio.callout(ax, (5.62, pin_an), (2.0, 7.6), "Anthers")
bio.callout(ax, (19.0, th_st), (23.0, 7.6), "Stigma")
bio.callout(ax, (19.38, th_an), (23.0, 12.6), "Anthers")
rows = [("pollen grains", "small", "large"), ("stigma papillae", "long", "short"),
        ("S-locus genotype", "s/s", "S/s (hemizygous S)")]
for i, (k, a, b) in enumerate(rows):
    y = 2.4 - 0.8 * i
    bio.label(ax, (12.5, y), k, size="small")
    bio.label(ax, (6.0, y), a, size="small")
    bio.label(ax, (19.0, y), b, size="small")
bio.label(ax, (12.5, 0.0), "compatible: pin x thrum only (heteromorphic self-incompatibility)", size="tiny")
