"""k-means versus a Gaussian mixture fitted by EM on elongated clusters, and BIC against the number of components."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

rng = np.random.default_rng(0)
band = rng.normal(size=(400, 2)) * [2.0, 0.3]
blob = rng.normal(size=(200, 2)) * 0.6
X = np.vstack([band[:200], band[200:] + [0, 2.2], blob + [7, 1.1]])

km = KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)
gm = GaussianMixture(n_components=3, covariance_type="full", n_init=10, init_params="random_from_data", random_state=0).fit(X)

fig, axes = plt.subplots(1, 3, figsize=(15, 4.2), gridspec_kw={"width_ratios": [1.3, 1.3, 1]})
markers = ["o", "^", "s"]
for ax, lab, title in [(axes[0], km.labels_, "k-means, k = 3"), (axes[1], gm.predict(X), "Gaussian mixture (EM), k = 3")]:
    for k in range(3):
        ax.scatter(*X[lab == k].T, s=8, color=f"C{k}", marker=markers[k], alpha=0.7)
    ax.set_title(title)
    ax.set_xlabel("x1")
axes[0].set_ylabel("x2")
for mean, cov in zip(gm.means_, gm.covariances_):
    vals, vecs = np.linalg.eigh(cov)
    angle = np.degrees(np.arctan2(vecs[1, -1], vecs[0, -1]))
    for r in (1, 2):
        axes[1].add_patch(Ellipse(mean, 2 * r * np.sqrt(vals[-1]), 2 * r * np.sqrt(vals[0]), angle=angle, fill=False, color="k", lw=1))

ks = range(1, 8)
bic = [GaussianMixture(n_components=k, covariance_type="full", n_init=5, init_params="random_from_data", random_state=0).fit(X).bic(X) for k in ks]
axes[2].plot(list(ks), bic, marker="o", color="C3")
axes[2].set_xlabel("number of components k")
axes[2].set_ylabel("BIC = -2 ln L + m ln n")
axes[2].set_title("Model selection by BIC")
axes[2].grid(alpha=0.3)
fig.tight_layout()
