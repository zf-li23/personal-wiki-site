"""Modules of a small simulated interaction network. Four complexes of 8, 7, 6 and 5 proteins (each
pair within a complex interacts with probability 0.7), linked by a few interactions between
complexes, and four peripheral proteins. A: communities found by recursive spectral bisection of
the modularity matrix (leading-eigenvector method), each colored; the modularity Q of the partition
is given. B: the same network with vertex size proportional to degree and color by betweenness
centrality (dark: high). Two proteins share the highest degree, 7: the one labeled 'highest
degree' lies inside its complex (normalized betweenness 0.06), while the one with the highest
betweenness (0.41) joins its complex to two others."""

import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import wikigraph as G

rng = np.random.default_rng(0)
sizes = [8, 7, 6, 5]
names, comp = [], []
for c, s in enumerate(sizes):
    for i in range(s):
        names.append(f"{'ABCD'[c]}{i + 1}"); comp.append(c)
names += ["P1", "P2", "P3", "P4"]; comp += [-1] * 4
n = len(names)
A = np.zeros((n, n), int)
start = np.cumsum([0] + sizes)
for c in range(4):
    for i in range(start[c], start[c + 1]):
        for j in range(i + 1, start[c + 1]):
            if rng.random() < 0.7:
                A[i, j] = A[j, i] = 1
for i, j in [(0, 8), (8, 16), (2, 18), (16, 23), (12, 21)]:     # links between complexes
    A[i, j] = A[j, i] = 1
for p, t in zip(range(26, 30), [1, 9, 17, 22]):                  # peripheral proteins
    A[p, t] = A[t, p] = 1
k = A.sum(1); M = k.sum() / 2


def modularity(groups):
    B = A - np.outer(k, k) / (2 * M)
    return sum(B[np.ix_(g, g)].sum() for g in groups) / (2 * M)


def bisect(g):
    B = A - np.outer(k, k) / (2 * M)
    Bg = B[np.ix_(g, g)] - np.diag(B[np.ix_(g, g)].sum(1))
    w, V = np.linalg.eigh(Bg)
    if w[-1] < 1e-9:
        return [g]
    s = V[:, -1] >= 0
    g1, g2 = [g[i] for i in range(len(g)) if s[i]], [g[i] for i in range(len(g)) if not s[i]]
    if not g1 or not g2 or (np.outer(s * 2 - 1, s * 2 - 1) * Bg).sum() <= 1e-9:
        return [g]
    return bisect(g1) + bisect(g2)


groups = bisect(list(range(n)))
Q = modularity(groups)
Qtrue = modularity([list(range(start[c], start[c + 1])) for c in range(4)])
# betweenness centrality (Brandes)
bet = np.zeros(n)
for s in range(n):
    S, Pd, sig, d = [], [[] for _ in range(n)], np.zeros(n), -np.ones(n)
    sig[s], d[s] = 1, 0
    dq = deque([s])
    while dq:
        v = dq.popleft(); S.append(v)
        for w in np.nonzero(A[v])[0]:
            if d[w] < 0:
                d[w] = d[v] + 1; dq.append(w)
            if d[w] == d[v] + 1:
                sig[w] += sig[v]; Pd[w].append(v)
    delta = np.zeros(n)
    while S:
        w = S.pop()
        for v in Pd[w]:
            delta[v] += sig[v] / sig[w] * (1 + delta[w])
        if w != s:
            bet[w] += delta[w]
bet /= 2 * ((n - 1) * (n - 2) / 2)
hub, bridge = names[int(np.argmax(k))], names[int(np.argmax(bet))]

centers = [(1.6, 4.2), (5.6, 4.2), (1.8, 1.0), (5.4, 1.0)]
pos = {}
for c in range(4):
    sub = G.circle(names[start[c]:start[c + 1]], radius=1.0, center=centers[c])
    pos.update(sub)
for p, t in zip(range(26, 30), [1, 9, 17, 22]):
    x, y = pos[names[t]]
    cx, cy = centers[comp[t]]
    pos[names[p]] = (x + 0.9 * (x - cx), y + 0.9 * (y - cy))
edges = [(names[i], names[j]) for i in range(n) for j in range(i + 1, n) if A[i, j]]
palette = [G.BLUE, G.RED, G.GREEN, G.AMBER, G.VIOLET, G.GREY]
vc = {names[v]: palette[gi % len(palette)] for gi, g in enumerate(groups) for v in g}
fig, axes = G.panels(2, 7.4, 6.0, scale=0.62, titles=[f"A  Communities (Q = {Q:.2f})",
                                                         "B  Degree (size) and betweenness (color)"])
G.draw(axes[0], pos, edges, vertex_color=vc, labels=False)
bc = G.colors({names[i]: bet[i] for i in range(n)}, cmap="Blues", vmin=0, vmax=bet.max())
G.draw(axes[1], pos, edges, vertex_color=bc, labels=False, vertices=False)
from matplotlib.patches import Circle
for i in range(n):
    r = 0.1 + 0.03 * k[i]
    axes[1].add_patch(Circle(pos[names[i]], r, facecolor=bc[names[i]], edgecolor="black", lw=0.8, zorder=3))
for name, lab, dx, dy, ha in [(hub, "highest\ndegree", -0.45, 0.0, "right"),
                              (bridge, "highest betweenness", 0.0, 0.6, "center")]:
    x, y = pos[name]
    axes[1].text(x + dx, y + dy, lab, ha=ha, va="center", fontsize=8)
