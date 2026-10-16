import numpy as np
import matplotlib.pyplot as plt

# Rigid rotation (-y, x) versus the vortex (-y, x) / (x^2 + y^2)
q = np.linspace(-2, 2, 16)
QX, QY = np.meshgrid(q, q)
s = np.linspace(0, 2 * np.pi, 200)

fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
R2 = QX**2 + QY**2
fields = [
    ((-QY, QX), "(-y, x):  rot = 2k everywhere", ["circulation 2 pi r^2", "tab:red"]),
    ((-QY / R2, QX / R2), "(-y, x)/(x^2+y^2):  rot = 0 except at O", ["circulation 2 pi for every r", "tab:purple"]),
]
for ax, ((U, V), title, (txt, color)) in zip(axes, fields):
    M = np.hypot(U, V)
    ax.quiver(QX, QY, U / M, V / M, M, cmap="viridis", angles="xy", pivot="mid", width=0.004, scale=22)
    for r in (0.6, 1.2, 1.8):
        ax.plot(r * np.cos(s), r * np.sin(s), color=color, lw=1.6)
        ax.annotate("", xy=(r * np.cos(0.9), r * np.sin(0.9)), xytext=(r * np.cos(0.8), r * np.sin(0.8)),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.6, mutation_scale=16))
    ax.text(0, -2.35, txt, ha="center", color=color, fontsize=10)
    ax.set_title(title)
    ax.set_aspect("equal")
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.5, 2.2)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
axes[1].plot([0], [0], "x", color="tab:red", ms=10, mew=2)
fig.tight_layout()
