"""One gene or two? F2 of albino x brown mice (F1 black): 90 black, 30 brown, 40 albino.
A: observed counts and expected counts under 9:3:4 (two genes, recessive epistasis; chi2 = 0) and 2:1:1
(one gene with a black heterozygote; chi2 = 3.75, 2 df, p = 0.15). B: the breeding test, each F2 albino x
true-breeding brown: predicted fractions of crosses giving all black, half black + half brown, or all brown."""
import numpy as np
from scipy import stats

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24.0, 8.6)
obs = np.array([90, 30, 40])
e1 = np.array([9, 3, 4]) / 16 * 160
e2 = np.array([2, 1, 1]) / 4 * 160
c2 = ((obs - e2) ** 2 / e2).sum()
bio.panel(ax, "A", (0.2, 8.5))
a = charts.axes_at(ax, (1.9, 1.5, 9.5, 6.0))
x = np.arange(3)
a.bar(x - 0.27, obs, 0.26, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.6, label="observed")
a.bar(x, e1, 0.26, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.6, label="9:3:4 (two genes), χ² = 0")
a.bar(x + 0.27, e2, 0.26, color=P.fill("trna"), edgecolor=P.edge("trna"), lw=0.6,
      label=f"2:1:1 (one gene), χ² = {c2:.2f}, p = {stats.chi2.sf(c2, 2):.2f}")
a.set_xticks(x, ["black", "brown", "albino"])
a.set_ylim(0, 115)
charts.style_axes(a, None, "F₂ mice")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")

bio.panel(ax, "B", (12.8, 8.5))
b = charts.axes_at(ax, (14.5, 1.5, 9.0, 6.0))
cats = ["all black", "1/2 black,\n1/2 brown", "all brown"]
two = [0.25, 0.5, 0.25]
one = [1.0, 0.0, 0.0]
x = np.arange(3)
b.bar(x - 0.18, two, 0.34, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.6, label="two-gene model")
b.bar(x + 0.18, one, 0.34, color=P.fill("trna"), edgecolor=P.edge("trna"), lw=0.6, label="one-gene model")
b.set_xticks(x, cats)
b.set_ylim(0, 1.15)
charts.style_axes(b, "progeny of F₂ albino × brown", "fraction of crosses")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
