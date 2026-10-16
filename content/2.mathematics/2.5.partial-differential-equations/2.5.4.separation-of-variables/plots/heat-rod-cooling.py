"""Cooling of a rod with initial temperature 1 and ends held at 0 (k = l = 1)."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 801)
m = np.arange(0, 400)
n = 2 * m + 1
modes = np.sin(np.outer(n, x) * np.pi)

fig, ax = plt.subplots(figsize=(7.5, 4.4))
ax.plot(x, np.ones_like(x), color="0.5", lw=1.2, ls=":", label="t = 0")
for i, t in enumerate([0.002, 0.01, 0.04, 0.1, 0.2, 0.4]):
    coef = 4 / (np.pi * n) * np.exp(-(n * np.pi) ** 2 * t)
    ax.plot(x, coef @ modes, color=f"C{i}", lw=1.8, label=f"t = {t}")
    if t >= 0.1:
        ax.plot(x, coef[0] * modes[0], color=f"C{i}", lw=1.0, ls="--")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.32)
ax.set_xlabel("x")
ax.set_ylabel("u(x, t)")
ax.set_title("u_t = u_xx, u(0, t) = u(1, t) = 0, u(x, 0) = 1")
ax.legend(loc="upper center", fontsize=8, ncol=7, handlelength=1.5, columnspacing=1.0)
fig.tight_layout()
