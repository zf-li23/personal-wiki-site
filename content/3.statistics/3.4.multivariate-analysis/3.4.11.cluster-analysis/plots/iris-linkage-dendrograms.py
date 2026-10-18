"""Dendrograms of the iris data under single, complete, average and Ward linkage."""

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.datasets import load_iris

X = load_iris().data
fig, axes = plt.subplots(2, 2, figsize=(12, 7))
for ax, method in zip(axes.ravel(), ["single", "complete", "average", "ward"]):
    Z = linkage(X, method=method)
    threshold = Z[-2, 2] * 0.999 + Z[-3, 2] * 0.001  # cut that leaves three clusters
    dendrogram(Z, ax=ax, no_labels=True, color_threshold=threshold, above_threshold_color="gray")
    ax.axhline(threshold, color="k", ls="--", lw=0.8)
    ax.set_title(f"{method} linkage")
    ax.set_ylabel("height")
fig.tight_layout()
