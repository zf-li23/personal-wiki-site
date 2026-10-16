"""Cauchy's theorem on a region with two holes: cuts turn the boundary into one closed curve."""

import numpy as np
import matplotlib.pyplot as plt

s = np.linspace(0, 2 * np.pi, 400)
outer = np.c_[2.7 * np.cos(s), 1.8 * np.sin(s)]
c1, r1 = np.array([-1.1, 0.0]), 0.5
c2, r2 = np.array([1.1, 0.1]), 0.45
holes = [np.c_[c1[0] + r1 * np.cos(s), c1[1] + r1 * np.sin(s)],
         np.c_[c2[0] + r2 * np.cos(s), c2[1] + r2 * np.sin(s)]]

fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.6))


def arrows(ax, curve, reverse, color, label=None):
    c = curve[::-1] if reverse else curve
    ax.plot(c[:, 0], c[:, 1], color=color, lw=2, label=label)
    n = len(c)
    for k in range(n // 8, n - 1, n // 3):
        ax.annotate("", xy=c[k + 4], xytext=c[k],
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=2, mutation_scale=18))


for ax in (a1, a2):
    ax.fill(outer[:, 0], outer[:, 1], color="C2", alpha=0.2, lw=0)
    for h in holes:
        ax.fill(h[:, 0], h[:, 1], color=fig.get_facecolor(), lw=0)
        ax.plot(h[:, 0], h[:, 1], color="0.5", lw=0.6)
    ax.set_aspect("equal")
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2.1, 2.1)
    ax.set_xticks([])
    ax.set_yticks([])

arrows(a1, outer, False, "C0", "C0 counterclockwise")
arrows(a1, holes[0], True, "C3", "C1, C2 clockwise")
arrows(a1, holes[1], True, "C3")
a1.text(c1[0], c1[1], "C1", ha="center", va="center")
a1.text(c2[0], c2[1], "C2", ha="center", va="center")
a1.text(0, 1.3, "D", fontsize=15, ha="center")
a1.legend(loc="lower center", fontsize=8, ncol=2)
a1.set_title("boundary of D, positively oriented")

# cuts from the outer curve to the holes and between the holes
cuts = [([-2.7, c1[0] - r1], [0.0, 0.0]), ([c1[0] + r1, c2[0] - r2], [0.0, 0.08]), ([c2[0] + r2, 2.7], [0.1, 0.0])]
for xs, ys in cuts:
    a2.plot(xs, ys, color="C1", lw=2)
    a2.annotate("", xy=(np.mean(xs) + 0.12, np.mean(ys) + 0.06), xytext=(np.mean(xs) - 0.12, np.mean(ys) + 0.06),
                arrowprops=dict(arrowstyle="-|>", color="C1", lw=1.5))
    a2.annotate("", xy=(np.mean(xs) - 0.12, np.mean(ys) - 0.06), xytext=(np.mean(xs) + 0.12, np.mean(ys) - 0.06),
                arrowprops=dict(arrowstyle="-|>", color="C1", lw=1.5))
a2.plot(outer[:, 0], outer[:, 1], color="C0", lw=2)
for h in holes:
    a2.plot(h[:, 0], h[:, 1], color="C3", lw=2)
a2.text(0, 1.0, "upper part", ha="center")
a2.text(0, -1.0, "lower part", ha="center")
a2.set_title("cuts: each is traversed twice in opposite directions")
fig.tight_layout()
