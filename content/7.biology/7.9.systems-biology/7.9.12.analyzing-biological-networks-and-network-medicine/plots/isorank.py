"""Global alignment of two small interaction networks (illustrative). Network 2 (right in each panel)
is the network 1 (left) of a related species with one interaction lost and one gained and an extra
protein. Sequence similarity identifies most orthologs, but two pairs of paralogs (a1/a2 and b1/b2)
are equally similar to both candidate orthologs. A: the alignment from sequence similarity alone
(maximum-weight matching), in which the ties between paralogs are broken arbitrarily, here both
wrongly: correct pairs green, wrong pairs red. B: the IsoRank alignment (alpha =
0.6), which adds the similarity of the neighborhoods and resolves the paralogs. Edge correctness EC,
the fraction of the 11 edges of network 1 mapped onto edges of network 2, is given for both; the
edge d-e has no counterpart in network 2, so 10/11 is the maximum."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linear_sum_assignment
import wikigraph as G

rng = np.random.default_rng(0)
V1 = ["a1", "a2", "b1", "b2", "c", "d", "e", "f"]
E1 = [("a1", "c"), ("a1", "d"), ("a2", "e"), ("a2", "f"), ("c", "d"), ("b1", "c"), ("b2", "f"),
      ("b1", "a1"), ("b2", "a2"), ("e", "f"), ("d", "e")]
iso = {v: v + "'" for v in V1}
V2 = [iso[v] for v in V1] + ["g'"]
E2 = [(iso[u], iso[v]) for u, v in E1 if (u, v) != ("d", "e")] + [("a1'", "e'"), ("g'", "f'")]


def adjacency(V, E):
    ix = {v: i for i, v in enumerate(V)}
    A = np.zeros((len(V), len(V)))
    for u, v in E:
        A[ix[u], ix[v]] = A[ix[v], ix[u]] = 1
    return A


A1, A2 = adjacency(V1, E1), adjacency(V2, E2)
S = np.zeros((len(V1), len(V2)))                     # sequence similarity
for i, v in enumerate(V1):
    S[i, V2.index(iso[v])] = 1.0
for p, q in [("a1", "a2"), ("b1", "b2")]:            # paralogs: equally similar to both orthologs
    i, j = V1.index(p), V1.index(q)
    S[i, V2.index(iso[q])] = S[j, V2.index(iso[p])] = 1.0
S += rng.uniform(0, 0.05, S.shape) * (S == 0)
E = S / S.sum()
W1, W2 = A1 / A1.sum(0), A2 / A2.sum(0)
alpha = 0.6
R = E.copy()
for _ in range(200):                                  # power iteration of R = a W1 R W2^T + (1 - a) E
    R = alpha * W1 @ R @ W2.T + (1 - alpha) * E
    R /= R.sum()


def align(M):
    r, c = linear_sum_assignment(-M)
    return {V1[i]: V2[j] for i, j in zip(r, c)}


def ec(f):
    e2 = {frozenset(e) for e in E2}
    return sum(frozenset((f[u], f[v])) in e2 for u, v in E1) / len(E1)


pos1 = {"a1": (0.6, 4.6), "a2": (0.6, 1.6), "b1": (0.0, 5.6), "b2": (0.0, 0.6), "c": (1.6, 5.2),
        "d": (1.8, 3.8), "e": (1.8, 2.2), "f": (1.6, 0.6)}
pos = dict(pos1)
pos.update({iso[v]: (6.8 - x, y) for v, (x, y) in pos1.items()})
pos["g'"] = (6.1, -0.05)
fseq, fiso = align(S + rng.uniform(0, 1e-6, S.shape)), align(R)
fig, axes = G.panels(2, 6.8, 5.8, scale=0.62, titles=[f"A  Sequence only (EC = {ec(fseq):.2f})",
                                                        f"B  IsoRank (EC = {ec(fiso):.2f})"])
for ax, f in zip(axes, [fseq, fiso]):
    for u, v in f.items():
        col = G.GREEN if v == iso[u] else G.RED
        ax.plot(*zip(pos[u], pos[v]), color=col, lw=1.0, ls=":", zorder=1)
    G.draw(ax, pos, E1 + E2, radius=0.3)
