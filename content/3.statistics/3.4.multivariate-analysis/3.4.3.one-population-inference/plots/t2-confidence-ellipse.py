"""95% confidence ellipse for a bivariate mean with individual, Bonferroni and T^2 intervals."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy import stats

rng = np.random.default_rng(0)
n, p, alpha = 55, 2, 0.05
mu = np.array([5.12, 4.72])
Sigma = np.array([[0.55, 0.62], [0.62, 0.85]])
X = rng.multivariate_normal(mu, Sigma, size=n)
xbar = X.mean(axis=0)
S = np.cov(X.T)
se = np.sqrt(np.diag(S) / n)

c_t = stats.t.ppf(1 - alpha / 2, n - 1)
c_bonf = stats.t.ppf(1 - alpha / (2 * p), n - 1)
c_T2 = np.sqrt(p * (n - 1) / (n - p) * stats.f.ppf(1 - alpha, p, n - p))

lam, P = np.linalg.eigh(S / n)
t = np.linspace(0, 2 * np.pi, 400)
ell = xbar[:, None] + P @ np.diag(c_T2 * np.sqrt(lam)) @ np.vstack([np.cos(t), np.sin(t)])

fig, axes = plt.subplots(1, 2, figsize=(12, 5.2))
ax = axes[0]
ax.scatter(X[:, 0], X[:, 1], s=12, color="0.45")
ax.plot(ell[0], ell[1], color="C3", lw=1.8, label="95% confidence ellipse")
ax.plot(*xbar, "k+", ms=10)
ax.set_xlabel("Achievement-like rating")
ax.set_ylabel("Recognition-like rating")
ax.set_title("Data and confidence ellipse")
ax.set_aspect("equal")
ax.legend(loc="upper left", fontsize=8)
ax.grid(alpha=0.3)

ax = axes[1]
ax.plot(ell[0], ell[1], color="C3", lw=1.8, label="95% confidence ellipse")
for c, col, ls, name in [(c_t, "C0", "--", "individual t"), (c_bonf, "C4", "-.", "Bonferroni, m = 2"), (c_T2, "C1", ":", "T^2 intervals")]:
    lo = xbar - c * se
    ax.add_patch(Rectangle(lo, 2 * c * se[0], 2 * c * se[1], fill=False, ec=col, ls=ls, lw=1.6, label=f"{name} (c = {c:.2f})"))
ax.plot(*xbar, "k+", ms=10)
ax.set_xlabel("mu1")
ax.set_ylabel("mu2")
ax.set_title("Intervals for the two component means")
ax.set_aspect("equal")
ax.autoscale_view()
pad = 1.25 * c_T2 * se
ax.set_xlim(xbar[0] - pad[0], xbar[0] + pad[0])
ax.set_ylim(xbar[1] - pad[1], xbar[1] + 1.5 * pad[1])
ax.legend(loc="upper left", fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
