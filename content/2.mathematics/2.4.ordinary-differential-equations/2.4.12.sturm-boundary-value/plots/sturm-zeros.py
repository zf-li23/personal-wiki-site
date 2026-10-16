"""Sturm separation (Airy equation) and comparison (y'' + (1 + x/5) y = 0 vs sin x)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def solve(q, y0, x_end, n=4000):
    xs = np.linspace(0, x_end, n)
    sol = solve_ivp(lambda x, u: [u[1], -q(x) * u[0]], (0, x_end), y0,
                    t_eval=xs, rtol=1e-10, atol=1e-12)
    return xs, sol.y[0]


def zeros(xs, ys):
    idx = np.where(np.sign(ys[:-1]) * np.sign(ys[1:]) < 0)[0]
    return xs[idx] - ys[idx] * (xs[idx + 1] - xs[idx]) / (ys[idx + 1] - ys[idx])


fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

ax = axes[0]
xs, u = solve(lambda x: x, [1.0, 0.0], 14)
_, v = solve(lambda x: x, [0.0, 1.0], 14)
ax.plot(xs, u, color="C0", lw=1.6, label="u: u(0) = 1, u'(0) = 0")
ax.plot(xs, v, color="C1", lw=1.6, label="v: v(0) = 0, v'(0) = 1")
ax.plot(zeros(xs, u), 0 * zeros(xs, u), "o", color="C0", ms=5)
ax.plot(zeros(xs, v), 0 * zeros(xs, v), "s", color="C1", ms=5)
ax.axhline(0, color="0.5", lw=0.8)
ax.set_title("Separation: y'' + x y = 0")
ax.set_xlabel("x")
ax.legend(loc="upper right", fontsize=9)

ax = axes[1]
xs, y = solve(lambda x: 1 + x / 5, [0.0, 1.0], 6 * np.pi)
z = np.sin(xs)
ax.plot(xs, z, color="C0", lw=1.6, label="z = sin x  (Q = 1)")
ax.plot(xs, y, color="C3", lw=1.6, label="y'' + (1 + x/5) y = 0")
for zz in np.arange(1, 6) * np.pi:
    ax.axvline(zz, color="C0", lw=0.6, ls=":")
ax.plot(zeros(xs, y), 0 * zeros(xs, y), "o", color="C3", ms=5)
ax.axhline(0, color="0.5", lw=0.8)
ax.set_title("Comparison: larger coefficient, denser zeros")
ax.set_xlabel("x")
ax.legend(loc="upper right", fontsize=9)

fig.tight_layout()
