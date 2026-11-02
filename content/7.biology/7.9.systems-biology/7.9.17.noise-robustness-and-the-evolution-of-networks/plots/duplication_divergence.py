"""Growth of a network by gene duplication and divergence. Starting from two linked vertices, a random
vertex u is duplicated; the copy keeps each of u's links with probability q (retention) and links to u
with probability p = 0.3. Twenty networks of 3000 vertices are grown for each q.
A: mean degree against network size (points: mean of the twenty networks; lines: the exact expectation
from the recursion E_(N+1) = E_N (1 + 2q/N) + p, Theorem 17.4.2). For q < 1/2 the mean degree approaches 2p/(1 - 2q) (3 for
q = 0.4); for q = 1/2 it grows like 2p ln N; for q > 1/2 like N^(2q - 1). The
sample mean scatters about the expectation, most for q > 1/2, because chance duplications of early hubs
are amplified as the network grows.
B: complementary cumulative degree distribution at N = 3000 (all twenty networks pooled): heavy tails
without preferential attachment; isolated vertices, which the model also produces, are not shown."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
pp, N = 0.3, 3000
sizes = np.unique(np.logspace(1, np.log10(N), 25).astype(int))


def grow(q):
    adj = [{1}, {0}]
    E = 1
    kbar = {}
    for n in range(2, N):
        u = int(rng.integers(n))
        nb = [w for w in adj[u] if rng.random() < q]
        new = set(nb)
        if rng.random() < pp:
            new.add(u)
        adj.append(new)
        for w in new:
            adj[w].add(n)
        E += len(new)
        if n + 1 in sizes:
            kbar[n + 1] = 2 * E / (n + 1)
    return kbar, np.array([len(a) for a in adj])


fig, axs = plt.subplots(1, 2, figsize=(8.5, 3.4))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.86, wspace=0.3)
for q, tok in [(0.4, "positive"), (0.5, "protein"), (0.6, "negative")]:
    runs = [grow(q) for _ in range(20)]
    ns = sorted(runs[0][0])
    km = [np.mean([r[0][n] for r in runs]) for n in ns]
    axs[0].loglog(ns, km, "o", ms=3.5, color=charts.line(tok), label=f"q = {q:g}")
    Ev, nn = [1.0], [2]
    for n in range(2, N):
        Ev.append(Ev[-1] * (1 + 2 * q / n) + pp)
        nn.append(n + 1)
    nn, Ev = np.array(nn), np.array(Ev)
    m = nn >= 5
    axs[0].loglog(nn[m], 2 * Ev[m] / nn[m], color=charts.line(tok), lw=1.2)
    deg = np.concatenate([r[1] for r in runs])
    deg = deg[deg > 0]
    ks = np.unique(deg)
    ccdf = np.array([(deg >= k).mean() for k in ks])
    axs[1].loglog(ks, ccdf, "-", lw=1.4, color=charts.line(tok), label=f"q = {q:g}")
axs[0].legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(axs[0], "number of vertices N", "mean degree")
charts.title(axs[0], "A  Mean degree")
axs[1].legend(fontsize=7, frameon=False, loc="lower left")
charts.style_axes(axs[1], "degree k", "P(degree >= k)")
charts.title(axs[1], "B  Degree distribution at N = 3000")
