"""First two principal components versus t-SNE for the 8 x 8 handwritten digits data bundled with scikit-learn."""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.manifold import TSNE

digits = load_digits()
x, y = digits.data, digits.target
xc = x - x.mean(0)
_, _, Vt = np.linalg.svd(xc, full_matrices=False)
pcs = xc @ Vt[:2].T
emb = TSNE(n_components=2, perplexity=30, init="pca", random_state=0).fit_transform(x)

cmap = plt.get_cmap("tab10")
fig, axes = plt.subplots(1, 2, figsize=(12, 5.4))
for ax, data, title in [(axes[0], pcs, "PCA: first two components"), (axes[1], emb, "t-SNE (perplexity 30)")]:
    for d in range(10):
        m = y == d
        ax.scatter(data[m, 0], data[m, 1], s=5, color=cmap(d), label=str(d), alpha=0.8)
    for d in range(10):
        cx, cy = np.median(data[y == d], axis=0)
        ax.text(cx, cy, str(d), fontsize=13, fontweight="bold", ha="center", va="center")
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])
axes[1].legend(markerscale=3, fontsize=8, loc="center left", bbox_to_anchor=(1.0, 0.5), title="digit")
fig.tight_layout()
