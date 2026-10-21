"""Two-beam interference: I = I1 + I2 + 2 sqrt(I1 I2) cos(dphi) for several intensity ratios."""

import numpy as np
import matplotlib.pyplot as plt

phi = np.linspace(-4 * np.pi, 4 * np.pi, 1200)
I1 = 1.0

fig, ax = plt.subplots(figsize=(8.0, 3.8))
for i, ratio in enumerate([1.0, 0.25, 0.04]):
    I2 = ratio * I1
    I = I1 + I2 + 2 * np.sqrt(I1 * I2) * np.cos(phi)
    V = 2 * np.sqrt(I1 * I2) / (I1 + I2)
    ax.plot(phi / np.pi, I, color=f"C{i}", lw=1.4,
            label=f"I2/I1 = {ratio:g},  V = {V:.2f}")
ax.axhline(I1, color="0.6", lw=0.8, ls=":")
ax.text(3.05, I1 + 0.07, "incoherent: I1 + I2", fontsize=8, color="0.45")
ax.set_xlabel("phase difference  Δφ / π")
ax.set_ylabel("intensity  I / I1")
ax.set_xticks(np.arange(-4, 5, 1))
ax.set_xlim(-4, 4)
ax.set_ylim(0, 4.3)
ax.legend(loc="upper left", fontsize=8, ncol=3, frameon=False)
fig.tight_layout()
