"""Estimating the size of an interactome from the overlap of two screens (simulation, Formula
10.5.2). A true interactome of 60000 binary interactions is sampled by two independent screens with
sensitivities 0.15 and 0.10; each screen also reports false positives (precision 0.8 and 0.7)
drawn from the 2 x 10^8 non-interacting pairs, so false positives almost never overlap.
A: 400 repetitions: the naive Lincoln-Petersen estimate n1 n2 / m (orange) is biased upward by
the false positives; multiplying n1 and n2 by the precisions (blue) recovers the true size
(dashed). B (80 repetitions per value, median and 90% range): when interactions differ in detectability (log-normal propensity shared by both
screens, SD sigma on the log scale), the screens overlap more than independent sampling predicts
and the precision-corrected estimate falls below the truth: the estimate is a lower bound."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
Ntrue, s1, s2, pr1, pr2 = 60000, 0.15, 0.10, 0.8, 0.7


def screens(sigma, rng):
    w = np.exp(rng.normal(0, sigma, Ntrue))
    w = w / w.mean()
    t1 = rng.random(Ntrue) < np.minimum(1, s1 * w)
    t2 = rng.random(Ntrue) < np.minimum(1, s2 * w)
    tp1, tp2, m = t1.sum(), t2.sum(), (t1 & t2).sum()
    fp1 = rng.poisson(tp1 * (1 - pr1) / pr1)
    fp2 = rng.poisson(tp2 * (1 - pr2) / pr2)
    m += rng.binomial(fp1, fp2 / 2e8) if fp1 else 0
    n1, n2 = tp1 + fp1, tp2 + fp2
    return n1, n2, m


naive, corr = [], []
for _ in range(400):
    n1, n2, m = screens(0.0, rng)
    naive.append(n1 * n2 / m)
    corr.append(n1 * pr1 * n2 * pr2 / m)
naive, corr = np.array(naive), np.array(corr)

sig = np.linspace(0, 1.5, 11)
med, lo, hi = [], [], []
for sgm in sig:
    e = []
    for _ in range(80):
        n1, n2, m = screens(sgm, rng)
        e.append(n1 * pr1 * n2 * pr2 / m)
    e = np.array(e)
    med.append(np.median(e)); lo.append(np.percentile(e, 5)); hi.append(np.percentile(e, 95))

fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.6))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.88, wspace=0.3)
bins = np.linspace(40, 140, 61)
a.hist(naive / 1e3, bins, color=P.fill("rna"), alpha=0.75, label="n1 n2 / m")
a.hist(corr / 1e3, bins, color=P.fill("dna"), alpha=0.75, label="precision-corrected")
a.axvline(Ntrue / 1e3, color=P.muted(), ls="--", lw=0.9)
a.legend(frameon=False, fontsize=7.5)
charts.style_axes(a, "estimated interactions (thousands)", "repetitions")
charts.title(a, "A  Independent screens")

b.fill_between(sig, np.array(lo) / 1e3, np.array(hi) / 1e3, color=P.fill("dna"), alpha=0.35, lw=0)
b.plot(sig, np.array(med) / 1e3, "o-", ms=3, color=charts.line("dna"), lw=1.4)
b.axhline(Ntrue / 1e3, color=P.muted(), ls="--", lw=0.9)
b.set_ylim(0, 70)
charts.style_axes(b, "heterogeneity of detectability sigma", "precision-corrected estimate (thousands)")
charts.title(b, "B  Shared detectability biases it downward")
