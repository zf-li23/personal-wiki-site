"""Thread break points: the EDF with the 95% Kolmogorov confidence band (critical value 0.294),
the hypothesized U(0, 6) distribution function and the alternative piecewise-linear one."""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.6, 0.8, 1.1, 1.2, 1.4, 1.7, 1.8, 1.9, 2.2, 2.4,
              2.5, 2.9, 3.1, 3.4, 3.4, 3.9, 4.4, 4.9, 5.2, 5.9])
n, d_crit = len(x), 0.294

steps_x = np.concatenate([[0.0], x, [6.0]])
steps_y = np.concatenate([[0.0], np.arange(1, n + 1) / n, [1.0]])
grid = np.linspace(0, 6, 601)
f_unif = grid / 6
f_alt = np.where(grid <= 3, grid / 5, 0.2 + 4 * grid / 30)

fig, ax = plt.subplots(figsize=(7.6, 4.8))
ax.step(steps_x, steps_y, where="post", color="C0", lw=1.8, label="EDF $F_n$ ($n = 20$)")
ax.fill_between(steps_x, np.clip(steps_y - d_crit, 0, 1), np.clip(steps_y + d_crit, 0, 1),
                step="post", color="C0", alpha=0.15, label="95% band $F_n \\pm 0.294$")
ax.plot(grid, f_unif, color="C1", lw=1.8, label="(i) $\\mathrm{U}(0, 6)$")
ax.plot(grid, f_alt, color="C2", lw=1.8, ls="--", label="(ii) piecewise linear")
# the Kolmogorov distance for (i) is attained just after the jump at x = 3.4
ax.annotate("", xy=(3.4, 0.75), xytext=(3.4, 3.4 / 6),
            arrowprops=dict(arrowstyle="<->", color="C3", lw=1.6, shrinkA=0, shrinkB=0))
ax.text(3.5, 0.64, "$D_n = 0.183$", color="C3", fontsize=10)
ax.set_xlim(0, 6)
ax.set_ylim(-0.02, 1.02)
ax.set_xlabel("break point $x$ (cm)")
ax.set_ylabel("cumulative probability")
ax.grid(alpha=0.3)
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
