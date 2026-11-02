"""Rat tumor example: beta-binomial hierarchical model with the prior p(alpha, beta) ~ (alpha + beta)^(-5/2)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import special

# Tarone (1982): 70 historical control groups and the current group 4/14
table = """0/20 0/20 0/20 0/20 0/20 0/20 0/20 0/19 0/19 0/19
0/19 0/18 0/18 0/17 1/20 1/20 1/20 1/20 1/19 1/19
1/18 1/18 2/25 2/24 2/23 2/20 2/20 2/20 2/20 2/20
2/20 1/10 5/49 2/19 5/46 3/27 2/17 7/49 7/47 3/20
3/20 2/13 9/48 10/50 4/20 4/20 4/20 4/20 4/20 4/20
4/20 10/48 4/19 4/19 4/19 5/22 11/46 12/49 5/20 5/20
6/23 5/19 6/22 6/20 6/20 6/20 16/52 15/47 15/46 9/24 4/14"""
pairs = [tuple(int(v) for v in s.split("/")) for s in table.split()]
y = np.array([a for a, _ in pairs])
n = np.array([b for _, b in pairs])

# grid on u = log(alpha / beta), v = log(alpha + beta)
u = np.linspace(-2.4, -1.2, 241)
v = np.linspace(1.0, 5.0, 401)
U, V = np.meshgrid(u, v, indexing="ij")
s = np.exp(V)
a = s / (1 + np.exp(-U))
b = s - a
loglik = np.sum(special.betaln(a[..., None] + y, b[..., None] + n - y) - special.betaln(a, b)[..., None], axis=-1)
# prior (alpha + beta)^(-5/2) and the Jacobian alpha * beta of the transformation
lp = loglik - 2.5 * np.log(a + b) + np.log(a) + np.log(b)
p = np.exp(lp - lp.max())
p /= p.sum()

# grid sampling of the hyperparameters, then theta_j | alpha, beta, y ~ Beta(alpha + y_j, beta + n_j - y_j)
rng = np.random.default_rng(0)
k = rng.choice(p.size, size=2000, p=p.ravel())
du, dv = u[1] - u[0], v[1] - v[0]
us = U.ravel()[k] + rng.uniform(-du / 2, du / 2, k.size)
vs = V.ravel()[k] + rng.uniform(-dv / 2, dv / 2, k.size)
sa = np.exp(vs) / (1 + np.exp(-us))
sb = np.exp(vs) - sa
theta = rng.beta(sa[:, None] + y, sb[:, None] + n - y)
med = np.median(theta, axis=0)
lo, hi = np.quantile(theta, [0.025, 0.975], axis=0)

fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.3))
ax = axes[0]
ax.contour(U, V, p, levels=p.max() * np.arange(0.05, 1.0, 0.1), colors="C0", linewidths=1)
ax.scatter(us[:500], vs[:500], s=3, color="C3", alpha=0.5)
ax.set_xlabel(r"$\log(\alpha/\beta)$")
ax.set_ylabel(r"$\log(\alpha+\beta)$")
ax.set_title("marginal posterior of the hyperparameters", fontsize=11)
ax.set_xlim(-2.4, -1.2)
ax.set_ylim(1.0, 4.5)
ax.grid(alpha=0.3)

ax = axes[1]
raw = y / n
jit = rng.uniform(-0.004, 0.004, raw.size)
ax.vlines(raw + jit, lo, hi, color="0.6", lw=0.8)
ax.scatter(raw + jit, med, s=12, color="C0", zorder=3, label="posterior median and 95% interval")
ax.scatter(raw[-1] + jit[-1], med[-1], s=30, color="C3", zorder=4, label="current group 4/14")
ax.plot([0, 0.4], [0, 0.4], color="0.3", ls="--", lw=1, label="y = x (no pooling)")
ax.set_xlabel(r"observed rate $y_j / n_j$")
ax.set_ylabel(r"$\theta_j \mid y$")
ax.set_title("shrinkage of the 71 tumor rates", fontsize=11)
ax.set_xlim(-0.02, 0.42)
ax.set_ylim(-0.02, 0.5)
ax.legend(fontsize=8.5, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
