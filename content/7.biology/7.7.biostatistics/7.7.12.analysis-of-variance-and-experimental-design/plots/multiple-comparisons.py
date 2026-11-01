"""Multiple comparisons. A: probability of at least one false positive when all pairwise two-sample t tests
among k groups are done at alpha = 0.05 with all null hypotheses true: the bound 1 - 0.95^m for m = k(k-1)/2
independent tests, and a simulation (normal data, 10 per group, 2000 repetitions per k) in which the
tests are correlated and the rate is lower, but still far above 0.05. B: ToothGrowth (Crampton 1947;
R datasets::ToothGrowth), doses pooled over delivery: 95 % intervals for the three pairwise differences
of mean length, unadjusted (pooled-variance t, thin) and Tukey simultaneous (thick).
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
ks = np.arange(2, 11)
sim = []
for k in ks:
    X = rng.normal(size=(2000, k, 10))
    m, v = X.mean(2), X.var(2, ddof=1)
    hit = np.zeros(2000, bool)
    for i in range(k):
        for j in range(i + 1, k):
            t = (m[:, i] - m[:, j]) / np.sqrt((v[:, i] + v[:, j]) / 10)
            hit |= np.abs(t) > stats.t.ppf(0.975, 18)
    sim.append(hit.mean())
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.5))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.87, wspace=0.42)
ax = axs[0]
mm = ks * (ks - 1) / 2
ax.plot(ks, 1 - 0.95 ** mm, color=charts.line("neutral"), lw=1.4, ls="--", label="1 - 0.95^m (independent)")
ax.plot(ks, sim, color=charts.line("rna"), lw=1.6, marker="o", ms=4, label="simulated, pairwise t tests")
ax.axhline(0.05, color=P.muted(), lw=0.8, ls=":")
ax.set_ylim(0, 1)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "number of groups k", "family-wise error rate")
charts.title(ax, "A  Error inflation")

with open("toothgrowth.csv") as fh:
    rows = list(csv.DictReader(fh))
y = np.array([float(r["len"]) for r in rows])
dose = np.array([float(r["dose"]) for r in rows])
g = {d: y[dose == d] for d in (0.5, 1.0, 2.0)}
mse = sum(((v - v.mean()) ** 2).sum() for v in g.values()) / 57
se = np.sqrt(mse * 2 / 20)
t = stats.t.ppf(0.975, 57)
q = stats.studentized_range.ppf(0.95, 3, 57) / np.sqrt(2)
ax = axs[1]
pairs = [(1.0, 0.5), (2.0, 0.5), (2.0, 1.0)]
for k, (a, b) in enumerate(pairs):
    d = g[a].mean() - g[b].mean()
    yk = 2 - k
    ax.plot([d - q * se, d + q * se], [yk, yk], color=charts.line("enzyme"), lw=4, solid_capstyle="butt", alpha=0.6)
    ax.plot([d - t * se, d + t * se], [yk, yk], color=charts.line("dna"), lw=1.4)
    ax.scatter([d], [yk], s=24, color=P.ink(), zorder=3)
    ax.text(d, yk + 0.2, f"{d:.2f}", fontsize=FT["tiny"], color=P.ink(), ha="center")
ax.axvline(0, color=P.muted(), lw=0.8, ls="--")
ax.set_yticks([2, 1, 0])
ax.set_yticklabels(["1 - 0.5", "2 - 0.5", "2 - 1"], fontsize=FT["tiny"])
ax.set_ylim(-0.6, 2.7)
ax.set_xlim(-1, 20)
charts.style_axes(ax, "difference in mean length")
charts.title(ax, "B  Tukey (thick) vs unadjusted (thin)")
