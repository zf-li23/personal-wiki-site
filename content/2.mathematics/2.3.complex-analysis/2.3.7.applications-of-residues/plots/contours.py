"""Three standard contours: the closed upper semicircle (Jordan's lemma),
the semicircle indented at a pole on the real axis, and the keyhole contour
around a branch cut along the positive real axis."""

import numpy as np
import matplotlib.pyplot as plt


def arrow_along(ax, xs, ys, i, color):
    ax.annotate("", xy=(xs[i + 1], ys[i + 1]), xytext=(xs[i], ys[i]),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.6, mutation_scale=16))


def frame(ax, title):
    ax.axhline(0, color="gray", lw=0.6)
    ax.axvline(0, color="gray", lw=0.6)
    ax.set_aspect("equal")
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.35, 1.35)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title)


fig, axes = plt.subplots(1, 3, figsize=(15, 5.2))
c = "C0"
R = 1.0

# (a) upper semicircle
ax = axes[0]
frame(ax, "(a) semicircle: Jordan's lemma")
t = np.linspace(0, np.pi, 200)
ax.plot([-R, R], [0, 0], color=c, lw=2)
ax.plot(R * np.cos(t), R * np.sin(t), color=c, lw=2)
arrow_along(ax, np.array([-0.2, 0.2]), np.array([0, 0]), 0, c)
arrow_along(ax, R * np.cos(t), R * np.sin(t), 60, c)
for p in (0.3 + 0.45j, -0.5 + 0.3j):
    ax.plot(p.real, p.imag, "rx", ms=9, mew=2)
ax.plot(0.4, -0.5, "x", color="gray", ms=9, mew=2)
ax.text(0.62, 0.9, r"$C_R$", fontsize=13)
ax.text(-1.25, -0.2, r"$-R$", fontsize=12)
ax.text(1.0, -0.2, r"$R$", fontsize=12)

# (b) indented semicircle
ax = axes[1]
frame(ax, "(b) indentation at a pole on the axis")
eps = 0.18
ax.plot([-R, -eps], [0, 0], color=c, lw=2)
ax.plot([eps, R], [0, 0], color=c, lw=2)
ts = np.linspace(np.pi, 0, 100)
ax.plot(eps * np.cos(ts), eps * np.sin(ts), color=c, lw=2)
ax.plot(R * np.cos(t), R * np.sin(t), color=c, lw=2)
arrow_along(ax, np.array([-0.7, -0.5]), np.array([0, 0]), 0, c)
arrow_along(ax, np.array([0.5, 0.7]), np.array([0, 0]), 0, c)
arrow_along(ax, eps * np.cos(ts), eps * np.sin(ts), 40, c)
arrow_along(ax, R * np.cos(t), R * np.sin(t), 60, c)
ax.plot(0, 0, "rx", ms=9, mew=2)
ax.plot(0.4 + 0, 0.55, "rx", ms=9, mew=2)
ax.text(-0.12, 0.25, r"$C_\varepsilon$", fontsize=13)
ax.text(0.62, 0.9, r"$C_R$", fontsize=13)

# (c) keyhole
ax = axes[2]
frame(ax, "(c) keyhole around a branch cut")
d = 0.06
rs, Rb = 0.2, 1.0
a1, a2 = np.arcsin(d / Rb), np.arcsin(d / rs)
tb = np.linspace(a1, 2 * np.pi - a1, 300)
tsm = np.linspace(2 * np.pi - a2, a2, 200)
ax.plot([np.sqrt(rs**2 - d**2), np.sqrt(Rb**2 - d**2)], [d, d], color=c, lw=2)
ax.plot([np.sqrt(Rb**2 - d**2), np.sqrt(rs**2 - d**2)], [-d, -d], color=c, lw=2)
ax.plot(Rb * np.cos(tb), Rb * np.sin(tb), color=c, lw=2)
ax.plot(rs * np.cos(tsm), rs * np.sin(tsm), color=c, lw=2)
arrow_along(ax, np.array([0.45, 0.6]), np.array([d, d]), 0, c)
arrow_along(ax, np.array([0.6, 0.45]), np.array([-d, -d]), 0, c)
arrow_along(ax, Rb * np.cos(tb), Rb * np.sin(tb), 100, c)
arrow_along(ax, rs * np.cos(tsm), rs * np.sin(tsm), 60, c)
ax.plot([0, 1.3], [0, 0], color="C3", lw=3, alpha=0.5, label="branch cut")
ax.plot(-0.5, 0.0, "rx", ms=9, mew=2)
ax.legend(loc="lower left")
fig.tight_layout()
