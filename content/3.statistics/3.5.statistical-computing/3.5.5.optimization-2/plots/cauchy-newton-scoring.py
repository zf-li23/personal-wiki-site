"""Cauchy location log-likelihood: Newton-Raphson versus Fisher scoring."""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.77, -0.23, 2.76, 3.80, 3.47, 56.75, -1.34, 4.24, -2.44, 3.29,
              3.71, -2.40, 4.53, -0.07, -1.05, -13.87, -2.53, -1.75, 0.27, 43.21])
n = len(x)


def loglik(t):
    return -np.sum(np.log1p((x - t) ** 2)) - n * np.log(np.pi)


def score(t):
    return np.sum(2 * (x - t) / (1 + (x - t) ** 2))


def obs_info(t):
    # J(theta) = -l''(theta)
    return 2 * np.sum((1 - (x - t) ** 2) / (1 + (x - t) ** 2) ** 2)


def newton(t, k):
    path = [t]
    for _ in range(k):
        t = t + score(t) / obs_info(t)
        path.append(t)
    return np.array(path)


def scoring(t, k):
    # expected information I(theta) = n / 2
    path = [t]
    for _ in range(k):
        t = t + score(t) / (n / 2)
        path.append(t)
    return np.array(path)


mle = newton(-0.2, 50)[-1]
grid = np.linspace(-20, 60, 4000)
ll = np.array([loglik(t) for t in grid])

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
ax = axes[0]
ax.plot(grid, ll, color="C0", lw=1.5)
starts = [1.5, 7.0]
for s, c in zip(starts, ["C3", "C2"]):
    p = newton(s, 30)
    ax.plot(p[:6], [loglik(t) for t in p[:6]], "o--", color=c, ms=4, lw=1,
            label=f"Newton from {s:g} -> {p[-1]:.2f}")
p = scoring(7.0, 30)
ax.plot(p[:8], [loglik(t) for t in p[:8]], "s:", color="C1", ms=4, lw=1,
        label=f"scoring from 7 -> {p[-1]:.2f}")
ax.axvline(mle, color="gray", lw=0.8, ls="--")
ax.set_xlabel("theta")
ax.set_ylabel("log-likelihood l(theta)")
ax.set_title(f"Cauchy(theta, 1) sample, n = 20: MLE = {mle:.4f}", fontsize=10)
ax.legend(fontsize=8, loc="lower left")
ax.grid(alpha=0.3)

ax = axes[1]
k = 25
for name, path, c, m in [("Newton-Raphson", newton(-1.0, k), "C3", "o"),
                         ("Fisher scoring", scoring(-1.0, k), "C1", "s")]:
    err = np.abs(path - mle)
    err = np.where(err < 1e-16, np.nan, err)
    ax.semilogy(np.arange(k + 1), err, marker=m, ms=4, color=c, label=name)
ax.set_xlabel("iteration t")
ax.set_ylabel("|theta_t - MLE|")
ax.set_title("start theta_0 = -1: quadratic versus linear convergence", fontsize=10)
ax.legend(fontsize=9)
ax.grid(alpha=0.3, which="both")
fig.tight_layout()
