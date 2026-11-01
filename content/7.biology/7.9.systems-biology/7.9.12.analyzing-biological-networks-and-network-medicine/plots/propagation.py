"""Network propagation on a small simulated interaction network (40 proteins grown by preferential
attachment, two edges per new protein). Three seed proteins (thick outline), for example genes
mutated in patients, are the starting points of a random walk with restart (restart probability
r = 0.3). A: the stationary visiting probability p of each protein (Formula 12.4.1), shown on a
logarithmic color scale. B: the same scores as z-scores against 1000 random seed sets of three
proteins with matching degrees. The hub (degree 14, a neighbor of one seed) has the highest score
after the seeds in A (p = 0.082), because many walks pass through it, but a z-score of only 0.52 in
B; after the seeds, the highest z-score (1.04) belongs to a protein of degree 5 adjacent to a seed."""

import numpy as np
import matplotlib.pyplot as plt
import wikigraph as G

rng = np.random.default_rng(0)
n, m = 40, 2
A = np.zeros((n, n))
A[0, 1] = A[1, 0] = A[1, 2] = A[2, 1] = A[0, 2] = A[2, 0] = 1
for v in range(3, n):
    k = A[:v, :v].sum(1)
    for u in rng.choice(v, m, replace=False, p=k / k.sum()):
        A[u, v] = A[v, u] = 1
k = A.sum(1)
W = A / k                                    # column-stochastic: W[i, j] = A[i, j] / k_j
r = 0.3
K = r * np.linalg.inv(np.eye(n) - (1 - r) * W)   # column j: RWR scores from seed j


def rwr(seeds):
    return K[:, seeds].mean(1)


hub = int(np.argmax(k))
leaves = np.where(k <= 3)[0]
seeds = [int(x) for x in rng.choice(leaves, 3, replace=False)]
p = rwr(seeds)
bins = {}
for v in range(n):
    bins.setdefault(int(min(k[v], 6)), []).append(v)
null = np.array([rwr([int(rng.choice(bins[int(min(k[s], 6))])) for s in seeds]) for _ in range(1000)])
z = (p - null.mean(0)) / null.std(0)

# force-directed layout (Fruchterman-Reingold)
X = rng.normal(0, 1, (n, 2))
for it in range(500):
    D = X[:, None, :] - X[None, :, :]
    d = np.sqrt((D**2).sum(-1)) + 1e-9
    F = (D / d[..., None] ** 2).sum(1) * 0.6 - (A[..., None] * D * d[..., None]).sum(1) * 0.25
    step = 0.05 * (1 - it / 500) + 0.005
    X += step * F / (np.linalg.norm(F, axis=1, keepdims=True) + 1e-9)
X = (X - X.min(0)) / (X.max(0) - X.min(0)) * [7.0, 5.6]
names = [str(i) for i in range(n)]
pos = {names[i]: tuple(X[i]) for i in range(n)}
edges = [(names[i], names[j]) for i in range(n) for j in range(i + 1, n) if A[i, j]]
fig, axes = G.panels(2, 7.0, 5.6, scale=0.62, titles=["A  Random walk with restart: log10 p",
                                                         "B  z-score against degree-matched seeds"])
G.draw(axes[0], pos, edges, labels=False, vertex_color=G.colors({names[i]: np.log10(p[i]) for i in range(n)},
       cmap="YlOrRd"), highlight={names[s]: G.BLUE for s in seeds}, radius=0.2)
G.draw(axes[1], pos, edges, labels=False, vertex_color=G.colors({names[i]: z[i] for i in range(n)}, cmap="coolwarm"),
       highlight={names[s]: G.BLUE for s in seeds}, radius=0.2)
for ax in axes:
    x, y = pos[names[hub]]
    ax.text(x, y + 0.42, "hub", ha="center", fontsize=8)
