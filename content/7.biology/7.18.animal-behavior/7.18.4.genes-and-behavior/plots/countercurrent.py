"""Benzer's countercurrent phototaxis apparatus: schematic and binomial distributions after n = 10 trials."""

import math
import numpy as np
from matplotlib.patches import FancyBboxPatch
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 11.0)
bio.panel(ax, "A", (0.3, 10.7))
# two rows of tubes, light on the right
for r, y in enumerate([7.6, 5.6]):
    for i in range(6):
        x = 1.0 + 1.6 * i + (0.8 if r == 1 else 0)
        ax.add_patch(FancyBboxPatch((x, y), 1.3, 0.8, boxstyle="round,pad=0,rounding_size=0.35",
                                    facecolor=P.mix(P.fill("neutral"), P.surface(), 0.7), edgecolor=P.edge("neutral"), lw=1.0, zorder=5))
for i in range(5):
    x = 1.0 + 1.6 * i
    bio.arrow(ax, (x + 1.0, 7.55), (x + 1.4, 6.45), kind="process", color=P.edge("highlight"))
bio.label(ax, (11.6, 6.9), "light", size="small", color=P.edge("highlight"))
for k in range(6):
    ax.plot([11.0 + 0.5 * math.cos(a) for a in [k * math.pi / 6]], [6.9], alpha=0)
ax.plot([11.0, 11.0], [5.6, 8.4], color=P.edge("highlight"), lw=3)
bio.label(ax, (5.4, 9.2), "flies that walk toward the light pass to the next tube", size="small")
bio.label(ax, (5.4, 4.6), "after n trials: n + 1 tubes", size="small", color=P.muted())
bio.label(ax, (5.4, 3.8), "k = number of moves toward light", size="small", color=P.muted())
# fly icons not needed; panel B
n = 10
k = np.arange(n + 1)
pb = C.axes_at(ax, (15.0, 1.8, 14.2, 8.0))
w = 0.27
for j, (p, tok, lab) in enumerate([(0.15, "dna", "mutant, p = 0.15"), (0.5, "neutral", "p = 0.5"),
                                   (0.85, "negative", "wild type, p = 0.85")]):
    pk = [math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in k]
    pb.bar(k + (j - 1) * w, pk, width=w, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.6, label=lab)
leg = pb.legend(frameon=False, fontsize=FS["tiny"], loc="upper center")
for t in leg.get_texts():
    t.set_color(P.ink())
pb.set_xticks(k)
pb.set_ylim(0, 0.45)
C.style_axes(pb, "tube k (number of moves toward the light)", "fraction of flies")
bio.panel(ax, "B", (13.4, 10.7))
