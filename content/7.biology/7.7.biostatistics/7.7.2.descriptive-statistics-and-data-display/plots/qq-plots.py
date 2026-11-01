"""Normal Q-Q plots: sample quantiles against standard normal quantiles. A: birth weight (birthwt,
n = 189) lies close to a straight line. B: FEV (n = 654) bends upward at both ends, the signature of a
right-skewed distribution. C: the logarithm of FEV is much closer to normal. The reference line passes
through the first and third quartiles.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def col(name, key):
    with open(name) as fh:
        return np.array([float(r[key]) for r in csv.DictReader(fh)])


sets = [("A  Birth weight", col("birthwt.csv", "bwt"), "birth weight / g", "dna"),
        ("B  FEV", col("fev.csv", "fev"), "FEV / L", "rna"),
        ("C  log FEV", np.log(col("fev.csv", "fev")), "ln(FEV / L)", "plant")]
fig, axs = plt.subplots(1, 3, figsize=(10.4, 3.4))
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.16, top=0.87, wspace=0.32)
for ax, (title, x, lab, tok) in zip(axs, sets):
    n = x.size
    q = stats.norm.ppf((np.arange(1, n + 1) - 0.5) / n)
    xs = np.sort(x)
    ax.scatter(q, xs, s=5, color=charts.line(tok), lw=0)
    q1, q3 = np.quantile(x, [0.25, 0.75])
    z1, z3 = stats.norm.ppf([0.25, 0.75])
    slope = (q3 - q1) / (z3 - z1)
    zz = np.array([q[0], q[-1]])
    ax.plot(zz, q1 + slope * (zz - z1), color=P.muted(), lw=1, ls="--")
    ax.text(0.97, 0.05, f"skewness {stats.skew(x):.2f}", transform=ax.transAxes, ha="right", fontsize=FT["tiny"], color=P.ink())
    charts.style_axes(ax, "standard normal quantile", lab)
    charts.title(ax, title)
