"""A pooled CRISPR knockout screen for essential genes (simulation). 2000 genes, 4 guides each;
100 genes are essential: their guides deplete with log2 fold change -2.5 times a guide efficiency
drawn from Beta(4, 1.5), and 15% of all guides are inactive; 1% of the guides of non-essential
genes (84 guides) deplete with log2 fold change -3 because they cut toxic off-target sites. Guide abundances in the plasmid
library vary log-normally (SD 0.5), the mean depth is 500 reads per guide, and counts are negative
binomial with dispersion 0.05. Guides are tested for depletion against the negative binomial null,
ranked by p-value, and the ranks are aggregated per gene by alpha-robust rank aggregation (alpha
0.05; Formula 10.7.2) with a permutation p-value. A: guide log2 fold changes. B: gene scores
against the median guide log fold change; essential genes in red; dashed: FDR 0.05.
C: precision-recall curves for ranking genes by the RRA score, the mean and the median guide fold
change; a single off-target guide can make a gene look depleted by RRA or by the mean, not by the
median."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
ng, k, ness, depth, phi = 2000, 4, 100, 500, 0.05
gene = np.repeat(np.arange(ng), k)
ess = np.zeros(ng, bool)
ess[rng.choice(ng, ness, replace=False)] = True
eff = rng.beta(4, 1.5, ng * k) * (rng.random(ng * k) > 0.15)
lfc_true = np.where(ess[gene], -2.5 * eff, 0.0)
off = (~ess[gene]) & (rng.random(ng * k) < 0.01)          # 1% of guides cut toxic off-target sites
lfc_true[off] = -3.0
a = np.exp(rng.normal(0, 0.5, ng * k))
a = a / a.mean()


def nb(mu):
    r = 1 / phi
    return rng.negative_binomial(r, r / (r + mu))


c0 = nb(depth * a)
w = a * 2.0 ** lfc_true
c1 = nb(depth * w / w.mean())
s0, s1 = c0.sum() / (ng * k), c1.sum() / (ng * k)
mu1 = (c0 + 0.5) / s0 * s1                         # expected final count if the guide is neutral
lfc = np.log2((c1 + 0.5) / s1) - np.log2((c0 + 0.5) / s0)
r = 1 / phi
pg = stats.nbinom.cdf(c1, r, r / (r + mu1))        # lower tail: depletion
rank = stats.rankdata(pg) / len(pg)


def rra(ranks, alpha=0.05):
    """rho = min_j P(Beta(j, n - j + 1) <= r_(j)) over the guides with normalized rank <= alpha."""
    ranks = np.sort(ranks)
    n = len(ranks)
    sel = ranks[ranks <= alpha]
    if len(sel) == 0:
        return 1.0
    j = np.arange(1, len(sel) + 1)
    return stats.beta.cdf(sel, j, n - j + 1).min()


rho = np.array([rra(rank[gene == g]) for g in range(ng)])
null = np.array([rra(rng.random(k)) for _ in range(20000)])
pval = (1 + (null[None, :] <= rho[:, None]).sum(1)) / (1 + len(null))
o = np.argsort(pval)
q = np.empty(ng)
q[o] = np.minimum.accumulate((pval[o] * ng / np.arange(1, ng + 1))[::-1])[::-1]
med = np.array([np.median(lfc[gene == g]) for g in range(ng)])
mean = np.array([np.mean(lfc[gene == g]) for g in range(ng)])
hits = q < 0.05
TP, FP = (hits & ess).sum(), (hits & ~ess).sum()


def pr(score):
    o = np.argsort(score)
    tp = np.cumsum(ess[o])
    return tp / ness, tp / np.arange(1, ng + 1)


fig, (A, B, C) = plt.subplots(1, 3, figsize=(10.5, 3.4))
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.16, top=0.88, wspace=0.32)
bins = np.linspace(-6, 2.5, 69)
A.hist(lfc[~ess[gene]], bins, color=P.fill("neutral"), alpha=0.7, density=True, label="non-essential genes")
A.hist(lfc[ess[gene]], bins, histtype="step", color=charts.line("negative"), lw=1.4, density=True, label="essential genes")
A.legend(frameon=False, fontsize=7)
charts.style_axes(A, "guide log2 fold change", "density")
charts.title(A, "A  Guides")
B.scatter(med[~ess], -np.log10(pval[~ess]), s=4, color=P.muted(), lw=0)
B.scatter(med[ess], -np.log10(pval[ess]), s=7, color=charts.line("negative"), lw=0)
thr = pval[q < 0.05].max() if hits.any() else 1e-4
B.axhline(-np.log10(thr), color=P.muted(), ls="--", lw=0.8)
charts.style_axes(B, "median guide log2 fold change", "-log10 p (RRA)")
charts.title(B, f"B  Genes: {TP} essential, {FP} other at FDR 0.05")
for score, lab, tok in [(rho, "RRA score", "dna"), (mean, "mean fold change", "rna"), (med, "median fold change", "positive")]:
    rec, prec = pr(score)
    C.plot(rec, prec, color=charts.line(tok), lw=1.5, label=lab)
C.set_ylim(0, 1.05)
C.legend(frameon=False, fontsize=7, loc="lower left")
charts.style_axes(C, "recall", "precision")
charts.title(C, "C  Ranking the genes")
