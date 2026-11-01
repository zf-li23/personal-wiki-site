"""Chi-square test for trend: the international case-control study of breast cancer and age at first
birth (MacMahon et al. 1970, Bull. WHO 43:209), 3220 cases and 10 245 controls who had given birth.
Points: proportion of cases among women in each category of age at first birth, with 95 % Wilson
intervals; line: weighted least-squares fit against the scores 1-5 used by the Cochran-Armitage test
(trend chi-square 129.0 on 1 df; departure from linearity 1.3 on 3 df).
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
cases = np.array([320, 1206, 1011, 463, 220])
controls = np.array([1422, 4432, 2893, 1092, 406])
n = cases + controls
p = cases / n
s = np.arange(1, 6)
z = stats.norm.isf(0.025)
centre = (p + z**2 / (2 * n)) / (1 + z**2 / n)
half = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / (1 + z**2 / n)
w = n
b = np.sum(w * (s - np.average(s, weights=w)) * (p - np.average(p, weights=w))) / np.sum(w * (s - np.average(s, weights=w)) ** 2)
a = np.average(p, weights=w) - b * np.average(s, weights=w)
fig, ax = plt.subplots(figsize=(7.2, 3.4))
fig.subplots_adjust(left=0.11, right=0.98, bottom=0.17, top=0.88)
ax.errorbar(s, p, yerr=[p - (centre - half), (centre + half) - p], fmt="o", ms=5, color=charts.line("rna"), capsize=3, lw=1.2)
ax.plot(s, a + b * s, color=charts.line("enzyme"), lw=1.4, ls="--")
for si, pi, ni in zip(s, p, n):
    ax.text(si + 0.08, pi - 0.012, f"{pi:.3f}\nn = {ni}", fontsize=FT["tiny"] - 1, color=P.ink(), va="top")
ax.set_xticks(s)
ax.set_xticklabels(["< 20", "20-24", "25-29", "30-34", ">= 35"], fontsize=FT["tiny"])
ax.set_xlim(0.6, 5.7)
charts.style_axes(ax, "age at first birth / years", "proportion of cases")
charts.title(ax, "Breast cancer and age at first birth")
