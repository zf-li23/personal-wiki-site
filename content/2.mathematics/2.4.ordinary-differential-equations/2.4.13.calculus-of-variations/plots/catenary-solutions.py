"""Catenaries y = C cosh(x / C) through (-1, h) and (1, h): two, one or no solutions."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq, minimize_scalar

a = 1.0
g = lambda s: np.cosh(s) / s  # h / a as a function of s = a / C
s_star = minimize_scalar(g, bounds=(0.5, 3), method="bounded").x
h_star = g(s_star)

x = np.linspace(-a, a, 400)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))

ax = axes[0]
s = np.linspace(0.3, 3.5, 400)
ax.plot(s, g(s), color="C0", lw=1.8)
for h, c in [(2.0, "C2"), (h_star, "C1"), (1.3, "C3")]:
    ax.axhline(h, color=c, lw=1, ls="--", label=f"h = {h:.4f}" if h == h_star else f"h = {h}")
ax.plot([s_star], [h_star], "o", color="C1")
ax.set_xlabel("s = a / C")
ax.set_ylabel("cosh(s) / s")
ax.set_ylim(1, 4)
ax.set_title("Endpoint condition C cosh(a / C) = h")
ax.legend(loc="upper center", fontsize=9)

ax = axes[1]
h = 2.0
s1 = brentq(lambda s: g(s) - h / a, 0.05, s_star)
s2 = brentq(lambda s: g(s) - h / a, s_star, 10)
for sv, style, lab in [(s1, "-", "shallow (local minimum)"), (s2, "--", "deep (not a minimum)")]:
    C = a / sv
    ax.plot(x, C * np.cosh(x / C), color="C2", ls=style, lw=1.8, label=f"h = 2, {lab}")
C = a / s_star
ax.plot(x, C * np.cosh(x / C), color="C1", lw=1.8, label=f"h = {h_star:.4f}, critical")
ax.plot([-a, a], [h, h], "o", color="C2")
ax.plot([-a, a], [h_star, h_star], "o", color="C1")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_ylim(0, 2.2)
ax.set_title("Catenaries through (-1, h) and (1, h)")
ax.legend(loc="lower center", fontsize=9)

fig.tight_layout()
