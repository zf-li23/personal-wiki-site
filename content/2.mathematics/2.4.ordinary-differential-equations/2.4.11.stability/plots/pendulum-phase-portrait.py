"""Phase portraits of the pendulum x' = y, y' = -sin x - k y for k = 0 and k = 0.25."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

xs = np.linspace(-3 * np.pi, 3 * np.pi, 300)
ys = np.linspace(-3.2, 3.2, 200)
X, Y = np.meshgrid(xs, ys)

fig, axes = plt.subplots(1, 2, figsize=(13, 4.6))
for ax, k in zip(axes, [0.0, 0.25]):
    U, V = Y, -np.sin(X) - k * Y
    ax.streamplot(X, Y, U, V, density=1.3, color="C0", linewidth=0.8, arrowsize=0.9)
    if k == 0:
        # separatrices: energy level y^2/2 + 1 - cos x = 2
        sep = 2 * np.cos(xs / 2)
        ax.plot(xs, sep, color="C3", lw=2)
        ax.plot(xs, -sep, color="C3", lw=2)
        title = "undamped pendulum, k = 0"
    else:
        # stable manifolds of the saddle at (pi, 0), integrated backward in time
        for x0 in [np.pi, -np.pi]:
            J = np.array([[0.0, 1.0], [1.0, -k]])
            lam, vec = np.linalg.eig(J)
            v = vec[:, np.argmin(lam)]
            for sgn in [1, -1]:
                start = np.array([x0, 0.0]) + 1e-4 * sgn * v
                sol = solve_ivp(lambda t, u: [u[1], -np.sin(u[0]) - k * u[1]], (0, -25), start,
                                max_step=0.02, rtol=1e-9)
                ax.plot(sol.y[0], sol.y[1], color="C3", lw=2)
        title = "damped pendulum, k = 0.25"
    for m in range(-3, 4):
        style = "o" if m % 2 == 0 else "s"
        ax.plot([m * np.pi], [0], style, color="k", ms=5)
    ax.set_xlim(xs[0], xs[-1])
    ax.set_ylim(ys[0], ys[-1])
    ax.set_xticks(np.arange(-3, 4) * np.pi)
    ax.set_xticklabels([f"{m}π" if m not in (0, 1, -1) else {0: "0", 1: "π", -1: "-π"}[m] for m in range(-3, 4)])
    ax.set_xlabel("x = θ")
    ax.set_ylabel("y = θ'")
    ax.set_title(title + " (circles: centers/foci, squares: saddles)")
fig.tight_layout()
