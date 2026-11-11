"""Firing maps of the four classical spatial cell types (idealized models).

Box: 1 m x 1 m, rate maps on a 100 x 100 grid; colors give firing rate (viridis).
A: place cell: Gaussian field, r = 20 Hz exp(-|x - c|^2 / (2 * 0.1 m^2)), c = (0.35, 0.6) m.
B: grid cell: rectified sum of three plane waves at 60 deg to each other,
   g(x) = sum_k cos(k_k . (x - x0)), |k_k| = 4 pi / (sqrt(3) lambda), lambda = 0.4 m, orientation 7 deg,
   r = 15 Hz * max(0, (g + 1.5) / 4.5)^2 (Formula 42.4.1).
C: head direction cell: von Mises-like tuning r(phi) = 40 Hz exp(4 (cos(phi - 90 deg) - 1)), polar plot.
D: border cell: fires along the east wall, r = 18 Hz exp(-(1 - x) / 0.06 m) for 0.1 < y < 0.9.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
n = 100
xs = np.linspace(0, 1, n)
X, Y = np.meshgrid(xs, xs)
place = 20 * np.exp(-((X - 0.35) ** 2 + (Y - 0.6) ** 2) / (2 * 0.1**2))
lam, ori = 0.4, np.radians(7)
kmag = 4 * np.pi / (np.sqrt(3) * lam)
g = np.zeros_like(X)
for j in range(3):
    a = ori + j * np.pi / 3
    g += np.cos(kmag * (np.cos(a) * (X - 0.2) + np.sin(a) * (Y - 0.3)))
grid = 15 * np.clip((g + 1.5) / 4.5, 0, None) ** 2
border = 18 * np.exp(-(1 - X) / 0.06) * ((Y > 0.1) & (Y < 0.9))

fig = plt.figure(figsize=(13, 3.6))
specs = [(place, "A  Place cell"), (grid, "B  Grid cell"), (None, "C  Head direction cell"), (border, "D  Border cell")]
for k, (m, ttl) in enumerate(specs):
    if m is None:
        ax = fig.add_subplot(1, 4, k + 1, projection="polar")
        phi = np.linspace(0, 2 * np.pi, 361)
        r = 40 * np.exp(4 * (np.cos(phi - np.pi / 2) - 1))
        ax.fill(phi, r, color=P.fill("dna"), alpha=0.6)
        ax.plot(phi, r, color=P.edge("dna"), lw=1.8)
        ax.set_rticks([20, 40])
        ax.set_yticklabels(["20 Hz", "40 Hz"], fontsize=7)
        ax.set_thetagrids([0, 90, 180, 270], ["E", "N", "W", "S"])
        ax.set_title(ttl, loc="left", fontsize=10, pad=14)
        continue
    ax = fig.add_subplot(1, 4, k + 1)
    im = ax.imshow(m, origin="lower", extent=(0, 1, 0, 1), cmap="viridis")
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xlabel("x / m", labelpad=-6)
    ax.set_ylabel("y / m", labelpad=-6)
    cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cb.set_label("Rate / Hz", fontsize=8)
    ax.set_title(ttl, loc="left", fontsize=10)
fig.tight_layout()
