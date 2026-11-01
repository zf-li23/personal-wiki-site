"""Mean, median and mode of a left-skewed, a symmetric and a right-skewed distribution (Beta densities,
computed exactly). In a right-skewed distribution the long right tail pulls the mean above the median,
which lies above the mode; the order reverses for a left-skewed distribution.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
cases = [("left-skewed", 5, 2), ("symmetric", 4, 4), ("right-skewed", 2, 5)]
fig, axs = plt.subplots(1, 3, figsize=(10.4, 3.0), sharey=True)
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.17, top=0.86, wspace=0.08)
x = np.linspace(0, 1, 400)
for ax, (name, a, b) in zip(axs, cases):
    d = stats.beta(a, b)
    ax.fill_between(x, d.pdf(x), color=P.fill("dna"), alpha=0.5, lw=0)
    ax.plot(x, d.pdf(x), color=charts.line("dna"), lw=1.6)
    marks = [("mode", (a - 1) / (a + b - 2), ":", "enzyme"), ("median", d.median(), "--", "plant"), ("mean", d.mean(), "-", "rna")]
    for k, (lab, v, ls, tok) in enumerate(marks):
        ax.plot([v, v], [0, d.pdf(v)], color=charts.line(tok), ls=ls, lw=1.4, label=f"{lab} {v:.2f}")
    ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left" if a >= b and a != b else "upper right")
    ax.set_ylim(0, 2.9)
    charts.style_axes(ax, "x", "density" if ax is axs[0] else None)
    charts.title(ax, f"{name}  Beta({a}, {b})")
