"""Impurity experiment without replication: interaction plot of the single observations."""

import numpy as np
import matplotlib.pyplot as plt

pressure = [25, 30, 35, 40, 45]
impurity = {100: [5, 4, 6, 3, 5], 125: [3, 1, 4, 2, 3], 150: [1, 1, 3, 1, 2]}

fig, ax = plt.subplots(figsize=(7, 4.3))
for (t, y), mk in zip(impurity.items(), ["o", "s", "^"]):
    ax.plot(pressure, y, marker=mk, lw=1.6, label=f"temperature {t} F")
ax.set_xticks(pressure)
ax.set_xlabel("pressure (psi)")
ax.set_ylabel("impurity")
ax.set_title("Impurity data (n = 1): roughly parallel profiles")
ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
