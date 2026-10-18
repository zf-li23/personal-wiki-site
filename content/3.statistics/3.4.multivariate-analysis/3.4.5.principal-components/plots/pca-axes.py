"""Principal axes of a correlated bivariate sample and the rotated (uncorrelated) principal component scores."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 150
Sigma = np.array([[3.0, 1.8], [1.8, 1.6]])
x = rng.multivariate_normal([2.0, 1.0], Sigma, n)
xbar = x.mean(0)
S = np.cov(x.T)
lam, E = np.linalg.eigh(S)
order = np.argsort(lam)[::-1]
lam, E = lam[order], E[:, order]
if E[0, 0] < 0:
    E[:, 0] *= -1
if E[1, 1] < 0:
    E[:, 1] *= -1
y = (x - xbar) @ E

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
ax = axes[0]
ax.scatter(x[:, 0], x[:, 1], s=12, color="C0", alpha=0.7)
t = np.linspace(0, 2 * np.pi, 300)
for c in [1, 2]:
    ell = xbar[:, None] + c * E @ (np.sqrt(lam)[:, None] * np.vstack([np.cos(t), np.sin(t)]))
    ax.plot(ell[0], ell[1], color="gray", lw=1)
for k, color in [(0, "C3"), (1, "C2")]:
    v = 2.2 * np.sqrt(lam[k]) * E[:, k]
    ax.annotate("", xy=xbar + v, xytext=xbar, arrowprops=dict(arrowstyle="->", color=color, lw=2))
    ax.text(*(xbar + 1.08 * v), f"e_{k + 1}", color=color, fontsize=12)
ax.set_aspect("equal")
ax.set_xlabel("x_1")
ax.set_ylabel("x_2")
ax.set_title("original coordinates")
ax.grid(alpha=0.3)

ax = axes[1]
ax.scatter(y[:, 0], y[:, 1], s=12, color="C1", alpha=0.7)
ax.axhline(0, color="C2", lw=1)
ax.axvline(0, color="C3", lw=1)
ax.set_aspect("equal")
ax.set_xlabel(f"y_1 (sample variance {lam[0]:.2f})")
ax.set_ylabel(f"y_2 (sample variance {lam[1]:.2f})")
ax.set_title("principal component scores")
ax.grid(alpha=0.3)
fig.tight_layout()
