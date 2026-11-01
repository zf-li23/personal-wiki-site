"""Exact permutation test: odontoblast length of 10 guinea pigs given orange juice (OJ) and 10 given
ascorbic acid (VC) at 0.5 mg/d of vitamin C (ToothGrowth, Crampton 1947). Under H0 the labels are
exchangeable; all C(20, 10) = 184 756 ways of choosing which 10 animals are labelled OJ give the null
distribution of the difference in means (histogram). The observed difference 5.25 and its mirror image
mark the two tails; the two-sided permutation p-value is 0.0052.
"""
import csv
import itertools

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("toothgrowth.csv") as fh:
    rows = [r for r in csv.DictReader(fh) if float(r["dose"]) == 0.5]
oj = np.array([float(r["len"]) for r in rows if r["supp"] == "OJ"])
vc = np.array([float(r["len"]) for r in rows if r["supp"] == "VC"])
allv = np.concatenate([oj, vc])
total = allv.sum()
idx = np.array(list(itertools.combinations(range(20), 10)))
s1 = allv[idx].sum(axis=1)
diff = s1 / 10 - (total - s1) / 10
obs = oj.mean() - vc.mean()
p = (np.abs(diff) >= abs(obs) - 1e-9).mean()

fig, ax = plt.subplots(figsize=(7.6, 3.3))
fig.subplots_adjust(left=0.1, right=0.98, bottom=0.16, top=0.88)
bins = np.linspace(-7, 7, 71)
h, e = np.histogram(diff, bins)
c = 0.5 * (e[:-1] + e[1:])
tail = np.abs(c) >= abs(obs)
ax.bar(c[~tail], h[~tail] / len(diff), e[1] - e[0], color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.4)
ax.bar(c[tail], h[tail] / len(diff), e[1] - e[0], color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.4)
for v in (obs, -obs):
    ax.axvline(v, color=charts.line("rna"), lw=1.2, ls="--")
ax.text(obs + 0.15, ax.get_ylim()[1] * 0.85, f"observed {obs:.2f}\np = {p:.4f}", fontsize=FT["tiny"], color=P.ink())
charts.style_axes(ax, "difference in means, OJ - VC (all 184 756 relabellings)", "proportion")
charts.title(ax, "Permutation distribution under H0")
