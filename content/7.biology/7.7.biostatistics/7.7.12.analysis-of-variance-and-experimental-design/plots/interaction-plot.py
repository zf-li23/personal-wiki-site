"""Interaction plot for ToothGrowth (Crampton 1947; R datasets::ToothGrowth): mean odontoblast length of each
group of 10 guinea pigs with 95 % confidence intervals based on the pooled two-way ANOVA error mean
square (54 df), against daily dose on a log scale, for orange juice (OJ) and ascorbic acid (VC).
The lines are far from parallel: orange juice is better at 0.5 and 1 mg/d, the two are equal at 2 mg/d.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("toothgrowth.csv") as fh:
    rows = list(csv.DictReader(fh))
y = np.array([float(r["len"]) for r in rows])
dose = np.array([float(r["dose"]) for r in rows])
supp = np.array([r["supp"] for r in rows])
doses = [0.5, 1.0, 2.0]
cells = {(d, s): y[(dose == d) & (supp == s)] for d in doses for s in ("OJ", "VC")}
sse = sum(((v - v.mean()) ** 2).sum() for v in cells.values())
mse = sse / (60 - 6)
half = stats.t.ppf(0.975, 54) * np.sqrt(mse / 10)
fig, ax = plt.subplots(figsize=(5.4, 3.8))
fig.subplots_adjust(left=0.13, right=0.97, bottom=0.14, top=0.92)
for s, tok, off, lab in [("OJ", "rna", -0.03, "orange juice (OJ)"), ("VC", "dna", 0.03, "ascorbic acid (VC)")]:
    xs = np.log2(doses) + off
    ms = [cells[(d, s)].mean() for d in doses]
    ax.errorbar(xs, ms, yerr=half, color=charts.line(tok), lw=1.5, capsize=3, marker="o", ms=5,
                mfc=P.fill(tok), mec=charts.line(tok), label=lab)
ax.set_xticks(np.log2(doses))
ax.set_xticklabels(["0.5", "1", "2"])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "vitamin C dose / (mg/d), log scale", "mean odontoblast length")
charts.title(ax, "Dose x delivery interaction")
