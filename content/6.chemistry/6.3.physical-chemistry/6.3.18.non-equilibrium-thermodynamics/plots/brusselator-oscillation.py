"""Brusselator x' = a - (b+1) x + x^2 y, y' = b x - x^2 y with a = 1:
time series and phase plane below (b = 1.5) and above (b = 3) the Hopf point b_c = 1 + a^2 = 2."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

a = 1.0


def rhs(t, u, b):
    x, y = u
    return [a - (b + 1) * x + x * x * y, b * x - x * x * y]


fig, axes = plt.subplots(2, 2, figsize=(12, 8.4))
for col, b in enumerate([1.5, 3.0]):
    t_end = 40
    sol = solve_ivp(rhs, (0, t_end), [0.5, 0.5], args=(b,), max_step=0.02, rtol=1e-8)
    ax = axes[0, col]
    ax.plot(sol.t, sol.y[0], color="C0", label="x")
    ax.plot(sol.t, sol.y[1], color="C1", label="y")
    ax.set_xlabel("dimensionless time")
    ax.set_ylabel("dimensionless concentration")
    state = "stable steady state" if b < 1 + a * a else "limit cycle"
    ax.set_title(f"a = {a:g}, b = {b:g}: {state}")
    ax.legend(loc="upper right")

    ax = axes[1, col]
    xs = np.linspace(0.05, 4.0, 40)
    ys = np.linspace(0.05, 5.0, 40)
    X, Y = np.meshgrid(xs, ys)
    U = a - (b + 1) * X + X * X * Y
    V = b * X - X * X * Y
    ax.streamplot(X, Y, U, V, density=1.0, color="0.65", linewidth=0.6, arrowsize=0.8)
    xx = np.linspace(0.05, 4.0, 300)
    ax.plot(xx, ((b + 1) * xx - a) / xx**2, color="C2", lw=1.2, ls="--", label="x-nullcline")
    ax.plot(xx, b / xx, color="C4", lw=1.2, ls=":", label="y-nullcline")
    for x0, y0 in [(0.5, 0.5), (1.05, b / a + 0.05)]:
        s = solve_ivp(rhs, (0, 60), [x0, y0], args=(b,), max_step=0.02, rtol=1e-8)
        ax.plot(s.y[0], s.y[1], color="C0", lw=1.4)
    if b > 1 + a * a:
        s = solve_ivp(rhs, (0, 200), [0.5, 0.5], args=(b,), max_step=0.02, rtol=1e-8)
        m = s.t > 150
        ax.plot(s.y[0][m], s.y[1][m], color="C3", lw=2.4, label="limit cycle")
    ax.plot([a], [b / a], "o", color="C3", ms=6, label="steady state (a, b/a)")
    ax.set_xlim(0, 4.0)
    ax.set_ylim(0, 5.0)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="upper right", fontsize=8)
fig.tight_layout()
