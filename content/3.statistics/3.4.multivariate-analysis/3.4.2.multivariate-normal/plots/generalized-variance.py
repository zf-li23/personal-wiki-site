"""Three samples with the same generalized variance det S = 9 but different shapes."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
mean = np.array([2.0, 1.0])
covs = [np.array([[5.0, 4.0], [4.0, 5.0]]), np.array([[3.0, 0.0], [0.0, 3.0]]), np.array([[5.0, -4.0], [-4.0, 5.0]])]
titles = ["r = 0.8", "r = 0", "r = -0.8"]
c2 = stats.chi2.ppf(0.95, 2)
t = np.linspace(0, 2 * np.pi, 400)
circle = np.vstack([np.cos(t), np.sin(t)])

fig, axes = plt.subplots(1, 3, figsize=(13, 4.6), sharex=True, sharey=True)
for ax, S, title in zip(axes, covs, titles):
    X = rng.multivariate_normal(mean, S, size=40)
    lam, P = np.linalg.eigh(S)
    ell = mean[:, None] + P @ np.diag(np.sqrt(lam * c2)) @ circle
    ax.scatter(X[:, 0], X[:, 1], s=14, color="C0", alpha=0.8)
    ax.plot(ell[0], ell[1], color="C3", lw=1.5)
    for k in range(2):
        v = P[:, k] * np.sqrt(lam[k] * c2)
        ax.annotate("", xy=mean + v, xytext=mean, arrowprops=dict(arrowstyle="->", color="C2", lw=1.5))
    ax.set_title(f"{title}, det S = {np.linalg.det(S):.0f}")
    ax.set_aspect("equal")
    ax.axhline(0, color="0.6", lw=0.8)
    ax.axvline(0, color="0.6", lw=0.8)
    ax.set_xlabel("x1")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("x2")
axes[0].set_xlim(-6, 10)
axes[0].set_ylim(-7, 9)
fig.tight_layout()
