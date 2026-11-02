"""Risk of the MLE and of James-Stein estimators for p = 10 normal means (sigma = 1)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

p = 10
norms = np.linspace(0, 8, 81)


def inv_moment(lam, p, kmax=400):
    # E[1 / chi^2_p(lam)] as a Poisson(lam / 2) mixture of central chi-square terms
    k = np.arange(kmax)
    w = stats.poisson(lam / 2).pmf(k)
    return np.sum(w / (p - 2 + 2 * k))


risk_js = np.array([p - (p - 2) ** 2 * inv_moment(r**2, p) for r in norms])

# positive-part James-Stein estimator by simulation
rng = np.random.default_rng(0)
reps = 20000
risk_pp = []
for r in norms:
    theta = np.zeros(p)
    theta[0] = r
    x = theta + rng.standard_normal((reps, p))
    c = np.maximum(0.0, 1 - (p - 2) / np.sum(x**2, axis=1))
    risk_pp.append(np.mean(np.sum((c[:, None] * x - theta) ** 2, axis=1)))

fig, ax = plt.subplots(figsize=(6.5, 4))
ax.axhline(p, color="0.4", ls="--", lw=1.5, label="MLE x (risk p)")
ax.plot(norms, risk_js, color="C0", lw=1.8, label="James-Stein (exact)")
ax.plot(norms, risk_pp, color="C3", lw=1.4, ls="-.", label="positive-part James-Stein (simulated)")
ax.set_xlabel(r"$\|\theta\|$")
ax.set_ylabel(r"risk $R(\tilde\theta, \theta)$")
ax.set_title("p = 10 normal means, shrinkage toward 0", fontsize=11)
ax.set_ylim(0, 11)
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
fig.tight_layout()
