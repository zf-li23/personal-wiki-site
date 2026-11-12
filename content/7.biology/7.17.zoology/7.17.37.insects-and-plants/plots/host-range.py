# Diet breadth of phytophagous insects (schematic): proportion of species feeding on k plant families
# under a discrete truncated Pareto distribution p(k) ~ k^-a, k = 1..K, the form fitted to global rearing
# records by Forister and coauthors (2015). Exponents are illustrative, not fitted values.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(16, 9.5)
a = charts.axes_at(ax, (1.8, 1.4, 13.4, 7.4))
K = 15
k = np.arange(1, K + 1)
for expo, lab, tok, off in [(2.6, "steeper exponent (more specialized, e.g. tropical)", "positive", -0.2),
                            (1.8, "shallower exponent (e.g. temperate)", "negative", 0.2)]:
    p = k ** -expo
    p /= p.sum()
    a.bar(k + off, p, width=0.38, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.6, label=lab)
a.set_xticks(k)
a.set_xlabel("Number of plant families in the diet, k")
a.set_ylabel("Proportion of insect species")
a.set_ylim(0, 0.8)
a.legend(fontsize=7, frameon=False, loc="upper right")
ins = charts.axes_at(ax, (8.8, 3.6, 5.6, 2.9))
ex = np.linspace(1.4, 3.2, 50)
mean = [(k * k ** -e).sum() / (k ** -e).sum() for e in ex]
ins.plot(ex, mean, color=P.edge("enzyme"), lw=1.6, label="mean")
ins.plot(ex, np.ones_like(ex), color=P.muted(), lw=1.2, ls="--", label="median")
ins.set_xlabel("exponent a", fontsize=6)
ins.set_ylabel("families", fontsize=6)
ins.tick_params(labelsize=6)
ins.legend(fontsize=6, frameon=False)
