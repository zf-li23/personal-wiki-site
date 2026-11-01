"""Antibody titres of 112 children one month after vaccination (reciprocal dilutions 4 to 512, a classic
textbook example). A: on the linear scale the distribution is skewed and the arithmetic mean (69.3) is pulled
by the few high titres. B: on a log2 scale the dilution steps are equally spaced and the distribution is
nearly symmetric; the mean of log2(titre) is 5.57, and its antilog, the geometric mean, is 47.6 (about 1:48).
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
titre = np.array([4, 8, 16, 32, 64, 128, 256, 512])
count = np.array([1, 3, 15, 32, 43, 11, 5, 2])
x = np.repeat(titre, count)
am = x.mean()
gm = np.exp(np.log(x).mean())
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.3))
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.17, top=0.87, wspace=0.22)
ax = axs[0]
ax.bar(titre, count, width=10, color=P.fill("antibody"), edgecolor=P.edge("antibody"), lw=0.8)
ax.axvline(am, color=charts.line("rna"), lw=1.2, label=f"arithmetic mean {am:.1f}")
ax.axvline(gm, color=charts.line("dna"), lw=1.2, ls="--", label=f"geometric mean {gm:.1f}")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, "titre (reciprocal dilution)", "children")
charts.title(ax, "A  Linear scale")
ax = axs[1]
k = np.log2(titre)
ax.bar(k, count, width=0.7, color=P.fill("antibody"), edgecolor=P.edge("antibody"), lw=0.8)
ax.axvline(np.log2(x).mean(), color=charts.line("dna"), lw=1.2, ls="--", label=f"mean of log2 = {np.log2(x).mean():.2f}")
ax.set_xticks(k)
ax.set_xticklabels([f"1:{t}" for t in titre], fontsize=FT["tiny"])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, "titre (log2 scale)", None)
charts.title(ax, "B  Log scale: dilution steps are equal")
