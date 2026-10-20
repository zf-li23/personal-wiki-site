"""Choosing k for k-means: within-cluster sum of squares (elbow) and mean silhouette."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
centers = np.array([[0, 0], [5, 0], [0, 5], [5, 5]])
X = np.vstack([rng.normal(c, 1.0, (100, 2)) for c in centers])
D = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(axis=2))


def kmeans_pp(X, k, rng):
    """k-means++ seeding followed by Lloyd iterations; returns labels and SSE."""
    c = [X[rng.integers(len(X))]]
    for _ in range(k - 1):
        d2 = ((X[:, None, :] - np.array(c)) ** 2).sum(axis=2).min(axis=1)
        c.append(X[rng.choice(len(X), p=d2 / d2.sum())])
    c = np.array(c)
    for _ in range(100):
        lab = ((X[:, None, :] - c) ** 2).sum(axis=2).argmin(axis=1)
        new = np.array([X[lab == j].mean(axis=0) if np.any(lab == j) else c[j] for j in range(k)])
        if np.allclose(new, c):
            break
        c = new
    return lab, ((X - c[lab]) ** 2).sum()


def mean_silhouette(D, lab):
    s = np.zeros(len(lab))
    for i in range(len(lab)):
        same = lab == lab[i]
        if same.sum() == 1:
            continue
        a = D[i, same].sum() / (same.sum() - 1)
        b = min(D[i, lab == j].mean() for j in set(lab) if j != lab[i])
        s[i] = (b - a) / max(a, b)
    return s.mean()


ks = range(1, 9)
sse, sil = [], []
for k in ks:
    best = min((kmeans_pp(X, k, rng) for _ in range(5)), key=lambda r: r[1])
    sse.append(best[1])
    sil.append(mean_silhouette(D, best[0]) if k > 1 else np.nan)

fig, axes = plt.subplots(1, 3, figsize=(13, 3.8))
axes[0].scatter(X[:, 0], X[:, 1], s=8)
axes[0].set_title("data (4 true clusters)")
axes[0].set_aspect("equal")
axes[1].plot(list(ks), sse, "o-")
axes[1].axvline(4, color="gray", ls="--", lw=0.8)
axes[1].set_xlabel("k")
axes[1].set_ylabel("within-cluster SSE $W_k$")
axes[1].set_title("elbow method")
axes[2].plot(list(ks), sil, "o-", color="C1")
axes[2].axvline(4, color="gray", ls="--", lw=0.8)
axes[2].set_xlabel("k")
axes[2].set_ylabel("mean silhouette")
axes[2].set_title("silhouette")
fig.tight_layout()
