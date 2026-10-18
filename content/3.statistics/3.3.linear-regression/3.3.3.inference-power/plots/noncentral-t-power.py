"""Power of the slope t-test as an area under a noncentral t density (Toluca planning example)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = 23
delta = 1.5 / np.sqrt(2500 / 19800)
c = stats.t.ppf(0.975, df)
power = stats.nct.sf(c, df, delta) + stats.nct.cdf(-c, df, delta)

x = np.linspace(-5, 10, 600)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

ax = axes[0]
f0 = stats.t.pdf(x, df)
f1 = stats.nct.pdf(x, df, delta)
ax.plot(x, f0, color="C0", lw=2, label="t_23 (under H0: beta_1 = 0)")
ax.plot(x, f1, color="C3", lw=2, label=f"t_23(delta = {delta:.2f}) (beta_1 = 1.5)")
ax.fill_between(x, f1, where=x > c, color="C3", alpha=0.3, label=f"power = {power:.3f}")
ax.fill_between(x, f1, where=x < -c, color="C3", alpha=0.3)
ax.fill_between(x, f0, where=np.abs(x) > c, color="C0", alpha=0.3, label="alpha = 0.05")
for v in (-c, c):
    ax.axvline(v, color="gray", ls="--", lw=1)
ax.set_xlabel("t")
ax.set_ylabel("density")
ax.set_ylim(0, 0.58)
ax.set_title(f"Critical values +/- {c:.3f}", fontsize=10)
ax.legend(fontsize=8, loc="upper right")
ax.grid(alpha=0.3)

ax = axes[1]
x = np.linspace(-5, 6, 500)
for k, (d, nu) in enumerate([(0, 1), (0, 4), (2, 1), (2, 4)]):
    ax.plot(x, stats.nct.pdf(x, nu, d) if d else stats.t.pdf(x, nu), lw=1.8, color=f"C{k}",
            label=f"delta = {d}, df = {nu}")
ax.set_xlabel("t")
ax.set_title("Noncentral t densities", fontsize=10)
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
