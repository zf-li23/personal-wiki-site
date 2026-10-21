"""Energy levels of hydrogen and the first spectral series."""

import numpy as np
import matplotlib.pyplot as plt

E1 = -13.606  # eV
fig, ax = plt.subplots(figsize=(9, 5.2))

nmax = 7
for n in range(1, nmax + 1):
    E = E1 / n**2
    ax.plot([0, 10], [E, E], color="0.35", lw=1.0)
    if n <= 4:
        ax.text(10.15, E, f"n = {n}", va="center", fontsize=8)
    if n <= 4:
        ax.text(-0.15, E, f"{E:.2f}", va="center", ha="right", fontsize=8)
ax.plot([0, 10], [0, 0], color="0.35", lw=1.0, ls="--")
ax.text(10.15, -0.25, r"n = 5, 6, 7, ...", va="center", fontsize=8)
ax.text(10.15, 0.4, r"n = $\infty$", va="center", fontsize=8)
ax.text(-0.15, 0, "0", va="center", ha="right", fontsize=8)

series = [("Lyman (UV)", 1, 0.6), ("Balmer (visible)", 2, 3.4), ("Paschen (IR)", 3, 6.2), ("Brackett (IR)", 4, 8.4)]
for i, (name, nf, x0) in enumerate(series):
    Ef = E1 / nf**2
    for j, ni in enumerate(range(nf + 1, nf + 5)):
        Ei = E1 / ni**2
        x = x0 + 0.38 * j
        ax.annotate("", xy=(x, Ef), xytext=(x, Ei),
                    arrowprops=dict(arrowstyle="-|>", color=f"C{i}", lw=1.2, shrinkA=0, shrinkB=0))
    ax.text(x0 + 0.55, Ef - 0.55, name, ha="center", va="top", fontsize=8.5, color=f"C{i}")

ax.set_xlim(-1.3, 11.3)
ax.set_ylim(-14.8, 1.0)
ax.set_xticks([])
ax.set_ylabel("E / eV")
ax.set_title(r"Hydrogen: $E_n = -13.6\,\mathrm{eV}/n^2$ and the spectral series")
for s in ["top", "right", "bottom"]:
    ax.spines[s].set_visible(False)

fig.tight_layout()
