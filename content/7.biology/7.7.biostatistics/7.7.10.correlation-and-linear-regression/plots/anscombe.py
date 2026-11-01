"""Anscombe's quartet (Anscombe 1973): four data sets of 11 points with the same means, variances,
correlation (r = 0.82) and least-squares line (y = 3.0 + 0.5 x), but four different relationships:
roughly linear, curved, linear with one outlier, and a single point that creates the correlation.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
ys = [[8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68],
      [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74],
      [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]]
x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]
sets = [(x, ys[0]), (x, ys[1]), (x, ys[2]), (x4, y4)]
names = ["I  Linear", "II  Curved", "III  One outlier", "IV  One leverage point"]
fig, axs = plt.subplots(1, 4, figsize=(10.5, 2.9), sharey=True)
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.17, top=0.86, wspace=0.12)
for ax, (xx, yy), nm in zip(axs, sets, names):
    xx, yy = np.array(xx, float), np.array(yy, float)
    b, a = np.polyfit(xx, yy, 1)
    r = np.corrcoef(xx, yy)[0, 1]
    g = np.linspace(3, 20, 10)
    ax.plot(g, a + b * g, color=charts.line("enzyme"), lw=1.4)
    ax.scatter(xx, yy, s=22, color=P.fill("dna"), edgecolor=charts.line("dna"), lw=0.8, zorder=3)
    ax.text(3.5, 12.6, f"r = {r:.2f}\ny = {a:.2f} + {b:.3f} x", fontsize=FT["tiny"], color=P.ink(), va="top")
    ax.set_xlim(2.5, 20.5)
    ax.set_ylim(2, 13.5)
    charts.style_axes(ax, "x", "y" if ax is axs[0] else None)
    charts.title(ax, nm)
