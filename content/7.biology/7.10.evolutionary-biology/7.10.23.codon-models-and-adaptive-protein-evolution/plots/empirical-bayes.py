"""Empirical Bayes identification of sites under positive selection (Eq. (23.8)), in a simplified
model in which the data at codon site h are the numbers of nonsynonymous changes over the tree,
Poisson with mean omega_h * lambda_N (lambda_N = expected number of nonsynonymous changes per site for
omega = 1); synonymous changes do not depend on the class and cancel from the posterior. Sites belong
to three classes: omega = 0.05 (75 %), omega = 1 (15 %) and omega = 4 (10 %). A: posterior probability
of the class omega = 4 at each of 200 simulated sites with lambda_N = 1.5 (bars), computed with the
true parameter values; ticks mark the sites truly in that class; dashed: the cutoff 0.95. B: as the
tree becomes longer (larger lambda_N, more sequences or more divergence), the proportion of truly
selected sites identified at P > 0.95 (power) increases, while the proportion of identified sites
that are not truly selected (false discovery proportion) stays low (means of 200 simulated proteins)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(11)
p = np.array([0.75, 0.15, 0.10])
w = np.array([0.05, 1.0, 4.0])


def simulate(L, lam):
    k = rng.choice(3, L, p=p)
    x = rng.poisson(w[k] * lam)
    like = stats.poisson.pmf(x[:, None], w[None, :] * lam) * p[None, :]
    return k, like[:, 2] / like.sum(1)


fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8), gridspec_kw=dict(width_ratios=[1.6, 1]))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.9, wspace=0.25)
k, post = simulate(200, 1.5)
site = np.arange(1, 201)
a.bar(site, post, width=1.0, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.3)
a.scatter(site[k == 2], np.full((k == 2).sum(), 1.06), marker="|", s=40, color=charts.line("negative"))
a.axhline(0.95, color=P.muted(), lw=0.8, ls="--")
a.set_xlim(0, 201)
a.set_ylim(0, 1.12)
charts.style_axes(a, "codon site", "$\\mathbb{P}(\\omega_h = 4 \\mid x_h)$")
charts.title(a, "A  Posterior probability of positive selection along a protein")
lams = np.array([0.5, 1, 1.5, 2, 3, 4, 6, 8])
power, fdp = [], []
for lam in lams:
    pw, fd = [], []
    for _ in range(200):
        kk, pp = simulate(200, lam)
        call = pp > 0.95
        pw.append(call[kk == 2].mean() if (kk == 2).any() else np.nan)
        fd.append((kk[call] != 2).mean() if call.any() else 0.0)
    power.append(np.nanmean(pw))
    fdp.append(np.mean(fd))
b.plot(lams, power, "o-", color=charts.line("dna"), lw=1.5, ms=3.5, label="power")
b.plot(lams, fdp, "s--", color=charts.line("negative"), lw=1.2, ms=3.5, label="false discovery proportion")
b.set_ylim(0, 1)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "$\\lambda_{\\mathrm{N}}$ (expected changes per site at $\\omega = 1$)", "proportion")
charts.title(b, "B  Power grows with tree length")
