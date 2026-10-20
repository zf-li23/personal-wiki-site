"""Maximum-margin separating line, margin boundaries and support vectors on separable data."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

rng = np.random.default_rng(3)
pos = rng.normal([2.5, 2.5], 0.6, (20, 2))
neg = rng.normal([0.0, 0.3], 0.6, (20, 2))
X = np.r_[pos, neg]
y = np.r_[np.ones(20), -np.ones(20)]

G = (y[:, None] * y[None, :]) * (X @ X.T)
res = minimize(lambda a: 0.5 * a @ G @ a - a.sum(), np.zeros(len(y)), jac=lambda a: G @ a - 1,
               bounds=[(0, None)] * len(y), method="SLSQP", options={"ftol": 1e-12, "maxiter": 500},
               constraints=[{"type": "eq", "fun": lambda a: a @ y, "jac": lambda a: y}])
alpha = res.x
sv = alpha > 1e-6
w = (alpha * y) @ X
b = np.mean(y[sv] - X[sv] @ w)

fig, ax = plt.subplots(figsize=(6, 5))
ax.scatter(pos[:, 0], pos[:, 1], color="C0", label="positive (y = +1)")
ax.scatter(neg[:, 0], neg[:, 1], color="C1", marker="s", label="negative (y = -1)")
ax.scatter(X[sv, 0], X[sv, 1], s=180, facecolors="none", edgecolors="black", linewidths=1.5,
           label="support vectors")
xs = np.linspace(X[:, 0].min() - 0.5, X[:, 0].max() + 0.5, 2)
for level, style in [(0, "-"), (1, "--"), (-1, "--")]:
    ax.plot(xs, (level - b - w[0] * xs) / w[1], color="black", linestyle=style, linewidth=1.2)
ax.text(0.02, 0.02, f"margin width 2/||w|| = {2 / np.linalg.norm(w):.2f}", transform=ax.transAxes)
ax.set_xlabel("x_1")
ax.set_ylabel("x_2")
ax.set_ylim(X[:, 1].min() - 1, X[:, 1].max() + 1)
ax.legend(loc="upper left", fontsize=8)
ax.set_aspect("equal")
ax.grid(alpha=0.3)
fig.tight_layout()
