"""A network of 30 vertices drawn from a planted three-group model (edge probability 0.45 inside a
group, 0.03 between groups), with the communities found by the Louvain algorithm (colours) and the
modularity Q of that partition and of the planted one."""

import numpy as np
import wikigraph as G

rng = np.random.default_rng(11)
n, groups = 30, 3
planted = np.repeat(np.arange(groups), n // groups)
A = np.zeros((n, n))
for i in range(n):
    for j in range(i + 1, n):
        if rng.random() < (0.45 if planted[i] == planted[j] else 0.03):
            A[i, j] = A[j, i] = 1


def modularity(W, labels):
    two_m = W.sum()
    k = W.sum(1)
    same = labels[:, None] == labels[None, :]
    return ((W - np.outer(k, k) / two_m) * same).sum() / two_m


def local_moves(W):
    """Phase 1 of Louvain: move single vertices to the neighbouring community with the largest gain."""
    size = len(W)
    comm = np.arange(size)
    k = W.sum(1)
    two_m = W.sum()
    tot = k.copy()
    improved = True
    while improved:
        improved = False
        for i in rng.permutation(size):
            tot[comm[i]] -= k[i]
            links = np.bincount(comm, weights=W[i], minlength=size)
            links[comm[i]] -= W[i, i]  # a self-loop is not a link to the rest of the community
            cands = np.unique(comm[W[i] > 0])
            best, gain = comm[i], links[comm[i]] - tot[comm[i]] * k[i] / two_m
            for c in cands:
                g = links[c] - tot[c] * k[i] / two_m
                if g > gain + 1e-12:
                    best, gain = c, g
            if best != comm[i]:
                improved = True
            comm[i] = best
            tot[best] += k[i]
    return np.unique(comm, return_inverse=True)[1]


def louvain(W):
    labels = np.arange(len(W))
    while True:
        c = local_moves(W)
        if c.max() + 1 == len(W):
            return labels
        labels = c[labels]
        P = np.zeros((len(W), c.max() + 1))
        P[np.arange(len(W)), c] = 1
        W = P.T @ W @ P  # aggregate: communities become vertices, internal edges become self-loops


found = louvain(A)
q_found, q_planted = modularity(A, found), modularity(A, planted)


def layout(adj, steps=500):
    x = rng.random((n, 2)) - 0.5
    kk = 1.0 / np.sqrt(n)
    temp = 0.1
    for _ in range(steps):
        d = x[:, None, :] - x[None, :, :]
        dist = np.linalg.norm(d, axis=2) + 1e-9
        disp = (d * (kk * kk / dist ** 2)[:, :, None]).sum(1)
        disp -= (d * (adj * dist / kk)[:, :, None]).sum(1)
        disp -= 0.3 * x / kk
        length = np.linalg.norm(disp, axis=1)[:, None] + 1e-9
        x += disp / length * np.minimum(length, temp)
        temp = max(temp * 0.99, 0.002)
    x -= x.min(0)
    return x / x.max(0)


x = layout(A)
W, H = 5.0, 4.0
pos = {i: (W * x[i, 0], H * x[i, 1]) for i in range(n)}
edges = [(i, j) for i in range(n) for j in range(i + 1, n) if A[i, j]]
cols = [G.BLUE, G.RED, G.GREEN, G.AMBER, G.VIOLET]
fig, ax = G.canvas(W, H + 0.5)
G.draw(ax, pos, edges, labels=False, radius=0.13, width=1.0,
       vertex_color={i: cols[found[i] % len(cols)] for i in range(n)},
       highlight={(i, j): G.GREY for i, j in edges if found[i] != found[j]})
G.caption(ax, (W / 2, H + 0.4), f"Louvain: {found.max() + 1} communities, Q = {q_found:.3f} (planted partition: Q = {q_planted:.3f})")
