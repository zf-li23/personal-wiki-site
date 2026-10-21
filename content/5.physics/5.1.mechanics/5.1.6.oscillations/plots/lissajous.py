"""Lissajous figures x = cos(m t), y = cos(n t + phi)."""

import numpy as np
import matplotlib.pyplot as plt

ratios = [(1, 1), (1, 2), (2, 3)]
phases = [(0.0, "0"), (np.pi / 4, "pi/4"), (np.pi / 2, "pi/2")]
t = np.linspace(0, 2 * np.pi, 2000)

fig, axes = plt.subplots(3, 3, figsize=(7.5, 7.5))
for i, (m, n) in enumerate(ratios):
    for j, (phi, lab) in enumerate(phases):
        ax = axes[i, j]
        ax.plot(np.cos(m * t), np.cos(n * t + phi), lw=1.6, color="C0")
        ax.set_xlim(-1.15, 1.15)
        ax.set_ylim(-1.15, 1.15)
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])
        if i == 0:
            ax.set_title("phi = " + lab)
        if j == 0:
            ax.set_ylabel(f"omega_x : omega_y = {m}:{n}")
fig.tight_layout()
