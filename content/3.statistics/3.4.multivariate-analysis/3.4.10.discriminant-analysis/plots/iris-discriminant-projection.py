"""Iris data on the first two sample discriminants versus the first two principal components."""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA

iris = load_iris()
X, y = iris.data, iris.target
names = iris.target_names
markers = ["o", "^", "s"]

Z_lda = LinearDiscriminantAnalysis(n_components=2).fit(X, y).transform(X)
Z_pca = PCA(n_components=2).fit_transform(X)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
for ax, Z, title, labels in [
    (axes[0], Z_lda, "Fisher discriminants", ("first discriminant", "second discriminant")),
    (axes[1], Z_pca, "Principal components", ("PC1", "PC2")),
]:
    for k in range(3):
        ax.scatter(*Z[y == k].T, s=14, marker=markers[k], color=f"C{k}", alpha=0.75, label=names[k])
        ax.scatter(*Z[y == k].mean(axis=0), s=180, marker="X", color=f"C{k}", edgecolor="k", linewidth=1)
    ax.set_title(title)
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.grid(alpha=0.3)
axes[0].legend(fontsize=8, loc="upper center")
fig.tight_layout()
