"""Jablonski diagram: singlet states S0, S1, S2 and triplet T1, T2 with vibrational levels;
absorption, vibrational relaxation, internal conversion, intersystem crossing,
fluorescence and phosphorescence, with typical time scales."""

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9, 5.6))
states = {"S0": (0.0, 0.0), "S1": (0.0, 4.0), "S2": (0.0, 6.0), "T1": (4.2, 3.0), "T2": (4.2, 5.4)}
for name, (x0, e) in states.items():
    for v in range(5):
        lw = 1.6 if v == 0 else 0.6
        ax.plot([x0, x0 + 2.6], [e + 0.22 * v] * 2, color="0.2" if v == 0 else "0.55", lw=lw)
    ax.text(x0 - 0.15, e, name.replace("0", r"$_0$").replace("1", r"$_1$").replace("2", r"$_2$"),
            ha="right", va="center", fontsize=11)


def arrow(x0, y0, x1, y1, color, style="-|>", ls="-"):
    ax.annotate("", (x1, y1), (x0, y0), arrowprops=dict(arrowstyle=style, color=color, lw=1.4, ls=ls))


arrow(0.3, 0.0, 0.3, 4.66, "C0")
arrow(0.6, 0.0, 0.6, 6.66, "C0")
ax.text(0.45, 2.0, "absorption\n$10^{-15}$ s", color="C0", fontsize=8, ha="center", rotation=90, va="center")
arrow(1.0, 4.66, 1.0, 4.04, "C2")
arrow(1.0, 6.66, 1.0, 6.04, "C2")
ax.text(1.12, 6.4, "vibrational relaxation\n$10^{-12}$ s", color="C2", fontsize=8, va="center")
arrow(1.4, 6.0, 1.4, 4.85, "C4", ls="--")
ax.text(1.52, 5.4, "internal conversion", color="C4", fontsize=8, va="center")
arrow(1.6, 4.0, 1.6, 0.0, "C3")
ax.text(1.72, 1.6, "fluorescence\n$10^{-9}$-$10^{-6}$ s", color="C3", fontsize=8)
arrow(2.4, 4.0, 4.5, 3.88, "C1", ls="--")
ax.text(3.15, 4.05, "intersystem\ncrossing", color="C1", fontsize=8, ha="center")
arrow(5.6, 3.0, 5.6, 0.0, "C5")
ax.text(5.72, 1.4, "phosphorescence\n$10^{-4}$ s to s", color="C5", fontsize=8)
arrow(4.7, 3.0, 2.3, 0.66, "C1", ls="--")
ax.text(3.55, 1.3, "ISC", color="C1", fontsize=8, ha="center")
ax.set_xlim(-0.8, 7.6)
ax.set_ylim(-0.4, 7.4)
ax.axis("off")
fig.tight_layout()
