# UPGMA and neighbor joining on additive distances from a tree without a molecular clock. A: the true tree,
# in which taxon B evolves five times faster than its sister A; its path-length distances (table) are the
# input of both methods. B: UPGMA assumes equal rates (an ultrametric tree): it joins D with E, A with the
# slowly evolving C, and these two clusters before B, so the clade (A, B) is lost. C: neighbor joining
# corrects each distance by the total divergence of the two taxa and recovers the true unrooted tree with its
# branch lengths (drawn rooted on the branch between the (A, B, C) and (D, E) groups, as in A). All trees are drawn on the same scale.
import numpy as np
import wikibio as bio
from wikibio import phylo

P = bio.P
TRUE = "(((A:1,B:5):1,C:2):1,(D:1,E:2):1);"
names = list("ABCDE")
D0 = np.array([[0, 6, 4, 5, 6],
               [6, 0, 8, 9, 10],
               [4, 8, 0, 5, 6],
               [5, 9, 5, 0, 3],
               [6, 10, 6, 3, 0]], float)


def upgma(D, names):
    cl = [(n, 1, 0.0) for n in names]
    D = D.copy()
    while len(cl) > 1:
        m = len(cl)
        i, j = min(((a, b) for a in range(m) for b in range(a + 1, m)), key=lambda p: D[p])
        h = D[i, j] / 2
        (ni, si, hi), (nj, sj, hj) = cl[i], cl[j]
        new = (f"({ni}:{h - hi:g},{nj}:{h - hj:g})", si + sj, h)
        row = (si * D[i] + sj * D[j]) / (si + sj)
        keep = [k for k in range(m) if k not in (i, j)]
        D2 = np.zeros((len(keep) + 1,) * 2)
        D2[:-1, :-1] = D[np.ix_(keep, keep)]
        D2[-1, :-1] = D2[:-1, -1] = row[keep]
        cl = [cl[k] for k in keep] + [new]
        D = D2
    return cl[0][0] + ";"


def nj(D, names):
    nodes = list(names)
    D = D.copy()
    joins = []
    while len(nodes) > 3:
        n = len(nodes)
        R = D.sum(1)
        Q = (n - 2) * D - R[:, None] - R[None, :]
        np.fill_diagonal(Q, np.inf)
        i, j = sorted(np.unravel_index(np.argmin(Q), Q.shape))
        bi = 0.5 * D[i, j] + (R[i] - R[j]) / (2 * (n - 2))
        new = f"({nodes[i]}:{bi:g},{nodes[j]}:{D[i, j] - bi:g})"
        row = 0.5 * (D[i] + D[j] - D[i, j])
        keep = [k for k in range(n) if k not in (i, j)]
        D2 = np.zeros((n - 1, n - 1))
        D2[:-1, :-1] = D[np.ix_(keep, keep)]
        D2[-1, :-1] = D2[:-1, -1] = row[keep]
        nodes = [nodes[k] for k in keep] + [new]
        D = D2
    return nodes, D


up = upgma(D0, names)
nodes, D3 = nj(D0, names)
# three remaining nodes: C, (D,E) and (A,B) in some order; resolve as ((AB, C), DE) with the root on the
# branch to (D, E), splitting that branch in the same proportions as the true tree
la = (D3[0, 1] + D3[0, 2] - D3[1, 2]) / 2
lb, lc = D3[0, 1] - la, D3[0, 2] - la
lens = dict(zip(nodes, (la, lb, lc)))
de = next(k for k in nodes if "D:" in k)
ab = next(k for k in nodes if "A:" in k)
c = next(k for k in nodes if k not in (de, ab))
njtree = f"(({ab}:{lens[ab]:g},{c}:{lens[c]:g}):{lens[de] / 2:g},{de}:{lens[de] / 2:g});"

fig, ax = bio.canvas(27.0, 10.5)
for k, (nw, title, scaled) in enumerate([(TRUE, "True tree (no clock)", True),
                                         (up, "UPGMA", True), (njtree, "Neighbor joining", True)]):
    x0 = 0.8 + 9.0 * k
    phylo.tree(ax, nw, origin=(x0, 3.6), width=6.0, height=5.2, scaled=scaled, span=7.0, label_size="normal")
    bio.label(ax, (x0 + 3.2, 9.6), title, size="normal", bold=True)
    bio.panel(ax, "ABC"[k], (x0 - 0.6, 10.1))
# distance table under panel A
cw, rh = 0.62, 0.42
tx, ty = 1.2, 2.6
for j, nm in enumerate(names):
    bio.label(ax, (tx + (j + 1) * cw, ty), nm, size="small", bold=True)
    bio.label(ax, (tx, ty - (j + 1) * rh), nm, size="small", bold=True)
    for i in range(len(names)):
        if i > j:
            bio.label(ax, (tx + (j + 1) * cw, ty - (i + 1) * rh), f"{D0[i, j]:g}", size="small")
bio.label(ax, (tx + 3.6, ty - 1.0), "path-length\ndistances", size="small", color=P.muted(), ha="left")
