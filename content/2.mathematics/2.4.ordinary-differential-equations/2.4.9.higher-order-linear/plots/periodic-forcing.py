"""Solutions of y'' + M^2 y = f with 2*pi-periodic forcing: non-resonant,
resonant, and M*T in 2*pi*Z without resonance."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

cases = [
    (np.sqrt(2.0), np.cos, r"$y'' + 2y = \cos x$ (non-resonant)", lambda x: np.cos(x)),
    (1.0, np.cos, r"$y'' + y = \cos x$ (resonance)", None),
    (2.0, np.sin, r"$y'' + 4y = \sin x$ (all solutions periodic)", None),
]
x = np.linspace(0, 8 * np.pi, 3000)
starts = [(0.0, 0.0), (0.6, -0.4)]

fig, axes = plt.subplots(1, 3, figsize=(14, 4.2))
for ax, (M, f, title, periodic) in zip(axes, cases):
    for j, y0 in enumerate(starts):
        sol = solve_ivp(lambda s, u: [u[1], f(s) - M**2 * u[0]], (x[0], x[-1]), y0,
                        t_eval=x, rtol=1e-9, atol=1e-11)
        ax.plot(x, sol.y[0], color=f"C{j}", lw=1.1, label=f"y(0) = {y0[0]:g}, y'(0) = {y0[1]:g}")
    if periodic is not None:
        ax.plot(x, periodic(x), color="C3", lw=2.2, alpha=0.8, label="periodic solution cos x")
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_xticks(np.arange(0, 8.5 * np.pi, 2 * np.pi))
    ax.set_xticklabels(["0"] + [f"{k}π" for k in range(2, 9, 2)])
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc="upper left")
fig.tight_layout()
