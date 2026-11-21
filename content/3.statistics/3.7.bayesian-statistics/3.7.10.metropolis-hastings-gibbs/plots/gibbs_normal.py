"""Gibbs sampler for the normal model with the semi-conjugate prior mu ~ N(0, 10), sigma^2 ~ Inv-chi^2(1, 1):
10 simulated observations, 1000 iterations from mu = 0, sigma^2 = 1."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
data = rng.normal(size=10)
n, ybar = data.size, data.mean()
m, C, nu, s2 = 0.0, 10.0, 1.0, 1.0

T = 1000
mu, sig2 = np.empty(T + 1), np.empty(T + 1)
mu[0], sig2[0] = 0.0, 1.0
for t in range(1, T + 1):
    Cp = 1.0 / (n / sig2[t - 1] + 1.0 / C)
    mp = Cp * (n * ybar / sig2[t - 1] + m / C)
    mu[t] = rng.normal(mp, np.sqrt(Cp))
    nup = nu + n
    scale = nu * s2 + np.sum((data - mu[t]) ** 2)
    sig2[t] = scale / rng.chisquare(nup)

fig, axes = plt.subplots(1, 3, figsize=(13, 3.6))
axes[0].plot(mu, lw=0.7)
axes[0].set_xlabel("iteration")
axes[0].set_ylabel("μ")
axes[0].set_title("Trace of μ")
axes[1].plot(sig2, lw=0.7, color="C1")
axes[1].set_xlabel("iteration")
axes[1].set_ylabel("σ²")
axes[1].set_title("Trace of σ²")
axes[2].plot(mu, sig2, ".", ms=2, alpha=0.5)
axes[2].set_xlabel("μ")
axes[2].set_ylabel("σ²")
axes[2].set_title("Joint draws")
fig.tight_layout()
