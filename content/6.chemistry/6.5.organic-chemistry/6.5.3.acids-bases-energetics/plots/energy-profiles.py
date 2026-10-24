"""Free-energy profiles. Left: a one-step exergonic reaction; the activation free energy decides the
rate, the reaction free energy the position of equilibrium. Right: a two-step reaction through an
intermediate (a local minimum); the first transition state is the highest point, so the first step
is rate-determining. Transition states are maxima along the reaction coordinate, intermediates are
minima."""

import numpy as np
import matplotlib.pyplot as plt


def profile(levels):
    """Smooth curve through alternating minima and maxima (zero slope at each stationary point)."""
    xs, ys = [], []
    for k in range(len(levels) - 1):
        t = np.linspace(0, 1, 60)
        xs.append(k + t)
        ys.append(levels[k] + (levels[k + 1] - levels[k]) * (1 - np.cos(np.pi * t)) / 2)
    return np.concatenate(xs), np.concatenate(ys)


ink = plt.rcParams["text.color"]
fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.2), sharey=True)


def gap(ax, x, y0, y1, text, side="right"):
    ax.annotate("", xy=(x, y1), xytext=(x, y0), arrowprops=dict(arrowstyle="<->", color=ink, lw=1))
    ax.text(x + (0.06 if side == "right" else -0.06), (y0 + y1) / 2, text, ha="left" if side == "right" else "right", va="center", fontsize=11)


# One step: R -> TS -> P
lv = [0, 80, -30]
x, y = profile(lv)
a.plot(x, y, color="#2563eb", lw=2)
a.plot([-0.25, 0.35], [0, 0], color=ink, lw=0.8, ls=":")
gap(a, 1.0, 0, 80, r"$\Delta^{\ddagger}G^\circ$")
gap(a, 2.05, 0, -30, r"$\Delta_{\mathrm{r}}G^\circ$")
a.plot([0.35, 2.25], [0, 0], color=ink, lw=0.8, ls=":")
a.text(1, 86, "transition state", ha="center", fontsize=10)
a.text(0, -9, "reactants", ha="center", fontsize=10)
a.text(2, -39, "products", ha="center", fontsize=10)
a.set_title("one step", fontsize=11)

# Two steps: R -> TS1 -> I -> TS2 -> P
lv = [0, 85, 40, 65, -35]
x, y = profile(lv)
b.plot(x, y, color="#2563eb", lw=2)
b.text(1, 91, r"TS$_1$", ha="center", fontsize=10)
b.text(3, 71, r"TS$_2$", ha="center", fontsize=10)
b.text(2, 30, "intermediate", ha="center", fontsize=10)
b.text(0, -9, "reactants", ha="center", fontsize=10)
b.text(4, -44, "products", ha="center", fontsize=10)
b.plot([-0.25, 1.3], [0, 0], color=ink, lw=0.8, ls=":")
gap(b, 1.0, 0, 85, r"$\Delta^{\ddagger}G^\circ_1$")
b.plot([2.0, 3.3], [40, 40], color=ink, lw=0.8, ls=":")
gap(b, 3.0, 40, 65, r"$\Delta^{\ddagger}G^\circ_2$")
b.set_title("two steps: step 1 is rate-determining", fontsize=11)

for ax in (a, b):
    ax.set_xlabel("reaction coordinate")
    ax.set_xticks([])
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
a.set_ylabel(r"$G$ / kJ mol$^{-1}$ (relative)")
a.set_ylim(-50, 100)
fig.tight_layout()
