"""Clustering cells by community detection on a nearest-neighbor graph (simulated data). 600 cells of five
types (200, 150, 110, 90 and 50 cells) with negative binomial counts for 400 genes; type 5 differs from type
4 in only 16 genes. Counts were normalized (shifted log), scaled, reduced to 15 principal components, and
each cell was joined to its 15 nearest neighbors (the union of the directed kNN relations gives about 7100
edges). A: the graph in a force-directed layout, cells colored by their true type. B: the communities
found by the Louvain algorithm maximizing modularity with resolution 1, which recover the five types. C:
the number of communities and the agreement with the true types (adjusted Rand index) as the resolution
parameter gamma of the modularity varies: small gamma merges the subtype with its parent, large gamma
splits the largest type."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import wikibio as bio
from wikibio import charts
import wikigraph as G

P = bio.P
rng = np.random.default_rng(0)

def simulate():
    sizes = [200, 150, 110, 90, 50]
    G = 400
    base = rng.normal(-1.0, 1.2, G)
    prof = np.tile(base, (5, 1))
    for t in range(4):
        idx = rng.choice(G, 25, replace=False)
        prof[t, idx] += rng.uniform(1.5, 3.0, 25)
    # type 4 is a subtype of type 3: copy of 3 with 8 genes changed
    prof[4] = prof[3].copy()
    idx = rng.choice(G, 16, replace=False)
    prof[4, idx] += rng.uniform(1.2, 2.2, 16)
    labels = np.repeat(np.arange(5), sizes)
    lib = rng.lognormal(0, 0.35, len(labels))
    mu = np.exp(prof[labels]) * lib[:, None]
    th = 5.0
    X = rng.negative_binomial(th, th / (th + mu))
    return X, labels

def embed(X, npc=15, k=15):
    tot = X.sum(1, keepdims=True)
    Y = np.log1p(X / tot * np.median(tot))
    Y = (Y - Y.mean(0)) / (Y.std(0) + 1e-9)
    Y = np.clip(Y, -10, 10)
    U, s, Vt = np.linalg.svd(Y, full_matrices=False)
    Z = U[:, :npc] * s[:npc]
    D = ((Z[:, None, :] - Z[None, :, :]) ** 2).sum(-1)
    np.fill_diagonal(D, np.inf)
    nn = np.argsort(D, 1)[:, :k]
    A = np.zeros((len(Z), len(Z)))
    A[np.repeat(np.arange(len(Z)), k), nn.ravel()] = 1
    A = np.maximum(A, A.T)
    return Z, A, s

def modularity(A, c, gamma=1.0):
    k = A.sum(1); m2 = k.sum()
    Q = 0.0
    for g in np.unique(c):
        s = c == g
        Q += A[np.ix_(s, s)].sum() / m2 - gamma * (k[s].sum() / m2) ** 2
    return Q

def louvain(A, gamma=1.0, seed=0):
    r = np.random.default_rng(seed)
    n0 = len(A)
    member = np.arange(n0)
    W = A.copy()
    while True:
        n = len(W)
        k = W.sum(1); m2 = k.sum()
        comm = np.arange(n)
        tot = k.copy()
        improved = False
        moved = True
        while moved:
            moved = False
            for i in r.permutation(n):
                ci = comm[i]
                tot[ci] -= k[i]
                w = W[i].copy(); w[i] = 0
                cw = np.bincount(comm, weights=w, minlength=n)
                gain = cw - gamma * tot * k[i] / m2
                best = ci
                bg = gain[ci]
                cand = np.nonzero(cw > 0)[0]
                for c in cand:
                    if gain[c] > bg + 1e-12:
                        bg, best = gain[c], c
                comm[i] = best
                tot[best] += k[i]
                if best != ci:
                    moved = True; improved = True
        if not improved:
            break
        _, comm = np.unique(comm, return_inverse=True)
        member = comm[member]
        nc = comm.max() + 1
        P = np.zeros((n, nc)); P[np.arange(n), comm] = 1
        W = P.T @ W @ P
    _, member = np.unique(member, return_inverse=True)
    return member

def ari(a, b):
    from math import comb
    ct = np.zeros((a.max()+1, b.max()+1))
    np.add.at(ct, (a, b), 1)
    s = sum(comb(int(x), 2) for x in ct.ravel())
    sa = sum(comb(int(x), 2) for x in ct.sum(1)); sb = sum(comb(int(x), 2) for x in ct.sum(0))
    n = comb(len(a), 2); e = sa*sb/n
    return (s - e)/((sa+sb)/2 - e)



def layout(A, Z, iters=250):
    r = np.random.default_rng(1)
    n = len(A)
    pos = Z[:, :2] / np.abs(Z[:, :2]).max() + 0.01 * r.standard_normal((n, 2))
    k = 4.0 / np.sqrt(n)
    t = 0.1
    for _ in range(iters):
        d = pos[:, None, :] - pos[None, :, :]
        dist = np.sqrt((d ** 2).sum(-1)) + 1e-6
        rep = (k * k / dist ** 2)[:, :, None] * d
        att = -(A * dist / k)[:, :, None] * d
        disp = (rep + att).sum(1)
        ln = np.sqrt((disp ** 2).sum(1)) + 1e-9
        pos += disp / ln[:, None] * np.minimum(ln, t)[:, None]
        t *= 0.985
    return pos


X, lab = simulate()
Z, A, s = embed(X)
pos = layout(A, Z)
cols = G.ACCENTS
c1 = louvain(A, 1.0)
gammas = [0.1, 0.2, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 2.5, 3.0]
res = [(g, louvain(A, g)) for g in gammas]
fig, axs = plt.subplots(1, 3, figsize=(12.4, 4.0), gridspec_kw={"width_ratios": [1, 1, 1.1]})
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.15, top=0.9, wspace=0.12)
iu = np.argwhere(np.triu(A, 1) > 0)
for ax, c, ttl in [(axs[0], lab, "A  kNN graph, true cell types"), (axs[1], c1, "B  Louvain communities, gamma = 1")]:
    ax.add_collection(LineCollection(pos[iu], colors=P.fill("neutral"), linewidths=0.25, zorder=1))
    # match community colors to the true type that dominates each community
    if c is lab:
        cc = [cols[x % 5] for x in c]
    else:
        dom = {g: np.bincount(lab[c == g]).argmax() for g in np.unique(c)}
        cc = [cols[dom[x] % 5] for x in c]
    ax.scatter(pos[:, 0], pos[:, 1], s=7, c=cc, lw=0, zorder=2)
    ax.set_aspect("equal"); ax.axis("off")
    charts.title(ax, ttl)
ax = axs[2]
ncl = [r.max() + 1 for _, r in res]
ar = [ari(lab, r) for _, r in res]
ax.plot(gammas, ncl, "o-", color=charts.line("dna"), ms=4, lw=1.4, label="number of communities")
ax.axhline(5, color=P.muted(), lw=0.6, ls=":")
ax2 = ax.twinx()
ax2.plot(gammas, ar, "s--", color=charts.line("rna"), ms=4, lw=1.2, label="adjusted Rand index")
ax2.set_ylim(0, 1.05)
charts.style_axes(ax2, None, "adjusted Rand index")
ax2.spines["right"].set_visible(True)
charts.style_axes(ax, "resolution gamma", "number of communities")
ax.set_ylim(0, 14)
h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, frameon=False, fontsize=7.5, loc="lower right")
charts.title(ax, "C  The resolution parameter")
print("edges", A.sum() / 2, [(g, n, round(a, 3)) for g, n, a in zip(gammas, ncl, ar)])
