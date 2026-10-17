"""Beta prior densities, and a Beta(14, 6) prior updated by binomial data with n = 10 and n = 100."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

t = np.linspace(0.001, 0.999, 500)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))

for k, (a, b) in enumerate([(1, 1), (20, 20), (1, 3), (8, 2)]):
    ax1.plot(t, stats.beta.pdf(t, a, b), color=f"C{k}", lw=1.8, label=f"Beta({a}, {b})")
ax1.set_xlabel(r"$\theta$")
ax1.set_ylabel("density")
ax1.set_title("Beta priors")
ax1.set_ylim(0, 5.5)
ax1.grid(alpha=0.3)
ax1.legend(fontsize=9)

a0, b0 = 14, 6                      # prior mean 0.7, sd 0.1
curves = [("prior Beta(14, 6)", a0, b0, "C0"),
          ("posterior, n = 10, x = 3", a0 + 3, b0 + 7, "C1"),
          ("posterior, n = 100, x = 30", a0 + 30, b0 + 70, "C2")]
for label, a, b, c in curves:
    ax2.plot(t, stats.beta.pdf(t, a, b), color=c, lw=1.8, label=label)
ax2.axvline(0.3, color="0.5", ls="--", lw=1)
ax2.text(0.29, 8.6, r"true $\theta = 0.3$", color="0.4", fontsize=9, ha="right")
ax2.set_xlabel(r"$\theta$")
ax2.set_title("Prior and posteriors")
ax2.grid(alpha=0.3)
ax2.legend(fontsize=9, loc="upper right")
fig.tight_layout()
