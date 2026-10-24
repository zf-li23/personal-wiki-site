"""The two quenching cycles of photoredox catalysis, drawn for Ru(bpy)3(2+) (potentials vs SCE).
Oxidative quenching: the excited catalyst gives an electron to an acceptor A and becomes Ru(III),
which takes an electron back from a donor D. Reductive quenching: the excited catalyst takes an
electron from D and becomes Ru(I), which reduces A. In both cycles the catalyst is regenerated and
the net change is one electron moved from D to A, pumped uphill by the absorbed photon."""

import math

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def node(ax, angle, text, r=1.0, cx=0.0):
    x, y = cx + r * math.cos(math.radians(angle)), r * math.sin(math.radians(angle))
    ax.text(x, y, text, ha="center", va="center", fontsize=11,
            bbox=dict(boxstyle="round,pad=0.25", fc="none", ec="0.5", lw=0.8))
    return x, y


def arc(ax, p, q, color, rad=0.35):
    ax.add_patch(FancyArrowPatch(p, q, connectionstyle=f"arc3,rad={rad}", arrowstyle="-|>",
                                 mutation_scale=14, color=color, lw=1.5, shrinkA=22, shrinkB=22))


def side(ax, a, b, text, color):
    """A small curved arrow for a substrate entering (a) and leaving (b) next to an arc."""
    ax.add_patch(FancyArrowPatch(a, b, connectionstyle="arc3,rad=0.5", arrowstyle="-|>",
                                 mutation_scale=10, color=color, lw=1.0))
    ax.text((a[0] + b[0]) / 2, (a[1] + b[1]) / 2, text, ha="center", va="center", fontsize=9, color=color)


fig, axes = plt.subplots(1, 2, figsize=(10, 4.6))
for ax, kind in zip(axes, ("oxidative", "reductive")):
    top = node(ax, 90, r"Ru$^{2+}$")
    star = node(ax, 210, r"*Ru$^{2+}$")
    other = node(ax, 330, r"Ru$^{3+}$" if kind == "oxidative" else r"Ru$^{+}$")
    arc(ax, top, star, "C1")
    ax.text(-1.5, 0.55, r"$h\nu$" + "\n452 nm", color="C1", fontsize=9, ha="center")
    arc(ax, star, other, "C0")
    arc(ax, other, top, "C2")
    if kind == "oxidative":
        side(ax, (-0.6, -1.2), (0.6, -1.2), "A $\\to$ A$^{\\bullet-}$", "C0")
        side(ax, (1.6, -0.15), (1.3, 1.05), "D $\\to$ D$^{\\bullet+}$", "C2")
        ax.text(0, -0.15, "*Ru$^{2+}$ as reductant\n$E$(Ru$^{3+}$/*Ru$^{2+}$) = −0.81 V", ha="center", fontsize=8)
        ax.set_title("oxidative quenching", fontsize=11)
    else:
        side(ax, (-0.6, -1.2), (0.6, -1.2), "D $\\to$ D$^{\\bullet+}$", "C0")
        side(ax, (1.6, -0.15), (1.3, 1.05), "A $\\to$ A$^{\\bullet-}$", "C2")
        ax.text(0, -0.15, "*Ru$^{2+}$ as oxidant\n$E$(*Ru$^{2+}$/Ru$^{+}$) = +0.77 V", ha="center", fontsize=8)
        ax.set_title("reductive quenching", fontsize=11)
    ax.set_xlim(-2.1, 2.3)
    ax.set_ylim(-1.8, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")
fig.tight_layout()
