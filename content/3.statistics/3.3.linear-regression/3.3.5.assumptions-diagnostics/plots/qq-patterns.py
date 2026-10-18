"""Normal Q-Q plots of typical shapes: normal, light tails, heavy tails, right skew, left skew, bimodal."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(0)
n = 60
samples = {
    "normal": rng.normal(0, 1, n),
    "light-tailed (uniform)": rng.uniform(-1, 1, n),
    "heavy-tailed (t, 2 df)": rng.standard_t(2, n),
    "right-skewed (exponential)": rng.exponential(1, n),
    "left-skewed (minus exponential)": -rng.exponential(1, n),
    "bimodal (normal mixture)": np.concatenate([rng.normal(-2, 0.6, n // 2), rng.normal(2, 0.6, n - n // 2)]),
}
p = (np.arange(1, n + 1) - 0.5) / n
z = stats.norm.ppf(p)
fig, axes = plt.subplots(2, 3, figsize=(10, 6.4))
for ax, (name, x) in zip(axes.flat, samples.items()):
    xs = np.sort(x)
    q1, q3 = np.quantile(xs, [0.25, 0.75])
    z1, z3 = stats.norm.ppf([0.25, 0.75])
    slope = (q3 - q1) / (z3 - z1)
    ax.plot(z, xs, "o", ms=3.5, color="C0")
    ax.plot(z, q1 + slope * (z - z1), color="C3", lw=1.3)
    ax.set_title(name, fontsize=10)
    ax.grid(alpha=0.3)
for ax in axes[1]:
    ax.set_xlabel("theoretical quantile z_i")
for ax in axes[:, 0]:
    ax.set_ylabel("sample quantile x_(i)")
fig.suptitle("Normal Q-Q plots (n = 60); the line passes through the quartiles", fontsize=11)
fig.tight_layout()
