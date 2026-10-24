"""Metal-carbonyl bonding (Dewar-Chatt-Duncanson picture for CO). Left: sigma donation, the filled
5-sigma orbital (lone pair on carbon) overlaps an empty metal d-sigma orbital. Right: pi
back-donation, a filled metal d-pi orbital overlaps the empty pi* orbital of CO, which has its
larger lobes on carbon. Grey lobes are occupied; + and - mark the phases that overlap."""

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

GREY = "0.62"
fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.6))


def lobe(ax, xy, w, h, angle=0, filled=False, sign=None):
    ax.add_patch(Ellipse(xy, w, h, angle=angle, facecolor=GREY if filled else "none", edgecolor="k", lw=1.3))
    if sign:
        ax.text(*xy, sign, ha="center", va="center", fontsize=13)


def atoms(ax):
    for x, s in ((0.0, "M"), (2.2, "C"), (3.3, "O")):
        ax.text(x, 0, s, ha="center", va="center", fontsize=15, fontweight="bold",
                bbox=dict(boxstyle="circle,pad=0.15", fc="none", ec="none"))
    for dy in (-0.09, 0.0, 0.09):  # the C-O triple bond
        ax.plot([2.45, 3.05], [dy, dy], color="k", lw=1.2)


# sigma donation: empty d(z2)-like lobes on M, filled sp lobe on C pointing at M
ax = axes[0]
lobe(ax, (0.75, 0), 1.2, 0.55)                 # lobe of the empty d-sigma orbital toward C
lobe(ax, (-0.75, 0), 1.2, 0.55)
ax.add_patch(Ellipse((0, 0), 0.55, 0.32, facecolor="none", edgecolor="k", lw=1.0))
lobe(ax, (1.55, 0), 1.05, 0.6, filled=True)    # 5-sigma lone pair on carbon
atoms(ax)
ax.annotate("", xy=(0.55, 0.62), xytext=(1.6, 0.62), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.6))
ax.text(1.1, 0.95, "sigma donation  C $\\to$ M", ha="center", fontsize=12)
ax.text(1.55, -0.75, "filled 5$\\sigma$", ha="center", fontsize=11)
ax.text(-0.3, -0.75, "empty d$_\\sigma$", ha="center", fontsize=11)

# pi back-donation: filled d(xz)-like clover on M, empty pi* on C and O
ax = axes[1]
for (dx, dy), sign in (((0.5, 0.5), "+"), ((-0.5, -0.5), "+"), ((0.5, -0.5), "\u2212"), ((-0.5, 0.5), "\u2212")):
    lobe(ax, (dx, dy), 0.95, 0.42, angle=45 if dx * dy > 0 else -45, filled=True, sign=sign)
lobe(ax, (2.2, 0.55), 0.48, 1.0, sign="+")      # pi* lobes: larger on carbon, opposite phases on C and O
lobe(ax, (2.2, -0.55), 0.48, 1.0, sign="\u2212")
lobe(ax, (3.3, 0.42), 0.36, 0.72, sign="\u2212")
lobe(ax, (3.3, -0.42), 0.36, 0.72, sign="+")
atoms(ax)
ax.annotate("", xy=(1.85, 1.2), xytext=(0.7, 1.2), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.6))
ax.text(1.3, 1.45, "pi back-donation  M $\\to$ CO", ha="center", fontsize=12)
ax.text(0.0, -1.35, "filled d$_\\pi$", ha="center", fontsize=11)
ax.text(2.75, -1.35, "empty $\\pi^*$", ha="center", fontsize=11)

for ax in axes:
    ax.set_xlim(-1.5, 4.0)
    ax.set_ylim(-1.6, 1.75)
    ax.set_aspect("equal")
    ax.axis("off")
fig.tight_layout()
