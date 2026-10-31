"""Statistics of complex networks. A: degree distributions of an Erdos-Renyi random graph
(N = 20000, mean degree 6) and of a Barabasi-Albert preferential-attachment graph (same size, m = 3
links per new vertex, logarithmic bins): Poisson against the power law P(k) = 2m(m+1)/k(k+1)(k+2) ~ k^-3. B: the Watts-Strogatz
construction (ring of N = 400 vertices, each linked to its 10 nearest neighbours, every edge
rewired with probability p): clustering coefficient C(p) and mean shortest path length L(p),
relative to the ring; for 0.003 < p < 0.05 paths are already short while clustering is still high,
the small-world regime."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(7)
N = 20000

# Erdos-Renyi: N k / 2 random edges
M = N * 3
e = rng.integers(0, N, (M, 2))
e = e[e[:, 0] != e[:, 1]]
deg_er = np.bincount(e.ravel(), minlength=N)

# Barabasi-Albert: each new vertex links to m existing ones chosen in proportion to degree
m = 3
targets = list(range(m))
pool = []
deg_ba = np.zeros(N, int)
for v in range(m, N):
    if pool:
        chosen = set()
        while len(chosen) < m:
            chosen.add(pool[rng.integers(len(pool))])
    else:
        chosen = set(targets)
    for u in chosen:
        pool += [u, v]
        deg_ba[u] += 1
        deg_ba[v] += 1

fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.4))
fig.subplots_adjust(wspace=0.3, left=0.08, right=0.98, bottom=0.17, top=0.88)
ax = axs[0]
k, c = np.unique(deg_er, return_counts=True)
ax.plot(k[k > 0], c[k > 0] / N, "o", ms=2.5, color=charts.line("dna"), label="random (Erdős–Rényi)")
edges = np.unique(np.round(np.logspace(np.log10(3), np.log10(deg_ba.max() + 1), 25)))
h, _ = np.histogram(deg_ba, bins=edges)
mid = np.sqrt(edges[:-1] * (edges[1:] - 1).clip(edges[:-1]))
ax.plot(mid[h > 0], (h / np.diff(edges) / N)[h > 0], "o", ms=3, color=charts.line("blood"),
        label="preferential attachment (log bins)")
kk = np.arange(1, 25)
ax.plot(kk, stats.poisson.pmf(kk, 6), color=charts.line("dna"), lw=1.0)
kk = np.logspace(0.5, 2.5, 50)
ax.plot(kk, 2 * m * (m + 1) / (kk * (kk + 1) * (kk + 2)), color=charts.line("blood"), lw=1.0, ls="--",
        label=r"$2m(m+1)/k(k+1)(k+2)$")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(1e-5, 0.5)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, "degree k", "fraction of vertices P(k)")
charts.title(ax, "A  Degree distributions")

ax = axs[1]
n, kh = 400, 5


def ws(p):
    edges = [(i, (i + j) % n) for i in range(n) for j in range(1, kh + 1)]
    S = set()
    out = []
    for a, b in edges:
        if rng.random() < p:
            while True:
                b = int(rng.integers(n))
                if b != a and (a, b) not in S and (b, a) not in S:
                    break
        S.add((a, b))
        out.append((a, b))
    A = np.zeros((n, n))
    for a, b in out:
        A[a, b] = A[b, a] = 1
    k = A.sum(1)
    tri = np.einsum("ij,jk,ki->i", A, A, A) / 2
    C = np.mean(np.where(k > 1, 2 * tri / (k * (k - 1)), 0))
    D = shortest_path(csr_matrix(A), unweighted=True)
    L = D[np.isfinite(D) & (D > 0)].mean()
    return C, L


C0, L0 = ws(0.0)
ps = np.logspace(-4, 0, 14)
res = np.array([np.mean([ws(p) for _ in range(2)], axis=0) for p in ps])
ax.plot(ps, res[:, 0] / C0, "o-", ms=3.5, lw=1.0, color=charts.line("protein"), label="clustering C(p)/C(0)")
ax.plot(ps, res[:, 1] / L0, "s-", ms=3.5, lw=1.0, color=charts.line("dna"), label="path length L(p)/L(0)")
ax.axvspan(0.003, 0.05, color=P.light("highlight"), lw=0)
ax.text(0.0035, 0.5, "small world", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "rewiring probability p", "relative to the ring")
charts.title(ax, "B  Small-world networks")
