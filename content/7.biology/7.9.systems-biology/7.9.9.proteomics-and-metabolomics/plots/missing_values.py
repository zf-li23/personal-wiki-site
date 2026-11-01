"""Missing values in label-free proteomics are not missing at random (simulation). A: log2
intensities of 3000 proteins in one sample (true values) and the values that are observed when
everything below a detection limit of 20 is lost, plus 3% of values lost at random: the missing
values are the low ones. B: 600 proteins with a true 4-fold decrease (log2 fold change -2) between
two groups of 4 samples, plotted against their log2 abundance in the control group; noise SD 0.5.
Complete-case means (ignoring missing values) shrink the decrease of low-abundance proteins;
filling missing values with random draws from a down-shifted normal distribution (mean 1.8 SD
below the observed mean, SD 0.3 times the observed SD) replaces the true values by an arbitrary
level; a maximum-likelihood fit of a normal model left-censored at the detection limit (SD known,
at least one observed value per group) has the smallest bias. Proteins with no observed value in a
group (31%, mostly below 21) have no complete-case or censored estimate. Lines: running means over
60 proteins."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, optimize
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
L, sd, n = 20.0, 0.5, 4


def observe(x):
    x = x.copy()
    x[(x < L) | (rng.random(x.shape) < 0.03)] = np.nan
    return x


def censored_mean(x, s):
    """ML estimate of the mean of normal data (known SD s) left-censored at L; needs one observed value."""
    o, k = x[~np.isnan(x)], np.isnan(x).sum()
    nll = lambda m: -(stats.norm.logpdf(o, m, s).sum() + k * stats.norm.logcdf(L, m, s))
    return optimize.minimize_scalar(nll, bounds=(L - 10, L + 15), method="bounded").x


fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.7))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.88, wspace=0.28)
true1 = rng.normal(23, 2.2, 3000)
obs1 = observe(true1 + rng.normal(0, sd, 3000))
bins = np.linspace(15, 31, 65)
a.hist(true1, bins, color=P.fill("neutral"), alpha=0.6, label="all proteins (true)")
a.hist(obs1[~np.isnan(obs1)], bins, histtype="step", color=charts.line("dna"), lw=1.4, label="observed")
a.axvline(L, color=P.muted(), ls="--", lw=0.8)
a.text(L - 0.2, a.get_ylim()[1] * 0.9, "detection\nlimit", ha="right", fontsize=7, color=P.muted())
a.legend(frameon=False, fontsize=7.5)
charts.style_axes(a, "log2 intensity", "proteins")
charts.title(a, f"A  {100 * np.mean(np.isnan(obs1)):.0f}% missing, mostly low values")

mu = rng.uniform(19.5, 26, 600)
est = {"complete case": [], "down-shifted imputation": [], "censored likelihood": []}
o1 = obs1[~np.isnan(obs1)]
shift, width = o1.mean() - 1.8 * o1.std(), 0.3 * o1.std()
for m in mu:
    xa = observe(m + rng.normal(0, sd, n))
    xb = observe(m - 2 + rng.normal(0, sd, n))
    est["complete case"].append(np.nanmean(xb) - np.nanmean(xa) if np.any(~np.isnan(xa)) and np.any(~np.isnan(xb)) else np.nan)
    fa = np.where(np.isnan(xa), rng.normal(shift, width, n), xa)
    fb = np.where(np.isnan(xb), rng.normal(shift, width, n), xb)
    est["down-shifted imputation"].append(fb.mean() - fa.mean())
    both = np.any(~np.isnan(xa)) and np.any(~np.isnan(xb))
    est["censored likelihood"].append(censored_mean(xb, sd) - censored_mean(xa, sd) if both else np.nan)
for (k, v), tok in zip(est.items(), ["rna", "positive", "dna"]):
    v = np.array(v)
    b.scatter(mu, v, s=4, color=charts.line(tok), alpha=0.5, lw=0)
    o = np.argsort(mu)
    ok = ~np.isnan(v[o])
    xs, ys = mu[o][ok], v[o][ok]
    w = 60
    b.plot(np.convolve(xs, np.ones(w) / w, "valid"), np.convolve(ys, np.ones(w) / w, "valid"),
           color=charts.line(tok), lw=1.8, label=k)
b.axhline(-2, color=P.muted(), ls="--", lw=0.8)
b.set_ylim(-4.5, 1)
b.legend(frameon=False, fontsize=7.5, loc="lower right")
charts.style_axes(b, "log2 abundance in the control group", "estimated log2 fold change")
charts.title(b, "B  Estimates of a true log2 fold change of -2")
EST = {k: np.array(v) for k, v in est.items()}
MU = mu
