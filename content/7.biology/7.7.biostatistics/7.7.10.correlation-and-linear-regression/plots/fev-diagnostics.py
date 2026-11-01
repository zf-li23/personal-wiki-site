"""Residual diagnostics for the regression of FEV on height (654 children; Tager et al. 1979, public
version Kahn 2005). A: residuals of the linear model against fitted values fan out (variance grows with
FEV) and bend. B: residuals of the log-linear model have nearly constant spread. C: normal Q-Q plot of
the standardized residuals of the log model. D: leverage against studentized residuals for the model
ln FEV ~ age + height + sex + smoke; marker area proportional to Cook's distance, the largest
labelled (an 8-year-old recorded as 171 cm tall).
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
age = np.array([float(r["age"]) for r in rows])
h = np.array([float(r["height"]) for r in rows]) * 2.54
sex = np.array([float(r["sex"]) for r in rows])
sm = np.array([float(r["smoke"]) for r in rows])
y = np.array([float(r["fev"]) for r in rows])
n = y.size


def fit(X, y):
    X = np.column_stack([np.ones(n)] + list(X))
    H = X @ np.linalg.solve(X.T @ X, X.T)
    yhat = H @ y
    e = y - yhat
    p = X.shape[1]
    s2 = e @ e / (n - p)
    lev = np.diag(H)
    r = e / np.sqrt(s2 * (1 - lev))
    s2i = ((n - p) * s2 - e ** 2 / (1 - lev)) / (n - p - 1)
    t = e / np.sqrt(s2i * (1 - lev))
    cook = r ** 2 * lev / (p * (1 - lev))
    return yhat, e, r, t, lev, cook, p


def smooth(x, y, frac=0.25):
    o = np.argsort(x)
    xs, ys = x[o], y[o]
    k = max(5, int(frac * n))
    g = np.linspace(xs[0], xs[-1], 40)
    out = [ys[np.argsort(np.abs(xs - v))[:k]].mean() for v in g]
    return g, np.array(out)


fig, axs = plt.subplots(1, 4, figsize=(11.2, 3.0))
fig.subplots_adjust(left=0.05, right=0.99, bottom=0.17, top=0.86, wspace=0.34)
for k, (yy, nm) in enumerate([(y, "A  Linear: residuals"), (np.log(y), "B  Log-linear: residuals")]):
    yhat, e, r, *_ = fit([h], yy)
    ax = axs[k]
    ax.scatter(yhat, e, s=4, color=charts.line("dna"), alpha=0.4, lw=0)
    gx, gy = smooth(yhat, e)
    ax.plot(gx, gy, color=charts.line("rna"), lw=1.4)
    ax.axhline(0, color=P.muted(), lw=0.8, ls="--")
    charts.style_axes(ax, "fitted value", "residual")
    charts.title(ax, nm)

ax = axs[2]
_, _, r, *_ = fit([h], np.log(y))
q = stats.norm.ppf((np.arange(1, n + 1) - 0.5) / n)
ax.scatter(q, np.sort(r), s=4, color=charts.line("dna"), alpha=0.5, lw=0)
ax.plot([-3.2, 3.2], [-3.2, 3.2], color=charts.line("enzyme"), lw=1.2)
charts.style_axes(ax, "normal quantile", "standardized residual")
charts.title(ax, "C  Normal Q-Q (log model)")

ax = axs[3]
_, _, _, t, lev, cook, p = fit([age, h, sex, sm], np.log(y))
ax.scatter(lev, t, s=4 + 2000 * cook, color=P.fill("dna"), edgecolor=charts.line("dna"), lw=0.5, alpha=0.7)
ax.axvline(2 * p / n, color=P.muted(), lw=0.8, ls="--")
for v in (-3, 3):
    ax.axhline(v, color=P.muted(), lw=0.8, ls=":")
i = int(np.argmax(cook))
ax.annotate(f"age {age[i]:.0f}, {h[i]:.0f} cm", (lev[i], t[i]), (lev[i] + 0.006, t[i] + 0.3),
            fontsize=FT["tiny"], color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
charts.style_axes(ax, "leverage", "studentized residual")
charts.title(ax, "D  Influence (full log model)")
