"""Cosets and the quotient group (Sections 2.5 and 2.6). A: the subgroup H = {0, 3} of Z_6 splits Z_6
into three cosets H, 1 + H, 2 + H of equal size (each colour is one coset), so |Z_6| = [Z_6 : H] |H|,
6 = 3 x 2, as Lagrange's theorem requires. B: the cosets added as sets form the quotient group
Z_6/H, whose table is that of Z_3."""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(9.6, 4.4))
ax = fig.add_axes([0.02, 0.05, 0.42, 0.9])
ang = np.pi / 2 - 2 * np.pi * np.arange(6) / 6
x, y = np.cos(ang), np.sin(ang)
ax.plot(np.append(x, x[0]), np.append(y, y[0]), color="0.75", lw=1.0)
for k in range(6):
    c = f"C{k % 3}"
    ax.text(x[k], y[k], f"${k}$", ha="center", va="center", fontsize=15,
            bbox=dict(boxstyle="circle,pad=0.35", fc=c, alpha=0.3, ec=c, lw=1.5))
for k in range(3):
    ax.plot([x[k], x[k + 3]], [y[k], y[k + 3]], color=f"C{k}", lw=2, alpha=0.6)
cosets = [r"$H = \{0, 3\}$", r"$1 + H = \{1, 4\}$", r"$2 + H = \{2, 5\}$"]
for k, s in enumerate(cosets):
    ax.text(1.55, 0.55 - 0.45 * k, s, color=f"C{k}", fontsize=13, va="center")
ax.text(-1.45, 1.35, "A", fontsize=13, weight="bold")
ax.set_xlim(-1.5, 3.4); ax.set_ylim(-1.35, 1.5); ax.set_aspect("equal"); ax.axis("off")

ax = fig.add_axes([0.6, 0.12, 0.36, 0.76])
q = ["H", "1 + H", "2 + H"]
for i in range(3):
    for j in range(3):
        z = (i + j) % 3
        ax.add_patch(plt.Rectangle((j, -i), 1, 1, fc=f"C{z}", alpha=0.3, ec="0.6", lw=0.6))
        ax.text(j + 0.5, -i + 0.5, f"${q[z]}$", ha="center", va="center", fontsize=12)
    ax.text(-0.45, -i + 0.5, f"${q[i]}$", ha="center", va="center", fontsize=12)
    ax.text(i + 0.5, 1.3, f"${q[i]}$", ha="center", va="center", fontsize=12)
ax.text(-0.45, 1.3, "$+$", ha="center", va="center", fontsize=13)
ax.text(-1.0, 1.75, "B", fontsize=13, weight="bold")
ax.text(1.5, -2.6, r"$\mathbb{Z}_6/H \cong \mathbb{Z}_3$", ha="center", fontsize=13)
ax.set_xlim(-1.05, 3.1); ax.set_ylim(-2.9, 2.0); ax.set_aspect("equal"); ax.axis("off")
