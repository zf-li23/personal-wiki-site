"""Images of a grid and of the unit square under six linear maps of the plane."""

import numpy as np
import matplotlib.pyplot as plt

theta = np.pi / 6
maps = [
    ("Rotation $R_{\\pi/6}$", np.array([[np.cos(theta), -np.sin(theta)],
                                         [np.sin(theta), np.cos(theta)]])),
    ("Reflection $H_{\\pi/6}$", np.array([[np.cos(2 * theta), np.sin(2 * theta)],
                                           [np.sin(2 * theta), -np.cos(2 * theta)]])),
    ("Stretch diag(1.5, 0.5)", np.diag([1.5, 0.5])),
    ("Shear $S_1$", np.array([[1.0, 1.0], [0.0, 1.0]])),
    ("Projection diag(1, 0)", np.diag([1.0, 0.0])),
    ("General matrix", np.array([[1.0, 0.5], [-0.5, 1.2]])),
]

ticks = np.linspace(-1, 1, 5)
t = np.linspace(-1, 1, 50)
square = np.array([[0, 1, 1, 0, 0], [0, 0, 1, 1, 0]], dtype=float)

fig, axes = plt.subplots(2, 3, figsize=(10, 6.6))
for ax, (title, A) in zip(axes.flat, maps):
    # original grid (faint) and its image
    for c in ticks:
        for line in (np.vstack([t, np.full_like(t, c)]), np.vstack([np.full_like(t, c), t])):
            ax.plot(*line, color="0.75", lw=0.6)
            ax.plot(*(A @ line), color="C0", lw=0.9)
    ax.fill(*square, color="0.6", alpha=0.25)
    ax.fill(*(A @ square), color="C1", alpha=0.45)
    # images of the standard coordinate vectors
    for k, name in enumerate(["$Ae_1$", "$Ae_2$"]):
        v = A[:, k]
        if np.allclose(v, 0):
            continue
        ax.annotate("", xy=v, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="->", color="C3", lw=1.6))
        ax.text(v[0] * 1.08, v[1] * 1.08 + 0.05, name, color="C3", fontsize=10)
    ax.set_title(title, fontsize=11)
    ax.set_aspect("equal")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.7, 1.7)
    ax.set_xticks([])
    ax.set_yticks([])
fig.tight_layout()
