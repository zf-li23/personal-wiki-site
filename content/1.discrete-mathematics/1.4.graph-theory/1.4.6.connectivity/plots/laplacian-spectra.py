# Laplacian spectra of small graphs: the second smallest eigenvalue a(G) never exceeds kappa(G)
import numpy as np
import matplotlib.pyplot as plt


def laplacian(n, edges):
    L = np.zeros((n, n))
    for u, v in edges:
        L[u, v] -= 1
        L[v, u] -= 1
        L[u, u] += 1
        L[v, v] += 1
    return L


def k4(o):
    return [(o + i, o + j) for i in range(4) for j in range(i + 1, 4)]


path8 = [(i, i + 1) for i in range(7)]
graphs = [
    ("P8", 8, path8, 1),
    ("C8", 8, path8 + [(7, 0)], 2),
    ("star K1,7", 8, [(0, i) for i in range(1, 8)], 1),
    ("two K4 + one edge", 8, k4(0) + k4(4) + [(3, 4)], 1),
    ("two K4 + 2 edges", 8, k4(0) + k4(4) + [(3, 4), (3, 5)], 1),
    ("K3,5", 8, [(i, 3 + j) for i in range(3) for j in range(5)], 3),
    ("Petersen", 10, [(i, (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)]
     + [(5 + i, 5 + (i + 2) % 5) for i in range(5)], 3),
]

fig, ax = plt.subplots(figsize=(7.5, 3.8))
for row, (name, n, edges, kappa) in enumerate(graphs):
    mu = np.linalg.eigvalsh(laplacian(n, edges))
    y = len(graphs) - 1 - row
    ax.scatter(mu, np.full(n, y), s=28, color="#94a3b8", zorder=2)
    ax.scatter([mu[1]], [y], s=46, color="#dc2626", zorder=3, label="$a(G)$" if row == 0 else None)
    ax.scatter([kappa], [y], marker="|", s=420, color="#2563eb", zorder=4, label=r"$\kappa(G)$" if row == 0 else None)
ax.set_yticks(range(len(graphs)))
ax.set_yticklabels([g[0] for g in reversed(graphs)])
ax.set_xlabel("Laplacian eigenvalue")
ax.set_xlim(-0.3, 8.6)
ax.grid(axis="x", alpha=0.3)
ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, frameon=False)
fig.tight_layout()
