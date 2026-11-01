"""Methylation levels from bisulfite sequencing and the test for differential methylation (simulated).
Each CpG of each sample has a true methylation fraction drawn from a beta distribution around the group
mean (precision 10, so replicates differ biologically), and its coverage is Poisson with mean 12; the
numbers of methylated reads are binomial. A: 40 CpGs over 4 kb in three samples of each of two groups;
CpGs 15-28 form a differentially methylated region (group means 0.80 and 0.30, elsewhere 0.75 in both).
Points are single-sample levels M/(M + U), lines the running means over five CpGs of the pooled group
levels. B: 20000 null CpGs (equal group means 0.7) tested with Fisher's exact test on the counts pooled over
replicates, which ignores biological variation, and with a Wald test in which the variance of each
sample's level is inflated by the beta-binomial factor 1 + (N - 1) rho (rho estimated from the data);
the fraction of p-values below 0.05 should be 5 %. The spikes of the Fisher histogram come from the
discreteness of the exact test."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
prec, depth = 10.0, 12


def sample(mean, shape):
    m = rng.beta(mean * prec, (1 - mean) * prec, shape)
    N = rng.poisson(depth, shape)
    M = rng.binomial(N, m)
    return M, N


ncpg = 40
pos = np.sort(rng.uniform(0, 4000, ncpg))
mA = np.full(ncpg, 0.75); mB = np.full(ncpg, 0.75)
dmr = np.arange(14, 28)
mA[dmr], mB[dmr] = 0.80, 0.30
MA, NA = sample(mA, (3, ncpg))
MB, NB = sample(mB, (3, ncpg))

fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.8), gridspec_kw={"width_ratios": [1.5, 1]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.88, wspace=0.28)
ax = axs[0]
ax.axvspan(pos[dmr[0]] / 1000, pos[dmr[-1]] / 1000, color=P.fill("neutral"), alpha=0.35, lw=0)
for M, N, tok, name in [(MA, NA, "negative", "group 1"), (MB, NB, "dna", "group 2")]:
    with np.errstate(invalid="ignore"):
        lv = M / N
    for r in range(3):
        ax.plot(pos / 1000, lv[r], "o", ms=3, color=charts.line(tok), alpha=0.6, mew=0)
    pooled = M.sum(0) / np.maximum(N.sum(0), 1)
    sm = np.convolve(pooled, np.ones(5) / 5, mode="same")
    sm[:2] = pooled[:2]; sm[-2:] = pooled[-2:]
    ax.plot(pos / 1000, sm, color=charts.line(tok), lw=1.6, label=name)
ax.set_ylim(-0.03, 1.03)
ax.legend(frameon=False, fontsize=7.5, loc="lower left")
charts.style_axes(ax, "position (kb)", "methylation level")
charts.title(ax, "A  A differentially methylated region")

# B: calibration on null CpGs
G = 20000
M1, N1 = sample(np.full(G, 0.7), (3, G))
M2, N2 = sample(np.full(G, 0.7), (3, G))
pf = np.array([stats.fisher_exact([[a, b - a], [c, d - c]])[1] for a, b, c, d in
               zip(M1.sum(0), N1.sum(0), M2.sum(0), N2.sum(0))])
# moment estimate of rho: the Pearson statistic of each group, corrected for the estimated mean
num = den = 0.0
for M, N in ((M1, N1), (M2, N2)):
    Nt = N.sum(0)
    p = M.sum(0) / np.maximum(Nt, 1)
    ok = (p > 0) & (p < 1)
    X2 = ((M - N * p) ** 2 / (p * (1 - p) + 1e-12))[:, ok].sum()
    f = (1 - N / np.maximum(Nt, 1))[:, ok]
    num += X2 - (N[:, ok] * f).sum()
    den += (N[:, ok] * (N[:, ok] - 1) * f).sum()
rho = num / den


def wald(M, N):
    p = M.sum(0) / np.maximum(N.sum(0), 1)
    v = (N * p * (1 - p) * (1 + (N - 1) * rho)).sum(0) / np.maximum(N.sum(0), 1) ** 2
    return p, v


p1, v1 = wald(M1, N1); p2, v2 = wald(M2, N2)
z = (p1 - p2) / np.sqrt(np.maximum(v1 + v2, 1e-12))
pw = 2 * stats.norm.sf(np.abs(z))
print("rho_hat", round(rho, 4), "true", round(1 / (1 + prec), 4),
      "FPR Fisher pooled", round(np.mean(pf < 0.05), 4), "FPR beta-binomial Wald", round(np.mean(pw < 0.05), 4))
ax = axs[1]
bins = np.linspace(0, 1, 21)
ax.hist(pf, bins=bins, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.4, alpha=0.9,
        label=f"Fisher, pooled reads: {100 * np.mean(pf < 0.05):.0f}% < 0.05")
ax.hist(pw, bins=bins, histtype="step", color=charts.line("dna"), lw=1.6,
        label=f"beta-binomial Wald: {100 * np.mean(pw < 0.05):.1f}% < 0.05")
ax.axhline(G / 20, color=P.muted(), lw=0.8, ls="--")
ax.legend(frameon=False, fontsize=7.5, loc="upper right")
charts.style_axes(ax, "p-value", "null CpGs")
charts.title(ax, "B  Replicates, not reads")
