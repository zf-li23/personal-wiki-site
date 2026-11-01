"""Distributions derived from the normal. A: chi-square densities with 1, 4 and 9 degrees of freedom
(mean = df, variance = 2 df). B: t densities with 1, 4 and 30 degrees of freedom against the standard
normal; heavier tails for small df. C: F densities for (2, 57), (4, 30) and (9, 9) degrees of freedom.
The dashed lines mark the upper 2.5 % points of t_9 (2.262) and of the standard normal (1.960).
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
toks = ["dna", "rna", "enzyme"]
fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.2))
fig.subplots_adjust(left=0.05, right=0.99, bottom=0.17, top=0.86, wspace=0.22)

x = np.linspace(0.02, 20, 500)
for df, tok in zip([1, 4, 9], toks):
    axs[0].plot(x, stats.chi2.pdf(x, df), color=charts.line(tok), lw=1.5, label=f"df = {df}")
axs[0].set_ylim(0, 0.5)
charts.title(axs[0], "A  Chi-square")

x = np.linspace(-5, 5, 500)
axs[1].plot(x, stats.norm.pdf(x), color=charts.line("neutral"), lw=2.2, label="N(0, 1)")
for df, tok in zip([1, 4, 30], toks):
    axs[1].plot(x, stats.t.pdf(x, df), color=charts.line(tok), lw=1.3, label=f"t, df = {df}")
for v, ls in [(stats.t.isf(0.025, 9), "--"), (stats.norm.isf(0.025), ":")]:
    axs[1].axvline(v, color=P.muted(), lw=0.8, ls=ls)
axs[1].text(2.75, 0.22, f"t_9: {stats.t.isf(0.025, 9):.3f}\nz: {stats.norm.isf(0.025):.3f}", fontsize=FT["tiny"],
            color=P.ink())
charts.title(axs[1], "B  t and standard normal")

x = np.linspace(0.01, 5, 500)
for (a, b), tok in zip([(2, 57), (4, 30), (9, 9)], toks):
    axs[2].plot(x, stats.f.pdf(x, a, b), color=charts.line(tok), lw=1.5, label=f"F({a}, {b})")
charts.title(axs[2], "C  F")
for ax in axs:
    ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
    charts.style_axes(ax, "x", "density" if ax is axs[0] else None)
