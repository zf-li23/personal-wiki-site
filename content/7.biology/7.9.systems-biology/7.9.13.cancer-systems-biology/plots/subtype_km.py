"""Survival by molecular subtype, and the optimal-cutpoint trap (simulation). A: 200 patients, 100 in
each of two subtypes, with exponential survival times (median 60 months in subtype 1, 30 in
subtype 2: hazard ratio 2) and uniform censoring between 24 and 120 months; Kaplan-Meier curves
with censoring ticks, log-rank test and Cox hazard ratio. B: 200 genes whose expression is
unrelated to survival (in patients with survival simulated as in subtype 1). For each gene the patients are split at
every cutpoint between the 10th and 90th percentiles of expression and the smallest log-rank p value
is kept; the histogram shows these minimal p values on a logarithmic axis, with the nominal 0.05
(dashed). C: the Kaplan-Meier curves of the gene with the smallest minimal p value, split at its
best cutpoint: a convincing-looking but false prognostic marker."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st
import wikibio as bio
from wikibio import charts, stats

P = bio.P
rng = np.random.default_rng(0)


def cohort(n, median):
    t = rng.exponential(median / np.log(2), n)
    c = rng.uniform(24, 120, n)
    return np.minimum(t, c), (t <= c).astype(int)


t1, e1 = cohort(100, 60.0)
t2, e2 = cohort(100, 30.0)
time = np.r_[t1, t2]
event = np.r_[e1, e2]
group = np.r_[np.zeros(100, int), np.ones(100, int)]
lr = stats.logrank(time, event, group)
cox = stats.cox_ph(time, event, group)


def logrank_fast(time, event, g):
    """Two-group log-rank chi-square for a boolean group vector (vectorized over event times)."""
    o = np.argsort(time)
    t, e, x = time[o], event[o], g[o]
    n_at = np.arange(len(t), 0, -1)
    n1_at = np.cumsum(x[::-1])[::-1]
    d, d1 = e, e * x
    keep = d > 0
    n, n1 = n_at[keep], n1_at[keep]
    E1 = n1 / n
    V = n1 * (n - n1) / n ** 2
    O1 = d1[keep]
    return (O1.sum() - E1.sum()) ** 2 / V.sum()


tn, en = cohort(200, 60.0)
minp, best = [], None
for gene in range(200):
    expr = rng.normal(0, 1, 200)
    cuts = np.quantile(expr, np.linspace(0.1, 0.9, 81))
    ps = [st.chi2.sf(logrank_fast(tn, en, expr > c), 1) for c in cuts]
    j = int(np.argmin(ps))
    minp.append(ps[j])
    if best is None or ps[j] < best[0]:
        best = (ps[j], expr > cuts[j], np.linspace(0.1, 0.9, 81)[j])
minp = np.array(minp)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(11, 3.6))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.17, top=0.86, wspace=0.32)


def km_plot(ax, time, event, grp, names, toks):
    for k, (nm, tok) in enumerate(zip(names, toks)):
        km = stats.kaplan_meier(time[grp == k], event[grp == k])
        col = charts.line(tok)
        tt = np.r_[km.times, time[grp == k].max()]
        ss = np.r_[km.S, km.S[-1]]
        ax.step(tt, ss, where="post", color=col, lw=1.6, label=nm)
        ax.plot(km.censored, km.S_censored, "|", color=col, ms=5)
    ax.set_ylim(0, 1.03)
    ax.set_xlim(0, 120)
    charts.style_axes(ax, "months", "survival probability")


km_plot(ax1, time, event, group, ["subtype 1", "subtype 2"], ["positive", "negative"])
ax1.legend(fontsize=7, frameon=False, loc="upper right")
ax1.text(3, 0.06, f"log-rank p = {lr['p']:.1e}\nHR = {cox['hr']:.2f} ({cox['hr_ci'][0]:.2f}-{cox['hr_ci'][1]:.2f})",
         fontsize=7, color=P.ink())
charts.title(ax1, "A  Two subtypes, true HR = 2")
ax2.hist(np.log10(minp), bins=25, color=charts.line("neutral"))
ax2.axvline(np.log10(0.05), color=P.ink(), ls="--", lw=1)
ax2.text(np.log10(0.05) - 0.08, ax2.get_ylim()[1] * 0.9, f"{np.mean(minp < 0.05):.0%} below 0.05", ha="right",
         fontsize=7, color=P.ink())
charts.style_axes(ax2, "log10 minimal p over cutpoints", "number of null genes")
charts.title(ax2, "B  Optimal cutpoints, no true effect")
km_plot(ax3, tn, en, best[1].astype(int), ["low expression", "high expression"], ["dna", "highlight"])
ax3.legend(fontsize=7, frameon=False, loc="upper right")
ax3.text(3, 0.06, f"best cut at {best[2]:.0%} quantile\nlog-rank p = {best[0]:.1e}", fontsize=7, color=P.ink())
charts.title(ax3, "C  The best null gene")
