"""Degree distributions of an Erdos-Renyi graph (N = 50000, mean degree 6) and a Barabasi-Albert graph
(N = 50000, m = 3) drawn three ways: A linear bins on log-log axes, B logarithmic bins, C the
complementary cumulative distribution P(K >= k), with the maximum-likelihood power-law fit above the
k_min chosen by the Kolmogorov-Smirnov criterion of Clauset, Shalizi and Newman."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikigraph as G

rng = np.random.default_rng(4)
N, m = 50000, 3


def ba(n, m):
    pool = np.empty(2 * m * n, dtype=np.int64)
    size = 0
    for v in range(m + 1):  # start from a complete graph on m + 1 vertices
        for u in range(v):
            pool[size:size + 2] = (u, v)
            size += 2
    for v in range(m + 1, n):
        chosen = set()
        while len(chosen) < m:
            chosen.add(int(pool[rng.integers(size)]))
        for u in chosen:
            pool[size:size + 2] = (u, v)
            size += 2
    return np.bincount(pool[:size], minlength=n)


def er(n, c):
    e = rng.integers(0, n, (int(c * n / 2), 2))
    e = e[e[:, 0] != e[:, 1]]
    return np.bincount(e.ravel(), minlength=n)


def fit(k):
    """Discrete power-law fit (continuous approximation with kmin - 1/2) and KS choice of kmin."""
    best = None
    for kmin in range(int(k.min()), 200):
        tail = np.sort(k[k >= kmin])
        if tail.size < 100:
            break
        g = 1 + tail.size / np.log(tail / (kmin - 0.5)).sum()
        emp = np.arange(1, tail.size + 1) / tail.size
        model = 1 - ((tail + 0.5) / (kmin - 0.5)) ** (1 - g)
        d = np.max(np.abs(emp - model))
        if best is None or d < best[2]:
            best = (kmin, g, d, tail.size)
    return best


kb, ke = ba(N, m), er(N, 6.0)
kmin, gam, ks, ntail = fit(kb)

fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.4))
fig.subplots_adjust(wspace=0.32, left=0.07, right=0.98, bottom=0.17, top=0.88)
for k, col, name in ((ke, G.BLUE, "Erdős–Rényi"), (kb, G.RED, "Barabási–Albert")):
    vals, cnt = np.unique(k[k > 0], return_counts=True)
    axs[0].loglog(vals, cnt / N, "o", ms=2.5, color=col, label=name)
    edges = np.unique(np.floor(np.logspace(0, np.log10(k.max() + 1), 28)).astype(int))
    h, _ = np.histogram(k, bins=edges)
    w = np.diff(edges)
    mid = np.sqrt(edges[:-1] * (edges[1:] - 1).clip(edges[:-1]))
    axs[1].loglog(mid[h > 0], (h / w / N)[h > 0], "o", ms=3.5, color=col, label=name)
    ks_sorted = np.sort(k)
    ccdf = 1 - np.arange(N) / N
    axs[2].loglog(ks_sorted, ccdf, color=col, lw=1.4, label=name)
kk = np.arange(1, 21)
axs[1].loglog(kk, stats.poisson.pmf(kk, 6), color=G.BLUE, lw=0.8)
kk = np.logspace(np.log10(m), np.log10(kb.max()), 50)
axs[1].loglog(kk, 2 * m * (m + 1) / (kk * (kk + 1) * (kk + 2)), color="black", lw=0.9, ls="--",
              label=r"$\frac{2m(m+1)}{k(k+1)(k+2)}$")
frac = ntail / N
kk = np.logspace(np.log10(kmin), np.log10(kb.max()), 50)
axs[2].loglog(kk, frac * ((kk - 0.5) / (kmin - 0.5)) ** (1 - gam), color="black", lw=0.9, ls="--",
              label=rf"fit $\hat\gamma = {gam:.2f}$, $k_{{\min}} = {kmin}$")
titles = ("A  linear bins", "B  logarithmic bins", r"C  cumulative $P(K \geq k)$")
for ax, t in zip(axs, titles):
    ax.set_title(t, loc="left", fontsize=10)
    ax.set_xlabel(r"degree $k$")
    ax.legend(frameon=False, fontsize=7.5, loc="lower left")
axs[0].set_ylabel(r"$p_k$")
axs[2].set_ylim(1 / N / 2, 1.5)
