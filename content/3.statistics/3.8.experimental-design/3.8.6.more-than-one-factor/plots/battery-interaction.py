"""Battery life experiment: interaction plot of the cell means with standard error bars."""

import numpy as np
import matplotlib.pyplot as plt

temps = [15, 70, 125]
life = {1: [[130, 155, 74, 180], [34, 40, 80, 75], [20, 70, 82, 58]],
        2: [[150, 188, 159, 126], [136, 122, 106, 115], [25, 70, 58, 45]],
        3: [[138, 110, 168, 160], [174, 120, 150, 139], [96, 104, 82, 60]]}
mse = 675.2
se = np.sqrt(mse / 4)

fig, ax = plt.subplots(figsize=(7, 4.5))
for k, (m, ls, mk) in enumerate([(1, ":", "o"), (2, "--", "s"), (3, "-", "^")]):
    means = [np.mean(c) for c in life[m]]
    ax.errorbar(np.array(temps) + (k - 1) * 2, means, yerr=se, ls=ls, marker=mk,
                capsize=3, lw=1.6, label=f"material {m}")
ax.set_xticks(temps)
ax.set_xlabel("temperature (F)")
ax.set_ylabel("mean life (h)")
ax.set_title("Battery life: cell means +/- one standard error")
ax.legend(title="material type")
ax.grid(alpha=0.3)
fig.tight_layout()
