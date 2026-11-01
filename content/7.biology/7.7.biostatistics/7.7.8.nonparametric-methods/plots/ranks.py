"""Ranks discard scale but keep order. Hours of extra sleep of 10 patients given a hypnotic (Cushny and
Peebles 1905, the data of Student 1908). A: the differences on their original scale; the value 4.6 lies
far from the rest. B: the ranks of the absolute differences used by the Wilcoxon signed-rank test (ties
share the average rank, the zero difference is dropped); moving 4.6 to 46 would not change any rank.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
d = np.array([1.2, 2.4, 1.3, 1.3, 0.0, 1.0, 1.8, 0.8, 4.6, 1.4])
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.1))
fig.subplots_adjust(left=0.05, right=0.98, bottom=0.2, top=0.86, wspace=0.15)

ax = axs[0]
order = np.argsort(d)
for k, i in enumerate(order):
    ax.plot(d[i], 0, "o", ms=7, color=charts.line("rna" if d[i] > 0 else "neutral"), zorder=3)
    ax.text(d[i], 0.12 + 0.1 * (k % 2), f"{d[i]:.1f}", fontsize=FT["tiny"], color=P.ink(), ha="center")
ax.axhline(0, color=P.muted(), lw=0.8)
ax.set_ylim(-0.3, 0.5)
ax.set_yticks([])
ax.set_xlim(-0.3, 5)
charts.style_axes(ax, "extra sleep / h", None)
ax.spines["left"].set_visible(False)
charts.title(ax, "A  Original scale")

ax = axs[1]
nz = d[d != 0]
r = stats.rankdata(np.abs(nz))
for k, (v, rv) in enumerate(sorted(zip(nz, r))):
    ax.plot(rv, 0, "o", ms=7, color=charts.line("rna"), zorder=3)
    ax.text(rv, 0.12 + 0.1 * (k % 2), f"{rv:g}", fontsize=FT["tiny"], color=P.ink(), ha="center")
    ax.text(rv, -0.2, f"{v:.1f}", fontsize=FT["tiny"] - 1, color=P.muted(), ha="center")
ax.axhline(0, color=P.muted(), lw=0.8)
ax.set_ylim(-0.3, 0.5)
ax.set_yticks([])
ax.set_xlim(0, 10)
charts.style_axes(ax, "rank of |difference| (value below)", None)
ax.spines["left"].set_visible(False)
charts.title(ax, "B  Ranks: the outlier is just rank 9")
