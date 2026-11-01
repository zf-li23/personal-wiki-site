"""FEV against height for 654 children (East Boston; Tager et al. 1979, public version Kahn 2005).
A: least-squares line with the 95 % confidence band for the mean FEV and the 95 % prediction band for
one child. B: the same on the log scale; the back-transformed fit curves upward and the prediction band
widens with height, as the data do.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("fev.csv") as fh:
    rows = list(csv.DictReader(fh))
h = np.array([float(r["height"]) for r in rows]) * 2.54
y = np.array([float(r["fev"]) for r in rows])


def fit_bands(x, y, g):
    n = x.size
    b, a = np.polyfit(x, y, 1)
    s = np.sqrt(((y - a - b * x) ** 2).sum() / (n - 2))
    sxx = ((x - x.mean()) ** 2).sum()
    t = stats.t.ppf(0.975, n - 2)
    m = a + b * g
    se_m = s * np.sqrt(1 / n + (g - x.mean()) ** 2 / sxx)
    se_p = s * np.sqrt(1 + 1 / n + (g - x.mean()) ** 2 / sxx)
    return m, m - t * se_m, m + t * se_m, m - t * se_p, m + t * se_p, a, b


g = np.linspace(h.min(), h.max(), 200)
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.5))
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.15, top=0.88, wspace=0.22)
for k, ax in enumerate(axs):
    yy = y if k == 0 else np.log(y)
    m, lo, hi, plo, phi, a, b = fit_bands(h, yy, g)
    tr = (lambda v: v) if k == 0 else np.exp
    ax.scatter(h, y, s=4, color=charts.line("dna"), alpha=0.35, lw=0)
    ax.fill_between(g, tr(plo), tr(phi), color=P.fill("neutral"), alpha=0.45, lw=0, label="95 % prediction band")
    ax.fill_between(g, tr(lo), tr(hi), color=P.fill("enzyme"), alpha=0.9, lw=0, label="95 % confidence band")
    ax.plot(g, tr(m), color=charts.line("enzyme"), lw=1.4)
    eq = f"FEV = {a:.2f} + {b:.4f} height" if k == 0 else f"ln FEV = {a:.2f} + {b:.4f} height"
    ax.text(0.03, 0.96, eq, transform=ax.transAxes, fontsize=FT["tiny"], color=P.ink(), va="top")
    ax.set_ylim(0, 6.2)
    charts.style_axes(ax, "height / cm", "FEV / L")
    charts.title(ax, "A  Linear model" if k == 0 else "B  Log-linear model, back-transformed")
axs[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
