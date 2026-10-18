"""Leverage in a regression with two predictors: contours of constant h_ii are Mahalanobis ellipses."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 60
cov = np.array([[1.0, 0.8], [0.8, 1.0]])
P = rng.multivariate_normal([0, 0], cov, size=n)
P[0] = [1.3, -1.2]
X = np.column_stack([np.ones(n), P])
h = np.einsum("ij,ji->i", X, np.linalg.solve(X.T @ X, X.T))
xbar = P.mean(axis=0)
S = np.cov(P, rowvar=False)
Sinv = np.linalg.inv(S)
g1, g2 = np.meshgrid(np.linspace(-3.2, 3.2, 300), np.linspace(-3.2, 3.2, 300))
D = np.stack([g1 - xbar[0], g2 - xbar[1]], axis=-1)
d2 = np.einsum("...i,ij,...j->...", D, Sinv, D)
lev = 1 / n + d2 / (n - 1)

fig, ax = plt.subplots(figsize=(6.4, 5.6))
cs = ax.contour(g1, g2, lev, levels=[0.05, 0.1, 0.15, 0.2, 0.3], colors="C0", linewidths=1)
ax.clabel(cs, fmt="h = %.2f", fontsize=8)
sc = ax.scatter(P[:, 0], P[:, 1], c=h, cmap="viridis", s=28, zorder=3)
ax.annotate(f"h = {h[0]:.2f}", P[0], xytext=(P[0][0] + 0.3, P[0][1] - 0.5), fontsize=9, color="C3",
            arrowprops=dict(arrowstyle="->", color="C3"))
fig.colorbar(sc, ax=ax, label="leverage h_ii")
ax.set_xlabel("X_1")
ax.set_ylabel("X_2")
ax.set_title("h_ii = 1/n + D^2/(n - 1): the marked point is not extreme\nin X_1 or X_2 alone, but it has the largest leverage", fontsize=10)
ax.set_aspect("equal")
ax.grid(alpha=0.3)
fig.tight_layout()
