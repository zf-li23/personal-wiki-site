"""Contours of a bivariate normal density with their principal axes, and the chi-square coverage."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
mu = np.array([1.0, 2.0])
Sigma = np.array([[2.0, 1.2], [1.2, 1.5]])
X = rng.multivariate_normal(mu, Sigma, size=400)
lam, P = np.linalg.eigh(Sigma)
t = np.linspace(0, 2 * np.pi, 400)
circle = np.vstack([np.cos(t), np.sin(t)])

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
ax = axes[0]
ax.scatter(X[:, 0], X[:, 1], s=6, color="0.5", alpha=0.5)
for level, col in [(0.5, "C0"), (0.9, "C1"), (0.99, "C3")]:
    c = np.sqrt(stats.chi2.ppf(level, 2))
    ell = mu[:, None] + P @ np.diag(c * np.sqrt(lam)) @ circle
    ax.plot(ell[0], ell[1], color=col, lw=1.8, label=f"{int(level * 100)}% contour")
c = np.sqrt(stats.chi2.ppf(0.9, 2))
for k in range(2):
    v = c * np.sqrt(lam[k]) * P[:, k]
    ax.annotate("", xy=mu + v, xytext=mu, arrowprops=dict(arrowstyle="->", color="C2", lw=1.8))
ax.plot(*mu, "k+", ms=10)
ax.set_aspect("equal")
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_title("Contours (x - mu)^T Sigma^(-1) (x - mu) = c^2")
ax.legend(loc="upper left", fontsize=8)
ax.grid(alpha=0.3)

ax = axes[1]
d2 = np.einsum("ij,jk,ik->i", X - mu, np.linalg.inv(Sigma), X - mu)
levels = np.linspace(0.01, 0.99, 99)
frac = [np.mean(d2 <= stats.chi2.ppf(q, 2)) for q in levels]
ax.plot(levels, frac, color="C0", lw=2, label="fraction of sample inside")
ax.plot([0, 1], [0, 1], color="0.5", ls="--", lw=1, label="1 - alpha")
ax.set_xlabel("nominal probability 1 - alpha")
ax.set_ylabel("fraction of the 400 points")
ax.set_title("Probability content of the ellipses")
ax.set_aspect("equal")
ax.legend(loc="upper left", fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
