"""Bivariate normal target with correlation 0.9, started at (-3, 3): the Gibbs sampler and
Metropolis-within-Gibbs (Gibbs step for theta_1, random-walk step with variance 2.4^2 (1 - rho^2) for theta_2)."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
rho = 0.9
sd = np.sqrt(1 - rho ** 2)
T = 1000


def gibbs():
    th = np.empty((T + 1, 2))
    th[0] = -3, 3
    for t in range(1, T + 1):
        th1 = rng.normal(rho * th[t - 1, 1], sd)
        th2 = rng.normal(rho * th1, sd)
        th[t] = th1, th2
    return th


def mwg():
    th = np.empty((T + 1, 2))
    th[0] = -3, 3
    acc = 0
    for t in range(1, T + 1):
        th1 = rng.normal(rho * th[t - 1, 1], sd)
        cur = th[t - 1, 1]
        cand = cur + 2.4 * sd * rng.normal()
        # log full conditional of theta_2 given theta_1: N(rho theta_1, 1 - rho^2)
        log_r = (-(cand - rho * th1) ** 2 + (cur - rho * th1) ** 2) / (2 * sd ** 2)
        if np.log(rng.uniform()) < log_r:
            cur = cand
            acc += 1
        th[t] = th1, cur
    return th, acc / T


g = gibbs()
w, rate = mwg()
xx = np.linspace(-4, 4, 200)
X, Y = np.meshgrid(xx, xx)
dens = np.exp(-(X ** 2 - 2 * rho * X * Y + Y ** 2) / (2 * (1 - rho ** 2)))

fig, axes = plt.subplots(1, 2, figsize=(10, 4.6), sharey=True)
for ax, chain, title in ((axes[0], g, "Gibbs sampler"), (axes[1], w, f"Metropolis-within-Gibbs (acceptance {rate:.2f})")):
    ax.contour(X, Y, dens, levels=[0.05, 0.3, 0.7], colors="gray", linewidths=0.7)
    # staircase path of the first 20 iterations: theta_1 moves first, then theta_2
    path = [chain[0]]
    for t in range(1, 21):
        path.append((chain[t, 0], chain[t - 1, 1]))
        path.append(chain[t])
    path = np.array(path)
    ax.plot(path[:, 0], path[:, 1], "-", lw=0.8, color="C0")
    ax.plot(chain[21:, 0], chain[21:, 1], ".", ms=1.5, alpha=0.4, color="C1")
    ax.plot(*chain[0], "s", color="C3")
    ax.set_xlabel("θ1")
    ax.set_title(title, fontsize=10)
    ax.set_aspect("equal")
axes[0].set_ylabel("θ2")
fig.tight_layout()
