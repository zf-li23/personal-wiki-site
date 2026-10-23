"""Two Gaussian peaks of equal area and equal width (standard deviation sigma) at resolution
Rs = 0.75, 1.0 and 1.5, i.e. a distance of 3, 4 and 6 sigma between the maxima. The number in
each panel is the fraction of each peak that lies beyond the midpoint between them,
Phi(-2 Rs), the cross-contamination when the fractions are cut at the midpoint."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.0), sharey=True)
x = np.linspace(-5, 11, 1200)
for ax, Rs in zip(axes, [0.75, 1.0, 1.5]):
    d = 4 * Rs
    g1 = stats.norm.pdf(x, 0, 1)
    g2 = stats.norm.pdf(x, d, 1)
    ax.fill_between(x, g1, color="C0", alpha=0.25, lw=0)
    ax.fill_between(x, g2, color="C3", alpha=0.25, lw=0)
    ax.plot(x, g1 + g2, color="0.1", lw=1.4)
    ax.axvline(d / 2, color="0.5", lw=0.8, ls=":")
    ov = stats.norm.cdf(-2 * Rs)
    ax.set_title(rf"$R_\mathrm{{s}}$ = {Rs:g}  (overlap {100 * ov:.2g}%)", fontsize=10)
    ax.set_xlabel(r"time / $\sigma$")
    ax.set_xlim(-4.5, 10.5)
    ax.set_yticks([])
axes[0].set_ylabel("detector signal")
fig.tight_layout()
