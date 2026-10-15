import numpy as np
import matplotlib.pyplot as plt

# Maximize / minimize f = xy on the circle (x - 1)^2 + y^2 = 1
g = np.linspace(-0.5, 2.5, 401)
X, Y = np.meshgrid(g, np.linspace(-1.5, 1.5, 401))
F = X * Y

fig, ax = plt.subplots(figsize=(7.5, 6))
fmax = 3 * np.sqrt(3) / 4
levels = [-1.6, -fmax, -0.8, -0.4, 0.4, 0.8, fmax, 1.6]
cs = ax.contour(X, Y, F, levels=levels, cmap="coolwarm", linewidths=1.0)
ax.clabel(cs, fmt="%.2f", fontsize=7)
t = np.linspace(0, 2 * np.pi, 400)
ax.plot(1 + np.cos(t), np.sin(t), color="tab:green", lw=2.5, label="constraint g = 0")

for s, color in [(1, "tab:red"), (-1, "tab:blue")]:
    px, py = 1.5, s * np.sqrt(3) / 2
    ax.plot(px, py, "o", color=color, ms=8)
    gf = np.array([py, px])
    gg = np.array([2 * (px - 1), 2 * py])
    gf, gg = 0.5 * gf / np.linalg.norm(gf), 0.5 * gg / np.linalg.norm(gg)
    ax.annotate("", xy=(px + 1.4 * gg[0], py + 1.4 * gg[1]), xytext=(px, py),
                arrowprops=dict(arrowstyle="->", color="tab:green", lw=2))
    ax.annotate("", xy=(px + 0.7 * gf[0], py + 0.7 * gf[1]), xytext=(px, py),
                arrowprops=dict(arrowstyle="->", color="tab:purple", lw=2.5))
    label = "max 3 sqrt(3)/4" if s > 0 else "min -3 sqrt(3)/4"
    ax.text(px + 0.3, py - 0.05, label, color=color, fontsize=9)

ax.plot([], [], color="tab:purple", lw=2, label="grad f")
ax.plot([], [], color="tab:green", lw=2, label="grad g (parallel to grad f)")
ax.set_aspect("equal")
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Level curves of f = xy touch the constraint at the extrema")
ax.legend(loc="lower left", fontsize=8)
fig.tight_layout()
