"""Transcript-length bias in over-representation analysis (simulation). 15000 genes with log-normal
lengths (median 2 kb) and expression; 10% of them, chosen independently of length, change twofold.
Counts are negative binomial (dispersion 0.05) in 3 + 3 samples, and genes are called differentially
expressed at p < 0.001. A: the fraction of genes called in each length bin rises with length,
although the true fraction is the same in every bin (dashed): a long gene collects more reads, so
the same fold change is easier to detect. The line is the probability weighting function used for
correction. B: 200 gene sets of 150 genes, drawn with a preference for long genes but with no
association with the true changes. Hypergeometric p-values (red) are far from uniform; p-values
from a null that draws the selected genes with the length-dependent probabilities of A (blue, 2000
draws, the resampling idea of GOseq) are close to uniform."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
G, n, phi = 15000, 3, 0.05
length = np.exp(rng.normal(np.log(2000), 0.8, G))
expr = np.exp(rng.normal(np.log(20), 1.2, G))  # reads per kb per library
mu = expr * length / 1000
de = rng.random(G) < 0.1
lfc = np.where(de, rng.choice([-1, 1], G), 0) * np.log(2)


def nb(m, size):
    return rng.poisson(rng.gamma(1 / phi, m[:, None] * phi, size=(m.size, size)))


a, b = nb(mu, n), nb(mu * np.exp(lfc), n)
ma, mb = a.mean(1) + 0.5 / n, b.mean(1) + 0.5 / n
z = np.log(mb / ma) / np.sqrt((1 / ma + 1 / mb + 2 * phi) / n)
called = 2 * stats.norm.sf(np.abs(z)) < 0.001
K = int(called.sum())

edges = np.quantile(length, np.linspace(0, 1, 11))
mid, frac = [], []
for lo, hi in zip(edges[:-1], edges[1:]):
    s = (length >= lo) & (length <= hi)
    mid.append(np.exp(np.log(length[s]).mean()))
    frac.append(called[s].mean())
# probability weighting function: called fraction as a smooth function of log length (logistic fit)
X = np.c_[np.ones(G), np.log(length)]
beta = np.zeros(2)
for _ in range(25):
    p = 1 / (1 + np.exp(-X @ beta))
    beta += np.linalg.solve(X.T @ (X * (p * (1 - p))[:, None]), X.T @ (called - p))
pwf = 1 / (1 + np.exp(-X @ beta))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 3.6))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.88, wspace=0.3)
ax1.plot(mid, frac, "o", color=charts.line("rna"), ms=5)
gl = np.exp(np.linspace(np.log(length.min()), np.log(length.max()), 200))
ax1.plot(gl, 1 / (1 + np.exp(-(beta[0] + beta[1] * np.log(gl)))), color=charts.line("rna"), lw=1.2)
ax1.axhline(0.1, color=P.muted(), ls="--", lw=0.8)  # fraction truly changed
ax1.set_xscale("log")
ax1.set_ylim(0, 0.11)
charts.style_axes(ax1, "gene length (nt), deciles", "fraction called DE")
charts.title(ax1, f"A  Detection depends on length ({K} genes called)")

S, m = 200, 150
w = length ** 1.5
w /= w.sum()
sets = np.zeros((S, G), bool)
for i in range(S):
    sets[i, rng.choice(G, m, replace=False, p=w)] = True
k_obs = sets[:, called].sum(1)
p_hyper = stats.hypergeom.sf(k_obs - 1, G, m, K)
B = 2000
q = pwf / pwf.sum()
null = np.empty((B, S))
for bidx in range(B):
    pick = np.zeros(G, bool)
    pick[rng.choice(G, K, replace=False, p=q)] = True
    null[bidx] = sets[:, pick].sum(1)
p_adj = (1 + (null >= k_obs).sum(0)) / (B + 1)
bins = np.linspace(0, 1, 21)
ax2.hist(p_hyper, bins, color=P.fill("negative"), alpha=0.7, label="hypergeometric")
ax2.hist(p_adj, bins, color=P.fill("dna"), alpha=0.7, label="length-weighted null")
ax2.axhline(S / 20, color=P.muted(), ls="--", lw=0.8)
ax2.legend(frameon=False, fontsize=7.5)
charts.style_axes(ax2, "ORA p-value of a long-gene set", "number of sets")
charts.title(ax2, f"B  p < 0.05 in {np.sum(p_hyper < 0.05)} vs {np.sum(p_adj < 0.05)} of {S} sets")
