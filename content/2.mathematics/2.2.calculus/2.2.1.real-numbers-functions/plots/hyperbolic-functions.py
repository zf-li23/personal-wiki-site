"""Hyperbolic functions, and the point (cosh t, sinh t) on the unit hyperbola."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))

x = np.linspace(-2.5, 2.5, 400)
ax = axes[0]
ax.plot(x, np.sinh(x), color="C0", lw=2, label="$\\sinh x$")
ax.plot(x, np.cosh(x), color="C1", lw=2, label="$\\cosh x$")
ax.plot(x, np.tanh(x), color="C2", lw=2, label="$\\tanh x$")
ax.plot(x, np.exp(x) / 2, color="0.6", lw=1, ls="--", label="$\\mathrm{e}^x/2$")
ax.plot(x, np.exp(-x) / 2, color="0.6", lw=1, ls=":", label="$\\mathrm{e}^{-x}/2$")
for level in (-1, 1):
    ax.axhline(level, color="0.8", lw=0.8, ls="--")
ax.set_ylim(-4, 4)
ax.set_title("$\\cosh x \\geq 1$, $\\ |\\tanh x| < 1$", fontsize=11)
ax.legend(loc="lower right", fontsize=9)

ax = axes[1]
t = np.linspace(-1.6, 1.6, 300)
ax.plot(np.cosh(t), np.sinh(t), color="C0", lw=2, label="$x^2 - y^2 = 1$")
ax.plot(-np.cosh(t), np.sinh(t), color="C0", lw=2)
s = np.linspace(0, 2 * np.pi, 300)
ax.plot(np.cos(s), np.sin(s), color="C1", lw=1.5, label="$x^2 + y^2 = 1$")
t0 = 1.0
ts = np.linspace(0, t0, 100)
# the hyperbolic sector has area t0/2, just as the circular sector of angle t0
ax.fill(np.r_[0, np.cosh(ts), 0], np.r_[0, np.sinh(ts), 0], color="C0", alpha=0.25)
ax.plot([np.cosh(t0)], [np.sinh(t0)], "o", color="C0")
ax.annotate("$(\\cosh t, \\sinh t)$", (np.cosh(t0), np.sinh(t0)), xytext=(8, -4),
            textcoords="offset points", fontsize=10)
ax.fill(np.r_[0, np.cos(ts), 0], np.r_[0, np.sin(ts), 0], color="C1", alpha=0.25)
ax.plot([np.cos(t0)], [np.sin(t0)], "o", color="C1")
ax.annotate("$(\\cos t, \\sin t)$", (np.cos(t0), np.sin(t0)), xytext=(-70, 10),
            textcoords="offset points", fontsize=10)
ax.set_xlim(-3, 3.2)
ax.set_ylim(-2.6, 2.6)
ax.set_aspect("equal")
ax.set_title("Shaded sectors both have area $t/2$ ($t = 1$)", fontsize=11)
ax.legend(loc="lower left", fontsize=9)

for ax in axes:
    ax.axhline(0, color="0.8", lw=0.8)
    ax.axvline(0, color="0.8", lw=0.8)
fig.tight_layout()
