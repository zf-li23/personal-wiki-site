"""Dropout that depends on observed values (missing at random), simulation with seed 0.

Data are generated from the mixed model fitted to sleepstudy (fixed intercept 251.4 ms, slope 10.47 ms per
day; random-effect SDs 24.7 and 5.92 with correlation 0.07; residual SD 25.6), 100 subjects and 10 days.
From day 3 on, a subject drops out with probability logistic(-3 + 0.03 (y_prev - 300)), where y_prev is
the reaction time observed on the previous day: slow responders leave the study. 300 replicate studies.

A: one simulated study, observed (solid) and missing (faint) values. B: the estimated mean slope per
replicate for four analyses: completers only, all available data by ordinary least squares, last
observation carried forward (LOCF), and the likelihood analysis of all available data under the mixed
model (generalized least squares with the true covariance). Only the last is unbiased under MAR.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
beta = np.array([251.4, 10.47])
G = np.array([[612.1, 9.6], [9.6, 35.07]])
s2 = 654.9
days = np.arange(10.0)
X = np.column_stack([np.ones(10), days])
V = X @ G @ X.T + s2 * np.eye(10)


def simulate(n=100):
    u = rng.multivariate_normal([0, 0], G, n)
    y = (X @ beta)[None, :] + u @ X.T + rng.normal(0, np.sqrt(s2), (n, 10))
    obs = np.ones((n, 10), bool)
    for i in range(n):
        for j in range(3, 10):
            if rng.random() < 1 / (1 + np.exp(3.0 - 0.03 * (y[i, j - 1] - 300))):
                obs[i, j:] = False
                break
    return y, obs


def gls_slope(y, obs):
    A, c = np.zeros((2, 2)), np.zeros(2)
    for i in range(len(y)):
        m = obs[i]
        Vi = np.linalg.inv(V[np.ix_(m, m)])
        A += X[m].T @ Vi @ X[m]
        c += X[m].T @ Vi @ y[i, m]
    return np.linalg.solve(A, c)[1]


est = []
for rep in range(300):
    y, obs = simulate()
    if rep == 0:
        y0, obs0 = y, obs
    comp = obs.all(1)
    cc = np.polyfit(np.tile(days, comp.sum()), y[comp].ravel(), 1)[0]
    av = np.polyfit(np.tile(days, (len(y), 1))[obs], y[obs], 1)[0]
    lo = y.copy()
    for i in range(len(y)):
        k = obs[i].sum()
        lo[i, k:] = y[i, k - 1]
    lf = np.polyfit(np.tile(days, len(y)), lo.ravel(), 1)[0]
    est.append((cc, av, lf, gls_slope(y, obs)))
est = np.array(est)

fig, axs = plt.subplots(1, 2, figsize=(10, 3.6), gridspec_kw=dict(width_ratios=[1, 1.15]))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.87, wspace=0.25)
ax = axs[0]
for i in range(40):
    m = obs0[i]
    ax.plot(days, y0[i], color=P.fill("neutral"), lw=0.5, alpha=0.5)
    ax.plot(days[m], y0[i, m], color=charts.line("dna" if m.all() else "rna"), lw=0.9)
ax.plot([], [], color=charts.line("dna"), label="completer")
ax.plot([], [], color=charts.line("rna"), label="drops out (observed part)")
ax.plot([], [], color=P.fill("neutral"), label="unobserved values")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "day", "reaction time / ms")
charts.title(ax, f"A  One study ({100 * (1 - obs0.all(1).mean()):.0f}% drop out)")
ax = axs[1]
names = ["completers only", "available data, OLS", "LOCF", "mixed model (GLS)"]
toks = ["rna", "protein", "plant", "dna"]
for k in range(4):
    parts = ax.violinplot(est[:, k], positions=[k], widths=0.7, showextrema=False)
    for b in parts["bodies"]:
        b.set_facecolor(P.fill(toks[k]))
        b.set_edgecolor(charts.line(toks[k]))
        b.set_alpha(0.7)
    ax.plot([k - 0.25, k + 0.25], [est[:, k].mean()] * 2, color=charts.line(toks[k]), lw=2)
    ax.text(k, est[:, k].min() - 0.15, f"mean {est[:, k].mean():.2f}", ha="center", va="top", fontsize=FT["tiny"], color=P.ink())
ax.axhline(beta[1], color=P.ink(), lw=0.9, ls="--")
ax.text(-0.45, beta[1] + 0.15, "true slope 10.47", fontsize=FT["tiny"], color=P.ink(), ha="left", va="bottom")
ax.set_xticks(range(4))
ax.set_xticklabels(names, fontsize=FT["tiny"])
ax.set_ylim(4.0, 13.0)
charts.style_axes(ax, None, "estimated slope / ms per day")
charts.title(ax, "B  300 replicate studies")
