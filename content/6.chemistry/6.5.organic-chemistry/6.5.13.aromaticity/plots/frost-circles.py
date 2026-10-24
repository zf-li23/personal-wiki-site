"""Frost circles for n = 3 to 8: a regular n-gon inscribed in a circle of radius 2|beta| centred on
E = alpha, with one vertex at the bottom; the vertex heights are the Hueckel levels
alpha + 2 beta cos(2 pi k / n). Dots: the electron count that makes each ring aromatic
(C3H3+ 2, C4H4 2+ 2, C5H5- 6, C6H6 6, C7H7+ 6, C8H8 2- 10)."""

import numpy as np
import matplotlib.pyplot as plt

ink = plt.rcParams["text.color"]
cases = [(3, 2, r"C$_3$H$_3^+$"), (4, 2, r"C$_4$H$_4^{2+}$"), (5, 6, r"C$_5$H$_5^-$"),
         (6, 6, r"C$_6$H$_6$"), (7, 6, r"C$_7$H$_7^+$"), (8, 10, r"C$_8$H$_8^{2-}$")]
fig, axes = plt.subplots(1, 6, figsize=(11, 3.4), sharey=True)
t = np.linspace(0, 2 * np.pi, 200)
for ax, (n, electrons, name) in zip(axes, cases):
    ax.plot(2 * np.cos(t), 2 * np.sin(t), color="0.6", lw=0.8)
    ang = -np.pi / 2 + 2 * np.pi * np.arange(n + 1) / n
    vx, vy = 2 * np.cos(ang), 2 * np.sin(ang)
    ax.plot(vx, vy, color="C0", lw=1.5)
    ax.axhline(0, color="0.6", lw=0.6, ls="--")
    remaining = electrons
    order = np.argsort(vy[:n], kind="stable")
    for k in order:
        occ = min(2, remaining)
        remaining -= occ
        for q in range(occ):
            ax.plot(vx[k] + (q - 0.5) * 0.32, vy[k], "o", ms=3.5, color=ink, zorder=3)
    ax.set_title(f"n = {n}\n{name}", fontsize=9)
    ax.set_aspect("equal")
    ax.set_xlim(-2.6, 2.6)
    ax.set_ylim(-2.6, 2.6)
    ax.set_xticks([])
    for side in ("top", "right", "bottom"):
        ax.spines[side].set_visible(False)
    if ax is not axes[0]:
        ax.spines["left"].set_visible(False)
        ax.tick_params(left=False)
axes[0].set_yticks([-2, -1, 0, 1, 2])
axes[0].set_ylabel(r"$(E - \alpha)/|\beta|$")
fig.tight_layout()
