"""Equal-tailed versus highest posterior density 90% credible intervals for a Beta(3, 12) posterior."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, optimize

a, b, level = 3, 12, 0.90
post = stats.beta(a, b)
eq = post.ppf([(1 - level) / 2, (1 + level) / 2])

# HPD: shortest interval [lo, hi] with mass `level`
def width(lo):
    return post.ppf(post.cdf(lo) + level) - lo
res = optimize.minimize_scalar(width, bounds=(0, post.ppf(1 - level) - 1e-9), method="bounded")
hpd = np.array([res.x, post.ppf(post.cdf(res.x) + level)])

t = np.linspace(0, 0.7, 600)
fig, axes = plt.subplots(1, 2, figsize=(11, 3.8), sharey=True)
for ax, (name, (lo, hi), c) in zip(axes, [("Equal-tailed", eq, "C0"), ("HPD", hpd, "C1")]):
    ax.plot(t, post.pdf(t), color="0.3", lw=1.6)
    mask = (t >= lo) & (t <= hi)
    ax.fill_between(t[mask], post.pdf(t[mask]), color=c, alpha=0.35)
    for v in (lo, hi):
        ax.plot([v, v], [0, post.pdf(v)], color=c, lw=1.4)
    ax.set_title(f"{name}: [{lo:.3f}, {hi:.3f}], length {hi - lo:.3f}", fontsize=11)
    ax.set_xlabel(r"$\theta$")
    ax.grid(alpha=0.3)
axes[1].axhline(post.pdf(hpd[0]), color="C1", ls=":", lw=1)
axes[0].set_ylabel("posterior density")
fig.tight_layout()
