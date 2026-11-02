"""Powder milk example: posterior of sigma under the conjugate, Jeffreys and uniform-on-sigma priors."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

y = np.array([1011, 1009, 1019, 1012, 1011, 1016, 1018, 1021, 1016, 1012])
ss = np.sum((y - 1015) ** 2)  # 149, known mean 1015
n = len(y)
s02 = 25 * stats.chi2(1).median()  # prior median of sigma is 5 with nu0 = 1

cases = [
    ("conjugate Inv-chi2(1, 11.37)", 1 + n, s02 + ss, "C3"),
    (r"Jeffreys $p(\sigma^2) \propto 1/\sigma^2$", n, ss, "C0"),
    (r"uniform $p(\sigma) \propto 1$", n - 1, ss, "C2"),
]
s = np.linspace(1.5, 10, 1000)
fig, ax = plt.subplots(figsize=(8, 3.9))
for label, nu, S, c in cases:
    # sigma^2 | y ~ Inv-Gamma(nu/2, S/2); density of sigma = density of sigma^2 times 2 sigma
    ax.plot(s, stats.invgamma(nu / 2, scale=S / 2).pdf(s**2) * 2 * s, color=c, lw=1.8, label=label)
prior = stats.invgamma(0.5, scale=s02 / 2).pdf(s**2) * 2 * s
ax.plot(s, prior, color="0.5", ls="--", lw=1.3, label="conjugate prior of sigma")
ax.set_xlabel(r"$\sigma$ (g)")
ax.set_ylabel("posterior density")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
fig.tight_layout()
