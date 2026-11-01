"""Estimates of the effect of maternal smoking on birth weight (189 births, Baystate Medical Center 1986;
Hosmer and Lemeshow; R MASS::birthwt), adjusting for the same eight covariates as the propensity model:
mean difference in grams with 95 % intervals. Percentile bootstrap intervals (2000 resamples, the propensity
model refitted in each) except for matching (paired t interval over 52 caliper-matched pairs). Matching
estimates the effect among smokers, overlap weighting the effect in the population where both choices
are common, the other methods the average effect in the whole sample.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("birthwt.csv") as fh:
    rows = list(csv.DictReader(fh))
c = {k: np.array([float(r[k]) for r in rows]) for k in ("age", "lwt", "race", "smoke", "ptl", "ht", "ui", "ftv", "bwt")}
X0 = np.column_stack([np.ones(c["age"].size), c["age"], c["lwt"], c["race"] == 2, c["race"] == 3, c["ptl"] > 0,
                      c["ht"], c["ui"], c["ftv"] > 0]).astype(float)
T0, Y0 = c["smoke"], c["bwt"]


def fit_ps(X, t):
    b = np.zeros(X.shape[1])
    for _ in range(40):
        p = 1 / (1 + np.exp(-X @ b))
        b = b + np.linalg.solve(X.T @ (X * (p * (1 - p))[:, None]) + 1e-10 * np.eye(X.shape[1]), X.T @ (t - p))
    return 1 / (1 + np.exp(-X @ b))


def wdiff(y, t, w):
    return np.average(y[t == 1], weights=w[t == 1]) - np.average(y[t == 0], weights=w[t == 0])


def estimates(X, t, y):
    ps = fit_ps(X, t)
    w = np.where(t == 1, 1 / ps, 1 / (1 - ps))
    lo, hi = np.quantile(w, [0.01, 0.99])
    q = np.searchsorted(np.quantile(ps, [0.2, 0.4, 0.6, 0.8]), ps, side="right")
    strat = np.nan
    if all(((q == k) & (t == 1)).any() and ((q == k) & (t == 0)).any() for k in range(5)):
        strat = sum((q == k).sum() * (y[(q == k) & (t == 1)].mean() - y[(q == k) & (t == 0)].mean())
                    for k in range(5)) / y.size
    reg = np.linalg.lstsq(np.column_stack([X, t]), y, rcond=None)[0][-1]
    return [reg, strat, wdiff(y, t, w), wdiff(y, t, np.clip(w, lo, hi)), wdiff(y, t, np.where(t == 1, 1 - ps, ps))]


est = estimates(X0, T0, Y0)
rng = np.random.default_rng(0)
boot = []
for _ in range(2000):
    i = rng.integers(0, Y0.size, Y0.size)
    boot.append(estimates(X0[i], T0[i], Y0[i]))
ci = np.nanpercentile(np.array(boot), [2.5, 97.5], axis=0)
# greedy 1:1 nearest-neighbour matching on the logit of the propensity score, caliper 0.2 SD
ps = fit_ps(X0, T0)
lp = np.log(ps / (1 - ps))
cal = 0.2 * lp.std(ddof=1)
treated = np.where(T0 == 1)[0]
controls = list(np.where(T0 == 0)[0])
diffs = []
for i in treated[np.argsort(-ps[treated], kind="stable")]:
    d = [abs(lp[i] - lp[j]) for j in controls]
    k = int(np.argmin(d))
    if d[k] <= cal:
        diffs.append(Y0[i] - Y0[controls.pop(k)])
diffs = np.array(diffs)
m = diffs.mean()
h = stats.t.ppf(0.975, diffs.size - 1) * diffs.std(ddof=1) / np.sqrt(diffs.size)
crude = Y0[T0 == 1].mean() - Y0[T0 == 0].mean()
s_cr = np.sqrt(Y0[T0 == 1].var(ddof=1) / 74 + Y0[T0 == 0].var(ddof=1) / 115)
rows_ = [("crude difference", crude, crude - 1.96 * s_cr, crude + 1.96 * s_cr, "neutral"),
         ("regression adjustment", est[0], ci[0, 0], ci[1, 0], "dna"),
         ("PS strata (quintiles)", est[1], ci[0, 1], ci[1, 1], "dna"),
         (f"PS matching ({diffs.size} pairs)", m, m - h, m + h, "dna"),
         ("IPW", est[2], ci[0, 2], ci[1, 2], "rna"),
         ("IPW, truncated weights", est[3], ci[0, 3], ci[1, 3], "rna"),
         ("overlap weights", est[4], ci[0, 4], ci[1, 4], "plant")]
fig, ax = plt.subplots(figsize=(7.6, 3.4))
fig.subplots_adjust(left=0.43, right=0.97, bottom=0.17, top=0.95)
for k, (name, e, l, u, tok) in enumerate(rows_):
    y = len(rows_) - k
    ax.plot([l, u], [y, y], color=charts.line(tok), lw=1.4)
    ax.plot(e, y, "s", ms=6, color=P.fill(tok), mec=charts.line(tok))
ax.set_yticks(range(len(rows_), 0, -1))
ax.set_yticklabels([f"{r[0]}   {r[1]:.0f} ({r[2]:.0f}, {r[3]:.0f})" for r in rows_], fontsize=FT["tiny"])
ax.axvline(0, color=P.muted(), lw=0.8, ls="--")
charts.style_axes(ax, "effect of smoking on birth weight / g")
