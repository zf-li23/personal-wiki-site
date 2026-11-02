"""F(3, 16) reference distribution, the 5% rejection region and the observed F0 of the etching experiment."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

d1, d2 = 3, 16
f0 = 66.797
crit = stats.f.ppf(0.95, d1, d2)
x = np.linspace(0.001, 8, 600)
dens = stats.f.pdf(x, d1, d2)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, dens, color="C0", lw=2, label="F(3, 16) density")
mask = x >= crit
ax.fill_between(x[mask], dens[mask], color="C3", alpha=0.4, label=f"rejection region, F > {crit:.2f}")
ax.axvline(crit, color="C3", lw=1)
ax.annotate(f"observed F0 = {f0:.1f}\n(far to the right, p = 2.9e-9)", xy=(8, 0.02), xytext=(5.0, 0.35),
            arrowprops=dict(arrowstyle="->", color="C2"), color="C2")
ax.set_xlim(0, 8)
ax.set_ylim(0, None)
ax.set_xlabel("F")
ax.set_ylabel("density")
ax.legend(frameon=False)
ax.grid(alpha=0.3)
fig.tight_layout()
