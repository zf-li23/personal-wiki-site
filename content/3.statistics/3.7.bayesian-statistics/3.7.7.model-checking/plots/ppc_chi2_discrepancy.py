"""Chi-square discrepancy for the rat tumor data under a common-rate and a hierarchical model."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import betaln

rng = np.random.default_rng(0)

# Tarone (1982): 70 historical control groups and the current group 4/14
rows = ["0/20 0/20 0/20 0/20 0/20 0/20 0/20 0/19 0/19 0/19", "0/19 0/18 0/18 0/17 1/20 1/20 1/20 1/20 1/19 1/19",
        "1/18 1/18 2/25 2/24 2/23 2/20 2/20 2/20 2/20 2/20", "2/20 1/10 5/49 2/19 5/46 3/27 2/17 7/49 7/47 3/20",
        "3/20 2/13 9/48 10/50 4/20 4/20 4/20 4/20 4/20 4/20", "4/20 10/48 4/19 4/19 4/19 5/22 11/46 12/49 5/20 5/20",
        "6/23 5/19 6/22 6/20 6/20 6/20 16/52 15/47 15/46 9/24", "4/14"]
pairs = [tuple(map(int, p.split("/"))) for r in rows for p in r.split()]
y = np.array([a for a, _ in pairs])
n = np.array([b for _, b in pairs])
J, S = len(y), 5000


def chi2(counts, theta):
    return np.sum((counts - n * theta) ** 2 / (n * theta * (1 - theta)), axis=-1)


# model 1: one common rate (the data dominate any reasonable prior; uniform prior here)
theta1 = rng.beta(1 + y.sum(), 1 + (n - y).sum(), S)[:, None] * np.ones(J)

# model 2: theta_j ~ Beta(alpha, beta), p(alpha, beta) ∝ (alpha + beta)^(-5/2), grid on (log(alpha/beta), log(alpha + beta))
u, v = np.meshgrid(np.linspace(-2.3, -1.3, 250), np.linspace(1, 5, 250))
a = np.exp(v) / (1 + np.exp(-u))
b = np.exp(v) - a
logp = np.log(a) + np.log(b) - 2.5 * np.log(a + b)
logp = logp + sum(betaln(a + y[j], b + n[j] - y[j]) - betaln(a, b) for j in range(J))
w = np.exp(logp - logp.max()).ravel()
idx = rng.choice(w.size, S, p=w / w.sum())
theta2 = rng.beta(a.ravel()[idx][:, None] + y, b.ravel()[idx][:, None] + n - y)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
for ax, theta, title in [(axes[0], theta1, "common rate"), (axes[1], theta2, "variable rates (hierarchical)")]:
    t_obs = chi2(y, theta)
    t_rep = chi2(rng.binomial(n, theta), theta)
    ax.scatter(t_obs, t_rep, s=4, alpha=0.25, color="C0", edgecolors="none")
    lo = min(t_obs.min(), t_rep.min())
    hi = max(t_obs.max(), t_rep.max())
    ax.plot([lo, hi], [lo, hi], color="k", lw=1)
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_title(f"{title}: p = {np.mean(t_rep >= t_obs):.2f}", fontsize=11)
    ax.set_xlabel(r"$T(y,\theta^s)$")
    ax.set_ylabel(r"$T(y^{\mathrm{rep},s},\theta^s)$")
    ax.grid(alpha=0.3)
fig.tight_layout()
