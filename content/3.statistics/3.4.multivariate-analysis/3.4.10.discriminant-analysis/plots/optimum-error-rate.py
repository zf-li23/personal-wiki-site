"""Optimum error rate for two normal populations: densities of the discriminant score and Phi(-Delta/2)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

delta = 1.6
mu1, mu2 = delta**2 / 2, -delta**2 / 2  # centered so that the midpoint is 0
y = np.linspace(-6, 6, 600)
f1 = norm.pdf(y, mu1, delta)
f2 = norm.pdf(y, mu2, delta)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
ax = axes[0]
ax.plot(y, f2, color="C0", label="f2(y): N(mu_2Y, Delta^2)")
ax.plot(y, f1, color="C1", label="f1(y): N(mu_1Y, Delta^2)")
ax.fill_between(y, f1, where=y < 0, color="C1", alpha=0.3, label="P(2|1)")
ax.fill_between(y, f2, where=y >= 0, color="C0", alpha=0.3, label="P(1|2)")
ax.axvline(0, color="k", ls="--", lw=1)
ax.text(-5.6, 0.2, "classify as pi_2", fontsize=9)
ax.text(2.2, 0.2, "classify as pi_1", fontsize=9)
ax.set_title(f"Delta^2 = {delta**2:.2f}: each error probability = {norm.cdf(-delta / 2):.4f}")
ax.set_xlabel("discriminant score y (midpoint at 0)")
ax.set_ylim(0, 0.32)
ax.legend(fontsize=8, loc="upper left")

ax = axes[1]
d = np.linspace(0, 6, 300)
ax.plot(d, norm.cdf(-d / 2), color="C2")
ax.scatter([delta], [norm.cdf(-delta / 2)], color="C3", zorder=3)
ax.annotate("Delta = 1.6: 0.2119", (delta, norm.cdf(-delta / 2)), xytext=(2.3, 0.3), arrowprops=dict(arrowstyle="->"))
ax.set_xlabel("Mahalanobis distance Delta")
ax.set_ylabel("minimum TPM = Phi(-Delta/2)")
ax.set_title("Optimum error rate")
ax.grid(alpha=0.3)
fig.tight_layout()
