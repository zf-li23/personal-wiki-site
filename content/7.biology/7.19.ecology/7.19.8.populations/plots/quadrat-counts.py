"""Quadrat counts: Poisson and negative binomial fits, and variance-mean relations.

A: frequency distribution of counts in 100 quadrats (illustrative data, Table in Example 8.4.1), with expected
frequencies under the Poisson distribution (same mean) and under the negative binomial distribution with k from the
method of moments, k = mean^2 / (s^2 - mean).
B: variance against mean for random samples of 50 quadrats at a range of mean densities (10 replicate sets each)
from a Poisson process and from negative binomial populations with k = 2 and k = 0.5; lines: s^2 = m (Poisson)
and s^2 = m + m^2 / k.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
freq = np.array([30, 18, 14, 10, 8, 6, 4, 3, 3, 2, 2])
x = np.arange(len(freq))
nq = freq.sum()
mean = (x * freq).sum() / nq
var = ((x - mean) ** 2 * freq).sum() / (nq - 1)
k = mean ** 2 / (var - mean)
pois = stats.poisson.pmf(x, mean) * nq
nb = stats.nbinom.pmf(x, k, k / (k + mean)) * nq

fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.0, 4.5))
ax.bar(x, freq, width=0.7, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.8, label="observed")
ax.plot(x, pois, "o-", color=P.edge("rna"), lw=1.4, ms=4, label=f"Poisson, mean {mean:.2f}")
ax.plot(x, nb, "s--", color=P.edge("plant"), lw=1.4, ms=4, label=f"negative binomial, $k$ = {k:.2f}")
ax.set_xticks(x)
ax.set_xlabel("individuals per quadrat")
ax.set_ylabel("number of quadrats")
ax.text(5.2, 19, f"$s^2$ = {var:.2f},  $s^2/\\bar x$ = {var / mean:.2f}", fontsize=9, color=P.ink())
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title("A  A clumped population (100 quadrats)", loc="left", fontsize=10)

means = np.logspace(-1, 1.5, 12)
for kk, tok, lab in ((None, "rna", "random (Poisson)"), (2.0, "highlight", "clumped, $k$ = 2"),
                     (0.5, "plant", "clumped, $k$ = 0.5")):
    mm, vv = [], []
    for mu in means:
        for _ in range(10):
            if kk is None:
                s = rng.poisson(mu, 50)
            else:
                s = rng.negative_binomial(kk, kk / (kk + mu), 50)
            if s.mean() > 0 and s.var(ddof=1) > 0:
                mm.append(s.mean())
                vv.append(s.var(ddof=1))
    bx.scatter(mm, vv, s=10, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.4, alpha=0.8)
    line = means if kk is None else means + means ** 2 / kk
    bx.plot(means, line, color=P.edge(tok), lw=1.8, label=lab)
bx.set_xscale("log")
bx.set_yscale("log")
bx.set_xlabel("mean per quadrat $\\bar x$")
bx.set_ylabel("variance $s^2$")
bx.legend(frameon=False, fontsize=8, loc="upper left")
bx.set_title("B  Variance grows faster than the mean when clumped", loc="left", fontsize=10)
for a in (ax, bx):
    for s in ("top", "right"):
        a.spines[s].set_visible(False)
fig.tight_layout()
