"""Poisson-Gamma updating: traffic accidents and asthma mortality examples."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 2, figsize=(11, 3.9))

# traffic accidents: prior Gamma(6.25, 2.5), data sum 26 over n = 8 weeks
t = np.linspace(0, 7, 701)
ax = axes[0]
ax.plot(t, stats.gamma(6.25, scale=1 / 2.5).pdf(t), color="0.5", ls="--", lw=1.5, label="prior Gamma(6.25, 2.5)")
ax.plot(t, stats.gamma(27, scale=1 / 8).pdf(t), color="C0", ls=":", lw=1.5, label="normalized likelihood")
ax.plot(t, stats.gamma(32.25, scale=1 / 10.5).pdf(t), color="C3", lw=1.8, label="posterior Gamma(32.25, 10.5)")
ax.set_title("traffic accidents per week", fontsize=11)
ax.set_xlabel(r"$\theta$")
ax.set_ylabel("density")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)

# asthma mortality: prior Gamma(3, 5); y = 3 with exposure 2, or y = 30 with exposure 20
t = np.linspace(0, 3, 601)
ax = axes[1]
ax.plot(t, stats.gamma(3, scale=1 / 5).pdf(t), color="0.5", ls="--", lw=1.5, label="prior Gamma(3, 5)")
ax.plot(t, stats.gamma(6, scale=1 / 7).pdf(t), color="C0", lw=1.8, label="y = 3, one year: Gamma(6, 7)")
ax.plot(t, stats.gamma(33, scale=1 / 25).pdf(t), color="C3", lw=1.8, label="y = 30, ten years: Gamma(33, 25)")
ax.set_title("asthma deaths per 100,000 per year", fontsize=11)
ax.set_xlabel(r"$\theta$")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
fig.tight_layout()
