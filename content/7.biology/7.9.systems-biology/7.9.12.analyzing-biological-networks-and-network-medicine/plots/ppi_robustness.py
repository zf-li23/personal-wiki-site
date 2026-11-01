"""Robustness of a simulated protein interaction network and of an incomplete map of it. The 'true'
network of 3000 proteins is grown by duplication and divergence: at each step a random protein is
duplicated, the copy keeps each interaction of its parent with probability 0.4 and binds its parent
with probability 0.1 (copies without any interaction are discarded). The 'map' keeps each true
interaction independently with probability 0.4, as a screen of limited sensitivity would.
A: degree distributions (logarithmically binned) of the network and the map. B: size of the
largest connected component, relative to the number of proteins, when a fraction f of the proteins
is removed at random (solid) or in decreasing order of degree (dashed)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
N, q, pp = 3000, 0.4, 0.1
adj = [{1}, {0}]
while len(adj) < N:
    u = int(rng.integers(len(adj)))
    new = {w for w in adj[u] if rng.random() < q}
    if rng.random() < pp:
        new.add(u)
    if not new:
        continue
    v = len(adj)
    adj.append(new)
    for w in new:
        adj[w].add(v)
edges = np.array([(u, w) for u in range(N) for w in adj[u] if u < w])
mask = rng.random(len(edges)) < 0.4
nets = {"network": edges, "map (40% of edges)": edges[mask]}


def lcc_curve(E, order):
    """Largest component after removing order[:r], for all r, by adding vertices in reverse."""
    nbr = [[] for _ in range(N)]
    for a, b in E:
        nbr[a].append(b); nbr[b].append(a)
    parent = np.arange(N); size = np.ones(N, int); present = np.zeros(N, bool)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    best, out = 0, np.zeros(N + 1)
    for r in range(N, 0, -1):
        v = order[r - 1]; present[v] = True
        for w in nbr[v]:
            if present[w]:
                a, b = find(v), find(w)
                if a != b:
                    if size[a] < size[b]:
                        a, b = b, a
                    parent[b] = a; size[a] += size[b]
        best = max(best, size[find(v)])
        out[r - 1] = best
    return out / N


fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.14, top=0.9, wspace=0.3)
cols = {"network": charts.line("dna"), "map (40% of edges)": charts.line("rna")}
stats = {}
for name, E in nets.items():
    deg = np.bincount(E.ravel(), minlength=N)
    stats[name] = (len(E), deg.mean(), deg.max(), (deg == 0).mean())
    k = deg[deg > 0]
    bins = np.unique(np.round(np.logspace(0, np.log10(k.max() + 1), 14)))
    h, e = np.histogram(k, bins)
    mid = np.sqrt(e[1:] * e[:-1])
    ok = h > 0
    a.loglog(mid[ok], (h / np.diff(e) / len(k))[ok], "o-", ms=3.5, color=cols[name], label=name)
    rand = lcc_curve(E, rng.permutation(N))
    attack = lcc_curve(E, np.argsort(-deg, kind="stable"))
    f = np.arange(N + 1) / N
    b.plot(f, rand, color=cols[name], lw=1.3, label=f"{name}, random")
    b.plot(f, attack, color=cols[name], lw=1.3, ls="--", label=f"{name}, by degree")
    stats[name] += (rand[0], f[np.argmax(attack < 0.05)], f[np.argmax(rand < 0.05)])
a.legend(fontsize=7, frameon=False, labelcolor=P.ink())
charts.style_axes(a, "degree k", "p(k)")
charts.title(a, "A  Degree distributions")
b.set_xlim(0, 1); b.set_ylim(0, 1)
b.legend(fontsize=6.5, frameon=False, labelcolor=P.ink())
charts.style_axes(b, "fraction of proteins removed f", "largest component / N")
charts.title(b, "B  Random failure and targeted attack")
