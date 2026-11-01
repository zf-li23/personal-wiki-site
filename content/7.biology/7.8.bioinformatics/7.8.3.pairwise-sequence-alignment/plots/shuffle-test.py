# Significance by shuffling. Human MCM6 (821 residues) was aligned to yeast Mcm6 (1017 residues) with BLOSUM62
# and affine gaps (11 + k for a gap of length k), and to 300 shuffles of the yeast sequence, which keep its
# composition and length but destroy its order (scores in mcm6-shuffles.csv, computed with Biopython's
# PairwiseAligner). A: global scores; B: local scores. The real scores (arrows, 1608 and 1711) lie 81 and
# 355 standard deviations above the shuffles; the local scores of shuffles are small and right-skewed, the
# shape of the extreme-value distribution of 7.8.4.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
d = np.genfromtxt("mcm6-shuffles.csv", delimiter=",", names=True)
fig, ax = bio.canvas(24.0, 9.0)
for k, (col, real, rect, title) in enumerate([("global", 1608, (1.8, 1.5, 9.4, 6.4), "global (Needleman-Wunsch-Gotoh)"),
                                              ("local", 1711, (14.0, 1.5, 9.4, 6.4), "local (Smith-Waterman-Gotoh)")]):
    a = C.axes_at(ax, rect)
    v = d[col]
    a.hist(v, bins=25, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.6)
    a.axvline(v.mean(), color=P.muted(), lw=0.8, ls=(0, (3, 2)))
    z = (real - v.mean()) / v.std(ddof=1)
    a.annotate(f"real score {real}\n(z = {z:.0f}) off scale", xy=(1.0, 0.55), xycoords="axes fraction",
               xytext=(0.62, 0.8), textcoords="axes fraction", fontsize=bio.core.FONT["tiny"], color=P.ink(),
               arrowprops=dict(arrowstyle="->", color=C.line("negative"), lw=1.0))
    C.style_axes(a, "score of shuffled pair", "count")
    C.title(a, title)
bio.panel(ax, "A", (0.2, 8.7))
bio.panel(ax, "B", (12.4, 8.7))
