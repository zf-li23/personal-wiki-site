"""Lord's paradox: unchanged weight distributions but separated parallel regressions."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 150
groups = {"males": 70.0, "females": 55.0}   # mean weight in kg, same in Sep and Jun
sd, rho = 7.0, 0.7                           # common sd and Sep-Jun correlation

fig, ax = plt.subplots(figsize=(6.4, 5.4))
data = {}
for (name, mu), color, marker in zip(groups.items(), ["C0", "C3"], ["o", "s"]):
    x = rng.normal(mu, sd, n)
    # June weight has the same marginal distribution as September weight
    y = mu + rho * (x - mu) + rng.normal(0, sd * np.sqrt(1 - rho**2), n)
    data[name] = (x, y)
    ax.scatter(x, y, s=12, alpha=0.55, color=color, marker=marker, label=name)

# Parallel regression (common slope) as fitted by statistician 2
x_all = np.concatenate([data[k][0] for k in groups])
y_all = np.concatenate([data[k][1] for k in groups])
g_all = np.concatenate([np.full(n, i) for i in range(2)])
design = np.column_stack([np.ones(2 * n), x_all, g_all])
coef, *_ = np.linalg.lstsq(design, y_all, rcond=None)
grid = np.linspace(35, 95, 2)
for i, color in enumerate(["C0", "C3"]):
    ax.plot(grid, coef[0] + coef[1] * grid + coef[2] * i, color=color, lw=2)
ax.plot(grid, grid, color="gray", ls="--", lw=1.2, label="45-degree line (no change)")
for name, mu in groups.items():
    ax.plot(mu, mu, marker="X", color="black", ms=10)
ax.set_title(f"common slope = {coef[1]:.2f}, gap between lines = {-coef[2]:.1f} kg", fontsize=10)
ax.set_xlabel("weight in September / kg")
ax.set_ylabel("weight in June / kg")
ax.set_xlim(35, 95)
ax.set_ylim(35, 95)
ax.set_aspect("equal")
ax.legend(fontsize=9, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
