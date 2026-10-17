"""Bertrand's paradox: three ways of drawing a 'random chord' of the unit circle."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n_draw = 120
n_sim = 100000
L = np.sqrt(3.0)


def chords_endpoints(n):
    a = rng.uniform(0, 2 * np.pi, n)
    b = rng.uniform(0, 2 * np.pi, n)
    return np.cos(a), np.sin(a), np.cos(b), np.sin(b)


def chords_from_midpoints(mx, my):
    d = np.hypot(mx, my)
    half = np.sqrt(np.clip(1 - d**2, 0, None))
    ux, uy = -my / np.where(d > 0, d, 1), mx / np.where(d > 0, d, 1)
    return mx - half * ux, my - half * uy, mx + half * ux, my + half * uy


def chords_radius(n):
    theta = rng.uniform(0, 2 * np.pi, n)
    r = rng.uniform(0, 1, n)
    return chords_from_midpoints(r * np.cos(theta), r * np.sin(theta))


def chords_disk(n):
    r = np.sqrt(rng.uniform(0, 1, n))
    theta = rng.uniform(0, 2 * np.pi, n)
    return chords_from_midpoints(r * np.cos(theta), r * np.sin(theta))


methods = [
    ("(1) random endpoints", chords_endpoints, "1/3"),
    ("(2) random point on a radius", chords_radius, "1/2"),
    ("(3) random midpoint in the disk", chords_disk, "1/4"),
]

fig, axes = plt.subplots(1, 3, figsize=(12, 4.4))
phi = np.linspace(0, 2 * np.pi, 400)
for ax, (name, gen, exact) in zip(axes, methods):
    x1, y1, x2, y2 = gen(n_sim)
    long = np.hypot(x2 - x1, y2 - y1) >= L
    for i in range(n_draw):
        ax.plot([x1[i], x2[i]], [y1[i], y2[i]], color="C0" if long[i] else "C1", lw=0.6, alpha=0.7)
    ax.plot(np.cos(phi), np.sin(phi), color="black", lw=1.2)
    ax.set_aspect("equal")
    ax.set_xlim(-1.08, 1.08)
    ax.set_ylim(-1.08, 1.08)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"{name}\nexact {exact}, simulated {long.mean():.3f}", fontsize=10)
axes[0].plot([], [], color="C0", label="length >= sqrt(3)")
axes[0].plot([], [], color="C1", label="length < sqrt(3)")
axes[0].legend(loc="lower left", fontsize=8, bbox_to_anchor=(0, -0.2))
fig.tight_layout()
