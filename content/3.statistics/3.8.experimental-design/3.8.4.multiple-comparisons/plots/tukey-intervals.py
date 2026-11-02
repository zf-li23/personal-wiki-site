"""Tukey simultaneous 95% intervals and individual LSD intervals for the etching data."""

import itertools
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

power = [160, 180, 200, 220]
rate = np.array([
    [575, 542, 530, 539, 570],
    [565, 593, 590, 579, 610],
    [600, 651, 610, 637, 629],
    [725, 700, 715, 685, 710],
], float)
a, n = rate.shape
means = rate.mean(axis=1)
df = a * n - a
mse = ((rate - means[:, None]) ** 2).sum() / df
se = np.sqrt(2 * mse / n)
half = {
    "Tukey HSD": stats.studentized_range.ppf(0.95, a, df) * np.sqrt(mse / n),
    "LSD (unadjusted)": stats.t.ppf(0.975, df) * se,
}
pairs = list(itertools.combinations(range(a), 2))

fig, ax = plt.subplots(figsize=(8.5, 4.6))
for m, (name, h) in enumerate(half.items()):
    for k, (i, j) in enumerate(pairs):
        d = means[j] - means[i]
        y = k + (0.15 if m == 0 else -0.15)
        ax.plot([d - h, d + h], [y, y], color=f"C{m}", lw=2.5)
        ax.plot(d, y, "o", color=f"C{m}", ms=4)
    ax.plot([], [], color=f"C{m}", lw=2.5, label=f"{name}: +/- {h:.1f}")
ax.axvline(0, color="gray", lw=1)
ax.set_yticks(range(len(pairs)))
ax.set_yticklabels([f"{power[j]} - {power[i]}" for i, j in pairs])
ax.invert_yaxis()
ax.set_xlabel("difference of mean etch rates (Angstrom/min)")
ax.set_title("Pairwise differences of the etching means, 95% intervals")
ax.legend(frameon=False, loc="lower right")
ax.grid(alpha=0.3, axis="x")
fig.tight_layout()
