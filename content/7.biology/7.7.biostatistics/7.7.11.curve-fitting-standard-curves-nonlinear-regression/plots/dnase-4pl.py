"""Four-parameter logistic standard curve for run 1 of the rat-serum DNase ELISA (Davidian and Giltinan
1995; R datasets::DNase). A: the fitted curve on a log concentration axis with its 95 % confidence band;
three unknown samples (optical density 0.10, 0.50 and 1.50, mean of duplicate wells) are read back to
concentration with 95 % intervals (delta method). B: precision profile: the coefficient of variation of
the back-calculated concentration across the range; where it exceeds 20 % (dotted) the assay no longer
quantifies. C: the fitted curves of all 11 independent runs (run 1 highlighted); their EC50 values range from 3.7 to
5.0 ng/mL, so a standard curve belongs to its own plate and run.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats as st
import wikibio as bio
from wikibio import charts, stats

P = bio.P
FT = bio.core.FONT
with open("dnase.csv") as fh:
    rows = list(csv.DictReader(fh))
runs = {}
for r in rows:
    runs.setdefault(int(r["run"]), []).append((float(r["conc"]), float(r["density"])))
x, y = map(np.array, zip(*runs[1]))
fit = stats.fit_4pl(x, y, p0=[0, 2, 0.6, 1])
b, t, le, hh = fit.params


def inv(yv, par):
    b, t, le, hh = par
    return 10 ** (le - np.log10((t - b) / (yv - b) - 1) / hh)


def se_inv(y0, m=2):
    eps = 1e-6
    x0 = inv(y0, fit.params)
    g = np.array([(inv(y0, fit.params + eps * np.eye(4)[i]) - x0) / eps for i in range(4)])
    dy = (inv(y0 + eps, fit.params) - x0) / eps
    return x0, np.sqrt(g @ fit.cov @ g + dy ** 2 * fit.sigma ** 2 / m)


fig, axs = plt.subplots(1, 3, figsize=(11.0, 3.5))
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.16, top=0.87, wspace=0.3)
ax = axs[0]
g = np.logspace(np.log10(0.03), np.log10(20), 200)
lo, hi = fit.band(g)
ax.fill_between(g, lo, hi, color=P.fill("enzyme"), alpha=0.8, lw=0)
ax.plot(g, fit.predict(g), color=charts.line("enzyme"), lw=1.4)
ax.scatter(x, y, s=16, color=P.fill("dna"), edgecolor=charts.line("dna"), lw=0.8, zorder=3)
q = st.t.ppf(0.975, fit.df)
for y0 in (0.10, 0.50, 1.50):
    x0, se = se_inv(y0)
    l, u = x0 * np.exp(-q * se / x0), x0 * np.exp(q * se / x0)
    ax.plot([0.03, x0], [y0, y0], color=charts.line("rna"), lw=0.8, ls="--")
    ax.plot([x0, x0], [y0, -0.05], color=charts.line("rna"), lw=0.8, ls="--")
    ax.plot([l, u], [-0.02, -0.02], color=charts.line("rna"), lw=3, solid_capstyle="butt")
    ax.text(x0 * 1.1, y0 + 0.05, f"{x0:.2f}", fontsize=FT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.set_xlim(0.03, 20)
ax.set_ylim(-0.08, 2.0)
charts.style_axes(ax, "DNase / (ng/mL)", "optical density")
charts.title(ax, f"A  4PL, EC50 = {10 ** le:.2f} ng/mL")

ax = axs[1]
cs = np.logspace(np.log10(0.04), np.log10(20), 120)
cv = []
for c in cs:
    y0 = fit.predict(c)
    x0, se = se_inv(y0)
    cv.append(100 * se / x0)
ax.plot(cs, cv, color=charts.line("enzyme"), lw=1.5)
ax.axhline(20, color=P.muted(), lw=0.8, ls=":")
ax.set_xscale("log")
ax.set_ylim(0, 40)
charts.style_axes(ax, "DNase / (ng/mL)", "CV of estimate / %")
charts.title(ax, "B  Precision profile")

ax = axs[2]
for k, pts in sorted(runs.items()):
    xx, yy = map(np.array, zip(*pts))
    f = stats.fit_4pl(xx, yy, p0=[0, 2, 0.6, 1])
    ax.plot(g, f.predict(g), color=charts.line("dna" if k != 1 else "enzyme"), lw=1.0 if k != 1 else 1.6,
            alpha=0.6 if k != 1 else 1)
ax.set_xscale("log")
ax.set_xlim(0.03, 20)
charts.style_axes(ax, "DNase / (ng/mL)", "optical density")
charts.title(ax, "C  Eleven independent runs")
