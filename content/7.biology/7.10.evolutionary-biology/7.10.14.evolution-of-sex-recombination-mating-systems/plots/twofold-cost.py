"""The twofold cost of males (Theorem 14.1.1).

A: schematic pedigree over three generations: a sexual lineage (each female has one daughter and one son)
and an asexual lineage (each female has two daughters). B: frequency of asexual females when the ratio of
asexual to sexual daughters per female is 2, 1.5 or 1, starting at 0.001: u' = w u with u = p / (1 - p).
"""

import numpy as np
from matplotlib.patches import Circle, Rectangle
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 11.0)
bio.panel(ax, "A", (0.2, 10.8))
bio.label(ax, (1.2, 10.4), "Sexual and asexual lineages", size="small", bold=True, ha="left")


def female(x, y, tok):
    ax.add_patch(Circle((x, y), 0.32, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=5))


def male(x, y):
    ax.add_patch(Rectangle((x - 0.3, y - 0.3), 0.6, 0.6, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"),
                           lw=1.0, zorder=5))


ys = [8.6, 5.6, 2.6]
# sexual lineage
for g, y in enumerate(ys):
    female(2.5, y, "dna")
    if g > 0:
        male(4.0, y)
        ax.plot([2.5, 2.5], [ys[g - 1] - 0.35, y + 0.35], color=P.muted(), lw=1.0)
        ax.plot([2.5, 4.0], [ys[g - 1] - 1.3, ys[g - 1] - 1.3], color=P.muted(), lw=1.0)
        ax.plot([4.0, 4.0], [ys[g - 1] - 1.3, y + 0.32], color=P.muted(), lw=1.0)
bio.label(ax, (3.2, 1.3), "sexual: 1 female", size="tiny", color=P.muted())
# asexual lineage
xs_prev = [9.5]
for g, y in enumerate(ys):
    n = 2 ** g
    xs = [9.5 + (i - (n - 1) / 2) * 1.1 for i in range(n)]
    for i, x in enumerate(xs):
        female(x, y, "rna")
        if g > 0:
            px = xs_prev[i // 2]
            ax.plot([px, x], [ys[g - 1] - 0.35, y + 0.35], color=P.muted(), lw=1.0)
    xs_prev = xs
bio.label(ax, (9.5, 1.3), "asexual: 4 females", size="tiny", color=P.muted())
for y, t in zip(ys, ("generation 1", "generation 2", "generation 3")):
    bio.label(ax, (0.6, y), t, size="tiny", ha="left", color=P.muted(), rotation=0)
female(6.0, 10.0, "dna"); bio.label(ax, (6.5, 10.0), "female", size="tiny", ha="left")
male(8.4, 10.0); bio.label(ax, (8.9, 10.0), "male", size="tiny", ha="left")

pb = C.axes_at(ax, (17.5, 1.8, 11.0, 7.6))
t = np.arange(0, 41)
for w, tok in ((2.0, "negative"), (1.5, "enzyme"), (1.0, "protein")):
    u = 0.001 / 0.999 * w ** t
    pb.plot(t, u / (1 + u), color=C.line(tok), lw=1.9, label=f"relative fitness of asexuals = {w:g}")
pb.set_xlim(0, 40)
pb.set_ylim(0, 1.02)
C.style_axes(pb, "generation", "frequency of asexual females")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "B", (15.7, 10.8))
bio.label(ax, (17.5, 10.4), "An asexual clone takes over", size="small", bold=True, ha="left")
