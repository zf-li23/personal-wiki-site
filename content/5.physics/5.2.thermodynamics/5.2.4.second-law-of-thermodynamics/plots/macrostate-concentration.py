"""Number of microstates of N molecules with n in the left half, as a distribution of the fraction n/N."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gammaln

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# left: small N, microstate counts binom(N, n)
for i, N in enumerate([4, 6, 8]):
    n = np.arange(N + 1)
    omega = np.exp(gammaln(N + 1) - gammaln(n + 1) - gammaln(N - n + 1))
    ax1.plot(n / N, omega, "o-", color=f"C{i}", ms=4, lw=1.2, label=f"N = {N}")
ax1.set_xlabel("fraction in the left half  n/N")
ax1.set_ylabel(r"number of microstates $\Omega$")
ax1.set_title("Few molecules: every macrostate is visible")
ax1.legend(fontsize=9)

# right: probability of the macrostate, rescaled to a density in n/N
x = np.linspace(0, 1, 2001)
for i, N in enumerate([10, 100, 1000, 10000]):
    n = np.arange(N + 1)
    logp = gammaln(N + 1) - gammaln(n + 1) - gammaln(N - n + 1) - N * np.log(2)
    ax2.plot(n / N, np.exp(logp) * N, color=f"C{i}", lw=1.4, label=f"N = {N}")
ax2.set_xlim(0, 1)
ax2.set_yscale("log")
ax2.set_ylim(1e-3, 200)
ax2.set_xlabel("fraction in the left half  n/N")
ax2.set_ylabel("probability density of n/N")
ax2.set_title(r"Width shrinks like $1/\sqrt{N}$")
ax2.legend(fontsize=9)
fig.tight_layout()
