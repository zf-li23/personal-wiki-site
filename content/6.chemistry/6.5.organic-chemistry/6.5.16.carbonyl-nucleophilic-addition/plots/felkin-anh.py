"""Newman projections along the bond from the carbonyl carbon (front) to the stereogenic alpha
carbon (back circle). Left, Felkin-Anh model: the large group L is perpendicular to the carbonyl
plane and anti to the incoming nucleophile, which approaches at the Burgi-Dunitz angle past the
small group S. Right, Cram chelation model: a metal binds both the carbonyl oxygen and the alpha
alkoxy group, which locks them eclipsed; the nucleophile again approaches past the smaller group."""

import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch

fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.9))
ink = plt.rcParams["text.color"]


def ray(ax, ang, r0, r1, text=None, pad=0.32):
    t = math.radians(ang)
    u = np.array([math.cos(t), math.sin(t)])
    ax.plot(*zip(r0 * u, r1 * u), color=ink, lw=1.6, solid_capstyle="round")
    if text:
        ax.text(*((r1 + pad) * u), text, ha="center", va="center", fontsize=13, color=ink)


def nucleophile(ax):
    tip = np.array([-0.1, 0.08])
    start = np.array([-1.25, 2.15])
    ax.add_patch(FancyArrowPatch(start, tip, connectionstyle="arc3,rad=-0.15", arrowstyle="-|>", mutation_scale=14,
                                 color=ink, lw=1.4, shrinkB=2))
    ax.text(-1.45, 2.42, r"Nu$^-$", ha="center", va="center", fontsize=13, color=ink)


for ax, title, back in (
    (axes[0], "Felkin-Anh", [(-90, "L"), (30, "M"), (150, "S")]),
    (axes[1], "Cram chelate", [(-22, "OR"), (98, "S"), (218, "L")]),
):
    ax.add_patch(Circle((0, 0), 0.75, fill=False, color=ink, lw=1.6))
    for ang, text in back:
        ray(ax, ang, 0.75, 1.55, text)
    # front carbonyl carbon: C=O to the right, R to the left (the carbonyl plane is horizontal)
    for o in (-0.06, 0.06):
        ax.plot([0, 1.25], [o, o], color=ink, lw=1.6)
    ax.text(1.48, 0.0, "O", ha="center", va="center", fontsize=13, color=ink)
    ax.plot([0, -1.25], [0, 0], color=ink, lw=1.6)
    ax.text(-1.5, 0.0, "R", ha="center", va="center", fontsize=13, color=ink)
    nucleophile(ax)
    ax.text(0, -2.35, title, ha="center", va="center", fontsize=12, color=ink)
    ax.set_xlim(-2.3, 2.6)
    ax.set_ylim(-2.6, 2.7)
    ax.set_aspect("equal")
    ax.axis("off")

# the chelating metal bridges the carbonyl oxygen and the alkoxy oxygen
ax = axes[1]
ax.text(2.35, -0.35, r"M$^{n+}$", ha="center", va="center", fontsize=12, color=ink)
ax.plot([1.68, 2.05], [-0.05, -0.22], color=ink, lw=1.1, ls=(0, (2, 2)))
ax.plot([2.05, 2.15], [-0.6, -0.52], color=ink, lw=1.1, ls=(0, (2, 2)))
fig.subplots_adjust(0, 0, 1, 1, wspace=0.05)
