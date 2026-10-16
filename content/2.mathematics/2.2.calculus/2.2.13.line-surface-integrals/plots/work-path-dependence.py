import numpy as np
import matplotlib.pyplot as plt

# Work of two plane fields along three paths from (0, 0) to (1, 1)
t = np.linspace(0, 1, 200)
paths = [(t, t, "y = x"), (t, t**2, "y = x^2"), (t, t**3, "y = x^3")]
colors = ["tab:red", "tab:orange", "tab:purple"]
fields = [
    (lambda x, y: (2 * x * y, x**2), "u = (2xy, x^2)", ["1", "1", "1"]),
    (lambda x, y: (x * y, y - x), "v = (xy, y - x)", ["1/3", "1/12", "-1/20"]),
]

g = np.linspace(-0.1, 1.1, 13)
GX, GY = np.meshgrid(g, g)
fig, axes = plt.subplots(1, 2, figsize=(12, 5.6))
for ax, (F, name, works) in zip(axes, fields):
    U, V = F(GX, GY)
    ax.quiver(GX, GY, U, V, color="tab:gray", angles="xy", scale_units="xy", scale=6, width=0.004, alpha=0.8)
    for (px, py, label), c, w in zip(paths, colors, works):
        ax.plot(px, py, color=c, lw=2.2, label=f"{label}:  W = {w}")
        k = 120
        ax.annotate("", xy=(px[k + 1], py[k + 1]), xytext=(px[k], py[k]),
                    arrowprops=dict(arrowstyle="-|>", color=c, lw=2, mutation_scale=18))
    ax.plot([0, 1], [0, 1], "o", color="tab:blue", ms=6)
    ax.set_xlim(-0.12, 1.12)
    ax.set_ylim(-0.12, 1.12)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"Field {name}")
    ax.legend(loc="upper left", fontsize=9)
fig.suptitle("Work along three paths from (0,0) to (1,1): path-independent for u, path-dependent for v")
fig.tight_layout()
