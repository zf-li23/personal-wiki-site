"""Central 95% posterior interval versus the 95% HPD region for a bimodal posterior."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

t = np.linspace(0, 1, 4001)
dens = 0.6 * stats.beta(4, 14).pdf(t) + 0.4 * stats.beta(16, 6).pdf(t)
dt = t[1] - t[0]
cdf = np.cumsum(dens) * dt
lo, hi = t[np.searchsorted(cdf, 0.025)], t[np.searchsorted(cdf, 0.975)]

# HPD: highest density level k with mass >= 0.95 above it
order = np.argsort(dens)[::-1]
mass = np.cumsum(dens[order]) * dt
k = dens[order][np.searchsorted(mass, 0.95)]
inside = dens >= k

fig, axes = plt.subplots(1, 2, figsize=(11, 3.8), sharey=True)
axes[0].plot(t, dens, color="0.3", lw=1.6)
m = (t >= lo) & (t <= hi)
axes[0].fill_between(t[m], dens[m], color="C0", alpha=0.35)
axes[0].set_title(f"central interval [{lo:.3f}, {hi:.3f}]", fontsize=11)
axes[1].plot(t, dens, color="0.3", lw=1.6)
axes[1].fill_between(t, np.where(inside, dens, np.nan), color="C1", alpha=0.35)
axes[1].axhline(k, color="C1", ls=":", lw=1)
edges = t[np.flatnonzero(np.diff(inside.astype(int)))]
axes[1].set_title("HPD region: " + ", ".join(f"[{a:.3f}, {b:.3f}]" for a, b in zip(edges[::2], edges[1::2])), fontsize=11)
for ax in axes:
    ax.set_xlabel(r"$\theta$")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("posterior density")
fig.tight_layout()
