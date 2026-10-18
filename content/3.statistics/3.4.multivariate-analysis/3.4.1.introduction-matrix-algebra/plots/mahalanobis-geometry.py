"""Euclidean versus Mahalanobis distance for a correlated sample, before and after whitening."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
Sigma = np.array([[1.0, 1.2], [1.2, 2.25]])
X = rng.multivariate_normal([0, 0], Sigma, size=300)
lam, P = np.linalg.eigh(Sigma)
W = np.diag(lam ** -0.5) @ P.T  # whitening map Lambda^{-1/2} P^T

Pt = np.array([1.2, 1.8])   # along the cloud
Qt = np.array([1.2, -1.0])  # across the cloud
Sinv = np.linalg.inv(Sigma)


def maha(v):
    return np.sqrt(v @ Sinv @ v)


t = np.linspace(0, 2 * np.pi, 400)
circle = np.vstack([np.cos(t), np.sin(t)])
fig, axes = plt.subplots(1, 2, figsize=(11, 5))

ax = axes[0]
ax.scatter(X[:, 0], X[:, 1], s=8, alpha=0.35, color="C0")
r = np.linalg.norm(Pt)
ax.plot(r * circle[0], r * circle[1], color="0.5", ls="--", lw=1.5, label="Euclidean circle through P")
ell = P @ np.diag(np.sqrt(lam)) @ circle * maha(Pt)
ax.plot(ell[0], ell[1], color="C3", lw=2, label="Mahalanobis ellipse through P")
for name, v in [("P", Pt), ("Q", Qt)]:
    ax.plot(*v, "o", color="k", ms=7)
    ax.annotate(f"{name}: Euclid {np.linalg.norm(v):.2f}, Mahal {maha(v):.2f}", v, xytext=(8, 6), textcoords="offset points", fontsize=9)
ax.set_title("Original coordinates")
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_aspect("equal")
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.legend(loc="lower right", fontsize=8)
ax.grid(alpha=0.3)

ax = axes[1]
Y = X @ W.T
ax.scatter(Y[:, 0], Y[:, 1], s=8, alpha=0.35, color="C0")
c = maha(Pt)
ax.plot(c * circle[0], c * circle[1], color="C3", lw=2, label="image of the ellipse: a circle")
for name, v in [("P", Pt), ("Q", Qt)]:
    w = W @ v
    ax.plot(*w, "o", color="k", ms=7)
    ax.annotate(f"{name}: Euclid {np.linalg.norm(w):.2f}", w, xytext=(8, 6), textcoords="offset points", fontsize=9)
ax.set_title("Whitened coordinates y = Lambda^(-1/2) P^T x")
ax.set_xlabel("y1")
ax.set_ylabel("y2")
ax.set_aspect("equal")
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.legend(loc="lower right", fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
