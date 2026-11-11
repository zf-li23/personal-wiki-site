"""PCA and t-SNE of a synthetic population with clusters.

600 points (population states) in 50 dimensions from 6 clusters of 100 points: cluster centers
random (s.d. 3 per coordinate); the within-cluster s.d. is 0.4 for two clusters (tight), 1.0 for two
and 2.0 for two (wide). A: PCA (first two PCs). B-D: t-SNE (scikit-learn, PCA initialization) with
perplexity 5, 30 and 200. Colors are the true clusters.
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
d, k, n = 50, 6, 100
centers = rng.normal(0, 3, (k, d))
sds = [0.4, 0.4, 1.0, 1.0, 2.0, 2.0]
X = np.vstack([c + rng.normal(0, s, (n, d)) for c, s in zip(centers, sds)])
lab = np.repeat(np.arange(k), n)
cols = [P.edge("dna"), P.edge("rna"), P.edge("protein"), P.edge("positive"), P.edge("negative"), P.edge("enzyme")]

fig, axs = plt.subplots(1, 4, figsize=(14, 3.6))
emb = [("A  PCA", PCA(2).fit_transform(X))]
for p, l in ((5, "B"), (30, "C"), (200, "D")):
    emb.append((f"{l}  t-SNE, perplexity {p}", TSNE(2, perplexity=p, init="pca", random_state=0).fit_transform(X)))
for ax, (ttl, Y) in zip(axs, emb):
    for c in range(k):
        ax.scatter(Y[lab == c, 0], Y[lab == c, 1], s=6, color=cols[c])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(ttl, loc="left", fontsize=9.5)
fig.tight_layout()
