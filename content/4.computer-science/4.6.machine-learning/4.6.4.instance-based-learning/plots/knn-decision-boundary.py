"""Decision regions of k-nearest-neighbor classification for k = 1, 15 and 75
on the same noisy two-class data, with the 10-fold cross-validated error."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

rng = np.random.default_rng(0)
n = 200
# Two interleaving half-moons with Gaussian noise
theta = rng.uniform(0, np.pi, n)
y = rng.integers(0, 2, n)
X = np.c_[np.cos(theta) + y * 1.0, np.sin(theta) * (1 - 2 * y) + y * 0.4]
X += rng.normal(0, 0.3, X.shape)


def knn_predict(X_train, y_train, X_query, k):
    d2 = ((X_query[:, None, :] - X_train[None, :, :]) ** 2).sum(axis=2)
    nn = np.argpartition(d2, k - 1, axis=1)[:, :k]
    return (y_train[nn].mean(axis=1) > 0.5).astype(int)   # majority vote (k odd)


def cv_error(X, y, k, folds=10):
    idx = rng.permutation(len(y))
    errs = []
    for f in np.array_split(idx, folds):
        train = np.setdiff1d(idx, f)
        errs.append(np.mean(knn_predict(X[train], y[train], X[f], k) != y[f]))
    return np.mean(errs)


gx, gy = np.meshgrid(np.linspace(-1.8, 2.8, 230), np.linspace(-1.4, 1.9, 170))
grid = np.c_[gx.ravel(), gy.ravel()]
region_cmap = ListedColormap(["#9ecae1", "#fdae6b"])
point_colors = np.array(["#1f77b4", "#ff7f0e"])

fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True)
for ax, k in zip(axes, [1, 15, 75]):
    z = knn_predict(X, y, grid, k).reshape(gx.shape)
    ax.contourf(gx, gy, z, levels=[-0.5, 0.5, 1.5], cmap=region_cmap, alpha=0.45)
    ax.contour(gx, gy, z, levels=[0.5], colors="black", linewidths=0.8)
    ax.scatter(X[:, 0], X[:, 1], c=point_colors[y], s=12, edgecolors="none")
    ax.set_title(f"k = {k}   (10-fold CV error {cv_error(X, y, k):.2f})")
    ax.set_xlabel("x1")
axes[0].set_ylabel("x2")
fig.tight_layout()
