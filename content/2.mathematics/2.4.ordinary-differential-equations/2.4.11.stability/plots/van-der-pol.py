"""Van der Pol equation x'' - mu (1 - x^2) x' + x = 0: limit cycle and relaxation oscillations."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def vdp(mu):
    return lambda t, u: [u[1], -u[0] + mu * (1 - u[0] ** 2) * u[1]]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4.8))
mu = 1.0
cycle = solve_ivp(vdp(mu), (0, 60), [2.0, 0.0], max_step=0.01, rtol=1e-9)
keep = cycle.t > 40
starts = [(0.1, 0.0), (-0.05, 0.2), (3.0, 3.0), (-3.0, -3.0), (3.8, -1.0), (-3.8, 1.0)]
for j, s in enumerate(starts):
    sol = solve_ivp(vdp(mu), (0, 18), s, max_step=0.01, rtol=1e-9)
    ax1.plot(sol.y[0], sol.y[1], color="C0", lw=0.9)
    i = 60
    ax1.annotate("", xy=(sol.y[0][i + 1], sol.y[1][i + 1]), xytext=(sol.y[0][i], sol.y[1][i]),
                 arrowprops=dict(arrowstyle="-|>", color="C0", lw=1))
ax1.plot(cycle.y[0][keep], cycle.y[1][keep], color="C3", lw=2.4, label="limit cycle")
ax1.plot([0], [0], "o", color="k", ms=4)
ax1.set_xlabel("x")
ax1.set_ylabel("y = x'")
ax1.set_title("phase plane, mu = 1")
ax1.legend(loc="upper left")
ax1.set_xlim(-4.5, 4.5)
ax1.set_ylim(-4.5, 4.5)

for mu, col in [(1.0, "C0"), (5.0, "C1")]:
    sol = solve_ivp(vdp(mu), (0, 40), [0.5, 0.0], max_step=0.01, rtol=1e-9)
    ax2.plot(sol.t, sol.y[0], color=col, label=f"mu = {mu:g}")
ax2.set_xlabel("t")
ax2.set_ylabel("x(t)")
ax2.set_title("x(t): near-harmonic (mu = 1) and relaxation (mu = 5) oscillations")
ax2.legend(loc="upper right")
ax2.grid(alpha=0.3)
fig.tight_layout()
