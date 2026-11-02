"""Etch rate data of the plasma etching experiment: points, level means and box plots."""

import numpy as np
import matplotlib.pyplot as plt

power = [160, 180, 200, 220]
rate = [
    [575, 542, 530, 539, 570],
    [565, 593, 590, 579, 610],
    [600, 651, 610, 637, 629],
    [725, 700, 715, 685, 710],
]
grand = np.mean(np.concatenate(rate))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.4), sharey=True)
rng = np.random.default_rng(0)
for k, obs in enumerate(rate):
    x = k + rng.uniform(-0.08, 0.08, len(obs))
    ax1.plot(x, obs, "o", color="C0", alpha=0.8)
    ax1.plot(k, np.mean(obs), "D", color="C3", ms=8)
ax1.plot([], [], "D", color="C3", label="level mean")
ax1.axhline(grand, color="gray", ls="--", label=f"grand mean = {grand:.2f}")
ax1.set_xticks(range(4))
ax1.set_xticklabels(power)
ax1.set_xlabel("RF power (W)")
ax1.set_ylabel("etch rate (Angstrom/min)")
ax1.set_title("Observations and level means")
ax1.legend(loc="upper left", frameon=False)

ax2.boxplot(rate, positions=range(4), widths=0.5)
ax2.set_xticks(range(4))
ax2.set_xticklabels(power)
ax2.set_xlabel("RF power (W)")
ax2.set_title("Box plots by power level")
for ax in (ax1, ax2):
    ax.grid(alpha=0.3, axis="y")
fig.tight_layout()
