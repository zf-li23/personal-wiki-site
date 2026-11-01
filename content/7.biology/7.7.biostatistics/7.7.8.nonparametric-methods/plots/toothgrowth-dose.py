"""Kruskal-Wallis test on ToothGrowth (60 guinea pigs, Crampton 1947): odontoblast length by daily dose
of vitamin C, both supplements pooled (20 animals per dose). A: the data with group medians. B: the same
animals by their rank among all 60; the Kruskal-Wallis statistic compares the mean ranks (12.3, 31.9,
47.4) with the overall mean rank 30.5, H = 40.7 on 2 df.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("toothgrowth.csv") as fh:
    rows = list(csv.DictReader(fh))
L = np.array([float(r["len"]) for r in rows])
D = np.array([float(r["dose"]) for r in rows])
S = np.array([r["supp"] for r in rows])
R = stats.rankdata(L)
doses = [0.5, 1.0, 2.0]
TOK = ["neutral", "enzyme", "rna"]
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.4))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.87, wspace=0.28)
rng = np.random.default_rng(0)
for ax, val, lab, stat in [(axs[0], L, "length", np.median), (axs[1], R, "rank among 60", np.mean)]:
    for k, dd in enumerate(doses):
        m = D == dd
        for sp, mk in [("OJ", "o"), ("VC", "^")]:
            mm = m & (S == sp)
            ax.scatter(k + rng.uniform(-0.17, 0.17, mm.sum()), val[mm], s=14, marker=mk, color=charts.line(TOK[k]),
                       alpha=0.75, lw=0, label=sp if k == 0 else None)
        v = stat(val[m])
        ax.plot([k - 0.28, k + 0.28], [v, v], color=P.ink(), lw=1.8)
        ax.text(k + 0.31, v, f"{v:.1f}", fontsize=FT["tiny"], color=P.ink(), va="center")
    ax.set_xticks(range(3))
    ax.set_xticklabels([f"{d:g} mg/d" for d in doses], fontsize=FT["tiny"])
    ax.set_xlim(-0.5, 2.7)
axs[1].axhline(30.5, color=P.muted(), lw=0.8, ls=":")
axs[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(axs[0], None, "odontoblast length")
charts.style_axes(axs[1], None, "rank")
charts.title(axs[0], "A  Data and medians")
charts.title(axs[1], "B  Ranks and mean ranks")
