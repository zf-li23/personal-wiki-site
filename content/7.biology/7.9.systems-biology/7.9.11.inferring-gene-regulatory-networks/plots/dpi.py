"""The data processing inequality removes indirect edges (simulation). A: a regulatory network of eight
genes, with a feed-forward loop A -> B -> G, A -> G. Expression of the genes in n = 300 samples is
simulated from a linear Gaussian model in which each gene is the weighted sum of its regulators plus
noise. B: the mutual-information network: all pairs whose Gaussian mutual information exceeds the
threshold I0 (the largest value among 2000 permuted pairs): 26 edges, of which the 18 in red join
genes that are not directly connected. C: after ARACNe's pruning step (Algorithm
11.4.1, tolerance 0), which removes the weakest edge of every triangle: all 18 indirect edges are gone,
but so is the true edge A -> G of the feed-forward loop (grey, dashed), the weakest of its triangle."""

import itertools
import numpy as np
import matplotlib.pyplot as plt
import wikigraph as G

rng = np.random.default_rng(0)
genes = list("ABCDEFGH")
true = {("A", "B"): 0.9, ("A", "C"): 0.8, ("B", "D"): 0.85, ("C", "E"): 0.8, ("D", "F"): 0.8,
        ("B", "G"): 0.7, ("A", "G"): 0.35, ("E", "H"): 0.75}
idx = {g: i for i, g in enumerate(genes)}
n = 300
X = np.zeros((n, len(genes)))
for g in genes:                                  # genes are listed in a topological order
    X[:, idx[g]] = rng.normal(0, 0.6, n)
    for (u, v), w in true.items():
        if v == g:
            X[:, idx[g]] += w * X[:, idx[u]]
R = np.corrcoef(X.T)
np.fill_diagonal(R, 0)
MI = -0.5 * np.log(1 - R**2)
null = []
for _ in range(2000):
    i, j = rng.choice(len(genes), 2, replace=False)
    null.append(-0.5 * np.log(1 - np.corrcoef(X[:, i], rng.permutation(X[:, j]))[0, 1] ** 2))
I0 = max(null)
edges = {(genes[i], genes[j]) for i, j in itertools.combinations(range(len(genes)), 2) if MI[i, j] > I0}
und_true = {tuple(sorted(e)) for e in true}
removed = set()
for a, b, c in itertools.combinations(genes, 3):
    tri = [tuple(sorted(p)) for p in ((a, b), (a, c), (b, c))]
    if all(t in edges for t in tri):
        removed.add(min(tri, key=lambda t: MI[idx[t[0]], idx[t[1]]]))
kept = edges - removed

pos = {"A": (2.0, 3.0), "B": (1.0, 2.0), "C": (3.0, 2.0), "D": (0.4, 1.0), "G": (1.6, 1.0),
       "E": (3.4, 1.0), "F": (0.4, 0.0), "H": (3.4, 0.0)}
fig, axes = G.panels(3, 3.8, 3.0, titles=["A  True network", "B  Mutual information > I0",
                                            "C  After the DPI pruning"])
G.draw(axes[0], pos, list(true), directed=True)
G.draw(axes[1], pos, sorted(edges), highlight={e: G.RED for e in edges if e not in und_true})
shown = sorted(kept) + sorted(e for e in removed if e in und_true)
G.draw(axes[2], pos, shown, highlight={**{e: G.RED for e in kept if e not in und_true},
                                     **{e: G.GREY for e in removed if e in und_true}},
       dashed=[e for e in removed if e in und_true])
