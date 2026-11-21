"""Independence Metropolis-Hastings for the normal-Cauchy model (y = 1) with the proposal N(y, 1):
target and proposal densities, and traces from a good and a poor starting value."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, integrate

rng = np.random.default_rng(0)
y = 1.0


def log_q(theta):
    # unnormalized log posterior: N(theta, 1) likelihood times t_1 prior
    return -0.5 * (y - theta) ** 2 - np.log1p(theta ** 2)


def indep_mh(log_target, draw, log_prop, theta0, n):
    theta = np.empty(n)
    theta[0] = theta0
    acc = 0
    for t in range(n - 1):
        cand = draw()
        log_r = (log_target(cand) - log_prop(cand)) - (log_target(theta[t]) - log_prop(theta[t]))
        if np.log(rng.uniform()) < log_r:
            theta[t + 1] = cand
            acc += 1
        else:
            theta[t + 1] = theta[t]
    return theta, acc / (n - 1)


def draw_prop():
    return rng.normal(y, 1.0)


def log_prop(theta):
    return stats.norm.logpdf(theta, y, 1.0)


const = integrate.quad(lambda t: np.exp(log_q(t)), -np.inf, np.inf)[0]
grid = np.linspace(-3, 4, 400)

fig, axes = plt.subplots(1, 3, figsize=(12, 3.4))
axes[0].plot(grid, np.exp(log_q(grid)) / const, label="target p(θ | y)")
axes[0].plot(grid, stats.norm.pdf(grid, y, 1.0), "--", label="proposal N(1, 1)")
axes[0].set_xlabel("θ")
axes[0].set_ylabel("density")
axes[0].legend(frameon=False)
axes[0].set_title("Target and proposal")
for ax, start, title in ((axes[1], 0.0, "Start at θ = 0"), (axes[2], 10.0, "Start at θ = 10")):
    chain, rate = indep_mh(log_q, draw_prop, log_prop, start, 100)
    ax.plot(np.arange(1, 101), chain, "o", ms=3)
    ax.set_xlabel("iteration")
    ax.set_ylabel("θ")
    ax.set_title(f"{title} (acceptance {rate:.2f})")
fig.tight_layout()
