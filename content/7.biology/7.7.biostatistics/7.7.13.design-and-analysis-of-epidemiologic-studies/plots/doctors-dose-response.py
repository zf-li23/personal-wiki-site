"""British male doctors, 1951-2001 (34 439 men; Doll, Peto, Boreham and Sutherland 2004, BMJ 328:1519,
Table 1): death rates per 1000 men per year, standardized indirectly for age and study year, by smoking habit
at the most recent survey. A: lung cancer, chronic obstructive pulmonary disease (COPD) and ischaemic heart
disease (IHD) for lifelong non-smokers, former cigarette smokers and current smokers of 1-14, 15-24 and
25 or more cigarettes a day. B: the same rates as ratios to lifelong non-smokers (log scale).
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
groups = ["never", "former", "1-14/d", "15-24/d", ">=25/d"]
rates = {
    "lung cancer": [0.17, 0.68, 1.31, 2.33, 4.17],
    "COPD": [0.11, 0.64, 1.04, 1.41, 2.61],
    "IHD": [6.19, 7.61, 9.10, 10.07, 11.11],
}
tok = {"lung cancer": "rna", "COPD": "plant", "IHD": "dna"}
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.6))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.87, wspace=0.3)
x = np.arange(5)
w = 0.26
ax = axs[0]
for k, (name, r) in enumerate(rates.items()):
    ax.bar(x + (k - 1) * w, r, w * 0.92, color=P.fill(tok[name]), edgecolor=P.edge(tok[name]), lw=0.8, label=name)
ax.set_xticks(x)
ax.set_xticklabels(groups, fontsize=FT["tiny"])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "smoking habit", "deaths per 1000 men per year")
charts.title(ax, "A  Age-standardized death rates")
ax = axs[1]
for name, r in rates.items():
    rr = np.array(r) / r[0]
    ax.plot(x, rr, "o-", color=charts.line(tok[name]), lw=1.6, ms=5, label=name)
    off = {"lung cancer": 1.12, "COPD": 0.88, "IHD": 1.0}[name]
    ax.text(4.12, rr[-1] * off, f"{rr[-1]:.1f}", va="center", fontsize=FT["tiny"], color=charts.line(tok[name]))
ax.set_yscale("log")
ax.set_yticks([1, 2, 5, 10, 20])
ax.set_yticklabels(["1", "2", "5", "10", "20"])
ax.axhline(1, color=P.muted(), lw=0.8, ls="--")
ax.set_xticks(x)
ax.set_xticklabels(groups, fontsize=FT["tiny"])
ax.set_xlim(-0.3, 4.6)
charts.style_axes(ax, "smoking habit", "rate ratio vs never smokers")
charts.title(ax, "B  Dose-response on the ratio scale")
