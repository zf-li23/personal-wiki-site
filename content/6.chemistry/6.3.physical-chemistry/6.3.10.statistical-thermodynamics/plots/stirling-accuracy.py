"""Relative error of the two forms of Stirling's approximation for ln N!."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gammaln

n = np.unique(np.logspace(0.31, 6, 200).astype(int))
n = n[n >= 2]
exact = gammaln(n + 1)
crude = n * np.log(n) - n
full = crude + 0.5 * np.log(2 * np.pi * n)

fig, ax = plt.subplots(figsize=(6.5, 4))
ax.loglog(n, np.abs(crude - exact) / exact, color="C0", lw=1.6, label=r"$N\ln N - N$")
ax.loglog(n, np.abs(full - exact) / exact, color="C1", lw=1.6, label=r"$N\ln N - N + \frac{1}{2}\ln(2\pi N)$")
ax.set_xlabel(r"$N$")
ax.set_ylabel(r"relative error in $\ln N!$")
ax.legend(frameon=False, fontsize=9)
fig.tight_layout()
