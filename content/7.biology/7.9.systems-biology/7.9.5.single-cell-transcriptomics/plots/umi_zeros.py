"""Zeros and variance in UMI counts (simulated: 3000 cells, 2000 genes, cell size factors log-normal with
s.d. 0.4, biological variation gamma-distributed with shape 5, so that counts are negative binomial given
the size factor). A: the fraction of cells with a zero count for each gene against its mean count; the
curves are the Poisson prediction exp(-mu) and the negative binomial prediction (1 + mu/theta)^(-theta)
averaged over the cell size factors. The 100 marker genes expressed in only one of two cell types
(orange) lie above the curve: their extra zeros come from heterogeneity, not from a technical dropout. B:
variance of each gene after the shifted logarithm log(1 + 10^4 x/n) and after analytic Pearson residuals
(theta = 100, clipped at sqrt(N)) against the mean: the logarithm leaves a strong dependence on the mean,
the residuals of genes without biological variation (dark) have variance close to 1, slightly less at
high means because of the overdispersion theta = 100 assumed for all genes, and genes with biological variation
rise above 1. C: the counts of one gene with
mean 2 (bars) and the Poisson and negative binomial distributions with the same mean."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
N, G, theta = 3000, 2000, 5.0
s = rng.lognormal(0, 0.4, N); s /= s.mean()
mu = np.exp(rng.uniform(np.log(0.01), np.log(50), G))
typ = rng.random(N) < 0.5
lam = s[:, None] * mu[None, :] * rng.gamma(theta, 1 / theta, (N, G))
marker = np.arange(100)
lam[:, marker] *= np.where(typ, 2.0, 0.0)[:, None]
X = rng.poisson(lam)
# null genes without biological variation, for panel B
mu0 = np.exp(rng.uniform(np.log(0.01), np.log(50), 400))
X0 = rng.poisson(s[:, None] * mu0[None, :])

fig, axs = plt.subplots(1, 3, figsize=(12.4, 3.6))
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.17, top=0.88, wspace=0.32)
ax = axs[0]
m = X.mean(0); z = (X == 0).mean(0)
other = np.ones(G, bool); other[marker] = False
ax.scatter(m[other], z[other], s=4, lw=0, color=charts.line("dna"), label="genes, one cell type", rasterized=True)
ax.scatter(m[marker], z[marker], s=6, lw=0, color=charts.line("rna"), label="markers of one of two types")
g = np.logspace(-2.2, 2, 200)
ax.plot(g, np.exp(-g), color=P.muted(), lw=1.1, ls="--", label="Poisson")
nbz = np.array([np.mean((1 + s * x / theta) ** (-theta)) for x in g])
ax.plot(g, nbz, color=P.ink(), lw=1.1, label="negative binomial")
ax.set_xscale("log")
ax.legend(frameon=False, fontsize=7, loc="lower left")
charts.style_axes(ax, "mean UMI count per cell", "fraction of zeros")
charts.title(ax, "A  Zeros follow the count model")

ax = axs[1]
Xa = np.hstack([X[:, other], X0])
ma = Xa.mean(0)
n = Xa.sum(1, keepdims=True)
lg = np.log1p(1e4 * Xa / n)
mu_hat = n * Xa.sum(0, keepdims=True) / Xa.sum()
th = 100.0
r = (Xa - mu_hat) / np.sqrt(mu_hat + mu_hat ** 2 / th)
r = np.clip(r, -np.sqrt(N), np.sqrt(N))
nullg = np.r_[np.zeros(other.sum(), bool), np.ones(X0.shape[1], bool)]
for v, tok, lab in [(lg.var(0), "rna", "shifted log"), (r.var(0), "dna", "Pearson residuals")]:
    ax.scatter(ma[~nullg], v[~nullg], s=3, lw=0, color=P.fill(tok), rasterized=True)
    ax.scatter(ma[nullg], v[nullg], s=5, lw=0, color=charts.line(tok), label=f"{lab} (dark: no biological variation)", rasterized=True)
ax.axhline(1, color=P.muted(), lw=0.6, ls=":")
ax.set_xscale("log"); ax.set_yscale("log")
ax.legend(frameon=False, fontsize=7, loc="upper left")
charts.style_axes(ax, "mean UMI count per cell", "variance across cells")
charts.title(ax, "B  Variance after normalization")

ax = axs[2]
j = np.argmin(np.abs(mu[other] - 2.0))
x = X[:, other][:, j]
kk = np.arange(0, 13)
ax.bar(kk, np.bincount(x, minlength=13)[:13] / N, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.5, label="cells")
mm, vv = x.mean(), x.var()
thm = mm ** 2 / max(vv - mm, 1e-9)
ax.plot(kk, stats.poisson.pmf(kk, mm), "o--", color=P.muted(), ms=3.5, lw=1, label=f"Poisson, mean {mm:.2f}")
ax.plot(kk, stats.nbinom.pmf(kk, thm, thm / (thm + mm)), "o-", color=charts.line("dna"), ms=3.5, lw=1.2,
        label=f"NB, theta = {thm:.1f}")
ax.legend(frameon=False, fontsize=7.5)
charts.style_axes(ax, "UMI count", "fraction of cells")
charts.title(ax, "C  One gene")
print("gene mean", mm, "var", vv, "theta", thm, "zeros obs", np.mean(x == 0), "pois", np.exp(-mm),
      "nb", (1 + mm / thm) ** -thm)
print("null var log range", lg.var(0)[nullg].min(), lg.var(0)[nullg].max(), "resid", r.var(0)[nullg].min(), r.var(0)[nullg].max())
