"""Agglomerative clustering of six points with Euclidean distance and centroid linkage."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

P = np.array([[0, 0], [1, 2], [2, 1], [4, 1], [5.2, 0], [5, 3]])
labels = ["(0,0)", "(1,2)", "(2,1)", "(4,1)", "(5.2,0)", "(5,3)"]
Z = linkage(P, method="centroid")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
ax = axes[0]
ax.scatter(*P.T, s=50, color="C0", zorder=3)
for (x, y), lab in zip(P, labels):
    ax.annotate(lab, (x, y), xytext=(5, 5), textcoords="offset points")
centroids = {"(1.5,1.5)": (1.5, 1.5), "(4.6,0.5)": (4.6, 0.5), "(1,1)": (1, 1), "(4.73,1.33)": (4.733, 1.333), "(2.87,1.17)": (2.867, 1.167)}
for lab, (x, y) in centroids.items():
    ax.scatter(x, y, marker="x", s=50, color="C3", zorder=3)
    ax.annotate(lab, (x, y), xytext=(4, -12), textcoords="offset points", color="C3", fontsize=8)
ax.set_xlim(-0.8, 6.3)
ax.set_ylim(-0.8, 3.8)
ax.set_aspect("equal")
ax.set_title("Points (o) and centroids of merged clusters (x)")
ax.grid(alpha=0.3)

ax = axes[1]
dendrogram(Z, labels=labels, ax=ax, color_threshold=3.0, above_threshold_color="gray")
ax.axhline(3.0, color="k", ls="--", lw=1)
ax.set_ylabel("centroid distance at merge")
ax.set_title("Dendrogram (cut at height 3 gives 2 clusters)")
fig.tight_layout()
