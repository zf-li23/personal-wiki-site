"""Normal Q-Q plots with a simultaneous band obtained from the DKW band for the CDF."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(7)
n, alpha = 50, 0.05
eps = np.sqrt(np.log(2 / alpha) / (2 * n))
samples = {"normal sample": rng.normal(3, 2, n), "exponential sample": rng.exponential(2, n)}

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
for ax, (name, s) in zip(axes, samples.items()):
    x = np.sort(s)
    i = np.arange(1, n + 1)
    z = stats.norm.ppf((i - 0.5) / n)
    # A normal CDF lies in the DKW band iff its line passes, at height x_(i),
    # between norm.ppf(i/n - eps) and norm.ppf((i-1)/n + eps)
    zl = stats.norm.ppf(np.clip(i / n - eps, 1e-9, 1 - 1e-9))
    zu = stats.norm.ppf(np.clip((i - 1) / n + eps, 1e-9, 1 - 1e-9))
    zl[i / n - eps <= 0] = -4
    zu[(i - 1) / n + eps >= 1] = 4
    ax.hlines(x, zl, zu, color="C0", alpha=0.35, lw=3, label="95% band (from DKW)")
    ax.plot(z, x, "o", color="C0", ms=3.5, label="data")
    b, a = np.polyfit(z, x, 1)
    zz = np.linspace(-3, 3, 10)
    ax.plot(zz, a + b * zz, color="C3", lw=1.3, label="fitted line")
    ax.set_xlim(-3, 3)
    ax.set_xlabel("theoretical normal quantile")
    ax.set_ylabel("sample quantile")
    ax.set_title(f"Normal Q-Q plot, {name}, n = {n}", fontsize=10)
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)
fig.tight_layout()
