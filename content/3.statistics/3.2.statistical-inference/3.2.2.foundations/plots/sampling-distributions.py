"""Densities of the chi-square, t and F distributions for several degrees of freedom."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(15, 4.2))

x = np.linspace(0.01, 16, 500)
ax = axes[0]
for r, c in zip([1, 2, 4, 8], ["C0", "C1", "C2", "C3"]):
    ax.plot(x, stats.chi2.pdf(x, r), color=c, lw=1.5, label=f"r = {r}")
q = stats.chi2.ppf(0.95, 4)
xs = np.linspace(q, 16, 200)
ax.fill_between(xs, stats.chi2.pdf(xs, 4), color="C2", alpha=0.3)
ax.annotate("area 0.05 beyond\nupper 0.05 quantile (r = 4)", xy=(q + 0.6, 0.02), xytext=(9, 0.25),
            arrowprops=dict(arrowstyle="->", lw=0.8), fontsize=9)
ax.set_ylim(0, 0.6)
ax.set_title("chi-square density, r degrees of freedom")
ax.set_xlabel("x")
ax.legend()

t = np.linspace(-4, 4, 500)
ax = axes[1]
for r, c in zip([1, 5, 10], ["C0", "C1", "C2"]):
    ax.plot(t, stats.t.pdf(t, r), color=c, lw=1.5, label=f"t, r = {r}")
ax.plot(t, stats.norm.pdf(t), color="C3", lw=1.5, ls="--", label="N(0,1)")
ax.set_title("t density approaches N(0,1)")
ax.set_xlabel("t")
ax.legend()

x = np.linspace(0.01, 5, 500)
ax = axes[2]
for (r1, r2), c in zip([(10, 4), (10, 10), (10, 50)], ["C0", "C1", "C2"]):
    ax.plot(x, stats.f.pdf(x, r1, r2), color=c, lw=1.5, label=f"F({r1}, {r2})")
ax.set_title("F density")
ax.set_xlabel("x")
ax.legend()

for ax in axes:
    ax.grid(alpha=0.3)
fig.tight_layout()
