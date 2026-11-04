"""Size reduction in diatoms (the MacDonald-Pfitzer rule). A: a centric diatom frustule in section; at each
division each daughter keeps one parental valve as its larger epitheca (lid) and builds a new hypotheca inside,
so the daughter that inherits the parental hypotheca is smaller by about twice the thickness of the wall.
B: the consequence for a clone started from one cell of diameter 60 um, with a reduction d = 1 um for the
smaller daughter: after g synchronous divisions the number of cells reduced k times is the binomial coefficient
C(g, k), the mean diameter falls by g d / 2, and cells below a critical size (here 40 um) can restore the
maximal size only through sexual reproduction and an auxospore."""
import numpy as np
from math import comb
from matplotlib.patches import FancyBboxPatch
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(25, 10)


def frustule(x, y, w, epi="dna", hypo="dna", h=1.0, new_hypo=False):
    # epitheca (outer, top) overlaps hypotheca (inner, bottom)
    t = 0.12
    ax.add_patch(FancyBboxPatch((x - w / 2, y), w, h * 0.55, boxstyle="round,pad=0,rounding_size=0.08",
                                facecolor=P.fill("cytoplasm"), edgecolor=P.edge(epi), lw=2.4, zorder=6))
    wi = w - 2 * t
    ax.add_patch(FancyBboxPatch((x - wi / 2, y - h * 0.45), wi, h * 0.7, boxstyle="round,pad=0,rounding_size=0.08",
                                facecolor=P.fill("cytoplasm"), edgecolor=P.edge(hypo), lw=2.4, zorder=5,
                                linestyle="--" if new_hypo else "-"))


bio.panel(ax, "A", (0.2, 9.8))
frustule(5.6, 7.6, 4.0, "dna", "rna")
bio.label(ax, (8.3, 8.0), "epitheca", size="tiny", ha="left")
bio.label(ax, (8.3, 7.2), "hypotheca", size="tiny", ha="left")
bio.arrow(ax, (4.6, 6.7), (3.2, 5.4), kind="process", head=0.16)
bio.arrow(ax, (6.6, 6.7), (8.0, 5.4), kind="process", head=0.16)
frustule(2.9, 4.4, 4.0, "dna", "positive", new_hypo=True)
frustule(8.3, 4.4, 3.5, "rna", "positive", new_hypo=True)
bio.label(ax, (2.9, 3.2), "same size", size="tiny")
bio.label(ax, (8.3, 3.2), "smaller", size="tiny")
bio.label(ax, (5.6, 2.2), "solid: parental valves;  dashed: new valves", size="tiny", color=P.muted())

bio.panel(ax, "B", (11.6, 9.8))
s0, d, crit = 60, 1.0, 40
pl = quant.Plot(ax, (13.2, 1.6, 10.8, 7.4), xlim=(24, 62), ylim=(0, 0.3), xlabel="cell diameter (µm)",
                ylabel="fraction of cells", xticks=[30, 40, 50, 60], yticks=[0, 0.1, 0.2, 0.3])
pl.span(24, crit, token="negative")
pl.text(32, 0.285, "sexual size range", size="tiny")
for g, tok in ((8, "dna"), (24, "positive"), (48, "rna")):
    k = np.arange(g + 1)
    f = np.array([comb(g, int(i)) for i in k], float) / 2.0 ** g
    sz = s0 - d * k
    m = f > 1e-4
    pl.line(sz[m], f[m], token=tok, lw=1.6)
    pl.points(sz[m], f[m], token=tok, r=0.06)
    i = np.argmax(f)
    pl.text(sz[i], f[i] + 0.02, f"g = {g}", size="tiny", token=tok)
