"""First-order splitting of an ethyl group (J = 7.0 Hz): the CH3 signal is split by the two
CH2 protons into a 1:2:1 triplet, the CH2 signal by the three CH3 protons into a 1:3:3:1
quartet. Splitting trees above, the resulting multiplets below (Lorentzian lines, 0.8 Hz wide)."""

import numpy as np
import matplotlib.pyplot as plt
from math import comb

J = 7.0
fig, axes = plt.subplots(1, 2, figsize=(10, 4.8))


def tree(ax, n, title):
    pos = [0.0]
    levels = [pos]
    for k in range(n):
        new = []
        for p in pos:
            new += [p - J / 2, p + J / 2]
        pos = new
        levels.append(pos)
    for k in range(n):
        y0, y1 = 3.25 - k * 0.45, 3.25 - (k + 1) * 0.45
        for p in levels[k]:
            for q in (p - J / 2, p + J / 2):
                ax.plot([p, q], [y0, y1], color="C0", lw=1.0)
    ax.text(0, 3.4, title, ha="center", fontsize=10)
    x = np.linspace(-20, 20, 4001)
    y = np.zeros_like(x)
    w = 0.8
    for m in range(n + 1):
        c = (m - n / 2) * J
        y += comb(n, m) * (w / 2)**2 / ((x - c)**2 + (w / 2)**2)
    base = 0.0
    ax.plot(x, base + 1.3 * y / comb(n, n // 2), color="k", lw=1.2)
    for m in range(n + 1):
        c = (m - n / 2) * J
        ax.text(c, 1.3 * comb(n, m) / comb(n, n // 2) + 0.06, str(comb(n, m)),
                ha="center", fontsize=9)
    ya = 1.62
    ax.annotate("", xy=(-n / 2 * J + J, ya), xytext=(-n / 2 * J, ya),
                arrowprops=dict(arrowstyle="<->", color="C3", lw=1.0))
    ax.text(-n / 2 * J + J / 2, ya + 0.07, "$J$", ha="center", color="C3", fontsize=9)
    ax.set_xlim(-16, 16)
    ax.set_ylim(-0.05, 3.65)
    ax.set_yticks([])
    ax.set_xlabel("frequency offset from the chemical shift / Hz")


tree(axes[0], 2, "CH$_3$ coupled to CH$_2$ (n = 2): triplet")
tree(axes[1], 3, "CH$_2$ coupled to CH$_3$ (n = 3): quartet")
fig.tight_layout()
