"""Chi-square plots of squared Mahalanobis distances: normal data versus heavy-tailed multivariate t data."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n, p, nu = 100, 4, 4
Sigma = 0.5 * np.eye(p) + 0.5
L = np.linalg.cholesky(Sigma)

normal = rng.standard_normal((n, p)) @ L.T
w = rng.chisquare(nu, n) / nu
heavy = (rng.standard_normal((n, p)) @ L.T) / np.sqrt(w)[:, None]

prob = (np.arange(1, n + 1) - 0.5) / n
q = stats.chi2.ppf(prob, p)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
for ax, x, title in [(axes[0], normal, "multivariate normal"), (axes[1], heavy, "multivariate t, 4 d.f.")]:
    xc = x - x.mean(0)
    S = np.cov(x.T)
    d2 = np.sort(np.einsum("ij,jk,ik->i", xc, np.linalg.inv(S), xc))
    ax.scatter(q, d2, s=14, color="C0", zorder=3)
    top = max(q.max(), d2.max()) * 1.05
    ax.plot([0, top], [0, top], color="C3", lw=1.2, label="y = x")
    ax.set_xlim(0, q.max() * 1.05)
    ax.set_ylim(0, top)
    ax.set_xlabel("chi-square(4) quantile q_(j)")
    ax.set_ylabel("ordered squared distance d^2_(j)")
    ax.set_title(title)
    ax.legend(loc="upper left")
    ax.grid(alpha=0.3)
fig.tight_layout()
