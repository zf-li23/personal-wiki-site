"""Pearson, Spearman and Kendall coefficients for a linear, a monotone nonlinear and an outlier-contaminated sample."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n = 30
x = np.sort(rng.uniform(0, 3, n))
cases = {
    "linear with noise": 1 + x + rng.normal(0, 0.6, n),
    "monotone, nonlinear: y = exp(2x)": np.exp(2 * x),
    "no association plus one outlier": rng.normal(0, 1, n),
}
y3 = cases["no association plus one outlier"]
x3 = x.copy()
x3[-1], y3[-1] = 12.0, 12.0

fig, axes = plt.subplots(1, 3, figsize=(11, 3.8))
for ax, (title, y) in zip(axes, cases.items()):
    xx = x3 if "outlier" in title else x
    r = stats.pearsonr(xx, y)[0]
    rs = stats.spearmanr(xx, y)[0]
    tau = stats.kendalltau(xx, y)[0]
    ax.scatter(xx, y, s=18, color="C0")
    ax.set_title(title, fontsize=10)
    ax.text(0.04, 0.96, f"Pearson r = {r:.2f}\nSpearman rho = {rs:.2f}\nKendall tau = {tau:.2f}",
            transform=ax.transAxes, va="top", fontsize=9)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(alpha=0.3)
fig.tight_layout()
