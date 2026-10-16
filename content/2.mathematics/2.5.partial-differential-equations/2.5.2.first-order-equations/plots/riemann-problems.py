"""Riemann problems for Burgers' equation: a shock and a rarefaction fan."""

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.2))
T = 2.0

# shock: u_l = 1, u_r = 0, speed 1/2
for x0 in np.arange(-3, 0, 0.25):
    t_hit = -2 * x0  # x0 + t = t/2
    t_end = min(t_hit, T)
    ax1.plot([x0, x0 + t_end], [0, t_end], color="C0", lw=0.9)
for x0 in np.arange(0.25, 3.01, 0.25):
    t_end = min(2 * x0, T)
    ax1.plot([x0, x0], [0, t_end], color="C2", lw=0.9)
ax1.plot([0, T / 2], [0, T], color="C3", lw=2.2, label="shock x = t/2")
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(0, T)
ax1.set_xlabel("x")
ax1.set_ylabel("t")
ax1.set_title("u_l = 1, u_r = 0: shock")
ax1.legend(loc="upper left", fontsize=9)

# rarefaction: u_l = 0, u_r = 1
for x0 in np.arange(-3, 0.01, 0.25):
    ax2.plot([x0, x0], [0, T], color="C0", lw=0.9)
for x0 in np.arange(0.0, 3.01, 0.25):
    ax2.plot([x0, x0 + T], [0, T], color="C2", lw=0.9)
for slope in np.linspace(0.1, 0.9, 9):
    ax2.plot([0, slope * T], [0, T], color="C1", lw=0.9)
ax2.plot([], [], color="C1", label="fan u = x/t")
ax2.set_xlim(-2.5, 2.5)
ax2.set_ylim(0, T)
ax2.set_xlabel("x")
ax2.set_ylabel("t")
ax2.set_title("u_l = 0, u_r = 1: rarefaction wave")
ax2.legend(loc="upper left", fontsize=9)

fig.tight_layout()
