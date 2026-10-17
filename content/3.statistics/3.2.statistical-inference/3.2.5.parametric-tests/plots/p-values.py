"""p-values of two-sided and one-sided tests based on a standard normal statistic."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

t_obs = 2.2
z = np.linspace(-4, 4, 600)
f = stats.norm.pdf(z)
za2 = stats.norm.ppf(0.975)
za = stats.norm.ppf(0.95)

fig, axes = plt.subplots(1, 2, figsize=(10, 3.6), sharey=True)
panels = [
    (axes[0], "Two-sided: p = P(|T| > |t(x)|)", np.abs(z) >= t_obs, [-za2, za2],
     [r"$-z_{\alpha/2}$", r"$z_{\alpha/2}$"], 2 * stats.norm.sf(t_obs)),
    (axes[1], "One-sided: p = P(T > t(x))", z >= t_obs, [za], [r"$z_\alpha$"],
     stats.norm.sf(t_obs)),
]
for ax, title, mask, crit, labels, p in panels:
    ax.plot(z, f, color="C0", lw=1.8)
    ax.fill_between(z, f, where=mask, color="C3", alpha=0.5,
                    label=f"p-value = {p:.4f}")
    for c, lab in zip(crit, labels):
        ax.axvline(c, color="0.5", ls=":", lw=1)
        ax.text(c, -0.045, lab, ha="center", fontsize=10)
    ax.axvline(t_obs, color="C3", ls="--", lw=1.2)
    ax.text(t_obs + 0.1, 0.3, "$t(x)$", color="C3", fontsize=10)
    ax.set_title(title, fontsize=11)
    ax.set_yticks([])
    ax.set_xlim(-4, 4)
    ax.set_ylim(-0.06, 0.43)
    ax.spines[["left", "top", "right"]].set_visible(False)
    ax.legend(loc="upper left", fontsize=9, frameon=False)
fig.tight_layout()
