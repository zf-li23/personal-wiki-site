"""Direction field of y' = x^2 + y^2, circular isoclines, numerically integrated curves."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

xs = np.linspace(-2, 2, 21)
ys = np.linspace(-2, 2, 21)
X, Y = np.meshgrid(xs, ys)
S = X**2 + Y**2
L = np.sqrt(1 + S**2)

fig, ax = plt.subplots(figsize=(6.5, 6))
ax.quiver(X, Y, 1 / L, S / L, angles="xy", headwidth=0, headlength=0, headaxislength=0,
          pivot="middle", scale=30, width=0.003, color="0.55")
phi = np.linspace(0, 2 * np.pi, 300)
for k in [1, 4]:
    r = np.sqrt(k)
    ax.plot(r * np.cos(phi), r * np.sin(phi), color="C3", ls="--", lw=1.0)
ax.plot([], [], color="C3", ls="--", label="isoclines x^2 + y^2 = k (k = 1, 4)")


def blowup(t, y):
    return abs(y[0]) - 6


blowup.terminal = True
for y0 in [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0]:
    for t_end in (2.5, -2.5):
        sol = solve_ivp(lambda t, y: t**2 + y**2, (0, t_end), [y0], events=blowup,
                        max_step=0.01, rtol=1e-8)
        ax.plot(sol.t, sol.y[0], color="C0", lw=1.5)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("y' = x^2 + y^2: direction field, isoclines, integral curves")
ax.legend(loc="lower right", fontsize=8)
fig.tight_layout()
