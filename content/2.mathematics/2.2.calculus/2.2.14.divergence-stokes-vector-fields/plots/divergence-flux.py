import numpy as np
import matplotlib.pyplot as plt

# Left: a source at (-1, 0) and a sink at (1, 0); right: the divergence-free field (x, -y)
g = np.linspace(-2.5, 2.5, 300)
X, Y = np.meshgrid(g, g)


def point_field(x0, q):
    dx, dy = X - x0, Y
    r2 = dx**2 + dy**2
    return q * dx / r2, q * dy / r2


U1, V1 = point_field(-1.0, 1.0)
U2, V2 = point_field(1.0, -1.0)
U, V = U1 + U2, V1 + V2

fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
ax = axes[0]
ax.streamplot(X, Y, U, V, color="tab:gray", density=1.3, linewidth=0.8, arrowsize=0.9)
s = np.linspace(0, 2 * np.pi, 200)
for (cx, color, label) in [(-1.0, "tab:red", "source: div > 0"), (1.0, "tab:blue", "sink: div < 0")]:
    rad = 0.45
    ax.plot(cx + rad * np.cos(s), rad * np.sin(s), color=color, lw=2, label=label)
    for a in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        px, py = cx + rad * np.cos(a), rad * np.sin(a)
        ax.annotate("", xy=(px + 0.35 * np.cos(a), py + 0.35 * np.sin(a)), xytext=(px, py),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.4))
ax.plot([-1, 1], [0, 0], "o", color="tab:orange", ms=6)
ax.text(-1, -0.95, "outward flux = +2 pi", ha="center", color="tab:red", fontsize=10)
ax.text(1, -0.95, "outward flux = -2 pi", ha="center", color="tab:blue", fontsize=10)
ax.set_title("Source and sink: outward normals n on small circles")
ax.legend(loc="upper right", fontsize=9)

ax = axes[1]
ax.streamplot(X, Y, X, -Y, color="tab:gray", density=1.2, linewidth=0.8, arrowsize=0.9)
sq = np.array([[0.5, 0.5], [1.5, 0.5], [1.5, 1.5], [0.5, 1.5], [0.5, 0.5]])
ax.plot(sq[:, 0], sq[:, 1], color="tab:green", lw=2)
ax.text(1.0, 1.65, "inflow (top) = outflow (right)", ha="center", color="tab:green", fontsize=10)
ax.set_title("Field (x, -y): div = 0, net flux through any closed curve is 0")
for ax in axes:
    ax.set_aspect("equal")
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
fig.tight_layout()
