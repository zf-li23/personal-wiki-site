"""Three realizations of the random graph G(N, p) with N = 60 vertices and mean degree c = p(N - 1)
equal to 0.5, 1 and 3; the largest connected component is drawn in red."""

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
import wikigraph as G

N = 60
W, H = 4.0, 4.0


def gnp(n, p, rng):
    iu, ju = np.triu_indices(n, 1)
    keep = rng.random(iu.size) < p
    return list(zip(iu[keep].tolist(), ju[keep].tolist()))


def layout(n, edges, rng, steps=400):
    """Fruchterman-Reingold force-directed layout with a weak pull towards the centre."""
    x = rng.random((n, 2)) - 0.5
    k = 1.0 / np.sqrt(n)
    e = np.array(edges, dtype=int).reshape(-1, 2)
    temp = 0.1
    for _ in range(steps):
        d = x[:, None, :] - x[None, :, :]
        dist = np.linalg.norm(d, axis=2) + 1e-9
        disp = (d * (k * k / dist ** 2)[:, :, None]).sum(1)
        if len(e):
            de = x[e[:, 0]] - x[e[:, 1]]
            le = np.linalg.norm(de, axis=1)[:, None] + 1e-9
            f = de * le / k
            np.add.at(disp, e[:, 0], -f)
            np.add.at(disp, e[:, 1], f)
        disp -= 0.6 * x / k  # gravity keeps isolated vertices and small trees on the canvas
        length = np.linalg.norm(disp, axis=1)[:, None] + 1e-9
        x += disp / length * np.minimum(length, temp)
        temp = max(temp * 0.99, 0.002)
    x -= x.min(0)
    x /= x.max(0)
    return x


rng = np.random.default_rng(3)
titles, graphs = [], []
for c in (0.5, 1.0, 3.0):
    edges = gnp(N, c / (N - 1), rng)
    m = coo_matrix((np.ones(len(edges)), tuple(np.array(edges).T)), shape=(N, N)) if edges else coo_matrix((N, N))
    _, lab = connected_components(m, directed=False)
    big = np.bincount(lab).argmax()
    giant = {v for v in range(N) if lab[v] == big}
    graphs.append((edges, giant))
    titles.append(rf"$c = {c:g}$: largest component {len(giant)} of {N}")

fig, axes = G.panels(3, W, H, scale=0.8, titles=titles)
for ax, (edges, giant) in zip(axes, graphs):
    x = layout(N, edges, rng)
    pos = {v: (W * x[v, 0], H * x[v, 1]) for v in range(N)}
    hl = {v: G.RED for v in giant}
    hl.update({(u, v): G.RED for u, v in edges if u in giant})
    G.draw(ax, pos, edges, labels=False, radius=0.07, width=0.9, highlight=hl,
           vertex_color={v: G.RED for v in giant})
