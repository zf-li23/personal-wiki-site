"""Collider bias (Berkson's bias), simulated. Two diseases with independent severities X and Y (standard
normal, 2000 people) are uncorrelated in the population (r = 0, panel A). A person is admitted to
hospital when X + Y > 1.5 (orange). Among the admitted, the two severities are negatively correlated
(panel B): admission is a common effect of both, and selecting on it opens a non-causal path between them.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
x, y = rng.standard_normal((2, 2000))
adm = x + y > 1.5
fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.7), sharex=True, sharey=True)
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.88, wspace=0.12)
ax = axs[0]
ax.scatter(x[~adm], y[~adm], s=5, color=P.fill("dna"), edgecolor="none", alpha=0.6)
ax.scatter(x[adm], y[adm], s=5, color=P.fill("rna"), edgecolor="none", alpha=0.9)
g = np.linspace(-4, 4, 10)
ax.plot(g, 1.5 - g, color=P.muted(), lw=0.9, ls="--")
ax.text(0.03, 0.95, f"all: r = {np.corrcoef(x, y)[0, 1]:.2f}", transform=ax.transAxes, va="top",
        fontsize=FT["tiny"], color=P.ink())
charts.style_axes(ax, "severity of disease X", "severity of disease Y")
charts.title(ax, "A  Population (n = 2000)")
ax = axs[1]
ax.scatter(x[adm], y[adm], s=6, color=P.fill("rna"), edgecolor=charts.line("rna"), lw=0.3, alpha=0.9)
b = np.polyfit(x[adm], y[adm], 1)
ax.plot(g, np.polyval(b, g), color=charts.line("rna"), lw=1.4)
ax.text(0.03, 0.95, f"admitted (n = {adm.sum()}): r = {np.corrcoef(x[adm], y[adm])[0, 1]:.2f}",
        transform=ax.transAxes, va="top", fontsize=FT["tiny"], color=P.ink())
ax.set_xlim(-3.8, 3.8)
ax.set_ylim(-3.8, 3.8)
charts.style_axes(ax, "severity of disease X")
charts.title(ax, "B  Hospital patients")
