"""Overfitted models are miscalibrated in new data (simulation, seed 0). True model: logit P(Y = 1) =
-1.5 + 0.5 (x1 + ... + x5) with 20 independent standard normal candidate predictors, 15 of them without
effect; event rate about 0.25. Models with all 20 predictors fitted by maximum likelihood. A: one
development sample of n = 200 (about 50 events, 2.5 events per variable): calibration plot in ten
groups of predicted risk, in the development data (apparent) and in 20000 new observations; lines:
the calibration slope fitted by logistic regression of the outcome on the model's linear predictor.
B: calibration slope in new data against the number of events per variable, median and interquartile
range over 200 development samples for each n = 100 ... 3200.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
p, beta = 20, np.r_[np.full(5, 0.5), np.zeros(15)]


def draw(n):
    X = rng.normal(size=(n, p))
    y = (rng.uniform(size=n) < 1 / (1 + np.exp(-(-1.5 + X @ beta)))).astype(float)
    return X, y


def logit_fit(X, y):
    A = np.column_stack([np.ones(len(y)), X])
    b = np.zeros(A.shape[1])
    for _ in range(25):
        pr = 1 / (1 + np.exp(-np.clip(A @ b, -30, 30)))
        b = b + np.linalg.solve(A.T @ (A * (pr * (1 - pr))[:, None]) + 1e-8 * np.eye(A.shape[1]), A.T @ (y - pr))
    return b


def slope(lp, y):
    return logit_fit(lp[:, None], y)[1]


Xv, yv = draw(20000)
Xd, yd = draw(200)
b = logit_fit(Xd, yd)
fig, axs = plt.subplots(1, 2, figsize=(9.6, 4.0))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.14, top=0.88, wspace=0.28)
ax = axs[0]
for X, y, tok, name in ((Xd, yd, "dna", "development (apparent)"), (Xv, yv, "rna", "new data")):
    lp = b[0] + X @ b[1:]
    pr = 1 / (1 + np.exp(-lp))
    q = np.quantile(pr, np.linspace(0, 1, 11))
    g = np.clip(np.searchsorted(q, pr, side="right") - 1, 0, 9)
    mp = [pr[g == k].mean() for k in range(10)]
    ob = [y[g == k].mean() for k in range(10)]
    s = slope(lp, y)
    ax.plot(mp, ob, "o", color=charts.line(tok), ms=5, label=f"{name}: slope {s:.2f}")
    a = logit_fit(lp[:, None], y)
    gg = np.linspace(-4, 3, 100)
    ax.plot(1 / (1 + np.exp(-gg)), 1 / (1 + np.exp(-(a[0] + a[1] * gg))), color=charts.line(tok), lw=1.2)
ax.plot([0, 1], [0, 1], color=P.muted(), ls="--", lw=0.8)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "predicted risk", "observed proportion")
charts.title(ax, f"A  n = 200, {int(yd.sum())} events, 20 predictors")
ax = axs[1]
ns = [100, 200, 400, 800, 1600, 3200]
med, lo, hi, epv = [], [], [], []
for n in ns:
    s, ev = [], []
    for _ in range(200):
        X, y = draw(n)
        bb = logit_fit(X, y)
        s.append(slope(bb[0] + Xv[:4000] @ bb[1:], yv[:4000]))
        ev.append(y.sum() / p)
    med.append(np.median(s))
    lo.append(np.quantile(s, 0.25))
    hi.append(np.quantile(s, 0.75))
    epv.append(np.mean(ev))
ax.fill_between(epv, lo, hi, color=P.fill("enzyme"), alpha=0.5, lw=0)
ax.plot(epv, med, "o-", color=charts.line("enzyme"), ms=4, lw=1.4)
for e, m in zip(epv, med):
    ax.text(e, m - 0.06, f"{m:.2f}", ha="center", fontsize=FT["tiny"], color=P.ink())
ax.axhline(1, color=P.muted(), ls="--", lw=0.8)
ax.axvline(10, color=P.muted(), ls=":", lw=0.8)
ax.set_xscale("log")
ax.set_ylim(0, 1.15)
charts.style_axes(ax, "events per variable (log scale)", "calibration slope in new data")
charts.title(ax, "B  Overfitting shrinks with sample size")
