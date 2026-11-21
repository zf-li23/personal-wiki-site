"""Adaptive random-walk Metropolis for the normal model with p(mu, sigma) proportional to 1/(1 + sigma^2):
n = 20 simulated observations, B = 10 adaptation rounds of M = 100 iterations, then K = 10000 iterations."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
data = rng.normal(size=20)
n, ybar, sumsq = data.size, data.mean(), np.sum(data ** 2)


def log_q(th):
    mu, sigma = th
    if sigma <= 0:
        return -np.inf
    return -n * np.log(sigma) - (sumsq - 2 * mu * n * ybar + n * mu ** 2) / (2 * sigma ** 2) - np.log1p(sigma ** 2)


def rwm(th0, S, iters):
    L = np.linalg.cholesky(S)
    out = np.empty((iters, 2))
    th, lq, acc = np.array(th0, float), log_q(th0), 0
    for t in range(iters):
        cand = th + L @ rng.normal(size=2)
        lc = log_q(cand)
        if np.log(rng.uniform()) < lc - lq:
            th, lq = cand, lc
            acc += 1
        out[t] = th
    return out, acc / iters


d, B, M, K = 2, 10, 100, 10000
S = np.eye(2)
th = np.array([0.0, 1.0])
history, rates = [], []
for b in range(B):
    draws, rate = rwm(th, 2.4 ** 2 * S / d, M)
    history.append(draws)
    rates.append(rate)
    th = draws[-1]
    # sample covariance of all draws so far; a small ridge keeps it positive definite
    S = np.cov(np.vstack(history).T) + 1e-6 * np.eye(d)
adapt = np.vstack(history)
final, final_rate = rwm(th, 2.4 ** 2 * S / d, K)

fig, axes = plt.subplots(1, 3, figsize=(13, 3.6))
for k, name in enumerate(("μ", "σ")):
    axes[k].plot(np.arange(1, B * M + 1), adapt[:, k], lw=0.8)
    for b in range(1, B):
        axes[k].axvline(b * M, color="gray", lw=0.5, ls=":")
    axes[k].set_xlabel("iteration (adaptation phase)")
    axes[k].set_ylabel(name)
    axes[k].set_title(f"Adaptation: trace of {name}")
axes[2].plot(final[:, 0], final[:, 1], ".", ms=1.5, alpha=0.4)
axes[2].set_xlabel("μ")
axes[2].set_ylabel("σ")
axes[2].set_title(f"{K} draws after adaptation (acceptance {final_rate:.2f})")
fig.tight_layout()
