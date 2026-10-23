"""The six vibrations of a CH2 group (typical wavenumbers of a long methylene chain).
In-plane motions are drawn as arrows; out-of-plane motions as + (towards the viewer)
and - (away from the viewer)."""

import numpy as np
import matplotlib.pyplot as plt

C = np.array([0.0, 0.0])
half = np.radians(54)  # half of the H-C-H angle as drawn
H1 = np.array([-np.sin(half), np.cos(half)])
H2 = np.array([np.sin(half), np.cos(half)])
R1 = np.array([-0.95, -0.55])  # bonds to the rest of the chain
R2 = np.array([0.95, -0.55])


def unit(v):
    return v / np.linalg.norm(v)


def frame(ax, title, sub):
    for R in (R1, R2):
        ax.plot([C[0], R[0]], [C[1], R[1]], color="0.55", lw=2, zorder=1)
    for H in (H1, H2):
        ax.plot([C[0], H[0]], [C[1], H[1]], color="k", lw=2, zorder=1)
        ax.add_patch(plt.Circle(H, 0.13, facecolor="C0", edgecolor="k", lw=1, zorder=3))
    ax.add_patch(plt.Circle(C, 0.2, facecolor="0.4", edgecolor="k", lw=1, zorder=3))
    ax.text(C[0], C[1], "C", ha="center", va="center", fontsize=9, color="w", zorder=4)
    ax.set_title(title, fontsize=10)
    ax.text(0, -1.05, sub, ha="center", fontsize=9)
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.25, 1.55)
    ax.set_aspect("equal")
    ax.axis("off")


def arrow(ax, start, vec, color="C3"):
    ax.annotate("", xy=start + vec, xytext=start,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8), zorder=5)


fig, axes = plt.subplots(2, 3, figsize=(9.6, 6.2))
L = 0.38

ax = axes[0, 0]
frame(ax, "symmetric stretch", r"$\nu_{\mathrm{s}}$  ~2850 cm$^{-1}$")
arrow(ax, H1, L * unit(H1))
arrow(ax, H2, L * unit(H2))

ax = axes[0, 1]
frame(ax, "antisymmetric stretch", r"$\nu_{\mathrm{as}}$  ~2925 cm$^{-1}$")
arrow(ax, H1, L * unit(H1))
arrow(ax, H2, -L * unit(H2))

perp1 = np.array([H1[1], -H1[0]])  # perpendicular to C-H1, pointing towards H2
perp2 = np.array([-H2[1], H2[0]])  # perpendicular to C-H2, pointing towards H1

ax = axes[0, 2]
frame(ax, "scissoring (in-plane bend)", r"$\delta$  ~1465 cm$^{-1}$")
arrow(ax, H1, L * unit(perp1))
arrow(ax, H2, L * unit(perp2))

ax = axes[1, 0]
frame(ax, "rocking (in-plane bend)", r"$\rho$  ~720 cm$^{-1}$")
arrow(ax, H1, L * unit(perp1))
arrow(ax, H2, -L * unit(perp2))


def sign(ax, H, s):
    ax.text(H[0] + (0.27 if H[0] > 0 else -0.27), H[1] + 0.12, s, ha="center",
            va="center", fontsize=15, color="C3", fontweight="bold")


ax = axes[1, 1]
frame(ax, "wagging (out-of-plane bend)", r"$\omega$  ~1300 cm$^{-1}$")
sign(ax, H1, "+")
sign(ax, H2, "+")

ax = axes[1, 2]
frame(ax, "twisting (out-of-plane bend)", r"$\tau$  ~1250 cm$^{-1}$")
sign(ax, H1, "+")
sign(ax, H2, "−")

fig.tight_layout()
