"""k-means versus DBSCAN on two interleaving half-moons with background noise."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
t = rng.uniform(0, np.pi, 200)
upper = np.c_[np.cos(t), np.sin(t)]
lower = np.c_[1 - np.cos(t), 0.5 - np.sin(t)]
X = np.vstack([upper, lower]) + rng.normal(0, 0.06, (400, 2))
X = np.vstack([X, rng.uniform([-1.5, -1.0], [2.5, 1.5], (20, 2))])  # noise

# k-means with k = 2
c = X[[0, 250]]
for _ in range(100):
    km = ((X[:, None, :] - c) ** 2).sum(axis=2).argmin(axis=1)
    c = np.array([X[km == j].mean(axis=0) for j in range(2)])


def dbscan(X, eps, min_pts):
    """Plain DBSCAN; label -1 marks noise."""
    D = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(axis=2))
    neigh = [np.flatnonzero(row <= eps) for row in D]
    core = np.array([len(nb) >= min_pts for nb in neigh])
    lab = np.full(len(X), -1)
    cid = 0
    for i in range(len(X)):
        if lab[i] != -1 or not core[i]:
            continue
        lab[i] = cid
        stack = [i]
        while stack:
            p = stack.pop()
            if not core[p]:
                continue
            for q in neigh[p]:
                if lab[q] == -1:
                    lab[q] = cid
                    stack.append(q)
        cid += 1
    return lab, core


db, core = dbscan(X, eps=0.2, min_pts=5)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
axes[0].scatter(X[:, 0], X[:, 1], c=km, cmap="coolwarm", s=10)
axes[0].scatter(c[:, 0], c[:, 1], marker="x", s=120, color="k")
axes[0].set_title("k-means, k = 2")
for j in range(db.max() + 1):
    m = db == j
    axes[1].scatter(X[m & core, 0], X[m & core, 1], s=12, color=f"C{j}", label=f"cluster {j + 1} (core)")
    axes[1].scatter(X[m & ~core, 0], X[m & ~core, 1], s=12, facecolors="none", edgecolors=f"C{j}",
                    label=f"cluster {j + 1} (border)")
axes[1].scatter(X[db == -1, 0], X[db == -1, 1], marker="x", s=20, color="gray", label="noise")
axes[1].set_title("DBSCAN, eps = 0.2, minPts = 5")
axes[1].legend(fontsize=8, loc="upper right")
for ax in axes:
    ax.set_aspect("equal")
fig.tight_layout()
