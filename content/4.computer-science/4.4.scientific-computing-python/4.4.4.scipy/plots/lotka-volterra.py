"""Lotka-Volterra predator-prey model solved with scipy.integrate.solve_ivp:
populations against time, and orbits in the phase plane for three initial
conditions (each orbit is a closed curve because H(x, y) is conserved)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

a, b, c, d = 1.0, 0.1, 1.5, 0.075


def lotka_volterra(t, z):
    x, y = z
    return [a * x - b * x * y, -c * y + d * x * y]


t = np.linspace(0, 30, 1500)
sol = solve_ivp(lotka_volterra, (0, 30), [10, 5], t_eval=t, rtol=1e-8, atol=1e-10)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(sol.t, sol.y[0], color="C0", label="prey x(t)")
ax1.plot(sol.t, sol.y[1], color="C3", label="predator y(t)")
ax1.set_xlabel("t")
ax1.set_ylabel("population")
ax1.set_title("x(0) = 10, y(0) = 5")
ax1.legend()
ax1.grid(alpha=0.3)

for x0, color in zip([10, 15, 20], ["C0", "C2", "C4"]):
    s = solve_ivp(lotka_volterra, (0, 15), [x0, 5], t_eval=np.linspace(0, 15, 1500),
                  rtol=1e-8, atol=1e-10)
    ax2.plot(s.y[0], s.y[1], color=color, label=f"x(0) = {x0}, y(0) = 5")
ax2.plot(c / d, a / b, "k+", ms=10, label="equilibrium (c/d, a/b)")
ax2.set_xlabel("prey x")
ax2.set_ylabel("predator y")
ax2.set_title("phase plane")
ax2.legend(fontsize=8)
ax2.grid(alpha=0.3)
fig.tight_layout()
