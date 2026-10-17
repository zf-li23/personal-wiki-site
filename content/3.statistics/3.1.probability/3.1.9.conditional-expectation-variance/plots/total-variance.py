"""Law of total variance: within-group variance plus between-group variance of group means."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
probs = np.array([0.1, 0.6, 0.3])
means = np.array([165.0, 175.0, 180.0])
sds = np.array([4.0, 5.0, 4.5])
n = 6000
g = rng.choice(3, size=n, p=probs)
x = rng.normal(means[g], sds[g])

mu = probs @ means
within = probs @ sds**2
between = probs @ (means - mu) ** 2

fig, ax = plt.subplots(figsize=(7.5, 4.3))
bins = np.linspace(145, 200, 70)
for k, lab in enumerate(["y = 24", "y = 25", "y = 26"]):
    ax.hist(x[g == k], bins=bins, alpha=0.45, color=f"C{k}", label=f"group {lab}: mean {means[k]:.0f}")
ax.hist(x, bins=bins, histtype="step", color="0.4", lw=1.4, label="all")
ax.axvline(mu, color="C3", lw=1.5, ls="--")
ax.set_xlabel("x (height)")
ax.set_ylabel("count")
ax.set_title(f"Var X = {within:.2f} (E Var(X|Y)) + {between:.2f} (Var E(X|Y)) = {within + between:.2f}")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)
fig.tight_layout()
