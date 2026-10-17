"""Likelihood functions: Bernoulli trials and the capture-recapture model."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gammaln

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

# Bernoulli likelihood theta^t (1 - theta)^(n - t), rescaled to maximum 1
ax = axes[0]
theta = np.linspace(0.001, 0.999, 999)
for n, t, ls in [(10, 6, "-"), (100, 60, "--")]:
    loglik = t * np.log(theta) + (n - t) * np.log(1 - theta)
    ax.plot(theta, np.exp(loglik - loglik.max()), ls, lw=2, label=f"n = {n}, t = {t}")
grid = np.arange(1, 10) / 10
lik10 = grid**6 * (1 - grid) ** 4
ax.plot(grid, lik10 / (0.6**6 * 0.4**4), "o", color="C0", ms=5, label="theta = 0.1, ..., 0.9")
ax.axvline(0.6, color="0.5", lw=1, ls=":")
ax.set_xlabel("theta")
ax.set_ylabel("L(theta) / max L")
ax.set_title("Bernoulli likelihood, MLE t/n = 0.6")
ax.legend(frameon=False)


# Capture-recapture: L(N) = C(N-10, 16) C(10, 4) / C(N, 20)
def log_binom(a, b):
    return gammaln(a + 1) - gammaln(b + 1) - gammaln(a - b + 1)


ax = axes[1]
N = np.arange(26, 121)
lik = np.exp(log_binom(N - 10, 16) + log_binom(10, 4) - log_binom(N, 20))
ax.plot(N, lik, "-", lw=1.5, color="C2")
ax.plot(N, lik, "o", ms=2.5, color="C2")
best = N[np.isclose(lik, lik.max())]
ax.plot(best, lik[np.isin(N, best)], "o", ms=7, color="C3", label=f"maximum at N = {best[0]} and {best[1]}")
ax.set_xlabel("population size N")
ax.set_ylabel("L(N)")
ax.set_title("Capture-recapture: 4 of 20 recaptured are tagged")
ax.legend(frameon=False)

fig.tight_layout()
