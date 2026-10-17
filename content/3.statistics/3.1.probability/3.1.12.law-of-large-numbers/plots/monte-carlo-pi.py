"""Monte Carlo estimate of pi: random points in the square and the running estimate."""

import numpy as np
import matplotlib.pyplot as plt

n_max = 100000
u = np.random.uniform(-1, 1, n_max)
v = np.random.uniform(-1, 1, n_max)
inside = u**2 + v**2 <= 1
est = 4 * np.cumsum(inside) / np.arange(1, n_max + 1)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
ax = axes[0]
k = 2000
ax.scatter(u[:k][inside[:k]], v[:k][inside[:k]], s=3, color="C1", label="I_j = 1")
ax.scatter(u[:k][~inside[:k]], v[:k][~inside[:k]], s=3, color="C0", label="I_j = 0")
th = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(th), np.sin(th), color="0.3", lw=1.0)
ax.set_aspect("equal")
ax.set_title("2000 uniform points in [-1, 1]^2")
ax.legend(loc="upper right", fontsize=8)

ax = axes[1]
ax.plot(np.arange(1, n_max + 1), est, color="C2", lw=1.0)
ax.axhline(np.pi, color="black", ls="--", lw=1.0, label="pi")
ax.set_xscale("log")
ax.set_ylim(2.5, 3.8)
ax.set_xlabel("number of points n (log scale)")
ax.set_ylabel("4 x (fraction inside)")
ax.set_title("running estimate of pi")
ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
