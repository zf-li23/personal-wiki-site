"""Robustness of an Erdos-Renyi graph (N = 10000, mean degree 4) and a Barabasi-Albert graph
(N = 10000, m = 2, mean degree 4) to the removal of a fraction f of the vertices, at random (failures)
or in decreasing order of degree (attack). The curves show the size of the largest component relative
to N, averaged over 5 realizations; the black line is the theory for random removal from the random
graph, (1 - f) S with S = 1 - exp(-c(1 - f)S)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikigraph as G

rng = np.random.default_rng(6)
N = 10000


def er_edges(n, c):
    e = rng.integers(0, n, (int(c * n / 2), 2))
    return e[e[:, 0] != e[:, 1]]


def ba_edges(n, m):
    pool = np.empty(2 * m * n, dtype=np.int64)
    size = 0
    for v in range(m + 1):
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
    return pool[:size].reshape(-1, 2)


def largest_after_removal(n, edges, order):
    """Newman-Ziff: put the vertices back in reverse order of removal, tracking the largest cluster."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    parent = list(range(n))
    size = [1] * n
    present = [False] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    big = 0
    out = np.zeros(n + 1)
    for i, v in enumerate(order[::-1]):
        present[v] = True
        big = max(big, 1)
        for u in adj[v]:
            if present[u]:
                a, b = find(u), find(v)
                if a != b:
                    if size[a] < size[b]:
                        a, b = b, a
                    parent[b] = a
                    size[a] += size[b]
                    big = max(big, size[a])
        out[n - i - 1] = big  # vertices removed: n - i - 1
    return out / n


f = np.arange(N + 1) / N
fig, ax = plt.subplots(figsize=(6.4, 3.8))
fig.subplots_adjust(left=0.11, right=0.97, bottom=0.14, top=0.95)
styles = {("ER", "random"): (G.BLUE, "-"), ("ER", "attack"): (G.BLUE, "--"),
          ("BA", "random"): (G.RED, "-"), ("BA", "attack"): (G.RED, "--")}
curves = {key: np.zeros(N + 1) for key in styles}
for _ in range(5):
    for name, edges in (("ER", er_edges(N, 4.0)), ("BA", ba_edges(N, 2))):
        deg = np.bincount(edges.ravel(), minlength=N)
        orders = {"random": rng.permutation(N),
                  "attack": np.lexsort((rng.random(N), -deg))}
        for kind, order in orders.items():
            curves[(name, kind)] += largest_after_removal(N, edges, order) / 5
labels = {"ER": "Erdős–Rényi", "BA": "Barabási–Albert"}
for (name, kind), (col, ls) in styles.items():
    ax.plot(f, curves[(name, kind)], color=col, ls=ls, lw=1.5, label=f"{labels[name]}, {kind}")


def theory(q, c=4.0):
    cc = c * (1 - q)
    return 0.0 if cc <= 1 else (1 - q) * brentq(lambda s: s - 1 + np.exp(-cc * s), 1e-12, 1.0)


qq = np.linspace(0, 1, 300)
ax.plot(qq, [theory(q) for q in qq], color="black", lw=0.8, label="theory, random removal (ER)")
ax.axvline(0.75, color=G.GREY, lw=0.8, ls=":")
ax.text(0.755, 0.9, r"$f_c = 1 - 1/c$", fontsize=8)
ax.set_xlabel(r"fraction of vertices removed $f$")
ax.set_ylabel("largest component / N")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.02)
ax.legend(frameon=False, fontsize=8, loc="upper right", bbox_to_anchor=(1.0, 0.85))
