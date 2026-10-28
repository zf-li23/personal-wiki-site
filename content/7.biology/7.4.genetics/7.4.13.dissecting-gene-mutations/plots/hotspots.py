"""Mutational hotspots: number of independent spontaneous mutations per site, simulated.
1600 spontaneous mutations fall on 400 mutable sites of a gene. Most sites have low, gamma-distributed rates; two
hotspot sites have rates about 100 times the median. (A) Mutations per site along the gene. (B) Number of sites
with k = 0, 1, 2, ... occurrences (bars, hotspots off scale) compared with the Poisson expectation for equal rates
(points, same mean): the excess of sites with 0 and 1 occurrences and of sites with many occurrences shows that
rates differ among sites. Simulated data; the shape, not the numbers, follows Benzer's rII observations."""

import numpy as np
from scipy.stats import poisson

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(1)

S, n = 400, 1600
w = rng.gamma(0.8, 1.0, S)
hot = [120, 310]
w[hot] = np.median(w) * np.array([110, 60])
counts = rng.multinomial(n, w / w.sum())

fig, ax = bio.canvas(16.0, 7.6)
bio.panel(ax, "A", (0.1, 7.5))
a = charts.axes_at(ax, (1.9, 1.3, 5.6, 5.6))
a.vlines(np.arange(S), 0, counts, color=charts.line("dna"), lw=0.8)
for h in hot:
    a.text(h, counts[h] + 8, "hotspot", fontsize=FT["tiny"], color=P.ink(), ha="center")
a.set_xlim(0, S)
a.set_ylim(0, None)
charts.style_axes(a, "site along the gene", "independent mutations")

bio.panel(ax, "B", (8.3, 7.5))
b = charts.axes_at(ax, (10.1, 1.3, 5.6, 5.6))
k = np.arange(0, 16)
obs = np.array([(counts == i).sum() for i in k])
b.bar(k, obs, color=charts.line("dna"), width=0.7, label="observed sites")
b.plot(k, S * poisson.pmf(k, n / S), "o-", color=charts.line("negative"), ms=4, lw=1.2,
       label=f"Poisson, mean {n / S:g}")
b.text(15, max(obs) * 0.6, f"beyond the axis: two sites\nwith {counts[hot[1]]} and {counts[hot[0]]} mutations", fontsize=FT["tiny"],
       color=P.ink(), ha="right")
b.set_xlim(-0.6, 15.6)
b.set_xticks(range(0, 16, 3))
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(b, "mutations per site k", "number of sites")
