"""Schematic of the Cu-Zn (Daniell) galvanic cell with a KCl salt bridge: electrode reactions,
direction of electron flow in the external circuit and of ion migration in the salt bridge."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

fig, ax = plt.subplots(figsize=(9, 5.2))
ax.set_xlim(0, 10)
ax.set_ylim(-1.0, 6.7)
ax.set_aspect("equal")
ax.axis("off")


def beaker(x0, label, sol_color):
    ax.add_patch(Rectangle((x0, 0.6), 3.0, 2.4, facecolor=sol_color, alpha=0.25, edgecolor="none"))
    ax.plot([x0, x0, x0 + 3.0, x0 + 3.0], [3.4, 0.6, 0.6, 3.4], color="black", lw=1.6)
    ax.text(x0 + 1.5, 0.25, label, ha="center", va="center", fontsize=10)


beaker(0.6, r"1 mol L$^{-1}$ ZnSO$_4$(aq)", "C0")
beaker(6.4, r"1 mol L$^{-1}$ CuSO$_4$(aq)", "C0")

# electrodes
ax.add_patch(Rectangle((1.6, 1.0), 0.35, 3.4, facecolor="0.65", edgecolor="black", lw=1))
ax.add_patch(Rectangle((8.05, 1.0), 0.35, 3.4, facecolor="C1", alpha=0.8, edgecolor="black", lw=1))
ax.text(1.78, 4.65, "Zn, anode (−)", ha="center", fontsize=10.5, weight="bold")
ax.text(8.22, 4.65, "Cu, cathode (+)", ha="center", fontsize=10.5, weight="bold")

# salt bridge (inverted U)
for off in (0.0, 0.45):
    ax.plot([3.0 + off, 3.0 + off, 7.0 - off, 7.0 - off],
            [1.6, 3.9 - off, 3.9 - off, 1.6], color="black", lw=1.3)
ax.text(5.0, 3.05, "salt bridge (KCl in agar)", ha="center", fontsize=9)
ax.annotate("", xy=(3.22, 1.9), xytext=(3.22, 3.1),
            arrowprops=dict(arrowstyle="-|>", color="C2", lw=1.4))
ax.text(3.6, 2.3, r"Cl$^-$", color="C2", fontsize=10)
ax.annotate("", xy=(6.78, 1.9), xytext=(6.78, 3.1),
            arrowprops=dict(arrowstyle="-|>", color="C3", lw=1.4))
ax.text(6.05, 2.3, r"K$^+$", color="C3", fontsize=10)

# external circuit with a voltmeter
ax.plot([1.78, 1.78, 4.55], [4.4, 5.9, 5.9], color="black", lw=1.3)
ax.plot([5.45, 8.22, 8.22], [5.9, 5.9, 4.4], color="black", lw=1.3)
ax.add_patch(plt.Circle((5.0, 5.9), 0.45, facecolor="none", edgecolor="black", lw=1.3))
ax.text(5.0, 5.9, "V", ha="center", va="center", fontsize=12)
ax.add_patch(FancyArrowPatch((2.4, 6.25), (4.2, 6.25), arrowstyle="-|>", mutation_scale=14, color="C0", lw=1.5))
ax.add_patch(FancyArrowPatch((5.8, 6.25), (7.6, 6.25), arrowstyle="-|>", mutation_scale=14, color="C0", lw=1.5))
ax.text(3.3, 6.4, r"e$^-$", color="C0", fontsize=11, ha="center")
ax.text(6.7, 6.4, r"e$^-$", color="C0", fontsize=11, ha="center")

# electrode reactions
ax.text(2.1, -0.2, r"oxidation: $\mathrm{Zn \to Zn^{2+} + 2e^-}$", fontsize=10, ha="center")
ax.text(7.9, -0.2, r"reduction: $\mathrm{Cu^{2+} + 2e^- \to Cu}$", fontsize=10, ha="center")
ax.text(5.0, -0.75, r"cell: $\mathrm{Zn(s)\,|\,Zn^{2+}(aq)\,\Vert\,Cu^{2+}(aq)\,|\,Cu(s)}$,  $E^\circ_\mathrm{cell} = 1.10$ V",
        ha="center", fontsize=10)
fig.tight_layout()
