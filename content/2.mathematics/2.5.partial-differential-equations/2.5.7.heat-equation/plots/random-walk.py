"""Random walks with step h every tau converge to the heat kernel with diffusivity k = h^2 / (2 tau)."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
h, tau = 0.1, 0.005
kappa = h**2 / (2 * tau)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

ax = axes[0]
n_steps = 400
steps = rng.choice([-h, h], size=(8, n_steps))
paths = np.concatenate([np.zeros((8, 1)), np.cumsum(steps, axis=1)], axis=1)
tt = np.arange(n_steps + 1) * tau
for k in range(8):
    ax.plot(tt, paths[k], lw=0.9, color=f"C{k}")
s = np.sqrt(2 * kappa * tt)
ax.plot(tt, 2 * s, color="0.4", ls="--", lw=1.2, label="+/- 2 sqrt(2 k t)")
ax.plot(tt, -2 * s, color="0.4", ls="--", lw=1.2)
ax.set_xlabel("t")
ax.set_ylabel("position")
ax.set_title("Sample random walks (h = 0.1, tau = 0.005)")
ax.legend(fontsize=9, loc="upper left")

ax = axes[1]
x = np.linspace(-5, 5, 801)
n_walkers = 50000
for i, t in enumerate([0.1, 0.5, 2.0]):
    n = int(round(t / tau))
    pos = h * (2 * rng.binomial(n, 0.5, size=n_walkers) - n)
    edges = np.arange(-5 - h, 5 + 2 * h, 2 * h)
    ax.hist(pos, bins=edges, density=True, color=f"C{i}", alpha=0.35)
    ax.plot(x, np.exp(-x**2 / (4 * kappa * t)) / np.sqrt(4 * np.pi * kappa * t), color=f"C{i}", lw=1.8, label=f"t = {t}")
ax.set_xlim(-5, 5)
ax.set_xlabel("x")
ax.set_title("Histogram of 50000 walkers vs heat kernel (k = 1)")
ax.legend(fontsize=9)
fig.tight_layout()
