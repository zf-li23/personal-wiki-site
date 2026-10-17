"""Type I and type II error probabilities of a one-sided Z test."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

alpha = 0.05
c = stats.norm.ppf(1 - alpha)   # critical value z_alpha
delta = 2.5                     # mean of Z under the alternative
z = np.linspace(-3.8, 6.3, 600)
f0 = stats.norm.pdf(z)
f1 = stats.norm.pdf(z, loc=delta)

fig, ax = plt.subplots(figsize=(8, 3.8))
ax.plot(z, f0, color="C0", lw=2, label="density of Z under $H_0$")
ax.plot(z, f1, color="C3", lw=2, label="density of Z under $H_1$")
ax.fill_between(z, f0, where=z >= c, color="C0", alpha=0.45,
                label=r"type I error $\alpha$")
ax.fill_between(z, f1, where=z <= c, color="C3", alpha=0.25,
                label=r"type II error $\beta$")
ax.axvline(c, color="0.4", ls="--", lw=1.2)
ax.text(c + 0.08, 0.415, "critical value $z_\\alpha$", fontsize=10)
ax.annotate("", xy=(6.2, -0.03), xytext=(c, -0.03),
            arrowprops=dict(arrowstyle="->", color="0.4"), annotation_clip=False)
ax.text((c + 6.2) / 2, -0.06, "rejection region", ha="center", fontsize=10)
ax.text(-1.6, -0.06, "acceptance region", ha="center", fontsize=10)
ax.set_ylim(-0.08, 0.45)
ax.set_xlim(z[0], z[-1])
ax.set_yticks([])
ax.set_xticks([0, delta])
ax.set_xticklabels(["0", r"$\sqrt{n}(\mu-\mu_0)/\sigma$"])
ax.spines[["left", "top", "right"]].set_visible(False)
ax.legend(loc="upper right", fontsize=9, frameon=False)
fig.tight_layout()
