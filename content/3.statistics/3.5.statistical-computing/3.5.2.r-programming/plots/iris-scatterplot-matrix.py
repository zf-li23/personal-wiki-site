"""Scatterplot matrix of the four iris measurements, colored by species, with sample correlations in the lower panels."""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target
labels = ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width"]
markers = ["o", "^", "+"]

fig, axes = plt.subplots(4, 4, figsize=(8.5, 8.5))
for i in range(4):
    for j in range(4):
        ax = axes[i, j]
        if i == j:
            ax.text(0.5, 0.5, labels[i], ha="center", va="center", fontsize=10, transform=ax.transAxes)
        elif i < j:
            for k in range(3):
                ax.scatter(X[y == k, j], X[y == k, i], s=9, marker=markers[k], color=f"C{k}",
                           facecolors="none" if k < 2 else None, linewidths=0.8)
        else:
            r = np.corrcoef(X[:, i], X[:, j])[0, 1]
            ax.text(0.5, 0.5, f"R = {r:.2f}", ha="center", va="center", fontsize=10, transform=ax.transAxes)
        ax.set_xticks([])
        ax.set_yticks([])
handles = [plt.Line2D([], [], ls="", marker=markers[k], color=f"C{k}", mfc="none", label=iris.target_names[k])
           for k in range(3)]
fig.legend(handles=handles, loc="lower center", ncol=3, fontsize=9, frameon=False)
fig.suptitle("pairs(iris[, 1:4]): species in the upper panels, Pearson correlations in the lower panels", fontsize=10)
fig.tight_layout(rect=(0, 0.04, 1, 0.97))
