"""Random walk Metropolis for the normal-Cauchy model (y = 1) with proposals N(theta_t, v^2), v = 0.1, 2.4 and 10."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
y = 1.0


def log_q(theta):
    return -0.5 * (y - theta) ** 2 - np.log1p(theta ** 2)


def rwm(v, n, theta0=0.0):
    theta = np.empty(n)
    theta[0] = theta0
    acc = 0
    for t in range(n - 1):
        cand = theta[t] + v * rng.normal()
        if np.log(rng.uniform()) < log_q(cand) - log_q(theta[t]):
            theta[t + 1] = cand
            acc += 1
        else:
            theta[t + 1] = theta[t]
    return theta, acc / (n - 1)


fig, axes = plt.subplots(3, 1, figsize=(10, 6.5), sharex=True)
for ax, v, c in zip(axes, (0.1, 2.4, 10.0), ("C3", "C0", "C1")):
    chain, rate = rwm(v, 500)
    ax.plot(chain, color=c, lw=0.9)
    ax.set_ylabel("θ")
    ax.set_title(f"v = {v:g}: acceptance rate {rate:.2f}", fontsize=10)
axes[-1].set_xlabel("iteration")
fig.tight_layout()
