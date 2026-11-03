"""Explicit (forward Euler) time stepping of the heat equation u_t = u_xx on
[0, 1] with u = 0 at both ends, from a step-shaped initial profile.
With r = dt / dx^2 = 0.48 the scheme is stable; with r = 0.52 the
highest-frequency grid mode grows by a factor |1 - 4r| per step."""

import numpy as np
import matplotlib.pyplot as plt

n = 49                                   # interior grid points
dx = 1.0 / (n + 1)
x = np.linspace(0, 1, n + 2)
u0 = np.where(np.abs(x - 0.5) < 0.2, 1.0, 0.0)
u0[[0, -1]] = 0.0


def step(u, r):
    v = u.copy()
    v[1:-1] = u[1:-1] + r * (u[2:] - 2 * u[1:-1] + u[:-2])
    return v


fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), sharey=True)
snapshots = [0, 15, 30, 45]
for ax, r in zip(axes, [0.48, 0.52]):
    u = u0.copy()
    for m in range(max(snapshots) + 1):
        if m in snapshots:
            ax.plot(x, u, marker="." if m else None, ms=3,
                    label=f"step {m}, t = {m * r * dx ** 2:.4f}")
        u = step(u, r)
    ax.set_title(f"r = dt/dx^2 = {r}" + ("  (stable)" if r <= 0.5 else "  (unstable)"))
    ax.set_xlabel("x")
    ax.set_ylim(-0.6, 1.2)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc="upper right")
axes[0].set_ylabel("u")
fig.tight_layout()
