"""Priors on branch lengths and topologies. A: the prior on the tree length T (sum of 2s - 3 branch
lengths) for s = 123 sequences induced by independent exponential priors with mean 0.1 on each branch
(a gamma distribution with mean 24.3), compared with the gamma-Dirichlet prior with a gamma(1, 1) prior on
T (mean 1); the vertical line marks a maximum likelihood tree length of 2.48 (lizard mitochondrial data
quoted by Yang (2014)). B: the induced prior on one branch length under the two priors. C: the expected
number of clades of each size k in a rooted tree of n = 10 tips under the uniform prior on labeled
topologies and under the Yule prior (equivalently, uniform on labeled histories), from the formulas
C(n, k) R(k) R(n - k + 1)/R(n), with R(m) = (2m - 3)!!, and 2n/(k(k + 1)); dots: 20 000 simulated Yule
trees."""
import numpy as np
import matplotlib.pyplot as plt
from math import comb
from scipy.stats import gamma, beta
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

fig, (a, b, c) = plt.subplots(1, 3, figsize=(12.0, 3.8))
fig.subplots_adjust(left=0.06, right=0.985, bottom=0.16, top=0.9, wspace=0.3)
s = 123
K = 2 * s - 3
T = np.logspace(-2, 2, 800)
a.plot(T, T * gamma.pdf(T, K, scale=0.1), color=charts.line("negative"), lw=1.6, label="i.i.d. Exp(mean 0.1)")
a.plot(T, T * gamma.pdf(T, 1, scale=1.0), color=charts.line("dna"), lw=1.6, label="gamma-Dirichlet, T ~ G(1, 1)")
a.axvline(2.48, color=P.muted(), lw=0.8, ls=":")
a.text(2.6, 0.9, "MLE 2.48", fontsize=FT["tiny"], color=P.ink())
a.set_xscale("log")
a.set_ylim(0, 3.6)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "tree length $T$", "density of $\\log T$")
charts.title(a, f"A  Induced prior on tree length ($s = {s}$)")

t = np.logspace(-6, 1, 200)
a_iid = t * gamma.pdf(t, 1, scale=0.1)
# gamma-Dirichlet: t = T x with T ~ G(1, 1), x ~ Beta(1, K - 1); density by numerical integration over T
Tg = np.logspace(-4, 2, 800)
wT = gamma.pdf(Tg, 1, scale=1.0)
dens = np.array([np.trapezoid(wT * beta.pdf(ti / Tg, 1, K - 1) / Tg, Tg) for ti in t])
b.plot(t, a_iid, color=charts.line("negative"), lw=1.6, label="i.i.d. Exp(mean 0.1)")
b.plot(t, t * dens, color=charts.line("dna"), lw=1.6, label="gamma-Dirichlet")
b.set_xscale("log")
b.set_ylim(0, None)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "branch length $t$", "density of $\\log t$")
charts.title(b, "B  Induced prior on one branch")


def R(m):
    r = 1
    for j in range(3, 2 * m - 2, 2):
        r *= j
    return r


nn = 10
k = np.arange(2, nn)
uni = [comb(nn, kk) * R(kk) * R(nn - kk + 1) / R(nn) for kk in k]
yule = 2 * nn / (k * (k + 1))
rng = np.random.default_rng(5)
cnt = np.zeros(nn + 1)
for _ in range(20000):
    g = [1] * nn
    while len(g) > 1:
        i, j = sorted(rng.choice(len(g), 2, replace=False))
        m = g[i] + g[j]
        cnt[m] += 1
        g = [v for q, v in enumerate(g) if q not in (i, j)] + [m]
c.plot(k, uni, "s-", color=charts.line("rna"), lw=1.4, ms=4, label="uniform on topologies")
c.plot(k, yule, "-", color=charts.line("plant"), lw=1.4, label="Yule (labeled histories)")
c.plot(k, cnt[2:nn] / 20000, "o", color=charts.line("plant"), ms=3.5, mfc="none", label="simulated Yule trees")
c.set_yscale("log")
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(c, "clade size $k$", "expected number of clades")
charts.title(c, f"C  Topology priors, $n = {nn}$")
