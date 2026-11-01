"""Why pairing saves subjects. Number of subjects needed to detect a mean difference of 10 mmHg with a
two-sided test at alpha = 0.05 and 80 % power when the between-subject SD of a single reading is 20 mmHg,
as a function of the correlation rho between the two readings of the same subject. Paired design:
n pairs with SD of differences sigma_d = sigma sqrt(2(1 - rho)), and every subject measured twice. Two
independent groups: 2n subjects in total, unaffected by rho. Normal approximation.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
sigma, delta = 20.0, 10.0
k = (stats.norm.isf(0.025) + stats.norm.isf(0.2)) ** 2
rho = np.linspace(0, 0.95, 200)
n_pair = 2 * sigma**2 * (1 - rho) * k / delta**2
n_ind = 2 * 2 * sigma**2 * k / delta**2
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.4))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.87, wspace=0.3)

ax = axs[0]
ax.plot(rho, n_pair, color=charts.line("rna"), lw=1.8, label="paired: subjects (= pairs)")
ax.axhline(n_ind, color=charts.line("dna"), lw=1.8, label="independent groups: total subjects")
for r in [0, 0.5, 0.9]:
    v = 2 * sigma**2 * (1 - r) * k / delta**2
    ax.plot(r, v, "o", ms=4, color=charts.line("rna"))
    ax.text(r + 0.02, v + 5, f"{np.ceil(v):.0f}", fontsize=FT["tiny"], color=P.ink())
ax.text(0.02, n_ind + 5, f"{np.ceil(n_ind / 2):.0f} + {np.ceil(n_ind / 2):.0f}", fontsize=FT["tiny"], color=P.ink())
ax.set_ylim(0, 150)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center left", bbox_to_anchor=(0, 0.55))
charts.style_axes(ax, "within-subject correlation rho", "subjects needed")
charts.title(ax, "A  Sample size, 80% power")

ax = axs[1]
ax.plot(rho, np.sqrt(2 * (1 - rho)), color=charts.line("enzyme"), lw=1.8)
ax.axhline(np.sqrt(2), color=P.muted(), lw=0.8, ls=":")
ax.axhline(1, color=P.muted(), lw=0.8, ls=":")
ax.text(0.6, np.sqrt(2) + 0.04, "independent difference (sqrt 2)", fontsize=FT["tiny"], color=P.muted())
ax.text(0.02, 1.04, "one reading", fontsize=FT["tiny"], color=P.muted())
ax.axvline(0.5, color=P.muted(), lw=0.7, ls="--")
ax.set_ylim(0, 1.6)
charts.style_axes(ax, "within-subject correlation rho", "sigma_d / sigma")
charts.title(ax, "B  SD of a within-pair difference")
