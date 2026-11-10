"""PC algorithm with Fisher-z tests on simulated linear Gaussian data: structure recovery versus sample size."""

from itertools import combinations

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
p = 5
# True DAG X1 -> X2, X1 -> X3, X2 -> X4, X3 -> X4, X3 -> X5, X4 -> X5 (0-based indices)
B = np.zeros((p, p))
for (i, j), w in {(0, 1): -0.6, (0, 2): -0.7, (1, 3): -0.7, (2, 3): 0.9, (2, 4): 0.9, (3, 4): -0.8}.items():
    B[i, j] = w
true_skel = {frozenset((i, j)) for i in range(p) for j in range(p) if B[i, j] != 0}
true_cpdag = {(1, 3), (2, 3), (3, 4), (2, 4)}  # directed edges of the CPDAG; X1-X2, X1-X3 stay undirected


def simulate(n):
    x = np.zeros((n, p))
    for j in range(p):
        x[:, j] = x @ B[:, j] + rng.normal(0, 1, n)
    return x


def ci_test(corr, n, i, j, s, alpha):
    """Fisher-z test of zero partial correlation between i and j given s; True means independent."""
    idx = [i, j, *s]
    prec = np.linalg.inv(corr[np.ix_(idx, idx)])
    r = -prec[0, 1] / np.sqrt(prec[0, 0] * prec[1, 1])
    z = 0.5 * np.log((1 + r) / (1 - r)) * np.sqrt(n - len(s) - 3)
    return 2 * stats.norm.sf(abs(z)) > alpha


def pc(x, alpha=0.05):
    n = x.shape[0]
    corr = np.corrcoef(x, rowvar=False)
    adj = {i: set(range(p)) - {i} for i in range(p)}
    sepset = {}
    size = 0
    while any(len(adj[i]) - 1 >= size for i in range(p)):
        frozen = {i: set(adj[i]) for i in range(p)}  # PC-stable: neighbours fixed within a level
        for i in range(p):
            for j in list(frozen[i]):
                if j not in adj[i]:
                    continue
                for s in combinations(sorted(frozen[i] - {j}), size):
                    if ci_test(corr, n, i, j, s, alpha):
                        adj[i].discard(j)
                        adj[j].discard(i)
                        sepset[frozenset((i, j))] = set(s)
                        break
        size += 1
    directed = set()
    for k in range(p):  # v-structures i -> k <- j
        for i, j in combinations(sorted(adj[k]), 2):
            if j not in adj[i] and k not in sepset.get(frozenset((i, j)), set()):
                directed |= {(i, k), (j, k)}
    changed = True
    while changed:  # Meek rules 1 and 2
        changed = False
        for i in range(p):
            for j in adj[i]:
                if (i, j) in directed or (j, i) in directed:
                    continue
                rule1 = any((k, i) in directed and j not in adj[k] and k != j for k in range(p))
                rule2 = any((i, k) in directed and (k, j) in directed for k in range(p))
                if rule1 or rule2:
                    directed.add((i, j))
                    changed = True
    skel = {frozenset((i, j)) for i in range(p) for j in adj[i]}
    return skel, directed


sizes = [25, 50, 100, 200, 400, 800, 1600, 3200]
reps = 200
skel_ok, cpdag_ok, shd = [], [], []
for n in sizes:
    a = b = 0
    d = []
    for _ in range(reps):
        skel, directed = pc(simulate(n))
        a += skel == true_skel
        b += skel == true_skel and directed == true_cpdag
        d.append(len(skel ^ true_skel))
    skel_ok.append(a / reps)
    cpdag_ok.append(b / reps)
    shd.append(np.mean(d))

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
axes[0].plot(sizes, skel_ok, "o-", label="skeleton correct")
axes[0].plot(sizes, cpdag_ok, "s--", label="CPDAG correct")
axes[0].set_xscale("log")
axes[0].set_xlabel("sample size $n$")
axes[0].set_ylabel("proportion of 200 replications")
axes[0].set_ylim(0, 1.02)
axes[0].legend(fontsize=9)
axes[1].plot(sizes, shd, "o-", color="C3")
axes[1].set_xscale("log")
axes[1].set_xlabel("sample size $n$")
axes[1].set_ylabel("mean number of wrong edges in skeleton")
fig.suptitle("PC algorithm, Fisher-z tests at level 0.05, linear Gaussian SEM on 5 variables", fontsize=10)
fig.tight_layout()
