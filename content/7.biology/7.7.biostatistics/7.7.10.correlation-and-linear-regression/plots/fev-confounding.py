"""Confounding of smoking and FEV by age (654 children, Tager et al. 1979; public version Kahn 2005).
A: FEV against age; the 65 smokers (orange) are all 9 years or older. Lines: the model
FEV = b0 + b1 age + b2 smoke, two parallel lines whose vertical gap is the age-adjusted smoking effect.
B: the estimated smoking coefficient with its 95 % confidence interval as covariates are added (the last
row on the log scale, converted to a percentage difference in FEV).
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


def ols(X, y):
    X = np.column_stack([np.ones(len(y))] + list(X))
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    res = y - X @ beta
    df = len(y) - X.shape[1]
    cov = res @ res / df * np.linalg.inv(X.T @ X)
    return beta, np.sqrt(np.diag(cov)), df


fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.5), gridspec_kw=dict(width_ratios=[1.25, 1]))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.88, wspace=0.62)
ax = axs[0]
rng = np.random.default_rng(0)
for g, tok, lab in [(0, "dna", "non-smoker"), (1, "rna", "smoker")]:
    m = sm == g
    ax.scatter(age[m] + rng.uniform(-0.25, 0.25, m.sum()), y[m], s=6 if g == 0 else 12, color=charts.line(tok),
               alpha=0.35 if g == 0 else 0.85, lw=0, label=lab)
beta, se, df = ols([age, sm], y)
xs = np.linspace(3, 19, 10)
ax.plot(xs, beta[0] + beta[1] * xs, color=charts.line("dna"), lw=1.5)
xs1 = np.linspace(9, 19, 10)
ax.plot(xs1, beta[0] + beta[1] * xs1 + beta[2], color=charts.line("rna"), lw=1.5)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left", markerscale=1.6)
ax.set_xticks(range(3, 20, 2))
charts.style_axes(ax, "age / years", "FEV / L")
charts.title(ax, "A  Smokers are older children")

ax = axs[1]
models = [("crude", [sm], False), ("+ age", [age, sm], False), ("+ age, height, sex", [age, h, sex, sm], False),
          ("log FEV, same covariates", [age, h, sex, sm], True)]
for k, (nm, X, lg) in enumerate(models):
    beta, se, df = ols(X, np.log(y) if lg else y)
    t = stats.t.ppf(0.975, df)
    est, lo, hi = beta[-1], beta[-1] - t * se[-1], beta[-1] + t * se[-1]
    if lg:
        est, lo, hi = [100 * (np.exp(v) - 1) / 100 for v in (est, lo, hi)]
    yk = 3 - k
    tok = "rna" if k == 0 else "enzyme"
    ax.plot([lo, hi], [yk, yk], color=charts.line(tok), lw=1.6)
    ax.scatter([est], [yk], s=30, color=P.fill(tok), edgecolor=charts.line(tok), zorder=3)
    lab = f"{est:+.3f} L" if not lg else f"{100 * est:+.1f} %"
    ax.text(hi + 0.03, yk + 0.18, lab, fontsize=FT["tiny"], color=P.ink())
ax.axvline(0, color=P.muted(), lw=0.8, ls="--")
ax.set_yticks([3, 2, 1, 0])
ax.set_yticklabels([m[0] for m in models], fontsize=FT["tiny"])
ax.set_ylim(-0.6, 3.6)
ax.set_xlim(-0.45, 1.15)
charts.style_axes(ax, "smoking effect (L; last row: relative)")
charts.title(ax, "B  Adjusting for age and size")
