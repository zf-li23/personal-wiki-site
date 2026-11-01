"""The Watts-Strogatz model: a ring of N = 1000 vertices, each joined to its K = 10 nearest neighbours,
with every edge rewired with probability p. A: three small examples (N = 20, K = 4). B: clustering
coefficient C(p) and average path length l(p) relative to the ring (averages of 4 realizations), with
the Barrat-Weigt approximation C(p)/C(0) = (1 - p)^3."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
import wikigraph as G

rng = np.random.default_rng(2)


def ws(n, k, p):
    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(1, k // 2 + 1):
            adj[i].add((i + j) % n)
            adj[(i + j) % n].add(i)
    for i in range(n):
        for j in range(1, k // 2 + 1):
            t = (i + j) % n
            if t in adj[i] and rng.random() < p:
                new = rng.integers(n)
                while new == i or new in adj[i]:
                    new = rng.integers(n)
                adj[i].discard(t)
                adj[t].discard(i)
                adj[i].add(new)
                adj[new].add(i)
    return adj


def stats(adj):
    n = len(adj)
    c = []
    for i in range(n):
        nb = list(adj[i])
        k = len(nb)
        if k < 2:
            c.append(0.0)
            continue
        t = sum(1 for a in range(k) for b in range(a + 1, k) if nb[b] in adj[nb[a]])
        c.append(2 * t / (k * (k - 1)))
    rows = [i for i in range(n) for _ in adj[i]]
    cols = [j for i in range(n) for j in adj[i]]
    d = shortest_path(csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n)), unweighted=True)
    d = d[np.isfinite(d) & (d > 0)]
    return np.mean(c), d.mean()


fig = plt.figure(figsize=(9.0, 6.4))
axes = [fig.add_axes([0.02 + 0.33 * i, 0.58, 0.29, 0.36]) for i in range(3)]
for ax, p, name in zip(axes, (0.0, 0.1, 1.0), ("regular ring, p = 0", "small world, p = 0.1", "random, p = 1")):
    adj = ws(20, 4, p)
    pos = G.circle(range(20), radius=1.0, center=(1.1, 1.1))
    edges = [(i, j) for i in range(20) for j in adj[i] if i < j]
    ax.set_xlim(-0.1, 2.3)
    ax.set_ylim(-0.1, 2.3)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(name, fontsize=10)
    G.draw(ax, pos, edges, labels=False, radius=0.07, width=1.0)

bx = fig.add_axes([0.1, 0.09, 0.85, 0.4])
n, k = 1000, 10
c0, l0 = stats(ws(n, k, 0.0))
ps = np.logspace(-4, 0, 14)
cr, lr = [], []
for p in ps:
    vals = np.array([stats(ws(n, k, p)) for _ in range(4)])
    cr.append(vals[:, 0].mean() / c0)
    lr.append(vals[:, 1].mean() / l0)
bx.semilogx(ps, cr, "o", color=G.BLUE, ms=5, label=r"$C(p)/C(0)$")
bx.semilogx(ps, lr, "s", color=G.RED, ms=5, label=r"$\ell(p)/\ell(0)$")
pp = np.logspace(-4, 0, 200)
bx.semilogx(pp, (1 - pp) ** 3, color=G.BLUE, lw=0.9, ls="--", label=r"$(1-p)^3$")
bx.axvspan(0.003, 0.05, color=G.GREY, alpha=0.2, lw=0)
bx.text(0.0125, 0.5, "small world", ha="center", fontsize=9)
bx.set_xlabel(r"rewiring probability $p$")
bx.set_ylabel("relative to the ring")
bx.set_ylim(0, 1.08)
bx.legend(frameon=False, fontsize=9, loc="lower left")
bx.set_title(f"B  N = {n}, K = {k}: C(0) = {c0:.3f}, l(0) = {l0:.1f}", loc="left", fontsize=10)
fig.text(0.01, 0.96, "A", fontsize=11)
