# Fiedler vectors of a path, a cycle and two cliques joined by one edge; colour = vector component
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_hex
import wikigraph as G


def laplacian(n, edges):
    L = np.zeros((n, n))
    for u, v in edges:
        L[u, v] -= 1
        L[v, u] -= 1
        L[u, u] += 1
        L[v, v] += 1
    return L


n = 10
path = [(i, i + 1) for i in range(n - 1)]
cycle = path + [(n - 1, 0)]
clique = lambda o: [(o + i, o + j) for i in range(5) for j in range(i + 1, 5)]
barbell = clique(0) + clique(5) + [(4, 5)]

pos_path = {i: (0.25 + 0.5 * i, 1.0) for i in range(n)}
pos_cycle = G.circle(range(n), radius=1.0, center=(2.5, 1.0), start=180)
left = G.circle(range(5), radius=0.75, center=(1.0, 1.0), start=0)
right = G.circle(range(5, 10), radius=0.75, center=(4.0, 1.0), start=180)
pos_bar = {**left, **right}

cases = [("path P10", path, pos_path), ("cycle C10", cycle, pos_cycle), ("two K5 joined by an edge", barbell, pos_bar)]
cmap = LinearSegmentedColormap.from_list("fiedler", [G.BLUE, G.GREY, G.RED])

fig, axes = plt.subplots(2, 3, figsize=(10, 4.6), gridspec_kw={"height_ratios": [1.1, 1]})
for col, (name, edges, pos) in enumerate(cases):
    mu, Q = np.linalg.eigh(laplacian(n, edges))
    x = Q[:, 1]
    if name.startswith("cycle"):
        # the eigenvalue has multiplicity 2; pick the cosine eigenvector cos(2 pi k / n)
        x = np.cos(2 * np.pi * np.arange(n) / n)
        x /= np.linalg.norm(x)
    x = x if x[0] <= 0 else -x
    m = np.abs(x).max()
    colours = {i: to_hex(cmap(0.5 + 0.5 * x[i] / m)) for i in range(n)}
    top = axes[0, col]
    top.set_xlim(-0.2, 5.2)
    top.set_ylim(-0.2, 2.2)
    top.set_aspect("equal")
    top.axis("off")
    top.set_title(f"{name}: a = {mu[1]:.3f}", fontsize=10)
    G.draw(top, pos, edges, labels=True, vertex_labels={i: str(i + 1) for i in range(n)}, vertex_color=colours, radius=0.2)
    bottom = axes[1, col]
    bottom.axhline(0, color="black", lw=0.8)
    bottom.bar(np.arange(1, n + 1), x, color=[colours[i] for i in range(n)])
    bottom.set_xticks(range(1, n + 1))
    bottom.set_xlabel("vertex")
    if col == 0:
        bottom.set_ylabel("Fiedler vector component")
fig.tight_layout()
