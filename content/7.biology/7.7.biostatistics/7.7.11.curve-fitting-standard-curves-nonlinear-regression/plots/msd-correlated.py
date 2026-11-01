"""Correlated residuals make naive standard errors too small (simulated). 200 two-dimensional Brownian
trajectories of 1000 steps (D = 1, time step 1). For each trajectory the time-averaged mean squared
displacement MSD(lag) is computed for lags 1-100 and a line MSD = 4 D lag is fitted by least squares.
A: MSD curves of 20 trajectories: neighbouring lags share almost the same displacements, so each curve
wanders smoothly away from the truth (dashed). B: the D estimates of all 200 trajectories (histogram)
scatter far more than the ordinary least-squares standard error of a single fit claims (bar: mean
estimate +/- 1.96 x the median naive SE).
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
N, T, L = 200, 1000, 100
lags = np.arange(1, L + 1)
Dhat, se = [], []
curves = []
for i in range(N):
    xy = np.cumsum(rng.normal(0, np.sqrt(2.0), (T, 2)), axis=0)
    msd = np.array([((xy[l:] - xy[:-l]) ** 2).sum(1).mean() for l in lags])
    X = 4 * lags
    d = (X @ msd) / (X @ X)
    res = msd - d * X
    s2 = res @ res / (L - 1)
    Dhat.append(d)
    se.append(np.sqrt(s2 / (X @ X)))
    if i < 20:
        curves.append(msd)
Dhat, se = np.array(Dhat), np.array(se)
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.5))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.87, wspace=0.27)
ax = axs[0]
for c in curves:
    ax.plot(lags, c, color=charts.line("dna"), lw=0.8, alpha=0.6)
ax.plot(lags, 4 * lags, color=P.ink(), lw=1.4, ls="--")
charts.style_axes(ax, "lag / steps", "time-averaged MSD")
charts.title(ax, "A  MSD curves of single trajectories")
ax = axs[1]
ax.hist(Dhat, bins=25, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.6)
m, s = Dhat.mean(), np.median(se)
ax.plot([m - 1.96 * s, m + 1.96 * s], [2, 2], color=charts.line("rna"), lw=4, solid_capstyle="butt")
ax.axvline(1.0, color=P.ink(), lw=1.0, ls="--")
ax.text(0.03, 0.95, f"SD of estimates {Dhat.std(ddof=1):.3f}\nmedian naive SE {s:.4f}", transform=ax.transAxes,
        fontsize=FT["tiny"], color=P.ink(), va="top")
charts.style_axes(ax, "estimated D", "trajectories")
charts.title(ax, "B  Spread across trajectories vs naive SE")
