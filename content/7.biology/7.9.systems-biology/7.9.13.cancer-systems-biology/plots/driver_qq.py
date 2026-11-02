"""Why recurrence tests need the right background mutation rate (simulation). 18000 genes with
coding lengths drawn from a log-normal distribution (median 1.2 kb) are sequenced in 400 tumors. The
background rate per base varies between genes with a covariate x (standing for replication timing
and expression: late-replicating, silent genes have high x), log mu_g = log(1.5e-6) + 0.6 x + u_g with
u_g ~ N(0, 0.5^2), and 40 driver genes receive an excess of mutations. A: mutations per Mb per
tumor against x (drivers in red; genes without mutations are drawn at the bottom), with the
fitted rate (solid) and the genome-wide rate (dashed). B: quantile-quantile plot of -log10 p for the 17960 non-driver
genes under three background models: one genome-wide rate (Poisson), a rate depending on x (Poisson
regression), and the same with gene-to-gene overdispersion (negative binomial, dispersion estimated by moments after
leaving out the 1 % of genes with the largest residuals). C: the number of
genes called at a false discovery rate of 10 % (Benjamini-Hochberg) under each model, split into
true drivers and false positives."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, optimize
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
G, T = 18000, 400
L = rng.lognormal(np.log(1200), 0.6, G)
x = rng.normal(0, 1, G)
mu = 1.5e-6 * np.exp(0.6 * x + rng.normal(0, 0.5, G))
lam = mu * L * T
driver = np.zeros(G, bool)
driver[rng.choice(G, 40, replace=False)] = True
lam_obs = lam.copy()
lam_obs[driver] += rng.uniform(0.02, 0.15, 40) * T          # 2-15 % of tumors carry a driver mutation
n = rng.poisson(lam_obs)

# model 1: one genome-wide rate
r1 = n.sum() / (L.sum() * T)
e1 = r1 * L * T
p1 = stats.poisson.sf(n - 1, e1)


# model 2: Poisson regression of counts on x with offset log(L T)
def nll(b):
    eta = b[0] + b[1] * x + np.log(L * T)
    return np.sum(np.exp(eta) - n * eta)


b = optimize.minimize(nll, [np.log(r1), 0.0], method="BFGS").x
e2 = np.exp(b[0] + b[1] * x) * L * T
p2 = stats.poisson.sf(n - 1, e2)

# model 3: negative binomial, dispersion by moments from the residual variance, with the 1 % of genes
# with the largest Pearson residuals left out so that candidate drivers do not inflate it
pearson = (n - e2) / np.sqrt(e2)
core = pearson < np.quantile(pearson, 0.99)
phi = max(np.mean(((n - e2) ** 2 - e2)[core]) / np.mean(e2[core] ** 2), 1e-6)
r_nb = 1 / phi
p3 = stats.nbinom.sf(n - 1, r_nb, r_nb / (r_nb + e2))


def bh(p, q=0.1):
    o = np.argsort(p)
    ok = p[o] <= q * np.arange(1, p.size + 1) / p.size
    k = np.max(np.nonzero(ok)[0]) + 1 if ok.any() else 0
    hit = np.zeros(p.size, bool)
    hit[o[:k]] = True
    return hit


models = [("one rate", p1, "negative"), ("rate ~ x", p2, "highlight"), ("rate ~ x, overdispersed", p3, "positive")]
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(11, 3.6), gridspec_kw=dict(width_ratios=[1, 1, 0.8]))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.17, top=0.86, wspace=0.45)
rate = n / (L * T) * 1e6
ax1.semilogy(x[~driver], np.maximum(rate[~driver], 0.05), ".", ms=1.5, color=charts.line("neutral"), alpha=0.4)
ax1.semilogy(x[driver], rate[driver], "o", ms=3, color=charts.line("negative"))
xs = np.linspace(-4, 4, 50)
ax1.semilogy(xs, np.exp(b[0] + b[1] * xs) * 1e6, color=P.ink(), lw=1.2)
ax1.axhline(r1 * 1e6, color=P.ink(), ls="--", lw=1)
ax1.set_ylim(0.04, 400)
charts.style_axes(ax1, "covariate x", "mutations per Mb per tumor")
charts.title(ax1, "A  Rate varies with x")
m = (~driver).sum()
expct = -np.log10((np.arange(1, m + 1) - 0.5) / m)
for name, p, tok in models:
    ax2.plot(expct, np.sort(-np.log10(p[~driver]))[::-1], color=charts.line(tok), lw=1.6, label=name)
ax2.plot([0, 5], [0, 5], color=P.muted(), ls="--", lw=0.8)
ax2.set_ylim(0, 40)
ax2.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax2, "expected -log10 p", "observed -log10 p (non-drivers)")
charts.title(ax2, "B  Quantile-quantile plot")
calls = [(bh(p) & driver).sum() for _, p, _ in models]
false = [(bh(p) & ~driver).sum() for _, p, _ in models]
ypos = np.arange(3)
ax3.barh(ypos, calls, color=charts.line("positive"), label="true drivers")
ax3.barh(ypos, false, left=calls, color=charts.line("negative"), label="false positives")
for i in range(3):
    ax3.text(calls[i] + false[i] + 3, i, f"{calls[i]} + {false[i]}", va="center", fontsize=7, color=P.ink())
ax3.set_yticks(ypos)
ax3.set_yticklabels(["one rate", "rate ~ x", "rate ~ x,\noverdispersed"], fontsize=7)
ax3.invert_yaxis()
ax3.set_xlim(0, max(c + f for c, f in zip(calls, false)) * 1.35)
ax3.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax3, "genes called (FDR 10 %)", None)
charts.title(ax3, "C  Calls")
