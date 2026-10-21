"""Polarization states: tip of E for Ex = Ax cos(wt), Ey = Ay cos(wt + dphi), seen facing the oncoming light."""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 400)
cases = [(0.0, 0.6, "0"), (np.pi / 4, 0.6, "π/4"), (np.pi / 2, 0.6, "π/2"), (3 * np.pi / 4, 0.6, "3π/4"),
         (np.pi, 0.6, "π"), (5 * np.pi / 4, 0.6, "5π/4"), (3 * np.pi / 2, 0.6, "3π/2"),
         (np.pi / 2, 1.0, "π/2, Ay = Ax")]

fig, axes = plt.subplots(2, 4, figsize=(9.6, 5.0))
for ax, (dphi, ay, label) in zip(axes.flat, cases):
    ex = np.cos(t)
    ey = ay * np.cos(t + dphi)
    ax.plot(ex, ey, color="C0", lw=1.6)
    # arrow showing the sense of rotation as time increases
    i0, i1 = 40, 55
    if abs(np.sin(dphi)) > 1e-9:
        ax.annotate("", xy=(ex[i1], ey[i1]), xytext=(ex[i0], ey[i0]),
                    arrowprops=dict(arrowstyle="-|>", color="C3", lw=1.4, mutation_scale=14))
        sense = "right (clockwise)" if np.sin(dphi) > 0 else "left (counterclockwise)"
    else:
        sense = "linear"
    ax.axhline(0, color="0.7", lw=0.6)
    ax.axvline(0, color="0.7", lw=0.6)
    ax.set_title(f"Δφ = {label}\n{sense}", fontsize=8.5)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("Ex", fontsize=8)
    ax.set_ylabel("Ey", fontsize=8)
fig.tight_layout()
