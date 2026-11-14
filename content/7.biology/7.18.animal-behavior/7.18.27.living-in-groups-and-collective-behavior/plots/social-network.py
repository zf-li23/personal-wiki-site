"""Social network analysis of simulated association data.

Thirty individuals belong to three communities that usually forage together; in each of 200 sampling periods
every community splits at random into three subgroups and each individual joins a subgroup of another community
with probability 0.03, except three wide-ranging individuals that spend half of the periods with one particular
other community ("gambit of the group": individuals seen in
the same subgroup are associated).
A: the association network. The edge weight is the simple ratio index (periods together / periods observed);
edges with index > 0.08 are kept, thicker for stronger associations. Node size shows degree; the three nodes with
the highest betweenness centrality (the share of shortest paths between other pairs that pass through them) are
outlined. B: network-based diffusion of an innovation: each day a naive individual learns with probability
1 - exp(-0.3 x sum of its edge weights to informed individuals). Mean proportion informed (200 runs)
when the demonstrator is the individual with the highest betweenness or the one with the lowest degree.
"""

from collections import deque

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(11)
n, C, T = 30, 3, 200
comm = np.repeat(np.arange(C), n // C)
together = np.zeros((n, n))
roam = np.full(n, 0.03)
bridge = {4: 1, 13: 2, 25: 0}  # wide-ranging individuals and the community they often visit
for i in bridge:
    roam[i] = 0.5
for _ in range(T):
    sub = comm * 3 + rng.integers(0, 3, n)
    move = rng.random(n) < roam
    other = (comm + rng.integers(1, C, n)) % C
    for i, c in bridge.items():
        other[i] = c
    sub = np.where(move, other * 3 + rng.integers(0, 3, n), sub)
    together += sub[:, None] == sub[None, :]
W = together / T
np.fill_diagonal(W, 0)
A = W > 0.08
W = W * A
deg = A.sum(1)


def betweenness(adj):
    m = len(adj)
    bc = np.zeros(m)
    for s in range(m):
        stack, pred = [], [[] for _ in range(m)]
        sigma, dist = np.zeros(m), -np.ones(m)
        sigma[s], dist[s] = 1, 0
        q = deque([s])
        while q:
            v = q.popleft()
            stack.append(v)
            for w in np.flatnonzero(adj[v]):
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    q.append(w)
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    pred[w].append(v)
        delta = np.zeros(m)
        while stack:
            w = stack.pop()
            for v in pred[w]:
                delta[v] += sigma[v] / sigma[w] * (1 + delta[w])
            if w != s:
                bc[w] += delta[w]
    return bc / 2


bc = betweenness(A)

# force-directed layout (Fruchterman-Reingold)
pos = rng.normal(0, 1, (n, 2)) + np.c_[np.cos(comm * 2.1), np.sin(comm * 2.1)] * 2
k = 1.1
for it in range(400):
    d = pos[:, None, :] - pos[None, :, :]
    r = np.maximum(np.hypot(d[..., 0], d[..., 1]), 1e-3)
    f = (k * k / r ** 2)[..., None] * d - (A * r / k)[..., None] * d
    disp = f.sum(1) - 0.3 * pos
    step = 0.1 * (1 - it / 400) + 0.005
    ln = np.maximum(np.hypot(disp[:, 0], disp[:, 1]), 1e-9)[:, None]
    pos += disp / ln * np.minimum(ln, step)

fig, ax = bio.canvas(30.0, 11.0)
pa = Ch.axes_at(ax, (0.8, 0.8, 12.5, 9.6))
toks = ["dna", "rna", "protein"]
for i in range(n):
    for j in range(i + 1, n):
        if A[i, j]:
            pa.plot(*pos[[i, j]].T, color=P.muted(), lw=0.3 + 4.0 * (W[i, j] - 0.08), zorder=1, solid_capstyle="round")
top = set(np.argsort(bc)[-3:])
for i in range(n):
    pa.scatter(*pos[i], s=12 + 9 * deg[i], color=P.fill(toks[comm[i]]), edgecolor=P.ink() if i in top else
               P.edge(toks[comm[i]]), lw=1.8 if i in top else 0.6, zorder=3)
pa.set_aspect("equal")
pa.axis("off")
bio.label(ax, (7.0, 0.5), "node size: degree;  outlined: highest betweenness", size="tiny", color=P.muted())
bio.panel(ax, "A", (0.2, 10.8))

pb = Ch.axes_at(ax, (17.8, 1.8, 11.2, 7.8))
days = 40
for start, tok, name in ((int(np.argmax(bc)), "rna", "demonstrator: highest betweenness"),
                         (int(np.argmin(deg + bc * 1e-3)), "dna", "demonstrator: lowest degree")):
    curves = np.zeros(days + 1)
    for _ in range(200):
        inf = np.zeros(n, bool)
        inf[start] = True
        c = [inf.mean()]
        for _ in range(days):
            pr = 1 - np.exp(-0.3 * (W * inf[None, :]).sum(1))
            inf = inf | (rng.random(n) < pr)
            c.append(inf.mean())
        curves += np.array(c) / 200
    pb.plot(range(days + 1), curves, color=Ch.line(tok), lw=1.7)
    pb.text(12.5, curves[12], name, fontsize=FS["tiny"], color=Ch.line(tok), va="center", ha="left")
pb.set_xlim(0, days)
pb.set_ylim(0, 1.02)
Ch.style_axes(pb, "days", "proportion that has learned")
bio.panel(ax, "B", (15.8, 10.8))
