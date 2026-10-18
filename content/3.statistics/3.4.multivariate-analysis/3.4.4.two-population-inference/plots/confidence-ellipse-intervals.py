"""Two-sample T^2 confidence ellipse for mu1 - mu2 (p = 2), its projections, Bonferroni and one-at-a-time intervals."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
p, n1, n2, alpha = 2, 30, 25, 0.05
Sigma = np.array([[1.0, 0.7], [0.7, 1.5]])
x1 = rng.multivariate_normal([1.0, 0.5], Sigma, n1)
x2 = rng.multivariate_normal([0.3, 0.2], Sigma, n2)
d = x1.mean(0) - x2.mean(0)
Sp = ((n1 - 1) * np.cov(x1.T) + (n2 - 1) * np.cov(x2.T)) / (n1 + n2 - 2)
V = (1 / n1 + 1 / n2) * Sp

df = n1 + n2 - 2
c2 = df * p / (df - p + 1) * stats.f.ppf(1 - alpha, p, df - p + 1)
c = np.sqrt(c2)

# ellipse {delta : (d - delta)' V^{-1} (d - delta) <= c^2}
w, U = np.linalg.eigh(V)
t = np.linspace(0, 2 * np.pi, 400)
circle = np.vstack([np.cos(t), np.sin(t)])
ell = d[:, None] + c * U @ (np.sqrt(w)[:, None] * circle)

se = np.sqrt(np.diag(V))
half_t2 = c * se
half_bon = stats.t.ppf(1 - alpha / (2 * p), df) * se
half_one = stats.t.ppf(1 - alpha / 2, df) * se

fig, ax = plt.subplots(figsize=(6.4, 5.6))
ax.plot(ell[0], ell[1], color="C0", lw=2, label="95% confidence ellipse")
for half, color, style, label in [
    (half_t2, "C0", "--", "T^2 simultaneous intervals"),
    (half_bon, "C1", "-.", "Bonferroni intervals"),
    (half_one, "C2", ":", "one-at-a-time t intervals"),
]:
    lo, hi = d - half, d + half
    ax.plot([lo[0], hi[0], hi[0], lo[0], lo[0]], [lo[1], lo[1], hi[1], hi[1], lo[1]],
            color=color, ls=style, lw=1.5, label=label)
ax.plot(*d, "o", color="C3", label="observed mean difference")
ax.axhline(0, color="gray", lw=0.6)
ax.axvline(0, color="gray", lw=0.6)
ax.set_xlabel("delta_1 = mu_11 - mu_21")
ax.set_ylabel("delta_2 = mu_12 - mu_22")
ax.set_aspect("equal")
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
