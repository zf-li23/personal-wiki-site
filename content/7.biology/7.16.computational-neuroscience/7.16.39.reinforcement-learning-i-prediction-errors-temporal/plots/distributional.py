"""Distributional TD learning with asymmetric learning rates (after Dabney et al. 2020).

Rewards drawn from a bimodal distribution: Normal(0.1, 0.04) with probability 0.6, otherwise Normal(0.8, 0.08).
Each of 15 units updates V_i <- V_i + alpha_i^+ delta (delta > 0) or alpha_i^- delta (delta < 0),
delta = r - V_i, with asymmetry tau_i = alpha^+ / (alpha^+ + alpha^-) evenly spaced in (0.05, 0.95),
alpha^+ + alpha^- = 0.02. Each unit converges to the tau_i-expectile of the reward distribution.
A: reward distribution with the learned values (ticks). B: learned value against tau with the exact expectiles.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)


def sample(n):
    hi = rng.random(n) > 0.6
    return np.where(hi, rng.normal(0.8, 0.08, n), rng.normal(0.1, 0.04, n))


taus = np.linspace(0.05, 0.95, 15)
ap, am = 0.02 * taus, 0.02 * (1 - taus)
V = np.full(15, 0.4)
for r in sample(25000):
    d = r - V
    V += np.where(d > 0, ap, am) * d


def expectile(x, tau, it=60):
    e = x.mean()
    for _ in range(it):
        wts = np.where(x > e, tau, 1 - tau)
        e = np.sum(wts * x) / np.sum(wts)
    return e


big = sample(200000)
fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
axs[0].hist(big, bins=80, density=True, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.3)
cmap = plt.get_cmap("coolwarm")
for v, t in zip(V, taus):
    axs[0].axvline(v, color=cmap(t), lw=1.5)
axs[0].axvline(big.mean(), color=P.ink(), lw=1.2, ls="--")
axs[0].text(big.mean() + 0.02, axs[0].get_ylim()[1] * 0.9, "mean", fontsize=8.5)
axs[0].set_xlabel("Reward")
axs[0].set_ylabel("Density")
axs[0].set_title("A  Reward distribution and learned values", loc="left", fontsize=10)
axs[1].plot(taus, [expectile(big, t) for t in taus], color=P.muted(), lw=1.5, label="exact expectiles")
axs[1].scatter(taus, V, c=[cmap(t) for t in taus], s=30, zorder=3, label="learned $V_i$")
axs[1].set_xlabel("Asymmetry $\\tau_i = \\alpha_i^+ / (\\alpha_i^+ + \\alpha_i^-)$")
axs[1].set_ylabel("Converged value (reversal point)")
axs[1].set_title("B  Optimism sets the reversal point", loc="left", fontsize=10)
axs[1].legend(frameon=False, fontsize=8)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
