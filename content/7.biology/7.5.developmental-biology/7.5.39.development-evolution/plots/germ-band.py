"""Long-germ and short-germ development in insects (schematic, after Davis and Patel and Wolpert et al.).

A: blastoderm fate maps, anterior to the left. In the long-germ fly Drosophila the embryonic anlage covers most
of the blastoderm and contains all future segments (head, thorax, abdomen); in the short-germ beetle
Tribolium castaneum the germ rudiment covers the posterior part and contains the head, part of the thorax and
a posterior growth zone, the rest being extraembryonic serosa; in the "extreme short-germ" grasshopper
Schistocerca a small posterior disc forms the head lobes and the growth zone. B: number of segments
specified against developmental time (relative): simultaneous in long-germ insects, sequential in short-germ
insects, where a segmentation clock in the growth zone adds one segment per period (one segment pair per
oscillation of the pair-rule genes in Tribolium).
"""

import numpy as np
from matplotlib.patches import Ellipse, Polygon
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(30.0, 11.0)


def egg(cy, name, regions):
    cx, a, b = 7.5, 5.5, 1.3
    ax.add_patch(Ellipse((cx, cy), 2 * a, 2 * b, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=1.0, zorder=4))
    for x0, x1, tok, lab in regions:
        xs = np.linspace(cx - a + 2 * a * x0, cx - a + 2 * a * x1, 60)
        top = cy + b * np.sqrt(np.clip(1 - ((xs - cx) / a) ** 2, 0, 1))
        bot = cy - b * np.sqrt(np.clip(1 - ((xs - cx) / a) ** 2, 0, 1))
        ax.add_patch(Polygon(np.r_[np.c_[xs, top], np.c_[xs[::-1], bot[::-1]]], closed=True, facecolor=P.fill(tok),
                             edgecolor=P.edge(tok), lw=0.7, zorder=5))
        if lab:
            bio.label(ax, ((xs[0] + xs[-1]) / 2, cy), lab, size="tiny", color=P.on_fill(), zorder=12)
    bio.label(ax, (cx - a - 0.3, cy), name, size="small", italic=True, ha="right")


bio.panel(ax, "A", (0.2, 10.7))
egg(8.8, "Drosophila", [(0.08, 0.32, "dna", "head"), (0.32, 0.5, "positive", "thorax"), (0.5, 0.95, "drug", "abdomen")])
egg(5.6, "Tribolium", [(0.45, 0.68, "dna", "head"), (0.68, 0.8, "positive", "th."), (0.8, 0.98, "highlight", "growth zone")])
egg(2.4, "Schistocerca", [(0.8, 0.88, "dna", "h"), (0.88, 0.99, "highlight", "gz")])
bio.label(ax, (7.5, 0.5), "grey: extraembryonic tissue (serosa, amnioserosa)", size="tiny", color=P.muted())

pa = charts.axes_at(ax, (18.5, 1.8, 10.5, 7.6))
t = np.linspace(0, 1, 400)
long_germ = np.where(t > 0.2, 15, 0)
short = np.clip(np.floor((t - 0.1) / 0.06) + 3, 0, 15) * (t > 0.1)
pa.plot(t, long_germ, color=charts.line("drug"), lw=1.8, label="long germ: all at once")
pa.plot(t, short, color=charts.line("dna"), lw=1.8, label="short germ: one by one")
pa.set_ylim(0, 17)
pa.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(pa, "developmental time (relative)", "segments specified")
bio.panel(ax, "B", (16.8, 10.7))
