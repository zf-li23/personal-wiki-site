"""Isogonal trajectories of the pencil of lines y = Cx: logarithmic spirals and circles."""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 6))
r = np.linspace(0, 3, 10)
for th in np.linspace(0, np.pi, 12, endpoint=False):
    ax.plot(r * np.cos(th), r * np.sin(th), color="0.6", lw=0.9)
    ax.plot(-r * np.cos(th), -r * np.sin(th), color="0.6", lw=0.9)

alpha = np.pi / 3
k = np.tan(alpha)
theta = np.linspace(-12, 6, 3000)
for C in [0.3, 0.6, 1.2]:
    rho = C * np.exp(theta / k)
    keep = rho < 3.2
    ax.plot(rho[keep] * np.cos(theta[keep]), rho[keep] * np.sin(theta[keep]), color="C0", lw=1.6)
ax.plot([], [], color="C0", lw=1.6, label="alpha = pi/3: rho = C exp(theta/k)")
phi = np.linspace(0, 2 * np.pi, 300)
for R in [1.0, 2.0]:
    ax.plot(R * np.cos(phi), R * np.sin(phi), color="C3", lw=1.3, ls="--")
ax.plot([], [], color="C3", ls="--", label="alpha = pi/2: circles")
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Isogonal trajectories of the lines y = Cx")
ax.legend(loc="lower right", fontsize=8)
fig.tight_layout()
