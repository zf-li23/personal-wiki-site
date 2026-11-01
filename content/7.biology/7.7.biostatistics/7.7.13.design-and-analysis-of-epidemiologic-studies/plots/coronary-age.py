"""Coronary deaths among British male doctors in the first ten years of follow-up, by age and smoking
in 1951 (Doll and Hill 1966; tabulated in Breslow and Day 1987). A: deaths per 100 000 person-years
(log scale) for smokers and non-smokers in five age groups. B: the age-specific rate ratio with 95 %
intervals (log scale), the crude ratio of the pooled rates (1.72) and the age-standardized ratios:
direct standardization to the combined person-years (1.42) and the Mantel-Haenszel estimate (1.42).
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
ages = ["35-44", "45-54", "55-64", "65-74", "75-84"]
d_s = np.array([32, 104, 206, 186, 102])
py_s = np.array([52407, 43248, 28612, 12663, 5317])
d_n = np.array([2, 12, 28, 28, 31])
py_n = np.array([18790, 10673, 5710, 2585, 1462])
r_s = d_s / py_s * 1e5
r_n = d_n / py_n * 1e5
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.6))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.87, wspace=0.3)
x = np.arange(5)
ax = axs[0]
ax.plot(x, r_s, "o-", color=charts.line("rna"), lw=1.6, ms=5, label="smokers")
ax.plot(x, r_n, "s-", color=charts.line("dna"), lw=1.6, ms=5, label="non-smokers")
ax.set_yscale("log")
ax.set_xticks(x)
ax.set_xticklabels(ages, fontsize=FT["tiny"])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "age / years", "deaths per 100 000 person-years")
charts.title(ax, "A  Age-specific coronary death rates")
ax = axs[1]
rr = r_s / r_n
se = np.sqrt(1 / d_s + 1 / d_n)
lo, hi = rr * np.exp(-1.96 * se), rr * np.exp(1.96 * se)
ax.errorbar(x, rr, yerr=[rr - lo, hi - rr], fmt="o", color=charts.line("rna"), capsize=3, lw=1.2, ms=5)
crude = (d_s.sum() / py_s.sum()) / (d_n.sum() / py_n.sum())
w = (py_s + py_n) / (py_s + py_n).sum()
direct = (w * r_s).sum() / (w * r_n).sum()
T = py_s + py_n
mh = (d_s * py_n / T).sum() / (d_n * py_s / T).sum()
ax.axhline(1, color=P.muted(), lw=0.8, ls="--")
ax.axhline(crude, color=charts.line("neutral"), lw=1.0, ls=":")
ax.text(4.45, crude * 1.06, f"crude {crude:.2f}", ha="right", fontsize=FT["tiny"], color=P.muted())
ax.axhline(mh, color=charts.line("enzyme"), lw=1.0)
ax.text(4.45, mh * 0.86, f"standardized {direct:.2f}, MH {mh:.2f}", ha="right", fontsize=FT["tiny"],
        color=charts.line("enzyme"))
ax.set_yscale("log")
ax.set_yticks([0.5, 1, 2, 5, 10, 20])
ax.set_yticklabels(["0.5", "1", "2", "5", "10", "20"])
ax.set_xticks(x)
ax.set_xticklabels(ages, fontsize=FT["tiny"])
ax.set_xlim(-0.4, 4.5)
charts.style_axes(ax, "age / years", "rate ratio, smokers vs non-smokers")
charts.title(ax, "B  Rate ratio falls with age")
