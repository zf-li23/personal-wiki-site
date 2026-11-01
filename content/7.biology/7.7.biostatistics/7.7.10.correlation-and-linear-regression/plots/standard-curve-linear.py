"""A linear standard curve and inverse prediction: run 1 of the rat-serum DNase ELISA (Davidian and
Giltinan 1995; R datasets::DNase), the five lowest concentrations in duplicate wells. A: least-squares
line, 95 % prediction band for the mean of two wells, and the inverse prediction of an unknown sample
whose two wells read OD 0.50 (horizontal arrow) with its 95 % interval on the concentration axis.
B: residuals: the straight line misses systematically at both ends, a sign that the response is
already bending.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("dnase.csv") as fh:
    rows = [r for r in csv.DictReader(fh) if r["run"] == "1" and float(r["conc"]) < 1.6]
x = np.array([float(r["conc"]) for r in rows])
y = np.array([float(r["density"]) for r in rows])
n = x.size
b, a = np.polyfit(x, y, 1)
e = y - a - b * x
s = np.sqrt(e @ e / (n - 2))
sxx = ((x - x.mean()) ** 2).sum()
t = stats.t.ppf(0.975, n - 2)
g = np.linspace(0, 1.7, 100)
half = t * s * np.sqrt(1 / 2 + 1 / n + (g - x.mean()) ** 2 / sxx)
y0 = 0.50
x0 = (y0 - a) / b
se0 = s / abs(b) * np.sqrt(1 / 2 + 1 / n + (y0 - y.mean()) ** 2 / (b * b * sxx))

fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.4), gridspec_kw=dict(width_ratios=[1.5, 1]))
fig.subplots_adjust(left=0.08, right=0.99, bottom=0.16, top=0.88, wspace=0.3)
ax = axs[0]
ax.fill_between(g, a + b * g - half, a + b * g + half, color=P.fill("neutral"), alpha=0.5, lw=0)
ax.plot(g, a + b * g, color=charts.line("enzyme"), lw=1.4)
ax.scatter(x, y, s=20, color=P.fill("dna"), edgecolor=charts.line("dna"), lw=0.8, zorder=3)
ax.annotate("", (x0, y0), (0, y0), arrowprops=dict(arrowstyle="->", color=charts.line("rna"), lw=1.2))
ax.plot([x0, x0], [y0, 0], color=charts.line("rna"), lw=1.0, ls="--")
ax.plot([x0 - t * se0, x0 + t * se0], [0.012, 0.012], color=charts.line("rna"), lw=3, solid_capstyle="butt")
ax.text(x0 + 0.05, 0.06, f"{x0:.2f} ng/mL\n({x0 - t * se0:.2f}-{x0 + t * se0:.2f})", fontsize=FT["tiny"], color=P.ink())
ax.text(0.03, y0 + 0.02, "unknown, OD 0.50", fontsize=FT["tiny"], color=P.ink())
ax.set_xlim(0, 1.7)
ax.set_ylim(0, 0.75)
charts.style_axes(ax, "DNase / (ng/mL)", "optical density")
charts.title(ax, f"A  OD = {a:.3f} + {b:.3f} conc")
ax = axs[1]
ax.scatter(x, e, s=20, color=P.fill("dna"), edgecolor=charts.line("dna"), lw=0.8, zorder=3)
ax.axhline(0, color=P.muted(), lw=0.8, ls="--")
charts.style_axes(ax, "DNase / (ng/mL)", "residual")
charts.title(ax, "B  Residuals bend")
