"""Beats from two equal-amplitude oscillations with nearby frequencies."""

import numpy as np
import matplotlib.pyplot as plt

nu1, nu2 = 10.0, 11.0
t = np.linspace(0, 2.0, 4000)
x1 = np.cos(2 * np.pi * nu1 * t)
x2 = np.cos(2 * np.pi * nu2 * t)
env = 2 * np.abs(np.cos(np.pi * (nu2 - nu1) * t))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 5), sharex=True)
ax1.plot(t, x1, lw=1.2, label="x1, nu1 = 10 Hz")
ax1.plot(t, x2, lw=1.2, label="x2, nu2 = 11 Hz", alpha=0.8)
ax1.set_ylabel("x / A")
ax1.set_ylim(-1.4, 1.9)
ax1.legend(loc="upper right", ncol=2, fontsize=9)

ax2.plot(t, x1 + x2, color="C2", lw=1.2, label="x1 + x2")
ax2.plot(t, env, color="0.4", ls="--", lw=1)
ax2.plot(t, -env, color="0.4", ls="--", lw=1)
ax2.set_xlabel("t / s")
ax2.set_ylabel("x / A")
ax2.set_title("beat period 1 / |nu1 - nu2| = 1 s", fontsize=10)
ax2.set_xlim(0, 2)
fig.tight_layout()
