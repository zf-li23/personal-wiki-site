"""Minkowski diagram (c = 1): axes of a frame S' moving at v = 0.5c, light cone, lines of simultaneity."""

import numpy as np
import matplotlib.pyplot as plt

beta = 0.5
gamma = 1 / np.sqrt(1 - beta ** 2)

fig, ax = plt.subplots(figsize=(6.0, 5.0))
R = 3.0
s = np.linspace(-R, R, 2)

# S axes
ax.axhline(0, color="0.35", lw=1.0)
ax.axvline(0, color="0.35", lw=1.0)
ax.text(R - 0.1, -0.25, "x", fontsize=11, ha="right")
ax.text(0.1, R - 0.2, "ct", fontsize=11)

# light cone
ax.plot(s, s, color="C1", ls="--", lw=1.2)
ax.plot(s, -s, color="C1", ls="--", lw=1.2)
ax.text(1.75, 2.15, "x = ct", color="C1", fontsize=9, rotation=45)

# S' axes: ct' axis is x = beta ct, x' axis is ct = beta x
ax.plot(beta * s, s, color="C0", lw=1.8)
ax.plot(s, beta * s, color="C0", lw=1.8)
ax.text(beta * R + 0.05, R - 0.2, "ct'", color="C0", fontsize=11)
ax.text(R - 0.1, beta * R + 0.1, "x'", color="C0", fontsize=11, ha="right")

# lines of simultaneity in S' (t' = const) are parallel to the x' axis
for tp in [0.8, 1.6]:
    # event (x', t') = (xp, tp) maps to x = gamma (xp + beta tp), ct = gamma (tp + beta xp)
    xp = np.linspace(-4, 4, 2)
    ax.plot(gamma * (xp + beta * tp), gamma * (tp + beta * xp), color="C0", lw=0.8, ls=":")
    xl = -1.4
    xpl = xl / gamma - beta * tp
    ax.text(xl + 0.05, gamma * (tp + beta * xpl) + 0.08, f"t' = {tp}", color="C0", fontsize=8)

# two events simultaneous in S' (t' = 0.8) at x' = 0.4 and x' = 1.8
tp = 0.8
for name, xp in [("P1", 0.4), ("P2", 1.8)]:
    x, ct = gamma * (xp + beta * tp), gamma * (tp + beta * xp)
    ax.plot([x], [ct], "o", color="C3", ms=6)
    ax.text(x + 0.08, ct - 0.25, name, color="C3", fontsize=10)
    ax.plot([-1.5, x], [ct, ct], color="C3", lw=0.6, ls="-.")
    ax.text(-0.75, ct + 0.05, f"ct = {ct:.2f}", color="C3", fontsize=8)

ax.set_xlim(-1.5, R)
ax.set_ylim(-0.5, R)
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Minkowski diagram, v = 0.5c")
fig.tight_layout()
