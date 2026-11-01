"""Comparing whole distributions (654 children, East Boston FEV data; Tager et al. 1979, public version
Kahn 2005). A: empirical distribution functions of FEV for 589 non-smokers and 65 smokers; the
Kolmogorov-Smirnov statistic D = 0.435 is the largest vertical gap. B: the Hanley-McNeil (1982) CT
ratings of 58 normal and 51 abnormal patients (five ordered categories): the Mann-Whitney statistic
U / (n1 n2) = 0.893 is the area under the ROC curve.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("fev.csv") as fh:
    rows = list(csv.DictReader(fh))
fev = np.array([float(r["fev"]) for r in rows])
sm = np.array([int(r["smoke"]) for r in rows])
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.4))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.87, wspace=0.28)

ax = axs[0]
grid = np.sort(np.unique(fev))
F = []
for g, tok, lab in [(0, "dna", "non-smoker"), (1, "rna", "smoker")]:
    x = np.sort(fev[sm == g])
    Fg = np.searchsorted(x, grid, side="right") / x.size
    F.append(Fg)
    ax.step(grid, Fg, where="post", color=charts.line(tok), lw=1.5, label=f"{lab} (n = {x.size})")
gap = np.abs(F[0] - F[1])
k = np.argmax(gap)
ax.plot([grid[k]] * 2, [F[0][k], F[1][k]], color=P.ink(), lw=1.6)
ax.text(grid[k] + 0.08, (F[0][k] + F[1][k]) / 2, f"D = {gap[k]:.3f}", fontsize=FT["tiny"], color=P.ink())
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "FEV / L", "cumulative proportion")
charts.title(ax, "A  Two empirical distribution functions")

ax = axs[1]
normal = np.array([33, 6, 6, 11, 2])
abn = np.array([3, 2, 2, 11, 33])
pos = np.arange(1, 6)
ax.bar(pos - 0.2, normal / normal.sum(), 0.38, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.8, label="normal (58)")
ax.bar(pos + 0.2, abn / abn.sum(), 0.38, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.8, label="abnormal (51)")
# U counts abnormal > normal plus half of ties
cn = np.cumsum(normal) - normal
U = (abn * cn).sum() + 0.5 * (abn * normal).sum()
ax.text(2.6, 0.42, f"U / (n1 n2) = {U / (58 * 51):.3f} = AUC", fontsize=FT["tiny"], color=P.ink())
ax.set_xticks(pos)
ax.set_xticklabels(["definitely\nnormal", "probably\nnormal", "question-\nable", "probably\nabnormal", "definitely\nabnormal"],
                   fontsize=FT["tiny"] - 1)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper center")
charts.style_axes(ax, None, "proportion of patients")
charts.title(ax, "B  Ordinal ratings: Mann-Whitney = AUC")
