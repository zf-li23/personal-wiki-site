"""Random-walk Metropolis for the binomial model with a Beta(1/2, 1/2) prior, n = 10, y = 3:
trace of the first 1000 iterations and histogram of K = 10000 draws against the exact Beta(3.5, 7.5) posterior."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n, y = 10, 3
K = 10000


def log_q(theta):
    if theta <= 0 or theta >= 1:
        return -np.inf
    return (y - 0.5) * np.log(theta) + (n - y - 0.5) * np.log(1 - theta)


samps = np.empty(K)
samps[0] = 0.5
for t in range(K - 1):
    cand = rng.normal(samps[t], 0.4)
    if np.log(rng.uniform()) < log_q(cand) - log_q(samps[t]):
        samps[t + 1] = cand
    else:
        samps[t + 1] = samps[t]
rate = len(np.unique(samps)) / K

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 3.6), gridspec_kw={"width_ratios": [1.6, 1]})
ax1.plot(np.arange(1, 1001), samps[:1000], lw=0.8)
ax1.set_xlabel("iteration")
ax1.set_ylabel("θ")
ax1.set_title(f"Trace (acceptance rate {rate:.2f})")
grid = np.linspace(0, 1, 300)
ax2.hist(samps, bins=40, density=True, alpha=0.6, label="MCMC draws")
ax2.plot(grid, stats.beta.pdf(grid, y + 0.5, n - y + 0.5), label="Beta(3.5, 7.5)")
ax2.set_xlabel("θ")
ax2.set_ylabel("density")
ax2.legend(frameon=False)
ax2.set_title("Histogram of 10000 draws")
fig.tight_layout()
