import numpy as np
import matplotlib.pyplot as plt

# A letter "F" inside the unit square: its image shows whether orientation is kept
F = np.array([[0.3, 0.15], [0.3, 0.85], [0.7, 0.85], [0.7, 0.72], [0.43, 0.72],
              [0.43, 0.56], [0.62, 0.56], [0.62, 0.43], [0.43, 0.43], [0.43, 0.15], [0.3, 0.15]])
square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]], dtype=float)

cases = [
    ("shear", np.array([[1.0, 0.0], [1.0, 1.0]])),
    ("stretch", np.array([[2.0, 0.0], [0.0, 1.0]])),
    ("swap (reflection)", np.array([[0.0, 1.0], [1.0, 0.0]])),
    ("general", np.array([[2.0, 1.0], [0.5, 1.5]])),
]

fig, axes = plt.subplots(1, 4, figsize=(13, 3.9))
for ax, (name, A) in zip(axes, cases):
    img = square @ A.T
    ax.fill(square[:, 0], square[:, 1], color="gray", alpha=0.12)
    ax.plot(square[:, 0], square[:, 1], color="gray", lw=1, ls="--")
    ax.fill(img[:, 0], img[:, 1], color="C0", alpha=0.25)
    ax.plot(img[:, 0], img[:, 1], color="C0", lw=1.5)
    ax.fill(F[:, 0], F[:, 1], color="gray", alpha=0.35)
    Fi = F @ A.T
    ax.fill(Fi[:, 0], Fi[:, 1], color="C3", alpha=0.8)
    for col, color, label in [(A[:, 0], "C1", r"$A\boldsymbol{e}_1$"), (A[:, 1], "C2", r"$A\boldsymbol{e}_2$")]:
        ax.annotate("", xy=col, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=2, mutation_scale=12))
        ax.text(col[0] + 0.06, col[1] + 0.06, label, color=color, fontsize=10)
    ax.set_title(f"{name}: det A = {np.linalg.det(A):.3g}", fontsize=11)
    ax.set_aspect("equal")
    ax.set_xlim(-0.3, 3.3)
    ax.set_ylim(-0.3, 2.5)
    ax.grid(True, alpha=0.3)
fig.tight_layout()
